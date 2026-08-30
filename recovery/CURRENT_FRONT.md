# RQIR Current Front Pointer

**Updated:** 2026-08-31  
**Authoritative front:** through **Iteration 112**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–112 translate abstract preparation/calibration Fisher requirements into physical detector, source, control, characterization and wall-clock resources.
- **Candidate Gravity:** inactive future branch. `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md` is entry planning only; QG-001…QG-010 have not been passed by a concrete model.

## Mandatory inference/resource backbone

Use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time, transfer gain/phase and all consistency/degeneracy gates. NG-005, NG-006/007, NG-023, NG-025/026, NG-030 and later control gates remain active.

Mature resource objects include:

- simultaneous two-band science `R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`;
- physical calibration blocks `R_cal,j=lambda_min(F_j)`;
- source shots `N_acc=C/F_copy`, `N_try=C/(p_E F_copy)`;
- same-state temporal `f,2f` protocol (101);
- joint science/transfer profiling (102);
- complex campaign allocation (103);
- robust source+detector final significance (104);
- architecture crossover `(u,v,z,delta)` (105);
- detector matrix-ratio certificate (106);
- recertification-constrained schedule (107);
- exact timing convention (108);
- scalar control Fisher envelope (109);
- cross-chat recovery consolidation (110);
- multi-control architecture threshold surface (111);
- matrix complex-gain/phase recertification envelope (112).

## Final-significance architecture backbone — Iterations 103–107

For campaign Fisher-rate matrices `J_k` and times `t_k`,

`J=sum_k t_k J_k=[[a,b^T],[b,N]]`,

`Phi(J)=a-b^T N^-1 b`.

**RESOURCE-057:** `R_*=max_x Phi(sum_k x_k J_k)`, `T_min=Z^2/R_*`.

**RESOURCE-058:** with `q=N^-1b`, `w=(1,-q)`, marginal campaign value is `w^T J_k w`.

**RESOURCE-059:** robust scheduling uses `max_x min_u Phi(sum_k x_k J_k(u))`.

**RESOURCE-060:** independent detector/source rates combine as

`T_min=F_*[1/sqrt(R_s)+1/sqrt(R_a)]^2`.

For Toy014/Toy009 define

`u=R_D,14/R_D,09`, `v=R_A,14/R_A,09`, `z=R_A,09/R_D,09`, `delta=(1-d14)/(1-d09)`.

**RESOURCE-061:**

