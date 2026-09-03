#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 307.

Combine the two independently schema-valid actual weight-completed Tr U1
subsectors at the frozen timelike row:
  Iteration 302: four ordinary/raised bubble normalized cuts;
  Iteration 305: four ordinary/raised triangle normalized cuts.

No new loop integration occurs here. This is a provenance-locked authority
combination for the complete eight-family e=1,c=2 Tr U1 normalized cut.
The effective-action prefactor -i/2 is intentionally NOT applied here.
"""
import argparse, hashlib, json
from pathlib import Path

EXPECTED_302_SHA='d208274134a1b434b177f11c1fd4c5fb1cd078d5ee0687f1c0f945bf1b5298aa'
EXPECTED_305_SHA='82aac90c180e6da3e2f068b86aef5c5c821938f54d01751361576a9f464c0650'


def load_pair(result_path,audit_path,iteration,expected_sha,expected_class):
    b=Path(result_path).read_bytes()
    sha=hashlib.sha256(b).hexdigest()
    r=json.loads(b)
    a=json.loads(Path(audit_path).read_text())
    assert sha==expected_sha,(iteration,sha,expected_sha)
    assert r['iteration']==iteration
    assert r['classification']==expected_class
    assert r['candidate_residual'] is False
    assert r['model_readiness_percent']==24
    assert a['scientific_authority_pass'] is True
    assert a['expected_iteration']==iteration
    assert a['found_iterations']==[iteration]
    assert a['top_level_object_count']==1
    assert a['sha256']==expected_sha
    return r,a


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--iteration302',default='iteration302_source/iteration302_result.json')
    ap.add_argument('--iteration302-audit',default='iteration302_source/iteration302_authority_audit.json')
    ap.add_argument('--iteration305',default='iteration305_source/iteration305_result.json')
    ap.add_argument('--iteration305-audit',default='iteration305_source/iteration305_authority_audit.json')
    args=ap.parse_args()

    r302,a302=load_pair(
      args.iteration302,args.iteration302_audit,302,EXPECTED_302_SHA,
      'PASS_ACTUAL_WEIGHT_COMPLETED_TRU1_BUBBLE_NORMALIZED_CUT_SUBSECTOR_PROMOTED_IN_HV_SCOPE')
    r305,a305=load_pair(
      args.iteration305,args.iteration305_audit,305,EXPECTED_305_SHA,
      'PASS_ACTUAL_DIRECT_TIMELIKE_WEIGHT_COMPLETED_TRU1_TRIANGLE_NORMALIZED_CUT_FINITE_IN_HV_SCOPE')

    bcut=float(r302['sum_four_bubble_normalized_cut'])
    tcut=float(r305['sum_four_triangle_normalized_cut'])
    bpole=float(r302['sum_four_bubble_cut_pole_residue'])
    tpole=float(r305['sum_four_triangle_cut_one_over_eps_residue'])
    total=bcut+tcut
    pole=bpole+tpole

    # Cross-check exact eight-family coverage.
    assert len(r302['four_bubble_cut_coefficients'])==4
    assert len(r305['triangle_families'])==4
    assert abs(total-(-0.5157080054161807))<2e-12
    assert abs(pole-1.2896746939995822e-09)<2e-16
    assert max(abs(bpole),abs(tpole),abs(pole))<2e-8

    result={
      'iteration':307,
      'model_readiness_percent':24,
      'classification':'PASS_COMPLETE_WEIGHT_COMPLETED_TRU1_E1C2_EIGHT_FAMILY_NORMALIZED_CUT_AT_FROZEN_TIMELIKE_ROW',
      'candidate_residual':False,
      'frozen_external_row':r302['frozen_external_row'],
      'subsectors':{
        'bubble':{
          'iteration':302,
          'normalized_cut':bcut,
          'cut_one_over_eps_residue':bpole,
          'family_count':4,
          'scientific_json_sha256':EXPECTED_302_SHA,
          'run_id':33701297866,
          'artifact_id':9873604163,
          'artifact_digest':'sha256:1651521730f1cbb773507535947892ee18365d2055e968c5fd6ca03caea1d7b4'
        },
        'triangle':{
          'iteration':305,
          'normalized_cut':tcut,
          'cut_one_over_eps_residue':tpole,
          'family_count':4,
          'scientific_json_sha256':EXPECTED_305_SHA,
          'run_id':33703120855,
          'artifact_id':9874241096,
          'artifact_digest':'sha256:576a5597881b41cee0c3fc271459ebbc50df6c59d98ca2076e323777230e3895'
        }
      },
      'complete_e1c2_tru1_family_count':8,
      'complete_e1c2_tru1_normalized_cut':total,
      'complete_e1c2_tru1_cut_one_over_eps_residue':pole,
      'effective_action_prefactor_applied':False,
      'statement':'The complete eight-family weight-completed e=1,c=2 Tr U1 normalized discontinuity at the frozen timelike row is now executable and nonzero in the common HV-like CUT scope certified by Iterations 301 and 304.',
      'guardrails':[
        'THIS_IS_TRU1_ONLY_NOT_THE_COMPLETE_C5_GAMMA3',
        'DO_NOT_APPLY_OR_HIDE_THE_MINUS_I_OVER_2_EFFECTIVE_ACTION_PREFACTOR_INSIDE_THIS_TRU1_COORDINATE',
        'E2_C_LE1_AND_DETERMINANT_E0_C_LE3_SECTORS_REMAIN_OPEN',
        'SOURCE_WARD_CONTACT_AND_MATCHED_K2_LINKED_COMPLETION_REMAIN_OPEN',
        'FULL_FINITE_AMPLITUDE_SCHEME_REMAINS_SEPARATELY_BLOCKED',
        'NO_COMPARATOR_SUBTRACTED_RESIDUAL_NO_ANSATZ003_NO_FISHER_OR_RESOURCES'
      ],
      'next_gate':'freeze the exact e=2,c<=1 composite connection operator/trace placement for Tr U2 and Tr U1^2, including all background-order partitions needed for the null-soft cubic observable, before any scoped numerator computation.'
    }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
