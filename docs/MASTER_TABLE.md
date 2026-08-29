# RQIR Operational Master Table

**Version:** 2.6  
**Date:** 2026-08-29

The repository is authoritative. RQIR remains separate from RTK/DSIR. No toy, Fisher, resource or detector-model result is an empirical new-physics claim.

## Programme channels

| Channel | Main observable | Main obstacle | Current strategy | Status |
|---|---|---|---|---|
| Q1 clocks | conditional phase/visibility | ordinary relativity + timing drift | profiled likelihood + TDEV/phase controls | OPEN |
| Q2 superposed sources | potential/force/phase spectra | static-density blindness; tomography | finite NP3 + detector transfer | HIGH |
| Q3 source/backreaction | mean, centered noise, ordered/retarded response | source/calibration/control degeneracy + measurement backaction | source+calibration+detector Fisher + explicit source metrology | HIGHEST |
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
- positive states;
- selected exact equality residual `<1e-15`.

Toy009/Toy010 exact null/ordered-response results remain retained.

Primary inference object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Exact rank is not statistical identifiability.

## Mandatory corrections

- **RQIR-NUM-001:** exact trace+energy constraints must be eliminated analytically; huge Fisher penalties + threshold pseudoinverse can falsely remove weak nuisance directions.
- **RQIR-NUM-002:** Fisher/QFI must use one parameter coordinate. Current fractional hidden amplitude `alpha` obeys `a=0.08 alpha`, so `F_Q^(alpha)=0.08^2 F_Q^(a)~=0.0849323916` per ideal accepted single-branch source-metrology copy. Old `~17 copies for C_a=225` mapping is withdrawn.
- **RQIR-CAL-013:** finite-noise covariance rows must linearize the centered noise kernel, not raw second moments, unless raw moments are explicitly measured.

Current centered 90%-retention normalized weights:

- D1 `gamma_mean~1.266e6`, `gamma_cov~0.622e6`;
- D2 `gamma_mean=1.830264703e6`, `gamma_cov=5.901272925e5`.

## Retained structural / negative gates

- **NG-005:** exact gravitational null cannot self-calibrate hidden amplitude.
- **NG-006:** unconstrained timing/geometry/additive systematics can remain detector-degenerate even at very large exposure.
- **NG-007:** a stability floor cannot be repaired by faster white-noise averaging.
- **NG-008:** SI offset tolerances require physical transduction Jacobians.
- **NG-010:** replacing a calibration observable can rotate rather than remove a detector-relevant null.
- **NG-011:** detector-native force gives potential only relationally without a reference.
- **NG-012:** information on one old hidden amplitude is insufficient if another detector-aligned null survives.
- **NG-013:** PSD+bandwidth do not determine source-covariance Fisher without covariance/spectral derivatives.
- **NG-014:** current Toy009 covariance rows are nonstationary phase-referenced two-time observables.
- **NG-015:** detector-output covariance is not automatically the source symmetrized correlator for noncommuting source observables.
- **NG-016:** full-range affine covariance-only Gaussian readout has a positivity-limited per-shot Fisher ceiling.
- **NG-017:** several covariance coordinates share a finite matrix-Fisher budget.
- **NG-018:** the actual best4 shared-endpoint covariance graph limits per-edge Fisher to `<1/2` in the natural cross-covariance encoding.
- **NG-019:** the 14 D2 force means are not one disturbance-free multitime observable bundle; only same-time dual-probe pairs commute.
- **NG-020:** in the standard direct diffusive source-monitor class, resource-competitive mean Fisher entails non-negligible dephasing backaction.
- **NG-021:** reciprocal linear probe mediation cannot beat the source-referred quantum information/backaction product; coupling and probe susceptibility cancel from `S_u S_BA,src >= hbar^2/(4 eta)`.
- **NG-022:** raw signal attenuation is too optimistic; full nuisance profiling further tightens the same-copy backaction limit.
- **NG-023:** QND relative to the isolated source Hamiltonian is not equivalent to nondemolition of the ordered-response resource.

## Centered control benchmark

At `100 Hz`:

