#!/usr/bin/env python3
"""Iteration 599: corrected full nonlinear Ward evaluation on exact Iter596 route.

This is a prospective repair of Iter597's routing defect only.  The parent Fourier
matrix implementation, complete same-parent 13-family content, nonlinear spectator
and endpoint transformations, finite-difference grid, and all pre-result thresholds
are inherited unchanged.  The mandatory one-leg anchor and the full Ward rows now
use, for each gauge leg g, exactly p=-q_g/2 and p'=+q_g/2 as frozen by Iter596.
Iter594 cubic-family cross-checks remain on their inherited probes solely as an
implementation cross-check.
"""
from __future__ import annotations
import contextlib, hashlib, importlib.util, io, json, sys
from pathlib import Path
import numpy as np

ITERATION=599
ROOT=Path(__file__).resolve().parents[1]
P597=ROOT/'analysis'/'nonlinear_ward_full_response_iteration597.py'
OUT=ROOT/'results'/'iteration599_full_nonlinear_ward_symmetric_route'
OUT.mkdir(parents=True,exist_ok=True)

spec=importlib.util.spec_from_file_location('rqir_iter597_parent',P597)
if spec is None or spec.loader is None: raise SystemExit('cannot load Iter597 parent evaluator')
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

# Freeze inheritance checks before any numerical classification.
block=json.loads((ROOT/'candidate_gravity'/'results'/'iteration598_iter597_contract_conformance.json').read_text())
if block.get('classification') != 'BLOCKED_ITER597_IMPLEMENTATION_DOES_NOT_INSTANTIATE_FROZEN_ITER596_ROUTE__NEGATIVE_NUMBERS_PRESERVED_NONAUTHORITATIVE':
    raise SystemExit('Iter598 conformance authority drift')
contract=json.loads((ROOT/'candidate_gravity'/'results'/'iteration596_nonlinear_ward_contract.json').read_text())
if contract.get('classification') != 'PASS_PROSPECTIVE_FULL_NONLINEAR_WARD_CONTRACT_FREEZE_AND_ONE_LEG_REDUCTION__NON_RESIDUAL' or contract.get('failures') != []:
    raise SystemExit('Iter596 contract authority not PASS')
r594=json.loads((ROOT/'candidate_gravity'/'results'/'iteration594_full_cubic_routed_assembly.json').read_text())
if r594.get('classification') != 'PASS_FULL_SAME_ACTION_ROUTED_CUBIC_SOURCE_ASSEMBLY_AND_PERMUTATION_SYMMETRY__NON_WARD_NON_RESIDUAL' or r594.get('failures') != []:
    raise SystemExit('Iter594 authority not PASS')

# Explicitly assert no numerical conventions changed from Iter597.
FD_STEPS=m.FD_STEPS; ANCHOR_TOL=m.ANCHOR_TOL; ASSEMBLY_MATCH_TOL=m.ASSEMBLY_MATCH_TOL
WARD_ABS_TOL=m.WARD_ABS_TOL; WARD_STEP_TOL=m.WARD_STEP_TOL
qs,hs=m.inherit_fixture()
failures=[]
closure=float(np.max(np.abs(sum((qs[x] for x in m.LEGS),np.zeros(4)))))
if closure>1e-14: failures.append(f'fixture closure {closure}')

# Mandatory one-leg anchor: exact Iter596/Iter587 symmetric route per gauge leg.
anchors=[]
for g in m.LEGS:
    p0=-0.5*np.asarray(qs[g],float)
    u,v=tuple(x for x in m.LEGS if x!=g)
    for ix,xi in enumerate(m.XI_BASIS):
        C,inds,pos,*_=m.covariance_G(0.0,0.0,g,u,v,xi,p0,hs,qs)
        c=(0,0); r=m.MODE[g]
        if r not in pos: raise RuntimeError('lattice too small for exact symmetric anchor')
        # row momentum p0+q_g = +q_g/2, column momentum p0=-q_g/2
        val=C[pos[r],pos[c]]; err=abs(val)
        anchors.append({'gauge_leg':g,'q_g':np.asarray(qs[g]).tolist(),'p_in':p0.tolist(),
                        'p_out':(p0+np.asarray(qs[g])).tolist(),'xi_basis':ix,
                        'abs_covariance_residual':float(err)})
        if err>ANCHOR_TOL:
            failures.append(f'exact symmetric-route one-leg covariance anchor {g}/xi{ix} = {err}')

# Independent implementation cross-check: unchanged Iter594 inherited probes only.
assembly=[]
for ip,p0 in enumerate(m.PROBES):
    vals=[m.cubic_G_coeff(p0,hs,qs,h) for h in FD_STEPS]
    target=float(r594['probe_results'][ip]['canonical_assembly']['full_dabcG'])
    match=abs(vals[-1].real-target); imag=abs(vals[-1].imag); step=abs(vals[-1]-vals[-2])
    assembly.append({'p0':p0.tolist(),'fd_steps':list(FD_STEPS),
                     'matrix_cubic_values_real':[float(z.real) for z in vals],
                     'matrix_cubic_values_imag':[float(z.imag) for z in vals],
                     'iter594_target':target,'last_match_abs':float(match),
                     'last_imag_abs':float(imag),'last_step_abs':float(step)})
    if match>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 cubic assembly cross-check mismatch probe {ip}: {match}')
    if imag>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 cubic assembly cross-check imaginary probe {ip}: {imag}')
    if step>ASSEMBLY_MATCH_TOL: failures.append(f'Iter594 cubic assembly cross-check convergence probe {ip}: {step}')

