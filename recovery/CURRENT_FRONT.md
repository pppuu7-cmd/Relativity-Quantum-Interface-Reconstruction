# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 111**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–111 translate abstract preparation/calibration Fisher requirements into physical detector, source, control, characterization and wall-clock resources.
- **Candidate Gravity:** inactive future branch. `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md` is entry planning only.

## Mandatory inference/resource backbone

Use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time, transfer gain/phase and all consistency/degeneracy gates. NG-005, NG-006/007, NG-023, NG-025/026 and NG-030 remain active.

Mature resource objects:

- simultaneous two-band science: `R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`;
- physical calibration blocks: `R_cal,j=lambda_min(F_j)`;
- source shots: `N_acc=C/F_copy`, `N_try=C/(p_E F_copy)`;
- same-state temporal `f,2f` protocol: Iteration 101;
- joint science/transfer profiling: Iteration 102;
- complex campaign allocation: Iteration 103;
- robust source+detector final significance: Iteration 104;
- architecture crossover `(u,v,z,delta)`: Iteration 105;
- detector matrix-ratio certificate: Iteration 106;
- recertification-constrained schedule: Iteration 107;
- exact pure-dead timing convention: Iteration 108;
- scalar control Fisher envelope: Iteration 109;
- cross-chat recovery consolidation: Iteration 110;
- multi-control architecture threshold surface: Iteration 111.

## Iterations 103–107 — campaign/final-significance architecture

For campaign Fisher-rate matrices `J_k` and times `t_k`,

`J=sum_k t_k J_k=[[a,b^T],[b,N]]`,

`Phi(J)=F_beta=a-b^T N^-1 b`.

**RESOURCE-057:** `R_*=max_x Phi(sum_k x_k J_k)`, `T_min=Z^2/R_*`.

**RESOURCE-058:** with `q=N^-1b`, `w=(1,-q)`, marginal campaign value is `w^T J_k w`.

**RESOURCE-059:** robust scheduling uses `max_x min_u Phi(sum_k x_k J_k(u))`.

**RESOURCE-060:** independent detector/source rates combine as

`T_min=F_*[1/sqrt(R_s)+1/sqrt(R_a)]^2`.

For architectures Toy014/Toy009 define

`u=R_D,14/R_D,09`, `v=R_A,14/R_A,09`, `z=R_A,09/R_D,09`, `delta=(1-d14)/(1-d09)`.

**RESOURCE-061:**