`Q14/Q09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

**NG-062:** detector no-rescue condition is `delta v (1+sqrt(z))^2 <= 1`; otherwise

`u_req=[sqrt(delta)(1+z^-1/2)-(v z)^-1/2]^-2`.

**RESOURCE-062/063:** common-coordinate Fisher matrices can bound `u` through Loewner/generalized-eigenvalue certificates and propagate interval/joint uncertainty under NG-030.

**RESOURCE-064:** mandatory physical quotas use

`X={x>=0,1^T x=1,A x>=b}`,

`R_D^rob=max_{x in X} min_u Phi(sum_k x_k J_k(u))`.

## Iterations 108–111 — scalar/multi-control recertification

For pure-dead timing overhead/live ratio `r`,

`eta_live=1/(1+r)` and `u_wall=u_live(1+r09)/(1+r14)`.

For one scalar control with

`S=sigma_*^2-sigma_f^2>0`, Brownian convention `Var=D t/2`, reference Fisher rate `R_ref`,

**RESOURCE-067:**

`sigma_ref^2=S/2`, `t_ref*=2/(R_ref S)`, `tau_live*=S/D`, `r_min=2D/(R_ref S^2)`.

**RESOURCE-068:** `R_ref >= 2D/[r_max S^2]`.

For several independent, non-overlapping pure-dead controls,

**RESOURCE-069:** `H_i=sum_j h_ij`, `eta_i=1/(1+H_i)`,

`u_wall=u_live(1+H09)/(1+H14)`.

**RESOURCE-070/071:** per-control headroom and robust interval corners determine whether a missing physical reference channel can change the architecture decision.

Timing is already in a common physical coordinate and remains sub-percent in the stored benchmark slice. Geometry and additive SI transduction/stability remain open.

## Iteration 112 — matrix complex-gain/phase recertification

Complex transfer gain/phase must generally be treated as one correlated matrix control rather than independent scalar amplitude/phase loads.

Let

`S=Sigma_*-Sigma_f > 0`,

`F_ref` be the same-state reference Fisher-rate matrix, and `Q` the covariance-diffusion matrix with `Cov_drift=tau Q/2`.

Require

`(t_ref F_ref)^-1 + tau Q/2 <= S`.

Whiten with

`A=S^-1/2 F_ref^-1 S^-1/2`,

`B=S^-1/2 Q S^-1/2`.

At fixed cadence,

`t_ref,min(tau)=lambda_max[(I-tau B/2)^-1/2 A (I-tau B/2)^-1/2]`.

### RESOURCE-072

`r_mat*=min_tau t_ref,min(tau)/tau`, `0<tau<2/lambda_max(B)`.

This is an exact one-dimensional optimization retaining full gain/phase Fisher, drift and tolerance orientation. It reproduces RESOURCE-067 in one dimension and is invariant under nonsingular control-coordinate changes.

### NG-068

Correlated/shared complex gain/phase controls cannot generally be replaced by basis-dependent independent scalar overheads.

A deterministic same-spectrum 2D regression gives `r*~=51.005` versus `~200.000` under a change only in Fisher/drift orientation, a `~3.92x` difference. These are dimensionless regression values, not apparatus forecasts.

### DESIGN-016

Co-design reference Fisher with generalized fast-drift/tight-budget modes rather than marginal amplitude/phase SNR.

### RESOURCE-073

A joint pure-dead gain/phase block enters the Iteration-111 architecture headroom through `r_mat*`. For uniform reference-Fisher scaling `F_ref->kappa F_ref`,

`r_mat*(kappa)=r_mat*(1)/kappa`,

so `kappa_req=r_mat*/K_gain-phase` at the architecture boundary.

Files:

- `analysis/matrix_gain_phase_recertification_iteration112.py`
- `docs/PAPER_III_MATRIX_GAIN_PHASE_RECERTIFICATION_ITERATION112.md`
- `research_log/2026-08-31_iteration_112_matrix_gain_phase_recertification.md`
- `recovery/RECOVERY_DELTA_ITERATION_112.md`

## Current open Paper-III controls

- timing: physical/parameterized;
- complex gain/phase: **matrix algebraic recertification closed**, physical same-apparatus drift/floor and likelihood-derived covariance budget still open;
- geometry: common SI transduction + drift + reference Fisher open;
- additive mean/covariance: common SI transduction + drift + reference Fisher open;
- robust numerical `u=R_D,14/R_D,09` interval under one declared apparatus remains open.

## Immediate next gate — Paper III only

Do **not** start Toy015 and do not activate Candidate Gravity as a claimed model yet.

Derive the admissible complex-transfer covariance budget `Sigma_*` directly from detector-level profiled-Fisher loss geometry in Iterations 102–103, then combine it with RESOURCE-072. This removes arbitrary separate amplitude/phase tolerances.

If physical drift/stability matrices remain unavailable without external hardware assumptions, keep `Q`/`Sigma_f` symbolic and derive the strongest apparatus-independent threshold surface. Then recompute the robust detector-ratio interval and combine it with `(v,z,delta)` through RESOURCE-061/063/NG-030.

Toy015 becomes admissible only if the remaining dominant architecture uncertainty or marginal wall-clock cost is demonstrably source-dependent. Candidate Gravity begins only when a concrete dynamics can enter QG-001…QG-010; the reconstruction papers themselves are not a QG theory.
