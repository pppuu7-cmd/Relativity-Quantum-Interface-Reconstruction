# RQIR Recovery Delta — Iteration 057

**Date:** 2026-08-30

Apply after canonical Iteration 056.

## New retained result

Balanced Toy012 has been propagated through the centered finite-reference relational + direct-force complementary D2 architecture.

At common reference `y_ref=-4` and Toy012's centered NP3 D2 weights

- `gamma_mean=1.2086865e6`;
- `gamma_cov=1.8994980e6`,

relational means + force means + centered relational covariance already give hard rank `23/23`, with smallest hard singular value `~1.7141e-3`.

Nevertheless `F_beta|theta(C_alpha=0,lambda=1)~0.194405`.

### RQIR-NG-026 — local rank completion without statistical closure

Full hard rank does not imply finite-noise/profile closure. Toy012 has no exact relational null in this branch but still needs substantial calibration/source information.

## Force-covariance subset result at y_ref=-4

Minimum `C_alpha` needed for 90% at `lambda=1`:

- k0: `13.669415`;
- k1 `(1)`: `13.135585`;
- k2 `(1,3)`: `12.309076`;
- k3 `(1,3,5)`: `12.152511`;
- k4 `(1,3,4,5)`: `12.097052`;
- k5 `(0,1,3,4,5)`: `12.009588`;
- k6 `(0,1,2,3,4,5)`: `11.972118`;
- k7 `(0,1,3,4,5,6,7)`: `11.934827`;
- all8: `11.891638`.

All remain hard rank `23/23`.

### RQIR-DESIGN-004 — complementary covariance geometry is source-specific

Toy009's best4 covariance completion does not transfer to Toy012. Even all eight force-covariance rows reduce the source prior by only `~1.78`. Complementary calibration must be co-designed with the source Hamiltonian/hidden direction.

## Resource implication

At y_ref=-4, best four-by-Ca `(1,3,4,5)` have natural endpoint graph `rho^2=2`.

Using the retained Gaussian cross-covariance lower bound:

- `N_cov,4 > 3.798996e6` accepted trajectories;
- `Delta C_alpha~1.57236` saved relative to no added force covariance;
- at 100 Hz, p=.5 and 1 ms overhead, lower-bound covariance wall time `~19.83 h`;
- independent source-metrology break-even `R_alpha~2.2025e-5 s^-1`.

Balanced Toy012 zero-reset Ramsey coefficient is `max F_alpha/phi~0.00213429`, so at p_E=.5 the corresponding controlled-phase rate threshold is only `Omega_E~0.02064 s^-1`.

Finite reset/visibility must use RESOURCE-026.

## Architecture decision

Do not inherit Toy009 best4 covariance as the default local-source architecture. Current leading Toy012 source-amplitude closure route is independent source metrology unless a new complementary co-design proves a wall-clock advantage.

## Reproduction

Run `analysis/toy012_complementary_d2_branch_iteration057.py`.

## Next continuation step

Compare finite-resolution Gaussian QND pointer and Ramsey ancilla on one reset-aware physical Fisher-rate surface. If independent metrology remains robustly cheap, move next to total Toy012 SI detector/mean/control budget rather than forcing covariance completion.