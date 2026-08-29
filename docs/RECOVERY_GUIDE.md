# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v2.0

This file is the continuity backbone. The repository, not chat history, is authoritative project memory. Do not mix RQIR with RTK or DSIR. No toy/resource result is an empirical new-physics claim.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem:

`P_data(o|s) -> [interface class]`.

Rules:

- observable first;
- explicit baseline/domain;
- preserve operator ordering;
- retain negative/correction results;
- source response is not detector observability;
- exact nulls are not statistical identifiability;
- every numerical result gets reproducibility code;
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
- Toy007: first finite NP3; `eta_R~0.457682`, `s_min~1.463e-3`, condition `~3.18e3`.
- RQIR-NG-004: one additional independent exact row kills a one-dimensional exact nullspace.
- Toy008: soft-nullspace scan motivated likelihood/Fisher rather than maximal exact rank.
- RQIR-CAL-001: independent beta-blind calibration cannot reduce profiled Fisher under the stated regularity assumptions.

## 4. Statistical identifiability coordinate

For parameter of interest `beta` and nuisances `theta`,

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

After whitening,

`F_beta|theta = ||(I-P_J)s_tilde||^2`.

Rank alone is not an experimental identifiability metric. Exact null-pair geometry and noisy statistical identifiability are different objects.

Protocol 002 uses two response bands. For whitened powers `P2,P4` and a relative spectral-tilt nuisance,

`S_eff=4 P2 P4/(P2+P4)`.

Losing one band kills the shape discriminator.

D1 matter-wave phase needs deliberate lock-in/echo sensitivity because passive full-period integration cancels selected AC bands. D2 is naturally a force-domain/live-time problem; at a true force-noise floor mechanical susceptibility gives no free force-domain Fisher gain.

## 5. Toy009/Toy010 and current practical geometry

Toy009 source radii:

`(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Toy009 established RQIR-DESIGN-001:

`source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> profiled likelihood`.

Detector-only high-gain candidates can be projected away by calibration/nuisance geometry.

Toy010 established that calibration geometry itself is an active design variable. Changing probe position/times can rotate the exact null strongly for a fixed source.

Current practical balanced geometry (Iteration 011):

- `y1=-3.7766873837`;
- times `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact rank `24/25`;
- positive states;
- selected equality residual `<1e-15`;
- raw-row normalized `s_min~1.999540e-3`;
- condition `~2313`.

RQIR-CAL-002: finite calibration geometry steers the hidden direction and must be co-designed with detector observability.

## 6. RQIR-NG-005 and source-preparation metrology

If hidden source direction `n` obeys `A n=0` and detector signal is locally `mu_D=beta*a*s`, gravitational null calibration contains no information on the hidden amplitude. Without independent source preparation metrology, beta and amplitude are locally non-identifiable.

RQIR-NG-005:

`F_beta|a=0`

for the exact null-amplitude problem independently of arbitrarily strong orthogonal gravitational calibration.

Independent preparation metrology is logically required unless a complementary calibration protocol removes the detector-relevant null.

## 7. Mandatory hard-constraint numerical correction — RQIR-NUM-001

Iterations 013–014 originally approximated exact trace+energy constraints with a `1e12` Fisher penalty followed by thresholded pseudoinverse. This truncated genuine weak nuisance directions and inflated `F_beta`.

RQIR-NUM-001:

> Exact constraints must be eliminated analytically through a nullspace/reduced basis, not emulated by enormous penalties before pseudoinversion.

The large old heterogeneous-allocation gains were withdrawn. All later current calculations use exact trace+energy elimination.

## 8. Source-QFI physical-coordinate correction — Iteration 034

Iteration 020 correctly computed the QFI of

`rho(a)=I/5+a Delta0`

at physical single-branch amplitude `a=EPS=0.08`:

`F_Q^(a)~=13.27068619`

per ideal accepted copy.

However, Iterations 026+ use the fractional amplitude nuisance `alpha` with

`a=EPS alpha`.

Fisher must transform with the parameter Jacobian:

`F_Q^(alpha)=EPS^2 F_Q^(a)~=0.0849323916`.

### RQIR-NUM-002 — Fisher-coordinate Jacobian rule

Do not compare Fisher requirements, QFI or rates written in different parameter coordinates.

Current source-preparation rate coordinate:

