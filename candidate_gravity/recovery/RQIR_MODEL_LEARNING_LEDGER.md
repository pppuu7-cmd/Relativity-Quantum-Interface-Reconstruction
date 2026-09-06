# RQIR Model-Learning Ledger

**Status:** PRE-REGISTERED / PROVENANCE-GATED / NON_PROMOTING  
**Date:** 2026-09-06  
**Purpose:** machine-auditable bridge from existing-model RQIR results to Candidate Gravity design decisions.

This ledger implements `RQIR_MODEL_LEARNING_AND_HOLDOUT_PROTOCOL.md` and `RQIR_LEARNING_TRANSFER_HIERARCHY.md`. A row is not a scientific PASS/FAIL unless exact RQIR provenance supports that status. `T0` means hypothesis/reference-only transfer strength, not physical failure.

## Required schema

| Field | Meaning |
|---|---|
| `lesson_id` | Stable identifier for the learning record |
| `source_family` | Theory/comparator family |
| `representative` | Exact tested realization/equivalence class |
| `provenance` | Commit/result/gate; or explicit pending marker |
| `gate` | Frozen RQIR test producing the lesson |
| `scoped_status` | Controlled RQIR status |
| `transfer_tier` | `T0/T1/T2/T3` from the transfer hierarchy |
| `assumptions` | Assumptions required by the source result |
| `kg_applicability` | Why/how those assumptions apply to KG |
| `reusable_rule` | What KG is permitted to learn |
| `forbidden_inference` | What must not be generalized |
| `contaminated_tests` | Future confirmation tests made non-independent by use of the lesson |
| `authority` | Current epistemic authority |

## Current ledger

| lesson_id | source_family | representative | provenance | gate | scoped_status | transfer_tier | assumptions / KG applicability | reusable_rule | forbidden inference | contaminated_tests | authority |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `L-GR-0001` | GR / relativistic baseline | exact representative not yet mapped in this ledger | `PENDING_PROVENANCE_MAPPING` | baseline/IR role to be mapped | `UNTESTED` | `T0` | no complete model-to-gate assumption map recorded here | May seed explicit baseline/IR benchmark construction | Do not claim GR passed full RQIR; do not import unrecorded family-wide conclusions | none until used for design | hypothesis/reference only |
| `L-EFT-0001` | EFT-like gravity | representative not yet frozen | `PENDING_PROVENANCE_MAPPING` | comparator/quotient mapping pending | `UNTESTED` | `T0` | broad family label is insufficient for applicability | May motivate operator-basis benchmark candidates | Do not treat EFT-like gravity as one theory or infer universal equivalence | none until used | hypothesis/reference only |
| `L-HC-0001` | higher-curvature gravity | representative not yet frozen | `PENDING_PROVENANCE_MAPPING` | model benchmark pending | `UNTESTED` | `T0` | no frozen family coverage theorem here | May nominate candidate structural motifs/pathologies for testing | No family-wide PASS/FAIL or no-go transfer | none until used | hypothesis/reference only |
| `L-ST-0001` | scalar-tensor gravity | representative not yet frozen | `PENDING_PROVENANCE_MAPPING` | model benchmark pending | `UNTESTED` | `T0` | no scoped Horndeski/DHOST audit entered | May nominate explicit representatives for later RQIR mapping | No claim about all scalar-tensor/Horndeski/DHOST models | none until used | hypothesis/reference only |
| `L-LB-0001` | Lorentz-breaking gravity | representative not yet frozen | `PENDING_PROVENANCE_MAPPING` | consistency/causality benchmark pending | `UNTESTED` | `T0` | no exact representative or assumptions mapped | May motivate a future benchmark of causal/positivity restrictions | Do not infer universal causal failure/success | none until used | hypothesis/reference only |
| `L-C3-0001` | fixed comparator C3 | exact C3 definition/provenance not yet recovered into ledger | downstream chain named in `CURRENT_QG_FRONT.md` | fixed comparator quotient pending | `UNTESTED` | `T0` | quotient prerequisites not yet reached | Preserve C3 as preregistered downstream comparator target | Do not claim KG survives or fails C3 | none | preregistered target only |
| `L-C4-0001` | fixed comparator C4 | exact C4 definition/provenance not yet recovered into ledger | downstream chain named in `CURRENT_QG_FRONT.md` | fixed comparator quotient pending | `UNTESTED` | `T0` | quotient prerequisites not yet reached | Preserve C4 as preregistered downstream comparator target | Do not claim KG survives or fails C4 | none | preregistered target only |
| `L-C5-0001` | fixed comparator C5 | permanent reference `ANSATZ-PQG-EFT-001` v0.1 | `CURRENT_QG_FRONT.md`; detailed comparator mapping still pending | fixed C5 quotient not yet reached | `UNTESTED` | `T0` | reference existence is not quotient authority | Preserve frozen reference and future comparison target | Do not treat permanent reference as PASS, novelty, or active ansatz | none | reference present; outcome unavailable |
| `L-NL-0001` | nonlocal gravity comparator | exact representative/basis not yet mapped | downstream chain named in `CURRENT_QG_FRONT.md` | nonlocal quotient pending | `UNTESTED` | `T0` | prerequisites not reached; no exact comparator basis in ledger | Preserve as explicit comparator target; prepare provenance mapping only | No nonlocal PASS/FAIL/equivalence claim | none | preregistered target only |
| `L-AS-0001` | asymptotic-safety comparator | exact representative/basis not yet mapped | downstream chain named in `CURRENT_QG_FRONT.md` | asymptotic-safety quotient pending | `UNTESTED` | `T0` | prerequisites not reached; no exact comparator basis in ledger | Preserve as explicit comparator target; prepare provenance mapping only | No asymptotic-safety PASS/FAIL/equivalence claim | none | preregistered target only |
| `L-KG-0001` | Candidate Gravity current lineage | current pre-ansatz numerical/operator lineage | `CURRENT_QG_FRONT.md`, Iteration 421 blocker + current support authority | mass-support → assembly → blocker reevaluation | `BLOCKED` | `T1` for internal diagnostic lessons only | local support precision and exact estimator identities are scoped; physical index2 unresolved | Reuse validated numerical/provenance constraints and preserve frozen thresholds/order | Do not promote local support PASS into physical residual, ansatz, or novelty | any diagnostic inspected and used for redesign must be recorded under anti-leakage protocol | current internal scoped authority |

## Upgrade rule

A source-family row may be upgraded from `T0` only when an explicit representative and frozen RQIR provenance are entered. A `T1` result may become `T2` only after class coverage is established. `T3` requires a genuinely necessary/structural result plus an explicit applicability argument to KG.

No row may be upgraded by model reputation, literature popularity, or qualitative similarity alone.

## Candidate-Gravity design use

When a ledger row is actually used to modify KG, add a child learning record before or at the same commit as the design change containing:

1. exact source row/version;
2. exact design choice influenced;
3. transfer tier at time of use;
4. applicability argument;
5. list of contaminated validation/holdout gates;
6. replacement holdout, if required.

This converts “KG learns from other models” from an informal idea into auditable provenance.

## Current authority impact

Creating or populating this ledger with `T0`/preregistered entries is methodology only. It does not close the Iteration-421 blocker, does not certify a new comparator residual, does not create `ANSATZ-003`, and does not open Fisher/resources.

**MODEL_READINESS remains 24%.**
