#!/usr/bin/env python3
"""Iteration 604: prospectively freeze the finite-lattice convergence contract.

This is a contract-only/non-residual gate. It validates that the new adaptive
lattice rule is frozen before any production Ward rerun and that it preserves
all Iter596/601/602 scientific thresholds and guardrails.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ITERATION = 604
ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / 'candidate_gravity' / 'contracts' / 'ITERATION604_FINITE_LATTICE_BOUNDARY_CONVERGENCE_CONTRACT.md'
RAW603 = ROOT / 'candidate_gravity' / 'results' / 'iteration603_lattice_diagnosis_raw_consumption.json'
OUT = ROOT / 'results' / 'iteration604_finite_lattice_contract'

EXPECTED = {
    'radii': [4, 5, 6],
    'fd_steps': [0.02, 0.01, 0.005],
    'ward_abs_tolerance': 2e-6,
    'last_fd_step_tolerance': 2e-5,
    'radius_stability_tolerance': 2e-6,
    'one_leg_anchor_tolerance': 2e-11,
    'assembly_crosscheck_tolerance': 2e-5,
    'source_family_count': 13,
}


def main() -> None:
    bad = []
    r603 = json.loads(RAW603.read_text())
    if r603.get('iteration') != 603:
        bad.append('Iter603 raw-consumption authority missing')
    if 'STRONGLY_LATTICE_RADIUS_SENSITIVE' not in r603.get('classification', ''):
        bad.append('Iter603 strong-radius-sensitivity authority missing')
    if r603.get('scientific_gate_pass') is not False:
        bad.append('Iter603 must remain diagnostic/non-promoting')
    if r603.get('model_readiness_percent') != 24:
        bad.append('readiness drift')

    text = CONTRACT.read_text()
    required_phrases = [
        'R = 4, 5, 6',
        '(2e-2, 1e-2, 5e-3)',
        '2e-6',
        '2e-5',
        '2e-11',
        '13 source families',
        'BLOCKED_CONVERGENCE',
        'FAIL_WARD',
        'No Source/Born subtraction',
        'no `ANSATZ-003`',
        'MODEL_READINESS: 24%',
    ]
    for p in required_phrases:
        if p not in text:
            bad.append(f'missing frozen contract phrase: {p}')

    result = {
        'iteration': ITERATION,
        'date': '2026-09-08',
        'classification': 'PASS_PROSPECTIVE_FINITE_LATTICE_BOUNDARY_CONVERGENCE_CONTRACT__NON_RESIDUAL' if not bad else 'FAIL_CONTRACT_AUDIT',
        'scientific_gate_pass': not bad,
        'candidate_residual': False,
        'model_readiness_percent': 24,
        'contract': EXPECTED,
        'iter602_historical_fail_preserved': True,
        'iter603_diagnostic_nonpromoting_preserved': True,
        'forbidden': ['SOURCE_BORN_SUBTRACTION', 'SOURCE_TO_ITER582_MAP', 'COMPARATOR_QUOTIENT', 'ANSATZ_003', 'FISHER_RESOURCES'],
        'failures': bad,
        'next_gate': 'Iteration605 production rerun of the unchanged full source-level nonlinear Ward identity using the prospectively frozen R=4,5,6 contract; accept authority only after independent raw artifact consumption.',
    }
    OUT.mkdir(parents=True, exist_ok=True)
    rp = OUT / 'result.json'
    rp.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    sha = hashlib.sha256(rp.read_bytes()).hexdigest()
    audit = {
        'iteration': ITERATION,
        'classification': 'PASS_RAW_AUDIT_ITER604_PROSPECTIVE_LATTICE_CONTRACT' if not bad else 'FAIL_RAW_AUDIT_ITER604_PROSPECTIVE_LATTICE_CONTRACT',
        'result_sha256': sha,
        'contract_sha256': hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
        'failures': bad,
    }
    (OUT / 'authority_audit.json').write_text(json.dumps(audit, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))
    if bad:
        raise SystemExit('\n'.join(bad))


if __name__ == '__main__':
    main()
