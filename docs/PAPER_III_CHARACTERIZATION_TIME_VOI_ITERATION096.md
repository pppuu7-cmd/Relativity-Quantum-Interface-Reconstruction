# RQIR Iteration 096 — Characterization-Time Value of Information

**Date:** 2026-08-30  
**Status:** Paper-III decision/resource gate; no hardware forecast and no new-physics claim.

## 1. Question

Iterations 093–095 determine how the unresolved Toy009/Toy014 architecture band changes when an uncertainty interval is contracted and then propagate that sensitivity to primitive detector/calibration/source variables.  Is the largest decision derivative automatically the apparatus quantity that should be measured first?

**No.** A measurement priority is physical only after the rate/cost of reducing that uncertainty is included.

Let the unresolved robust-throughput width be `W` and let an uncertain primitive coordinate `x` have current half-width (or Gaussian one-sigma scale) `h_x`.  Iteration 094 defines the dimensionless local contraction leverage

`Lambda_x = (h_x/W) dW/dh_x`

on a fixed active robust branch.

## 2. RQIR-RESOURCE-048 — decision value per characterization second

Suppose an independent characterization channel accumulates Fisher information on `x` at physical rate `R_char,x`, so that, away from a systematic floor,

`h_x = I_x^(-1/2)`,  `dI_x/dt = R_char,x`.

Then

`dh_x/dt = -(1/2) R_char,x h_x^3`.

Therefore the instantaneous fractional shrink rate of the unresolved architecture band is

`boxed{Xi_x = -(1/W)dW/dt = (1/2) Lambda_x R_char,x h_x^2}`.

`Xi_x` has units of inverse time.  It is the correct local value-of-information **per characterization second** under the declared Fisher-limited model.

Consequences:

1. `Lambda_x` alone ranks equal fractional interval contractions, not equal wall-clock characterization campaigns;
2. the physical comparison variable is `G_x = R_char,x h_x^2` together with `Lambda_x`;
3. two characterization channels `x,y` are locally equal in value per second when

   `G_x/G_y = Lambda_y/Lambda_x`;

4. the Iteration-095 primitive chain rule can be inserted before this formula, so `x` may be a science-band coefficient, cross-PSD parameter, calibration-block entry, source acceptance/coupling/reset/visibility coordinate, or duty/control coordinate.

## 3. RQIR-NG-049 — decision sensitivity is not measurement priority

A larger raw uncertainty or a larger `Lambda_x` does **not** imply that measuring `x` first gives the fastest robust architecture decision.

The measurement that should be characterized first is the one with the largest `Xi_x`, after its own physical characterization Fisher rate and present uncertainty are included.

This sharpens NG-045.  NG-045 said percent uncertainty is not decision value; NG-049 says even decision value per equal interval contraction is not yet a physical characterization schedule.

A complete statement also requires the cost of the measurement itself if it consumes shared science/calibration hardware or alters duty.

## 4. Regression on the Iteration-094 synthetic box

The synthetic Iteration-094 interval box gave local leverages

- Toy014 `R_src`: `0.51911021046`;
- Toy009 `R_src`: `0.42737125993`;
- Toy014 `A`: `0.18109516727`;
- Toy014 duty: `0.15899646329`;
- Toy009 duty: `0.10243207462`;
- Toy009 `A`: `0.03527950118`.

If all channels have equal normalized characterization speed

`G_x = R_char,x h_x^2`,

the old ranking is recovered exactly.

But the break-even `G_x/G_Rsrc14` values are

| competitor | required normalized characterization speed relative to Toy014 `R_src` |
|---|---:|
| Toy009 `R_src` | `1.21466` |
| Toy014 `A` | `2.86651` |
| Toy014 duty | `3.26492` |
| Toy009 duty | `5.06785` |
| Toy009 `A` | `14.7142` |

Thus, for example, Toy014 `A` has only about 35% of the raw contraction leverage of Toy014 `R_src`, yet becomes the better characterization target per second if its normalized characterization channel is more than about `2.87x` faster.

These numbers are **regression-only** because the underlying Iteration-094 box is synthetic.  The new law, not that ranking, is retained.

## 5. RQIR-RESOURCE-049 — finite characterization time and systematic floors

Let a primitive uncertainty have an irreducible floor `h_floor` and Fisher-limited statistical component,

`h(t)^2 = h_floor^2 + 1/(I0 + R_char t)`.

For a target `h1` satisfying

`h_floor < h1 < h0`,

the additional characterization time is

`boxed{T_char = [1/(h1^2-h_floor^2) - 1/(h0^2-h_floor^2)] / R_char}`.

If `h1 <= h_floor`, the target is impossible regardless of characterization time.

With zero floor, halving an uncertainty requires

`T_char = 3/(R_char h0^2)`.

Thus an uncertainty-contraction proposal must quote both the current uncertainty and the physical rate/floor of the characterization channel; a requested percentage reduction alone is not a resource budget.

## 6. Composition with the Iteration-095 primitive Jacobian

For a primitive `z` entering an architecture coefficient `A_i`,

`dW/dz = (dW/dA_i)(dA_i/dz)`.

For a source-metrology primitive entering `R_src,i`,

`dW/dz = (dW/dR_src,i)(dR_src,i/dz)`.

Therefore RESOURCE-048 applies directly after the chain rule.  Examples already available from Iteration 095 include

- science `a2,a4,rho` derivatives;
- every smooth `2x2` calibration-block minimum-eigenvalue derivative;
- source acceptance/coupling/reset/visibility derivatives on a smooth optimized Ramsey branch.

NG-048 remains mandatory at eigenvalue crossings, PSD boundaries, robust-corner switches or Ramsey active-set changes: use finite interval contraction or subgradient/robust optimization rather than a single local derivative.

## 7. Scientific consequence

The request in the Iteration-095 front to identify the **actual** highest-value apparatus characterization measurement cannot be answered from primitive sensitivity alone.  One additional physical data layer is required:

`(h_x, R_char,x, h_floor,x, characterization duty/cost)`

for each candidate measurement coordinate (or the corresponding joint Fisher/covariance update for correlated parameters).

This is not a setback: it converts the remaining characterization problem into the same physical resource language already used for science, source preparation and calibration.

## 8. Next gate

Given physical characterization Fisher rates, optimize a **finite characterization-time allocation** rather than selecting one parameter once.  Because Fisher-limited uncertainties have diminishing returns, the optimal schedule should equalize marginal decision-band shrink rates across active characterization channels, with inactive channels receiving zero time until their marginal value reaches the active set.

Then apply that schedule to a declared Toy009/Toy014 primitive uncertainty envelope.  Do not start Toy015 unless the resulting robust rate-space budget shows a source-dependent bottleneck.

## 9. Reproducibility

Run:

`python analysis/characterization_time_voi_iteration096.py`

The script reproduces the Iteration-094 leverage ordering at equal normalized characterization speed, verifies the break-even laws, gives an explicit ranking-reversal counterexample, and checks the finite-time/floor contraction formula.
