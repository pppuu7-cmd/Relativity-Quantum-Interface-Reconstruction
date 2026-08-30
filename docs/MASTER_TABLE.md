# RQIR Operational Master Table

**Version:** 3.1  
**Date:** 2026-08-31  
**Authoritative scientific front:** **Iteration 132**.

> This is the current operational compression. Detailed historical numerical tables remain in their canonical iteration documents, analysis scripts, research logs, recovery deltas and Git history. Later named corrections supersede interpretation without deleting provenance.

## Programme objective

RQIR reconstructs operationally distinguishable gravity–quantum interface structure without assuming a preferred quantum-gravity theory in advance.

Primary detector inference object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Exact rank/nullspace is not statistical identifiability. Physical comparisons include source preparation, calibration, transfer/noise, controls, backaction and wall-clock resources in a common parameter convention.

## Readiness / publication table

| Branch | Scientific status | Current readiness | Canonical authority |
|---|---|---:|---|
| Paper I — operational hierarchy / finite discriminants | CLOSED Iter. 078 | **100% scientific** | `docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md` |
| Paper II — statistical identifiability / nuisance geometry | CLOSED Iter. 079 | **100% scientific** | `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md` |
| Paper III — physical resources / experiment architecture | CLOSED Iter. 128 | **100% scientific; 97% submission** | `docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md` |
| Candidate Gravity repository infrastructure | CLOSED/READY Iter. 132 | **100% ready to start model** | `docs/CANDIDATE_GRAVITY_INFRASTRUCTURE_CLOSURE_ITERATION132.md` |
| Concrete Candidate Gravity model | not instantiated | **~10% bookkeeping only** | future `candidate_gravity/models/...` |

Readiness history: `docs/READINESS_TRACKER.md`.

## Canonical corrections retained

- **NUM-001:** exact constraints are eliminated analytically before Fisher profiling; penalty+pseudoinverse artifacts are not admissible.
- **NUM-002:** source-amplitude coordinate transformations carry the Fisher Jacobian.
- **CAL-013:** finite-noise covariance uses centered covariance derivatives unless raw second moments are explicitly measured.
- **NUM-006/008:** `A_raw=25, C_src=225` is a raw-5-sigma/90%-retention regression giving final `F=22.5`, not a final 5-sigma certificate.

Canonical final-significance convention:

`F_*=Z_final^2`,

`F_final=A_raw C_src/(A_raw+C_src)`.

At fixed retention `r`:

`A_raw=F_*/r`, `C_src=F_*/(1-r)`.

For final `Z=5`, `r=.90`: `A_raw=27.77777778`, `C_src=250`.

## Paper I closed backbone

Paper I establishes the operational ordered source hierarchy and finite discriminants, including the distinction among mean source information, centered noise, ordered/retarded response and higher source structure.

`RQIR-THM-001` supplies finite nullspace response-discriminant existence under the declared assumptions.

Authority: Iteration 078 closure.

## Paper II closed backbone

Paper II establishes detector-level nuisance profiling and source-calibration/statistical-identifiability discipline.

Primary object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Retain NG-005 source-amplitude obstruction, exposure/systematic no-go results, exact hard-constraint discipline and detector-likelihood coordinate invariance.

Authority: Iteration 079 closure.

## Paper III closed backbone

Paper III converts identifiable RQIR differences into physical resource/design certificates.

Mature components include:

- source-metrology Fisher rates, accepted-copy/reset/coherence accounting;
- simultaneous two-band science PSD/cross-PSD;
- complex transfer gain/phase profiling;
- calibration Fisher matrices and span/rank gates;
- backaction/no-double-counting constraints;
- control recertification and drift/reference Fisher;
- robust campaign scheduling;
- final source+detector significance;
- Toy009/Toy014 architecture interval certificate.

Final independent detector/source time:

`T_min=F_*[1/sqrt(R_D)+1/sqrt(R_A)]^2`.

Architecture variables:

`u=R_D14/R_D09`, `v=R_A14/R_A09`, `z=R_A09/R_D09`, `delta=(1-d14)/(1-d09)`.

Final ratio:

`Q14/Q09=delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

NG-030 remains mandatory: overlapping certified intervals mean unresolved.

Paper-III scientific closure does not imply an apparatus-specific measured runtime/winner (NG-084).

## Candidate Gravity infrastructure — CLOSED Iteration 132

Canonical workspace: `candidate_gravity/`.

Required infrastructure:

- `MODEL_SPEC_TEMPLATE.md`;
- `MODEL_TO_RQIR_CONTRACT.md`;
- `GATE_STATUS_TEMPLATE.yaml`;
- `BASELINE_COMPARATORS.md`;
- `ASSUMPTIONS_LEDGER_TEMPLATE.md`;
- `DERIVATION_MAP_TEMPLATE.md`;
- `MODEL_REGISTRY.md`;
- `NEW_MODEL_CHECKLIST.md`;
- `recovery/CURRENT_QG_FRONT.md`;
- `recovery/RECOVERY_GUIDE.md`;
- `INFRASTRUCTURE_STATUS.yaml`.

### Single-dynamics rule

A concrete model must derive its RQIR-facing hierarchy from one coherent dynamics/convention:

`model -> J,N,D/chi^R,higher correlators -> Paper I -> Paper II -> Paper III`.

Do not independently tune kernels/observables to manufacture a discriminator.

### QG model gates

- QG-001 physical state space;
- QG-002 matter-gravity dynamics;
- QG-003 Newtonian/GR limit;
- QG-004 unitarity/positivity/CP;
- QG-005 gauge/constraint consistency;
- QG-006 ordinary-QM/semiclassical limits;
- QG-007 first model-specific discriminator;
- QG-008 Paper-I finite-discriminant propagation;
- QG-009 positive nuisance-profiled identifiability;
- QG-010 physical resource/measurability closure.

Cross-gates include conservation/Bianchi/Ward, causality, positivity/spectral structure, flat-QFT limit, EFT power counting, stress-energy renormalization, model degeneracy and detector measurability.

Allowed state: `PASS/FAIL/BLOCKED/NOT_TESTED/NOT_APPLICABLE`. PASS requires repository evidence; FAIL is retained.

### Comparator registry

Future candidates must address applicable:

- C0 classical GR/Newtonian;
- C1 semiclassical gravity;
- C2 stochastic gravity;
- C3 classical-channel/hybrid/postquantum gravity;
- C4 conventional quantum/technical mediator alternatives;
- C5 perturbative quantum gravity;
- C6 full-QFT-source + classical-interface alternatives.

The weakest unresolved comparator bounds claim strength.

### Process freeze

**CG-INFRA-009:** model evaluation rules are frozen before the first real ansatz. Candidate-dependent changes require explicit methodological correction/provenance.

**CG-NG-002:** 100% repository readiness to start Candidate Gravity is not 100% theory/model readiness.

## Recovery rules

Repository, not chat history, is authority. Read `docs/RECOVERY_GUIDE.md` and `recovery/CURRENT_FRONT.md` first.

RTK and DSIR remain separate; their results enter RQIR only after independent RQIR derivation.

Rejected/failed/superseded Candidate Gravity versions remain in the model registry and recovery history.

## Immediate next scientific priority

Repository preparation is complete.

Instantiate the first real construction as `ANSATZ-*` using `candidate_gravity/NEW_MODEL_CHECKLIST.md`.

**First physics targets:** QG-001 and QG-002. Freeze a coherent physical state space, variables, primary dynamics, interaction, constraints, parameter domain and approximation order before searching for a detector-level RQIR advantage.
