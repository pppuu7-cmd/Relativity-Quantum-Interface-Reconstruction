# RECOVERY DELTA — Iteration 619

Date: 2026-09-08

## Authoritative result

`PASS_ITER619_CONSUMED_ITER615_INDEPENDENT_REPRESENTATION_PROJECTIVE_REPRODUCIBILITY__DIAGNOSTIC_ONLY_NON_PROMOTING`

Iteration 619 compares the Iter618 projective ratios derived from the canonical Iter615 machine result against the independent Iter615 representation already preserved in `RECOVERY_DELTA_ITERATION_615.md`.

No new acceptance threshold is introduced; this is a reproducibility consumption of an already-authoritative independent cross-check.

## Observed projective agreement

Canonical ratios:

`[1, -2.966563737084728, -0.7800526753639322, -5.158207913624242, 2.997420912767025, 8.57973421373656]`.

Independent recovery ratios:

`[1, -2.966563737084729, -0.7800526753639321, -5.158207913624242, 2.9974209127670246, 8.579734213736554]`.

Maximum absolute ratio difference: `5.329070518200751e-15`.

Maximum relative ratio difference: `6.211230307890725e-16`.

The Iter618 normalization-invariant source shape is therefore reproduced at the floating-point level by the independent Iter615 representation.

## Scope

Diagnostic only / non-promoting. `N_native` remains BLOCKED. No roots are summed. Source/Born subtraction remains `NOT_PERFORMED`; comparator quotient remains blocked; no ANSATZ-003; no Fisher/resources.

## Reproducibility

- code: `candidate_gravity/code/iteration619_projective_independent_representation_reproducibility.py`
- result: `candidate_gravity/results/iteration619_projective_independent_representation_reproducibility.json`
- log: `candidate_gravity/research_log/2026-09-08_iteration_619.md`

MODEL_READINESS: 24%

Readiness change from Iter618: `0 pp`.
