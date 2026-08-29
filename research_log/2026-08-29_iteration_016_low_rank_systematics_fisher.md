# RQIR Research Log — Iteration 016: Low-Rank Calibration Systematics Fisher

**Date:** 2026-08-29

## Starting point

Iteration 015 corrected the heterogeneous Fisher numerics by analytically eliminating exact trace+energy constraints. The postponed Iteration-014 target was then resumed in the corrected 22D nuisance basis.

## Systematics promoted to explicit nuisances

Four calibration-row nuisance columns were included:

- second-probe geometry drift `delta y`;
- common phase/time drift `delta tau`;
- common additive mean-row offset `b_mean`;
- common additive covariance-row offset `b_cov`.

Finite independent control knowledge is represented by prior Fisher on these four amplitudes.

## Main negative result

With all four amplitudes unrestricted, profiled `F_beta` collapses to numerical zero for both D1 and D2. Multiplying gravitational calibration exposure by factors up to 100 does not cure the loss.

Recorded as **RQIR-NG-006**: uncontrolled low-rank calibration systematics can be structurally degenerate with detector-relevant source nuisance, so exposure alone cannot restore identifiability.

## Finite-prior result

Using the corrected Iteration-015 q=1 90%-retention allocations and constraining every systematic residual to about 10% of the corresponding statistical calibration sigma gives:

D1:
- `sigma(delta y)~0.472`;
- `sigma(delta tau)~5.95e-3`;
- `sigma(b_mean)~7.62e-5`;
- `sigma(b_cov)~1.03e-4`;
- retained `F_beta~0.89996`;
- timing equivalent at 100 Hz `~9.5 us`.

D2:
- `sigma(delta y)~0.399`;
- `sigma(delta tau)~5.03e-3`;
- `sigma(b_mean)~6.44e-5`;
- `sigma(b_cov)~1.04e-4`;
- retained `F_beta~0.89989`;
- timing equivalent at 100 Hz `~8.0 us`.

If calibration exposure and matched control precision are both improved by 2x in Fisher, retained information rises to about `0.947`.

## Design rule

**RQIR-CAL-007:** for systematics overlapping detector-relevant calibration directions, calibration shot count and independent control prior are not interchangeable resources.

## Gain note

Pure common multiplicative gain remains first-order suppressed at exact null. The leading contamination is bilinear `delta g * A delta theta`, so it belongs to a second-order nonlinear/bias audit, not a fake first-order Fisher column.

## Files

- `analysis/low_rank_systematics_fisher_iteration016.py`
- `docs/LOW_RANK_CALIBRATION_SYSTEMATICS_FISHER.md`
- this log

## Next gate

Second-order bias/nonlinear likelihood for gain-state coupling and finite timing nonlinearities, then physical clock/reference-channel translation for D1/D2.
