# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v2.2

This file is the continuity backbone. The repository, not chat history, is authoritative project memory. Do not mix RQIR with RTK or DSIR. No toy/resource result is an empirical new-physics claim.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance whether gravity is classical, stochastic, quantized, hybrid, emergent or described by a preferred UV theory.

Central inverse problem:

`P_data(o|s) -> [interface class]`.

Rules:

- observable first;
- explicit baseline/domain;
- preserve operator ordering;
- retain negative/correction results;
- source response is not detector observability;
- exact nulls are not statistical identifiability;
- use exact hard constraints;
- compare Fisher/QFI/rates only in the same physical parameter coordinate;
- distinguish centered noise from raw second moments;
- distinguish stationary PSD from phase-referenced/cyclostationary likelihoods;
- every substantive numerical result gets reproducibility code;
- no new-physics claim before classical/stochastic/full-QFT/hybrid alternatives and relativistic consistency gates are closed.

## 2. Ordered source hierarchy

At second order use

`K_T^(2)=(<T>,N,D or chi^R)`

with centered symmetrized noise `N`, ordered/commutator response `D`, and retarded susceptibility `chi^R`. Parent source object: Schwinger–Keldysh/CTP generating functional.

Working channels: Q1 clocks; Q2 superposed sources; Q3 backreaction/source rule; Q4 gravity-mediated quantum information; Q5 geometry fluctuations; Q6 causal/process structure; Q7 low-energy QG EFT.

Highest priority remains Q3 with Q2/Q5/Q4 cross-checks.

NP grades:

- NP0 global scalar;
- NP1 selected mean;
- NP2 selected mean + centered symmetrized noise;
- NP3 finite independent multiprobe/multipole mean/noise set;
- NP4 complete relevant smeared stress-energy mean/noise on declared domain;
- NP5 NP4 plus apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest exact positive construction remains finite NP3 Toy009/Toy010 family. NP grade is not experimental significance.

## 3. Retained exact result chain

- Toy001: equal mean can hide different covariance.
- RQIR-NG-001 / Toy002: static density phase blindness.
- RQIR-NG-002 / Toy003: minimal ordered-response split has an energy confound.
- Toy004: `(<H>,<B>,N_B)` does not determine ordered response `D_B`.
- PE-1 / Toy005: exact Newtonian one-channel embedding; NP2 only.
- RQIR-NG-003 / Toy006: generic complete local-density history becomes tomography.
- Toy007: first finite NP3.
- RQIR-NG-004: one additional independent exact row kills a one-dimensional exact nullspace.
- Toy008: soft-nullspace scan motivated likelihood/Fisher rather than maximal exact rank.
- Toy009: detector-aware source optimization; source must be scored only after calibration and detector projection.
- Toy010: calibration geometry is an active design variable and can steer the hidden null direction.
- Iteration-011 balanced geometry remains the practical Toy009 baseline.

Current source radii:

