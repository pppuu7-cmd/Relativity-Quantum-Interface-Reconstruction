# RQIR Research Log — Iteration 060

**Date:** 2026-08-30

## Question

Which Toy012 relational-covariance subset minimizes actual auxiliary wall clock once independent source metrology and mean calibration are charged explicitly?

## Result

The eight base relational covariance rows are not a free/common constant.

Resource-relevant subset minima reproduce the Iteration-059 prescan:

- k4 `(2,4,5,6)`: `C_alpha=15.06193956`, graph `rho^2=2`, covariance floor `19.83028 h`;
- k5 `(2,3,4,5,6)`: `C_alpha=13.81947864`, graph `rho^2=3.61803399`, covariance floor `35.87332 h`;
- all8: `C_alpha=13.66941472`, graph `rho^2=6`, covariance floor `59.49085 h`.

At the transparent Toy012 benchmark `p=.5`, 100 Hz, dead=1 ms, two independent seven-layer mean families cost

`T_mean=52.0440/xi_mu^2 h`,

so at `xi_mu=3` the mean contribution is `5.78267 h`.

The covariance/source-metrology wall-clock crossings are

- k4 -> k5: `R_alpha=2.151263806e-5 s^-1`;
- k5 -> all8: `R_alpha=1.764977970e-6 s^-1`.

New retained result **RQIR-RESOURCE-028**: the optimal covariance bundle is source-metrology-rate dependent. Sparse covariance is optimal for fast independent source metrology; slower source metrology can justify paying for more covariance rows despite shared-endpoint congestion.

No experimental-viability or new-physics claim is made.

## Next

Convert the normalized Toy012 mean sensitivity `xi_mu` into an explicit force-transduction / detector-PSD Fisher rate and place the absolute D2 science signal on the same mass/gap/separation/noise wall-clock budget. This is now the dominant unresolved resource translation.
