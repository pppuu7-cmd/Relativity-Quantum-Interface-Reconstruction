# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v1.8

This file is the continuity backbone. The repository, not chat history, is authoritative project memory.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance that gravity is classical, stochastic, quantized, hybrid, emergent, or described by a preferred UV theory.

Central inverse problem: `P_data(o|s) -> [interface class]`.

Rules: observable first; explicit baseline/domain; preserve operator ordering; retain negative/correction results; source response is not detector observability; exact nulls are not statistical identifiability; every numerical result gets reproducibility code; no new-physics claim before classical/stochastic/full-QFT/hybrid alternatives and relativistic consistency gates are closed.

Do not mix RQIR with RTK or DSIR.

## 2. Ordered source hierarchy and null grades

At second order `K_T^(2)=(<T>,N,D or chi^R)`, with symmetrized noise `N`, ordered/commutator response `D`, and retarded susceptibility `chi^R`. Parent source object: Schwinger-Keldysh/CTP generating functional.

Working channels: Q1 clocks; Q2 superposed sources; Q3 backreaction/source rule; Q4 gravity-mediated quantum information; Q5 geometry fluctuations; Q6 causal/process structure; Q7 low-energy QG EFT. Highest priority remains Q3 with Q2/Q5/Q4 cross-checks.

NP0 global scalar; NP1 selected mean; NP2 selected mean+symmetrized noise; NP3 finite independent multiprobe/multipole mean/noise set; NP4 complete relevant smeared stress-energy mean/noise on declared domain; NP5 NP4 plus apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Current strongest exact positive construction remains finite NP3 Toy009/Toy010 family. NP grade is not experimental significance.

## 3. Retained exact/statistical result chain

- Toy001: equal mean can hide different covariance.
- RQIR-NG-001 / Toy002: static density phase blindness.
- RQIR-NG-002 / Toy003: minimal ordered-response split has an energy confound.
- Toy004: `(<H>,<B>,N_B)` does not determine ordered response `D_B`.
- PE-1 / Toy005: exact Newtonian one-channel embedding; remains NP2.
- RQIR-NG-003 / Toy006: complete generic local-density history becomes tomography.
- Toy007: first finite NP3, `eta_R~0.457682`, `s_min~1.463e-3`, condition `~3.18e3`.
- RQIR-NG-004: one additional independent exact row kills a one-dimensional exact nullspace.
- Toy008: soft-nullspace scan motivated likelihood/Fisher rather than maximal exact rank.
- RQIR-CAL-001: independent beta-blind calibration cannot reduce profiled Fisher under stated regularity assumptions.
- RQIR-NG-005: if the gravitational calibration leaves a hidden source direction `n` exact-null and detector signal is locally `beta*a*s`, gravitational null calibration cannot self-calibrate amplitude `a`; without independent source metrology `F_beta|a=0`.
- RQIR-NG-006: uncontrolled low-rank timing/geometry/additive systematics can remain structurally detector-degenerate; more gravitational exposure alone does not cure them.
- RQIR-NG-007: if Allan/flicker floor plus immediate reference variance exhausts the required nuisance prior, no finite recertification cadence can satisfy it.
- RQIR-NG-008: a row-normalized additive prior cannot be assigned a unique SI tolerance without the physical readout/transduction Jacobian.
- RQIR-NG-010: replacing a calibration observable can rotate, rather than remove, an exact detector-relevant null.
- RQIR-NG-011: a force readout determines a potential only relationally unless an independent reference fixes the integration constant.
- RQIR-NG-012: nonzero calibration information on one previously hidden amplitude does not imply nonzero profiled beta Fisher if another detector-aligned null remains.

## 4. Statistical identifiability coordinate

For parameter of interest beta and nuisances theta,

`F_beta|theta=F_bb-F_btheta F_thetatheta^-1 F_thetab`.

After whitening: `F_beta|theta=||(I-P_J)s_tilde||^2`.

Rank alone is not an experimental identifiability metric. Exact null-pair geometry and noisy statistical identifiability are separate objects.

Protocol 002 uses two response bands. For whitened powers `P2,P4` and a relative spectral-tilt nuisance,

`S_eff=4 P2 P4/(P2+P4)`.

Losing one band kills the shape discriminator.

D1 matter-wave phase: passive full-period integration cancels selected AC bands; deliberate lock-in/echo sensitivity is required. D2 force: at a true force-noise floor, mechanical susceptibility does not provide free force-domain Fisher gain.

## 5. Toy009/Toy010 and practical calibration baseline

