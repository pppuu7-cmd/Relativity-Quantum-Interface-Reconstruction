# RQIR Research Log — Iteration 057

**Date:** 2026-08-30  
**Target:** rebuild Toy009's finite-reference relational + direct-force complementary D2 branch on balanced local Toy012.

## Main result

Toy012 does **not** reproduce Toy009's covariance-completion mechanism.

At fixed `y_ref=-4`, relational means + direct force means + centered relational covariance are already hard rank `23/23`, but at the Toy012 centered NP3 calibration scale give only

`F_beta|theta(C_alpha=0) ~= 0.194405`.

Thus exact rank completion is not statistical closure. Record **RQIR-NG-026**.

## Force-covariance subsets

Rank subsets by the smallest source prior needed for `F_beta|theta=0.90` at `lambda=1`:

- k0: `C_alpha*=13.669415`;
- k1 `(1)`: `13.135585`;
- k2 `(1,3)`: `12.309076`;
- k3 `(1,3,5)`: `12.152511`;
- k4 `(1,3,4,5)`: `12.097052`;
- k5 `(0,1,3,4,5)`: `12.009588`;
- k6 `(0,1,2,3,4,5)`: `11.972118`;
- k7 `(0,1,3,4,5,6,7)`: `11.934827`;
- all8: `11.891638`.

All are hard rank `23/23`.

On Toy009 best4 nearly removed the source prior; on Toy012 even all8 save only `~1.78` units of `C_alpha`. Record **RQIR-DESIGN-004**: complementary covariance geometry is source-specific and must be co-designed with the source.

## Resource check

Best four-by-Ca `(1,3,4,5)` have endpoint graph `rho^2=2`, giving under the retained Gaussian cross-covariance bound

`N_cov,4 > 3.798996e6`

accepted trajectories.

They save only

`Delta C_alpha ~=1.57236`.

At `100 Hz`, acceptance `.5`, `1 ms` overhead, current Toy012 max phase gives covariance lower-bound wall time `~19.83 h` and source-metrology break-even rate

`R_alpha ~2.20e-5 s^-1`.

Balanced Toy012 Ramsey no-reset coefficient is `0.00213429`, so at `p_E=.5` the corresponding controlled-phase-rate threshold is only

`Omega_E ~0.02064 s^-1`.

Thus independent source metrology is favored over best4 covariance in a broad zero-reset regime; RESOURCE-026 must be used for finite reset/visibility.

## Decision

Do not inherit Toy009's best4 covariance bundle into Toy012. Current preferred local branch is relational/force means + independent source metrology unless a new complementary source co-design demonstrates a real wall-clock gain.

## Files

- `analysis/toy012_complementary_d2_branch_iteration057.py`
- `docs/TOY012_COMPLEMENTARY_D2_BRANCH.md`
- `recovery/RECOVERY_DELTA_ITERATION_057.md`

## Next

Compare reset-aware Gaussian pointer vs Ramsey source metrology on the same physical Fisher-rate surface. If independent metrology remains cheap, prioritize total SI detector budget rather than another covariance-completion search.