# RQIR Iteration 057 — Toy012 Complementary D2 Branch

**Date:** 2026-08-30  
**Scope:** balanced exact-nearest-neighbour Toy012 from Iteration 055, centered finite-reference relational + direct-force D2 calibration.  
**Status:** profiled-Fisher/resource result; no hardware forecast and no new-physics claim.

## 1. Question

Toy012 recovered near-Toy009 NP3 calibration efficiency while enforcing an exactly nearest-neighbour source Hamiltonian. The next question is whether the more physical **complementary D2 architecture** discovered on Toy009 survives that redesign.

The Toy009 complementary architecture uses

- finite-reference relational potential means;
- direct force means;
- centered relational covariance;
- selected centered force-covariance rows;
- independent source-amplitude metrology when required.

Iteration 057 rebuilds that architecture on Toy012.

The primary comparison fixes

`y_ref=-4`

to match the mature Toy009 finite-reference benchmark. This prevents an apparent gain from being obtained merely by changing reference geometry.

## 2. Toy012 calibration scale

The balanced Toy012 NP3 centered D2 90%-retention optimization gives

- `gamma_mean ~= 1.2086865e6`;
- `gamma_cov ~= 1.8994980e6`.

These are row-normalized local Fisher weights, not SI exposure times.

## 3. Exact rank improves — but this does not solve finite-noise inference

With only

- 14 relational means;
- 14 direct force means;
- 8 centered relational covariance rows;

and **no added force-covariance rows**, the hard trace+energy source tangent already has

`rank = 23/23`.

The smallest hard singular value at `y_ref=-4` is

`~1.7141e-3`.

Thus Toy012 does **not** reproduce a one-dimensional exact relational null at this stage.

However, at the current normalized calibration scale and with no independent source-amplitude prior,

`F_beta|theta ~= 0.194405`.

So exact rank completion is a very poor predictor of finite-noise identifiability here.

### RQIR-NG-026 — local rank completion without statistical closure

> A calibration family can be full-rank on the hard finite-dimensional source tangent and still leave very poor profiled detector information at realistic finite calibration Fisher. Exact relational-null removal therefore does not imply a resource-closed gravity discriminator.

This strengthens the programme-wide distinction between algebraic rank and statistical identifiability.

## 4. Force-covariance subset enumeration

At `lambda=1`, subsets are ranked by the **smallest independent source prior `C_alpha` required to reach `F_beta|theta=0.90`**, rather than by unprofiled response alone.

| added force-cov rows | best subset | `F_beta(C_alpha=0)` | `C_alpha*` |
|---:|---|---:|---:|
| 0 | `()` | `0.194405` | `13.669415` |
| 1 | `(1)` | `0.414107` | `13.135585` |
| 2 | `(1,3)` | `0.462459` | `12.309076` |
| 3 | `(1,3,5)` | `0.518524` | `12.152511` |
| 4 | `(1,3,4,5)` | `0.519132` | `12.097052` |
| 5 | `(0,1,3,4,5)` | `0.519978` | `12.009588` |
| 6 | `(0,1,2,3,4,5)` | `0.520161` | `11.972118` |
| 7 | `(0,1,3,4,5,6,7)` | `0.598429` | `11.934827` |
| 8 | all | `0.598707` | `11.891638` |

All of these branches remain hard rank `23/23`.

The central contrast with Toy009 is immediate:

- on Toy009, four force-covariance rows almost eliminated the hidden-amplitude prior;
- on Toy012, the best four reduce `C_alpha` only from `13.67` to `12.10`;
- even all eight reduce it only to `11.89`.

Therefore the strong covariance complementarity of Toy009 is **not invariant under source redesign**.

### RQIR-DESIGN-004 — complementary covariance geometry is source-specific

> A covariance subset that closes detector-relevant nuisance geometry for one source Hamiltonian need not do so for another source, even when both sources have the same dimension, energy spectrum, radius sites, exact NP3 rank and detector observable family. Complementary calibration must be co-designed with the source rather than transferred as a universal module.

