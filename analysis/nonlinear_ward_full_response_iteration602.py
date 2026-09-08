#!/usr/bin/env python3
"""Iteration 602: rerun the frozen full nonlinear Ward gate with only the
Iter601 endpoint matrix realization corrected.

No physics, fixture, thresholds, family content, Fourier convention or route is
changed from Iter596/599.  The sole change is the left scalar endpoint operator:
  R_rc = xi.p_c, L_rc = -xi.p_r for p_r=p_c+q,
and covariance Delta G - R G - G L = 0.
"""
from __future__ import annotations
import hashlib,json
from pathlib import Path
import numpy as np
import nonlinear_ward_full_response_iteration597 as base
import source_endpoint_covariance_matrix_iteration601 as ep

ITERATION=602
ROOT=Path(__file__).resolve().parents[1]
LEGS=base.LEGS; XI_BASIS=base.XI_BASIS; FD_STEPS=base.FD_STEPS
ANCHOR_TOL=base.ANCHOR_TOL; ASSEMBLY_MATCH_TOL=base.ASSEMBLY_MATCH_TOL
WARD_ABS_TOL=base.WARD_ABS_TOL; WARD_STEP_TOL=base.WARD_STEP_TOL


def symmetric_route(qg):
    q=np.asarray(qg,float); return -0.5*q,+0.5*q


def covariance_G(eu,ev,g,u,v,xi,p0,hs,qs):
    inds,pos,ps=base.lattice(p0,qs); modes=base.needed_modes(inds)
    A,B,dA,dB=base.metric_and_variation_grids(eu,ev,g,u,v,xi,hs,qs)
    Ac={m:base.coeff_from_grid(A,m) for m in modes}; Bc={m:base.coeff_from_grid(B,m) for m in modes}
    dAc={m:base.coeff_from_grid(dA,m) for m in modes}; dBc={m:base.coeff_from_grid(dB,m) for m in modes}
    K=base.build_K_from_coeffs(Ac,Bc,inds,ps); dK=base.build_K_from_coeffs(dAc,dBc,inds,ps)
    G=np.linalg.inv(K); dG=-G@dK@G
    R,L=ep.build_endpoint_generators(g,xi,inds,pos,ps)
    C=dG-R@G-G@L
    return C,inds,pos,G,K,dK


