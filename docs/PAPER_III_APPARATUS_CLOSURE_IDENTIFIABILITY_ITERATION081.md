# RQIR Iteration 081 — Paper III Apparatus-Closure Identifiability Audit

**Date:** 2026-08-30  
**Status:** negative/closure result for the apparatus layer; not a hardware forecast and not a new-physics claim.

## 1. Question

Can the repository, as it stands after Iteration 080, produce an absolute Toy009/Toy014 wall-clock prediction from its existing physical benchmark files without inserting any new detector-noise or source-metrology performance assumption?

**No.** The repository now contains the correct transduction/rate formulas and several explicitly illustrative benchmarks, but it does not yet contain one declared apparatus data set that fixes the absolute detector PSD/cross-PSD normalization, seven calibration Jacobians/rates, and independent source-metrology coupling/reset/visibility in one consistent experiment.

This is a useful negative result because it identifies the exact remaining experimental inputs rather than replacing them with guessed ASD values.

## 2. What the repository already fixes

Existing physical files provide:

- Newtonian source-to-potential/phase scaling, including
  `Gamma_G = G m_s m_p T_D/(hbar L_0)`;
- the two-band detector design law and spectral-tilt-profiled shape information;
- D2 force-domain transfer and equivalent-force PSD formalism;
- native Fisher-rate formulas for D1/D2 mean calibration, covariance calibration, timing, offsets and gain references;
- source-metrology Fisher-per-copy/rate coefficients for energy/pointer/Ramsey channels;
- acceptance/reset/visibility/coherence structure;
- Toy009/Toy014 source-specific `gamma_mean`, timing targets and coherence spans;
- the Iteration-077 architecture certificate and Iteration-080 inverse rate envelope.

These are enough to specify **what must be measured**, but not enough to infer the missing measurements themselves.

## 3. RQIR-NG-032 — absolute wall-clock scale is not identifiable from normalized Fisher geometry

For a fixed transfer function, let an unknown common detector PSD normalization transform as

`S(f) -> lambda S(f)`.

Matched-filter detector and calibration Fisher rates then transform as

`R_beta -> R_beta/lambda`,

`R_cal,j -> R_cal,j/lambda`.

The dimensionless calibration ratio

`x = gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`

is invariant under this common rescaling, but

`T_sci + T_cal`

scales linearly with `lambda`.

Therefore normalized source/calibration geometry and architecture ratios cannot determine absolute seconds without at least one absolute detector Fisher-rate/noise normalization.

More generally, if **all** Fisher rates are multiplied by a common positive factor `k`, then `(x,y,d)` are unchanged while

`T_total -> T_total/k`.

Thus the Iteration-077 compressed architecture certificate selects branches only after an absolute rate scale is supplied; it cannot generate that scale by itself.

## 4. Independent source-rate freedom

The source-metrology fraction is

`y = C_prep R_beta/(Z^2 R_src)`.

The mature Toy009 zero-reset Ramsey result fixes only the dimensionless coefficient

`R_src/(p_E Omega_E) = 0.0025234392`

at its rate optimum. In the general physical case,

`R_src = p_E F_alpha(phi,V)/(t_reset + phi/Omega_E)`.

Hence `R_src` remains undetermined until the apparatus supplies at least `p_E`, `V`, `Omega_E` and `t_reset` (or an experimentally measured source-metrology Fisher rate directly). The same issue applies to the Gaussian-pointer branch with its protocol-specific coupling.

This source-rate freedom is independent of the detector PSD normalization unless a concrete apparatus model physically couples them.

## 5. RQIR-APP-001 — minimum apparatus closure vector

For each candidate architecture, an absolute Paper-III wall-clock certificate requires the following **measured, declared, or externally sourced** data.

### Science detector

1. physical source/probe geometry and mass/gap/drive parameters in one consistent coordinate convention;
2. complex detector transfer functions at the retained science bands, including finite acquisition windows;
3. the full output/equivalent-force PSD or covariance matrix, including cross-spectrum where two probes/channels are read simultaneously;
4. live-time/acceptance/cycle definition sufficient to turn per-cycle information into `R_beta`;
5. the complete detector nuisance Jacobian used for the spectral-tilt/timing/geometry/additive profile.

### Seven calibration layers

For every layer `j`:

6. the physical two-probe calibration Jacobian `J_j(f)` in the same output coordinate as the science readout;
7. its full `2x2` PSD/cross-PSD matrix (or a demonstrated common PSD model);
8. layer-specific acceptance, acquisition window and reset/dead time;
9. the resulting matrix Fisher rate `R_cal,j` with uncertainty.

### Independent source metrology

10. preparation success/acceptance;
11. Ramsey/pointer coupling rate (`Omega_E`, `Gamma_E`, or directly measured Fisher rate);
12. visibility/readout fidelity;
13. fresh-source reset/repreparation and readout overhead;
14. source coherence/stability over the metrology window;
15. resulting `R_src` and uncertainty.

### Controls/references

16. timing-reference low-frequency stability characterization (Allan/TDEV/PSD or equivalent) over the campaign timescale;
17. geometry/additive/gain reference rates and recertification cadence;
18. control/reference duty `d` and its uncertainty/correlation with science/calibration blocks.

With these inputs, Iterations 077/080 give the full wall-clock comparison without introducing an arbitrary standardized `xi` or guessed seconds conversion.

## 6. Why old benchmark numbers cannot be promoted to an apparatus forecast

`PROBE_PROTOCOL_002B_PHYSICAL_SCALING.md` explicitly labels its `sigma_phi=1e-3 rad`, `L_0=10 um`, `T_D=1 s` and mass examples as benchmark scaling, not realization claims.

`DETECTOR_BRANCH_D1_D2_COMPARISON.md` likewise labels the `1e-21 N/sqrt(Hz)` D2 point as deliberately optimistic and detector-agnostic.

`NATIVE_CALIBRATION_REFERENCE_FISHER_RATES.md` uses explicit unit-coupling examples to expose scaling and states that hardware-specific transduction/PSD values remain open.

Therefore importing any of those illustrative values as though they were measurements would violate the repository's own epistemic discipline.

## 7. Scientific consequence for Paper III

Paper III now has a clean boundary between two tasks:

- **closed theory/resource algebra:** Fisher profiling, source prior, shot/rate conversion, matrix calibration Fisher, reset/coherence/control duty, architecture certificate and target-duration envelope;
- **open apparatus instantiation:** supply the physical rate normalizations and uncertainty intervals listed in RQIR-APP-001.

This means the remaining Paper-III scientific uncertainty is no longer primarily algebraic. It is an apparatus-data/transfer-function problem.

## 8. Decision

Do not create a forced absolute hour/day forecast from the current illustrative benchmarks.

The next admissible Paper-III gate is to build a **declared reference apparatus model** whose parameters are either:

1. directly measured/externally sourced from a specific platform, with citations and uncertainty ranges; or
2. explicitly presented as a parameterized design envelope rather than a forecast.

Only after that model supplies `R_beta`, seven `R_cal,j`, `R_src`, `d` and uncertainties should Toy009/Toy014 robust dominance be evaluated with NG-030.

## 9. Reproducibility

Run

`python analysis/apparatus_closure_identifiability_iteration081.py`.

The script verifies:

- common detector PSD scaling leaves `x` invariant but rescales absolute detector wall time;
- independent source-rate freedom changes `y` arbitrarily until source metrology is physically normalized;
- a common Fisher-rate rescaling leaves `(x,y)` unchanged while changing total seconds;
- the mature Toy009 Ramsey coefficient by itself does not fix `R_src` without apparatus coupling/reset inputs.
