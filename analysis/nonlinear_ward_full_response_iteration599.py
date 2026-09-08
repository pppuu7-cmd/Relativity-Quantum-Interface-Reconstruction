#!/usr/bin/env python3
"""Iteration 599: corrected full nonlinear Ward evaluator for frozen Iter596 route.

This is a prospective repair of Iter597 after Iter598 proved that Iter597 evaluated
arbitrary scalar PROBES instead of the mandatory gauge-attached symmetric scalar
route.  No scientific threshold, family content, Fourier convention, fixture,
normalization, or transformation rule is changed.

For every cyclic gauge leg g the scalar route is constructed BEFORE evaluation as
    p = -q_g/2,   p' = +q_g/2.
The complete same-parent covariance identity retains the gauge-leg variation, both
spectator Lie derivatives and both scalar endpoint transformations.  The underlying
inverse-kernel derivative therefore still contains K3 + six K1/K2 placements + six
ordered K1^3 chains.

The inherited Iter594 PROBES are used only for the explicitly non-Ward 13-family
assembly implementation cross-check; they never enter the Ward anchor or Ward rows.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import numpy as np
import nonlinear_ward_full_response_iteration597 as base

ITERATION=599
ROOT=Path(__file__).resolve().parents[1]
LEGS=base.LEGS
XI_BASIS=base.XI_BASIS
FD_STEPS=base.FD_STEPS
ANCHOR_TOL=base.ANCHOR_TOL
ASSEMBLY_MATCH_TOL=base.ASSEMBLY_MATCH_TOL
WARD_ABS_TOL=base.WARD_ABS_TOL
WARD_STEP_TOL=base.WARD_STEP_TOL


def symmetric_route(qg):
    p=-0.5*np.asarray(qg,float)
    pp=+0.5*np.asarray(qg,float)
    return p,pp


def main():
    failures=[]
    contract=json.loads((ROOT/'candidate_gravity'/'results'/'iteration596_nonlinear_ward_contract.json').read_text())
    if contract.get('classification')!='PASS_PROSPECTIVE_FULL_NONLINEAR_WARD_CONTRACT_FREEZE_AND_ONE_LEG_REDUCTION__NON_RESIDUAL' or contract.get('failures')!=[]:
        raise SystemExit('Iter596 committed contract authority not PASS')
    r594=json.loads((ROOT/'candidate_gravity'/'results'/'iteration594_full_cubic_routed_assembly.json').read_text())
    if r594.get('classification')!='PASS_FULL_SAME_ACTION_ROUTED_CUBIC_SOURCE_ASSEMBLY_AND_PERMUTATION_SYMMETRY__NON_WARD_NON_RESIDUAL' or r594.get('failures')!=[]:
        raise SystemExit('Iter594 authority not PASS')
    qs,hs=base.inherit_fixture()
    closure=float(np.max(np.abs(sum((qs[x] for x in LEGS),np.zeros(4)))))
    if closure>1e-14: failures.append(f'fixture closure {closure}')

    # Mandatory one-leg reduction on the EXACT per-gauge Iter596/587 symmetric route.
    anchors=[]
    for g in LEGS:
        p0,pprime=symmetric_route(qs[g])
        route_err=float(np.max(np.abs((pprime-p0)-qs[g])))
        midpoint_err=float(np.max(np.abs(pprime+p0)))
        if route_err>1e-14 or midpoint_err>1e-14:
            failures.append(f'symmetric route construction {g}: route={route_err}, midpoint={midpoint_err}')
        u,v=tuple(x for x in LEGS if x!=g)
        for ix,xi in enumerate(XI_BASIS):
            C,inds,pos,*_=base.covariance_G(0.0,0.0,g,u,v,xi,p0,hs,qs)
            sh=base.MODE[g]; c=(0,0); r=(sh[0],sh[1])
            if r not in pos: raise RuntimeError('lattice too small for anchor')
            val=C[pos[r],pos[c]]
            err=abs(val)
            anchors.append({'route':'p=-q_g/2,pprime=+q_g/2','p':p0.tolist(),'pprime':pprime.tolist(),
                            'gauge_leg':g,'xi_basis':ix,'abs_covariance_residual':float(err),
                            'route_error':route_err,'midpoint_error':midpoint_err})
            if err>ANCHOR_TOL: failures.append(f'corrected one-leg covariance anchor {g}/xi{ix} = {err}')

    # Iter594 implementation cross-check remains on inherited PROBES ONLY; it is not a Ward route.
    assembly=[]
    for ip,p0 in enumerate(base.PROBES):
        vals=[base.cubic_G_coeff(p0,hs,qs,h) for h in FD_STEPS]
        target=float(r594['probe_results'][ip]['canonical_assembly']['full_dabcG'])
        match=abs(vals[-1].real-target); imag=abs(vals[-1].imag); step=abs(vals[-1]-vals[-2])
        assembly.append({'scope':'NON_WARD_IMPLEMENTATION_CROSSCHECK_ONLY','p0':p0.tolist(),
                         'fd_steps':list(FD_STEPS),'matrix_cubic_values_real':[float(z.real) for z in vals],
                         'matrix_cubic_values_imag':[float(z.imag) for z in vals],'iter594_target':target,
                         'last_match_abs':float(match),'last_imag_abs':float(imag),'last_step_abs':float(step)})
        if match>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 cubic assembly cross-check mismatch probe {ip}: {match}')
        if imag>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 cubic assembly cross-check imaginary probe {ip}: {imag}')
        if step>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 cubic assembly cross-check convergence probe {ip}: {step}')

    # Full nonlinear Ward rows: one and only one scalar route per gauge singleton, fixed by Iter596.
    ward=[]; max_abs=0.; max_step=0.
    for g in LEGS:
        p0,pprime=symmetric_route(qs[g])
        inds,pos,_=base.lattice(p0,qs); c=pos[(0,0)]
        u,v=tuple(x for x in LEGS if x!=g)
        for ix,xi in enumerate(XI_BASIS):
            vals=[]
            for h in FD_STEPS:
                def f(eu,ev):
                    C,*_=base.covariance_G(eu,ev,g,u,v,xi,p0,hs,qs)
                    return C[c,c]
                vals.append(base.mixed2(f,h))
            last=vals[-1]; step=abs(vals[-1]-vals[-2]); ab=abs(last)
            max_abs=max(max_abs,float(ab)); max_step=max(max_step,float(step))
            ward.append({'route':'p=-q_g/2,pprime=+q_g/2','p':p0.tolist(),'pprime':pprime.tolist(),
                         'gauge_leg':g,'spectators':[u,v],'xi_basis':ix,
                         'fd_steps':list(FD_STEPS),'ward_values_real':[float(z.real) for z in vals],
                         'ward_values_imag':[float(z.imag) for z in vals],
                         'last_abs':float(ab),'last_step_abs':float(step)})
            if ab>WARD_ABS_TOL: failures.append(f'full corrected nonlinear Ward residual {g}/xi{ix} = {ab}')
            if step>WARD_STEP_TOL: failures.append(f'full corrected nonlinear Ward convergence {g}/xi{ix} = {step}')

    scientific_pass=not failures
    result={
      'iteration':ITERATION,'date':'2026-09-08','model_readiness_percent':24,
      'classification':('PASS_FULL_SOURCE_LEVEL_NONLINEAR_WARD_ON_EXACT_FROZEN_ITER596_SYMMETRIC_ROUTE__NON_RESIDUAL'
                        if scientific_pass else
                        'FAIL_FULL_SOURCE_LEVEL_NONLINEAR_WARD_ON_EXACT_FROZEN_ITER596_SYMMETRIC_ROUTE__PRESERVED_NEGATIVE_RESULT'),
      'scientific_gate_pass':scientific_pass,'failures':failures,
      'scope':'FULL_SAME_PARENT_CUBIC_GREEN_FUNCTION_WARD__EXACT_PER_GAUGE_SYMMETRIC_ROUTE__NO_COMPARATOR_SUBTRACTION',
      'route_contract':'for each gauge singleton g: p=-q_g/2, pprime=+q_g/2; no arbitrary PROBES in anchor or Ward rows',
      'identity':'Delta G - T G - G T^T = 0; mixed spectator coefficient with exact Iter588 q_s+q_a+q_b=0',
      'full_family_content':'same parent K inverse; cubic derivative algebraically contains K3 + six K1/K2 + six ordered K1^3',
      'five_mandatory_classes':['gauge-leg linear contraction','spectator-u Lie derivative','spectator-v Lie derivative','left scalar/source endpoint','right scalar/source endpoint'],
      'parent_authorities':['Iter594 13-family assembly','Iter596 prospectively frozen nonlinear Ward recursion','Iter598 fail-closed route mismatch audit'],
      'thresholds_inherited_unchanged_from_iter597_pre_result':{'anchor_abs':ANCHOR_TOL,'assembly_match_abs':ASSEMBLY_MATCH_TOL,'ward_abs':WARD_ABS_TOL,'ward_last_step':WARD_STEP_TOL,'fd_steps':list(FD_STEPS),'grid_n':base.GRID_N,'lattice_radius':base.LAT_R},
      'fixture_closure':closure,'implemented_one_leg_anchors':anchors,'iter594_crosscheck':assembly,'ward_rows':ward,
      'observed':{'max_full_ward_abs':max_abs,'max_full_ward_last_step':max_step},
      'source_born_subtraction':'NOT_PERFORMED','source_to_iter582_map':'NOT_PERFORMED','candidate_residual':False,
      'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'explicit_nonclaims':['not a comparator identity','not a comparator-subtracted residual','not a novelty certificate'],
      'iter597_negative_numbers':'PRESERVED_NONAUTHORITATIVE_OFF_CONTRACT_DIAGNOSTIC',
      'next_gate_if_pass':'raw-consume this artifact; only after raw-valid PASS freeze/apply full-observable source-to-Iter582/native-linked map before fixed comparator quotient',
      'next_gate_if_fail':'preserve corrected negative Ward result as scientific FAIL; diagnose failed gauge/spectator/endpoint component without weakening Iter596, changing thresholds, or deleting source families'
    }
    out=ROOT/'results'/'iteration599_full_nonlinear_ward_corrected'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':ITERATION,'result_sha256':sha,'failures':failures,
           'classification':('PASS_RAW_AUTHORITY_AUDIT_ITER599_CORRECTED_FULL_NONLINEAR_WARD' if scientific_pass
                             else 'FAIL_RAW_AUTHORITY_AUDIT_ITER599_CORRECTED_FULL_NONLINEAR_WARD')}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    # Scientific FAIL is a retained result; nonzero exit prevents workflow green from being confused with a PASS.
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
