# Candidate Gravity article / negative-results matrix — Iteration 267

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## New scoped result

The Iteration-266 exact reduction of the null-soft physical cubic `B3[s,a,b]` to 8 independent transpose classes is now supplemented by an exact condensed-index/Fourier momentum-support certificate.

Every polarized coefficient carries the sum of its background Fourier momenta. Hence all 8 independent cubic representatives map `p -> p+K`, where `K=k_s+k_a+k_b`. `Q0` carries no background shift but must be evaluated at the routed orbit momentum at its insertion.

Freeze:

`PASS_EXACT_B3_CONDENSED_INDEX_MOMENTUM_SUPPORT`.

The full operator transpose exchanges kernel endpoints. Therefore the seven Iteration-266 transpose partners cannot be implemented as raw finite-dimensional transposes at unchanged `p` and unchanged `+k` legs. In canonical forward orientation they live in the `-K` routed sector; for real backgrounds this is supplied by the conjugate `-k` Fourier modes.

Guardrail:

`NO_FIXED_PLUS_K_MATRIX_TRANSPOSE_AS_KERNEL_TRANSPOSE`.

## Article-use classification

Potentially publishable as a methodological/negative-result component of the Candidate Gravity comparator construction: a superficially plausible local-matrix implementation of the Vilkovisky cubic numerator is insufficient because it can violate condensed-index momentum support while still producing a nonzero number. The result prevents false-positive C5 numerator claims.

Do not state that this proves a nonzero C5 coordinate or any new gravity model. It is not a consistency FAIL, comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

## Funnel status

- C3: retained formal nonlinear conserved-completion underdetermination blocker.
- C4: retained mediator-degenerate positive two-point information.
- C5: operationally BLOCKED, NOT ZERO; operator routing is now frozen before explicit numerator construction.
- nonlocal / asymptotic-safety comparator routes: unchanged frozen state.
- Candidate residual: absent.
- `ANSATZ-003`: not created.
- Fisher/resources: forbidden.

MODEL_READINESS: 24%

Change from Iteration 266: 0 percentage points; this iteration improves validity/provenance of the C5 construction but does not close a readiness rubric block.
