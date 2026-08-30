# RQIR Current Front Pointer

**Updated:** 2026-08-31  
**Authoritative front:** through **Iteration 117**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, the latest recovery deltas, and `docs/READINESS_TRACKER.md` before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–117 translate abstract preparation/calibration Fisher requirements into detector/source/control/transfer rates, robust final-significance scheduling, recertification, joint-reference accounting and reference-span identifiability.
- **Candidate Gravity:** inactive future branch. `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md` is entry planning only; no concrete model has passed QG-001…QG-010.

## Readiness status — Iteration 117

Project-management estimates, not statistical quantities:

- **Paper III scientific-content readiness:** **90%**.
- **Paper III submission readiness:** **71%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **84%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

Every new iteration from 116 onward must record these readiness metrics in its research log and recovery delta. History: `docs/READINESS_TRACKER.md`.

## Mandatory inference backbone

Always use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time, transfer gain/phase and all consistency/degeneracy gates. NG-005, NG-006/007, NG-023, NG-025/026, NG-030 and later transfer/control gates remain active.

The old post-Toy010 task of translating abstract `C_a` and `gamma` into physical repetitions/shot noise/calibration time/coherence/source metrology/detector SNR is already closed by the Paper-III resource chain. Do not restart it.

## Mature rate / architecture backbone

- correlated simultaneous two-band science:
  `R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`;
- physical calibration layer:
  `R_cal,j=lambda_min(F_j)`;
- source attempts:
  `N_acc=C/F_copy`, `N_try=C/(p_E F_copy)`;
- campaign profile:
  `Phi([[a,b^T],[b,N]])=a-b^T N^-1 b`;
- optimized campaign rate:
  `R_*=max_x Phi(sum_k x_k J_k)`, `T_min=Z^2/R_*`;
- robust scheduling:
  `max_x min_u Phi(sum_k x_k J_k(u))`;
- independent detector/source final-significance closure:
  `T_min=F_*[1/sqrt(R_D)+1/sqrt(R_A)]^2`;
- architecture variables:
  `u=R_D14/R_D09`, `v=R_A14/R_A09`, `z=R_A09/R_D09`, `delta=(1-d14)/(1-d09)`;
- final Toy014/Toy009 ratio:
  `Q14/Q09=delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

## Transfer/control front — Iterations 112–115

Matrix complex-gain/phase recertification (112):

`(t_ref F_ref)^-1 + tau Q/2 <= S`.

Likelihood-derived transfer retention (113): after profiling non-transfer nuisances,

`J_bar=[[F0,b^T],[b,G]]`,

`F_beta(C)=F0-b^T(G+C)^-1 b`,

and retention `F_beta>=qF0` is equivalent to

`G+C >= b b^T/[(1-q)F0]`.

NG-069: scalar-beta retention defines an admissible covariance set, not generally one unique full `Sigma_*`.

Two-band gain/tilt quotient (114): common fractional gain is beta-aligned, differential gain is spectral-tilt aligned, and free per-band gains imply exact `F_beta=0` (NG-071). For a phase-profiled gain Fisher,

`C_com=4 det(C_g)/(C22+C44-2C24)`.

Separate science/common-gain calibration:

`F_beta=F_s C_com/(F_s+C_com)`,

`R_DT=1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

Full-complex common-gain rate (115): with physical transfer coordinates `x=(g2,g4,phi2,phi4)`, transform to `y=(c,d,phi2,phi4)` and profile `nu=(d,phi2,phi4)`:

`R_c=k_cc-k_cnu K_nunu^-1 k_nuc` (**RESOURCE-079**).

Same hardware does not imply `R_c14/R_c09=1` (NG-072). Relative Loewner envelopes propagate to a robust common-gain-rate ratio interval (RESOURCE-080), then into the science+transfer quotient (RESOURCE-081).

## Iteration 116 — joint reference quota / no double counting

