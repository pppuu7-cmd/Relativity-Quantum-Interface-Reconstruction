#!/usr/bin/env python3
"""Iteration 596: fail-closed audit of the prospectively frozen nonlinear Ward contract.

This is a protocol/authority gate only. It does not evaluate the full nonlinear Ward
residual, perform Source/Born subtraction, map to Iter582, or create a model residual.
"""
from __future__ import annotations
import contextlib, hashlib, io, json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/'candidate_gravity'/'contracts'/'ITERATION596_NONLINEAR_WARD_CONTRACT.md'
R587=ROOT/'results'/'iteration587_source_offshell_symmetric_routing'/'result.json'
I588=ROOT/'analysis'/'source_k1_k2_fixture_binding_iteration588.py'
I368=ROOT/'candidate_gravity'/'code'/'iteration368_tru1sq_timelike_full_prepruning_routing.py'
LEGS=('s','a','b')
ETA_C=np.diag([-1.,1.,1.,1.])


def q2(v):
    v=np.asarray(v,float); return float(v@ETA_C@v)


def main():
    failures=[]
    text=CONTRACT.read_text()
    required=[
      'Status: PRE-RESULT FROZEN CONTRACT',
      'f(x)=∫_k exp(-i k·x) f(k)',
      'Delta^(0)_xi h_{mu nu}(l) = l_mu xi_nu(l) + l_nu xi_mu(l)',
      'Delta^(1)_xi h_{mu nu}(k)',
      'Delta_xi phi(k)',
      'K3 + six K1/K2 placements + six ordered K1^3 chains',
      'SpectatorLie_u', 'SpectatorLie_v', 'EndpointLeft', 'EndpointRight',
      "q_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu",
      'q_mu V^{mu nu}=(m^2-s/4)q^nu',
      'no Source/Born subtraction in Iter596',
      'no ANSATZ-003', 'no Fisher/resources'
    ]
    for token in required:
        if token not in text: failures.append('contract missing token: '+token)

    r587=json.loads(R587.read_text())
    if r587.get('iteration')!=587 or r587.get('failures')!=[] or not r587.get('scientific_gate_pass'):
        failures.append('Iter587 authority not raw-valid committed PASS')
    if r587.get('specialized_Ward_identity')!='q_mu V^{mu nu}=(m^2-s/4) q^nu':
        failures.append('Iter587 specialized Ward anchor drift')
    if r587.get('frozen_routing')!='for each physical timelike s in {1,0.34,0.14}, q=(sqrt(s),0,0,0), p=-q/2, p_prime=+q/2, k=q':
        failures.append('Iter587 symmetric route drift')

    s588=I588.read_text()
    for token in ["LEGS=('s','a','b')", "expected={'s':-1.0,'a':-0.14,'b':-0.34}",
                  "p=-0.5*q; pp=+0.5*q", "two_block_orientations_required"]:
        if token not in s588: failures.append('Iter588 fixture-binding source drift: '+token)

    # Re-execute only the frozen Iter368 setup prefix, exactly as Iter588 does.
    src=I368.read_text(); marker='# Cache expensive same-parent blocks by routed loop momentum.'
    if src.count(marker)!=1:
        failures.append('Iter368 setup boundary drift')
        M=None
    else:
        ns={'__name__':'iteration596_parent368_fixture','__file__':str(I368)}
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src.split(marker,1)[0],str(I368),'exec'),ns,ns)
        if tuple(ns.get('LEGS',()))!=LEGS: failures.append('Iter368 leg order drift')
        M=ns.get('M')

    fixture=[]; max_closure=0.; max_q2err=0.; expected={'s':-1.0,'a':-0.14,'b':-0.34}
    if M is not None:
        for g in LEGS:
            spectators=tuple(x for x in LEGS if x!=g)
            q=np.asarray(M[g][0],float)
            quv=sum((np.asarray(M[x][0],float) for x in spectators),np.zeros(4))
            closure=float(np.max(np.abs(q+quv))); max_closure=max(max_closure,closure)
            q2err=abs(q2(q)-expected[g]); max_q2err=max(max_q2err,q2err)
            p=-0.5*q; pp=0.5*q
            route=float(np.max(np.abs((p+q)-pp)))
            if closure>2e-15: failures.append(f'{g}: fixture closure {closure}')
            if q2err>2e-15: failures.append(f'{g}: q2 drift {q2err}')
            if route>2e-15: failures.append(f'{g}: symmetric route drift {route}')
            rows=[x for x in r587['rows'] if abs(float(x['candidate_q2_minus_plus_plus_plus'])-expected[g])<2e-15]
            if len(rows)!=1: failures.append(f'{g}: Iter587 anchor row count {len(rows)}')
            fixture.append({'gauge_leg':g,'spectators':list(spectators),'q':q.tolist(),'q2_candidate':q2(q),'closure':closure})

    # The contract's mandatory spectator-free reduction is checked against the exact
    # committed Iter587 coefficients, not re-fit from any Iter596 output.
    reduction=[]
    for row in r587.get('rows',[]):
        s=float(row['s']); m=float(r587['mass'])
        inherited=float(row['ward_longitudinal_coefficient_m2_minus_s_over_4'])
        exact=m*m-s/4.0
        err=abs(inherited-exact)
        if err>2e-15: failures.append(f'Iter587 reduction coefficient drift at s={s}: {err}')
        reduction.append({'s':s,'inherited_coefficient':inherited,'m2_minus_s_over_4':exact,'error':err})

    result={
      'iteration':596,'date':'2026-09-08','model_readiness_percent':24,
      'classification':'PASS_PROSPECTIVE_FULL_NONLINEAR_WARD_CONTRACT_FREEZE_AND_ONE_LEG_REDUCTION__NON_RESIDUAL' if not failures else 'FAIL_NONLINEAR_WARD_CONTRACT_AUDIT',
      'scientific_gate_pass':not failures,'failures':failures,
      'scope':'PRE_RESULT_CONTRACT_AND_REDUCTION_ONLY__NO_FULL_WARD_NUMERICAL_CLASSIFICATION',
      'contract_sha256':hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
      'parent_authorities':['Iter587 one-leg off-shell Ward anchor','Iter588 exact Iter368 three-mode fixture','Iter589 same-action normalization','Iter590/594 full 13-family cubic response'],
      'frozen_fourier_convention':'f(x)=int exp(-ik.x) f(k); stripped Delta_xi=i delta_xi',
      'mandatory_full_terms':['gauge-leg linear contraction','spectator-u Lie derivative','spectator-v Lie derivative','left scalar endpoint','right scalar endpoint'],
      'fixture_rows':fixture,'one_leg_reduction_rows':reduction,
      'observed':{'max_fixture_closure':max_closure,'max_candidate_q2_error':max_q2err},
      'source_born_subtraction':'NOT_PERFORMED','source_to_iter582_map':'NOT_PERFORMED',
      'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'explicit_nonclaims':['not nonlinear Ward PASS/FAIL','not comparator residual','not Candidate-Gravity model PASS/FAIL','not novelty certificate'],
      'next_gate_if_pass':'evaluate the full Iter594 13-family cubic source object for all three cyclic gauge legs using the frozen Iter596 gauge/spectator/endpoint recursion; preserve negative results and raw-consume artifact before any source-to-Iter582 map'
    }
    out=ROOT/'results'/'iteration596_nonlinear_ward_contract'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':596,'result_sha256':sha,'contract_sha256':result['contract_sha256'],'failures':failures,
           'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER596_NONLINEAR_WARD_CONTRACT' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER596_NONLINEAR_WARD_CONTRACT'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
