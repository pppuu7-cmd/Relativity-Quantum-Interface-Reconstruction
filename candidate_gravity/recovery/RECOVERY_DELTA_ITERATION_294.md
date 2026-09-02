# Recovery Delta — Iteration 294

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%

## New scoped timelike result

The actual weight-completed mixed-cubic trace `[Tr U1]_{sab}`, not the old weighted proxy `tr(B3)`, has been evaluated directly on the frozen Iteration-278 timelike translation-closed slice.

It is nonzero and positive on every row `s=0.004,...,0.032`:

`0.88125485, 0.93713710, 1.00201640, 1.07862794, 1.17089411, 1.28465260, 1.42899352, 1.61889698`.

Maximum step-scan relative spread: `2.92e-6`.

Freeze:

`PASS_SCOPED_TIMELIKE_TRANSLATION_CLOSED_WEIGHT_COMPLETED_TRU1_NONZERO_ALL_ROWS`.

## Important contrast

At `s=0.016`:

- old proxy `tr(B3)=-20.458473546663335`;
- flat-weight `tr(B3Y0)=+1.2194066904823941`;
- weight dressing `=-0.14077875193557943`;
- actual `[Tr U1]_{sab}=+1.0786279385468147`.

The old weighted-kernel scalar coefficients and pole cannot be transferred to the effective-action trace.

## Continuation protocol

Use Iteration 293 only as structural basis/reconstruction authority. For the integrated cut, reconstruct the complete family numerator coefficients directly at a timelike row (start `s=0.016`) and then evaluate the loop masters with `+/- i0`. Do not continue spacelike numerator coefficients by rotating denominators alone.

## Status

This is a numerator certificate, not an integrated discontinuity and not a Candidate Gravity residual.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN.
