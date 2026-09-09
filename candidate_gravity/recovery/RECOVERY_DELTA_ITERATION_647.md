# RECOVERY DELTA — Iteration 647

Date: 2026-09-09

Authoritative predecessor: Iter646 narrowed the closed-CTP normalization ambiguity to one common global factor and required a strictly pre-Iter645 provenance search.

## New authority

A full-snapshot fail-closed audit was pinned to authoritative Iter644 commit `a86b41cfc4e90d65073faa872b8cfa1b85f29193`, before Iter645 reduced values existed. It scanned 1566 tracked `candidate_gravity/` files for a same-parent chain explicitly binding `W=-i ln Z`, the CTP Legendre map, the real-scalar Gaussian global determinant prefactor, Fourier/loop measure, and native Gamma3 normalization.

No complete bridge exists. The pinned snapshot contains zero explicit `W=-i ln Z` hits. Separate loop-measure and i/2-like determinant formulas are present elsewhere, so the negative result is specifically a normalization-bridge provenance gap, not a claim that standard formulas are absent from the repository.

Exactly one common nonzero global scalar factor remains unbound. No root-, family-, q2-, or s-dependent factor is permitted. For this already-evaluated absolute observable branch the gap is permanent: no post-result choice of `i/2`, `+/-i`, or fitted constant may repair it.

Canonical Action `34309801822` succeeded; job `102333928118`; artifact `10087937807`; digest `sha256:b47ad24b181b07c9f7d9a22bea238b9d7693dae60a04cc4e4ad3563908856e76`. Raw artifact consumed.

Classification:
`BLOCKED_ITER647_PERMANENT_PRE645_NORMALIZATION_PROVENANCE_GAP__ONE_GLOBAL_FACTOR_UNBOUND__NON_RESIDUAL`.

This is operational/provenance BLOCKED, not consistency FAIL/PASS, exact comparator identity, regime-specific non-identifiability, near-degeneracy, novelty certificate, or Candidate residual.

Guardrails unchanged: Candidate values unused; `zero_fill=false`; Source/Born subtraction `NOT_PERFORMED`; native Y/T_cut projection `NOT_PERFORMED`; comparator quotient `NOT_PERFORMED`; no ANSATZ-003/Fisher/resources.

MODEL_READINESS: 24%
Readiness change: 0 percentage points. A permanent provenance classification is now closed, but robust unique residual remains `0/20`.

Exact next gate — Iter648: prospectively define, without reading Iter645 values, a projective/ratio observable invariant under multiplication of all reduced amplitudes by the one common nonzero complex factor; prove algebraic cancellation and domain conditions before any numerical evaluation.
