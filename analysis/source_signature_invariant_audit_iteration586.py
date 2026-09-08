#!/usr/bin/env python3
"""Iteration 586: signature/invariant audit before source matching.

The Candidate-Gravity discontinuity sector uses eta=(-,+,+,+) and q^2<0
for timelike channels, while MSSC-001 source calculations use eta=(+,-,-,-).
This gate prevents a same-number q^2 identification across those conventions.
It also checks whether the three Iter582 timelike invariants admit an on-shell
MSSC scalar elastic or pair realization for m=0.7.
"""
import hashlib,json,re
from pathlib import Path

M=0.7
CANDIDATE_Q2=(-1.0,-0.34,-0.14)

def main():
    c374=Path('candidate_gravity/code/iteration374_tru1sq_simple_simple_normalized_discontinuity.py').read_text()
    if 'return float(-a[0]*b[0]+np.dot(a[1:],b[1:]))' not in c374: raise SystemExit('candidate -+++ metric binding drift')
    c379=Path('candidate_gravity/code/iteration379_tru1sq_double_double_one_channel_pilot.py').read_text()
    if 'q2=float(np.real(mdot(q))); s=-q2' not in c379: raise SystemExit('candidate s=-q2 binding drift')
    s218=Path('analysis/minimal_scalar_source_completion_iteration218.py').read_text()
    if 'eta=np.diag([1.,-1.,-1.,-1.])' not in s218: raise SystemExit('MSSC +--- signature binding drift')
    qmap=json.loads(Path('candidate_gravity/contracts/iteration389_double_double_prospective_index_q2_map.json').read_text())
    qvals=tuple(sorted(set(float(v) for v in qmap['index_q2_map'].values())))
    if qvals!=tuple(sorted(CANDIDATE_Q2)): raise SystemExit(('candidate q2 map drift',qvals))

    svals=[-q for q in CANDIDATE_Q2]
    threshold=4*M*M
    rows=[]; failures=[]
    for cq,s in zip(CANDIDATE_Q2,svals):
        # Under a global signature flip the same physical timelike vector has
        # q_source^2(+---)=s=-q_candidate^2(-+++)>0.
        source_q2=s
        elastic_possible=False  # for future-directed equal-mass p,p': (p'-p)^2<=0
        pair_possible=source_q2>=threshold
        if source_q2<=0: failures.append(f'non-timelike mapped source invariant {source_q2}')
        if pair_possible: failures.append(f'unexpected above-threshold source bucket {source_q2}')
        rows.append({'candidate_q_squared_minus_plus_plus_plus':cq,
                     'candidate_s_equals_minus_q2':s,
                     'same_physical_source_q_squared_plus_minus_minus_minus':source_q2,
                     'MSSC_scalar_mass':M,'two_scalar_threshold_4m2':threshold,
                     'on_shell_equal_mass_elastic_difference_can_realize_timelike_q':elastic_possible,
                     'on_shell_scalar_pair_channel_open':pair_possible,
                     'source_channel_status':'OFFSHELL_SOURCE_COMPLETION_REQUIRED'})

    result={
      'iteration':586,'date':'2026-09-08','model_readiness_percent':24,
      'classification':'PASS_SIGNATURE_INVARIANT_AUDIT__OFFSHELL_SOURCE_REQUIRED__NON_RESIDUAL' if not failures else 'FAIL_SIGNATURE_INVARIANT_AUDIT',
      'scientific_gate_pass':not failures,'failures':failures,
      'candidate_convention':{'signature':'(-+++)','q2_buckets':list(CANDIDATE_Q2),'physical_timelike_s':svals,'D_s_meaning':'s-channel discontinuity, not a soft derivative'},
      'MSSC_convention':{'signature':'(+---)','mass':M,'same_physical_timelike_q2':svals,'two_scalar_threshold_4m2':threshold},
      'rows':rows,
      'iteration585_interpretation':'its Breit elastic K1/Ward calculation is internally correct but is NOT a matched bridge to Iter582 because it treated the same negative q2 numbers as spacelike in the opposite-signature source convention',
      'conclusion':'none of the three Iter582 timelike s values has an on-shell equal-mass MSSC elastic realization; all are also below the two-real-scalar pair threshold, so the matched MSSC observable must be off-shell/source-completed and must retain inverse-propagator Ward/contact terms',
      'explicit_nonclaims':['not a Candidate-Gravity failure','not a comparator residual','does not delete Iter585 internal algebra','does not authorize Source/Born subtraction'],
      'source_born_subtraction':'NOT_PERFORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'next_gate_if_pass':'freeze an off-shell MSSC scalar-source routing for s={1,0.34,0.14} under +---, verify the Iter218 off-shell K1 Ward identity including inverse-propagator terms, then use Iter584 K2 contact to form the complete two-graviton source Ward object before comparator subtraction'
    }
    out=Path('results/iteration586_source_signature_audit'); out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest(); audit={'iteration':586,'result_sha256':sha,'failures':failures,'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER586_SOURCE_SIGNATURE' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER586_SOURCE_SIGNATURE'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
