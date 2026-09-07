# RQIR Article Series Architecture

**Date fixed:** 2026-08-29  
**Publication architecture revised:** 2026-09-08  
**Current Candidate-Gravity status:** use `candidate_gravity/recovery/CURRENT_QG_FRONT.md` as the live authority; `MODEL_READINESS=24%` at the time of this publication-architecture revision.

## Purpose

RQIR results should be published as a linked series rather than compressed into one oversized article. The series preserves the logical progression from operational reconstruction to statistical identifiability, physical resource closure, an explicit comparison of existing gravity/quantum-gravity frameworks, and only then—if the comparison leaves a genuine robust gap—to a new Candidate Gravity model.

The publication logic is now formally five-stage:

`Paper I -> Paper II -> Paper III -> Paper IV comparator decision gate -> Paper V only if NEW_REQUIRED`.

Paper V is therefore conditional rather than presumed in advance.

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

**Scientific status:** **CLOSED at Iteration 078 — 100% for the frozen scientific scope.** See `docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md`. Remaining work is manuscript construction, literature/novelty audit, figures, references and independent reproduction; do not reopen the scientific toy search unless that audit exposes an actual logical gap.

**Manuscript status:** active. Canonical working draft begins at `docs/PAPER_I_MANUSCRIPT_V0_1.md`.

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
- RQIR-STAT-001 reference-likelihood regression certificate (Iteration 079);
- concise distinction between statistical/nuisance and structural/map non-identifiability from the later Iteration-217 audit.

The paper should end with the question of converting Fisher requirements into physical shots, time, SNR, PSD, coherence, and source-preparation resources.

**Scientific status:** **CLOSED at Iteration 079 — 100% for the frozen scientific scope.** See `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md`. Physical rate/wall-clock conversion is Paper III, not an unresolved Paper-II theorem. Remaining work is manuscript integration, literature/novelty audit, figures/tables and independent reruns.

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

Canonical closure authority: `docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md`.

**NG-084:** scientific closure is not apparatus closure. Paper III does not claim a measured same-apparatus runtime, an experimental RQIR signal or an experimentally established Toy009/Toy014 winner.

A numerical apparatus application remains a conditional extension requiring a compatible same-apparatus two-band transfer/PSD/cross-PSD likelihood, seven physical calibration rates, geometry/additive drift/reference rates, source-metrology rate/duty and any measurement/backaction likelihood needed for shared covariance credit.

**P3-CLOSE-001:** absent contradiction, failed regression or materially relevant new literature, do not expand Paper III merely to continue the research loop.

### Submission status

The last frozen submission-readiness estimate was **97%** after Iteration 128. Remaining tasks are manuscript production rather than scientific-scope research:

- generate/canonicalize figures and tables from the Iteration-126 reproducibility manifest;
- draft/polish prose from the Iteration-124 skeleton;
- refresh literature/priority search immediately before submission;
- perform an independent clean/reviewer-style rerun;
- apply journal-specific references and formatting.

## Paper IV — Existing gravity and quantum-gravity frameworks through the RQIR funnel

Working title:

**Relativity–Quantum Interface Reconstruction IV: Existing Gravity and Quantum-Gravity Frameworks Through a Common Operational Funnel**

Central question: after imposing the same RQIR consistency, comparator, source-completion, identifiability and measurability discipline, do existing frameworks already contain a viable realization of the required interface, or is a genuinely new model direction required?

Paper IV is a comparator/decision paper. It must not be written as a pre-decided argument for a new theory.

### Core material already accumulating in the repository

- semiclassical mean gravity as an early baseline/control;
- stochastic gravity and influence-functional/Einstein–Langevin response as stronger comparators;
- classical-channel, measurement-feedback, hybrid and postquantum classical-gravity realizations;
- Gaussian/Källén–Lehmann spin-2 controls where applicable;
- standard perturbative quantum-GR EFT as the permanent C5 reference;
- explicit distinction between on-shell amplitude information and the off-shell/source-completed retarded RQIR map;
- nonlocal/form-factor constructions when a concrete finite realization is specified;
- asymptotic-safety and other programme-level approaches only after a concrete effective realization is instantiated;
- later concrete realizations of string/LQG/emergent/etc. only when they define the state space, dynamics and observable map required by the RQIR contract;
- negative-result matrix recording `PASS_SCOPED`, `FAIL`, `BLOCKED` and exact comparator identities without converting failure-to-promote into theory falsification;
- robust comparator-subtracted residual as the decisive promotion object.

Canonical current scaffolds include:

- `docs/CANDIDATE_GRAVITY_ARTICLE_FUNNEL_SECTION_ITERATION137.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION150.md`;
- the subsequent `candidate_gravity/` comparator and source-completion audits.

### Paper-IV decision gate

Paper IV must end in one of four explicitly allowed outcomes:

