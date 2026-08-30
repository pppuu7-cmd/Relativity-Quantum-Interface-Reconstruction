# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 104**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–104 translate abstract source/calibration Fisher requirements into physical detector, transfer, calibration, source, characterization and wall-clock resources, with robust profiling and common-normalization apparatus cuts.

## Mandatory inference backbone

Use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time and all consistency/degeneracy gates.

Key still-open/mandatory guards include NG-005, NG-006/007, NG-023, NG-025/026 and NG-030.

## Mature physical pieces retained

- simultaneous two-band science:

  `R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`;

- seven physical calibration blocks:

  `R_cal,j=lambda_min(F_j)`;

- source Ramsey shot mapping:

  `N_acc=C/F_copy`, `N_try=C/(p_E F_copy)`;

- same-state temporal `f,2f` covariance/injection protocol from Iteration 101;
- joint transfer-gain profile from Iteration 102;
- full complex four-real `f,2f` campaign optimization from Iteration 103.

## Iteration 103 — full complex campaign simplex

For campaign Fisher-rate matrices `J_k` and non-negative times `t_k`,

`J=sum_k t_k J_k=[[a,b^T],[b,N]]`,

`F_beta=a-b^T N^-1 b`.

**RESOURCE-057:** the profiled Fisher is concave and positively homogeneous on a fixed identifiable branch. With campaign fractions `x_k`,

`R_*=max_{x>=0,sum x=1} F_beta(sum_k x_k J_k)`,

`T_min=Z^2/R_*`.

**RESOURCE-058:** if `q=N^-1b`, `w=(1,-q)`, then

`dF_beta/dt_k=w^T J_k w`.

At an interior optimum active campaigns equalize marginal profiled Fisher per second.

**NG-058:** transfer phase cannot be dropped merely from Euclidean amplitude/phase orthogonality; Fisher-metric orthogonality must be demonstrated.

## Iteration 104 — robust final-significance source closure

### NUM-006 — distinguish raw and final significance

For local source-amplitude profiling,

`F_final=A C/(A+C)`.

The historical benchmark

`A=25`, `C=225`

gives

`F_final=22.5`, `sqrt(F_final)=4.74341649`.

Thus `C_src=225` is correctly retained as **90% of a raw detector 5-sigma benchmark**, not as a final post-profile 5-sigma certificate.

For final `Z=5` at fixed 90% retention use

`A=27.77777778`, `C=250`.

### RESOURCE-060 — jointly optimize source metrology

With raw detector science rate `R_s` and independent source-amplitude Fisher rate `R_a`,

`1/F=1/(R_s T_s)+1/(R_a T_a)`.

The minimum-time final-target solution is

`T_s/T_a=sqrt(R_a/R_s)`,

`T_min=F_*[1/sqrt(R_s)+1/sqrt(R_a)]^2`,

with optimal retained fraction

`r_*=sqrt(R_a)/(sqrt(R_s)+sqrt(R_a))`.

**NG-059:** fixed 90% retention is wall-clock optimal only when `R_a/R_s=81`; otherwise it over- or under-calibrates relative to the minimum-time final-significance solution.

### RESOURCE-059 — robust campaign simplex

For apparatus uncertainty `u`,

`R_rob^*=max_x min_u F_beta(sum_k x_k J_k(u))`.

On a fixed identifiable branch with Fisher matrices affine over a polytope uncertainty set, the robust objective remains a convex scheduling problem and the uncertainty minimum is attained at an extreme point.

At a robust optimum, a convex combination of marginal profile-Fisher rates from the active worst-case vertices equalizes across active campaigns.

Regression: vertices `(R_s,R_a)=(1,9)` and `(9,1)` give robust fractions `(0.5,0.5)`, guaranteed rate `0.45`, and active-vertex marginal vectors `(0.81,0.09)` / `(0.09,0.81)`, averaging to `(0.45,0.45)`.

Files:

- `analysis/full_complex_campaign_allocation_iteration103.py`
- `docs/PAPER_III_FULL_COMPLEX_CAMPAIGN_ALLOCATION_ITERATION103.md`
- `recovery/RECOVERY_DELTA_ITERATION_103.md`
- `analysis/robust_campaign_source_target_iteration104.py`
- `docs/PAPER_III_ROBUST_CAMPAIGN_SOURCE_TARGET_ITERATION104.md`
- `research_log/2026-08-30_iteration_104_robust_campaign_source_target.md`
- `recovery/RECOVERY_DELTA_ITERATION_104.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 yet.

Build a unified Toy009/Toy014 **final-significance** campaign certificate in which source metrology is a Fisher campaign rather than a fixed `C_src` add-on, while the old `C_src=225` convention remains a regression slice. Add control/reference recertification and duty as explicit scheduling constraints, then run the same robust schedule for Toy009 and Toy014 and apply NG-030.

If a full common-normalization apparatus matrix is still unavailable, derive threshold surfaces in measurable rate ratios rather than fabricating an absolute winner. Toy015 becomes admissible only if the residual dominant marginal cost is demonstrably source-dependent.

Classical/stochastic/hybrid/full-QFT degeneracy and relativistic/gauge/conservation/causality/EFT/renormalization/measurability gates remain open unless explicitly closed elsewhere in the repository.
