# RQIR Research Log — Iteration 061

**Date:** 2026-08-30

A parallel preliminary Iteration 060 was committed first, so the concurrent deeper covariance/lambda/source-metrology calculation is canonically numbered 061.

## Main result

Exposing Toy012's eight base relational covariance rows and jointly optimizing

`T_aux=lambda(T_mean+T_cov)+C_alpha(lambda)/R_alpha`

changes the branch selection. New retained rules:

- **RQIR-RESOURCE-028:** base covariance is an active wall-clock variable, not a common constant;
- **RQIR-CAL-018:** covariance row cardinality is not physical cost; endpoint-graph spectral-radius saturation can make an added row improve Fisher without increasing the current graph lower bound;
- **RQIR-RESOURCE-029:** covariance topology, calibration exposure and independent source metrology must be co-optimized.

At 100 Hz, p=.5, 1-ms overhead:

- one 14-row mean family at xi=1 costs `~26.022 h`;
- four-row relational covariance `(2,4,5,6)`, rho²=2, costs `>19.830 h` per unit lambda;
- six-row `(1,2,3,4,5,6)`, rho²=3, `>29.745 h`;
- all8, rho²=6, `>59.491 h`.

At `R_alpha=2.20253e-5 s^-1` and equal mean sensitivity:

- xi=1: six-row set wins, lambda~.952, C_alpha~14.10, T_aux~255.69h;
- xi=1.5: four-row set wins, lambda~1.374, C_alpha~13.21, T_aux~225.70h;
- xi=3: four-row set wins, lambda~1.755, C_alpha~12.22, T_aux~199.02h.

The current equal-xi transition is near xi~1.48.

Fast source metrology drives optimal lambda below one; slow source metrology drives overexposure and eventually C_alpha toward zero.

## Next

Attach absolute Toy012 D2 science Fisher in SI-parametric form and derive the science-vs-auxiliary crossover surface in mass product / force ASD / duty. Covariance time remains a lower bound until finite-reference detector transduction is explicit.
