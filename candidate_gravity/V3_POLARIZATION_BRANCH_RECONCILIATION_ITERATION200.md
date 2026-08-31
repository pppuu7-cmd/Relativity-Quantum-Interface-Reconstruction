# RQIR Candidate Gravity — Iteration 200

## Reconciliation of concurrent v3 polarization branches

A repository concurrency event produced two independently prospectively frozen polarization realizations on the same `0.80/1.40` v3 hard-q geometry:

- **v3-A:** hourly automation seed stream, frozen before its cubic C5 evaluation;
- **v3-B:** concurrent manual seed stream, also frozen before its cubic C5 evaluation.

Neither branch used a Candidate Gravity target. They must therefore be preserved as two admissible observable protocols rather than choosing one post hoc.

## Both branches have the same theory-parameter rank

For each branch the zero-K2 local C5 soft2 map is

`V4 = Riemann3_soft2 * {1,-x,x^2,-x^3}`

and has rank `4/12`.

Conditioning differs:

- v3-A raw condition `1038.40`, column-normalized `981.36`;
- v3-B raw condition `4837.96`, column-normalized `4587.34`.

Thus polarization choice materially changes numerical geometry even at fixed hard q-nodes.

## Principal-angle comparison

Let `Q_A` and `Q_B` be orthonormal bases of the two rank-4 column spaces in the common twelve-row index representation. Singular values of `Q_A^T Q_B` give principal angles

`[1.3074°, 70.5977°, 76.7404°, 83.6588°]`.

Only one C5 direction is nearly common. The other three are strongly rotated.

Projector distances:

- Frobenius `||P_A-P_B||_F = 2.37712`;
- operator norm `||P_A-P_B||_2 = 0.993882`.

The union of the two alternate subspaces has rank 8 in the common 12-index representation. This **does not** mean eight C5 theory parameters; it measures how strongly two alternate row-functional choices rotate the four-parameter nuisance image.

## Interpretation

The deterministic seed is only a reproducibility mechanism. The resulting TT polarization is part of the physical observable definition. Two allowed polarization settings are therefore not interchangeable numerical nuisances.

There is no scientific contradiction between v3-A and v3-B. They are two different protocols probing the same four local C5 coefficients through different row functionals.

Post-hoc selection of the better-conditioned branch is forbidden for a future candidate claim. A robust candidate discriminator must be evaluated under separately frozen polarization protocols or under a new multi-polarization protocol frozen before candidate evaluation.

A diagnostic 24-row vertical stack of A and B, using the same four C5 coefficients, remains rank 4 with raw condition `1845.83` and column-normalized condition `1749.72`. It is not automatically superior and is **not** frozen here as a new protocol.

## Retained results

- `PROTO-NG-007 — ADMISSIBLE_TT_POLARIZATION_SETTINGS_DEFINE_DISTINCT_OBSERVABLE_PROTOCOLS_AND_MAY_NOT_BE_TREATED_AS_INTERCHANGEABLE_NUMERICAL_SEEDS`.
- `C5-NG-018 — TWO_PROSPECTIVELY_FROZEN_V3_POLARIZATION_PROTOCOLS_BOTH_HAVE_RANK4_BUT_THEIR_LOCAL_C5_NUISANCE_SUBSPACES_ARE_STRONGLY_ROTATED`.
- `REL-NG-013 — PRINCIPAL_ANGLES_SHOW_ONLY_ONE_NEAR_COMMON_C5_DIRECTION_BETWEEN_V3_A_AND_V3_B`.
- `NG-FUNNEL-054 — COMPARATOR_QUOTIENT_AUTHORITY_MUST_INCLUDE_POLARIZATION_SETTINGS_AS_PART_OF_THE_ROW_DEFINITION_BEFORE_RESIDUAL_TESTING`.

`MODEL_READINESS: 24%` — unchanged. AS/C3 remain BLOCKED and no candidate residual exists.
