# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 107**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–107 translate abstract preparation/calibration Fisher requirements into physical detector, transfer, source, control, characterization and wall-clock rates, with robust final-significance scheduling, common-normalization matrix certificates and explicit recertification constraints.

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

**DESIGN-012:** source domination favors Toy014 exactly when `v>u`; favors Toy009 when `v<u`; apart from duty it is neutral when `v=u`.

**NG-060:** the Toy014 Ramsey/source rate advantage alone is not an architecture certificate. A source-rescue claim requires common-normalization `u,v,z,delta` or the underlying robust Fisher matrices.

## Iteration 106 — robust detector-side ratio certificate

For the profiled Fisher functional

`Phi(J)=a-b^T N^-1 b=min_q (1,-q)^T J (1,-q)`,

Loewner monotonicity and positive homogeneity imply the following.

### RESOURCE-062

If uniformly over common campaigns and apparatus uncertainty

`alpha J_09,k <= J_14,k <= beta J_09,k`

and both architectures share the same feasible campaign-fraction set, then

`alpha <= u=R_D,14/R_D,09 <= beta`.

For positive-definite reference matrices, obtain the tight per-campaign envelope from generalized eigenvalues of

`J_09,k^-1/2 J_14,k J_09,k^-1/2`.

Singular Fisher supports must be audited explicitly.

### NG-061

Science-only SNR ratios, gamma ratios, calibration-cost ratios and marginal transfer-error ratios do not by themselves certify `u`; nuisance orientation/support and the physical schedule set matter.

### NG-062 — detector no-rescue condition

From RESOURCE-061, the `u -> infinity` limit is

`G_inf=delta v (1+sqrt(z))^2`.

If

`delta v (1+sqrt(z))^2 <= 1`,

Toy014 cannot beat Toy009 for any finite positive `u` in the separable final-significance model.

When rescue is possible, the direct detector threshold is

`u_req=[sqrt(delta)(1+z^-1/2)-(v z)^-1/2]^-2`.

### RESOURCE-063

For independent positive interval boxes in `(u,v,z,delta)`, exact lower/upper architecture-rate ratios follow from monotonicity in `u,v,delta` and the sign-controlled `z` dependence from Iteration 105. Apply NG-030 to the resulting nonoverlap certificate. Correlated physical uncertainties require the actual joint set.

Regression: synthetic common-coordinate campaign matrices give `alpha=.55`, `beta=1.40`, while direct schedule optimization gives `u~=0.617284516` inside the certified envelope.

## Iteration 107 — recertification-constrained scheduling

### RESOURCE-064

Represent physical minimum reference/calibration quotas with the constrained campaign polytope

`X={x>=0, 1^T x=1, A x>=b}`.

Then

`R_D^rob=max_{x in X} min_u Phi(sum_k x_k J_k(u))`.

On a fixed identifiable affine-polytope branch the optimization remains convex.

### DESIGN-013

Mandatory schedule constraints modify the Iteration-103 equal-marginal rule through KKT shadow prices. A required recertification campaign can remain active even when its unconstrained marginal Fisher/sec is lower.

### NG-063

A scalar duty factor is valid only for genuinely information-free dead/reference time. If a timing/gain/geometry/additive reference also supplies nuisance Fisher, include it inside the joint Fisher schedule; otherwise information can be discarded or double-counted.

### NG-064

If Toy009 and Toy014 have different feasible schedule sets, the two-sided RESOURCE-062 ratio bound does not follow automatically. Set inclusion preserves only the corresponding one-sided bound; otherwise optimize both constrained schedules directly.

### RESOURCE-065 — finite periodic-reference staircase

For a pure-dead reference block,

`L=F_*/R_live`,

`n_ref=ceil(L/tau_live)`,

`T_wall=L+n_ref t_ref`.

The asymptotic live fraction `tau_live/(tau_live+t_ref)` is only the long-campaign limit.

Retained Toy014 timing-reference illustration from Iteration 075, if treated as pure dead time only:

- `0.889 s` block at `0.2812 h` cadence -> duty loss `~8.774e-4`;
- at `0.02812 h` cadence -> `~8.705e-3`.

These are transparent drift benchmarks, not apparatus forecasts.

Files added:

- `analysis/detector_ratio_certificate_iteration106.py`
- `docs/PAPER_III_DETECTOR_RATIO_CERTIFICATE_ITERATION106.md`
- `research_log/2026-08-30_iteration_106_detector_ratio_certificate.md`
- `recovery/RECOVERY_DELTA_ITERATION_106.md`
- `analysis/recertification_constrained_schedule_iteration107.py`
- `docs/PAPER_III_RECERTIFICATION_CONSTRAINED_SCHEDULE_ITERATION107.md`
- `research_log/2026-08-30_iteration_107_recertification_constrained_schedule.md`
- `recovery/RECOVERY_DELTA_ITERATION_107.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 yet.

Use source-specific timing/geometry/additive/gain recertification intervals and cadence bounds to construct a **threshold/interval certificate for the constrained detector ratio `u`**. Combine the resulting `u` bounds with robust `(v,z,delta)` through RESOURCE-063/NG-030 and compute which control/reference requirement carries the largest architecture-decision shadow price.

If the common apparatus still lacks absolute control Fisher matrices, keep those rates/cadences parameterized and derive break-even surfaces rather than fabricating a winner.

Toy015 becomes admissible only if the residual dominant marginal wall-clock cost or architecture-decision uncertainty is demonstrably source-dependent. Classical/stochastic/hybrid/full-QFT degeneracy and relativistic/gauge/conservation/causality/EFT/renormalization/measurability gates remain open unless explicitly closed elsewhere in the repository.
