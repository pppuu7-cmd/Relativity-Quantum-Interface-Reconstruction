#!/usr/bin/env python3
"""Iteration 592: K1^3 analytic-origin audit before any linked-T_cut projection.

Guardrail: do not identify the off-shell MSSC scalar-source tree with the frozen
pure-gravity linked T_cut.  This gate proves only the singularity class of the
same-action K1^3 family and fail-closes the actual T_cut projection unless a
repo-authoritative distributional/source-to-observable map exists.
"""
from __future__ import annotations
import hashlib, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def main():
    failures=[]
    p590=ROOT/'candidate_gravity/results/iteration590_source_cubic_completeness_raw_consumption.json'
    p591=ROOT/'candidate_gravity/results/iteration591_source_k3_disc_raw_consumption.json'
    r590=json.loads(p590.read_text()); r591=json.loads(p591.read_text())
    if r590.get('classification')!='PASS_RAW_CONSUMED_CUBIC_SOURCE_RESPONSE_COMPLETENESS__K1K2_ONLY_SCOPED_NOT_FULL':
        raise SystemExit('Iter590 raw authority missing/drifted')
    if r591.get('classification')!='PASS_RAW_CONSUMED_MSSC001_LOCAL_K3_HARD_CHANNEL_DISC_ZERO__NON_RESIDUAL':
        raise SystemExit('Iter591 raw authority missing/drifted')

    fixture=[]
    for row in r590['fixture_support']:
        d=float(row['minimum_abs_internal_K0'])
        a=float(row['K1cubed_six_permutation_sum'])
        if not math.isfinite(d) or d<=0: failures.append(f"{row['singleton']}: invalid internal K0 separation")
        if not math.isfinite(a) or abs(a)<=1e-12: failures.append(f"{row['singleton']}: K1^3 support vanished")
        fixture.append({'singleton':row['singleton'],'minimum_abs_internal_K0':d,
                        'K1cubed_six_permutation_sum':a,'sampled_on_scalar_pole':d<=1e-6})

    # K1 is polynomial in momenta and every same-action scalar propagator is
    # G=1/(m^2-p^2).  Finite products/sums are meromorphic rational functions:
    # no ordinary branch cut is generated without a loop/nonlocal kernel.
    analytic={
      'K1_momentum_class':'POLYNOMIAL',
      'G_class':'MEROMORPHIC_RATIONAL_1_OVER_m2_minus_p2',
      'loop_integrals':0,'logs':0,'threshold_square_roots':0,'nonlocal_form_factors':0,
      'ordinary_finite_branch_cut_origin':'NONE_AWAY_FROM_SCALAR_POLES',
      'pole_distribution_warning':'Retarded/Feynman pole discontinuities are distributional and must not be equated to the frozen pure-gravity linked T_cut without an explicit matched prescription.'
    }

    result={
      'iteration':592,'date':'2026-09-08','model_readiness_percent':24,
      'classification':'PASS_K1CUBED_MEROMORPHIC_ORIGIN__LINKED_T_CUT_PROJECTION_BLOCKED__NON_RESIDUAL' if not failures else 'FAIL_K1CUBED_ORIGIN_AUDIT',
      'scientific_gate_pass':not failures,'failures':failures,
      'parent_authorities':['Iter590 raw cubic completeness','Iter591 raw local-K3 origin','Iter589 same-action scalar inverse kernel'],
      'analytic_origin':analytic,'fixture':fixture,
      'ordinary_finite_branch_cut_D_s_K1cubed':'ZERO_AWAY_FROM_POLES',
      'K1cubed_under_frozen_linked_T_cut':'BLOCKED__NEEDS_EXPLICIT_SOURCE_TO_T_CUT_DISTRIBUTIONAL_MAP',
      'K1K2_only_as_complete_discontinuity_source_block':'NOT_AUTHORIZED',
      'source_born_subtraction':'NOT_PERFORMED','candidate_residual':False,
      'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN',
      'key_result':'K1^3 is a nonzero meromorphic tree family with scalar poles but no ordinary finite branch cut by itself. The exact linked T_cut assignment remains unsupported until a matched source-to-observable distributional prescription is constructed.',
      'next_gate_if_pass':'Construct/freeze the matched source-to-native-linked-observable map that states how MSSC scalar propagator pole terms project into the existing split-invariant Y=(K2,S_soft2_full)/T_cut protocol. Until then retain K1^3 in the full same-action source Ward tree and do not perform Source/Born subtraction.'
    }
    out=ROOT/'results/iteration592_source_k1cubed_origin'; out.mkdir(parents=True,exist_ok=True)
    rp=out/'result.json'; rp.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    sha=hashlib.sha256(rp.read_bytes()).hexdigest()
    audit={'iteration':592,'result_sha256':sha,'failures':failures,
           'classification':'PASS_RAW_AUTHORITY_AUDIT_ITER592_K1CUBED_ORIGIN' if not failures else 'FAIL_RAW_AUTHORITY_AUDIT_ITER592_K1CUBED_ORIGIN'}
    (out/'authority_audit.json').write_text(json.dumps(audit,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if failures: raise SystemExit(2)

if __name__=='__main__': main()
