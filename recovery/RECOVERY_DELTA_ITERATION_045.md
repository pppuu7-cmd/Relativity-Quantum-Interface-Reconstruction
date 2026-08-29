# RQIR Recovery Delta — Iteration 045

**Date:** 2026-08-29

## New resource rule

**RQIR-RESOURCE-019 — response-preserving shared-credit cap**

Under the reciprocal linear quantum-limited reference class, requiring at least 90% of unperturbed raw D2 signal Fisher limits ideal same-copy mean information to

`xi_shared<=0.7239817`, `I_shared<=0.5241495`

per normalized mean row.

Across the current best4 covariance/science floor `N=1.180254e6`, maximum optimistic shared mean credit is

`~6.18630e5`

per row versus centered target

`gamma_mean=1.830265e6`.

Thus at most `~33.8%` of the mean target can be shared; at least `~66.2%` remains for independent/sacrificial time-layer calibration preparations. This is optimistic because it uses raw detector signal Fisher and ignores extra multitime backaction/profile degradation.

## Transparent benchmark

At `100 Hz`, `p=0.5`, `1 ms` dead/readout, parallel same-time dual-probe readout:

- best4 covariance/science floor `~5.864 h`;
- mixed total with independent `xi=3`: `~9.18 h`;
- with `xi=5`: `~7.06 h`;
- with `xi=10`: `~6.16 h`.

Sharing reduces but does not remove the independent mean-calibration layer.

## Next

Propagate the backaction/dephasing superoperator through the complete hard-constrained D2 detector/nuisance Jacobian and determine the true `xi_shared` allowed by final profiled `F_beta|theta>=0.90`.