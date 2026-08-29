# RQIR Iteration 044 — Reciprocal Linear Probe Information–Backaction Bound

**Date:** 2026-08-29  
**Scope:** probe-mediated D2 measurement architecture after Iteration 043.  
**Status:** quantum-noise/resource gate for reciprocal linear detectors; not a complete apparatus model and not a new-physics claim.

## 1. Question

Iteration 043 used a direct diffusive monitor of the Toy009 source force observable and found that the mean Fisher needed for a resource-competitive shared trajectory can strongly attenuate the ordered-response signal.

The intended D2 architecture is less direct:

`source -> gravitational/source-probe coupling -> probe -> detector`.

The obvious hope is that probe transduction can amplify the source information while reducing source disturbance. Iteration 044 tests that hope in the broad class of **reciprocal linear quantum detectors**.

## 2. Minimal reciprocal source–probe model

For one relevant source coordinate `u`, let a probe coordinate obey

`x_p = chi_p (g u + F_BA)`,

and detector output be

`y = x_p + x_imp`.

Here

- `g` is the reciprocal source–probe coupling;
- `chi_p` is the probe susceptibility in the measured quadrature/frequency band;
- `x_imp` is detector imprecision;
- `F_BA` is detector backaction force on the probe.

Reciprocity transmits detector backaction through the same source–probe channel. The detector-induced source force therefore scales as

`F_src^BA = g chi_p F_BA`.

For the relevant real quadrature, use the standard normalized quantum-noise inequality

`S_xx S_FF - S_xF^2 >= hbar^2/(4 eta)`,

where `eta<=1` represents net information efficiency in this reference class.

The result is deliberately apparatus-neutral: no specific mechanical resonator, optical cavity or atomic probe is assumed.

## 3. Source-referred measurement noise

The detector-output noise is

`S_y = S_xx + |chi_p|^2 S_FF + 2 Re(chi_p S_xF)`.

The source-referred imprecision is therefore

`S_u = S_y/(g^2 |chi_p|^2)`.

The source backaction PSD is

`S_BA,src = g^2 |chi_p|^2 S_FF`.

Multiplying gives, for the relevant optimized real quadrature,

`S_u S_BA,src`

`= S_xx S_FF + (chi_p S_FF + S_xF)^2 - S_xF^2`

and hence

`boxed: S_u S_BA,src >= hbar^2/(4 eta)`.

The coupling `g` and probe susceptibility `chi_p` cancel exactly from this input-referred product.

Optimal imprecision–backaction correlation can saturate the bound. For fixed `S_FF`, the saturating choice is

`S_xF = -chi_p S_FF`,

`S_xx = chi_p^2 S_FF + hbar^2/(4 eta S_FF)`.

Thus variational/correlated readout can remove avoidable probe backaction from the **detector output**, but reciprocal backaction on the source still enforces the same input-referred information–disturbance product.

## 4. RQIR-NG-021 — reciprocal linear probe cannot give free shared-copy gain

> In a reciprocal linear source–probe detector satisfying the quantum noise inequality, source-referred measurement imprecision times detector-induced source backaction is bounded below by `hbar^2/(4 eta)`. Increasing coupling or probe susceptibility can redistribute signal and technical detector noise but cannot reduce this reciprocal quantum-limited product.

This is a detector-class statement, not a theorem about arbitrary quantum measurements. It can be evaded only by changing assumptions — for example a genuinely QND variable, backaction-evading quadrature, nonreciprocal interaction, ancilla protocol, measurement on a sacrificial preparation, or a detector model outside the present linear reciprocal class.

## 5. Fisher/dephasing form

Use the white-noise convention matched to Iteration 043:

`I_u = T/S_u`,

`zeta = S_BA,src T/hbar^2`.

Then

`boxed: zeta >= I_u/(4 eta)`.

For standardized sensitivity `xi_mu=sqrt(I_u)`,

`boxed: zeta >= xi_mu^2/(4 eta)`.

This is exactly the ideal information/dephasing relation used by the direct diffusive monitor in Iteration 043.

Therefore a reciprocal probe can outperform the direct monitor against technical noise and hardware constraints, but at the quantum limit it cannot reduce the minimum source dephasing at fixed same-copy Fisher.