1. `EXISTING_SUFFICIENT` — a sufficiently specified existing framework survives the relevant RQIR gates and supplies the required interface direction;
2. `ADAPT_EXISTING` — the gap can be closed by a controlled extension of an existing framework without introducing a genuinely new parent theory;
3. `HYBRID_REQUIRED` — the surviving requirements point to a controlled hybridization of established ingredients;
4. `NEW_REQUIRED` — after the fixed comparator quotient closes, a concrete robust residual remains that is not supplied by the admissible existing classes.

Only `NEW_REQUIRED` authorizes Paper V as a genuinely new Candidate Gravity theory paper. A `BLOCKED` comparator is not evidence for `NEW_REQUIRED`.

### Current scientific state

The comparator foundation is nearly closed in the live Candidate-Gravity readiness rubric, but the decisive `robust unique residual` remains unclosed at the time of this revision. Therefore Paper IV is scientifically active and its conclusion is intentionally not predetermined.

## Paper V — Conditional RQIR-derived Candidate Gravity

Working title, only if authorized by Paper IV:

**Relativity–Quantum Interface Reconstruction V: An RQIR-Derived Candidate Gravity Model**

Paper V exists only if the Paper-IV decision gate returns `NEW_REQUIRED` (or an equivalently strong repository-certified result). It is not justified merely because no current model has yet been promoted.

### Entry conditions

Before a new promotable ansatz is created, the repository must contain a concrete nonzero robust comparator-subtracted residual and the relevant upstream observable/source-completion definition must be frozen.

A future construction starts as `ANSATZ-*`, not as an accepted `QGxxx` model.

### Candidate task

- specify a physical state/Hilbert/algebraic space and relational observables;
- construct one parent matter–gravity dynamics rather than tuning response kernels independently;
- derive `J`, `N`, `chi^R` and higher ordered/CTP correlators from that same dynamics;
- recover controlled Newtonian/GR, ordinary-QM/semiclassical and flat-QFT limits where applicable;
- impose conservation/Bianchi/Ward consistency, causality, positivity/unitarity/complete positivity as appropriate, EFT/renormalization consistency and spectral constraints;
- produce a model-specific discriminator not identical to an admitted comparator;
- propagate that discriminator through Papers I–III: finite discriminant -> nuisance-profiled identifiability -> physical resource/measurability closure;
- preserve all failed model versions and negative gates.

### Readiness interpretation

The live `MODEL_READINESS` score measures progress toward a fully promoted Candidate Gravity, not a countdown that must reach 100% before theory construction begins. In the current rubric, the comparator foundation contributes the first block; robust residual, parent dynamics, consistency, identifiability and resource closure are subsequent blocks. Thus **100% is the target state of a fully developed/promoted candidate, not the start point for constructing one.**

## Publication discipline

1. Do not move material into a later paper merely because it is newer; place it according to the logical question it answers.
2. Negative results and numerical corrections remain publishable methodological content and must not be hidden.
3. Do not label a CTP/channel architecture, comparator residual or Candidate Gravity model as novel without a dedicated literature/priority audit.
4. RQIR I–III reconstruct and certify operational constraints, identifiability and resources; Paper IV compares existing realizations; Paper V is conditional theory construction. These are different epistemic levels.
5. Failure of an RQIR promotion gate is not automatically falsification of an entire gravity framework.
6. A broad research programme is not assigned a binary pass/fail status until a concrete realization satisfying the RQIR model contract is specified.
7. `BLOCKED` is not zero and is not evidence that a new theory is required.
8. Paper-III 100% scientific readiness must not be represented as apparatus-specific experimental closure.
9. Papers I–III must not wait for Candidate Gravity completion.
10. The repository remains source of truth. Reopen a scientifically closed paper only for a documented contradiction, failed regression or materially relevant new requirement.

## Post-Candidate-development manuscript strengthening policy

A controlled post-closure audit performed on 2026-09-03 found that Papers I–III do **not** need to wait for Candidate Gravity completion. The detailed integration policy is frozen in:

`docs/PAPERS_I_III_POST_CANDIDATE_STRENGTHENING_PLAN.md`.

Key directives:

- Paper I: optionally add a concise Iteration-217 on-shell/off-shell structural-identifiability bridge;
- Paper II: add the Iteration-217 distinction between statistical/nuisance and structural/map non-identifiability as the highest-value post-closure strengthening;
- Paper III: preserve the scientific freeze and allow only a short downstream-model Outlook unless a claim-changing contradiction appears;
- model-specific C5/Vilkovisky and later comparator work stays in Paper IV;
- a new model-specific construction belongs in Paper V only after the Paper-IV decision gate authorizes it;
- after one controlled integration audit, freeze Papers I–III rather than continuously back-propagating every later Candidate-Gravity iteration.

## Frozen publication decisions

`PAPERS_I_II_III_DO_NOT_WAIT_FOR_CANDIDATE_GRAVITY_COMPLETION`.

`PAPER_IV_IS_THE_EXISTING_FRAMEWORK_COMPARATOR_AND_DECISION_PAPER`.

`PAPER_V_IS_CONDITIONAL_ON_NEW_REQUIRED`.

`MODEL_READINESS_100_PERCENT_IS_A_FULL_CANDIDATE_TARGET_NOT_A_THEORY_START_THRESHOLD`.