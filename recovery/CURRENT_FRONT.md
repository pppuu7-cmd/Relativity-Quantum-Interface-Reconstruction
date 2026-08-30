# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 102**.

> The repository, not chat history, is authoritative. `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework; for the fast Paper-III front read this pointer plus `recovery/RECOVERY_DELTA_ITERATION_096.md` through `RECOVERY_DELTA_ITERATION_102.md`. Do not mix RQIR with RTK/DSIR.

## Publication-track status

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–102 translate abstract preparation/calibration Fisher requirements into physical detector, calibration, source, control and characterization rates, audit what one real platform can supply, specify same-state temporal `f,2f` calibration, and now place transfer calibration inside the joint science Fisher with an exact wall-clock optimum.

No toy, Fisher, resource, detector or apparatus-certificate result is an empirical new-physics claim.

## Mandatory inference backbone

Primary detector quantity:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, detector nuisance profiling, full matrix PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time accounting and consistency gates.

Key no-go results remain active:

- **NG-005:** exact gravitational-null calibration cannot self-calibrate hidden source amplitude;
- **NG-006/007:** control degeneracies and low-frequency stability floors can survive arbitrarily high science exposure;
- **NG-023:** H-QND source metrology is not automatically ordered-response nondemolition;
- **NG-025/026:** locality belongs inside co-design; exact rank completion is not finite-noise closure;
- **NG-030:** robust architecture dominance requires conservative nonoverlap `T_i^upper < T_k^lower`.

## Physical wall-clock backbone

Use

`T_sci = Z^2/R_beta`,

`T_cal = gamma sum_j 1/R_cal,j`,

`T_src = C_src/R_src`,

with duty multiplier `m=1/(1-d)`.

For the standard late-front `Z=5`, 90% multiplicative source-retention benchmark, `C_src=225`.

Iteration 089 robust total-time envelope:

`T_total^upper = [Z^2/R_beta^- + gamma sum_j 1/R_cal,j^- + C_src/R_src^-]/(1-d^+)`.

## Correlated simultaneous two-band science

For raw band Fisher rates `r2,r4` and covariance correlation `rho`,

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`, `|rho|<1`.

Retain:

- **NG-036:** marginal PSD/ASD values do not determine simultaneous `R_beta`; cross-PSD/full spectral matrix is required;
- **RESOURCE-040:** robust lower rate uses the uncertainty upper bound on correlation plus rate-corner audit;
- **NG-037:** anti-correlation is not robust credit unless its uncertainty remains sufficiently negative.

## Seven-layer calibration and physical shots

For each same-time dual-probe block

`F_j=[[a_j,c_j],[c_j,b_j]]`,

use `R_cal,j=lambda_min(F_j)`.

Shot mapping:

`N_acc,j >= gamma/i_j^-`,

`N_try,j = gamma/(p_j^- i_j^-)`,

`R_cal,j^- = p_j^- i_j^- / t_cyc,j^+`.

**NG-038:** uncertainty crossing the PSD boundary does not certify positive calibration throughput.

## Source-preparation physical budget

For accepted-copy Ramsey Fisher `F_copy` and preparation success `p_E`,

**RESOURCE-051:**

`N_acc=C_src/F_copy`, `N_try=C_src/(p_E F_copy)`.

`T_src=N_try(t_reset+phi/Omega_E)=C_src/[p_E Omega_E q(V,Omega_E t_reset)]`.

Zero-reset `V=1` repository values at the rate optimum:

- Toy009 `F_copy~=0.00275637787`, `N_acc~=81628.866`;
- Toy014 `F_copy~=0.00348642430`, `N_acc~=64536.035`.

At the transparent `100 Hz`, `p_E=.5`, zero-reset benchmark:

- Toy009 `T_src~=283.818 s`;
- Toy014 `T_src~=190.311 s`.

These are model/benchmark resource conversions, not apparatus forecasts.

## Toy009/Toy014 physical crossover

For architecture `i`,

`T_i=m_i[A_i/R0+C_src/R_src,i]`,

where

`A_i=Z^2/s_i + gamma_i sum_j 1/k_ij`.

Nominal crossing follows from

`T_14-T_09=Delta_D/R0+Delta_S`.

Under interval uncertainty each robust boundary remains an exact `D/R0+S` curve (**RESOURCE-045**), and forward/reverse boundaries can leave an unresolved NG-043 throughput band.

Shared-kernel ratios `(q_s,q_c,q_p)` are regression summaries only and are not sufficient for robust physical dominance (**NG-044**).

## Characterization-time front

Iterations 094–097 turn apparatus uncertainty into decision value and finite measurement time.

For unresolved-band width `W` and half-width contraction coordinate `eta_x`,

`Lambda_x=(1/W)dW/deta_x`.

With physical characterization Fisher rate `R_char,x` and uncertainty scale `h_x`,

**RESOURCE-048:**

`Xi_x = -(1/W)dW/dt = 0.5 Lambda_x R_char,x h_x^2`.

Hence largest raw uncertainty or largest leverage need not be the best measurement per second (**NG-045/NG-049**).

Finite multi-channel characterization uses the water-filling allocation of Iteration 097 (**RESOURCE-050**); equal time is generally suboptimal (**NG-050**).

## Iteration 099 — primitive apparatus certificate

**APP-003:** absolute RESOURCE-045/NG-030 closure requires one common-normalization certificate containing, for both architectures:

