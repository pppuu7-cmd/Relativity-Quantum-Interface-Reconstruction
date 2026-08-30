# RQIR Iteration 096 — Decision Value per Characterization Fisher-Second

**Date:** 2026-08-30  
**Status:** Paper-III apparatus-characterization/resource gate; no hardware forecast and no new-physics claim.

## 1. Purpose

Iteration 094 ranked uncertainty intervals by how strongly their contraction shrinks the robust NG-043 Toy009/Toy014 unresolved throughput band. Iteration 095 pushed that sensitivity down to primitive apparatus coordinates.

That is still not a physical measurement priority: two coordinates with different decision leverage may require radically different characterization times.

Iteration 096 closes the missing bridge by attaching an explicit characterization Fisher rate to interval contraction. The resulting quantity is **decision-band reduction per characterization second**.

## 2. RQIR-NUM-005 — active endpoint implementation correction

A reproducibility audit found that the current `analysis/crossover_value_of_information_iteration094.py` used a generic endpoint-name construction inside `contraction_derivative()`. For the source-rate interval this is wrong because the robust upper-time branch uses `R_lo` while the robust lower-time branch uses `R_hi`.

The published Iteration-094 formulas and numerical leverage values already correspond to the correct monotonic endpoints, so the scientific result is unchanged. The code has now been corrected to select endpoints explicitly:

- for `A` and duty `d`: upper branch uses `*_hi`, lower branch uses `*_lo`;
- for `R_src`: upper branch uses `R_lo`, lower branch uses `R_hi`.

The corrected implementation reproduces the stored Iteration-094 leverage ordering and finite contractions.

## 3. Fisher information to uncertainty half-width

Consider one scalar apparatus coordinate `x` with current standard uncertainty `sigma_x` and a fixed confidence multiplier `z`, so the current interval half-width is

`h_x = z sigma_x`.

Define current information

`I_x0 = 1/sigma_x^2 = z^2/h_x^2`.

Let a declared characterization protocol supply Fisher information at constant physical rate

`R_x^char`.

After characterization time `t`,

`I_x(t) = I_x0 + R_x^char t`.

Therefore the interval half-width contracts by

`eta_x(t) = h_x(t)/h_x(0) = [1 + nu_x t]^-1/2`,

where the **normalized characterization information rate** is

`boxed{nu_x = R_x^char/I_x0 = R_x^char sigma_x^2}`.

This normalization is dimensionally `s^-1` and answers a physically meaningful question: how fast does the current information on `x` grow relative to what is already known?

### RQIR-RESOURCE-048 — exact characterization-time closure

For a target half-width contraction `0 < eta <= 1`,

`boxed{t_char(eta) = (eta^-2 - 1)/nu_x}`.

In particular, halving an interval half-width requires

`boxed{t_50 = 3/nu_x}`.

Thus a raw uncertainty interval cannot be converted into a characterization schedule without a physical Fisher rate.

## 4. Decision leverage per second

Iteration 094 defined, for the NG-043 unresolved-band width `W`,

`Lambda_x = (1/W) dW/deta_x` at the current interval.

Using

`d eta_x/dt |_(t=0) = -nu_x/2`,

the initial fractional reduction rate of the unresolved architecture band is

`boxed{Gamma_x = -(1/W) dW/dt = (1/2) Lambda_x nu_x}`.

### RQIR-DESIGN-010 — characterize by decision information rate

The next characterization measurement should be ranked by

`boxed{Lambda_x nu_x}`

or equivalently `Gamma_x`, not by `Lambda_x` alone, not by raw percentage uncertainty, and not by raw Fisher rate alone.

For two candidate measurements `x,y`, `x` is locally better per second iff

`nu_x/nu_y > Lambda_y/Lambda_x`.

This provides a hardware-independent break-even condition. Once experiment-specific characterization rates are supplied, the ranking is immediate.

## 5. Iteration-094 synthetic regression box

The corrected Iteration-094 synthetic box retains the local leverage values

| interval | `Lambda` |
|---|---:|
| Toy014 `R_src` | `0.51911021046` |
| Toy009 `R_src` | `0.42737125993` |
| Toy014 `A` | `0.18109516727` |
| Toy014 duty | `0.15899646329` |
| Toy009 duty | `0.10243207462` |
| Toy009 `A` | `0.03527950118` |

