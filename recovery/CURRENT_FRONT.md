# RQIR Current Front Pointer

**Updated:** 2026-08-31  
**Authoritative front:** through **Iteration 123**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, the latest recovery deltas, and `docs/READINESS_TRACKER.md` before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE and near scientific closure. Iterations 080–123 now connect theoretical discriminants to source metrology, detector/profile Fisher, transfer/control recertification, calibration span/backaction, robust wall clock and external apparatus requirements.
- **Candidate Gravity:** inactive future branch. `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md` is entry planning only; no concrete model has passed QG-001…QG-010.

## Readiness status — Iteration 123

Project-management estimates, not statistical quantities:

- **Paper III scientific-content readiness:** **95%**.
- **Paper III submission readiness:** **81%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **85%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

Every new iteration from 116 onward must record these readiness metrics in its research log and recovery delta. History: `docs/READINESS_TRACKER.md`.

## Mandatory inference backbone

Always use detector-level

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain exact hard constraints, centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-preparation calibration, coherence/reset/dead-time, transfer gain/phase and all consistency/degeneracy gates. NG-005, NG-006/007, NG-023, NG-025/026, NG-030 and later transfer/control/backaction gates remain active.

The old post-Toy010 task of translating abstract `C_a` and `gamma` into physical repetitions/shot noise/calibration time/coherence/source metrology/detector SNR is already closed by the Paper-III resource chain. Do not restart it.

## Mature architecture backbone

Correlated simultaneous two-band science:

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`.

Campaign profile:

`Phi([[a,b^T],[b,N]])=a-b^T N^-1 b`.

Optimized campaign rate:

`R_*=max_x Phi(sum_k x_k J_k)`, `T_min=Z^2/R_*`.

Independent detector/source final-significance closure:

`T_min=F_*[1/sqrt(R_D)+1/sqrt(R_A)]^2`.

For Toy014/Toy009:

`u=R_D14/R_D09`, `v=R_A14/R_A09`, `z=R_A09/R_D09`, `delta=(1-d14)/(1-d09)`

and

`Q14/Q09=delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

NG-030: do not retain an architecture decision when certified uncertainty intervals overlap the decision boundary.

## Transfer/control front — Iterations 112–115

Matrix complex-gain/phase recertification:

`(t_ref F_ref)^-1 + tau Q/2 <= S`.

Likelihood-derived transfer retention after profiling non-transfer nuisances:

`J_bar=[[F0,b^T],[b,G]]`,

`F_beta(C)=F0-b^T(G+C)^-1 b`,

with target retention `F_beta>=qF0` iff

`G+C >= b b^T/[(1-q)F0]`.

NG-069: scalar-beta retention defines an admissible covariance set, not generally one unique full `Sigma_*`.

For the two-band gain/tilt quotient, common fractional gain is beta-aligned and differential gain is spectral-tilt aligned. Free per-band gains imply exact `F_beta=0` (NG-071).

Phase-profiled common-gain calibration Fisher:

`C_com=4 det(C_g)/(C22+C44-2C24)`.

Separate science/common-gain calibration:

`F_beta=F_s C_com/(F_s+C_com)`,