- D1 `sigma_t~11.0511 us`, `sigma(b_mean)~8.88857e-5`, `sigma(b_cov)~1.26818e-4`;
- D2 `sigma_t~9.19001 us`, `sigma(b_mean)~7.39168e-5`, `sigma(b_cov)~1.30175e-4`.

Current largest phase gives

`T_coh,min=4.99085067/(2 pi f_gap)`;

at `100 Hz`, `~7.94319 ms`.

## D2 centered Fisher front before physical rate choice

At `y_ref=-4`, `lambda=1`:

| added force-covariance rows | `F_beta|theta` | `C_alpha*` |
|---|---:|---:|
| 0 | `~0.833432` | `4.55511` |
| best4 `(0,1,3,7)` | `~0.899477` | `0.05006144` |
| best5 `(0,1,3,6,7)` | `~0.903527` | `0` |
| all8 | `~0.905293` | `0` |

Natural covariance graph trajectory floors:

- best4: `N>1.180254e6`;
- best5: `N>2.135100e6`;
- all8: `N>3.540762e6`.

**RQIR-RESOURCE-015:** covariance graph congestion can make added rows increase the cost of the entire shared readout.

## Mean/calibration compatibility and conservative scheduling — Iterations 041–042

The 14 force-mean operators contain 91 pairs: only 7 same-time two-probe pairs commute; 84 cross-time pairs do not.

**RQIR-CAL-015:** same-time dual probes may be paired; this is the maximal disturbance-free grouping of current force means.

**RQIR-RESOURCE-016:** a physical cycle may be credited simultaneously to mean/covariance/control Fisher only if one declared likelihood supplies all score vectors, cross-Fisher and backaction.

**RQIR-RESOURCE-017:** independent phase layers pay `sum_j t_j`, not `7*t_max`, and cannot reuse one source copy across noncommuting phases without a measurement model.

At `100 Hz`, `p=.5`, `dead=1 ms`, parallel dual-probe mean calibration takes `45.09 h` at `xi_mu=1`, `11.27 h` at `2`, `5.01 h` at `3`, `1.80 h` at `5`. It equals the best4 covariance floor near `xi_mu=2.7728`.

## Information/backaction front — Iterations 043–046

Direct diffusive proxy:

`xi_mu^2=4 eta kappa T`, `zeta=kappa T=xi_mu^2/(4 eta)`.

At `eta=1`:

- `xi=1.245286` -> response norm `~0.856964`;
- `xi=2.772804` -> response norm `~0.493450`.

**RQIR-RESOURCE-018:** measurement efficiency is a coherence/backaction resource as well as time resource.

### Reciprocal source→probe→detector bound — Iteration 044

For reciprocal linear probe readout,

`S_u S_BA,src >= hbar^2/(4 eta)`.

Gain `g` and probe susceptibility `chi_p` cancel from the input-referred product; optimal imprecision/backaction correlation can saturate but not beat it.

To retain 90% of unperturbed raw detector signal Fisher in the Toy009 dephasing proxy at `eta=1`, require

`xi_shared<=0.723982`, `I_shared<=0.5241495`.

The current optimistic shared target `xi=1.245286` leaves only `~0.73439` raw detector signal Fisher; the mean/covariance crossover target leaves only `~0.24349`.

### Full profiled backaction — Iteration 046

With centered best4 calibration at `lambda=1`, even perfect source-amplitude metrology cannot retain final `F_beta|theta>=0.90` once

`xi_shared>~0.700101`, `I_shared>~0.490142`.

Across best4 trajectories this is at most `~31.61%` of current `gamma_mean`.

At fixed `lambda=1`, required `C_alpha90` grows rapidly: approximately `.211` at `xi=.1`, `.736` at `.2`, `1.787` at `.3`, `3.793` at `.4`, `8.091` at `.5`, `21.42` at `.6`, `128.85` at `.68`, then diverges near `.7001`.

Keeping baseline `C_alpha=0.05006144` instead requires calibration scale about `1.019,1.079,1.199,1.422,1.875,3.106,4.992,8.192,14.783` for `xi=.1,.2,.3,.4,.5,.6,.65,.68,.70`.

