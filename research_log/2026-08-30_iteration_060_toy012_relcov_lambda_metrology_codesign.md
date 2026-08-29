# RQIR Research Log — Iteration 060

**Date:** 2026-08-30

## Question

What changes when Toy012's eight base relational-covariance rows are no longer treated as common/free overhead and are optimized jointly with calibration exposure `lambda` and independent source-metrology Fisher `C_alpha`?

## Results

The eight-row block is expensive under the natural shared-endpoint Gaussian lower bound: at 100 Hz, `p=.5`, 1-ms overhead and `lambda=1`, all eight cost `>59.49 h` while the four-row set `(2,4,5,6)` costs `>19.83 h`.

At fixed `lambda=1`, fewer than three base covariance rows cannot reach `F_beta|theta=0.90` even with perfectly known source amplitude. This is not a hard no-go: stronger calibration can compensate. With perfect alpha, minimum `lambda` falls from `~9.01e4` for zero covariance rows to `~0.270` for the best four and `~0.247` for all eight.

New retained result **RQIR-RESOURCE-028**: base covariance is an active wall-clock variable, not a common constant.

The endpoint graph reveals a second effect. The six-row set `(1,2,3,4,5,6)` has `rho^2=3`, the same current graph floor as relevant five-row blocks, yet improves source-nuisance closure. New rule **RQIR-CAL-018**: select covariance observables by physical graph/resource cost, not cardinality.

Joint objective:

`T_aux = lambda(T_mean+T_cov) + C_alpha(lambda)/R_alpha`.

At `R_alpha=2.20253e-5 s^-1` and equal relational/force mean sensitivity:

- `xi=1`: six-row graph wins, `lambda~0.952`, `C_alpha~14.10`, `T_aux~255.69 h`;
- `xi=1.5`: four-row graph wins, `lambda~1.374`, `C_alpha~13.21`, `T_aux~225.70 h`;
- `xi=3`: four-row graph wins, `lambda~1.755`, `C_alpha~12.22`, `T_aux~199.02 h`.

The current equal-xi transition is near `xi~1.48`.

New retained result **RQIR-RESOURCE-029**: covariance subset, gravitational calibration exposure and independent source metrology are substitutable resources and must be optimized together. Fixed-`lambda` branch diagrams can select the wrong architecture.

Fast source metrology can make `lambda<1` optimal; slow source metrology drives `lambda>1` and eventually `C_alpha->0`.

## Next

Combine the optimized auxiliary envelope with Toy012 absolute D2 signal (`~0.21617` of Toy009), physical force ASD/mass scaling and Iteration-059 controls. Derive the parametric science-vs-auxiliary wall-clock crossover rather than guessing an apparatus.