`R_P^(alpha)=p_P eta_P EPS^2 F_Q^(a)/t_P`

per accepted single-branch metrology cycle.

At normalized detector Fisher `S_D=1`, 90% isolated-amplitude retention requires `C_alpha=9` and about `105.97` ideal accepted single-branch copies, or `52.98` independent plus/minus pair equivalents.

At historical `S_D=25`, `C_alpha=225` requires about `2649.17` single-branch copies or `1324.58` pair equivalents.

The old Iteration-020 `~17 copies for C_a=225` mapping is withdrawn for the fractional-amplitude Fisher used downstream. The QFI formula itself is retained.

## 9. Centered covariance/noise correction — Iteration 034

RQIR physically defines centered symmetrized noise. For a symmetric state pair around `rho0=I/5`, the correct covariance-difference derivative row on the trace-zero tangent is

`C_AB = sym(A,B) - <A>0 B - <B>0 A`.

### RQIR-CAL-013 — centered-noise linearization rule

Raw second-moment rows are equivalent only under exact mean conditioning or when raw second moments are explicitly the measured statistic.

The exact Toy009/Toy010 nullspace is unchanged because centered-row corrections lie in the already-declared mean-row span:

- raw rank `24/25`;
- centered rank `24/25`;
- exact-null overlap `1.0` numerically.

Preferred centered 90%-retention normalized row weights, with exact trace+energy elimination:

- D1 `gamma_mean~1.26572e6`, `gamma_cov~0.621783e6`, allocation gain `~1.09308`;
- D2 `gamma_mean~1.83026e6`, `gamma_cov~0.590127e6`, allocation gain `~1.18719`.

Old Iteration-015 numbers remain historical raw-second-moment protocol values.

## 10. Low-rank systematics after centered correction — Iteration 036

RQIR-NG-006 survives the correction. Uncontrolled second-probe drift, common timing drift and common additive offsets keep `F_beta|theta` at numerical zero for D1/D2 even when gravitational calibration exposure reaches `100x`.

Current centered first-order control bundle:

### D1

- `sigma(delta tau)~6.94360e-3`;
- `sigma_t~11.0511 us` at 100 Hz;
- `sigma(b_mean)~8.88857e-5`;
- `sigma(b_cov)~1.26818e-4`;
- restored `F_beta|theta~0.899915`.

### D2

- `sigma(delta tau)~5.77425e-3`;
- `sigma_t~9.19001 us`;
- `sigma(b_mean)~7.39168e-5`;
- `sigma(b_cov)~1.30175e-4`;
- restored `F_beta|theta~0.899893`.

Old `9.47 us` / `8.01 us` timing numbers are raw-second-moment historical values.

RQIR-CAL-007 remains: calibration exposure and independent control-prior information are non-interchangeable resources.

RQIR-DRIFT-001 remains: pure common multiplicative gain is first-order suppressed at the exact null; leading gain contamination is product-like.

The Iteration-017 second-order timing/gain numbers should be revalidated if they become competitive with the current covariance-rate gate.

## 11. Current timing/reference benchmark

Per-shot coherence and campaign integration time are distinct.

RQIR-RESOURCE-001/002: coherent evolution is a hard lower bound on physical shot duration.

Current largest stored dimensionless phase `4.99085067` gives

`T_coh,min=4.99085067/(2 pi f_gap)`.

At 100 Hz this is about `7.943 ms`.

Transparent centered timing benchmark with `sigma_event=10 us`, `sigma_ref=target/3`, acceptance `0.5`, `1 ms` dead time:

- reference blocks: D1 `~0.131812 s`, D2 `~0.190604 s`;
- random-walk `D=100 us^2/h`: D1 `~2.17114 h`, D2 `~1.50145 h`;
- `D=1000 us^2/h`: D1 `~13.03 min`, D2 `~9.01 min`;
- equal-diffusion cadence ratio D2/D1 `~0.69155`.

RQIR-NG-007 remains: if the stability floor plus immediate reference variance exhausts the target prior, no finite cadence or faster white averaging can satisfy the requirement.

RQIR-REF-001 remains: timing prior applies to differential source-drive-to-detector-reference delay, so certify the full relative path with TDEV/phase-error/relative-delay stability rather than one oscillator ADEV.

## 12. Detector-native rate layer

D1 phase/interference Fisher rate scales as

