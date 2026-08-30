# RQIR Current Front Pointer

**Updated:** 2026-08-31  
**Authoritative front:** through **Iteration 114**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, and the latest recovery deltas before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–114 translate abstract preparation/calibration Fisher requirements into detector/source/control/transfer Fisher rates, recertification, robust final significance and wall-clock architecture certificates.
- **Candidate Gravity:** inactive future branch. `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md` is entry planning only; no concrete model has passed QG-001…QG-010.

## Mandatory inference backbone

Use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time, transfer gain/phase and all consistency/degeneracy gates. NG-005, NG-006/007, NG-023, NG-025/026, NG-030 and later control/transfer gates remain active.

## Mature Paper-III architecture objects

- simultaneous correlated two-band science:
  `R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`;
- physical calibration blocks:
  `R_cal,j=lambda_min(F_j)`;
- source shots:
  `N_acc=C/F_copy`, `N_try=C/(p_E F_copy)`;
- complex campaign allocation:
  `R_*=max_x Phi(sum_k x_k J_k)`, `Phi([[a,b^T],[b,N]])=a-b^T N^-1 b`;
- robust scheduling:
  `max_x min_u Phi(sum_k x_k J_k(u))`;
- independent detector/source final-significance closure:
  `T_min=F_*[1/sqrt(R_D)+1/sqrt(R_A)]^2`;
- Toy014/Toy009 architecture variables:
  `u=R_D,14/R_D,09`, `v=R_A,14/R_A,09`, `z=R_A,09/R_D,09`, `delta=(1-d14)/(1-d09)`;
- final ratio:
  `Q14/Q09=delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`;
- constrained physical schedules use RESOURCE-064 and NG-030 interval/joint uncertainty.

## Iterations 108–111 — control recertification

For one scalar pure-dead control with usable variance budget

`S=sigma_*^2-sigma_f^2`, drift convention `Var=D tau/2`, and reference Fisher rate `R_ref`,

**RESOURCE-067:**

`sigma_ref^2=S/2`,

`t_ref*=2/(R_ref S)`,

`tau*=S/D`,

`r_min=2D/(R_ref S^2)`.

For independent non-overlapping pure-dead controls,

`H_i=sum_j h_ij`, `eta_i=1/(1+H_i)`,

`u_wall=u_live(1+H09)/(1+H14)`.

RESOURCE-070/071 turn unresolved control channels into architecture-decision Fisher thresholds and robust interval corners. Timing is already physical/parameterized; geometry/additive SI transduction and stability remain open.

## Iteration 112 — matrix complex-gain/phase recertification

For multivariate complex-transfer control, define

`S=Sigma_*-Sigma_f > 0`, reference Fisher-rate matrix `F_ref`, and drift covariance rate `Q` with `Cov_drift=tau Q/2`.

Require

`(t_ref F_ref)^-1 + tau Q/2 <= S`.

Whiten:

`A=S^-1/2 F_ref^-1 S^-1/2`,

`B=S^-1/2 Q S^-1/2`.

At fixed cadence,

`t_ref,min(tau)=lambda_max[(I-tau B/2)^-1/2 A (I-tau B/2)^-1/2]`.

**RESOURCE-072:**

`r_mat*=min_tau t_ref,min(tau)/tau`.

**NG-068:** correlated/shared gain/phase controls cannot generally be replaced by independent scalar overheads. A deterministic same-spectrum regression changes `r*` from `~51.005` to `~200.000` by changing only Fisher/drift orientation (`~3.92x`), not marginal spectra.

**RESOURCE-073:** under uniform `F_ref->kappa F_ref`, `r_mat*->r_mat*/kappa`.

## Iteration 113 — likelihood-derived transfer budget

After profiling all non-transfer nuisances, write the conditional beta/transfer Fisher block

`J_bar=[[F0,b^T],[b,G]]`.

With independent transfer-reference Fisher `C`,

`F_beta(C)=F0-b^T(G+C)^-1 b`.

### RESOURCE-074 — exact transfer-retention LMI

For retained fraction `q`,

`F_beta(C)>=qF0`

iff

`G+C >= b b^T/[(1-q)F0]`.

### NG-069 — no unique full covariance budget

For `C=Sigma^-1`, scalar-beta retention defines an admissible covariance **set**, not generally one unique full SPD `Sigma_*`.

### RESOURCE-075 — canonical science-coupled transfer mode

Define

`B=b^T G^-1 b`, `ell0=B/F0`, `q_free=1-ell0`.

For `q>q_free`,

`kappa*=ell0/(1-q)-1`,

`a=b/sqrt(B)`,

`C*=kappa* a a^T`,

and exactly `F_beta(C*)=qF0`.

Equivalent variance certificate:

`a^T Sigma a <= 1/kappa*`.

### RESOURCE-076 — likelihood-derived transfer recertification

For the science-coupled coordinate `eta=a^T g`,

`R_eta=1/[a^T F_ref^-1 a]`,

`D_eta=a^T Q a`,

