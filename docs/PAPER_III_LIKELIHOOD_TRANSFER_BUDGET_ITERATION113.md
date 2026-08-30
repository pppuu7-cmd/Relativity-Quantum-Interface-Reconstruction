# RQIR Iteration 113 — Likelihood-Derived Complex-Transfer Budget

**Date:** 2026-08-31  
**Status:** Paper-III detector/control resource gate. Exact local Gaussian Fisher result; no apparatus winner and no new-physics claim.

## 1. Purpose

Iteration 112 introduced a matrix recertification problem in terms of an admissible complex-transfer covariance budget `Sigma_*`. The immediate open question was how to derive that budget from the detector likelihood rather than assign independent amplitude/phase tolerances by hand.

The main result is slightly stronger than the planned step:

> in the general multivariate transfer problem there is **no unique physically preferred full covariance matrix `Sigma_*`**. The exact admissible uncertainty is a Fisher-retention set. For a scalar science parameter `beta`, a canonical one-dimensional science-coupled transfer mode can nevertheless be extracted and given an exact likelihood-derived variance budget.

This connects Iterations 102–103 directly to the recertification machinery of Iterations 109–112.

## 2. Profile all non-transfer nuisances first

Start from the full detector Fisher matrix for

`(beta, g, theta)`,

where

- `beta` is the scalar RQIR science/interface amplitude;
- `g` is the real local complex-transfer coordinate vector, e.g. four real amplitude/phase components for the temporal `f,2f` response;
- `theta` contains all other detector/source nuisances already included in the declared likelihood: spectral tilt, additive terms, geometry, timing, etc.

Eliminate exact hard constraints analytically and profile `theta` first. On the exact retained support, write the resulting conditional Fisher block as

`J_bar = [[F0, b^T], [b, G]]`.

Here

- `F0` is the detector-level Fisher for `beta` with transfer fixed but all other declared nuisances profiled;
- `b` is the conditional beta/transfer cross-Fisher vector;
- `G` is the conditional transfer Fisher block carried by the science record.

An independent transfer reference supplies Fisher matrix `C >= 0` in the same transfer coordinates.

Then

`boxed{F_beta(C)=F0-b^T (G+C)^-1 b}`.

This is the transfer-only Schur complement after all other nuisances have already been treated consistently.

## 3. Exact Fisher-retention LMI

Require a retained fraction `q in (0,1)` of `F0`:

`F_beta(C) >= q F0`.

Equivalently,

`b^T(G+C)^-1 b <= (1-q)F0`.

By the Schur complement this is exactly

`boxed{G+C >= b b^T / [(1-q)F0]}`

in Loewner order.

### RQIR-RESOURCE-074 — exact transfer-retention LMI

The transfer-calibration requirement should be imposed as a matrix Fisher inequality, not as independent post-hoc amplitude/phase error bars.

The condition is coordinate covariant: under any nonsingular transfer reparameterization, `G`, `C` and `b` transform by the usual Fisher congruence and the inequality is unchanged.

## 4. Why a unique full `Sigma_*` generally does not exist

If the residual transfer uncertainty is represented by an SPD covariance `Sigma`, then `C=Sigma^-1` and the exact admissible set is

`A_q={Sigma>0 : G+Sigma^-1 >= b b^T/[(1-q)F0]}`.

This is the correct likelihood-derived uncertainty object.

There is generally no unique largest covariance matrix in Loewner order inside `A_q`. Transfer directions that are weakly coupled or orthogonal to the scalar science direction can be much less constrained than the science-coupled combination, while another experiment may need those same directions for calibration or additional science parameters.

### RQIR-NG-069 — no unique full covariance budget

A single arbitrary SPD `Sigma_*` can over-calibrate science-insensitive gain/phase directions or encode a basis-dependent design convention. Use the exact admissible set or a declared targeted certificate.