`p_acc C^2 M^2 T^2/(T+t_dead)`

with branch/control-window factors. Acquisition throughput is separate from mass and coherence.

D2 detector rate is naturally

`R_D2=eta_duty*4 r2 r4/(r2+r4)`,

`r_n=|Delta F_n|^2/S_F,n`.

RQIR-RESOURCE-004: D1 and D2 cannot be globally ranked without native Fisher rates and explicit noise assumptions.

RQIR-RESOURCE-005/006: dimensionless calibration weights and nuisance normalization cannot create wall-clock time; use physical event precision, transduction, acceptance/cycle, PSD/bandwidth and physical priors.

## 13. D2 observable branches and null rotation

Direct force-gradient calibration detects the old hidden direction, but replacing potential means by force means does not guarantee source identifiability.

RQIR-NG-010: observable replacement can rotate rather than remove an exact detector-relevant null.

A complementary potential+force protocol can close the finite hard source tangent locally.

RQIR-CAL-009: complementary observables can complete the finite-dimensional calibration tangent. This is not global tomography or experimental feasibility.

Iteration 032 corrected a protocol-label issue: the old Iteration-026 `native-replace` branch used force means but retained potential covariance and is therefore hybrid, not fully force-native.

RQIR-CAL-011: mean and covariance/noise observables must come from the same declared physical observable family unless the protocol is explicitly labeled hybrid.

## 14. Finite-reference relational potential

A local force readout cannot directly provide an absolute Newtonian potential. A force-integral implementation measures

`Delta B(y;y_ref)=B(y)-B(y_ref)`.

RQIR-CAL-010: the reference geometry is part of the calibration model.

With shared white force PSD,

`q_pot=2||Delta B||^2/(L^2 S_F)`,

`q_force=2||G(y)||^2/S_F`

in the declared ideal force-integral convention.

Moving the reference outward makes the relational null approach the old absolute-potential null but suppresses the force-integral rate approximately as `1/L^2` after signal saturation.

RQIR-RESOURCE-010: reference distance is a joint geometry/resource tradeoff.

RQIR-NG-011: force determines potential only up to a reference/integration constant unless an independent potential reference is declared.

Iteration 031 showed that a finite reference can give nonzero calibration Fisher on the **old** hidden amplitude while leaving another detector-aligned exact null.

RQIR-NG-012: `I_cal(old amplitude)>0` is not a surrogate for full profiled beta identifiability.

## 15. Centered D2 branch front after Iteration 034

Fully force-native centered branch (`14 force means + 8 centered force covariance`):

- hard rank `22/23`;
- old-hidden overlap `~0.95003346`;
- detector alignment `~0.99003961`;
- `F_beta(C_alpha=0,lambda=1)~0.0195153`;
- `C_alpha90~7.78026`;
- strong-preparation `lambda90~0.10013`.

Complementary centered relational+force branch at `y_ref=-4`, with both centered covariance families:

- hard rank `23/23`;
- `F_beta(C_alpha=0,lambda=1)~0.905293`;
- `C_alpha90=0`;
- calibration-only `lambda90~0.94149`.

Centered force-covariance row selection at `y_ref=-4`:

- 0 added rows: `F_beta~0.833432`, `C_alpha*=4.55511`;
- best 4 `(0,1,3,7)`: `F_beta~0.899477`, `C_alpha*=0.0500614`;
- best 5 `(0,1,3,6,7)`: `F_beta~0.903527`, `C_alpha*=0`.

RQIR-CAL-012 remains: covariance-row orientation can dominate nuisance closure and must be optimized rather than treated as a fixed secondary bundle.

Local equal-row preparation-substitution thresholds:

- first four: `q_cov/R_P^(alpha)>~5.24e5`;
- fifth after first four: `>~1.18e7`.

## 16. Nonstationary covariance measurement gate — Iteration 035

The current Toy009 hidden states are not stationary:

`||[rho_+,H]||_F=||[rho_-,H]||_F~0.240672`.

For probe-0 force centered covariance,

`Delta N(TR,0)~-8.45063e-4`,

while after shifting both times by one dimensionless unit,

`Delta N(TR+1,1)~-4.79183e-3`.

Thus current covariance rows are phase-referenced two-time quantities, not stationary scalar PSD coordinates.

RQIR-NG-014: stationary PSD Fisher cannot be assigned without demonstrated stationarity/cyclostationarity.

