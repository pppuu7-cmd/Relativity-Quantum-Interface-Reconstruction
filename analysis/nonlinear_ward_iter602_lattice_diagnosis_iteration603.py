#!/usr/bin/env python3
"""Iteration 603: non-promoting diagnosis of the three nonconvergent Iter602 s-leg rows.

Iter602 is preserved exactly as a negative frozen-gate result.  This diagnostic
must NOT promote it.  It asks whether the failure is stable under enlarging only
the finite Fourier momentum lattice used to realize the already-frozen continuum
Ward identity.  No source family, fixture, endpoint rule, FD step, Ward tolerance,
q2 grouping, or physical normalization changes.

We evaluate all 12 Ward rows at LAT_R=3,4,5 with the exact same FD steps
(2e-2,1e-2,5e-3).  If the problematic s/xi0..2 rows collapse rapidly with radius
while the already-small a/b and s/xi3 rows remain small, classify the Iter602
failure as finite-lattice realization sensitivity (diagnostic only).  If they are
stable, classify as radius-stable negative Ward evidence.  Either outcome remains
NON_PROMOTING until a new prospective production contract is separately frozen.
"""
from __future__ import annotations
import contextlib, hashlib, json
from pathlib import Path
import numpy as np
import nonlinear_ward_full_response_iteration597 as base
import source_endpoint_covariance_matrix_iteration601 as ep

ITERATION=603
ROOT=Path(__file__).resolve().parents[1]
LEGS=base.LEGS; XI_BASIS=base.XI_BASIS; FD_STEPS=base.FD_STEPS
RADII=(3,4,5)


def covariance_G(eu,ev,g,u,v,xi,p0,hs,qs,lat_r):
    old=base.LAT_R
    try:
        base.LAT_R=lat_r
        inds,pos,ps=base.lattice(p0,qs); modes=base.needed_modes(inds)
        A,B,dA,dB=base.metric_and_variation_grids(eu,ev,g,u,v,xi,hs,qs)
        Ac={m:base.coeff_from_grid(A,m) for m in modes}; Bc={m:base.coeff_from_grid(B,m) for m in modes}
        dAc={m:base.coeff_from_grid(dA,m) for m in modes}; dBc={m:base.coeff_from_grid(dB,m) for m in modes}
        K=base.build_K_from_coeffs(Ac,Bc,inds,ps); dK=base.build_K_from_coeffs(dAc,dBc,inds,ps)
        cond=float(np.linalg.cond(K))
        G=np.linalg.inv(K); dG=-G@dK@G
        R,L=ep.build_endpoint_generators(g,xi,inds,pos,ps)
        C=dG-R@G-G@L
        return C,inds,pos,cond
    finally:
        base.LAT_R=old


def main():
    raw602=ROOT/'results'/'iteration602_full_nonlinear_ward_endpoint_corrected'/'result.json'
    # In Actions this may not be committed yet. The diagnosis is allowed from the
    # frozen Iter602 code/contract, but if a committed result exists ensure it is FAIL.
    if raw602.exists():
        r602=json.loads(raw602.read_text())
        if not str(r602.get('classification','')).startswith('FAIL_FULL_SOURCE_LEVEL_NONLINEAR_WARD_WITH_ITER601'):
            raise SystemExit('Iter602 committed state not the expected negative result')
    r601=json.loads((ROOT/'results'/'iteration601_endpoint_covariance_matrix'/'result.json').read_text())
    if not r601.get('scientific_gate_pass'): raise SystemExit('Iter601 authority missing')
    qs,hs=base.inherit_fixture()
    rows=[]
    for rad in RADII:
        for g in LEGS:
            p0=-0.5*np.asarray(qs[g],float); u,v=tuple(x for x in LEGS if x!=g)
            # central matrix element index depends on radius, so resolve per evaluation.
            for ix,xi in enumerate(XI_BASIS):
                vals=[]; conds=[]
                for h in FD_STEPS:
                    def f(eu,ev):
                        C,inds,pos,cond=covariance_G(eu,ev,g,u,v,xi,p0,hs,qs,rad)
                        conds.append(cond)
                        return C[pos[(0,0)],pos[(0,0)]]
                    vals.append(base.mixed2(f,h))
                rows.append({'lat_r':rad,'gauge_leg':g,'xi_basis':ix,
                             'ward_values_real':[float(z.real) for z in vals],
                             'ward_values_imag':[float(z.imag) for z in vals],
                             'last_abs':float(abs(vals[-1])),
                             'last_step_abs':float(abs(vals[-1]-vals[-2])),
                             'max_K_condition':max(conds)})
    by={(r['lat_r'],r['gauge_leg'],r['xi_basis']):r for r in rows}
    ratios={}
    for ix in (0,1,2):
        v3=by[(3,'s',ix)]['last_abs']; v5=by[(5,'s',ix)]['last_abs']
        ratios[f's_xi{ix}_R3_over_R5']=float(v3/max(v5,1e-300))
    s_problem_decreases=all(by[(5,'s',ix)]['last_abs'] < by[(3,'s',ix)]['last_abs']/10 for ix in (0,1,2))
    stable_small=max(r['last_abs'] for r in rows if r['lat_r']==5 and not (r['gauge_leg']=='s' and r['xi_basis'] in (0,1,2)))
    if s_problem_decreases:
        cls='DIAGNOSTIC_ITER602_S_ROWS_STRONGLY_LATTICE_RADIUS_SENSITIVE__NON_PROMOTING'
    else:
        cls='DIAGNOSTIC_ITER602_S_ROWS_NOT_STRONGLY_RESCUED_BY_LATTICE_RADIUS__NON_PROMOTING'
    result={'iteration':603,'date':'2026-09-08','model_readiness_percent':24,
            'classification':cls,'scientific_gate_pass':False,'candidate_residual':False,
            'scope':'DIAGNOSTIC_ONLY__ITER602_FROZEN_FAIL_PRESERVED',
            'radii':list(RADII),'fd_steps':list(FD_STEPS),'rows':rows,'radius_ratios':ratios,
            'R5_max_other_row_abs':float(stable_small),
            'guardrails':['NO_PROMOTION_FROM_RADIUS_DIAGNOSTIC','NO_THRESHOLD_CHANGE','NO_FAMILY_CHANGE','NO_FIXTURE_CHANGE','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
            'next_gate':'If strong lattice sensitivity is demonstrated, derive a prospective boundary-closure/convergence contract before any rerun. Otherwise localize the s-leg spectator/gauge algebra analytically under the existing continuum contract.'}
    out=ROOT/'results'/'iteration603_iter602_lattice_diagnosis'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    (out/'authority_audit.json').write_text(json.dumps({'iteration':603,'result_sha256':sha,'classification':'PASS_DIAGNOSTIC_RAW_AUDIT_ITER603','failures':[]},indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__': main()
