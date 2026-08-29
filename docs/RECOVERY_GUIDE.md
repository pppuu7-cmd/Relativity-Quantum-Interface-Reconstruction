# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v2.3

This file is the continuity backbone. The repository, not chat history, is authoritative project memory. Do not mix RQIR with RTK or DSIR. No toy/resource result is an empirical new-physics claim.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance whether gravity is classical, stochastic, quantized, hybrid, emergent or UV-completed in any preferred way.

Central inverse problem:

`P_data(o|s) -> [interface class]`.

Mandatory rules:

- observable first;
- explicit baseline/domain;
- preserve operator ordering;
- source response is not detector observability;
- exact null rank is not statistical identifiability;
- use exact hard constraints;
- compare Fisher/QFI/rates only in one parameter coordinate;
- use centered noise, not raw second moments, unless raw moments are explicitly measured;
- distinguish stationary PSD from phase-referenced/cyclostationary likelihoods;
- include preparation, calibration, detector, controls and wall clock in one resource chain;
- preserve negative/correction results;
- no new-physics interpretation before consistency and competitor-degeneracy gates are closed.

## 2. Ordered source hierarchy

At second order use

`K_T^(2)=(<T>,N,D or chi^R)`

with centered symmetrized noise `N`, commutator/ordered response `D`, and retarded susceptibility `chi^R`. Parent source object: Schwinger–Keldysh / CTP generating functional.

Highest-priority working channel remains Q3 source/backreaction, with Q2/Q5/Q4 cross-checks.

## 3. Exact Toy009/Toy010 baseline

Current source radii:

`(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Balanced Iteration-011 geometry:

- second probe `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact calibration rank `24/25`;
- positive hidden-pair states;
- selected exact equality residual `<1e-15`.

Toy009/Toy010 exact mean/noise equality and ordered-response split remain retained after all later resource/statistical corrections.

Toy009 design rule: optimize only after the whole chain

`source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> F_beta|theta`.

Toy010 design rule: finite calibration geometry actively steers the hidden null direction.

## 4. Statistical identifiability

Primary inference quantity:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

RQIR-NG-005: if the calibration has exact hidden direction `n` and detector signal is locally `mu_D=beta*a*s`, gravitational null calibration cannot self-calibrate `a`; without independent source metrology, local `F_beta|a=0`.

Independent source metrology is required unless a complementary calibration protocol removes the detector-relevant null.

## 5. Mandatory corrections

### RQIR-NUM-001 — exact constraints

Trace+energy are eliminated analytically through a reduced/nullspace basis. The old huge Fisher penalty + threshold pseudoinverse inflated weak-direction information and the large Iteration-013/014 gains are withdrawn.

### RQIR-NUM-002 — Fisher-coordinate Jacobian

Iteration 020 QFI is for physical amplitude `a` in

`rho(a)=I/5+a Delta0`, nominal `a=0.08`.

Current detector Fisher uses fractional amplitude `alpha` with

`a=0.08 alpha`.

Therefore

`F_Q^(alpha)=0.08^2 F_Q^(a)`.

Current values:

- `F_Q^(a)~=13.27068619`;
- `F_Q^(alpha)~=0.0849323916` per ideal accepted single-branch source-metrology copy.

At normalized detector Fisher `S_D=1`, isolated 90% amplitude retention requires `C_alpha=9`, about `105.97` single-branch copies or `52.98` independent plus/minus pair equivalents.

The old downstream `~17 copies for C_a=225` mapping is withdrawn.

Physical preparation rate:

`R_P^(alpha)=p_P eta_P F_Q^(alpha)/t_P`.

### RQIR-CAL-013 — centered noise

For a symmetric pair about `rho0=I/5`, the finite-noise centered covariance derivative is

`C_AB=sym(A,B)-<A>0 B-<B>0 A`

on the trace-zero tangent.

Exact Toy009/Toy010 nullspace is unchanged.

Preferred centered 90%-retention normalized row weights:

- D1 `gamma_mean~1.266e6`, `gamma_cov~0.622e6`;
- D2 `gamma_mean~1.830265e6`, `gamma_cov~0.590127e6`.

## 6. Controls and coherence

RQIR-NG-006 survives the centered correction: without independent timing/geometry/additive priors, D1/D2 profiled Fisher remains numerical zero even at `100x` calibration exposure.