The high-value force covariance rows `(0,1,3,7)` also involve noncommuting source operators.

RQIR-NG-015: detector-output covariance is not automatically the source symmetrized operator correlator for noncommuting observables; measurement transfer/order/backaction must be explicit.

Preferred apparatus-neutral phase-referenced Gaussian rate:

`I_ij^(shot)=(d_i mu)^T Sigma^-1(d_j mu)+1/2 Tr[Sigma^-1 Sigma_,i Sigma^-1 Sigma_,j]`,

`q_ij=p_C eta_C I_ij^(shot)/t_C`.

RQIR-RESOURCE-012: use the Fisher rate of the actual phase-referenced/cyclostationary detector-output likelihood. Stationary spectral Fisher is only a special case.

Coordinate-correct break-even:

- first four covariance rows require
  `I_cov^(shot)*(pC etaC/pP etaP)*(tP/tC)>~4.4502e4`;
- fifth requires `>~1.0012e6`.

## 17. Physical offset map

Row normalization can be undone exactly. If normalized additive nuisance is `b`, raw offset is `||a_i||b`. SI conversion still requires physical readout Jacobian `g_i`:

`sigma(o_i)<=|g_i| ||a_i|| sigma(b)`.

Current centered raw Toy-unit offset ranges:

D1:

- mean `3.396e-5..1.219e-4`;
- centered covariance `7.750e-6..8.109e-5`.

D2:

- mean `2.824e-5..1.014e-4`;
- centered covariance `7.955e-6..8.323e-5`.

RQIR-CAL-008 and RQIR-NG-008 remain.

## 18. Publication architecture

Future drafting architecture is fixed in

`docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`.

Planned logical sequence:

1. RQIR I — operational hierarchy, ordered source information, finite discriminants;
2. RQIR II — statistical identifiability, nuisance geometry, source calibration;
3. RQIR III — physical resource budgets and experiment architecture;
4. later Candidate Gravity paper only after a concrete model exists and is passed through RQIR I–III gates.

Do not merge the candidate-theory epistemic level into the reconstruction papers prematurely.

## 19. Mandatory open consistency gates

G1 gauge/relational observables;
G2 source+apparatus conservation/Bianchi;
G3/G3b positivity/unitarity/spectral response;
G4a causal retarded support;
G8 controlled Newtonian limit;
G9 EFT power counting;
G10/G10a stress-energy smearing/renormalization;
G12/G12a semiclassical/stochastic/classical-gravity+full-QFT/quantum degeneracy audit;
G13 detector covariance/nuisance/measurability.

Passing these gates is necessary, not sufficient.

## 20. Current priority order — v2.0

P1. Build a phase-referenced repeated-shot or cyclostationary D2 detector-output likelihood for the high-value centered covariance rows `(0,1,3,7)`.

P2. Derive row-specific `Sigma_,i` / covariance transduction from one declared detector model including imprecision, backaction and cross-noise; obtain physical `q_i`.

P3. Test the `~4.45e4` first-four resource product against coordinate-correct `R_P^(alpha)` and centered timing/additive priors.

P4. Optimize full D2 wall-clock cost over `(y_ref,lambda,C_alpha,covariance subset)` on the corrected centered likelihood.

P5. Revalidate second-order timing/gain bias only if it becomes competitive with the covariance-rate gate.

P6. Build a common D1/D2 resource budget at one source mass, gap, coherence, separation and campaign duration.

P7. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.

P8. After detector/inference geometry stabilizes, embed a more physical oscillator/atomic/full stress-energy source and close conservation, gauge and renormalization gates.

## 21. Continuation protocol

At every substantive iteration:

1. read `RECOVERY_GUIDE.md`, `MASTER_TABLE.md`, latest research log, Toy009/Toy010 and statistical-identifiability documents;
2. treat repository state as source of truth;
3. do not duplicate closed/active calculations without a stated reason;
4. derive before adding numerical complexity;
5. use exact hard constraints;
6. transform Fisher/QFI/rates into common physical coordinates;
7. distinguish raw second moments from centered noise;
8. distinguish stationary PSD from phase-referenced/cyclostationary covariance;
9. preserve negative results and corrections;
10. save reproducible code, main document, research log and recovery delta;
11. never promote toy-model/resource benchmarks to empirical new physics.