1. science `(a2,a4,rho)`;
2. seven physical calibration rates `k1...k7` or full `2x2` Fisher blocks;
3. absolute detector/calibration scale `R0`;
4. source apparatus `(p_E,Omega_E,t_reset,V)` or certified `R_src`;
5. control/duty interval `d`;
6. characterization covariance/rates/floors/cost if RESOURCE-050 is used.

**NG-052:** complete toy-source coefficients do not imply a complete experiment certificate.

## Iteration 100 — single-platform cross-spectral audit

External anchor: Gosling et al., *Phys. Rev. Research* 6, 013129 (2024), one levitated nanoparticle platform measuring ordinary PSDs and an x-y cross-correlation spectrum, with susceptibility-based force calibration.

**APP-004:** same-platform measured cross-spectral covariance plus calibrated transfer is a legitimate apparatus primitive.

**NG-053:** spectral covariance is coordinate-specific. The published spatial `x-y` cross-spectrum cannot be substituted for the RQIR temporal `f,2f` cross-PSD without an explicit transfer, normalization and acquisition map.

## Iteration 101 — same-state temporal `f,2f` calibration protocol

For same-record demodulation filters,

**RESOURCE-053:**

`C_24 = integral dnu/(2 pi) S_y(nu) W_2^*(nu) W_4(nu)`.

For white noise and a rectangular block,

`c_24=exp[-i pi fT] sinc(fT)`.

**DESIGN-011:** choosing `T=M/f` with integer `M!=0` gives exact white-noise orthogonality between `f` and `2f`.

**NG-054:** orthogonal DFT bins do not certify `rho=0` for colored/nonstationary/window-leaked/shared-nuisance noise. A finite AR(1) regression gives `|corr|~=0.03655` for lag coefficient `0.8` despite orthogonal bins.

For balanced bands, nominal `rho0=0`, and 90% robust retained science fraction:

`rho_hi <= 1/9 ~= 0.111111`.

**RESOURCE-054:** ideal independent real bivariate Gaussian blocks give `I_rho=1/(1-rho^2)^2`; at `z=1.96` the transparent lower bound is `N_rho>=312` independent blocks.

**CAL-021:** inject known forces simultaneously at `f` and `2f` in the science operating state and use the same filters. The joint transfer Fisher is `F_cal=J_chi^T Sigma_z^-1 J_chi`.

For a conservative common transfer-amplitude error, 90% rate retention requires `epsilon_g<=0.0513167`; at `z=1.96`, matched fractional-transfer Fisher must satisfy `N*SNR_inj^2>=1458.80` (SNR 10 -> 15 blocks; SNR 5 -> 59).

**NG-055:** dual-tone calibration must pass linearity/intermodulation checks.

## Iteration 102 — joint science + transfer profile

Let `s` be the science mean derivative, `W` the science Fisher metric, `D` the transfer nuisance map and `C` the same-state injected-transfer Fisher.

**RESOURCE-055:**

`F_beta|g = s^T W s - s^T W D (D^T W D + C)^-1 D^T W s`.

**NG-056:** if independent per-band multiplicative gains span the science amplitude direction and `C=0`, then `F_beta|g=0`; extra science exposure cannot cure the exact transfer degeneracy.

**STAT-003:** in an ordinary Gaussian model with separate mean and covariance parameters, pure covariance parameter `rho` is Fisher-orthogonal to pure mean parameter `beta`. Its uncertainty enters the robust covariance envelope and characterization cost rather than the same mean-nuisance Schur subtraction.

**NG-057:** that orthogonality is conditional and can fail for beta-dependent covariance, non-Gaussian/cyclostationary likelihoods, shared transfer/whitening parameters or robust active-set changes.

Balanced symmetric slice with raw per-band science rate `r`, correlation `rho`, per-gain calibration rate `c`, science time `T_sci` and calibration time `T_cal`:

`F = 2 c r T_cal T_sci/[c T_cal(1+rho)+r T_sci]`.

Define

`R_s=2r/(1+rho)`, `R_c=2c`.

Then

`1/F = 1/(R_s T_sci)+1/(R_c T_cal)`.

**RESOURCE-056:** for target `F_*=Z^2`, the exact separate-time optimum is

`T_sci/T_cal=sqrt(R_c/R_s)`,

`T_total^min=F_*[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

Relative to perfect transfer calibration, `P=[1+sqrt(R_s/R_c)]^2`; therefore `P<=1.10` requires `R_c/R_s>=419.76`, `P<=1.25` requires `>=71.78`, and `P<=2` requires `>=5.828`.

Files:

- `analysis/joint_science_transfer_profile_iteration102.py`
- `docs/PAPER_III_JOINT_SCIENCE_TRANSFER_PROFILE_ITERATION102.md`
- `research_log/2026-08-30_iteration_102_joint_science_transfer_profile.md`
- `recovery/RECOVERY_DELTA_ITERATION_102.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 yet.

Extend RESOURCE-055 to the full complex four-real-component temporal `f,2f` likelihood with gain amplitude/phase, measured covariance uncertainty, spectral tilt, and one shared calibration-time budget across transfer calibration and all seven calibration layers. Optimize `T_sci+T_transfer+T_7cal`, then add source metrology and control duty.

Only if the residual dominant marginal cost after this common-normalization closure is demonstrably source-dependent should Toy015 be opened. Classical/stochastic/hybrid/full-QFT degeneracy and relativistic/gauge/conservation/causality/EFT/renormalization/measurability gates remain open unless explicitly closed elsewhere in the repository.
