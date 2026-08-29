# RQIR Recovery Delta — Iteration 016

**Date:** 2026-08-29  
**Read after:** `docs/RECOVERY_GUIDE.md` v1.2 and `docs/RECOVERY_DELTA_ITERATION015.md`.

## Authoritative new result

The explicit low-rank drift/additive-offset gate has now been evaluated in the corrected 22D hard-constrained source-nuisance basis.

Calibration nuisance columns:

- second-probe position drift `delta y`;
- common phase/time drift `delta tau`;
- common additive mean offset `b_mean`;
- common additive covariance offset `b_cov`.

### RQIR-NG-006

If all four amplitudes are unrestricted, detector-level profiled `F_beta` collapses to numerical zero for both D1 and D2 and is not restored by arbitrarily increasing the common calibration exposure scale in the tested local model.

Independent control/prior information is therefore logically required for these overlapping systematic directions.

### Finite-prior bundle at corrected q=1 allocation

Constraining each systematic residual to about 10% of its statistical calibration sigma gives approximately 90% retained detector information.

D1:
- `sigma(delta y)~0.472`;
- `sigma(delta tau)~5.95e-3` (~9.5 us at 100 Hz);
- `sigma(b_mean)~7.62e-5`;
- `sigma(b_cov)~1.03e-4`.

D2:
- `sigma(delta y)~0.399`;
- `sigma(delta tau)~5.03e-3` (~8.0 us at 100 Hz);
- `sigma(b_mean)~6.44e-5`;
- `sigma(b_cov)~1.04e-4`.

Doubling both calibration Fisher and matched control-prior Fisher raises retained information to about 0.947.

### RQIR-CAL-007

Calibration exposure and independent control priors are non-substitutable when systematics overlap detector-relevant nuisance directions.

## Multiplicative gain

Pure common gain is still first-order suppressed at the exact null. Leading gain-state contamination is bilinear `delta g * A delta theta`; it must be handled by a nonlinear/second-order bias audit rather than first-order Fisher.

## Next step

Perform second-order gain-state/timing bias analysis, then convert timing/additive-offset priors into explicit D1 pulse-clock/reset and D2 reference/sampling-channel requirements.

Authoritative files:

- `docs/HARD_CONSTRAINT_FISHER_AUDIT.md`
- `docs/LOW_RANK_CALIBRATION_SYSTEMATICS_FISHER.md`
- `analysis/hard_constraint_fisher_audit_iteration015.py`
- `analysis/low_rank_systematics_fisher_iteration016.py`
