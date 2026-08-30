# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 108**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–108 translate abstract preparation/calibration Fisher requirements into physical detector, transfer, source, control, characterization and wall-clock resources, including robust final-significance scheduling, common-normalization matrix certificates and exact periodic recertification accounting.

## Mandatory inference backbone

Use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time and all consistency/degeneracy gates. NG-005, NG-006/007, NG-023, NG-025/026 and NG-030 remain active.

## Mature resource backbone

- simultaneous two-band science:
  `R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`;
- seven physical calibration blocks:
  `R_cal,j=lambda_min(F_j)`;
- source Ramsey shots:
  `N_acc=C/F_copy`, `N_try=C/(p_E F_copy)`;
- same-state temporal `f,2f` covariance/injection protocol: Iteration 101;
- joint transfer-gain profiling: Iteration 102;
- full complex campaign optimization: Iteration 103.

## Iteration 103 — full complex campaign simplex

For campaign Fisher-rate matrices `J_k` and times `t_k`,

`J=sum_k t_k J_k=[[a,b^T],[b,N]]`,

`F_beta=a-b^T N^-1 b`.

**RESOURCE-057:** with campaign fractions `x_k`,

`R_*=max_{x>=0,sum x=1} F_beta(sum_k x_k J_k)`,

`T_min=Z^2/R_*`.

**RESOURCE-058:** with `q=N^-1b`, `w=(1,-q)`,

`dF_beta/dt_k=w^T J_k w`.

At an unconstrained interior optimum, active campaigns equalize marginal profiled Fisher/sec.

**NG-058:** transfer phase can be omitted only after Fisher-metric, not merely Euclidean, orthogonality is demonstrated.

## Iteration 104 — robust final-significance source closure

For local source-amplitude profiling,

`F_final=A C/(A+C)`.

**NUM-006:** historical `A=25`, `C=225` gives `F_final=22.5` or `4.74341649 sigma`; `C=225` is therefore 90% retention of a raw detector 5-sigma benchmark, not a final 5-sigma certificate.

For final `Z=5` at fixed 90% retention use `A=27.77777778`, `C=250`.

**RESOURCE-060:** with detector rate `R_s` and independent source-amplitude rate `R_a`,

`1/F=1/(R_s T_s)+1/(R_a T_a)`,

`T_s/T_a=sqrt(R_a/R_s)`,

`T_min=F_*[1/sqrt(R_s)+1/sqrt(R_a)]^2`.

**NG-059:** fixed 90% retention is minimum-time optimal only for `R_a/R_s=81`.

**RESOURCE-059:** robust scheduling uses

`R_rob^*=max_x min_u F_beta(sum_k x_k J_k(u))`.

## Iteration 105 — final-significance architecture crossover

Where detector/source separation is valid, define

`R_final,i = 1/[1/sqrt(R_D,i)+1/sqrt(R_A,i)]^2`.

With information-free duty `d_i`, `Q_i=(1-d_i)R_final,i`.

Define

`u=R_D,14/R_D,09`, `v=R_A,14/R_A,09`, `z=R_A,09/R_D,09`, `delta=(1-d_14)/(1-d_09)`.

**RESOURCE-061:**

