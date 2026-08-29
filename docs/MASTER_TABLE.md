# RQIR Operational Master Table

**Version:** 2.3  
**Date:** 2026-08-29

The repository is authoritative. RQIR remains separate from RTK/DSIR. No toy/resource result is an empirical new-physics claim.

## Programme channels

| Channel | Main observable | Main obstacle | Current strategy | Status |
|---|---|---|---|---|
| Q1 clocks | conditional phase/visibility | ordinary relativity + timing drift | profiled likelihood + TDEV/phase controls | OPEN |
| Q2 superposed sources | potential/force/phase spectra | static-density blindness; tomography | finite NP3 + detector transfer | HIGH |
| Q3 source/backreaction | mean, centered noise, ordered/retarded response | source/calibration/control degeneracy | joint source+calibration+detector Fisher + source metrology | HIGHEST |
| Q4 gravity-mediated QI | entanglement/non-Gaussianity | non-unique interpretation | common likelihood across model classes | HIGH |
| Q5 geometry fluctuations | noise/response spectra | matter/intrinsic/technical degeneracy | joint covariance/response inference | HIGH |
| Q6 causal/process | relational timing/process observables | control confounds | nuisance-closed scaling tests | OPEN |
| Q7 low-energy QG EFT | nonanalytic/long-range corrections | tiny signal/local-UV degeneracy | cross-process fingerprints | OPEN |

## Exact/source baseline

Toy009 radii:

`(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Balanced Iteration-011 geometry:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact rank `24/25`;
- positive states and selected equality residual `<1e-15`.

Toy009/Toy010 exact null/ordered-response results remain retained.

Primary inference object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Exact rank is not statistical identifiability.

## Mandatory corrections

- **RQIR-NUM-001:** exact trace+energy constraints must be eliminated analytically; huge Fisher penalties + threshold pseudoinverse can falsely remove weak nuisance directions.
- **RQIR-NUM-002:** Fisher/QFI must use one parameter coordinate. Current fractional hidden amplitude `alpha` obeys `a=0.08 alpha`, so `F_Q^(alpha)=0.08^2 F_Q^(a)~=0.0849323916` per ideal accepted single-branch source-metrology copy. Old `~17 copies for C_a=225` mapping is withdrawn.
- **RQIR-CAL-013:** finite-noise covariance rows must linearize the centered noise kernel, not raw second moments, unless raw moments are explicitly the measured observable.

Current centered 90%-retention normalized weights:

- D1 `gamma_mean~1.266e6`, `gamma_cov~0.622e6`;
- D2 `gamma_mean~1.830265e6`, `gamma_cov~0.590127e6`.

## Retained structural gates

- **NG-005:** exact gravitational null cannot self-calibrate hidden amplitude.
- **NG-006:** unconstrained timing/geometry/additive systematics can remain detector-degenerate even at very large exposure.
- **NG-007:** stability floor cannot be repaired by faster white-noise averaging.
- **NG-008:** SI offset tolerances require physical transduction Jacobians.
- **NG-010:** replacing a calibration observable can rotate rather than remove a detector-relevant null.
- **NG-011:** detector-native force gives potential only relationally without a reference.
- **NG-012:** information on one old hidden amplitude is insufficient if another detector-aligned null survives.
- **NG-013:** PSD+bandwidth do not determine source-covariance Fisher without covariance/spectral derivatives.
- **NG-014:** current Toy009 covariance rows are nonstationary phase-referenced two-time observables.
- **NG-015:** detector-output covariance is not automatically the source symmetrized correlator for noncommuting source observables.
- **NG-016:** full-range affine covariance-only Gaussian readout has a positivity-limited per-shot Fisher ceiling.
- **NG-017:** multiple affine covariance coordinates share a finite matrix-Fisher budget.
- **NG-018:** the actual best4 shared-endpoint covariance graph limits per-edge Fisher to `<1/2` in the natural cross-covariance encoding.
- **NG-019:** the 14 D2 force means are not one disturbance-free multitime observable bundle; only same-time dual-probe pairs commute.
- **NG-020:** in the standard direct diffusive source-monitoring class, resource-competitive mean Fisher entails non-negligible dephasing backaction.

## Centered control benchmark

At `100 Hz`:

- D1 `sigma_t~11.0511 us`, `sigma(b_mean)~8.88857e-5`, `sigma(b_cov)~1.26818e-4`;
- D2 `sigma_t~9.19001 us`, `sigma(b_mean)~7.39168e-5`, `sigma(b_cov)~1.30175e-4`.

Current largest stored phase gives

`T_coh,min=4.99085067/(2 pi f_gap)`;

at `100 Hz`, `T_coh,min~7.94319 ms`.

## D2 centered branch front

At `y_ref=-4`, `lambda=1`:

| added force-covariance rows | `F_beta|theta` | `C_alpha*` |
|---|---:|---:|
| 0 | `~0.833432` | `4.55511` |
| best4 `(0,1,3,7)` | `~0.899477` | `0.0500614` |
| best5 `(0,1,3,6,7)` | `~0.903527` | `0` |
| all8 | `~0.905293` | `0` |

Covariance-only graph cost:

- best4: `N>1.180254e6` accepted shared trajectories;
- best5: `N>2.135100e6`;
- all8: `N>3.540762e6`.

**RQIR-RESOURCE-015:** covariance graph congestion can make added rows increase the cost of the entire shared readout.

At the fixed 90% target, best4 + a tiny independent source prior is favored over best5 unless source verification is extraordinarily slow.

## Iteration 041 — joint mean/covariance compatibility

The 14 force-mean operators contain 91 pairs:

- 7 commuting pairs;
- 84 noncommuting pairs.

The only commuting pairs are `G0(t_j),G1(t_j)` at the same phase. Also

`||[G0,H]||/||G0||~1.90564`,

`||[G1,H]||/||G1||~1.05862`.

Thus the seven phase settings are distinct quantum measurement layers unless an explicit weak/continuous/backaction model is supplied.

**RQIR-RESOURCE-016:** one physical cycle may be credited to mean/covariance/control Fisher simultaneously only if one declared likelihood supplies all score vectors and cross-Fisher including backaction/correlations.

If the best4 covariance floor `N=1.180254e6` trajectories also carried all D2 mean/control information, optimistic average per-cycle requirements would be:

- mean row `I~1.550738`, `xi~1.245286`;
- timing `I~0.0254117`;
- mean-offset reference `I~155.074`;
- covariance-offset reference `I~49.9999`.

## Iteration 042 — backaction-safe seven-layer mean budget

**RQIR-CAL-015:** same-time dual probes can be paired; this is the maximal disturbance-free grouping of the 14 current mean rows.

**RQIR-RESOURCE-017:** independent phase settings pay their own coherence/evolution time, so use `sum_j t_j`, not `7*t_max`; do not reuse one source copy across noncommuting phases without a measurement model.

At `100 Hz` the seven evolution times sum to `0.0373396341 s`.

For per-accepted-cycle standardized mean sensitivity `xi_mu`, parallel dual-probe wall time is

`T_mean = gamma_mean/(xi_mu^2 p) * sum_j(t_j+d)`.

Transparent `p=0.5`, `d=1 ms` benchmark:

- best4 covariance floor `~5.86402 h`;
- mean calibration `45.0852 h` at `xi=1`, `11.2713 h` at `xi=2`, `5.00946 h` at `xi=3`, `1.80341 h` at `xi=5`;
- mean becomes no slower than covariance at `xi_mu~2.77280` for parallel dual-probe readout (`~3.92134` if probes are sequential).

## Iteration 043 — information/backaction proxy

Use the standard direct diffusive source-monitoring reference class

`dy=2 sqrt(eta kappa)<M>dt+dW`, `dot rho=kappa D[M]rho`,

so for normalized mean sensitivity

`xi_mu^2=4 eta kappa T`, `zeta=kappa T=xi_mu^2/(4 eta)`.

For parallel normalized same-time force observables:

- at optimistic shared target `xi=1.245286`, `eta=1`, D2 ordered-response norm retention `~0.856964`, alignment `~0.998751`;
- at mean-vs-covariance crossover `xi=2.772804`, `eta=1`, response norm retention `~0.493450`, alignment `~0.956925`;
- at the same Fisher, retention falls to `~0.29954` for `eta=0.5`.

**RQIR-RESOURCE-018:** measurement efficiency is a coherence/backaction resource as well as a time resource; at fixed Fisher lower `eta` requires stronger disturbance.

This proxy is protocol-specific and does not rule out a probe-mediated D2 detector.

## Publication architecture

See `docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`:

1. RQIR I — operational hierarchy / ordered source information / finite discriminants;
2. RQIR II — statistical identifiability / nuisance geometry / source calibration;
3. RQIR III — physical resources / experiment architecture;
4. later Candidate Gravity paper only after a concrete model passes reconstruction gates.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy; G13 detector covariance/nuisance/measurability.

## Priority ranking v2.3

1. Build an explicit **source–probe linear-response D2 detector model** rather than directly monitoring the source operator.
2. Include detector imprecision, reciprocal/backaction force and imprecision-backaction cross-noise subject to the appropriate quantum-noise inequality.
3. Derive physical per-cycle `xi_mu`, covariance matrix Fisher and source-response attenuation from the same coupling/noise model.
4. Insert these into the full hard-constrained `F_beta|theta`, including timing/additive priors and any new detector backaction nuisance.
5. Compare best4 + minimal `C_alpha`, best5 and fully force-native branches by one wall-clock objective.
6. Revalidate second-order timing/gain only if it becomes competitive.
7. Build one common D1/D2 apparatus budget.
8. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood before any new-physics interpretation.
