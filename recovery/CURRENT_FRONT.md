# RQIR Current Front Pointer

**Updated:** 2026-08-31  
**Authoritative front:** through **Iteration 115**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–115 translate abstract preparation/calibration Fisher requirements into detector/source/control/transfer Fisher rates, recertification, robust final significance and wall-clock architecture certificates.
- **Candidate Gravity:** inactive future branch. `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md` is entry planning only; no concrete model has passed QG-001…QG-010.

## Mandatory inference backbone

Always use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time, transfer gain/phase and all consistency/degeneracy gates. In particular NG-005, NG-006/007, NG-023, NG-025/026, NG-030 and later transfer/control gates remain active.

The old post-Toy010 task of translating abstract `C_a` and `gamma` into physical repetitions/shot noise/calibration time/coherence/source metrology/detector SNR is already closed by the Paper-III resource chain. Do not restart it.

## Mature resource backbone

- correlated simultaneous two-band science:
  `R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`;
- physical calibration blocks:
  `R_cal,j=lambda_min(F_j)`;
- source shots:
  `N_acc=C/F_copy`, `N_try=C/(p_E F_copy)`;
- campaign allocation:
  `R_*=max_x Phi(sum_k x_k J_k)`, with `Phi([[a,b^T],[b,N]])=a-b^T N^-1 b`;
- robust scheduling:
  `max_x min_u Phi(sum_k x_k J_k(u))`;
- independent detector/source final-significance closure:
  `T_min=F_*[1/sqrt(R_D)+1/sqrt(R_A)]^2`;
- architecture variables:
  `u=R_D14/R_D09`, `v=R_A14/R_A09`, `z=R_A09/R_D09`, `delta=(1-d14)/(1-d09)`;
- final ratio:
  `Q14/Q09=delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

## Control/transfer front through Iteration 114

Scalar pure-dead recertification:

`r_min=2D/[R_ref (sigma_*^2-sigma_f^2)^2]`.

Matrix complex-gain/phase recertification (Iteration 112):

`(t_ref F_ref)^-1 + tau Q/2 <= S`,

with exact one-dimensional cadence optimization after whitening. NG-068 forbids replacing correlated gain/phase control by arbitrary independent scalar overheads.

Likelihood-derived transfer budget (Iteration 113): after profiling non-transfer nuisances,

`J_bar=[[F0,b^T],[b,G]]`,

`F_beta(C)=F0-b^T(G+C)^-1 b`.

Retention `F_beta>=qF0` is equivalent to

`G+C >= b b^T/[(1-q)F0]`.

NG-069: scalar-beta retention defines an admissible covariance set, not generally one unique full `Sigma_*`.

Two-band gain/tilt quotient (Iteration 114): common fractional gain is beta-aligned and differential gain is spectral-tilt aligned. Free per-band gains imply exact `F_beta=0` (NG-071). For a phase-profiled 2x2 gain-reference Fisher,

`C_com=4 det(C_g)/(C22+C44-2C24)`.

Science plus separate common-gain calibration obeys

`F_beta=F_s C_com/(F_s+C_com)`

and the optimized rate is

`R_DT=1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

## Iteration 115 — full-complex common-gain rate certificate

The same-state dual-tone reference is now reduced from its measurable full four-real transfer Fisher to the scalar common-gain rate without discarding amplitude/phase correlations.

Use physical transfer coordinates

`x=(g2,g4,phi2,phi4)`.

For one accepted block,

`F_blk=J_chi^T Sigma_z^-1 J_chi`.

For independent cycles with acceptance `p_cal` and full cycle wall time `tau_cyc`, when rejected blocks carry no usable transfer Fisher,

`K_x=(p_cal/tau_cyc) F_blk`.

Transform gains by

`g2=c-d`, `g4=c+d`,

and write the transformed rate matrix in coordinates `y=(c,d,phi2,phi4)` as

`K_y=[[k_cc,k_cnu],[k_nuc,K_nunu]]`, `nu=(d,phi2,phi4)`.

### RESOURCE-079 — full-complex common-gain rate

`R_c = k_cc - k_cnu K_nunu^-1 k_nuc`.

Direct profiling over `(d,phi2,phi4)` equals phase-first then differential-gain profiling. The deterministic 1000-matrix regression agrees to `<1.6e-15` relative error.

The phase-free slice exactly recovers Iteration 114:

`R_c=4 det(K_g)/(K22+K44-2K24)`.

### NG-072 — same hardware does not imply `c=1`

For Toy014/Toy009,

`c=R_c14/R_c09`.

`c=1` is exact if their same-state transfer Fisher-rate matrices are equal in the same coordinates. Using the same hardware is insufficient if source choice changes the transfer Jacobian, covariance, acquisition window, cycle duration, acceptance/reset/readout, feedback/trap state or included nuisance priors.

### RESOURCE-080 — Loewner-to-architecture certificate

RESOURCE-079 is homogeneous and Loewner-monotone. If

`m_i K0 <= K_i <= M_i K0`,

then

`m_i R_c0 <= R_c,i <= M_i R_c0`.

Therefore

`c in [m14/M09, M14/m09]`.

This propagates full correlated complex-transfer uncertainty without arbitrary independent amplitude/phase tolerances.

### RESOURCE-081 — robust detector+transfer quotient box

With

`s=R_s14/R_s09`, `c=R_c14/R_c09`, `z_c=R_c09/R_s09`,

`u_DT=[(1+z_c^-1/2)/(s^-1/2+(c z_c)^-1/2)]^2`.

For positive interval boxes in `(s,c,z_c)`, extrema are attained at box corners; no hidden interior extremum exists. A dimensionless regression box only (not an apparatus forecast) verifies the enclosure by dense scanning.

Files:

- `analysis/full_complex_common_gain_rate_iteration115.py`
- `docs/PAPER_III_FULL_COMPLEX_COMMON_GAIN_RATE_CERTIFICATE_ITERATION115.md`
- `research_log/2026-08-31_iteration_115_full_complex_common_gain_rate.md`
- `recovery/RECOVERY_DELTA_ITERATION_115.md`

## Current open Paper-III controls

- timing: physical/parameterized;
- common transfer amplitude: full-complex Fisher-rate reduction closed; measured/defensibly specified same-state `K_x` interval remains open;
- complex phase drift: algebraic matrix recertification exists; physical drift/floor remains open;
- geometry: common SI transduction + drift + reference Fisher open;
- additive mean/covariance: common SI transduction + drift + reference Fisher open;
- seven-layer calibration + transfer joint scheduling without double counting remains open;
- final robust numerical `u=R_D14/R_D09` under one declared apparatus remains open.

## Immediate next gate — Paper III only

Do **not** start Toy015 and do not activate Candidate Gravity as a claimed model yet.

Insert RESOURCE-079/080 into the seven-layer physical campaign scheduler. Determine whether same-state dual-tone blocks carry joint Fisher for transfer and any of the seven calibration-layer nuisance coordinates. If yes, credit the joint block once through RESOURCE-057/064; if blocks are non-overlapping pure-dead references, use Iterations 107–112 recertification overhead.

The target is the first non-double-counted robust interval for the full detector-side Toy014/Toy009 ratio `u`, followed by RESOURCE-061/063 and NG-030 with source metrology `(v,z)` and duty `delta`.

Keep phase drift, geometry and additive SI rates symbolic unless a same-apparatus physical likelihood supplies them. Toy015 becomes admissible only if the residual dominant architecture uncertainty or marginal wall-clock cost is demonstrably source-dependent.
