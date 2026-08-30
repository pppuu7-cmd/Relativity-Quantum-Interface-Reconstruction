# RQIR Article Series Architecture

**Date fixed:** 2026-08-29  
**Scientific status updated through:** **Iteration 128 (2026-08-31)**.

## Purpose

RQIR results should be published as a linked series rather than compressed into one oversized article. The series preserves the logical progression from operational reconstruction to statistical identifiability, physical resource closure, and only later to an explicit candidate gravity model.

## Paper I — Operational hierarchy and finite discriminants

Working title:

**Relativity–Quantum Interface Reconstruction I: Operational Hierarchy, Ordered Stress-Energy Information, and Finite Nullspace Discriminants**

Central question: what source information can a gravity–quantum interface transmit in principle?

Core material:

- operational inverse problem `P_data(o|s) -> [interface class]`;
- ordered source hierarchy `J=<T>`, symmetrized noise `N`, commutator/ordered response `D`, retarded response `chi^R`, and CTP parent functional;
- NP0–NP5 calibration hierarchy;
- Toy001–Toy010 as a logical sequence rather than disconnected examples;
- RQIR-NG-001 through NG-004;
- Toy009 detector-aware source design;
- Toy010 calibration/null-direction steering;
- RQIR-DESIGN-001 and RQIR-CAL-002;
- RQIR-THM-001 finite nullspace response-discriminant existence theorem (Iteration 078).

The paper should end by emphasizing that exact response separation is not yet experimental identifiability and use RQIR-NG-005 as the bridge to Paper II.

**Scientific status:** **CLOSED at Iteration 078** for this defined scope. See `docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md`. Remaining work is manuscript construction, literature/novelty audit, figures, references and independent reproduction; do not reopen the scientific toy search unless that audit exposes an actual logical gap.

## Paper II — Statistical identifiability and nuisance geometry

Working title:

**Relativity–Quantum Interface Reconstruction II: Statistical Identifiability, Source Calibration, and Detector-Level Degeneracy**

Central question: when does a genuine source/interface difference remain inferable after source, calibration, apparatus, and detector nuisances are profiled?

Primary object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab = ||(I-P_J) s_tilde||^2`.

Core material:

- exact-null versus statistical-identifiability geometry;
- soft nulls and calibration monotonicity;
- RQIR-NG-005 source-amplitude self-calibration obstruction;
- independent source-preparation metrology and RQIR-CAL-003;
- RQIR-NUM-001 hard-constraint correction and withdrawal of penalty/pseudoinverse overclaims;
- low-rank systematics, RQIR-NG-006 and RQIR-CAL-007;
- timing/gain nonlinear audit;
- D1/D2 detector-level nuisance profiling;
- RQIR-STAT-001 reference-likelihood regression certificate (Iteration 079).

The paper should end with the question of converting Fisher requirements into physical shots, time, SNR, PSD, coherence, and source-preparation resources.

**Scientific status:** **CLOSED at Iteration 079** for this defined scope. See `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md`. Physical rate/wall-clock conversion is Paper III, not an unresolved Paper-II theorem. Remaining work is manuscript integration, literature/novelty audit, figures/tables and independent reruns.

## Paper III — Physical resource budgets and experiment architecture

Working title:

**Relativity–Quantum Interface Reconstruction III: Physical Resource Budgets and Experiment Design for Gravity–Quantum Discriminants**

Central question: which statistically identifiable discriminants remain meaningful after source preparation, detector/transfer/calibration nuisances, coherence/reset/backaction and robust wall-clock resources are treated consistently?

### Frozen scientific claim

Paper III supplies an end-to-end **resource/design/certificate** formulation specialized to the RQIR interface-discrimination problem:

`interface discriminant -> exact source/calibration constraints -> detector nuisance profile -> source metrology -> transfer/cross-PSD calibration -> calibration span/backaction/no-double-counting -> physical Fisher rates -> robust wall clock -> final architecture certificate`.

### Core material

- source-preparation QFI/Fisher, accepted copies, reset/visibility/coherence and independent source-metrology rate;
- physical D1/D2 science Fisher rates from detector transfer and PSD/cross-PSD;
- NG-005 physical source-amplitude calibration and final-significance bookkeeping;
- same-state temporal `f,2f` covariance and dual-tone transfer calibration;
- full complex gain/phase nuisance profiling and common-gain quotient;
- physical calibration Fisher-rate matrices, seven-layer calibration, shots/SNR/coherence/wall-clock conversion;
- control/reference recertification including scalar and matrix drift/floor/Fisher envelopes;
- joint campaign scheduling and no-double-counting of shared physical records;
- rank/span feasibility: more SNR cannot create missing score directions;
- Toy009/Toy014 retained nuisance span `22 = 14 mean + 8 covariance complement`;
- covariance endpoint graph / matching-cover resource bounds with explicit backaction guard;
- robust detector-side interval `u=R_D14/R_D09` without fabricated apparatus ASD values;
- independent detector/source final-significance closure and the architecture variables `(u,v,z,delta)`;
- external component-feasibility audit and NG-080 prohibition on splicing incompatible apparatuses;
- claim/novelty boundary, canonical notation, reproducibility manifest and manuscript skeleton;
- Iteration-128 formal scientific-closure certificate.

### Canonical final-significance convention

Use

`F_*=Z_final^2`,

`F_final=A_raw C_src/(A_raw+C_src)`.

At fixed retention `r`,

`A_raw=F_*/r`, `C_src=F_*/(1-r)`.

For final `Z_final=5`, `r=.90`, the consistent pair is

`A_raw=27.7777777778`, `C_src=250`.

Historical `(25,225)` remains only a raw-5-sigma / 90%-retention regression and yields final `Z=4.74341649` (NUM-006/NUM-008).

### Final architecture certificate

Define

`u=R_D14/R_D09`,

`v=R_A14/R_A09`,

`z=R_A09/R_D09`,

`delta=(1-d14)/(1-d09)`.

Then

`Q14/Q09=delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