`(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Current balanced geometry:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact rank `24/25`;
- positive states;
- selected equality residual `<1e-15`.

## 4. Statistical identifiability

For parameter of interest `beta` and nuisances `theta`,

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

After whitening:

`F_beta|theta = ||(I-P_J)s_tilde||^2`.

Rank alone is not an experimental identifiability metric.

RQIR-NG-005: if the gravitational calibration leaves hidden direction `n` exact-null and detector signal is locally `mu_D=beta*a*s`, gravitational null calibration cannot self-calibrate `a`; without independent source metrology `F_beta|a=0`.

Independent source metrology is required unless a complementary calibration protocol removes the detector-relevant null.

## 5. Mandatory numerical/coordinate corrections

### RQIR-NUM-001 — exact constraints

Trace+energy must be eliminated analytically by a reduced/nullspace basis. The old `1e12` Fisher penalty + threshold pseudoinverse truncated weak physical nuisance directions and inflated Fisher. Large Iteration-013/014 allocation gains were withdrawn.

### RQIR-NUM-002 — Fisher-coordinate Jacobian

Iteration 020 QFI is for physical amplitude `a` in

`rho(a)=I/5+a Delta0`, `a=0.08`.

Current detector Fisher uses fractional amplitude `alpha` with

`a=0.08 alpha`.

Therefore

`F_Q^(alpha)=0.08^2 F_Q^(a)`.

Current values:

- `F_Q^(a)~=13.27068619`;
- `F_Q^(alpha)~=0.0849323916` per ideal accepted single-branch source-metrology copy.

At normalized detector Fisher `S_D=1`, isolated 90% amplitude retention needs `C_alpha=9`, about `105.97` single-branch copies or `52.98` independent plus/minus pair equivalents.

The old `~17 copies for C_a=225` downstream mapping is withdrawn.

Physical preparation rate:

`R_P^(alpha)=p_P eta_P F_Q^(alpha)/t_P`.

## 6. Centered-noise correction

RQIR physically targets centered symmetrized noise. For a symmetric state pair about `rho0=I/5`, use on the trace-zero tangent

`C_AB = sym(A,B) - <A>0 B - <B>0 A`.

RQIR-CAL-013: raw second-moment rows are equivalent only under exact mean conditioning or if raw moments are explicitly the measured statistic.

Exact Toy009/Toy010 null geometry survives unchanged.

Preferred centered 90%-retention normalized row weights:

- D1 `gamma_mean~1.266e6`, `gamma_cov~0.622e6`;
- D2 `gamma_mean~1.830e6`, `gamma_cov~0.590127e6`.

## 7. Low-rank systematics and timing

RQIR-NG-006 survives the centered correction. Without independent control priors, D1/D2 `F_beta|theta` remains numerical zero even at `100x` calibration exposure.

Current centered first-order benchmark at 100 Hz:

### D1

- `sigma(delta tau)~6.94360e-3`;
- `sigma_t~11.0511 us`;
- `sigma(b_mean)~8.88857e-5`;
- `sigma(b_cov)~1.26818e-4`;
- restored `F_beta|theta~0.899915`.

### D2

- `sigma(delta tau)~5.77425e-3`;
- `sigma_t~9.19001 us`;
- `sigma(b_mean)~7.39168e-5`;
- `sigma(b_cov)~1.30175e-4`;
- restored `F_beta|theta~0.899893`.

RQIR-NG-007: if the stability floor plus immediate reference variance exhausts the target prior, no finite cadence can repair it.

RQIR-REF-001: certify differential source-drive-to-detector-reference delay with TDEV/phase-error/relative-delay stability, not one oscillator ADEV.

Current hard coherence lower bound:

`T_coh,min=4.99085067/(2 pi f_gap)`.

At 100 Hz: `~7.94319 ms`.

## 8. D2 observable branches

Direct force-gradient calibration detects the old hidden direction, but replacement can rotate the null rather than remove it.

RQIR-NG-010: observable replacement can rotate rather than remove a detector-relevant exact null.

RQIR-CAL-009: complementary observables can complete the finite hard source tangent locally; this is not global tomography or experimental feasibility.

RQIR-CAL-011: mean and covariance/noise observables must come from the same physical observable family unless the branch is explicitly labeled hybrid.

A force detector supplies potential only relationally:

`Delta B(y;y_ref)=B(y)-B(y_ref)`.

RQIR-NG-011: an absolute potential needs an independent reference/integration constant.

RQIR-NG-012: nonzero calibration information on one old hidden amplitude is not a surrogate for full profiled beta identifiability.

Current centered branch at `y_ref=-4`:

- 0 added force-cov rows: `F_beta~0.833432`, `C_alpha*=4.55511`;
- best4 `(0,1,3,7)`: `F_beta~0.899477`, `C_alpha*=0.0500614`;
- best5 `(0,1,3,6,7)`: `F_beta~0.903527`, `C_alpha*=0`;
- all8: `F_beta~0.905293`, `C_alpha*=0`.

## 9. Nonstationary/ordered covariance gate

The current Toy009 hidden states are not stationary:

`||[rho_+,H]||_F=||[rho_-,H]||_F~0.240672`.

Current covariance rows are phase-referenced two-time quantities, not stationary scalar PSD coordinates.

RQIR-NG-014: stationary PSD Fisher cannot be assigned without demonstrated stationarity/cyclostationarity.

The high-value covariance rows involve noncommuting source operators.

RQIR-NG-015: detector-output covariance is not automatically the source symmetrized operator correlator; measurement transfer/order/backaction must be explicit.

Preferred phase-referenced Gaussian one-shot Fisher:

`I_ij^shot=(d_i mu)^T Sigma^-1(d_j mu)+1/2 Tr[Sigma^-1 Sigma_,i Sigma^-1 Sigma_,j]`,

`q_ij=p_C eta_C I_ij^shot/t_C`.

RQIR-RESOURCE-012: stationary spectral Fisher is a special case only after its assumptions are demonstrated.

## 10. Covariance positivity and shared-shot bounds — Iterations 037–038

For one full-range affine covariance coordinate in an `m`-dimensional Gaussian output, positivity gives

`I_alpha^shot < m/2`.

RQIR-NG-016: finite-dimensional affine covariance-only Gaussian readout has a positivity-limited per-shot Fisher ceiling.

For `q` independent full-range affine covariance coordinates with whitened derivatives `H_i`, full-hypercube positivity gives

`Tr K < m/2`, `lambda_min(K)<m/(2q)`,

where `K_ij=1/2 Tr(H_i H_j)`.

RQIR-NG-017: multi-parameter covariance information budget.

RQIR-RESOURCE-013: when one trajectory contributes to several covariance directions, use the full matrix Fisher; do not sum independent row times.

RQIR-CAL-014: encode source covariance derivatives Fisher-orthogonally to dominant imprecision/backaction/cross-noise nuisance derivatives. An aligned covariance nuisance can remove one direction exactly after profiling.

For a disjoint `m=8,q=4` near-saturating architecture:

- weakest per-shot covariance Fisher approaches `1`;
- centered `gamma_cov` needs `>5.90127e5` accepted cycles;
- best4 saves only `~53.04` source-copy equivalents;
- equal-efficiency break-even `t_P/t_C>~1.11255e4`;
- at 100 Hz coherence floor this requires `t_P>~88.37 s` before overhead, `~99.50 s` with `1 ms` detector overhead.

RQIR-RESOURCE-014: shared-shot speedup is dimension-limited.

## 11. Actual endpoint-sharing graph — Iteration 039

Best4 rows `(0,1,3,7)` use only six unique phase/probe endpoints:

- row0 `cov[G0(TR),G0(0)]`;
- row1 `cov[G0(T1),G1(0)]`;
- row3 `cov[G1(TR),G0(0)]`;
- row7 `cov[G0(T6),G1(0)]`.

They form two degree-two stars.

For the natural cross-covariance-only Gaussian edge encoding, full-hypercube positivity requires edge amplitude `<1/sqrt(2)`, hence per-row Fisher `<1/2`.

RQIR-NG-018: shared-endpoint covariance bound.

Resource consequence:

- accepted shared trajectories `>1.180254e6`;
- equal-efficiency `t_P/t_C>~2.22510e4`;
- at 100 Hz: source-metrology cycle must exceed `~176.74 s` before overhead, `~198.99 s` with `1 ms` overhead for covariance-only replacement to have a chance.

## 12. Covariance graph congestion — Iteration 040

For the natural uniform cross-covariance edge encoding, endpoint-graph spectral radius controls the per-edge Fisher ceiling:

`K_edge < 1/rho(A_G)^2`.

Current subset costs:

- best4 `(0,1,3,7)`: `rho^2=2`, `N>1.180254e6`;
- best5 `(0,1,3,6,7)`: `rho^2=3.61803399`, `N>2.135100e6`;
- all8: `rho^2=6`, `N>3.540762e6`.

RQIR-RESOURCE-015 — covariance graph congestion:

> Adding a jointly acquired covariance row can increase endpoint-graph spectral radius and reduce the admissible per-shot Fisher of the entire shared edge set. More rows are not automatically cheaper or better at fixed inference target.

Critical 90%-target comparison:

- best4 leaves only `C_alpha=0.0500614`, equivalent to `~0.58943` source-copy equivalents;
- best5 removes that prior but raises the ideal covariance-cycle floor by `~9.54846e5` trajectories;
- best5 beats best4 + residual source metrology only if
  `(p_C eta_C/p_P eta_P)*(t_P/t_C)>~1.61996e6`;
- at 100 Hz equal efficiencies: source-metrology cycle `>~3.57 h` before overhead, `~4.02 h` with `1 ms` overhead.

For the fixed 90% target, all8 is resource-dominated by best5 in the covariance-only cross-covariance graph architecture because both need `C_alpha=0` but all8 has greater graph congestion.

## 13. Current resource conclusion

The high-value covariance core remains geometrically useful, but covariance-only completion is no longer the favored wall-clock route under the natural Gaussian phase-referenced graph model.

Current best working hypothesis for experiment design:

`best4 centered covariance + small independent source metrology`

is likely cheaper than best5/all8 unless source verification is intrinsically very slow.

The complementary D2 branch can still become competitive if the **same coherent trajectory** also earns substantial force-mean and control Fisher or if a different measurement class changes the present covariance-only bounds.

## 14. Publication architecture

Fixed in `docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`:

1. RQIR I — operational hierarchy, ordered source information, finite discriminants;
2. RQIR II — statistical identifiability, nuisance geometry, source calibration;
3. RQIR III — physical resources and experiment architecture;
4. later Candidate Gravity paper only after a concrete model passes RQIR I–III gates.

## 15. Mandatory open consistency gates

G1 gauge/relational observables; G2 source+apparatus conservation/Bianchi; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a semiclassical/stochastic/classical-gravity+full-QFT/quantum degeneracy audit; G13 detector covariance/nuisance/measurability.

## 16. Current priority order — v2.2

P1. Build a **joint mean + covariance phase-referenced D2 trajectory likelihood** on the actual shared endpoints. The same accepted cycle must be credited simultaneously for direct force means and selected centered covariances.

P2. Include centered timing/additive controls and explicit imprecision/backaction/cross-noise derivatives in that same Fisher. Enforce RQIR-CAL-014 nuisance orthogonality where physically possible.

P3. Compare `best4 + minimal C_alpha` against best5 and the fully force-native branch using one shared-cycle wall-clock model, not row-time sums.

P4. Derive the physical mean transduction / per-cycle force SNR required for joint trajectories to overcome the covariance-only graph bounds.

P5. Revalidate second-order timing/gain bias only if it becomes competitive with the joint-readout gate.

P6. Build a common D1/D2 resource budget at one source mass, gap, coherence, separation and campaign duration.

P7. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.

P8. After detector/inference geometry stabilizes, embed a more physical oscillator/atomic/full stress-energy source and close conservation, gauge and renormalization gates.

## 17. Continuation protocol

At every substantive iteration:

1. read `RECOVERY_GUIDE.md`, `MASTER_TABLE.md`, latest research log, Toy009/Toy010 and Statistical Identifiability docs;
2. repository state is source of truth;
3. do not duplicate closed/active calculations without reason;
4. derive before adding numerical complexity;
5. use exact hard constraints;
6. transform Fisher/QFI/rates into common physical coordinates;
7. use centered noise, not raw moments, unless raw moments are explicitly the measured statistic;
8. do not map nonstationary two-time covariance directly to stationary PSD;
9. cost shared detector records with full matrix Fisher, not row-time sums;
10. include detector nuisance directions before claiming identifiability;
11. preserve negative results and corrections;
12. save reproducible code, main document, research log and recovery delta;
13. never promote toy/resource benchmarks to empirical new physics.
