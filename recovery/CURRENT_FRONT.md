# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 105**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–105 translate abstract preparation/calibration Fisher requirements into physical detector, transfer, source, control, characterization and wall-clock rates, with robust final-significance scheduling and common-normalization apparatus cuts.

## Mandatory inference backbone

Use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time and all consistency/degeneracy gates. NG-005, NG-006/007, NG-023, NG-025/026 and NG-030 remain active.

## Mature physical pieces retained

- simultaneous two-band science:

  `R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`;

- seven physical calibration blocks:

  `R_cal,j=lambda_min(F_j)`;

- source Ramsey shot mapping:

  `N_acc=C/F_copy`, `N_try=C/(p_E F_copy)`;

- same-state temporal `f,2f` covariance/injection protocol (Iteration 101);
- joint transfer-gain profiling (Iteration 102);
- full four-real complex campaign optimization (Iteration 103).

## Iteration 103 — full complex campaign simplex

For campaign Fisher-rate matrices `J_k` and times `t_k`,

`J=sum_k t_k J_k=[[a,b^T],[b,N]]`,

`F_beta=a-b^T N^-1 b`.

**RESOURCE-057:** profiled Fisher is concave and positively homogeneous on a fixed identifiable branch. With campaign fractions `x_k`,

`R_*=max_{x>=0,sum x=1} F_beta(sum_k x_k J_k)`,

`T_min=Z^2/R_*`.

**RESOURCE-058:** with `q=N^-1b`, `w=(1,-q)`,

`dF_beta/dt_k=w^T J_k w`.

At an interior optimum active campaigns equalize marginal profiled Fisher per second.

**NG-058:** transfer phase can be omitted only after Fisher-metric, not merely Euclidean, orthogonality is demonstrated.

## Iteration 104 — robust final-significance source closure

For local source-amplitude profiling,

`F_final=A C/(A+C)`.

**NUM-006:** the historical `A=25`, `C=225` benchmark gives `F_final=22.5` (`4.74341649 sigma`). It is correctly retained as 90% of a **raw detector** 5-sigma benchmark, not a final post-profile 5-sigma certificate.

For final `Z=5` at fixed 90% retention use

`A=27.77777778`, `C=250`.

**RESOURCE-060:** with raw detector rate `R_s` and source-amplitude rate `R_a`,

`1/F=1/(R_s T_s)+1/(R_a T_a)`,

`T_s/T_a=sqrt(R_a/R_s)`,

`T_min=F_*[1/sqrt(R_s)+1/sqrt(R_a)]^2`,

`r_*=sqrt(R_a)/(sqrt(R_s)+sqrt(R_a))`.

**NG-059:** fixed 90% retention is minimum-time optimal only for `R_a/R_s=81`.

**RESOURCE-059:** for apparatus uncertainty `u`,

`R_rob^*=max_x min_u F_beta(sum_k x_k J_k(u))`.

On a fixed identifiable affine-polytope branch the robust scheduling problem is convex and the uncertainty minimum is attained at a vertex. Active worst-case vertices combine to an equal-marginal KKT certificate.

## Iteration 105 — final-significance architecture crossover

Compress, where valid, the already optimized detector/transfer/seven-calibration side of architecture `i` to `R_D,i` and independent source-amplitude metrology to `R_A,i`:

`R_final,i = 1/[1/sqrt(R_D,i)+1/sqrt(R_A,i)]^2`.

With multiplicative duty `d_i`, `Q_i=(1-d_i)R_final,i`.

Define

`u=R_D,14/R_D,09`,

`v=R_A,14/R_A,09`,

`z=R_A,09/R_D,09`,

`delta=(1-d_14)/(1-d_09)`.

**RESOURCE-061:**

`Q_14/Q_09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

Toy014 is faster iff this ratio exceeds one. Final target `Z` cancels from the ranking in the local-linear regime.

With `w=1/sqrt(z)`, a positive finite crossing is

`w_cross=[1/sqrt(u)-sqrt(delta)]/[sqrt(delta)-1/sqrt(v)]`,

`z_cross=1/w_cross^2`.

**DESIGN-012:** source domination favors Toy014 exactly when `v>u`; favors Toy009 when `v<u`; is neutral when `v=u` apart from duty.

**NG-060:** the Toy014 Ramsey/source rate advantage alone is not an architecture certificate. A source-rescue claim requires common-normalization `u,v,z,delta` or the underlying robust Fisher matrices.

Regression only: using the retained Toy014/Toy009 **science-only shared-kernel** `u_reg=0.2830146574583767` and zero-reset Ramsey `v_reg=1.4913343179877905`, equal duty gives

`z_cross=0.042393961570158255`.

With illustrative `d09=.02`, `d14=.08`, it shifts to `0.027135455186203732`. These are not full detector+7cal apparatus decisions.

Files:

- `analysis/full_complex_campaign_allocation_iteration103.py`
- `docs/PAPER_III_FULL_COMPLEX_CAMPAIGN_ALLOCATION_ITERATION103.md`
- `recovery/RECOVERY_DELTA_ITERATION_103.md`
- `analysis/robust_campaign_source_target_iteration104.py`
- `docs/PAPER_III_ROBUST_CAMPAIGN_SOURCE_TARGET_ITERATION104.md`
- `recovery/RECOVERY_DELTA_ITERATION_104.md`
- `analysis/final_significance_architecture_crossover_iteration105.py`
- `docs/PAPER_III_FINAL_SIGNIFICANCE_ARCHITECTURE_CROSSOVER_ITERATION105.md`
- `research_log/2026-08-30_iteration_105_final_significance_architecture_crossover.md`
- `recovery/RECOVERY_DELTA_ITERATION_105.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 yet.

The highest-value missing physical quantity is now the robust common-apparatus detector-side ratio

`u=R_D,14/R_D,09`

after complex transfer calibration, temporal PSD/cross-PSD uncertainty, all seven physical calibration layers and mandatory detector/control scheduling.

If a full common-normalization apparatus matrix is unavailable, derive certified threshold surfaces for `u` from measurable transfer/calibration-rate intervals and control-duty bounds rather than fabricate an absolute winner. Then combine with robust `v,z,delta` using RESOURCE-061/NG-030.

Toy015 becomes admissible only if the residual dominant marginal wall-clock cost or decision uncertainty is demonstrably source-dependent. Classical/stochastic/hybrid/full-QFT degeneracy and relativistic/gauge/conservation/causality/EFT/renormalization/measurability gates remain open unless explicitly closed elsewhere in the repository.
