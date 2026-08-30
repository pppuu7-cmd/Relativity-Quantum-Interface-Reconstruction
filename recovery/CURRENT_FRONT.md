# RQIR Current Front Pointer

**Updated:** 2026-08-31  
**Authoritative front:** through **Iteration 124**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, `docs/READINESS_TRACKER.md`, and the latest recovery delta before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE; manuscript-facing closure phase.
- **Candidate Gravity:** inactive future branch; no concrete model has passed QG-001…QG-010.

## Readiness — Iteration 124

- Paper III scientific-content readiness: **96%**.
- Paper III submission readiness: **86%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **85%**.
- Concrete Candidate-Gravity model itself: **~10%**.

These are project-management estimates, not statistical confidence measures.

## Mandatory inference backbone

Always use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, independent source-preparation calibration, coherence/reset/dead-time, transfer gain/phase, backaction and all consistency/degeneracy gates.

**Do not restart the old post-Toy010 resource-conversion task.** The translation of abstract `C_a` and `gamma` into accepted copies/repetitions, shot/Fisher rates, detector SNR, calibration time, source reset/preparation and coherence-aware wall clock is already closed by the Paper-III resource chain.

## Mature Paper-III resource backbone

Source preparation:

`C_prep=[r/(1-r)]Z^2`,

`N_acc=C_prep/I_alpha,copy`,

`R_alpha=p I_alpha,copy/tau_copy`,

`T_src=C_prep/R_alpha`.

Calibration:

`I_j=4 int |d htilde_j/du_j|^2/S_out,j df`,

`R_cal,j=p_j I_j/tau_j`,

with full matrix Fisher / `lambda_min(F_j)` for correlated simultaneous rows.

Science:

`R_beta=4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`

for the retained simultaneous two-band reduction after the declared nuisance profile.

Campaign scheduling:

`Phi([[a,b^T],[b,N]])=a-b^T N^-1 b`,

`R_*=max_x Phi(sum_k x_k J_k)`,

with robust max-min extension under uncertainty.

Final independent detector/source significance:

`T_min=F_*[1/sqrt(R_D)+1/sqrt(R_A)]^2`.

Architecture variables:

`u=R_D14/R_D09`, `v=R_A14/R_A09`, `z=R_A09/R_D09`, `delta=(1-d14)/(1-d09)`.

Final ratio:

`Q14/Q09=delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

NG-030 remains active: overlapping certified architecture intervals mean unresolved, not a nominal winner.

## Current mature front — Iterations 115–124

### 115 — full-complex common-gain reference

In common/differential gain coordinates, after profiling differential gain and phases,

`R_c=k_cc-k_cnu K_nunu^-1 k_nuc`.

NG-072: same hardware does not imply identical transfer Fisher rate across Toy009/Toy014.

### 116–117 — joint-reference accounting and rank/span

For one joint reference requirement `H_*` and rate matrix `K_ref`,

`T_ref,*=lambda_max(K_ref^-1/2 H_* K_ref^-1/2)`.

For several campaigns:

`min sum_k t_k` subject to `sum_k t_k K_k>=H_*`.

One physical record receives one wall-clock charge. Finite quota feasibility requires

`range(H_*) subseteq range(K_tot)`.

More repetitions of an unchanged setting do not create missing Fisher directions.

### 118 — actual Toy009/Toy014 nuisance span

After hard constraints the retained source-nuisance space is dimension 22. Seven same-time dual-probe mean layers supply rank 14; centered covariance rows add the missing rank 8. There is no free exact redundancy that permits dropping these nuisance directions.

### 119 — covariance matching cover

The full eight-row covariance endpoint graph is congestion-limited in a one-shot cross-covariance-only Gaussian-output realization. Exhaustive partitioning yields four endpoint-disjoint matching blocks as the optimum within that declared class. Source backaction compatibility remains mandatory.

### 120–121 — calibration-cover and detector-rate brackets

Strong-measurement, matching-block and optimistic shared-output calibration branches were converted into explicit Fisher-rate/time envelopes. Science, transfer, mean and covariance uncertainties propagate directly into a certified interval for

`u=R_D14/R_D09`

without invented detector ASD values.

### 122 — external apparatus audit

Published experiments establish feasibility of several ingredients: calibrated force transfer, multimode/cross-spectral readout, gain/phase control and exact simultaneous fundamental/second-harmonic operation. No audited publication supplies the complete same-state RQIR closure vector required for a numerical `u`.

NG-080: do not splice numbers from different apparatuses into one forecast.

### 123 — claim/novelty audit

Generic Fisher Schur complements, Fisher/OED allocation, gravity-test shot/decoherence estimates, cross-spectral sensing and classical-gravity decoherence are prior ingredients. Candidate RQIR novelty must be claimed, if at all after final priority review, at the integrated reconstruction/resource-architecture level.

NG-081 and CAL-024 enforce claim-class discipline.

### 124 — manuscript-ready Paper III skeleton

Paper III now has an eight-section claim/equation/evidence/comparator/limitation structure. The end-to-end inferential chain is connected from source/interface discrimination through final significance.

The remaining unresolved object is **not another abstract Fisher parameter**. It is the physical same-apparatus closure vector needed for a numerical detector architecture verdict.

NG-082: manuscript/theorem closure is not numerical apparatus closure.

DESIGN-020: characterize the minimum same-state closure vector needed to instantiate `(u,v,z,delta)` rather than optimizing isolated headline sensitivities.

Files:

- `analysis/paper3_manuscript_skeleton_iteration124.py`
- `docs/PAPER_III_MANUSCRIPT_SKELETON_ITERATION124.md`
- `research_log/2026-08-31_iteration_124_manuscript_skeleton.md`
- `recovery/RECOVERY_DELTA_ITERATION_124.md`

## Remaining physical closure vector

A numerical Toy009/Toy014 detector winner still requires, in one compatible apparatus/accounting:

- same-state two-band science transduction and PSD/cross-PSD;
- full complex transfer-reference Fisher/covariance;
- seven calibration-layer Fisher-rate matrices;
- covariance/backaction compatibility if shared blocks are credited;
- geometry/additive SI reference Fisher rates;
- physical drift/floor/recertification inputs;
- independent source-metrology rate and duty.

Until this vector exists, do not state a measured Toy009/Toy014 winner and do not invent apparatus numbers.

## Immediate next gate — Paper III

Perform the final manuscript-facing **notation/dependency/reproducibility audit**:

1. canonical symbol table;
2. claim-to-file provenance map;
3. stale/duplicate resource/no-go/iteration numbering audit;
4. minimum reproducibility command list for manuscript figures/tables;
5. mark contradictory historical notation as superseded rather than silently deleting it.

After this audit, prose drafting is scientifically admissible. Candidate Gravity remains separate and inactive as a claimed model.