Iteration 112 therefore remains correct as a general matrix recertification envelope, but its `Sigma_*` input should not be treated as uniquely determined by scalar-beta Fisher retention.

## 5. Canonical science-coupled transfer mode

Assume `G` is positive definite on the exact retained transfer support. Define

`B=b^T G^-1 b`,

`ell0=B/F0`.

Because the full Fisher block is positive semidefinite,

`0 <= ell0 <= 1`.

With completely free transfer nuisance (`C=0`),

`F_beta(0)=F0-B=F0(1-ell0)`.

Thus the free-transfer retained fraction is

`q_free=1-ell0`.

If the requested `q <= q_free`, no transfer reference is required **for beta retention alone**.

For `q>q_free`, define

`boxed{kappa_* = ell0/(1-q)-1}`

and the normalized science-coupled transfer vector

`boxed{a=b/sqrt(B)}`.

Then the rank-one reference Fisher

`boxed{C_*=kappa_* a a^T = kappa_* b b^T/B}`

satisfies

`boxed{F_beta(C_*)=q F0}`

exactly.

### RQIR-RESOURCE-075 — targeted rank-one transfer certificate

For one scalar science parameter, the calibration Fisher needed solely to restore a chosen retained fraction can be concentrated in one generalized transfer mode. The relevant local coordinate is

`eta=a^T g`.

This is a canonical targeted design, not a claim that other transfer modes are experimentally irrelevant. Orthogonal modes may still be required by other science parameters, seven-layer calibration, linearity checks, control diagnostics or nonlinear robustness.

## 6. Likelihood-derived variance budget

The rank-one Fisher condition can be expressed directly as a covariance condition.

For any SPD residual transfer covariance `Sigma`,

`Sigma^-1 >= kappa_* a a^T`

is equivalent to

`boxed{a^T Sigma a <= 1/kappa_*}`.

Therefore the canonical science-coupled transfer coordinate

`eta=a^T g`

has the likelihood-derived variance budget

`boxed{sigma_eta,*^2 = 1/kappa_*}`.

This is the precise object needed to connect transfer stability to the scalar recertification machinery.

In the fully aligned one-dimensional case `ell0=1`,

`kappa_*=q/(1-q)`.

At `q=0.90`,

`kappa_*=9`.

## 7. NG-005 is the same local geometry

The source-amplitude obstruction NG-005 is recovered as the one-dimensional fully aligned case.

Take raw detector Fisher `F0=25` and

`G=b=25`.

At 90% retention,

`kappa_*=9`,

so the independent prior Fisher is

`C=9 F0=225`.

Then

`F_final=25*225/(25+225)=22.5`,

or `sqrt(22.5)=4.7434 sigma`.

This reproduces NUM-006: `C=225` is 90% retention of a raw 5-sigma detector benchmark, not a final 5-sigma certificate.

For a final target `F_final=25` at fixed 90% retention,

`F0=25/0.9=27.7777778`,

`C=250`.

Thus source-amplitude calibration and transfer-gain calibration share the same Schur geometry when their detector scores are fully aligned.

## 8. Direct recertification of the science-coupled mode

Iteration 112 used full matrices `(F_ref,Q,Sigma_f)`. For beta retention alone, RESOURCE-075 permits an exact scalar projection onto `eta`.

Let the same-state transfer reference have Fisher-rate matrix `F_ref`. The Fisher rate for the linear functional `eta=a^T g`, with all orthogonal transfer coordinates treated as nuisance, is

`boxed{R_eta = 1/[a^T F_ref^-1 a]}`.

Let

`D_eta = a^T Q a`,

`sigma_f,eta^2 = a^T Sigma_f a`,

under the Iteration-109 drift convention `Var_drift=tau D_eta/2`.

The usable likelihood-derived variance budget is

`S_eta = 1/kappa_* - sigma_f,eta^2`.

If `S_eta<=0`, the irreducible transfer-stability floor already violates the requested Fisher retention and no faster reference can rescue it.

