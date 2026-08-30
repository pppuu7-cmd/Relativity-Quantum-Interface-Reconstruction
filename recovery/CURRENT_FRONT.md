# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 110**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–109 translate abstract preparation/calibration Fisher requirements into physical detector, transfer, source, control, characterization and wall-clock resources, including robust final-significance scheduling, common-normalization matrix certificates and recertification Fisher-rate envelopes.
- **Iteration 110:** recovery/provenance consolidation only; no new scientific claim. Prior RQIR chats were reconciled against repository source-of-truth and the missing future Candidate Gravity entry checklist was migrated.

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

**NUM-006:** historical `A=25`, `C=225` gives `F_final=22.5` or `4.74341649 sigma`; `C=225` is 90% retention of a raw detector 5-sigma benchmark, not a final 5-sigma certificate.

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

**RESOURCE-062:** if uniformly over common campaigns and apparatus uncertainty

`alpha J_09,k <= J_14,k <= beta J_09,k`

and both architectures share the same feasible campaign set, then

`alpha <= u <= beta`.

Use generalized eigenvalues for positive-definite reference matrices and audit singular supports explicitly.

**NG-061:** science-only SNR, gamma, calibration-cost or marginal transfer-error ratios do not by themselves certify `u`; nuisance orientation/support and schedule set matter.

**NG-062:** detector no-rescue condition

`delta v (1+sqrt(z))^2 <= 1`.

When rescue is possible,

`u_req=[sqrt(delta)(1+z^-1/2)-(v z)^-1/2]^-2`.

**RESOURCE-063:** interval-safe architecture-rate bounds follow from the certified joint/interval set for `(u,v,z,delta)`; apply NG-030.

## Iteration 107 — recertification-constrained scheduling

**RESOURCE-064:** represent mandatory physical quotas with

`X={x>=0, 1^T x=1, A x>=b}`,

and use

`R_D^rob=max_{x in X} min_u Phi(sum_k x_k J_k(u))`.

**DESIGN-013:** active schedule constraints enter KKT conditions as shadow prices.

**NG-063:** scalar duty is valid only for genuinely information-free reference/dead time; reference campaigns carrying nuisance Fisher belong inside the joint schedule.

**NG-064:** architecture-specific feasible schedule sets can invalidate a two-sided matrix-ratio certificate; optimize both constrained schedules when set inclusion is absent.

**RESOURCE-065:** pure-dead periodic references obey

`L=F_*/R_live`, `n_ref=ceil(L/tau_live)`, `T_wall=L+n_ref t_ref`.

## Iteration 108 — exact timing-reference overhead convention

**NUM-007:** for overhead/live ratio `r=T_ref/T_cad`,

`m_wall=1+r`, `d_wall=r/(1+r)`, `eta_live=1/(1+r)`.

Retained centered timing targets:

- Toy009 D2 `sigma_t~=9.19001 us`;
- Toy014 `sigma_t~=3.97715 us`.

Under the transparent common jitter/Brownian benchmark, Toy014 has about `24.91x` larger timing-reference overhead than Toy009, but the timing-only detector-rate correction remains sub-percent over the stored `D_tau=100–1000 us^2/h` slice.

**RESOURCE-066:** for pure-dead timing references,

`u_wall=u_live (1+r09)/(1+r14)`.

## Iteration 109 — control recertification Fisher envelope

For a scalar physical control coordinate with allowed standard deviation `sigma_*`, irreducible floor `sigma_f`, Brownian drift convention `Var=D t/2`, and reference Fisher rate `R_ref`, define

`S=sigma_*^2-sigma_f^2>0`.

**RESOURCE-067 — optimal reference/drift split:**

`sigma_ref^2=S/2`,

`t_ref^*=2/(R_ref S)`,

`tau_live^*=S/D`,

`r_min=2D/(R_ref S^2)`.

**RESOURCE-068 — reference-rate threshold:**

`R_ref >= 2D/[r_max (sigma_*^2-sigma_f^2)^2]`.

