#!/usr/bin/env python3
"""Iteration 614: pole-root/Jacobian audit on frozen Iter613 MSSC001-NATIVE-S-KIN-V1.

No trajectory choice is made here.  Iter613 already froze

    p0(s)=(sqrt(s),0,0,0), s>0

in the MSSC-001 (+---) convention, with the exact Iter368/588 q_i fixed.
This script only derives the scalar-pole support implied by that frozen contract.
It does not evaluate source numerators, Source/Born subtraction, native T_cut
normalization, comparator quotient or Candidate residual.
"""
from __future__ import annotations
import json, math
from pathlib import Path

ITERATION=614
MASS=0.7
# Exact mode vectors from Iter368/588.  Source-sector scalar products here use
# the MSSC-001 / Iter594 signature (+---), not the connection-sector -+++ labels.
Q={
    's':(1.0,0.0,0.0,0.0),
    'a':(-0.4,0.1,0.1,0.0),
    'b':(-0.6,-0.1,-0.1,0.0),
}
LEGS=('s','a','b')
TOL=1e-12

def q2(q):
    return q[0]**2-q[1]**2-q[2]**2-q[3]**2

def roots_for(leg, sign):
    q=Q[leg]; q0=q[0]; qq=q2(q); c=MASS*MASS-qq
    rad=q0*q0+c
    if rad < -TOL:
        return []
    R=math.sqrt(max(rad,0.0))
    ws=((-q0+R,-q0-R) if sign=='+' else (q0+R,q0-R))
    out=[]
    for w in ws:
        if w <= TOL:
            continue
        s=w*w
        D=(MASS*MASS-s-qq-2*w*q0 if sign=='+' else MASS*MASS-s-qq+2*w*q0)
        deriv=(-1.0-q0/w if sign=='+' else -1.0+q0/w)
        out.append({
            'omega':w,'s':s,'D_at_root':D,
            'partial_s_D':deriv,'abs_partial_s_D':abs(deriv),
            'delta_pullback_weight_1_over_abs_partial_s_D':1.0/abs(deriv),
            'simple_root':abs(deriv)>TOL,
        })
    return sorted(out,key=lambda x:x['s'])

def main():
    closure=[sum(Q[x][mu] for x in LEGS) for mu in range(4)]
    closure_max=max(abs(x) for x in closure)
    rows=[]; failures=[]
    for leg in LEGS:
        for sign in ('+','-'):
            roots=roots_for(leg,sign)
            for r in roots:
                if abs(r['D_at_root'])>TOL: failures.append(f"root residual {leg}{sign}: {r['D_at_root']}")
                if not r['simple_root']: failures.append(f"non-simple root {leg}{sign}: {r['s']}")
            rows.append({
                'leg':leg,'denominator':f'D_{leg}^{sign}',
                'formula':('m^2-s-q_i^2-2sqrt(s)q_i^0' if sign=='+' else 'm^2-s-q_i^2+2sqrt(s)q_i^0'),
                'q0':Q[leg][0],'q2_source_signature_plus_minus_minus_minus':q2(Q[leg]),
                'positive_root_count':len(roots),'roots':roots,
                'classification':('NO_POSITIVE_ROOT' if not roots else 'POSITIVE_SIMPLE_ROOT_SUPPORT')
            })
    all_roots=[]
    for row in rows:
        for r in row['roots']:
            all_roots.append((r['s'],row['denominator']))
    all_roots.sort()
    min_sep=min((all_roots[i+1][0]-all_roots[i][0] for i in range(len(all_roots)-1)),default=float('inf'))
    if min_sep<=TOL: failures.append(f'coincident positive roots across denominator types: min separation {min_sep}')

    support={(r['leg'],r['denominator'][-1]):r['positive_root_count'] for r in rows}
    # Iter594 K1/K2 terms contain one D_i^- (pair first) and one D_i^+ (singleton first) per singleton.
    k1k2_supported=sum(1 for leg in LEGS for sign in ('+','-') if support[(leg,sign)]>0)
    # In each K1^3 permutation (i,j,k), the two nontrivial denominators are D_i^+ and D_k^-.
    import itertools
    chain_rows=[]
    for perm in itertools.permutations(LEGS):
        i,j,k=perm
        n=support[(i,'+')]+support[(k,'-')]
        chain_rows.append({'permutation':list(perm),'denominators':[f'D_{i}^+',f'D_{k}^-'],
                           'positive_root_occurrences':n,
                           'classification':'SUPPORTED' if n else 'NO_POSITIVE_ROOT'})
    if any(x['classification']!='SUPPORTED' for x in chain_rows):
        failures.append('unexpected unsupported K1^3 chain under frozen trajectory')

    classification=('PASS_ITER614_FROZEN_NATIVE_S_SCALAR_POLE_ROOT_AND_JACOBIAN_AUDIT__NON_RESIDUAL'
                    if not failures else 'FAIL_ITER614_FROZEN_NATIVE_S_SCALAR_POLE_ROOT_AND_JACOBIAN_AUDIT')
    result={
      'iteration':ITERATION,'date':'2026-09-08','model_readiness_percent':24,
      'classification':classification,'scientific_gate_pass':not failures,'failures':failures,
      'kinematic_contract':'MSSC001-NATIVE-S-KIN-V1 (frozen by Iter613 before root evaluation)',
      'metric_signature':'+---','mass':MASS,'q_vectors':Q,
      'q_squared_source_signature':{x:q2(Q[x]) for x in LEGS},
      'connection_sector_q2_labels_are_not_reused_as_source_signature_q2':True,
      'momentum_closure_max_abs':closure_max,
      'denominator_rows':rows,
      'support_summary':{
        'unique_denominator_types':6,
        'types_with_positive_support':sum(1 for r in rows if r['positive_root_count']>0),
        'types_without_positive_support':sum(1 for r in rows if r['positive_root_count']==0),
        'total_distinct_positive_root_points':len(all_roots),
        'minimum_positive_root_separation_in_s':min_sep,
        'all_positive_roots_simple':all(r['simple_root'] for row in rows for r in row['roots']),
        'K1K2_terms_with_positive_support_out_of_6':k1k2_supported,
        'K1cubed_chains_with_positive_support_out_of_6':sum(1 for x in chain_rows if x['classification']=='SUPPORTED'),
      },
      'K1cubed_chain_support':chain_rows,
      'distribution_pullback':'delta(D_A(s)) = sum_roots delta(s-s_r)/|partial_s D_A(s_r)| for the simple roots listed here',
      'all_13_source_families_retained':True,
      'K3_scalar_pole_note':'K3 is local in the Iter611 scalar-pole classification and adds no routed scalar denominator of this D_i^+/- class',
      'explicit_nonclaims':['no source numerator evaluated at a pole','no native Y/T_cut sign-normalization binding',
                            'no Source/Born subtraction','no comparator quotient','no Candidate residual','no novelty claim'],
      'zero_fill':False,'source_born_subtraction':'NOT_PERFORMED','candidate_residual':False,
      'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'readiness_change':'unchanged at 24%; pole-support/Jacobian prerequisite closes but no complete stable rubric sector',
      'next_gate_if_pass':'bind the supported distributional source tree, including numerator values and signs on every retained simple root, to the native Iter205 Y/T_cut convention and Iter582 operator normalization without Source/Born subtraction; preserve D_s^+ no-positive-root as support absence, not zero-filled amplitude'
    }
    out=Path(__file__).resolve().parents[1]/'results'
    out.mkdir(parents=True,exist_ok=True)
    (out/'iteration614_native_s_pole_root_jacobian_audit.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
