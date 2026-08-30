# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 100**.

> The repository, not chat history, is authoritative. `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework; for the fast Paper-III front read this pointer plus `recovery/RECOVERY_DELTA_ITERATION_096.md` through `RECOVERY_DELTA_ITERATION_100.md`. Do not mix RQIR with RTK/DSIR.

## Publication-track status

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–100 translate abstract preparation/calibration Fisher requirements into physical detector, calibration, source, control and characterization rates and then audit whether one real apparatus can supply the required common-normalization certificate.

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

Files:

- `analysis/single_platform_cross_spectral_audit_iteration100.py`
- `docs/PAPER_III_SINGLE_PLATFORM_CROSS_SPECTRAL_AUDIT_ITERATION100.md`
- `research_log/2026-08-30_iteration_100_single_platform_cross_spectral_audit.md`
- `recovery/RECOVERY_DELTA_ITERATION_100.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 yet.

First search the same experimental family/data for a tunable two-frequency transfer calibration or public spectra that permit construction of the temporal `f,2f` matrix in one input-referred force coordinate. If that dataset does not exist, derive the minimum injected `f,2f` calibration protocol, block-count/shot requirement and uncertainty targets required to close `R0,a2,a4,rho` experimentally.

Only after that common-normalization cut is closed should RESOURCE-050/RESOURCE-045 be used for an absolute Toy009/Toy014 decision.

Classical/stochastic/hybrid/full-QFT degeneracy and relativistic/gauge/conservation/causality/EFT/renormalization/measurability gates remain open unless explicitly closed elsewhere in the repository.