`R_DT=1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

Full-complex common-gain rate (115): transform physical transfer coordinates `x=(g2,g4,phi2,phi4)` to common/differential gain coordinates and profile differential gain plus phase:

`R_c=k_cc-k_cnu K_nunu^-1 k_nuc` (RESOURCE-079).

Same hardware does not imply `R_c14/R_c09=1` (NG-072).

## Iterations 116–117 — reference accounting and rank

For required nuisance information `H_*>=0` and one joint reference Fisher-rate matrix `K_ref>0`:

`T_ref,*=lambda_max(K_ref^-1/2 H_* K_ref^-1/2)` (RESOURCE-082).

For multiple campaigns:

`min sum_k t_k` subject to `sum_k t_k K_k>=H_*`, `t_k>=0` (RESOURCE-083).

CAL-023: one physical record receives one wall-clock charge. NG-073: marginal scalar rates cannot replace a correlated joint Fisher matrix.

A four-real same-state setting obeys `rank(K_b)<=4`. Repeating an unchanged setting cannot enlarge the score span (NG-074).

Finite quota feasibility requires

`range(H_*) subseteq range(K_tot)`

or `null(K_tot) subseteq null(H_*)` (RESOURCE-085).

With `m` distinct four-real settings and required rank `r_req`, necessarily

`m>=ceil(r_req/4)` (RESOURCE-086).

DESIGN-018: add settings that increase the missing score span / smallest singular value before increasing SNR in already-covered directions.

## Iteration 118 — exact Toy009/Toy014 calibration span

After hard constraints, the current source-calibration nuisance space is exactly 22-dimensional.

For both Toy009 and Toy014:

- 14 mean rows have rank `14`;
- each of seven same-time dual-probe mean layers adds rank `2`;
- eight centered-covariance rows add eight complementary rank-one directions;
- total mean+covariance rank is exactly `22`.

RESOURCE-087: the current calibration family spans the full hard-constrained 22D source-nuisance space.

NG-075: no current mean layer is exactly redundant.

NG-076: mean-only calibration cannot replace centered covariance through repetition/SNR.

RESOURCE-088: replacing the eight-dimensional covariance complement with four-real settings requires at least two distinct settings even dimensionally, and only if their orientations cover the complement.

Full normalized calibration conditioning:

- Toy009 `s_min~=0.0021266791`, condition `~409.93`;
- Toy014 `s_min~=0.0015010579`, condition `~650.58`.

## Iteration 119 — all-eight covariance endpoint graph

The eight indispensable covariance rows form an eight-edge graph with spectral radius squared `rho^2=6`.

In the declared affine whitened cross-covariance-only Gaussian output model, one all-eight trajectory has per-edge Fisher ceiling `<1/6` (NG-077), so

`N_all8 > 6 gamma_cov`.

Exhaustive enumeration of all 4140 edge partitions gives exact optimum

`min sum_k rho(G_k)^2=4`,

attained by four endpoint-disjoint two-edge matchings (RESOURCE-089), hence

`N_cov,partition > 4 gamma_cov`.

NG-078: endpoint-disjoint does not imply source-measurement compatibility; quantum noncommutation/backaction from Iteration 041 remains active.

## Iteration 120 — calibration-cover bracket

With weakest mean-layer Fisher `xi_mean^2`,

`M=7 gamma_mean/xi_mean^2`,

`C4=4 gamma_cov`, `C8=8 gamma_cov`.

RESOURCE-090 normalized branches:

`N_lower=max(M,C4)`

`N_match=M+C4`

`N_strong=M+C8`.

At the historical `xi_mean=3` regression, covariance dominates both Toy009 and Toy014. Toy014/Toy009 normalized calibration-burden ratios are approximately `4.60693`, `4.04082`, `4.25830` on the lower/matching/conservative branches.

DESIGN-019: characterize covariance throughput/backaction before reopening Toy015.

## Iteration 121 — physical detector-rate bracket

Science plus common-gain transfer:

`T_DT=F_*[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

Seven mean layers:

`T_m=gamma_m sum_j 1/R_m,j`.

Four matching covariance blocks and eight separate rows:

`T_C,match=gamma_c sum_b 1/R_C,b`,

`T_C,sep=gamma_c sum_k 1/r_C,k`.

RESOURCE-091:

`T_D^L=max(T_DT,T_m,T_C,match)`

`T_D^M=T_DT+T_m+T_C,match`

`T_D^U=T_DT+T_m+T_C,sep`.

RESOURCE-092 converts detector-time intervals directly to

`u in [L09/U14,U09/L14]`.

NG-079: if `1` lies in the certified `u` interval, detector-side architecture choice remains unresolved. RESOURCE-093: common scaling of all detector Fisher rates changes wall time but not the `u` interval.

## Iteration 122 — external apparatus evidence boundary

The literature audit confirms experimental precedent for the individual apparatus ingredients:

- multimode PSD/cross-spectrum acquisition;
- measured transfer-function force calibration;
- finite-integration directional force sensing;
- gain/phase feedback control with reduced cross-talk;
- exact simultaneous fundamental/second-harmonic mechanical operation.

EXPERIMENT-001: Song et al., Nature Communications 17, 8852 (2026) demonstrates simultaneous `17.8 kHz` fundamental and `35.6 kHz` second harmonic in one measurement. Exact `f:2f` mechanical operation is therefore an experimentally demonstrated platform class.

NG-080: do not splice sensitivity/cross-spectrum/harmonic-mode numbers from different apparatuses into one RQIR forecast.

RESOURCE-094 defines the minimum compatible public dataset for a numerical detector certificate: one apparatus/mapped state must provide simultaneous complex two-band transfer, full PSD/cross-PSD, common-gain reference data, seven mean-layer rates, covariance-complement rates/backaction model, geometry/additive SI controls, source metrology and timing/duty/drift.

No audited publication supplies that complete vector; the parametric certificate is therefore the correct public-data boundary.

## Iteration 123 — claim / novelty discipline

Generic ingredients are prior art and must be cited, not claimed as RQIR inventions:

- Fisher Schur complement nuisance profiling;
- Fisher/optimal experimental design and allocation;
- gravity-mediated-entanglement measurement/decoherence resource estimates;
- classical-channel/postquantum gravity decoherence/diffusion tests;
- cross-spectral force sensing and exact-harmonic platform precedent.

NG-081: RQIR novelty, if retained after final priority search, must be claimed at the **integration level**.

Candidate novelty classes:

1. ordered model-agnostic gravity-interface reconstruction hierarchy with finite discriminants/no-go boundaries;
2. finite nullspace source design linked to detector nuisance identifiability;
3. source-calibration + detector-profile + transfer/control + wall-clock chain;
4. final-significance architecture certificate `(u,v,z,delta)` inside the RQIR pipeline;
5. likelihood-derived transfer recertification plus non-double-counted calibration-span/backaction propagation.

CAL-024: keep theorem, deterministic regression, experimental precedent, parametric specification, open gate and candidate-novelty claim classes separate.

## Current Paper-III blockers

Scientific blockers for a **numerical apparatus forecast**:

- physical same-apparatus `R_s`, `R_c`, seven `R_m,j`, and covariance matching/separate rate matrices;
- physical overlap Jacobian if transfer and source-calibration records are to share wall time;
- covariance matching backaction feasibility;
- geometry and additive SI transduction/reference/drift rates;
- final robust numerical `u` and then full `(u,v,z,delta)` NG-030 comparison.

These are not blockers to writing Paper III as a **resource/specification/certificate paper**, provided they remain explicit parametric/open gates.

Submission blockers:

- manuscript synthesis;
- figures/tables;
- final priority/novelty search;
- unified notation and references;
- final reproducibility packaging.

## Immediate next gate — Paper III

Do **not** start Toy015 unless a demonstrably source-dependent bottleneck reappears. Do not fabricate a numerical apparatus forecast by mixing literature platforms.

Build a manuscript-ready Paper-III skeleton with, for every section:

1. one central claim;
2. exact supporting equations/results;
3. a figure/table target;
4. literature comparator/citation target;
5. explicit limitation/open gate.

Use that skeleton to expose the last scientific link(s) before full prose drafting. Further numerical detector closure becomes admissible when a RESOURCE-094-compatible same-apparatus dataset is available.

## Candidate Gravity boundary

The repository is increasingly ready to **test** a concrete model, but no model is active. A future candidate must supply one dynamics and derive the RQIR observables from it, then pass QG-001…QG-010 and comparison against semiclassical, stochastic, classical-channel/postquantum and perturbative-QG alternatives. Standard weak-field coupling, Lindblad structure or decoherence by themselves are not novelty.