## 6. Toy009 ordered-response consequence

Iteration 043 already supplies the exact Toy009 response attenuation under the corresponding commuting same-time force-basis dephasing channel.

At ideal efficiency, requiring the **raw detector signal Fisher** to retain 90% of its unperturbed value means the response norm must retain at least

`sqrt(0.9) ~= 0.948683`.

Inverting the Toy009 dephasing response gives

`boxed: xi_mu <= 0.723982`

for this 90%-raw-detector-Fisher requirement.

For comparison:

- 90% response-amplitude retention allows `xi_mu <= 1.02636`;
- 80% response-amplitude retention allows `xi_mu <= 1.50267`.

These are ideal `eta=1` bounds in the present dephasing proxy.

At lower efficiency the allowed `xi_mu` scales as `sqrt(eta)` for a fixed response-retention target. For 90% raw detector Fisher:

- `eta=1`: `xi_mu,max ~= 0.72398`;
- `eta=0.8`: `~0.64755`;
- `eta=0.5`: `~0.51193`;
- `eta=0.2`: `~0.32377`.

## 7. Conflict with the current shared-trajectory resource targets

Iteration 041 found that if the best-four covariance cycle count were also to supply the full current mean Fisher, the required per-cycle mean sensitivity would be

`xi_mu ~= 1.245286`.

At the reciprocal quantum limit, the Toy009 response norm is then only

`~0.856964`,

so the corresponding raw detector signal Fisher, if detector noise were otherwise unchanged, is at most

`boxed: ~0.73439`

of the unperturbed value.

Iteration 042 found the independent mean-vs-covariance wall-time crossover at

`xi_mu ~= 2.772804`.

At that strength the response norm is

`~0.49345`,

corresponding to only

`boxed: ~0.24349`

of the unperturbed raw detector signal Fisher under the same optimistic fixed-noise comparison.

Thus the attractive idea

`same source copy -> enough mean Fisher + covariance Fisher + essentially unchanged ordered-response signal`

is incompatible with the reciprocal linear quantum-limited reference class at the present Toy009 targets.

## 8. Important qualification: this does not kill D2

The result concerns **same-copy shared acquisition**.

A viable D2 strategy may still use:

1. independent/sacrificial source preparations for strong mean calibration;
2. a much weaker science-trajectory monitor;
3. QND/backaction-evading probe variables;
4. nonreciprocal or coherent-noise-cancellation architectures;
5. ancilla-assisted correlation measurements;
6. a detector that measures the external probe without transmitting the same backaction channel to the relevant source coherence.

Any such proposal must write its actual Hamiltonian/input-output map and demonstrate where the assumptions behind RQIR-NG-021 are changed.

## 9. Relation to full profiled Fisher

The squared response-retention numbers above are only an **optimistic raw detector-signal Fisher diagnostic**. Measurement backaction can also rotate source nuisance directions, alter calibration derivatives and introduce new detector noise parameters.

Therefore one must not identify `response_norm^2` with the final `F_beta|theta`.

The next calculation should propagate the reciprocal backaction superoperator through the complete detector/nuisance Jacobian and recompute the profiled Fisher. That will test whether the present shared-copy branch degrades even more strongly once nuisance geometry is included.

## 10. Reproducibility

Code:

`analysis/d2_reciprocal_linear_probe_bound_iteration044.py`

The script:

- verifies the source-referred quantum noise product analytically/numerically for arbitrary `g` and `chi_p`;
- verifies saturation by optimal imprecision–backaction correlation;
- reproduces the Iteration-043 minimum dephasing law;
- inverts the exact Toy009 dephasing proxy for response-retention limits;
- records regression values for the current shared/crossover resource targets.

## 11. Next gate

Propagate the dephasing/backaction channel through the **full hard-constrained D2 Fisher model** rather than only the hidden signal vector:

- transform beta signal and all 22 source nuisance detector derivatives;
- include the current centered calibration/source-preparation information;
- profile the resulting Fisher;
- determine the maximum same-copy mean Fisher compatible with final `F_beta|theta >= 0.90`.

In parallel, keep the independent-preparation time-layer branch from Iteration 042 as the backaction-safe baseline.