Let `H_*>=0` be the mandatory nuisance-information requirement in common coordinates and let one physical joint reference campaign provide Fisher-rate matrix `K_ref>0`.

### RESOURCE-082

`T_ref,* = lambda_max(K_ref^-1/2 H_* K_ref^-1/2)`.

For diagonal independent simultaneous quotas this reduces to

`T_joint=max_i h_i/r_i`,

whereas non-overlapping dedicated campaigns require

`T_sep=sum_i h_i/r_i`,

so `1<=T_sep/T_joint<=n` (RESOURCE-084).

### RESOURCE-083

For several distinct campaigns:

`min sum_k t_k` subject to `sum_k t_k K_k>=H_*`, `t_k>=0`.

This is an SDP. A physical acquisition that jointly estimates transfer and calibration appears once with all cross terms retained.

### NG-073 / CAL-023

Marginal scalar rates cannot replace a correlated shared Fisher block. One physical record receives one wall-clock charge. If it also carries science information, insert it once in RESOURCE-057/064 rather than adding the same time again as calibration.

## Iteration 117 — reference-span rank gate

One accepted same-state dual-tone setting has four real outputs. For local Jacobian `J_b`,

`K_b=J_b^T W_b J_b`,

hence

`rank(K_b)<=4`.

### NG-074

Repeating an unchanged setting multiplies Fisher but does not enlarge its score span. Missing reference directions cannot be repaired by more SNR/exposure.

### RESOURCE-085

Finite quota feasibility requires

`range(H_*) subseteq range(K_tot)`,

or equivalently

`null(K_tot) subseteq null(H_*)`.

### RESOURCE-086

With `m` distinct four-real settings and `r_req=rank(H_*)`, necessarily

`m>=ceil(r_req/4)`.

This is only a dimensional lower bound; settings can still be redundant.

### DESIGN-018

Use the stacked whitened Jacobian on the required subspace and require positive `sigma_min`. Add settings that increase missing score span before increasing SNR in already-covered directions.

Files:

- `analysis/joint_reference_quota_iteration116.py`
- `docs/PAPER_III_JOINT_REFERENCE_QUOTA_ITERATION116.md`
- `recovery/RECOVERY_DELTA_ITERATION_116.md`
- `analysis/reference_span_rank_iteration117.py`
- `docs/PAPER_III_REFERENCE_SPAN_RANK_ITERATION117.md`
- `recovery/RECOVERY_DELTA_ITERATION_117.md`
- `docs/READINESS_TRACKER.md`

## Current open Paper-III controls

- timing: physical/parameterized;
- common transfer amplitude: full-complex reduction closed; physical same-apparatus rate matrices/intervals remain open;
- complex phase drift: algebraic matrix recertification exists; physical drift/floor remains open;
- geometry: common SI transduction + drift + reference Fisher open;
- additive mean/covariance: common SI transduction + drift + reference Fisher open;
- actual rank/span overlap between same-state transfer and the seven calibration settings is open;
- minimal nonredundant reference-setting cover is open;
- final non-double-counted robust numerical `u=R_D14/R_D09` under one declared apparatus remains open.

## Immediate next gate — Paper III only

Do **not** start Toy015 and do not activate Candidate Gravity as a claimed model yet.

Reconstruct the actual required nuisance subspace for Toy009/Toy014 after hard constraints and the spectral-tilt quotient. Map the existing seven calibration settings and same-state dual-tone transfer setting into that common basis, compute their rank/span overlap, remove redundant settings, and form the minimum admissible setting cover satisfying RESOURCE-085.

Then feed the surviving physical/reference Fisher matrices into RESOURCE-083/057 without double counting to obtain the first full detector-side robust `u` interval.

Keep geometry/additive SI rates and physical drift symbolic unless the repository or an external same-apparatus likelihood genuinely supplies them. Toy015 becomes admissible only if the remaining dominant architecture uncertainty or marginal wall-clock cost is demonstrably source-dependent.