Current first-order centered D2 benchmark at 100 Hz:

- `sigma(delta tau)~5.77425e-3`;
- `sigma_t~9.19001 us`;
- `sigma(b_mean)~7.39168e-5`;
- `sigma(b_cov)~1.30175e-4`.

Current D1 timing benchmark: `~11.0511 us` at 100 Hz.

Largest stored phase gives

`T_coh,min=4.99085067/(2 pi f_gap)`;

at 100 Hz, `~7.94319 ms`.

RQIR-NG-007: if the low-frequency stability floor already exceeds the target prior, no faster white-noise averaging/cadence can repair it.

## 7. Current D2 branch front

At finite reference `y_ref=-4`, centered likelihood, `lambda=1`:

- relational covariance only: `F_beta~0.833432`, `C_alpha*=4.55511`;
- best4 force-cov rows `(0,1,3,7)`: `F_beta~0.899477`, `C_alpha*=0.0500614`;
- best5 `(0,1,3,6,7)`: `F_beta~0.903527`, `C_alpha*=0`;
- all8: `F_beta~0.905293`, `C_alpha*=0`.

RQIR-NG-010: observable replacement can rotate rather than remove a detector-relevant null.

RQIR-NG-011: detector-native force gives potential only relationally without a reference.

RQIR-NG-012: information on one old hidden amplitude is not sufficient if another detector-aligned null survives.

## 8. Covariance measurement corrections and bounds

Current hidden states are nonstationary and the high-value covariance pairs involve noncommuting source observables.

- **NG-014:** current covariance rows are phase-referenced two-time observables, not stationary scalar PSD coordinates.
- **NG-015:** detector-output covariance is not automatically the source symmetrized operator covariance; measurement transfer/order/backaction must be explicit.

Preferred one-shot Gaussian output Fisher:

`I_ij=(d_i mu)^T Sigma^-1(d_j mu)+1/2 Tr[Sigma^-1 Sigma_,i Sigma^-1 Sigma_,j]`.

Physical rate:

`q_ij=p_C eta_C I_ij/t_C`.

- **NG-016:** one affine covariance coordinate in `m` Gaussian outputs has `I_shot<m/2` over the full allowed amplitude range.
- **NG-017:** several simultaneous covariance coordinates share a finite matrix-Fisher budget.
- **RESOURCE-013:** shared shots must use full matrix Fisher, not a sum of independent row times.
- **CAL-014:** covariance signal directions should be Fisher-orthogonal to dominant imprecision/backaction/cross-noise nuisance derivatives.

## 9. Endpoint graph and covariance congestion

Best4 `(0,1,3,7)` uses six unique phase/probe endpoints and two degree-two stars.

Natural cross-covariance encoding gives per-row Fisher `<1/2` and accepted trajectory floor

`N_best4>1.180254e6`.

Graph-congestion result:

- best4 `N>1.180254e6`;
- best5 `N>2.135100e6`;
- all8 `N>3.540762e6`.

**RQIR-RESOURCE-015:** adding a shared covariance row can increase graph spectral radius and reduce per-shot information of the whole set.

At the fixed 90% target, best4 + tiny source prior is favored over best5 unless source metrology cycles are extraordinarily slow; all8 is resource-dominated by best5 in the covariance-only graph architecture.

## 10. Iteration 041 — joint mean/covariance compatibility

The current 14 D2 force-mean source operators have:

- 91 pairs total;
- 7 commuting pairs;
- 84 noncommuting pairs.

Only same-time two-probe pairs commute. Distinct-time force observables do not.

Also

`||[G0,H]||/||G0||~1.90564`,

`||[G1,H]||/||G1||~1.05862`.

**RQIR-NG-019:** the seven phase settings cannot be credited as one disturbance-free multitime source measurement. A shared trajectory needs an explicit weak/continuous/ancilla measurement model including backaction.

**RQIR-RESOURCE-016:** one cycle can count simultaneously toward mean/covariance/control Fisher only if one physical likelihood generates all score vectors and cross-Fisher.

If best4 covariance floor trajectories also supplied all current D2 mean/control information, optimistic per-accepted-cycle requirements are:

- one mean row: `I~1.550738`, `xi~1.245286`;
- timing: `I~0.0254117`;
- mean-offset reference: `I~155.074`;
- covariance-offset reference: `I~49.9999`.

