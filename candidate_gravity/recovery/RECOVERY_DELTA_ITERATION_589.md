# RECOVERY DELTA — RQIR Candidate Gravity Iteration 589

Date: 2026-09-08

## New authoritative result
Iteration 589 closes the relative-normalization ambiguity between the frozen MSSC-001 K1 source vertex and the raw-valid Iter584 mixed K2 contact before any nonlinear Ward cancellation is attempted.

Common parent inverse kernel:

`K[g]=-p'_cov (sqrt(-g) g^-1) p_cov + m^2 sqrt(-g)`, with `eta=(+---)`, `m=0.7`.

Derived from the same kernel:

`K1(h;p',p)=(1/2) h_{mu nu} V^{mu nu}(p',p)`

and

`K2(h1,h2;p',p)=-p'_cov bt(h1,h2) p_cov + m^2 bs(h1,h2)`.

Thus the relative K1/K2 sign and factor are fixed by one dynamics; independent tuning is forbidden.

## Provenance / raw authority
- Iter588 fixture-binding authority: singleton `s/a/b` + complementary mixed K2 pair, both block orientations retained.
- prospective Iter589 script commit: `c9f4b337a298b656bf0c3181a55b80b2dc52c6c5`;
- workflow commit: `50146e43c520a29812eec430cd1143f150b3c652`;
- canonical run: `34209731847`;
- artifact: `10049270625`;
- raw result SHA256: `90cd8591f34deb9a7c0d49a21d554bc8f776c5c2fdbef30cbcd88455b2a0dfad`;
- audit: `PASS_RAW_AUTHORITY_AUDIT_ITER589_K1_K2_NORMALIZATION`, failures `[]`.

Checks: max `|K1-(1/2)h.V|=1.1102230246251565e-16`; max pure-gauge Ward mismatch `3.552713678800501e-15`; frozen tolerance `2e-12`.

Exact classification:

`PASS_MSSC001_K1_K2_SAME_ACTION_NORMALIZATION_CONTRACT__NON_RESIDUAL`.

This is not a full Ward cancellation, source-tree value, comparator identity/residual, model-level non-identifiability, near-degeneracy, novelty certificate, or Candidate-Gravity consistency PASS/FAIL.

Source/Born subtraction: NOT PERFORMED.
ANSATZ-003: FORBIDDEN.
Fisher/resources: FORBIDDEN.

## Readiness
MODEL_READINESS: 24%

Change: 0 percentage points. The normalization hard constraint is now frozen and raw-valid, but no complete readiness-rubric sector closed; robust unique residual remains absent.

## Exact next gate
Assemble the complete same-fixture `K1-G-K2 + K2-G-K1` source response using exactly the Iter589 normalization, Iter588 singleton/pair routing, both block orientations, and Iter584 mixed contact. Test the off-shell Ward identity including the Iter587 inverse-propagator RHS. Only a valid completed source/Ward object may be mapped to Iter582 and then enter the unchanged fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