Toy009 source radii: `(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Toy009 established RQIR-DESIGN-001: optimize the whole chain `source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> profiled likelihood`; detector-only high-gain candidates can be projected away by NP3 calibration.

Toy010 showed calibration geometry is itself an active design variable. The exact-null direction can rotate strongly when probe position/times change even for a fixed source.

The later Iteration-011 balanced calibration remains the current practical geometry baseline:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- rank `24/25`;
- positive states and selected equality residual `<1e-15`;
- `eta_R~0.5734264`;
- `s_min~1.999540e-3`;
- condition `~2313.05`.

RQIR-CAL-002: finite calibration geometry steers the hidden direction and must be co-designed with detector observability.

## 6. Mandatory numerical correction — Iteration 015

The old trace+energy implementation used an artificial `1e12` Fisher penalty followed by a thresholded pseudoinverse. That procedure truncated real weak nuisance directions and inflated `F_beta`.

RQIR-NUM-001: exact constraints must be eliminated analytically through a nullspace/reduced basis, not emulated by enormous penalties before pseudoinversion.

Corrected 22D hard-constrained 90%-retention row weights:

- D1 `gamma_mean~1.722e6`, `gamma_cov~0.938e6`;
- D2 `gamma_mean~2.414e6`, `gamma_cov~0.929e6`.

Old large heterogeneous-allocation gains from Iterations 013–014 are withdrawn. Corrected gains are only about `x1.07` D1 and `x1.14` D2.

## 7. Low-rank controls and nonlinear audit

Iteration 016 includes second-probe drift `delta y`, common timing/phase drift `delta tau`, common mean offset and common covariance offset.

With no independent priors, profiled `F_beta` collapses to numerical zero for both D1 and D2 even when gravitational calibration exposure increases by up to `100x`.

A control bundle restoring about 90% information requires approximately:

- D1 `sigma(delta tau)=5.95e-3` -> `sigma_t~9.47 us` at 100 Hz; `sigma(b_mean)=7.62e-5`; `sigma(b_cov)=1.03e-4`.
- D2 `sigma(delta tau)=5.03e-3` -> `sigma_t~8.01 us`; `sigma(b_mean)=6.44e-5`; `sigma(b_cov)=1.04e-4`.

RQIR-CAL-007: calibration exposure and independent control-prior information are distinct resources.

RQIR-DRIFT-001: pure common multiplicative gain is first-order suppressed at exact null because `A theta0=0`; leading gain contamination is nonlinear/product-like.

At current timing priors, quadratic timing bias is tiny: `~3.49e-5 sigma_beta` D1 and `~8.75e-6 sigma_beta` D2.

RQIR-NL-001: once first-order timing control is satisfied, timing curvature is not the current bottleneck.

RQIR-NL-002: leading gain contamination scales with `delta_g*delta_theta`; no global gain-only tolerance exists.

## 8. Physical resource layer — Iterations 018–023

RQIR-RESOURCE-001: per-shot coherence and total integration time are distinct. Current largest dimensionless phase `4.99085067` requires `T_coh>=0.7943/f_gap`.

RQIR-RESOURCE-002: coherent evolution is a hard lower bound on physical shot duration.

D1 native phase/interference Fisher rate scales as `p_acc C^2 M^2 T^2/(T+t_dead)` with control-window factors. Acquisition throughput is separate from source mass/coherence.

D2 is naturally a force-PSD/live-time problem with `R_D2=eta_duty*4 r2 r4/(r2+r4)`, `r_n=|Delta F_n|^2/S_F,n`.

RQIR-RESOURCE-004: D1 and D2 cannot be globally ranked without native Fisher rates and explicit noise assumptions.

For `rho(a)=I/5+a Delta0` with `[rho,Delta0]=0`, source-amplitude QFI is `F_Q~13.2707` at `a=0.08`. At detector SNR 5, the ideal 90%-retention requirement `C_a=225` is only about 17 accepted copies at the QFI bound.

RQIR-PREP-001: RQIR-NG-005 is an obstruction of the gravitational null channel, not absence of source-state information in principle.

Physical preparation rate: `R_P=p_P eta_P F_Q/t_P`.

RQIR-RESOURCE-005: do not convert dimensionless calibration Fisher weights to hours without measurement-level Fisher rates.

Native calibration/reference rates:

- D1 mean row: `R_M,i=p_acc C_i^2 k_i^2/t_cycle`.
- Gaussian covariance/log-PSD row: `R_C~duty*B*k_C^2`.
- D2 mean row: one-sided force-template Fisher `I_i=4 int |dh_i/du_i|^2/S_F df`.
- timing reference: `T_tau=t_cycle/p_acc*(sigma_event/sigma_target)^2` after consistent unit conversion.

RQIR-RESOURCE-006: nuisance-coordinate normalization cannot create physical wall-time cost.

RQIR-DRIFT-002: white per-event timing Fisher does not certify long-run stability.

For immediate reference variance `sigma_ref^2`, random-walk diffusion `D`, and irreducible Allan/flicker floor `sigma_floor`, interval-averaged residual is

`<sigma^2>=sigma_floor^2+sigma_ref^2+D Delta/2`,

so

`Delta_max=2(sigma_target^2-sigma_floor^2-sigma_ref^2)/D`

when the numerator is positive.

RQIR-DRIFT-003: long campaigns must be budgeted by low-frequency stability `(D,sigma_floor)` or measured Allan/TDEV/PSD curves plus recertification duty, not per-event precision alone.

## 9. Differential references and physical offsets — Iteration 024

The timing nuisance is differential source-drive-to-detector-reference delay, not the ADEV of one oscillator. The acceptance object is the measured relative TDEV/phase-error of the complete synchronized chain.

RQIR-REF-001: certify the differential timing path actually entering the likelihood.

Row normalization can be undone exactly. If the raw calibration row is `a_i` and the normalized additive nuisance is `b`, then `delta x_i,raw=||a_i|| b`. For physical readout `y_i=g_i x_i,raw+o_i`, the physical offset requirement is

`sigma(o_i)<=|g_i| ||a_i|| sigma(b_group)`.

RQIR-CAL-008: normalized prior -> raw row norm -> physical transduction is the safe SI conversion chain.

## 10. D2 calibration branch split — Iterations 025–029

Direct force-gradient calibration detects the old Toy009 hidden direction, but replacing potential means by force means does not guarantee identifiability. On the hard 23D source tangent space, the Iteration-026 replacement branch still has rank `22/23`; the null rotates and remains detector-relevant.

RQIR-NG-010: observable replacement can rotate the null rather than remove it.

An augmented potential+force mean protocol in the old mathematical model reaches rank `23/23` and can eliminate the local exact source null.

RQIR-CAL-009: complementary observables can complete the finite hard-constrained source tangent space. This is local finite-dimensional tomography only, not a global or experimental claim.

Iteration 027 introduced the 90%-retention Pareto frontier `C_a^*(lambda)`: calibration exposure and source metrology are exchangeable only along a branch-specific frontier.

RQIR-RESOURCE-007: the full Pareto boundary, not a fixed `gamma` or `C_a`, is the correct resource object.

Iteration 028 showed there is no universal cheapest D2 branch in abstract rate-ratio space.

RQIR-RESOURCE-008: branch choice is a resource phase diagram.

Iteration 029 closed the abstract phase coordinates onto physical Fisher rates. For corrected D2 weights,

`x=K_force/K_pot=q_pot/q_force` for equal-row bundle structure,

`y=0.219907681382*(q_pot/q_cov)`,

`z=3.3796e7*(R_P/q_pot)`

under the declared simplifications.

RQIR-RESOURCE-009: branch-selection coordinates must be derived from native information rates, not hidden equal-rate assumptions.

## 11. Finite-reference relational potential — Iterations 030–031

A force readout cannot directly realize an absolute Newtonian potential row. A force-integral implementation measures

`Delta B(y;y_ref)=B(y)-B(y_ref)`.

RQIR-CAL-010: finite reference geometry is part of the physical calibration model.

For a shared white force PSD,

`q_pot=2||Delta B||^2/(L^2 S_F)`,

`q_force=2||G(y)||^2/S_F`.

Moving `y_ref` outward makes the relational null approach the old absolute-potential null, but suppresses `q_pot` approximately as `1/L^2` after signal saturation.

RQIR-RESOURCE-010: reference distance is a joint geometry/resource tradeoff; there is no free far-reference limit.

Iteration 031 propagated finite reference through the corrected profiled Fisher while keeping the physical Toy009 hidden state fixed. A finite reference gives nonzero Fisher on the *old* hidden amplitude but does not restore beta identifiability at `C_a=0`; a nearby detector-aligned exact null remains.

Representative values:

- `y_ref=-5`: `I_amp~3.18167`, `F_beta~8.17e-5`, new-null detector alignment `~0.999957`.
- `y_ref=-10`: `I_amp~0.6719`, `F_beta~1.23e-5`, alignment `~0.999994`.
- `y_ref=-100`: `F_beta~1.25e-8`, alignment `~0.999999993`.

At `lambda=1`, 90%-retention preparation requirements grow with distance: `C_a*=15.48` at `y_ref=-4`, `16.65` at `-5`, `21.92` at `-10`, `31.59` at `-20`, `59.67` at `-50`, `106.20` at `-100`.

RQIR-NG-012: `I_cal(old amplitude)>0` is not a surrogate for full profiled identifiability.

## 12. D2 observable-family covariance correction — Iteration 032

Important protocol-label correction: the Iteration-026 `native-replace` branch replaced the 14 mean rows by force-gradient means but retained the old potential covariance/noise rows. It is therefore a **hybrid force-mean/potential-covariance protocol**, not a fully force-native D2 calibration.

A fully force-native branch was rebuilt using `14 force means + 8 force covariances` from the same gradient operator family. On the corrected hard source tangent space:

- rank remains `22/23`;
- old-hidden overlap of the new exact null `~0.95003346`;
- detector alignment `~0.99003961`;
- `F_beta|theta(C_a=0,lambda=1)~0.0194450`;
- 90% at `lambda=1` requires `C_a*~8.29464`;
- with strong preparation metrology, 90% requires only `lambda~0.1537665`.

RQIR-CAL-011 — mean/covariance observable-family consistency: when the detector-native mean observable changes, covariance/noise calibration must be derived from the same declared physical observable family, or the branch must be explicitly labeled hybrid.

A fully complementary finite-reference branch was also built:

`14 relational-potential means + 14 force means + 8 relational covariances + 8 force covariances`.

It has rank `23/23`. At `y_ref=-4`, current corrected weights give

- `F_beta|theta~0.8994327` with `C_a=0`, `lambda=1`;
- only `C_a*~0.06708` is needed to reach 90% at `lambda=1`;
- calibration alone reaches 90% at `lambda~1.00632`.

However, this protocol uses sixteen covariance rows and has not yet been assigned physical covariance Fisher rates. It is not yet known to be cheaper in wall-clock time.

Subset audit at `y_ref=-4`: the best four added force-covariance rows are indices `(0,1,3,7)`. With relational+force means and the eight relational covariance rows, adding these four raises `F_beta` from `~0.819539` to `~0.894857` and reduces `C_a*` from `~5.82122` to `~0.58896`. Calibration-only 90% then occurs at `lambda~1.05755`.

RQIR-CAL-012 — covariance complementarity can dominate nuisance closure: a targeted covariance subset can remove most of the remaining detector-relevant nuisance penalty; covariance-row selection is an active design variable.

Consequently, Iterations 026–029 are retained numerically for their declared mixed protocol, but their `native-replace` region is **not** the final fully physical D2 phase diagram.

## 13. Current D2 protocol labels

Keep the following branches distinct:

1. **NP3-null + source metrology:** original null-preserving potential/noise model; RQIR-NG-005 applies.
2. **Hybrid force-mean/potential-covariance:** the Iteration-026/028 replacement branch; mathematically valid but not fully detector-native.
3. **Fully force-native:** force means + force covariance; still contains a detector-relevant exact null and needs source metrology.
4. **Finite-reference relational potential:** physically explicit potential-difference implementation; exact null persists and source-metrology burden grows as the reference moves outward.
5. **Complementary relational-potential + force:** full-rank locally when both observable families are combined; covariance subset/rates now determine whether it is resource-efficient.

Do not collapse these branches into one generic `gamma` model.

## 14. Mandatory open consistency gates

G1 gauge/relational observables; G2 source+apparatus conservation/Bianchi; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy audit; G13 detector covariance/nuisance/measurability.

The current Toy009/Toy010 resource results do not pass these gates globally and do not constitute evidence for new physics.

## 15. Current priority order

P1: derive physically consistent Fisher rates for **force covariance** and **relational-potential covariance** from one common D2 force-PSD/bandwidth/duty model.

P2: optimize the D2 wall-clock objective over `(y_ref,lambda,C_a,covariance-row subset)` and compare the fully force-native branch against the complementary relational+force branch on equal resource footing.

P3: insert differential timing/TDEV and additive-reference recertification duty into the same full `F_beta|theta/T_wall` objective.

P4: construct a common D1/D2 resource budget at one source mass, gap, coherence, separation and campaign duration.

P5: propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through the same likelihood.

P6: after detector/inference geometry stabilizes, embed a more physical oscillator/atomic/full stress-energy source and close conservation/gauge/renormalization gates.

## 16. Continuation protocol

At each substantive iteration: inspect repository state and latest log; avoid duplication; state one unresolved target; derive before numerical complexity; preserve negative/correction results; save reproducibility code; update this guide and `MASTER_TABLE.md` or an explicit recovery delta; never promote toy-model or detector benchmarks to empirical new physics.
