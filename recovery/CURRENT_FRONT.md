# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 103**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–103 translate abstract preparation/calibration Fisher requirements into physical detector, calibration, source, control and characterization rates; establish robust simultaneous `f,2f` likelihood requirements; audit single-platform apparatus primitives; put same-state complex transfer calibration inside detector-level profiling; and now solve science + transfer + multi-calibration scheduling at the full Fisher-matrix level.

No toy, Fisher, detector, calibration, resource or apparatus-certificate result is an empirical new-physics claim.

## Mandatory inference backbone

Primary detector quantity:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain:

- exact hard constraints;
- centered covariance derivatives;
- spectral-tilt profiling;
- full matrix PSD/cross-PSD Fisher;
- source-preparation calibration;
- coherence/reset/dead-time accounting;
- consistency/degeneracy gates.

Key retained no-go gates include:

- **NG-005:** exact gravitational-null calibration cannot self-calibrate hidden source amplitude;
- **NG-006/007:** low-rank control degeneracies and stability floors can survive arbitrarily high science exposure;
- **NG-023:** H-QND source metrology is not automatically ordered-response nondemolition;
- **NG-025/026:** locality belongs inside co-design; exact rank completion is not finite-noise/resource closure;
- **NG-030:** robust architecture dominance requires conservative nonoverlap `T_i^upper < T_k^lower`.

## Physical wall-clock backbone

Use

`T_sci = Z^2/R_beta`,

`T_cal = gamma sum_j 1/R_cal,j`,

`T_src = C_src/R_src`,

with duty multiplier `m=1/(1-d)`.

For the mature `Z=5`, 90% multiplicative source-retention benchmark:

`C_src=225`.

Iteration 089 robust upper envelope remains

`T_total^upper=[Z^2/R_beta^- + gamma sum_j 1/R_cal,j^- + C_src/R_src^-]/(1-d^+)`.

## Simultaneous two-band science and calibration