These remain regression-only values, not apparatus forecasts.

If all six coordinates had equal normalized characterization rate `nu`, the Iteration-094 ranking would remain unchanged. But the ranking can reverse once measurement cost is included.

For example, Toy014 `A` overtakes Toy014 `R_src` whenever

`boxed{nu_14,A / nu_14,R > 2.86650504416}`.

Other useful break-even ratios from the same regression geometry are

- Toy009 `R_src` overtakes Toy014 `R_src` if its normalized characterization rate is more than `1.21465868002x` larger;
- Toy014 duty overtakes Toy014 `R_src` only if its normalized characterization rate is more than `3.26491671391x` larger.

The deterministic script explicitly demonstrates a ranking inversion by assigning Toy014 `A` four times the normalized Fisher rate of Toy014 `R_src`.

## 6. Correlated primitive uncertainty

The scalar interval formula assumes one independently contracted coordinate. Iteration 095 already warned that correlated primitive uncertainties require their joint uncertainty geometry.

For a local Gaussian primitive vector `theta` with covariance `C`, and a characterization design supplying Fisher-rate matrix `J >= 0`,

`Cdot = - C J C`.

For a smooth scalar decision boundary `B(theta)` with gradient `g`, its local variance is

`sigma_B^2 = g^T C g`.

Hence

`d sigma_B^2/dt = - g^T C J C g`,

and the local fractional shrink rate of its standard uncertainty is

`boxed{-d ln sigma_B/dt = [g^T C J C g] / [2 g^T C g]}`.

### RQIR-RESOURCE-049 — directional characterization Fisher

Under correlated uncertainty, useful characterization information is the projection of `J` along the covariance-weighted decision direction `C g`.

Two characterization designs can have identical total Fisher `tr J` and very different architecture-decision value. The regression script gives an equal-trace two-parameter example with shrink rates `1.0` and `0.25` solely because the information is oriented differently relative to the decision direction.

### RQIR-NG-049 — raw VOI is not a measurement schedule

A coordinate with the largest `Lambda_x` is not necessarily the best next measurement if its characterization Fisher rate is low. Apparatus decisions must use value **per measurement time**.

### RQIR-NG-050 — total Fisher is not decision Fisher under correlations

For correlated primitive uncertainties, neither `tr J`, the largest diagonal entry of `J`, nor a list of marginal error bars is a valid decision-value proxy. The full covariance and characterization Fisher matrices must be projected through the active decision gradient. At active-set changes, PSD-boundary contact, repeated calibration eigenvalues, or non-Gaussian robust sets, recompute the finite robust contraction rather than using the smooth local formula.

## 7. Consequence for Toy009/Toy014

The research programme can now distinguish three different questions:

1. **Which uncertainty moves the architecture boundary most?** — Iterations 094–095.
2. **Which uncertainty can be reduced fastest by a real measurement?** — characterization Fisher rate.
3. **Which measurement shrinks the robust architecture ambiguity fastest per wall-clock second?** — Iteration 096 `Lambda nu` / matrix directional Fisher.

This means Toy015 remains premature. Before another source search, the physical characterization rates for the current Toy009/Toy014 primitive envelope should be supplied.

## 8. Next admissible gate

Construct physical characterization likelihoods/rates for the primitive coordinates already exposed by Iteration 095:

- two-band science `a2,a4,rho`, including cross-spectral estimation rather than marginal ASD only;
- all seven same-time `2x2` calibration blocks, using injected-reference/transfer-function Fisher rather than treating matrix entries as free numbers;
- Ramsey source parameters `p_E, Omega_E, t_reset, V`;
- control/reference duty and drift parameters.

Then evaluate `Lambda_x nu_x` or the correlated matrix formula on the active Toy009/Toy014 robust branches and allocate characterization time to the highest decision-rate measurement. Only if that physical ranking exposes an intrinsically source-dependent bottleneck should Toy015 be opened.

## 9. Reproducibility

Code:

- corrected `analysis/crossover_value_of_information_iteration094.py`;
- new `analysis/characterization_fisher_value_iteration096.py`.

The new script verifies the exact `t_50=3/nu` law, the Iteration-094 ranking under equal normalized rates, analytic break-even rate ratios, a finite-time derivative check, a deliberate ranking inversion, and the equal-trace correlated-Fisher counterexample.