**RQIR-RESOURCE-020:** same-copy mean Fisher, source metrology and gravitational calibration exposure form a three-way backaction compensation frontier.

## Concrete QND source-metrology channel — Iteration 047

Because Toy009 `H` is nondegenerate, exact Hermitian QND observables are energy-diagonal. After trace+energy removal the hard QND sector is 3D.

At `y_ref=-4`, relational centered calibration rank changes

`22/23 -> 23/23`

when a complete three-row diagonal QND basis is added.

**RQIR-CAL-016:** current relational null is locally visible to the QND diagonal sector.

Projective energy-basis population metrology gives

- `F_E^alpha(+)=0.0093918844` per accepted plus-branch copy;
- `F_E^alpha(-)=0.0095791291`;
- pair `=0.0189710135`.

The plus branch extracts about `11.1%` of full Toy009 QFI per copy.

**RQIR-PREP-002:** the ideal `Delta0` eigenbasis is not the only useful preparation-metrology channel; energy populations already carry finite hidden-amplitude information.

Best4 residual `C_alpha=0.05006144` costs only about `5.33` plus-branch energy copies (`2.64` plus/minus pair equivalents).

However, complete same-copy projective energy dephasing leaves only `~0.29848` of D2 response norm. Use this metrology on independent/sacrificial copies unless a weaker response-preserving scheme is demonstrated.

## Explicit energy-metrology D2 phase diagram — Iteration 048

Compare source-amplitude closure strategies using

`F_E^alpha=0.0093918844`.

Define

`x_E=(p_C eta_C)/(p_E eta_E) * t_E/t_C`.

Local lower-envelope branch sequence:

- `x_E<2460.53`: **no added force-covariance rows + energy metrology** is cheapest;
- `2460.53<x_E<1.79136e5`: **best4 + tiny energy metrology** is cheapest;
- `x_E>1.79136e5`: **best5 with no source prior** is cheapest.

At equal efficiency, `100 Hz`, `1 ms` covariance readout overhead:

- branch0 ↔ best4 boundary: `t_E~22.0 s`;
- best4 ↔ best5 boundary: `t_E~1602 s~26.7 min`.

**RQIR-RESOURCE-021:** branch choice must use a physically realizable source-metrology rate. If one accepted energy/population readout cycle is faster than ~22 s in the transparent benchmark, even best4 force-covariance is not wall-clock optimal for source-amplitude closure.

## Current working D2 architecture

The current preferred architecture is no longer fixed to best4 covariance. Keep two active branches until source metrology is physically timed:

1. **Branch 0 + independent energy-basis metrology** if source energy/population readout is relatively fast;
2. **best4 covariance + tiny energy-basis metrology** if source readout is intermediate;
3. best5 only if source metrology is very slow.

Strong same-copy mean monitoring is not favored in the generic reciprocal linear class. Independent/sacrificial mean-calibration copies remain the conservative baseline.

## Publication architecture

See `docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`:

1. RQIR I — operational hierarchy / ordered source information / finite discriminants;
2. RQIR II — statistical identifiability / nuisance geometry / source calibration;
3. RQIR III — physical resources / experiment architecture;
4. later Candidate Gravity paper only after a concrete model passes reconstruction gates.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy; G13 detector covariance/nuisance/measurability.

## Priority ranking v2.6

1. Build a minimally physical **energy/population source-metrology protocol** and estimate `t_E,p_E,eta_E`; determine which side of the ~22-s branch0/best4 boundary the intended source lies on.
2. Keep independent/sacrificial seven-layer force-mean calibration as the backaction-safe baseline and assign its physical force SNR/transduction.
3. Only pursue shared strong science monitoring if a concrete QND/backaction-evading, nonreciprocal, coherent-noise-cancellation or ancilla architecture explicitly violates an assumption of NG-021/022.
4. Recompute total wall-clock for branch0 vs best4 including common mean calibration, timing/additive controls, science integration and source reset/preparation.
5. Build one common D1/D2 apparatus budget at fixed source mass/gap/coherence/separation.
6. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.
7. After detector/inference geometry stabilizes, close gauge, conservation, renormalization and full stress-energy gates.