For raw band Fisher rates `r2,r4` and ordinary covariance correlation `rho`,

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`, `|rho|<1`.

Retain:

- **NG-036:** marginal ASD/PSD values do not determine simultaneous `R_beta`; the cross-PSD/full spectral matrix is required;
- **RESOURCE-040:** robust lower science rate uses the conservative covariance/rate envelope;
- **NG-037:** anti-correlation is not robust credit unless its uncertainty remains sufficiently negative.

Each same-time dual-probe calibration block is represented physically by

`F_j=[[a_j,c_j],[c_j,b_j]]`,

with robust calibration rate

`R_cal,j=lambda_min(F_j)`.

Shot mapping:

`N_acc,j >= gamma/i_j^-`,

`N_try,j = gamma/(p_j^- i_j^-)`,

`R_cal,j^- = p_j^- i_j^- / t_cyc,j^+`.

**NG-038:** uncertainty crossing the PSD boundary does not certify positive calibration throughput.

## Source-preparation physical budget

For accepted-copy Ramsey Fisher `F_copy` and preparation acceptance `p_E`,

`N_acc=C_src/F_copy`,

`N_try=C_src/(p_E F_copy)`,

`T_src=C_src/[p_E Omega_E q(V,Omega_E t_reset)]`.

Repository zero-reset `V=1` rate-optimal values:

- Toy009: `F_copy~=0.00275637787`, `N_acc~=81628.866`;
- Toy014: `F_copy~=0.00348642430`, `N_acc~=64536.035`.

At the transparent `Omega_E=100 Hz`, `p_E=.5`, zero-reset benchmark:

- Toy009 `T_src~=283.818 s`;
- Toy014 `T_src~=190.311 s`.

These remain model/resource conversions, not apparatus forecasts.

## Toy009/Toy014 physical decision backbone

For architecture `i`,

`T_i=m_i[A_i/R0+C_src/R_src,i]`,

where

`A_i=Z^2/s_i + gamma_i sum_j 1/k_ij`.

Nominal and robust physical crossover laws are in Iterations 092–093. Under uncertainty, forward and reverse robust boundaries can leave an unresolved NG-043 throughput band. Shared-kernel ratios `(q_s,q_c,q_p)` are regression summaries only (**NG-044**).

Iterations 094–097 add characterization value-of-information, physical characterization Fisher rates and water-filling. Measurement priority is by decision reduction per physical characterization second, not raw percent uncertainty.

## Primitive apparatus certificate — Iterations 099–101

**APP-003:** an absolute NG-030 decision requires one common-normalization certificate containing, for both architectures:

1. science `(a2,a4,rho)` or equivalent full spectral Fisher object;
2. seven physical calibration rates/matrices;
3. absolute detector/calibration normalization `R0`;
4. source apparatus `(p_E,Omega_E,t_reset,V)` or certified `R_src`;
5. control/duty interval;
6. characterization covariance/rates/floors if physical scheduling is optimized.

**NG-052:** complete toy-source coefficients do not imply a complete experimental certificate.

Iteration 100 shows that same-platform spectral covariance plus calibrated susceptibility is experimentally available, but a spatial `x-y` cross-spectrum cannot be substituted for the temporal `f,2f` matrix (**NG-053**).

Iteration 101 converts the temporal `f,2f` cut into an explicit same-state protocol:

`C_24 = integral dnu/(2 pi) S_y(nu) W_2^*(nu) W_4(nu)`.

For white noise and rectangular blocks, choosing `T=M/f` gives exact white-noise `f,2f` orthogonality, but **NG-054** forbids assuming `rho=0` under colored/nonstationary/window-leaked/shared-nuisance noise.

For balanced bands and nominal `rho=0`, 90% robust retention requires

`rho_hi <= 1/9`.

Ideal Gaussian block estimation gives the transparent `z=1.96` lower bound `N_rho>=312` blocks.

Same-state dual-tone transfer calibration is mandatory (**CAL-021**) and must pass linearity/intermodulation checks (**NG-055**).

## Iteration 102 — joint science + transfer profile

With science derivative `s`, Fisher metric `W`, transfer nuisance map `D` and injected-transfer Fisher `C`,

**RESOURCE-055:**

`F_beta|g = s^T W s - s^T W D (D^T W D + C)^-1 D^T W s`.

**NG-056:** free independent per-band multiplicative gains can erase common-amplitude science Fisher completely.

**STAT-003:** in an ordinary Gaussian model, a covariance-only parameter such as `rho` is expected-Fisher orthogonal to a pure mean parameter; its uncertainty belongs in the covariance envelope/characterization budget rather than the same mean-nuisance Schur subtraction. **NG-057** lists the cases where that separation can fail.

Balanced symmetric slice:

`1/F = 1/(R_s T_sci)+1/(R_c T_cal)`.

**RESOURCE-056:**

`T_sci/T_cal=sqrt(R_c/R_s)`,

`T_total^min=Z^2[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

## Iteration 103 — full complex campaign allocation

The data vector is now the complete four-real temporal two-band object

`(Re z_f, Im z_f, Re z_2f, Im z_2f)`.

Let every science/calibration campaign `k` provide a PSD Fisher-rate matrix `J_k` in the common parameter vector `(beta,theta)`. For times `t_k`,

`J(t)=sum_k t_k J_k=[[a,b^T],[b,N]]`,

`F_beta(t)=a-b^T N^-1 b`.

### RESOURCE-057 — campaign-simplex theorem

`F_beta(t)` is concave and positively homogeneous on an identifiable fixed-likelihood branch. Hence

`min sum_k t_k  subject to F_beta>=Z^2`

is convex. With campaign fractions `x_k>=0`, `sum x_k=1`, define

`R_*=max_x F_beta(sum_k x_k J_k)`.

Then

`T_min=Z^2/R_*`.

This includes science acquisition, same-state complex-transfer injection and all seven calibration layers in one scheduling problem.

### RESOURCE-058 — equal marginal profiled-Fisher rule

Let

`q=N^-1b`, `w=(1,-q)`.

Then

`partial F_beta/partial t_k = w^T J_k w`.

At an interior optimum every active campaign has marginal retained science Fisher rate exactly `R_*`; inactive campaigns have no larger marginal value. Equal time, equal raw SNR and equal standalone calibration precision are generally not optimal.

### NG-058 — transfer phase is Fisher-metric dependent

Euclidean complex amplitude/phase orthogonality is not enough to drop phase calibration. The relevant condition is Fisher-metric orthogonality such as

`s_beta^T W p_n=0`

after the declared whitening/nuisance structure. A deterministic positive-definite non-isotropic regression gives nonzero beta/phase couplings even though unweighted quadrature products vanish.

The full-complex regression also reproduces NG-056: free independent complex gains erase beta information, while same-state transfer Fisher restores it.

Files:

- `analysis/full_complex_campaign_allocation_iteration103.py`
- `docs/PAPER_III_FULL_COMPLEX_CAMPAIGN_ALLOCATION_ITERATION103.md`
- `research_log/2026-08-30_iteration_103_full_complex_campaign_allocation.md`
- `recovery/RECOVERY_DELTA_ITERATION_103.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 yet.

Extend RESOURCE-057/058 to the **robust max-min apparatus envelope**:

1. optimize campaign fractions against the worst admissible temporal PSD/cross-PSD, transfer and calibration-rate uncertainty;
2. include the physical source-metrology rate and source-copy constraint;
3. include control/reference duty and mandatory recertification constraints;
4. run the same robust scheduler for Toy009 and Toy014 and apply NG-030.

Only if the resulting dominant marginal wall-clock cost/decision uncertainty is demonstrably source-dependent should Toy015 be opened.

Classical/stochastic/hybrid/full-QFT degeneracy and relativistic/gauge/conservation/causality/EFT/renormalization/measurability gates remain open unless explicitly closed elsewhere in the repository.