# Full nonlinear Ward rows on the exact gauge-attached symmetric scalar route.
ward=[]; max_abs=0.; max_step=0.
for g in m.LEGS:
    p0=-0.5*np.asarray(qs[g],float)
    inds,pos,_=m.lattice(p0,qs); c=pos[(0,0)]
    u,v=tuple(x for x in m.LEGS if x!=g)
    for ix,xi in enumerate(m.XI_BASIS):
        vals=[]
        for h in FD_STEPS:
            def f(eu,ev):
                C,*_=m.covariance_G(eu,ev,g,u,v,xi,p0,hs,qs)
                # After q_s+q_a+q_b=0, the full cubic response returns to the
                # same scalar momentum, hence diagonal (0,0)->(0,0).
                return C[c,c]
            vals.append(m.mixed2(f,h))
        last=vals[-1]; step=abs(vals[-1]-vals[-2]); ab=abs(last)
        max_abs=max(max_abs,float(ab)); max_step=max(max_step,float(step))
        ward.append({'gauge_leg':g,'q_g':np.asarray(qs[g]).tolist(),'p_in':p0.tolist(),
                     'p_out':(p0+np.asarray(qs[g])).tolist(),'spectators':[u,v],
                     'xi_basis':ix,'fd_steps':list(FD_STEPS),
                     'ward_values_real':[float(z.real) for z in vals],
                     'ward_values_imag':[float(z.imag) for z in vals],
                     'last_abs':float(ab),'last_step_abs':float(step)})
        if ab>WARD_ABS_TOL: failures.append(f'full nonlinear Ward residual {g}/xi{ix} = {ab}')
        if step>WARD_STEP_TOL: failures.append(f'full nonlinear Ward convergence {g}/xi{ix} = {step}')

classification=('PASS_FULL_SOURCE_LEVEL_NONLINEAR_WARD_ON_EXACT_FROZEN_ITER596_SYMMETRIC_ROUTE__NON_RESIDUAL'
                if not failures else
                'FAIL_FULL_SOURCE_LEVEL_NONLINEAR_WARD_ON_EXACT_FROZEN_ITER596_SYMMETRIC_ROUTE__PRESERVED_NEGATIVE_RESULT')
result={
 'iteration':ITERATION,'date':'2026-09-08','model_readiness_percent':24,
 'classification':classification,'scientific_gate_pass':not failures,'failures':failures,
 'scope':'FULL_SAME_PARENT_CUBIC_GREEN_FUNCTION_WARD__EXACT_ITER596_SYMMETRIC_ROUTE__NO_COMPARATOR_SUBTRACTION',
 'routing_repair_only':True,
 'route':'for each gauge g: p=-q_g/2, p_prime=+q_g/2',
 'identity':'Delta G - T G - G T^T = 0; mixed spectator coefficient with exact Iter588 q_s+q_a+q_b=0',
 'full_family_content':'same parent K inverse; cubic derivative algebraically contains K3 + six K1/K2 + six ordered K1^3',
 'parent_authorities':['Iter594 13-family assembly','Iter596 frozen nonlinear Ward recursion','Iter598 contract mismatch audit'],
 'thresholds_frozen_pre_result':{'anchor_abs':ANCHOR_TOL,'assembly_match_abs':ASSEMBLY_MATCH_TOL,
    'ward_abs':WARD_ABS_TOL,'ward_last_step':WARD_STEP_TOL,'fd_steps':list(FD_STEPS),
    'grid_n':m.GRID_N,'lattice_radius':m.LAT_R},
 'fixture_closure':closure,'exact_symmetric_route_anchors':anchors,'iter594_crosscheck':assembly,'ward_rows':ward,
 'observed':{'max_full_ward_abs':max_abs,'max_full_ward_last_step':max_step},
 'source_born_subtraction':'NOT_PERFORMED','source_to_iter582_map':'NOT_PERFORMED','candidate_residual':False,
 'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
 'explicit_nonclaims':['not a comparator identity','not a comparator-subtracted residual','not a novelty certificate'],
 'next_gate_if_pass':'raw-consume; then freeze/apply full-observable source-to-Iter582/native-linked map before Source/Born subtraction/comparator quotient',
 'next_gate_if_fail':'raw-consume and preserve negative Ward result; decompose gauge-leg, spectator-u, spectator-v, endpoint-left, endpoint-right contributions on the same exact route without weakening Iter596 or deleting source families'
}
rp=OUT/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
sha=hashlib.sha256(rp.read_bytes()).hexdigest()
audit={'iteration':ITERATION,'classification':'PASS_RAW_INTEGRITY_ITER599_SYMMETRIC_ROUTE_WARD',
       'failures':[],'result_sha256':sha,'scientific_classification':classification}
(OUT/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
# Preserve scientific FAIL as raw output while allowing audit/upload steps to run.
raise SystemExit(0 if not failures else 2)
