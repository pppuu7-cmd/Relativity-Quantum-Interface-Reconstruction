# RQIR Recovery Delta — Iteration 061

**Date:** 2026-08-30

Numbering: parallel preliminary Iteration 060 was committed first. This delta is the canonical continuation for the deeper joint covariance/lambda/source-metrology optimization.

## Retained rules

**RQIR-RESOURCE-028 — base covariance is an active wall-clock variable.**

At the Toy012 transparent benchmark (`100 Hz`, `p=.5`, `1 ms`, per unit lambda):

- relational covariance `(2,4,5,6)`, `rho^2=2`: `>19.8303 h`;
- `(1,2,3,4,5,6)`, `rho^2=3`: `>29.7454 h`;
- all8, `rho^2=6`: `>59.4909 h`.

**RQIR-CAL-018 — graph-cost saturation.**

Select covariance observables by physical graph/resource cost, not row count. The six-row set `(1,2,3,4,5,6)` has the same current `rho^2=3` lower-bound cost as relevant five-row blocks while improving nuisance Fisher.

**RQIR-RESOURCE-029 — joint auxiliary co-optimization.**

Use

`T_aux,S(lambda)=lambda[T_mean+T_cov,S]+C_alpha,S(lambda)/R_alpha`

and optimize covariance topology, `lambda`, and independent source Fisher together.

One 14-row Toy012 mean family at xi=1 costs `~26.0220 h` at 100 Hz, p=.5, 1-ms overhead. Relational and direct-force mean families are conservatively separate unless a common physical likelihood is supplied.

At `R_alpha=2.20253e-5 s^-1`, equal mean sensitivities:

- xi=1 -> six-row graph, lambda~0.952, C_alpha~14.10, T_aux~255.69 h;
- xi=1.5 -> four-row graph, lambda~1.374, C_alpha~13.21, T_aux~225.70 h;
- xi=3 -> four-row graph, lambda~1.755, C_alpha~12.22, T_aux~199.02 h.

Transition near this rate: xi~1.48.

Fast source metrology may make `lambda<1` optimal; slow source metrology favors overexposure and eventually calibration-only alpha closure.

## Reproduction

Canonical entry point:

`analysis/toy012_relcov_lambda_metrology_codesign_iteration061.py`

The full implementation remains in the provisional file `analysis/toy012_relcov_lambda_metrology_codesign_iteration060.py` because it was committed during the numbering race. Treat Iteration 061 as the authority for interpretation.

## Next gate

Combine this auxiliary lower envelope with the absolute D2 science Fisher rate. Use Toy012 absolute D2 information ratio ~0.21617 and the equivalent-force ASD formula to derive the parametric science-vs-auxiliary wall-clock crossover. Do not freeze hardware parameters yet.