`Q14/Q09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

**NG-062:** detector no-rescue condition is `delta v (1+sqrt(z))^2 <= 1`; otherwise

`u_req=[sqrt(delta)(1+z^-1/2)-(v z)^-1/2]^-2`.

**RESOURCE-062/063:** common-coordinate Fisher matrices can bound `u` through Loewner/generalized-eigenvalue certificates and then propagate interval/joint uncertainty under NG-030.

**RESOURCE-064:** mandatory physical quotas use

`X={x>=0,1^T x=1,A x>=b}`,

`R_D^rob=max_{x in X} min_u Phi(sum_k x_k J_k(u))`.

**NG-063/064:** pure scalar duty is invalid for Fisher-carrying references; differing feasible schedule sets can invalidate a two-sided architecture ratio certificate.

## Iteration 108 — timing overhead correction

For pure-dead timing overhead/live ratio `r=T_ref/T_cad`,

`m_wall=1+r`, `d_wall=r/(1+r)`, `eta_live=1/(1+r)`.

Retained timing targets:

- Toy009 D2 `sigma_t~=9.19001 us`;
- Toy014 `sigma_t~=3.97715 us`.

Stored `D_tau=100–1000 us^2/h` timing-only corrections remain sub-percent despite Toy014's tighter tolerance.

**RESOURCE-066:** `u_wall=u_live(1+r09)/(1+r14)`.

## Iteration 109 — scalar recertification Fisher envelope

For allowed `sigma_*`, floor `sigma_f`, Brownian convention `Var=D t/2`, reference Fisher rate `R_ref`, define

`S=sigma_*^2-sigma_f^2>0`.

**RESOURCE-067:**

`sigma_ref^2=S/2`,

`t_ref*=2/(R_ref S)`,

`tau_live*=S/D`,

`r_min=2D/(R_ref S^2)`.

**RESOURCE-068:** for maximum overhead/live `r_max`,

`R_ref >= 2D/[r_max (sigma_*^2-sigma_f^2)^2]`.

**NG-065:** tolerance alone is not a control-time budget.

For physical timing with equal drift/overhead/Fisher normalization,

`R_ref,14/R_ref,09 ~= 28.5086209`.

This is a required Fisher-rate ratio under that model, not a wall-clock forecast.

**NG-066:** normalized additive tolerances are not cross-source SI controls without common transduction/drift/reference likelihood.

Open control status after Iteration 109:

- timing: physical/parameterized;
- geometry: SI transduction + drift + reference Fisher open;
- additive mean/covariance: SI transduction + drift + reference Fisher open;
- complex gain/phase: injected-transfer Fisher exists; temporal stability/recertification process open.

## Iteration 110 — recovery/provenance consolidation

Cross-chat recovery verified that major earlier RQIR numerical/scientific results are already present in the repository. Candidate Gravity entry gates QG-001…QG-010 were migrated as future planning only.

**RQIR-RECOVERY-001:** project provenance is a hard recovery constraint; RTK/DSIR results do not enter RQIR unless independently rederived in RQIR.

## Iteration 111 — parameterized multi-control threshold surface

For each genuinely pure-dead scalar control `j` in architecture `i`,

`S_ij=sigma_*ij^2-sigma_f,ij^2`,

`h_ij=2D_ij/[R_ref,ij S_ij^2]`.

### RESOURCE-069 — aggregate control load

For non-overlapping pure-dead references,

`H_i=sum_j h_ij`,

`eta_i=1/(1+H_i)`,

`boxed{u_wall=u_live(1+H09)/(1+H14)}`.

This is the exact multi-control extension of RESOURCE-066 within the declared scalar scope.

### RESOURCE-070 — decision-relevant Fisher threshold

For one unresolved Toy014 control `j`, define

`K_14,j=(u_live/u_req)(1+H09)-1-H14,-j`.

If `K<=0`, increasing that one reference Fisher rate cannot rescue Toy014. If `K>0`, require

`boxed{R_ref,14,j > 2D_14,j/[K_14,j (sigma_*14,j^2-sigma_f,14,j^2)^2]}`.

At fixed `R_ref,D,K`, the stability floor must satisfy

`boxed{sigma_f^2 <= sigma_*^2-sqrt[2D/(R_ref K)]}`.

**NG-067:** reference-rate improvement cannot repair an irreducible floor that leaves insufficient usable variance budget.

### RESOURCE-071 — robust independent-box certificate

For

`u_live in [uL,uU]`, `H09 in [H09L,H09U]`, `H14 in [H14L,H14U]`,

`u_wall,L=uL(1+H09L)/(1+H14U)`,

`u_wall,U=uU(1+H09U)/(1+H14L)`.

- robust Toy014 detector-side sufficiency if `u_wall,L>u_req`;
- full-box impossibility if `u_wall,U<=u_req`;
- otherwise characterization remains decision-relevant.

Correlated uncertainty still requires the physical joint set under NG-030.

**DESIGN-015:** characterize control channels whose physical uncertainty spans the architecture boundary first, then rank surviving channels by RESOURCE-064 shadow price.

Scope guard: `H=sum h_j` is exact only for genuinely pure-dead, non-overlapping references. Joint/Fisher-carrying references remain full RESOURCE-064 matrix-schedule problems.

Files added:

- `analysis/control_threshold_surface_iteration111.py`
- `docs/PAPER_III_CONTROL_THRESHOLD_SURFACE_ITERATION111.md`
- `research_log/2026-08-30_iteration_111_control_threshold_surface.md`
- `recovery/RECOVERY_DELTA_ITERATION_111.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 and do not activate Candidate Gravity yet.

Close at least one same-apparatus physical control channel and insert its certified `(R_ref,D,sigma_f)` interval into RESOURCE-071. The leading candidate is **complex gain/phase stability**, because injected-transfer Fisher already exists from Iterations 101–103 and only the time-domain drift/stability process remains missing.

If no defensible common-apparatus drift object can be derived without external hardware assumptions, keep that channel symbolic and instead derive the strongest apparatus-independent joint-control bound possible. Do not fabricate SI rates.

After one control closure, recompute the robust detector-ratio box and combine it with `(v,z,delta)` through RESOURCE-061/063/NG-030. Toy015 becomes admissible only if the residual dominant architecture uncertainty or marginal wall-clock cost is demonstrably source-dependent.