## 11. Iteration 042 — backaction-safe seven-layer mean budget

**RQIR-CAL-015:** `G0(t_j)` and `G1(t_j)` commute and may be paired at each phase; this is the maximal disturbance-free grouping of the 14 force-mean rows.

For single-cycle standardized row sensitivity `xi_mu`, each of seven independent time layers needs

`N_layer=gamma_mean/xi_mu^2`.

At 100 Hz, the seven layer evolution times sum to

`0.0373396341 s`.

**RQIR-RESOURCE-017:** independent phase layers pay `sum_j t_j`; do not use either `7*t_max` or one reused noncommuting source copy.

Transparent `p=.5`, `dead=1 ms` benchmark:

- best4 covariance floor `~5.86402 h`;
- parallel dual-probe mean calibration `45.0852 h` at `xi=1`, `11.2713 h` at `xi=2`, `5.00946 h` at `xi=3`, `1.80341 h` at `xi=5`;
- mean becomes no slower than covariance at `xi_mu~2.77280` (`~3.92134` for sequential probes).

This `xi_mu` is the next detector-transduction target, not beta SNR.

## 12. Iteration 043 — direct diffusive information/backaction proxy

Reference measurement class:

`dy=2 sqrt(eta kappa)<M>dt+dW`,

`dot rho=kappa D[M]rho`.

For normalized mean information,

`xi_mu^2=4 eta kappa T`, so `zeta=kappa T=xi_mu^2/(4 eta)`.

For parallel normalized same-time force observables:

- at `xi=1.245286`, `eta=1`: ordered-response norm retention `~0.856964`, alignment `~0.998751`;
- at the mean-vs-cov wall-time crossover `xi=2.772804`, `eta=1`: retention `~0.493450`, alignment `~0.956925`;
- at the same Fisher with `eta=.5`: retention `~0.29954`.

**RQIR-NG-020:** in this direct non-QND diffusive source-monitoring class, resource-competitive mean Fisher is not free; the current `xi~2.77` benchmark approximately halves the raw ordered-response norm even at ideal efficiency.

**RQIR-RESOURCE-018:** measurement efficiency is a coherence/backaction resource as well as a time resource because fixed Fisher requires `zeta proportional 1/eta`.

This is protocol-specific and does not rule out probe-mediated D2 readout.

## 13. Publication architecture

Fixed in `docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`:

1. RQIR I — operational hierarchy, ordered source information, finite discriminants;
2. RQIR II — statistical identifiability, nuisance geometry, source calibration;
3. RQIR III — physical resources and experiment architecture;
4. later Candidate Gravity paper only after a concrete model passes the reconstruction gates.

## 14. Mandatory open consistency gates

G1 gauge/relational observables; G2 source+apparatus conservation/Bianchi; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a semiclassical/stochastic/classical-gravity+full-QFT/quantum degeneracy; G13 detector covariance/nuisance/measurability.

## 15. Current priority — v2.3

1. Build an explicit **source–probe linear-response D2 detector model** instead of directly monitoring the source operator.
2. Include detector imprecision, reciprocal/backaction force and imprecision-backaction cross-noise subject to the relevant quantum-noise inequality.
3. Derive `xi_mu`, covariance Fisher and source-response attenuation from the same physical coupling/noise model.
4. Insert these into the exact hard-constrained `F_beta|theta` including timing/additive priors and any detector-backaction nuisance.
5. Compare best4 + minimal `C_alpha`, best5 and fully force-native branches in one wall-clock objective.
6. Revalidate second-order timing/gain only if it becomes competitive.
7. Build one common D1/D2 apparatus budget.
8. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood before any interpretation as new physics.

## 16. Continuation protocol

At every substantive iteration:

1. read `RECOVERY_GUIDE.md`, `MASTER_TABLE.md`, latest research log, Toy009/Toy010 and Statistical Identifiability docs;
2. repo is source of truth;
3. do not duplicate closed/active calculations without reason;
4. derive before adding numerical complexity;
5. preserve exact hard constraints and parameter-coordinate consistency;
6. distinguish raw/cen­tered and stationary/phase-referenced quantities;
7. save reproducible code, main document, research log and recovery delta;
8. do not claim new physics before consistency/degeneracy/experimental gates close.