**NG-065:** a tolerance alone is not a control-time budget; physical drift/floor and reference Fisher rate are required.

For the physical timing coordinate, equal drift/equal target overhead/equal Fisher normalization gives

`R_ref,14/R_ref,09=(sigma_t,09/sigma_t,14)^4 ~= 28.5086209`.

This is a required reference-Fisher-rate ratio under the same model, not a claim of `28.5x` wall-clock cost.

**NG-066:** normalized additive mean/covariance tolerances are not cross-source SI controls; common output/force transduction, offset drift spectrum and same-apparatus reference likelihood are still required.

Control-cut status after Iteration 109:

- timing: parameterized/partial in a common physical coordinate;
- geometry: physical transduction/drift/reference Fisher open;
- additive mean/covariance: physical transduction/drift/reference Fisher open;
- complex gain/phase: injected-transfer Fisher exists, but same-state stability/recertification process remains open.

**DESIGN-014:** rank controls by architecture-decision shadow price once physical schedules exist, not by raw tolerance alone.

## Iteration 110 — cross-chat recovery audit

Prior RQIR discussion history was reconciled against repository source-of-truth.

Verified already present and therefore not duplicated:

- RQIR-NUM-001 and revocation of false early `6.3x/4.6x` heterogeneous-calibration gains;
- Iteration-032 fully force-native D2 rank/null/covariance-complementarity results;
- source QFI in both physical amplitude `a` and fractional amplitude `alpha` coordinates;
- the Paper I/II/III and later Candidate Gravity publication architecture.

Coordinate reconciliation:

`a=0.08 alpha`,

`F_Q^(alpha)=0.08^2 F_Q^(a)`.

Repository values `F_Q^(a)~=13.270686` and `F_Q^(alpha)~=0.0849324` are consistent. An ideal full-QFI `C_alpha=9` target is about `105.97` accepted-copy QFI units; do not substitute this ceiling for realistic energy-population/Ramsey copy budgets.

**RQIR-RECOVERY-001:** project provenance is a hard recovery constraint. RTK/DSIR results do not enter RQIR unless independently rederived in RQIR.

Newly migrated planning document:

`docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`

with future QG-001…QG-010 gates. Candidate Gravity remains inactive; this document only preserves previously discussed entry criteria.

Files:

- `analysis/control_recertification_fisher_envelope_iteration109.py`
- `docs/PAPER_III_CONTROL_RECERTIFICATION_FISHER_ENVELOPE_ITERATION109.md`
- `research_log/2026-08-30_iteration_109_control_recertification_fisher_envelope.md`
- `recovery/RECOVERY_DELTA_ITERATION_109.md`
- `docs/RQIR_CROSS_CHAT_RECOVERY_AUDIT_ITERATION110.md`
- `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`
- `research_log/2026-08-30_iteration_110_cross_chat_recovery_audit.md`
- `recovery/RECOVERY_DELTA_ITERATION_110.md`

## Immediate next gate — Paper III only

Do **not** start Toy015 yet and do not open Candidate Gravity as active science yet.

Construct a **parameterized control-threshold surface** for the constrained detector ratio

`u=R_D,14/R_D,09`

using measurable `(R_ref,D,sigma_floor)` for timing, geometry, additive mean/covariance and complex gain/phase. Convert each control into RESOURCE-064 schedule quotas with RESOURCE-067/068, then combine certified `u` bounds with robust `(v,z,delta)` through RESOURCE-063/NG-030.

Where common-apparatus SI Fisher matrices are unavailable, keep rates/shadow prices symbolic or interval-bounded rather than fabricating an apparatus winner.

Toy015 becomes admissible only if the residual dominant marginal wall-clock cost or architecture-decision uncertainty is demonstrably source-dependent. Classical/stochastic/hybrid/full-QFT degeneracy and relativistic/gauge/conservation/causality/EFT/renormalization/measurability gates remain open unless explicitly closed elsewhere in the repository.
