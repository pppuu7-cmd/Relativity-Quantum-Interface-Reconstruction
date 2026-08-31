# Candidate Gravity — Iteration 190: prospectively frozen withheld null-soft extension

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Protocol:** `RQIR-WITHHELD-NULLSOFT-12-v1`

## Motivation

Iteration 188 found that the unique algebraic complement of the current rank-5 six-row comparator span is dominated at the 94.67% level by one row. A future candidate must not be optimized to that accidental geometry.

Therefore the extension is frozen **before any candidate is evaluated**.

## Selection rule

Start only from the six original hard four-vectors `q_i` already frozen by Iteration 185.

Create twelve additional rows by the deterministic rule

`q_i -> 0.75 q_i` and `q_i -> 1.25 q_i`,

for every original row `i=0..5`.

No current left-null weight, comparator residual, candidate parameter, or target amplitude enters the rule.

Keep

- the same null soft direction `k0=(1,0,0,1)`;
- soft steps `[0.01,0.005,0.0025,0.00125,0.000625]`;
- fixed new deterministic polarization seed pairs recorded in the JSON authority.

## Kinematic certificate

The twelve withheld hard rows span

`q^2 in [0.1621125,0.793125]`,

compared with roughly `[0.2882,0.5076]` for the original six rows.

Across all five soft steps, the partner hard leg remains spacelike:

`r^2 in [0.1574625,0.793]`.

Thus every withheld hard and partner leg is spacelike in the frozen signature convention.

## Mandatory future order

1. Compute C5 local and exact K2-compensation columns on the withheld rows.
2. Compute the fixed `QG-NL-EXP-001` conditioned column with no row retuning.
3. Carry forward AS/C3 as blocked, or insert newly derived columns only if their parent authority becomes available.
4. Only after comparator construction may any future Candidate Gravity residual be evaluated on these rows.

## Retained results

- `PROTO-NG-001 — WITHHELD_ROW_EXTENSION_FROZEN_BEFORE_ANY_CANDIDATE_TEST`.
- `NUM-NG-005 — HARD_Q2_LEVER_ARM_EXPANDED_FROM_BASELINE_TO_0P162_0P793_WITHOUT_TARGET_OPTIMIZATION`.
- `NG-FUNNEL-045 — FUTURE_RESIDUAL_MUST_SURVIVE_PROSPECTIVELY_FROZEN_ROW_EXTENSION`.

## Readiness

`MODEL_READINESS: 24%` — unchanged. This is a prospective robustness gate, not a residual or comparator-foundation closure by itself.
