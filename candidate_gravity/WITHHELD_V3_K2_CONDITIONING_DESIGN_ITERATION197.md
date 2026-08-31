# RQIR Candidate Gravity — Iteration 197

## Target-independent K2 conditioning design

The rank-7 hard K2 separation is already structural (Iteration 196). This iteration improves numerical conditioning without using any candidate target.

### Frozen design rule

Reuse the six base hard q-vectors. Search a deterministic two-scale grid:

- low scale: `0.60,0.65,...,0.90`;
- high scale: `1.10,1.15,...,1.40`.

Require all 12 hard values to satisfy the internal design window

`0.10 <= x=q^2 <= 1.00`.

For each valid pair form the supported hard matrix

`A7=[x,x^2,...,x^6,x^2 exp(x)]`.

Objective: minimize the condition number after column normalization. Tie-break by the raw condition number. No candidate residual, candidate amplitude, soft2 value or left-null enters the design.

### Selected prospective K2 geometry

The best of 49 valid grid pairs is

`low_scale=0.80`, `high_scale=1.40`.

The 12 hard x values are

`[0.324864,0.246656,0.27264,0.201792,0.256256,0.184448,0.994896,0.755384,0.83496,0.617988,0.784784,0.564872]`.

All hard nodes remain positive and all partner legs remain spacelike on the same `epsilon in [-0.01,0.01]` 81-point geometry window. Partner `q^2` range is approximately `[0.179488,0.997136]`.

### Conditioning improvement

For withheld-v2:

- raw condition number `2.04935e7`;
- column-normalized condition number `2.38767e7`;
- raw smallest singular value `1.39038e-7`.

For v3 K2 geometry:

- raw condition number `6.36910e6`;
- column-normalized condition number `7.77614e6`;
- raw smallest singular value `7.87933e-7`.

Thus v3 improves

- raw condition number by factor `3.2176`;
- column-normalized condition number by factor `3.0705`;
- raw smallest singular value by factor `5.6670`.

The block remains near-degenerate and this is not finite-noise identifiability.

### Freeze boundary

`RQIR-WITHHELD-NULLSOFT-12-v3-K2-FROZEN` is now frozen **before** any cubic polarization selection or any candidate evaluation. The next step must freeze the v3 polarization geometry using a target-independent rule before computing cubic C5/nonlocal observables.

### Retained results

- `NUM-NG-011 — TARGET_INDEPENDENT_SCALE_DESIGN_IMPROVES_SUPPORTED_HARD_K2_CONDITIONING_WITHOUT_USING_CANDIDATE_INFORMATION`.
- `PROTO-NG-004 — WITHHELD_V3_K2_GEOMETRY_IS_FROZEN_BEFORE_CUBIC_POLARIZATION_OR_CANDIDATE_EVALUATION`.
- `NG-FUNNEL-051 — CONDITIONING_OPTIMIZATION_MAY_USE_FIXED_COMPARATOR_GEOMETRY_BUT_NOT_FUTURE_CANDIDATE_RESIDUALS`.

`MODEL_READINESS: 24%` — unchanged.
