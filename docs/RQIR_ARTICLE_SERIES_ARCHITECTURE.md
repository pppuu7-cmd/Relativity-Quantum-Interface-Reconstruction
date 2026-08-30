# RQIR Article Series Architecture

**Date fixed:** 2026-08-29  
**Status:** publication-planning note; scientific status updated through Iteration 080.

## Purpose

RQIR results should eventually be published as a linked series rather than compressed into one oversized article. The series must preserve the logical progression from operational reconstruction to statistical identifiability, physical resource closure, and only later to an explicit candidate gravity model.

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

**Scientific status:** CLOSED at Iteration 078 for this defined scope. See `docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md`. Remaining work is manuscript construction, literature/novelty audit, figures, references and independent reproduction; do not reopen the scientific toy search unless that audit exposes an actual logical gap.

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

**Scientific status:** CLOSED at Iteration 079 for this defined scope. See `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md`. Physical rate/wall-clock conversion is Paper III, not an unresolved Paper-II theorem. Remaining work is manuscript integration, literature/novelty audit, figures/tables and independent reruns.

## Paper III — Physical resource budgets and experiment architecture

Working title:

**Relativity–Quantum Interface Reconstruction III: Physical Resource Budgets and Experiment Design for Gravity–Quantum Discriminants**

Central question: which statistically identifiable discriminants remain feasible after a complete physical resource budget?

Core material:

- source-preparation QFI and `R_P`;
- detector SNR and native D1/D2 Fisher rates;
- shots, acceptance, dead time, coherence time and wall-clock duration;
- timing/reference TDEV/Allan/PSD and recertification duty;
- physical offset/transduction maps;
- D2 potential/force/relational calibration branches;
- nullspace rotation, finite-reference obstruction and observable-family consistency;
- covariance complementarity and row selection;
- branch-specific Pareto/resource phase diagrams;
- Iteration-077 minimal apparatus-rate certificate `(R_beta,x,y,d)`;
- Iteration-080 inverse apparatus specification envelope using `H_cal` and a declared wall-clock cap;
- final `F_beta|theta/T_wall` comparison under one apparatus model.

The conclusion should define a minimum experimental specification, not claim a ready experiment unless the apparatus-level gates have actually been closed.

**Scientific status:** ACTIVE after Iteration 080. The abstract Fisher parameters are now translated into rates, shot/source throughput, reset/coherence/control and inverse duration targets, but a repository-backed physical apparatus model with source-specific transfer functions, PSD/cross-PSD, `R_beta`, seven `R_cal,j`, `R_src`, duty and uncertainty intervals is still required.

## Paper IV — only after the reconstruction papers mature

Working title:

**A Minimal Causal Gravity–Quantum Interface Consistent with RQIR Constraints**

This is deliberately separated from Papers I–III. It should begin only when a concrete candidate dynamical model exists.

Candidate task:

- construct a minimal CTP/influence-functional or quantum-channel gravity interface;
- impose diffeomorphism/relational consistency, conservation/Bianchi/Ward identities, causality, positivity/unitarity/CP as appropriate, controlled GR/Newtonian and flat-QFT limits, and EFT/renormalization consistency;
- derive `J`, `N`, `chi^R` and higher correlators from one model rather than inserting them independently;
- propagate the candidate through the RQIR I–III likelihood/resource pipeline;
- compare against semiclassical, stochastic, classical-gravity+full-QFT, hybrid, and perturbative-QG alternatives before any new-physics claim.

## Publication discipline

1. Do not move material into a later paper merely because it is newer; place it according to the logical question it answers.
2. Negative results and numerical corrections remain publishable methodological content and must not be hidden.
3. Do not label a CTP/channel architecture itself as novel without a dedicated literature/novelty audit.
4. RQIR I–III reconstruct constraints; Paper IV proposes a candidate. These are different epistemic levels.
5. The repository remains source of truth. When article drafting starts, this architecture may be revised only if the scientific front genuinely changes.