`Q_14/Q_09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

**DESIGN-012:** source domination favors Toy014 iff `v>u`, favors Toy009 iff `v<u`.

**NG-060:** Ramsey/source-rate advantage alone is not an architecture certificate.

## Iteration 106 — robust detector-side ratio certificate

For

`Phi(J)=a-b^T N^-1 b=min_q (1,-q)^T J (1,-q)`,

Loewner monotonicity and positive homogeneity give:

### RESOURCE-062

If uniformly over common campaigns and apparatus uncertainty

`alpha J_09,k <= J_14,k <= beta J_09,k`

and both architectures share the same feasible campaign set, then

`alpha <= u <= beta`.

For positive-definite reference matrices, use generalized eigenvalues of `J_09^-1/2 J_14 J_09^-1/2`. Audit singular supports explicitly.

### NG-061

Science-only SNR, gamma, calibration-cost or marginal transfer-error ratios do not by themselves certify `u`; nuisance orientation/support and the schedule set matter.

### NG-062

The detector no-rescue condition is

`delta v (1+sqrt(z))^2 <= 1`.

If true, Toy014 cannot beat Toy009 for any finite positive detector ratio `u` in the separable final-significance model.

When rescue is possible,

`u_req=[sqrt(delta)(1+z^-1/2)-(v z)^-1/2]^-2`.

### RESOURCE-063

For independent positive interval boxes in `(u,v,z,delta)`, exact lower/upper architecture-rate ratios follow from monotonicity in `u,v,delta` and sign-controlled `z` dependence. Apply NG-030. Correlated physical uncertainty requires the actual joint set.

Regression: synthetic common-coordinate matrices give `alpha=.55`, `beta=1.40`; direct optimized `u~=0.617284516` lies inside the certificate.

## Iteration 107 — recertification-constrained scheduling

### RESOURCE-064

Represent mandatory physical quotas with

`X={x>=0, 1^T x=1, A x>=b}`,

and use

`R_D^rob=max_{x in X} min_u Phi(sum_k x_k J_k(u))`.

The fixed-branch problem remains convex.

### DESIGN-013

Active schedule constraints enter KKT conditions as shadow prices; mandatory reference campaigns need not satisfy the unconstrained equal-marginal rule.

### NG-063

A scalar duty factor is valid only for genuinely information-free reference/dead time. If a reference also constrains timing/gain/geometry/additive nuisance parameters, put it inside the Fisher schedule or risk discarding/double-counting information.

### NG-064

If Toy009 and Toy014 have different feasible schedule sets, the two-sided RESOURCE-062 ratio bound does not follow automatically. Set inclusion preserves only the corresponding one-sided bound; otherwise optimize both constrained schedules directly.

### RESOURCE-065

For a pure-dead periodic reference block,

`L=F_*/R_live`, `n_ref=ceil(L/tau_live)`, `T_wall=L+n_ref t_ref`.

Smooth duty is only the long-campaign limit; finite campaigns have staircase overhead.

## Iteration 108 — exact timing-reference overhead convention

Re-audit of Iteration 076 against RESOURCE-065 found a resource-convention correction.

### NUM-007

When `T_cad` is the allowed informative/live interval and `T_ref` is a pure-dead reference block, define

`r=T_ref/T_cad`.

Then `r` is overhead/live ratio, not total-wall duty:

`m_wall=1+r`,

`d_wall=r/(1+r)`,

`eta_live=1/(1+r)`.

The older `1/(1-r)` multiplier is only first-order accurate for small `r`.

Retained centered timing targets:

- Toy009 D2 `sigma_t~=9.19001 us`;
- Toy014 `sigma_t~=3.97715 us`.

Under the common transparent jitter/Brownian-drift benchmark, Toy014 retains about `24.91x` larger timing-reference overhead than Toy009.

Exact total-wall reference fractions:

- `D_tau=100 us^2/h`: Toy014 `8.7751553e-4`, Toy009 `3.5261872e-5`;
- `D_tau=1000 us^2/h`: Toy014 `8.7063953e-3`, Toy009 `3.5250685e-4`.

The qualitative small/moderate-drift conclusion of Iteration 076 is unchanged.

The old formal `r=1` point is exactly 50% total-wall reference time, not 100%. Exact Toy014 10% total-wall timing-reference duty occurs at `D_tau~=1.26509e4 us^2/h` in the declared zero-floor benchmark.

### RESOURCE-066

For pure-dead timing references,

`u_wall=u_live (1+r09)/(1+r14)`.

Thus a final detector threshold requires

`u_live > u_req (1+r14)/(1+r09)`.

Do not use this scalar correction if reference blocks carry nuisance Fisher; use RESOURCE-064.

Files added in Iterations 106–108:

- `analysis/detector_ratio_certificate_iteration106.py`
- `docs/PAPER_III_DETECTOR_RATIO_CERTIFICATE_ITERATION106.md`
- `research_log/2026-08-30_iteration_106_detector_ratio_certificate.md`
- `recovery/RECOVERY_DELTA_ITERATION_106.md`
- `analysis/recertification_constrained_schedule_iteration107.py`
- `docs/PAPER_III_RECERTIFICATION_CONSTRAINED_SCHEDULE_ITERATION107.md`
- `research_log/2026-08-30_iteration_107_recertification_constrained_schedule.md`
- `recovery/RECOVERY_DELTA_ITERATION_107.md`
- `analysis/timing_overhead_convention_iteration108.py`
- `docs/PAPER_III_TIMING_OVERHEAD_CONVENTION_ITERATION108.md`
- `research_log/2026-08-30_iteration_108_timing_overhead_convention.md`
- `recovery/RECOVERY_DELTA_ITERATION_108.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 yet.

Build a Toy009/Toy014 **control-cut status matrix**. Timing is now parameterized source-specifically. Geometry, additive and gain tolerances exist in toy coordinates but still lack a common-apparatus transduction, drift spectrum and reference Fisher-rate model. For each open control cut, derive the minimum same-apparatus measurement/Fisher object required to promote it into RESOURCE-064.

Then construct constrained robust bounds on `u`, combine them with `(v,z,delta)` through RESOURCE-063/NG-030, and rank remaining control/reference measurements by architecture-decision shadow price.

Do not invent SI control rates. Toy015 becomes admissible only if the residual dominant marginal wall-clock cost or architecture-decision uncertainty is demonstrably source-dependent. Classical/stochastic/hybrid/full-QFT degeneracy and relativistic/gauge/conservation/causality/EFT/renormalization/measurability gates remain open unless explicitly closed elsewhere in the repository.
