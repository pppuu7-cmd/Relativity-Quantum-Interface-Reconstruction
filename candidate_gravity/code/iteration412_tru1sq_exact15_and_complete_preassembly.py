#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 412 prospective fail-closed preassembly.

This script is intentionally frozen *before* Iteration-411 physical results are
accepted.  It assembles the 15-channel double-double Tr(U1^2) sector only from
raw scientifically valid CONVERGED channel JSON records.  It refuses duplicate
indices, missing indices, wrong q^2 buckets, BLOCKED_CONVERGENCE records,
scientific_gate_pass=False, or non-finite channel coordinates.

After exact 15/15 closure it combines only the already-authoritative
Iteration-374 simple-simple and Iteration-393 simple-double q^2 coordinates to
produce the complete Tr(U1^2) operator coordinate.  No -i/4 effective-action
weight is folded here.  Distinct q^2 buckets are never summed.

Usage:
  python candidate_gravity/code/iteration412_tru1sq_exact15_and_complete_preassembly.py raw/*.json

The 15 paths may mix Iteration-389 ordinary raw channel records and later
raw-authoritative targeted recovery records (e.g. Iterations 399/407/411), but
each record must identify exactly one frozen double-double global index.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

ITERATION = 412
EXPECTED_Q2 = {
    **{i: -1.0 for i in range(0, 5)},
    **{i: -0.14 for i in range(5, 10)},
    **{i: -0.34 for i in range(10, 15)},
}
QKEY = {-1.0: '-1.0', -0.34: '-0.34', -0.14: '-0.14'}
SIMPLE_SIMPLE = {
    '-1.0': 6.253219881951187e-05,
    '-0.34': 3.5044107116946374e-05,
    '-0.14': 2.9297648005638963e-05,
}
SIMPLE_DOUBLE = {
    '-1.0': -0.002329411286740447,
    '-0.34': -0.0005948791870822445,
    '-0.14': -7.368142632096214e-05,
}


def scaled_equal(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def extract_record(path: Path) -> dict:
    raw = json.loads(path.read_text())
    if raw.get('scientific_gate_pass') is not True:
        raise RuntimeError(('scientific_gate_not_pass', str(path), raw.get('scientific_gate_pass')))
    ch = raw.get('channel')
    if not isinstance(ch, dict):
        raise RuntimeError(('missing_channel_object', str(path)))

    # Iteration 389 stores the frozen global index at top level; targeted
    # analytic/spectral recoveries store it inside channel.
    idx = ch.get('double_double_global_index', raw.get('channel_index'))
    if not isinstance(idx, int) or idx not in EXPECTED_Q2:
        raise RuntimeError(('invalid_or_missing_frozen_index', str(path), idx))

    status = ch.get('status')
    if status != 'CONVERGED':
        raise RuntimeError(('nonconverged_record_forbidden', str(path), idx, status))

    q2 = float(ch.get('q_squared'))
    if not scaled_equal(q2, EXPECTED_Q2[idx]):
        raise RuntimeError(('q2_bucket_drift', str(path), idx, q2, EXPECTED_Q2[idx]))

    coord = ch.get('D_s_TrU1sq_double_double_channel')
    if not (isinstance(coord, list) and len(coord) == 2):
        raise RuntimeError(('missing_channel_coordinate', str(path), idx, coord))
    re, im = float(coord[0]), float(coord[1])
    if not (math.isfinite(re) and math.isfinite(im)):
        raise RuntimeError(('nonfinite_channel_coordinate', str(path), idx, coord))

    return {
        'index': idx,
        'q_squared': q2,
        'value': complex(re, im),
        'iteration': raw.get('iteration'),
        'classification': raw.get('classification'),
        'source_path': str(path),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('records', nargs='+', type=Path)
    args = ap.parse_args()

    records = [extract_record(p) for p in args.records]
    by_index = {}
    for rec in records:
        idx = rec['index']
        if idx in by_index:
            raise RuntimeError(('duplicate_frozen_index', idx, by_index[idx]['source_path'], rec['source_path']))
        by_index[idx] = rec

    missing = sorted(set(EXPECTED_Q2) - set(by_index))
    extra = sorted(set(by_index) - set(EXPECTED_Q2))
    if missing or extra or len(by_index) != 15:
        raise RuntimeError(('exact15_required', {'missing': missing, 'extra': extra, 'count': len(by_index)}))

    dd = {'-1.0': 0j, '-0.34': 0j, '-0.14': 0j}
    counts = {k: 0 for k in dd}
    provenance = []
    for idx in range(15):
        rec = by_index[idx]
        key = QKEY[EXPECTED_Q2[idx]]
        dd[key] += rec['value']
        counts[key] += 1
        provenance.append({
            'index': idx,
            'q_squared': EXPECTED_Q2[idx],
            'iteration': rec['iteration'],
            'classification': rec['classification'],
            'source_path': rec['source_path'],
        })

    if counts != {'-1.0': 5, '-0.34': 5, '-0.14': 5}:
        raise RuntimeError(('q2_count_drift', counts))

    complete = {}
    for key in ('-1.0', '-0.34', '-0.14'):
        val = complex(SIMPLE_SIMPLE[key], 0.0) + complex(SIMPLE_DOUBLE[key], 0.0) + dd[key]
        complete[key] = [float(val.real), float(val.imag)]

    out = {
        'iteration': ITERATION,
        'date': '2026-09-04',
        'classification': 'PASS_TRU1SQ_EXACT15_DOUBLE_DOUBLE_AND_COMPLETE_OPERATOR_COORDINATE_PREASSEMBLY',
        'scientific_gate_pass': True,
        'candidate_residual': False,
        'exact_double_double_channel_count': 15,
        'double_double_q2_counts': counts,
        'D_s_TrU1sq_double_double_q2': {k: [float(v.real), float(v.imag)] for k, v in dd.items()},
        'components': {
            'simple_simple_iteration': 374,
            'simple_simple_q2': SIMPLE_SIMPLE,
            'simple_double_iteration': 393,
            'simple_double_q2': SIMPLE_DOUBLE,
            'double_double_records': provenance,
        },
        'D_s_TrU1sq_complete_q2': complete,
        'effective_action_weight': 'NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE',
        'model_readiness_percent': 24,
        'guardrails': [
            'EXACT_15_UNIQUE_DOUBLE_DOUBLE_INDICES_REQUIRED',
            'ONLY_RAW_AUTHORITY_CONVERGED_RECORDS_ALLOWED',
            'NO_BLOCKED_DIAGNOSTIC_VALUE_IN_SUM',
            'NO_ZERO_FILL',
            'EXACT_FIVE_CHANNELS_PER_Q2_BUCKET',
            'DISTINCT_Q2_BUCKETS_NEVER_SUMMED',
            'NO_EFFECTIVE_ACTION_WEIGHT_FOLDING',
            'NO_ANSATZ003',
            'NO_FISHER_RESOURCES',
        ],
        'next_gate': 'after raw authority validation of this exact15 assembly, combine q2-by-q2 with Iteration406 TrU2 using +(i/2)TrU2-(i/4)TrU1sq; then proceed to Source/Ward/contact + matched K2 and fixed comparator quotient',
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
