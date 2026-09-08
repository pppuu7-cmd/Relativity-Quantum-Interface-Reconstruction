#!/usr/bin/env python3
"""Iteration 588: bind MSSC K1/K2 source routing to the frozen Iter582 parent fixture.

No source amplitude, Ward cancellation, Born subtraction, comparator quotient or
residual is evaluated here.  The purpose is to remove the last momentum-routing
ambiguity before constructing the source-completed nonlinear observable.

The parent Iter368 fixture already freezes three background modes s,a,b with
s+a+b=0.  For each cyclic role assignment the singleton is the output leg and
the other two modes are the K2 input pair.  Iter587 supplies the parameter-free
symmetric off-shell scalar routing for the singleton total momentum.  Since the
pair sum is exactly minus the singleton momentum, the K2 pair closes the same
scalar line without introducing any new kinematic parameter.
"""
from __future__ import annotations
import contextlib, hashlib, io, json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
CROOT=ROOT/'candidate_gravity'/'code'
ETA_C=np.diag([-1.,1.,1.,1.])
ETA_S=-ETA_C
LEGS=('s','a','b')


def q2(v,eta):
    v=np.asarray(v,float); return float(v@eta@v)


def main():
    # Bind Iter587 exact raw result.
    p587=ROOT/'results'/'iteration587_source_offshell_symmetric_routing'/'result.json'
    raw587=p587.read_bytes()
    if hashlib.sha256(raw587).hexdigest()!='1fb42e1ab8e3de2ae31426297c40f9c845ddd38e08d3f3f63cd6d4381252bcfd':
        raise SystemExit('iteration587 raw sha drift')
    r587=json.loads(raw587)
    if r587.get('classification')!='PASS_PROSPECTIVE_MSSC001_SYMMETRIC_OFFSHELL_K1_ROUTING_AND_WARD_CONTRACT__NON_RESIDUAL' or r587.get('failures')!=[]:
        raise SystemExit('iteration587 prerequisite not pass')

    # Re-execute only the setup prefix of the exact Iter368 parent so that the
    # fixture momenta are inherited rather than retyped.
    p368=CROOT/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
    src=p368.read_text(); marker='# Cache expensive same-parent blocks by routed loop momentum.'
    if src.count(marker)!=1: raise SystemExit('iteration368 setup boundary drift')
    ns={'__name__':'iteration588_parent368_fixture','__file__':str(p368)}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src.split(marker,1)[0],str(p368),'exec'),ns,ns)
    if tuple(ns['LEGS'])!=LEGS: raise SystemExit(('leg order drift',ns['LEGS']))
    M=ns['M']

    rows=[]; failures=[]; max_closure=0.; max_scalar_closure=0.; max_q2_map=0.
    expected={'s':-1.0,'a':-0.14,'b':-0.34}
    for singleton in LEGS:
        pair=tuple(x for x in LEGS if x!=singleton)
        q=np.asarray(M[singleton][0],float)
        qpair=sum((np.asarray(M[x][0],float) for x in pair),np.zeros(4))
        clos=float(np.max(np.abs(q+qpair))); max_closure=max(max_closure,clos)
        cq2=q2(q,ETA_C); sq2=q2(q,ETA_S)
        q2err=max(abs(cq2-expected[singleton]),abs(sq2+expected[singleton])); max_q2_map=max(max_q2_map,q2err)
        p=-0.5*q; pp=+0.5*q
        # K1(singleton) changes p -> p+q = pp.  K2(pair) carries qpair=-q
        # and therefore changes pp -> pp+qpair = p.
        scalar_close=float(np.max(np.abs((p+q)-pp)))
        scalar_close=max(scalar_close,float(np.max(np.abs((pp+qpair)-p))))
        max_scalar_closure=max(max_scalar_closure,scalar_close)
        if clos>2e-15: failures.append(f'{singleton}: external fixture closure {clos}')
        if q2err>2e-15: failures.append(f'{singleton}: q2/signature map {q2err}')
        if scalar_close>2e-15: failures.append(f'{singleton}: scalar K1/K2 line closure {scalar_close}')
        # Match the exact Iter587 row by physical source q^2=s=-candidate q^2.
        candidates=[x for x in r587['rows'] if abs(float(x['s'])-sq2)<2e-15]
        if len(candidates)!=1: failures.append(f'{singleton}: Iter587 source-routing row match count {len(candidates)}')
        rr=candidates[0] if candidates else None
        rows.append({
          'output_singleton':singleton,
          'input_K2_pair':list(pair),
          'candidate_momenta_minus_plus_plus_plus':{
             'singleton_q':q.tolist(),'pair_sum':qpair.tolist(),
             'singleton_q2':cq2,'pair_sum_q2':q2(qpair,ETA_C)},
          'MSSC_same_physical_momenta_plus_minus_minus_minus':{
             'singleton_q2':sq2,'pair_sum_q2':q2(qpair,ETA_S)},
          'scalar_routing':{
             'p_before_K1':p.tolist(),'p_after_K1_before_K2':pp.tolist(),
             'p_after_K2':(pp+qpair).tolist(),
             'K1_momentum':q.tolist(),'K2_total_pair_momentum':qpair.tolist(),
             'closure_error':scalar_close,
             'inverse_propagator_delta':None if rr is None else rr['inverse_propagator_delta_p2_minus_m2'],
             'K1_Ward_longitudinal_coefficient':None if rr is None else rr['ward_longitudinal_coefficient_m2_minus_s_over_4']
          },
          'two_block_orientations_required':['K1_SINGLETON_THEN_K2_PAIR','K2_PAIR_THEN_K1_SINGLETON']
        })

    result={
      'iteration':588,'date':'2026-09-08','model_readiness_percent':24,
      'classification':'PASS_ITER582_FIXTURE_BOUND_MSSC_K1_K2_ROUTING_CONTRACT__NON_RESIDUAL' if not failures else 'FAIL_ITER582_FIXTURE_BOUND_MSSC_K1_K2_ROUTING',
      'scientific_gate_pass':not failures,'failures':failures,
      'parent_operator_fixture':'Iter368 -> Iter370/372 -> Iter582',
      'parent_source_authorities':['Iter218 MSSC-001 K1 Ward','Iter584 mixed K2 contact','Iter587 symmetric off-shell scalar routing'],
      'frozen_role_rule':'for each Iter368 singleton leg, the complementary two legs form the K2 input pair; both block orientations retained',
      'rows':rows,
      'observed':{'max_external_momentum_closure':max_closure,'max_scalar_K1_K2_line_closure':max_scalar_closure,'max_signature_q2_map_error':max_q2_map},
      'interpretation':'The source completion can be constructed on exactly the same three-mode fixture as the connection-sector operator. No new q=k1+k2 split is needed: the original singleton/pair decomposition already fixes it prospectively.',
      'explicit_nonclaims':['not yet a Ward cancellation test','not a source tree value','not a comparator residual','not Candidate-Gravity PASS/FAIL','does not authorize Source/Born subtraction'],
      'source_born_subtraction':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'evaluate the complete same-fixture source-completed second-order response block with both K1/K2 orientations and the Iter584 contact, and test the correct off-shell Ward identity including the Iter587 inverse-propagator RHS before mapping onto Iter582'
    }
    out=ROOT/'results'/'iteration588_source_k1_k2_fixture_binding'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest(); audit={'iteration':588,'result_sha256':sha,'failures':failures,'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER588_SOURCE_FIXTURE_BINDING' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER588_SOURCE_FIXTURE_BINDING'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