If `S_eta>0`, RESOURCE-067 applies directly:

`boxed{t_ref,* = 2/(R_eta S_eta)}`,

`boxed{tau_* = S_eta/D_eta}`,

`boxed{r_eta,* = 2 D_eta/(R_eta S_eta^2)}`.

### RQIR-RESOURCE-076 — likelihood-derived transfer recertification

The arbitrary amplitude/phase tolerance matrix can be replaced, for scalar-beta retention, by one likelihood-derived science-coupled transfer mode with physical reference rate, drift rate and stability floor.

This is the requested bridge from detector-level `F_beta|theta` to recertification wall-clock cost.

## 9. Relation to the Iteration-101 5.13% amplitude specification

Iteration 101 derived

`epsilon_g <= 1-sqrt(q)`

from a **deterministic worst-case common multiplicative attenuation** requirement. At `q=0.90` this gives about `5.13%`.

The new Fisher-prior result has different semantics.

For the scalar fully aligned example `F0=25`, `q=0.90`,

`C=225`,

so a Gaussian prior has

`sigma_g=1/sqrt(225)=6.67%`.

These numbers must not be forced to agree: one is a hard/worst-case amplitude-retention specification, the other is a local stochastic nuisance-Fisher specification.

### RQIR-NG-070 — hard transfer bounds and Fisher-prior budgets are different objects

Do not substitute the deterministic 5.13% amplitude bound for a Gaussian prior covariance, or vice versa. State which uncertainty semantics is being used and propagate it through the corresponding likelihood.

## 10. Numerical regressions

`analysis/transfer_likelihood_covariance_budget_iteration113.py` checks:

1. a four-real-component SPD transfer block with free-transfer loss fraction `ell0=0.8` and target `q=0.9`;
2. `kappa_*=7` and exact `F_beta=2.7` for `F0=3`;
3. saturation of the exact LMI boundary to numerical precision;
4. NG-005 scalar recovery `C=225`, `F=22.5`;
5. final-5-sigma correction `F0=27.7777778`, `C=250`, `F=25`;
6. projection of a full reference Fisher/drift/floor model onto `eta`, followed by the scalar recertification optimum;
7. the covariance/Fisher rank-one equivalence `a^T Sigma a=1/kappa_* <=> Sigma^-1 >= kappa_* a a^T` at the boundary.

## 11. What is now closed

Closed algebraically:

- likelihood-derived complex-transfer retention condition;
- the reason a unique full `Sigma_*` is not generally defined;
- canonical science-coupled transfer direction for scalar beta;
- exact rank-one Fisher requirement;
- exact variance budget for that mode;
- its physical reference/drift/floor recertification reduction;
- unification with NG-005/NUM-006 geometry;
- separation between deterministic hard transfer errors and stochastic Fisher priors.

Still open physically:

- same-apparatus `F_ref`, `Q` and `Sigma_f` intervals for Toy009 and Toy014;
- whether the best experimental reference measures the targeted `eta` mode efficiently or should remain a full matrix campaign;
- geometry and additive SI stability/reference channels;
- robust numerical detector ratio `u=R_D,14/R_D,09` and final architecture decision.

## 12. Next admissible gate

Use the source-specific Toy009/Toy014 detector likelihoods to compute their actual conditional transfer objects `(F0,b,G)` and therefore their **science-coupled transfer modes `a_09,a_14` and target `kappa_09,kappa_14`** under one declared retention/final-significance convention.

Then compare those modes with the same-state dual-tone reference Fisher geometry from Iterations 101–103. This can reveal whether one architecture is intrinsically harder to stabilize because its science-coupled transfer direction is poorly observed by the available reference.

If the necessary source-specific transfer Jacobians are not yet physical/common-coordinate objects, keep the result as a normalized generalized-eigenvalue/angle certificate rather than inventing SI stability.

Do not open Toy015 unless the residual dominant decision uncertainty is demonstrably source-dependent.