## 5. Best-four covariance rows are expensive relative to the information they replace

At `y_ref=-4`, the best four-by-source-prior subset is

`(1,3,4,5)`.

Its natural shared-endpoint graph has

`rho(A_G)^2 = 2`.

Under the same phase-referenced Gaussian cross-covariance lower-bound model used for Toy009,

`N_cov,4 > gamma_cov * rho^2`

so

`N_cov,4 > 3.798996e6`

accepted covariance trajectories.

The four rows save only

`Delta C_alpha ~= 1.572363`.

At the transparent benchmark

- gap frequency `100 Hz`;
- `p_accept=0.5`;
- `1 ms` detector dead/readout time;
- maximum Toy012 phase `5.275220686`;

the covariance lower-bound wall time is

`~19.83 h`.

For those four rows to beat independent source metrology, the latter would need to be slower than approximately

`R_alpha ~= 2.20e-5 s^-1`.

## 6. Toy012 Ramsey source metrology strongly favors the no-extra-force-covariance branch in the zero-reset limit

Iteration 055 found for balanced Toy012 independent QND Ramsey metrology

`max F_alpha(phi)/phi ~= 0.00213429`.

With `p_E=0.5` and negligible reset overhead,

`R_alpha ~= 0.5 * 0.00213429 * Omega_E`.

Equating this to the best-four break-even rate gives

`Omega_E ~= 0.02064 s^-1`.

Therefore, within this transparent zero-reset comparison, a controlled source-energy phase accumulation faster than only about `0.021 rad/s` already makes

**no added force covariance + independent Toy012 source metrology**

cheaper than acquiring the best four additional force-covariance rows solely to reduce the hidden-amplitude prior.

Finite reset/visibility must be evaluated with RESOURCE-026 before turning this into a hardware claim.

## 7. Reference-position scan does not restore Toy009-like covariance completion

An exploratory finite-reference scan shows that changing `y_ref` can modestly improve individual numbers, but does not recover Toy009's dramatic covariance closure.

Representative minima over the scanned negative-reference domain were approximately

- no force covariance: `C_alpha* ~12.86`;
- best four: `~11.54`;
- best five: `~11.45`;
- all eight: `~11.38`.

The corresponding best references move farther from the source for some branches, which would also increase the physical cost of reconstructing relational potential from force. Therefore reference optimization cannot be judged from normalized Fisher alone.

## 8. Scientific interpretation

Toy012 gives a useful separation of two effects:

1. **Locality itself is no longer the dominant nuisance-calibration penalty** — Iteration 055 reduced the NP3 D2 cost to `~1.06x` Toy009.
2. **The Toy009 complementary covariance mechanism does not transfer** — once the source hidden direction changes, force-covariance rows overlap much less efficiently with the remaining detector-relevant nuisance geometry.

This is not a failure of Toy012. It identifies the next co-design variable.

The preferred local-source architecture currently becomes

`Toy012 + relational/force mean calibration + independent source metrology`

rather than automatically inheriting Toy009's best4 covariance bundle.

## 9. Reproducibility

Code:

`analysis/toy012_complementary_d2_branch_iteration057.py`

The script reconstructs the balanced Toy012 source, uses centered covariance derivatives and exact trace+energy elimination, enumerates all force-covariance subsets at `y_ref=-4`, checks hard rank, and derives the natural best-four covariance graph and source-metrology break-even.

## 10. Next gate

There are now two scientifically sensible paths, and they should be compared rather than guessed:

1. **local branch A:** Toy012 with no additional force covariance plus reset-aware independent Ramsey/pointer source metrology;
2. **local branch B:** re-optimize the Toy012 source/calibration geometry with the complementary D2 `C_alpha` penalty included directly in the design objective.

Before launching a much larger source search, first place Gaussian QND pointer and Ramsey metrology on one common reset-aware Fisher-rate surface. If independent source metrology is robustly cheap, there is little reason to spend computation forcing covariance completion into the local source.