NG-030 requires interval-safe separation for a robust architecture winner.

### Scientific status

**CLOSED at Iteration 128 — 100% scientific-content readiness for the frozen resource/design/certificate scope.**

Canonical closure authority:

`docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md`.

**NG-084:** scientific closure is not apparatus closure. Paper III does not claim a measured same-apparatus runtime, an experimental RQIR signal or an experimentally established Toy009/Toy014 winner.

A numerical apparatus application remains a conditional extension requiring a compatible same-apparatus two-band transfer/PSD/cross-PSD likelihood, seven physical calibration rates, geometry/additive drift/reference rates, source-metrology rate/duty and any measurement/backaction likelihood needed for shared covariance credit.

**P3-CLOSE-001:** absent contradiction, failed regression or materially relevant new literature, do not expand Paper III merely to continue the research loop. New source searches such as Toy015 belong to later work unless a manuscript review exposes a gap required by the frozen claim.

### Submission status

Current submission readiness after Iteration 128: **97%**. Remaining tasks are manuscript production rather than scientific-scope research:

- generate/canonicalize figures and tables from the Iteration-126 reproducibility manifest;
- draft/polish prose from the Iteration-124 skeleton;
- refresh literature/priority search immediately before submission;
- perform an independent clean/reviewer-style rerun;
- apply journal-specific references and formatting.

## Paper IV — only after the reconstruction papers mature

Working title:

**A Minimal Causal Gravity–Quantum Interface Consistent with RQIR Constraints**

This remains deliberately separated from Papers I–III. The repository is now approximately **90% ready to start** a concrete Candidate-Gravity branch because the RQIR I→II→III test pipeline is scientifically closed, but the **concrete Candidate-Gravity model itself remains ~10%** and no model has passed QG-001…QG-010.

Entry authority:

`docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`.

Candidate task:

- specify a physical state/Hilbert/algebraic space and observables;
- construct a concrete matter–gravity dynamical interaction rather than inserting response kernels independently;
- impose diffeomorphism/relational consistency, conservation/Bianchi/Ward identities, causality, positivity/unitarity/CP as appropriate, controlled GR/Newtonian and flat-QFT limits, and EFT/renormalization consistency;
- derive `J`, `N`, `chi^R` and higher correlators from one model;
- propagate the candidate through the closed RQIR I–III discriminant/identifiability/resource pipeline;
- compare against semiclassical, stochastic, classical-channel/postquantum, hybrid and perturbative-QG alternatives before any new-physics claim.

## Publication discipline

1. Do not move material into a later paper merely because it is newer; place it according to the logical question it answers.
2. Negative results and numerical corrections remain publishable methodological content and must not be hidden.
3. Do not label a CTP/channel architecture itself as novel without a dedicated literature/novelty audit.
4. RQIR I–III reconstruct and certify constraints/resources; Paper IV proposes a concrete candidate. These are different epistemic levels.
5. Paper-III 100% scientific readiness must not be represented as apparatus-specific experimental closure.
6. The repository remains source of truth. Reopen a scientifically closed paper only for a documented contradiction, failed regression or materially relevant new requirement.
