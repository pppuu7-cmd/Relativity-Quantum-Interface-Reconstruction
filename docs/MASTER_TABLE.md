# RQIR Operational Master Table

**Version:** 1.0  
**Date:** 2026-08-29

`OPEN` means the required comparison has not yet been demonstrated at RQIR precision.

| Channel | Operational observable | Main obstacle | Current discriminator strategy | Status |
|---|---|---|---|---|
| Q1 Quantum clocks | conditional phase, visibility, correlations | ordinary relativistic/control effects | profiled likelihood with explicit calibration | OPEN |
| Q2 Superposed sources | potential/force/phase spectra | static density phase blindness; full history becomes tomography | finite NP3 multiprobe calibration + detector transfer | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, symmetrized noise, retarded response | response can be projected away by calibration/detector geometry | joint source+calibration+detector Fisher optimization | HIGHEST PRIORITY |
| Q4 Gravity-mediated QI | entanglement/non-Gaussianity/scaling | entanglement alone is not unique to quantized gravity | common detector likelihood across interface classes | HIGH PRIORITY |
| Q5 Geometry fluctuations | noise/response spectra | matter, intrinsic-gravity and technical noise degeneracies | joint N/chi/covariance fit | HIGH PRIORITY |
| Q6 Causal/process | relational timing/process observables | control-system nonclassicality | gravity-dependent scaling with nuisance closure | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections | tiny universal pieces and local-UV degeneracy | cross-process long-range/nonanalytic fingerprints | OPEN |

## Current mathematical coordinate

`K_T^(2)=(<T>,N,D or chi^R)`, with the Schwinger-Keldysh/CTP functional as parent source object. Operator ordering is not to be merged without an explicit identity/limit.

## Retained closed/negative results

- RQIR-NG-001 / Toy002: static density phase blindness.
- RQIR-NG-002 / Toy003: minimal response split has an energy confound.
- Toy004: `(<H>,<B>,N_B)` does not determine ordered response.
- PE-1 / Toy005: exact Newtonian one-channel embedding; still NP2.
- RQIR-NG-003 / Toy006: generic complete density history becomes state tomography.
- Toy007: first finite NP3; `eta_R~0.4577`, `s_min~1.463e-3`, condition `~3.18e3`.
- RQIR-NG-004: one extra independent exact row kills a one-dimensional exact nullspace.
- Toy008: soft-nullspace scan motivates likelihood/Fisher over maximal exact rank.
- RQIR-CAL-001: independent beta-blind calibration cannot reduce profiled Fisher under stated assumptions.

## Statistical identifiability

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab` and, after whitening, `F_beta|theta=||(I-P_J)s_tilde||^2`.

For two whitened response bands with a free antisymmetric tilt nuisance, `S_eff=4 P2 P4/(P2+P4)`. Losing one band kills the shape discriminator. Independent static amplitude calibration `C` gives `F=S_eff C/(S_eff+C)`.

## Detector branches

D1 matter-wave phase: full-period passive integration cancels the chosen AC bands; deliberate lock-in/echo control is mandatory. Repeated switch contrast is an explicit resource.

D2 force: at a true force-noise floor, mechanical susceptibility gives no free force-domain Fisher gain. Realistic thermal/backaction/imprecision covariance remains open.

## Toy009 source baseline — Iteration 010

Accepted source radii approximately `(1.00000,1.60090,1.77911,2.60901,5.90724)`. Fixed inherited NP3 calibration: rank `24/25`, states positive, exact selected residual `<6e-16`, `eta_R~0.568823`, `s_min~1.5122e-3`, condition `~3.03e3`. Relative to Toy007, ideal two-band D1 gain `x1.22184`, D2 gain `x1.40358`.

Negative detector-only candidate reached D1 `x5.36`, D2 `x4.17` before calibration but was almost projected away (`eta_R~0.03`, condition `~1.75e4`). This is retained as the main counterexample motivating downstream-aware design.

Toy009 four/six-switch D1 control gives more information than Toy007 eight-switch with fewer hard switches.

### RQIR-DESIGN-001

Optimize in the order `source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> profiled likelihood`. Upstream response gain is not sufficient.

## Joint Toy009 calibration geometry — Iteration 011

Main file: `docs/TOY009_JOINT_CALIBRATION_GEOMETRY.md`.

Accepted balanced calibration:

- `y1=-3.7766873837`;
- sampling phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- rank remains `24/25`;
- exact selected equality residual `<1e-15`;
- states positive;
- `eta_R~0.573426`;
- `s_min~1.99954e-3` (~+32% vs inherited Toy009);
- condition `~2313` (~24% better);
- D1 `S_eff x1.7268` vs inherited Toy009;
- D2 `S_eff x1.6838` vs inherited Toy009.

Cumulative ideal two-band detector-source gains vs Toy007 are approximately D1 `x2.11`, D2 `x2.36`.

An aggressive Pareto point reaches roughly `x1.81` in both D1/D2 vs inherited Toy009 but sits near the old conditioning guard and is not the operational baseline.

### RQIR-CAL-002

Calibration geometry is an active information resource: at fixed source and fixed NP3 constraint count/type, probe location and sampling phases rotate the surviving state-difference direction relative to detector harmonics, changing downstream information. Scope: finite-dimensional numerical design result, not universal theorem.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy audit; G13 detector covariance/nuisance/measurability.

## Priority ranking v1.0

1. **Direct covariance-profiled Fisher optimization:** replace detector-agnostic/equal-noise `S_eff` and eta/s_min proxy guards by a declared detector covariance and directly optimize `F_beta|theta`.
2. **Realistic D2 covariance:** thermal force, backaction, displacement imprecision; compare one-mode, dual-mode and tuned strategies.
3. **Continuous D1 control:** compare continuous/phase-modulated sensitivity with four/six hard switches under the same bandwidth, contrast, dead-time and timing-jitter budget.
4. **Common resource budget:** D1/D2 at one source mass, gap, coherence, separation and integration budget.
5. **Interface-class fingerprints:** semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.
6. **Relativistic/full-stress embedding:** only after detector/inference geometry stabilizes, close conservation, gauge and renormalization gates.
