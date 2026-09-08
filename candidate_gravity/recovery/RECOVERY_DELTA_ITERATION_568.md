# RECOVERY DELTA — Iteration 568

**Date:** 2026-09-08

## New exact authority
Iteration568 freezes the coordinate-wise variance-leverage map of the Iteration-424 QUARTER central4 tensor stencil.

Classification:
`PASS_ITER424_QUARTER_COORDINATE_VARIANCE_LEVERAGE_MAP_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`

Files:
- `candidate_gravity/code/iteration568_iter424_quarter_coordinate_variance_leverage_exact.py`
- `candidate_gravity/results/iteration568_iter424_quarter_coordinate_variance_leverage_exact.json`
- `candidate_gravity/research_log/2026-09-08_iteration_568.md`

Exact facts:
- `C=w⊗w`, `w=[1,-8,+8,-1]`;
- `||C||_F^2=16900`;
- iid equal-variance coordinate leverage is `C_ij^2/16900`;
- four central `(±h,±h)` points carry `4096/4225 ≈96.946746%` of iid assembled variance;
- eight edge points carry `128/4225 ≈3.029586%`;
- four corners carry `1/4225 ≈0.023669%`;
- each final rank11/rank12 coordinate carries `16/4225`, pair `32/4225 ≈0.757396%`.

This is conditioning-only. It does not alter precision/support/frozen order or physical thresholds and cannot be used to omit low-leverage coordinates.

## Authority state at freeze
- latest raw support: rank10 Iteration565 PASS;
- QUARTER new coordinates raw-closed: `10/12 = 83.333333%`;
- full grid including 4 HALF overlaps: `14/16 = 87.5%`;
- rank11 run `34168897005`, job `101885271903` remained active;
- only raw-valid rank11 PASS can authorize rank12;
- `MODEL_READINESS=24%` unchanged;
- physical index2 unresolved;
- `ANSATZ-003` absent; Fisher/resources forbidden.