def main():
    failures=[]
    r601=json.loads((ROOT/'results'/'iteration601_endpoint_covariance_matrix'/'result.json').read_text())
    if r601.get('classification')!='PASS_SCALAR_ENDPOINT_COVARIANCE_MATRIX_REALIZATION_REPRODUCES_ITER587_ANCHOR__NON_RESIDUAL':
        raise SystemExit('Iter601 authority missing')
    contract=json.loads((ROOT/'candidate_gravity'/'results'/'iteration596_nonlinear_ward_contract.json').read_text())
    if contract.get('classification')!='PASS_PROSPECTIVE_FULL_NONLINEAR_WARD_CONTRACT_FREEZE_AND_ONE_LEG_REDUCTION__NON_RESIDUAL' or contract.get('failures')!=[]:
        raise SystemExit('Iter596 contract not PASS')
    r594=json.loads((ROOT/'candidate_gravity'/'results'/'iteration594_full_cubic_routed_assembly.json').read_text())
    if r594.get('classification')!='PASS_FULL_SAME_ACTION_ROUTED_CUBIC_SOURCE_ASSEMBLY_AND_PERMUTATION_SYMMETRY__NON_WARD_NON_RESIDUAL' or r594.get('failures')!=[]:
        raise SystemExit('Iter594 authority not PASS')
    qs,hs=base.inherit_fixture()
    closure=float(np.max(np.abs(sum((qs[x] for x in LEGS),np.zeros(4)))))
    if closure>1e-14: failures.append(f'fixture closure {closure}')

    anchors=[]
    for g in LEGS:
        p0,pprime=symmetric_route(qs[g]); u,v=tuple(x for x in LEGS if x!=g)
        for ix,xi in enumerate(XI_BASIS):
            C,inds,pos,*_=covariance_G(0.0,0.0,g,u,v,xi,p0,hs,qs)
            sh=base.MODE[g]; c=(0,0); r=(sh[0],sh[1]); val=C[pos[r],pos[c]]
            ab=float(abs(val)); anchors.append({'gauge_leg':g,'xi_basis':ix,'abs':ab})
            if ab>ANCHOR_TOL: failures.append(f'Iter601-corrected anchor {g}/xi{ix}={ab}')

    assembly=[]
    for ip,p0 in enumerate(base.PROBES):
        vals=[base.cubic_G_coeff(p0,hs,qs,h) for h in FD_STEPS]
        target=float(r594['probe_results'][ip]['canonical_assembly']['full_dabcG'])
        match=abs(vals[-1].real-target); imag=abs(vals[-1].imag); step=abs(vals[-1]-vals[-2])
        assembly.append({'p0':p0.tolist(),'last_match_abs':float(match),'last_imag_abs':float(imag),'last_step_abs':float(step)})
        if match>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 crosscheck mismatch probe {ip}: {match}')
        if imag>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 crosscheck imaginary probe {ip}: {imag}')
        if step>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 crosscheck convergence probe {ip}: {step}')

    ward=[]; max_abs=0.; max_step=0.
    for g in LEGS:
        p0,pprime=symmetric_route(qs[g]); inds,pos,_=base.lattice(p0,qs); c=pos[(0,0)]
        u,v=tuple(x for x in LEGS if x!=g)
        for ix,xi in enumerate(XI_BASIS):
            vals=[]
            for h in FD_STEPS:
                def f(eu,ev):
                    C,*_=covariance_G(eu,ev,g,u,v,xi,p0,hs,qs)
                    return C[c,c]
                vals.append(base.mixed2(f,h))
            last=vals[-1]; step=abs(vals[-1]-vals[-2]); ab=abs(last)
            max_abs=max(max_abs,float(ab)); max_step=max(max_step,float(step))
            ward.append({'gauge_leg':g,'spectators':[u,v],'xi_basis':ix,
                         'ward_values_real':[float(z.real) for z in vals],
                         'ward_values_imag':[float(z.imag) for z in vals],
                         'last_abs':float(ab),'last_step_abs':float(step)})
            if ab>WARD_ABS_TOL: failures.append(f'full endpoint-corrected Ward residual {g}/xi{ix}={ab}')
            if step>WARD_STEP_TOL: failures.append(f'full endpoint-corrected Ward convergence {g}/xi{ix}={step}')

    ok=not failures
    result={
      'iteration':602,'date':'2026-09-08','model_readiness_percent':24,
      'classification':('PASS_FULL_SOURCE_LEVEL_NONLINEAR_WARD_WITH_ITER601_ENDPOINT_REALIZATION__NON_RESIDUAL' if ok else
                        'FAIL_FULL_SOURCE_LEVEL_NONLINEAR_WARD_WITH_ITER601_ENDPOINT_REALIZATION__PRESERVED_NEGATIVE_RESULT'),
      'scientific_gate_pass':ok,'failures':failures,
      'sole_change_from_iter599':'left endpoint matrix realization replaced by Iter601 R/L; all frozen science unchanged',
      'identity':'Delta G - R G - G L = 0; mixed spectator coefficient on exact Iter588 fixture',
      'full_family_content':'K3 + six K1/K2 + six ordered K1^3 from same inverse kernel',
      'five_mandatory_classes':['gauge-leg linear contraction','spectator-u Lie derivative','spectator-v Lie derivative','left scalar/source endpoint','right scalar/source endpoint'],
      'thresholds':{'anchor_abs':ANCHOR_TOL,'assembly_match_abs':ASSEMBLY_MATCH_TOL,'ward_abs':WARD_ABS_TOL,'ward_last_step':WARD_STEP_TOL,'fd_steps':list(FD_STEPS)},
      'anchors':anchors,'iter594_crosscheck':assembly,'ward_rows':ward,
      'observed':{'max_full_ward_abs':max_abs,'max_full_ward_last_step':max_step,'fixture_closure':closure},
      'source_born_subtraction':'NOT_PERFORMED','source_to_iter582_map':'NOT_PERFORMED','candidate_residual':False,
      'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'raw-consume; then freeze full-observable source-to-Iter582/native-linked map and classify pole/cut origin before fixed comparator quotient',
      'next_gate_if_fail':'preserve scientific negative result and localize remaining spectator/gauge/source component without threshold or family changes'
    }
    out=ROOT/'results'/'iteration602_full_nonlinear_ward_endpoint_corrected'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':602,'result_sha256':sha,'failures':failures,
           'classification':('PASS_RAW_AUTHORITY_AUDIT_ITER602_FULL_WARD' if ok else 'FAIL_RAW_AUTHORITY_AUDIT_ITER602_FULL_WARD')}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
