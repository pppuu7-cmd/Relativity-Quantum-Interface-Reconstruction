# RQIR Candidate Gravity — Iteration 210

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Objective

Turn the Iteration-209 regular+log soft basis into an executable, target-independent numerical protocol before importing any physical loop comparator.

At one loop through soft order `n=2`, after factoring/subtracting the observable-specific leading soft pole, use

\[
F(\epsilon)=a_0+b_0L+z(a_1+b_1L)+z^2(a_2+b_2L),
\]

where

\[
z=\epsilon/\epsilon_{\max},\qquad
L=\log(\epsilon/\epsilon_{\rm ref}).
\]

## Frozen grid

Use 12 geometric soft points from

`epsilon_max = 0.04`

to

`epsilon_min = 0.0003125`,

with dynamic range `128` and

`epsilon_ref = sqrt(epsilon_min epsilon_max) = 0.0035355339059...`.

The grid is selected from basis conditioning only; no physical C5 or Candidate Gravity target enters its construction.

## Rank and conditioning

The design matrix

`[1, L, z, zL, z^2, z^2L]`

has shape `12 x 6`, exact numerical rank `6`, singular values

`[6.1782067247, 3.9043880048, 1.9743852421, 0.2953352072, 0.02063710717, 0.001448712095]`

and condition number

\[
\kappa = 4264.620104.
\]

Thus the regular/log basis is structurally identifiable on the frozen grid, but coefficient extraction is not perfectly conditioned and requires an explicit numerical/model error envelope in any physical use.

## Synthetic positive control

Freeze coefficients

`[a0,b0,a1,b1,a2,b2] = [0.70,-0.11,0.23,0.05,-0.09,0.02]`.

A least-squares recovery using the correct basis gives

- relative coefficient error `1.28e-14`;
- relative fit residual `4.19e-16`.

Classification: `PASS_MACHINE_PRECISION`.

## Pure-Taylor negative control

Fit the same logarithmic data using the same number of free parameters but a pure Taylor degree-five basis

`[1,z,z^2,z^3,z^4,z^5]`.

The relative residual is

\[
1.905923234\times10^{-2}
\]

or approximately **1.91%**.

Therefore equal parameter count does not make a pure-Taylor basis equivalent to the one-loop regular+log basis on the frozen protocol.

## Deterministic perturbation audit

For a fixed noise direction:

| relative input perturbation | relative coefficient error |
|---:|---:|
| `1e-12` | `1.02e-9` |
| `1e-10` | `1.02e-7` |
| `1e-8` | `1.02e-5` |
| `1e-6` | `1.02e-3` |

This is a deterministic conditioning diagnostic, not Fisher/resource inference.

## Retained results

- `NUM-NG-015 — TWELVE_POINT_DYNAMIC_RANGE_128_GRID_RESOLVES_THE_SIX_COLUMN_ONE_LOOP_REGULAR_PLUS_LOG_SOFT_BASIS`;
- `SOFT-NG-007 — PURE_TAYLOR_BASIS_WITH_EQUAL_PARAMETER_COUNT_LEAVES_PERCENT_LEVEL_RESIDUAL_ON_A_LOG_SOFT_CONTROL`;
- `NUM-NG-016 — LOG_SOFT_COEFFICIENT_EXTRACTION_HAS_NONTRIVIAL_CONDITIONING_AND_REQUIRES_A_DECLARED_NUMERICAL_ERROR_ENVELOPE`;
- `NG-FUNNEL-067 — LOOP_SOFT_PROTOCOL_MUST_VALIDATE_REGULAR_LOG_SEPARATION_BEFORE_PHYSICAL_COMPARATOR_IMPORT`.

## What this does not establish

No physical C5 loop expression has yet been projected through this extractor. No Candidate Gravity residual exists. This is protocol validation only.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

## Next gate

Import one fixed physical standard-QG nonanalytic soft/cut control into the finite-epsilon extractor. The preferred route is an explicitly IR-safe/subtracted on-shell control or a source-completed gauge-safe expression. Preserve the operation order: finite soft momentum -> hard-channel cut -> source/Ward completion -> regular+log extraction.
