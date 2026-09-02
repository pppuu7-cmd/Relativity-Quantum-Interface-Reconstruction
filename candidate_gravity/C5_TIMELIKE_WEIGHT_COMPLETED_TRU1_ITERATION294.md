# Candidate Gravity C5 — Iteration 294 timelike weight-completed Tr U1 scan

**Date:** 2026-09-03  
**MODEL_READINESS:** **24%**

## Purpose

Evaluate the actual mixed-cubic effective-action insertion `[Tr U1]_{sab}` directly on the frozen timelike translation-closed slice from Iteration 278, rather than continuing the old weighted proxy `tr(B3)`.

Frozen slice:

- `k_s^2=0`;
- `k_s.k_a=-0.1`;
- `k_a^2=-s`;
- `k_b=-(k_s+k_a)` and `k_b^2=-(s+0.2)`;
- `s={0.004,...,0.032}`.

## Result

The complete trace is nonzero and positive on all eight timelike rows:

`[0.88125485, 0.93713710, 1.00201640, 1.07862794, 1.17089411, 1.28465260, 1.42899352, 1.61889698]`.

Minimum absolute value:

`0.8812548497486561`.

Maximum finite-difference step relative spread over the frozen stress rows is

`2.919327861777802e-6`.

Freeze:

`PASS_SCOPED_TIMELIKE_TRANSLATION_CLOSED_WEIGHT_COMPLETED_TRU1_NONZERO_ALL_ROWS`.

## Strong proxy-versus-trace contrast

The old Iteration-278 weighted proxy `tr(B3)` is large and negative on this same slice:

`-15.55 ... -34.65`.

The actual `Tr U1` coefficient is instead order one and positive. At the planned reduction checkpoint `s=0.016`:

- old proxy `tr(B3) = -20.458473546663335`;
- `tr(B3Y0) = +1.2194066904823941`;
- total weight dressing `B2Y1+B1Y2 = -0.14077875193557943`;
- complete `[Tr U1]_{sab} = +1.0786279385468147`.

Thus weight completion changes both magnitude and qualitative sign structure. The old proxy pole/tensor coefficients cannot be transferred to the effective-action trace.

## Scope

This is still a fixed-loop-momentum numerator certificate. It is not yet the integrated discontinuity, source-completed linked `T_cut`, comparator-subtracted residual or novelty result.

## Cleaner continuation protocol

Iteration 293 is being used only to certify the structural polynomial basis and complete family reconstruction. For the physical cut, numerator coefficients should be reconstructed directly on the timelike row, starting at `s=0.016`, and only the loop-integral branch prescription should be evaluated with `+/- i0`.

This avoids importing spacelike numerator coefficients into a timelike denominator continuation by assumption.

## Next gate

After Iteration 293 passes, rebuild the complete Iteration-292 family oracle at `s=0.016`, fit every non-scaleless numerator directly there with the certified basis, and then perform a common-normalization DR `+i0/-i0` tensor/Laurent reduction.

No Candidate Gravity residual is declared. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.
