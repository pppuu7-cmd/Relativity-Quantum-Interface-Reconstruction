# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 101**.

> The repository, not chat history, is authoritative. `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework; for the fast Paper-III front read this pointer plus `recovery/RECOVERY_DELTA_ITERATION_096.md` through `RECOVERY_DELTA_ITERATION_101.md`. Do not mix RQIR with RTK/DSIR.

## Publication-track status

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–101 translate abstract preparation/calibration Fisher requirements into physical detector, calibration, source, control and characterization rates, audit what one real platform can supply, and now specify the minimum same-state temporal `f,2f` calibration needed to close the remaining detector cut.

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

**APP-004:** same-platform measured cross-spectral covariance plus calibrated transfer is a legitimate apparatus primitive. This strengthens the experimental grounding of NG-036: off-diagonal spectral information is measurable rather than merely formal.

**NG-053:** spectral covariance is coordinate-specific. The published spatial `x-y` cross-spectrum cannot be substituted for the RQIR temporal `f,2f` cross-PSD without an explicit transfer, normalization and acquisition map between those channel bases.

APP-003 status after Iteration 100:

- same-platform PSD + cross-spectrum capability: **CLOSED**;
- generic force-domain susceptibility/calibration relation: **PARTIAL**;
- exact temporal `f,2f` input-referred force matrix: **OPEN**;
- seven RQIR calibration Fisher blocks/rates: **OPEN**;
- Toy009/Toy014 preparation/reset/visibility/coherence throughput: **OPEN**;
- campaign duty/control/characterization-rate envelope: **OPEN**.

## Iteration 101 — same-state temporal `f,2f` calibration protocol

The same-family follow-up did not expose a public same-state two-tone `f,2f` force-transfer plus temporal covariance dataset, so the missing cut is now expressed as an explicit measurement protocol rather than a literature substitution.

For same-record demodulation filters,

**RESOURCE-053:**

`C_24 = integral dnu/(2 pi) S_y(nu) W_2^*(nu) W_4(nu)`.

For white noise and a rectangular block,

`c_24=exp[-i pi fT] sinc(fT)`.

**DESIGN-011:** choosing `T=M/f` with integer `M!=0` gives exact white-noise orthogonality between `f` and `2f`.

**NG-054:** orthogonal DFT bins do not certify `rho=0` for colored/nonstationary/window-leaked/shared-nuisance noise. A finite AR(1) regression gives `|corr|~=0.03655` for lag coefficient `0.8` despite orthogonal bins.

For robust retained fraction `q`, fixed raw rates give an analytic allowed `rho_hi`. For balanced bands, nominal `rho0=0`, `q=.90`:

`rho_hi <= 1/9 ~= 0.111111`.

**RESOURCE-054:** with ideal independent real bivariate Gaussian blocks and marginal variances profiled, `I_rho=1/(1-rho^2)^2`; at `z=1.96` the transparent lower bound is `N_rho>=312` independent blocks. Gosling's published `3.3 ms` block corresponds to `1.0296 s` only as an illustrative block-time scale, not an RQIR forecast.

**CAL-021:** inject known forces simultaneously at `f` and `2f` in the science operating state and use the same filters. The joint transfer Fisher is `F_cal=J_chi^T Sigma_z^-1 J_chi`.

For a conservative common transfer-amplitude error, 90% rate retention requires

`epsilon_g<=1-sqrt(.90)=0.0513167`.

At `z=1.96`, matched fractional-transfer Fisher must satisfy

`N*SNR_inj^2>=1458.80`;

examples: SNR 10 -> 15 independent blocks, SNR 5 -> 59.

**NG-055:** dual-tone calibration must pass linearity/intermodulation checks; high-SNR injection outside the weak-response regime cannot be credited as science-state transfer Fisher.

Files:

- `analysis/same_state_f2f_calibration_protocol_iteration101.py`
- `docs/PAPER_III_SAME_STATE_F2F_CALIBRATION_PROTOCOL_ITERATION101.md`
- `research_log/2026-08-30_iteration_101_same_state_f2f_calibration_protocol.md`
- `recovery/RECOVERY_DELTA_ITERATION_101.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 yet.

Build one **joint science + injected-transfer likelihood** with transfer amplitude/phase and temporal `rho` inside the nuisance vector. Compute the Schur-complement `F_beta|transfer,rho`, convert it to a physical Fisher rate, and optimize the split between calibration blocks and science blocks. This should identify whether cross-covariance estimation, transfer calibration or raw science exposure is the active detector bottleneck.

Only if the residual dominant cost after this common-normalization closure is demonstrably source-dependent should Toy015 be opened. Classical/stochastic/hybrid/full-QFT degeneracy and relativistic/gauge/conservation/causality/EFT/renormalization/measurability gates remain open unless explicitly closed elsewhere in the repository.
