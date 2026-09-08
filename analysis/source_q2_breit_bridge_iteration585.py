#!/usr/bin/env python3
"""Iteration 585: frozen conserved MSSC-001 source bridge to Iter582 q^2 buckets.

This gate fixes only the kinematic/linear-source mapping.  It does not identify
an on-shell Compton amplitude with the off-shell Iter582 operator coordinate,
does not choose the second graviton slot, and performs no Source/Born subtraction.

For each prospectively inherited spacelike q^2 bucket use the unique symmetric
Breit-frame elastic scalar kinematics
  q=(0,Q,0,0), p=(E,-Q/2,0,0), p'=(E,+Q/2,0,0),
  Q=sqrt(-q^2), E=sqrt(m^2+Q^2/4), m=0.7,
so p^2=p'^2=m^2 and q=p'-p.  The frozen Iter218 K1 vertex then obeys the
source Ward identity exactly on shell.
"""
import hashlib,json,math
from pathlib import Path
import numpy as np

ETA=np.diag([1.,-1.,-1.,-1.]); M=0.7
Q2=(-1.0,-0.34,-0.14)

def dot(a,b): return float(a@ETA@b)

def vertex(p,pp):
    return np.outer(p,pp)+np.outer(pp,p)-ETA*(dot(p,pp)-M*M)

def main():
    # Bind exact Iter584 raw authority and the prospective q2 map.
    p584=Path('results/iteration584_source_k2_bilinear/result.json')
    raw=p584.read_bytes()
    if hashlib.sha256(raw).hexdigest()!='4ba39a78550e27575939fec03fb9a1514d43e478ca25fb354c87939ed316c76d':
        raise SystemExit('iteration584 raw sha drift')
    o584=json.loads(raw)
    if o584.get('classification')!='PASS_MSSC001_MIXED_BILINEAR_K2_CONTACT__NON_RESIDUAL' or o584.get('source_born_subtraction')!='NOT_PERFORMED':
        raise SystemExit('iteration584 prerequisite not pass')
    qmap=json.loads(Path('candidate_gravity/contracts/iteration389_double_double_prospective_index_q2_map.json').read_text())
    inherited=tuple(sorted(set(float(x) for x in qmap['index_q2_map'].values())))
    if inherited!=tuple(sorted(Q2)): raise SystemExit(('q2 bucket drift',inherited,Q2))

    rows=[]; failures=[]; maxward=0.; maxshell=0.; maxq=0.; maxinv=0.
    for q2 in Q2:
        if q2>=0: failures.append(f'non-spacelike q2 {q2}'); continue
        Q=math.sqrt(-q2); E=math.sqrt(M*M+Q*Q/4.)
        p=np.array([E,-Q/2.,0.,0.]); pp=np.array([E,Q/2.,0.,0.]); q=pp-p
        V=vertex(p,pp); ql=ETA@q
        ward=ql@V
        shell=max(abs(dot(p,p)-M*M),abs(dot(pp,pp)-M*M))
        qerr=abs(dot(q,q)-q2)
        inv=abs(dot(p,pp)-(M*M-q2/2.))
        w=float(np.max(np.abs(ward)))
        maxward=max(maxward,w); maxshell=max(maxshell,shell); maxq=max(maxq,qerr); maxinv=max(maxinv,inv)
        if shell>2e-15: failures.append(f'q2 {q2}: scalar shell drift {shell}')
        if qerr>2e-15: failures.append(f'q2 {q2}: q2 drift {qerr}')
        if inv>2e-15: failures.append(f'q2 {q2}: invariant drift {inv}')
        if w>2e-14: failures.append(f'q2 {q2}: K1 Ward drift {w}')
        rows.append({'q_squared':q2,'Q':Q,'E':E,'p':p.tolist(),'p_prime':pp.tolist(),'q':q.tolist(),
                     'p_squared':dot(p,p),'p_prime_squared':dot(pp,pp),'q_reconstructed_squared':dot(q,q),
                     'p_dot_p_prime':dot(p,pp),'expected_p_dot_p_prime':M*M-q2/2.,
                     'K1_vertex':V.tolist(),'q_lower_contract_K1':ward.tolist(),'max_abs_Ward':w})

    result={
      'iteration':585,'date':'2026-09-08','model_readiness_percent':24,
      'parent_source':'MSSC-001 / Iteration218','parent_contact':'Iter584 raw-valid',
      'q2_authority':'Iteration389 prospective map inherited by Iter581/582',
      'bridge':'symmetric Breit-frame elastic on-shell scalar source for each Iter582 spacelike q2 bucket',
      'mass':M,'rows':rows,
      'observed':{'max_scalar_shell_error':maxshell,'max_q2_error':maxq,'max_invariant_error':maxinv,'max_K1_Ward_abs':maxward},
      'failures':failures,'scientific_gate_pass':not failures,
      'classification':'PASS_MSSC001_CONSERVED_SOURCE_BREIT_Q2_BRIDGE__NON_RESIDUAL' if not failures else 'FAIL_MSSC001_CONSERVED_SOURCE_BREIT_Q2_BRIDGE',
      'explicit_nonclaims':['does not identify Iter219/220 on-shell Compton values with Iter582','does not define the second graviton/source-contact slot','does not apply comparator quotient','does not perform Source/Born subtraction','not a Candidate-Gravity model PASS'],
      'source_born_subtraction':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'freeze the second graviton insertion/soft or response leg from the pre-existing matched-observable protocol, then construct K1 exchange + Iter584 K2 contact on these same q2 buckets and verify the complete source Ward identity before any comparator subtraction'
    }
    out=Path('results/iteration585_source_q2_breit_bridge'); out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest(); audit={'iteration':585,'result_sha256':sha,'failures':failures,'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER585_SOURCE_Q2_BRIDGE' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER585_SOURCE_Q2_BRIDGE'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