`sigma_f,eta^2=a^T Sigma_f a`,

`S_eta=1/kappa*-sigma_f,eta^2`.

If `S_eta>0`,

`t_ref*=2/(R_eta S_eta)`, `tau*=S_eta/D_eta`, `r_eta*=2D_eta/(R_eta S_eta^2)`.

If `S_eta<=0`, the stability floor alone violates the target.

Scalar NG-005/NUM-006 is recovered: raw `F0=25`, `q=.9` requires `C=225` and yields final `F=22.5`; final `F=25` at the same retention requires raw `F0=27.7777778`, `C=250`.

**NG-070:** deterministic hard transfer-error bounds and Gaussian Fisher-prior covariance budgets are different uncertainty semantics.

## Iteration 114 — two-band gain/tilt quotient

For current two-real-band science amplitudes `s=(s2,s4)`:

- beta score: `(s2,s4)`;
- spectral-tilt score: `(-s2,s4)`;
- fractional band-gain scores: `(s2,0)` and `(0,s4)`.

With `g2=c-d`, `g4=c+d`, the common-gain score is exactly beta-aligned and the differential-gain score is exactly tilt-aligned.

### NG-071

Free per-band gains imply exact `F_beta=0` regardless of science exposure/source harmonic balance/detector covariance.

### RESOURCE-077 — common-gain quotient Fisher

For gain-reference Fisher `C_g`, transform to `(c,d)` and profile differential gain:

`C_com=C_cc-C_cd^2/C_dd`.

For SPD per-band matrix

`C_g=[[C22,C24],[C24,C44]]`,

`C_com=4 det(C_g)/(C22+C44-2C24)`.

For independent band references,

`C_com=4 C2 C4/(C2+C4)`.

**DESIGN-017:** at fixed independent `C2+C4`, balance the two band-reference Fisher values unless the apparatus can measure common gain directly.

After spectral-tilt profiling, let `F_s` be transfer-fixed science Fisher. Then exactly

`F_beta=F_s C_com/(F_s+C_com)`.

At retained fraction `q`,

`C_com >= q/(1-q) F_s`.

Thus Toy009 and Toy014 share the same algebraic common-gain retention coefficient; their transfer burden differs through physical accumulation rates, not through a different formal `kappa`.

### RESOURCE-078 — detector+common-transfer effective rate

For separate science/reference rates,

`R_DT=1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

For Toy014/Toy009 define

`s=R_s14/R_s09`, `c=R_c14/R_c09`, `z_c=R_c09/R_s09`.

Then

`u_DT=[(1+z_c^-1/2)/(s^-1/2+(c z_c)^-1/2)]^2`.

The Iteration-074 value `s=0.28301465746` is only an equal-ASD/shared-kernel regression slice, not a physical apparatus ratio. With illustrative `c=1`, a slow common transfer reference drives `u_DT` toward `1`, while a fast reference recovers the science-only ratio.

Files added:

- `analysis/transfer_likelihood_covariance_budget_iteration113.py`
- `docs/PAPER_III_LIKELIHOOD_TRANSFER_BUDGET_ITERATION113.md`
- `research_log/2026-08-31_iteration_113_likelihood_transfer_budget.md`
- `recovery/RECOVERY_DELTA_ITERATION_113.md`
- `analysis/two_band_gain_tilt_quotient_iteration114.py`
- `docs/PAPER_III_TWO_BAND_GAIN_TILT_QUOTIENT_ITERATION114.md`
- `research_log/2026-08-31_iteration_114_two_band_gain_tilt_quotient.md`
- `recovery/RECOVERY_DELTA_ITERATION_114.md`

## Current open Paper-III controls

- timing: physical/parameterized;
- amplitude transfer: likelihood-derived two-band common-gain quotient **algebraically closed**; physical same-state `R_c` interval/stability still open;
- complex phase transfer: full matrix recertification exists, physical phase Jacobian/drift/floor remains open;
- geometry: common SI transduction + drift + reference Fisher open;
- additive mean/covariance: common SI transduction + drift + reference Fisher open;
- robust numerical `u=R_D,14/R_D,09` under one declared apparatus remains open.

## Immediate next gate — Paper III only

Do **not** start Toy015 and do not activate Candidate Gravity as a claimed model yet.

Use the same-state dual-tone reference likelihood of Iterations 101–103 to certify a physical/common-coordinate interval for the common-gain quotient rate `R_c`. If one source-independent detector reference is justified, evaluate the `c=1` slice; otherwise keep `c=R_c14/R_c09` interval-valued.

Then propagate `R_DT` through the seven-layer calibration/control scheduler and update the robust detector-side ratio `u`, followed by RESOURCE-061/063/NG-030 with source-metrology `(v,z)` and duty `delta`.

Keep complex phase drift, geometry and additive SI rates symbolic unless the same-apparatus physical likelihood supplies them. Toy015 becomes admissible only if the residual dominant architecture uncertainty or marginal wall-clock cost is demonstrably source-dependent.
