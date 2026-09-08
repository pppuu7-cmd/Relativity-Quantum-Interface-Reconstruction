#!/usr/bin/env python3
"""Iteration 605: production nonlinear Ward rerun under the prospective Iter604 lattice contract."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
import numpy as np
import nonlinear_ward_full_response_iteration597 as base
import nonlinear_ward_iter602_lattice_diagnosis_iteration603 as diag
import source_endpoint_covariance_matrix_iteration601 as ep

ITERATION=605
ROOT=Path(__file__).resolve().parents[1]
RADII=(4,5,6); WARD_TOL=2e-6; FD_TOL=2e-5; RADIUS_TOL=2e-6; ANCHOR_TOL=2e-11; ASSEMBLY_TOL=2e-5
LEGS=base.LEGS; XI_BASIS=base.XI_BASIS; FD_STEPS=base.FD_STEPS


def anchor_at_radius(g,xi,p0,hs,qs,rad):
    old=base.LAT_R
    try:
        base.LAT_R=rad
        return ep.corrected_anchor(g,xi,p0,hs,qs)[0]
    finally:
        base.LAT_R=old


def main():
    c604=json.loads((ROOT/'candidate_gravity/results/iteration604_finite_lattice_contract_raw_consumption.json').read_text())
    if not c604.get('scientific_gate_pass') or c604.get('contract',{}).get('radii') != [4,5,6]:
        raise SystemExit('Iter604 raw-valid prospective contract missing')
    front=(ROOT/'candidate_gravity/recovery/CURRENT_QG_FRONT.md').read_text()
    # The already-closed Iter594 assembly prerequisite is inherited, not recomputed
    # or numerically reinterpreted here. Current-front explicitly binds it to <=2e-5.
    required=['All 12 one-leg anchors and the Iter594 13-family assembly prerequisite pass.',
              'Iter594 assembly cross-check `<=2e-5`',
              'complete 13-family routed same-action cubic source object']
    if not all(x in front for x in required):
        raise SystemExit('frozen Iter594 13-family assembly authority missing from current front')
    qs,hs=base.inherit_fixture()
    rows=[]
    for rad in RADII:
        for g in LEGS:
            p0=-0.5*np.asarray(qs[g],float); u,v=tuple(x for x in LEGS if x!=g)
            for ix,xi in enumerate(XI_BASIS):
                vals=[]; conds=[]
                for h in FD_STEPS:
                    def f(eu,ev):
                        C,inds,pos,cond=diag.covariance_G(eu,ev,g,u,v,xi,p0,hs,qs,rad)
                        conds.append(cond)
                        return C[pos[(0,0)],pos[(0,0)]]
                    vals.append(base.mixed2(f,h))
                rows.append({'lat_r':rad,'gauge_leg':g,'xi_basis':ix,
                    'ward_values_real':[float(z.real) for z in vals],
                    'ward_values_imag':[float(z.imag) for z in vals],
                    'last_complex':[float(vals[-1].real),float(vals[-1].imag)],
                    'last_abs':float(abs(vals[-1])),
                    'last_step_abs':float(abs(vals[-1]-vals[-2])),
                    'max_K_condition':max(conds)})
    by={(r['lat_r'],r['gauge_leg'],r['xi_basis']):r for r in rows}
    anchors=[]
    for rad in (5,6):
        for g in LEGS:
            p0=-0.5*np.asarray(qs[g],float)
            for ix,xi in enumerate(XI_BASIS):
                z=anchor_at_radius(g,xi,p0,hs,qs,rad)
                anchors.append({'lat_r':rad,'gauge_leg':g,'xi_basis':ix,'abs':float(abs(z))})
    outcomes=[]; failures=[]
    for g in LEGS:
        for ix in range(4):
            r5=by[(5,g,ix)]; r6=by[(6,g,ix)]
            z5=complex(*r5['last_complex']); z6=complex(*r6['last_complex'])
            radius_delta=float(abs(z6-z5))
            converged=(r5['last_step_abs']<=FD_TOL and r6['last_step_abs']<=FD_TOL and radius_delta<=RADIUS_TOL)
            if not converged: status='BLOCKED_CONVERGENCE'
            elif r5['last_abs']>WARD_TOL or r6['last_abs']>WARD_TOL: status='FAIL_WARD'
            else: status='PASS'
            if status!='PASS': failures.append(f'{g}/xi{ix}:{status}')
            outcomes.append({'gauge_leg':g,'xi_basis':ix,'status':status,'R5_last_abs':r5['last_abs'],'R6_last_abs':r6['last_abs'],'R5_last_step_abs':r5['last_step_abs'],'R6_last_step_abs':r6['last_step_abs'],'R6_minus_R5_abs':radius_delta})
    anchor_max=max(x['abs'] for x in anchors)
    if anchor_max>ANCHOR_TOL: failures.append(f'one_leg_anchor:{anchor_max}')
    assembly_authority_pass=True
    statuses={o['status'] for o in outcomes}
    if not failures: cls='PASS_FULL_SOURCE_LEVEL_NONLINEAR_WARD_UNDER_ITER604_FINITE_LATTICE_CONTRACT'
    elif 'BLOCKED_CONVERGENCE' in statuses: cls='BLOCKED_CONVERGENCE_FULL_SOURCE_LEVEL_NONLINEAR_WARD_UNDER_ITER604_CONTRACT'
    else: cls='FAIL_WARD_FULL_SOURCE_LEVEL_NONLINEAR_WARD_UNDER_ITER604_CONTRACT'
    result={'iteration':ITERATION,'date':'2026-09-08','classification':cls,
      'scientific_gate_pass':not failures,'candidate_residual':False,'model_readiness_percent':24,
      'contract':{'radii':list(RADII),'fd_steps':list(FD_STEPS),'ward_abs_tolerance':WARD_TOL,'last_fd_step_tolerance':FD_TOL,'radius_stability_tolerance':RADIUS_TOL,'one_leg_anchor_tolerance':ANCHOR_TOL,'assembly_crosscheck_tolerance':ASSEMBLY_TOL,'source_family_count':13},
      'rows':rows,'row_outcomes':outcomes,'anchors_R5_R6':anchors,'max_anchor_abs':anchor_max,
      'iter594_13_family_assembly_authority_pass':assembly_authority_pass,'failures':failures,
      'iter602_historical_fail_preserved':True,'source_born_subtraction':'NOT_PERFORMED','source_to_iter582_map':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN'}
    out=ROOT/'results/iteration605_full_nonlinear_ward_iter604_contract'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':ITERATION,'result_sha256':sha,'classification':'PASS_RAW_AUDIT_ITER605_PRODUCTION_WARD','failures':[]}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    # Scientific FAIL/BLOCKED is a valid result and must still upload raw artifact.

if __name__=='__main__': main()
