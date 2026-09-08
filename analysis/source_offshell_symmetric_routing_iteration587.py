#!/usr/bin/env python3
"""Iteration 587: prospectively freeze the minimal symmetric off-shell MSSC-001 routing.

This step uses only the frozen Iter218 parent action/convention and its exact K1
Ward identity.  It is intentionally upstream of any K2 tree/contact cancellation,
Source/Born subtraction, comparator quotient, or residual fit.

Candidate timelike buckets use eta=(-,+,+,+), q_cand^2=-s.  The same physical
vector in MSSC-001 eta=(+,-,-,-) has q_src^2=+s.  For each s we freeze the
parameter-free symmetric off-shell routing
    p=-q/2,  p'=+q/2,  k=p'-p=q,
with q=(sqrt(s),0,0,0) in the MSSC rest frame.
"""
from fractions import Fraction
from pathlib import Path
import hashlib, json, math
import numpy as np

ETA=np.diag([1.0,-1.0,-1.0,-1.0])
M=Fraction(7,10)
S_BUCKETS=(Fraction(1,1),Fraction(17,50),Fraction(7,50))

def dot(a,b): return float(a@ETA@b)

def main():
    rows=[]; failures=[]
    for sf in S_BUCKETS:
        s=float(sf); q=np.array([math.sqrt(s),0.,0.,0.])
        p=-0.5*q; pp=0.5*q; k=pp-p
        m=float(M)
        V=np.outer(p,pp)+np.outer(pp,p)-ETA*(dot(p,pp)-m*m)
        lhs=(ETA@k)@V
        delta=dot(p,p)-m*m
        rhs=(dot(pp,pp)-m*m)*p-(dot(p,p)-m*m)*pp
        expected_coeff=M*M-sf/Fraction(4,1)
        expected=float(expected_coeff)*q
        err=float(max(np.max(np.abs(lhs-rhs)),np.max(np.abs(lhs-expected))))
        if err>2e-15: failures.append(f's={s}: Ward mismatch {err}')
        if abs(dot(p,p)-s/4)>2e-15 or abs(dot(pp,pp)-s/4)>2e-15:
            failures.append(f's={s}: symmetric routing invariant drift')
        rows.append({
          's':s,
          'candidate_q2_minus_plus_plus_plus':-s,
          'source_q2_plus_minus_minus_minus':s,
          'routing':'p=-q/2, p_prime=+q/2, k=q, q=(sqrt(s),0,0,0)',
          'p2_equals_pprime2':s/4,
          'inverse_propagator_delta_p2_minus_m2':delta,
          'ward_longitudinal_coefficient_m2_minus_s_over_4':float(expected_coeff),
          'ward_longitudinal_coefficient_exact':f'{expected_coeff.numerator}/{expected_coeff.denominator}',
          'ward_identity_max_error':err,
          'on_shell_status':'OFFSHELL_BY_CONSTRUCTION'
        })
    result={
      'iteration':587,
      'date':'2026-09-08',
      'model_readiness_percent':24,
      'parent_authority':'Iter218 MSSC-001 exact off-shell K1 Ward identity; signature mapping audited independently in Iter586 workflow',
      'classification':'PASS_PROSPECTIVE_MSSC001_SYMMETRIC_OFFSHELL_K1_ROUTING_AND_WARD_CONTRACT__NON_RESIDUAL' if not failures else 'FAIL_MSSC001_SYMMETRIC_OFFSHELL_K1_ROUTING',
      'scientific_gate_pass':not failures,
      'failures':failures,
      'source_action':'S_phi=-1/2 int sqrt(-g)[g^{mu nu} partial_mu phi partial_nu phi + m^2 phi^2]',
      'source_signature':'(+---)',
      'mass':float(M),
      'frozen_routing':'for each physical timelike s in {1,0.34,0.14}, q=(sqrt(s),0,0,0), p=-q/2, p_prime=+q/2, k=q',
      'exact_K1_Ward_identity':'k_mu V^{mu nu}=(p_prime^2-m^2)p^nu-(p^2-m^2)p_prime^nu',
      'specialized_Ward_identity':'q_mu V^{mu nu}=(m^2-s/4) q^nu',
      'rows':rows,
      'interpretation':'The K1 source is necessarily longitudinal off shell by an amount fixed exactly by the scalar inverse propagator. This term must be retained and cancelled/matched only within the complete same-dynamics K1-exchange plus K2-contact Ward object; it may not be dropped by imposing on-shell transversality.',
      'explicit_nonclaims':['not a Candidate-Gravity consistency PASS or FAIL','not a comparator identity','not a model-level non-identifiability result','not a near-degeneracy claim','not a novelty certificate','does not authorize Source/Born subtraction'],
      'source_born_subtraction':'NOT_PERFORMED',
      'ANSATZ_003':'FORBIDDEN',
      'Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'after Iter586 raw authority is consumed, construct the complete same-routing two-graviton MSSC-001 source Ward object from K1 exchange plus Iter584 K2 contact and verify cancellation of the inverse-propagator longitudinal terms before any mapping to Iter582 or comparator subtraction'
    }
    out=Path('results/iteration587_source_offshell_symmetric_routing'); out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':587,'result_sha256':sha,'failures':failures,'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER587_OFFSHELL_ROUTING' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER587_OFFSHELL_ROUTING'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
