# RQIR Model Benchmark Matrix

**Status:** PRE-REGISTERED BENCHMARK SCAFFOLD / NON_PROMOTING  
**Date:** 2026-09-06  
**Scope:** existing-model learning, comparator mapping, and Candidate Gravity anti-bias control  
**Authority rule:** populate scientific statuses only from explicit frozen RQIR provenance. Reputation, textbook acceptance, literature popularity, or model-family name alone is not a PASS/FAIL certificate.

This matrix is the operational companion to `RQIR_MODEL_LEARNING_AND_HOLDOUT_PROTOCOL.md` and `KG_ARCHITECTURAL_PRINCIPLES.md`.

## Controlled statuses

- `SCOPED_PASS` — a specified realization passed a specified frozen gate.
- `SCOPED_FAIL` — a specified realization failed a specified frozen gate.
- `COMPARATOR_EQUIVALENT` — claimed effect is absorbed by an admitted comparator in the tested scope; novelty fails for that effect.
- `NON_IDENTIFIABLE` — tested observable/regime does not distinguish the candidates.
- `BLOCKED` — authority insufficient; neither PASS nor FAIL.
- `UNTESTED` — no qualifying frozen RQIR result yet.
- `PENDING_PROVENANCE_MAPPING` — potentially relevant prior repository work exists or the family is a declared comparator target, but a scoped auditable model-to-gate record has not yet been entered here.

## Benchmark matrix — current preregistration

| Family / comparator target | Current RQIR status | Authority scope | Allowed KG lesson now? | Forbidden inference | Next action |
|---|---|---|---|---|---|
| GR / relativistic baseline | `UNTESTED / PENDING_PROVENANCE_MAPPING` | Baseline role is conceptually admitted, but no family-level full-funnel certificate is recorded in this matrix | Only universally required baseline/limit structure already frozen elsewhere | Do not say “GR passed full RQIR” | Map exact baseline gates and provenance |
| EFT-like gravity | `UNTESTED / PENDING_PROVENANCE_MAPPING` | Mentioned as admissible learning/comparator material in KG design doctrine | Structural EFT lessons only when tied to explicit provenance | Do not equate EFT-like with a single theory or infer family-wide novelty failure | Map representative(s) and quotient coordinates |
| Higher-curvature gravity | `UNTESTED / PENDING_PROVENANCE_MAPPING` | Declared possible learning family; no scoped matrix authority yet | None beyond already frozen generic consistency lessons | No family-wide PASS/FAIL | Freeze representative set and gates |
| Scalar-tensor gravity | `UNTESTED / PENDING_PROVENANCE_MAPPING` | Declared possible learning family; no scoped matrix authority yet | None beyond already frozen generic consistency lessons | No Horndeski/DHOST family claim without explicit realization audit | Freeze representative set and gates |
| Lorentz-breaking gravity | `UNTESTED / PENDING_PROVENANCE_MAPPING` | Declared possible learning family; no scoped matrix authority yet | None beyond already frozen generic consistency lessons | No family-wide causal/positivity conclusion | Freeze representative set and gates |
| Nonlocal gravity comparator target | `PENDING_PROVENANCE_MAPPING` | Explicitly named in the current downstream comparator-quotient chain, but quotient not yet reached | Comparator design may be prepared; no outcome may be assumed | Do not call it PASS, FAIL, or equivalent before quotient authority | Recover/freeze exact nonlocal comparator basis and representative(s) |
| Asymptotic-safety comparator target | `PENDING_PROVENANCE_MAPPING` | Explicitly named in the current downstream comparator-quotient chain, but quotient not yet reached | Comparator design may be prepared; no outcome may be assumed | Do not infer asymptotic-safety success/failure from KG calculations | Recover/freeze exact comparator representation and representative(s) |
| Fixed comparator class C3 | `PENDING_PROVENANCE_MAPPING` | Explicit downstream quotient target | May be used only after exact definition/provenance is recovered | No claim that KG survives C3 yet | Map exact C3 definition and frozen coordinates |
| Fixed comparator class C4 | `PENDING_PROVENANCE_MAPPING` | Explicit downstream quotient target | May be used only after exact definition/provenance is recovered | No claim that KG survives C4 yet | Map exact C4 definition and frozen coordinates |
| Fixed comparator class C5 / `ANSATZ-PQG-EFT-001` v0.1 reference | `REFERENCE_PRESENT / QUOTIENT_NOT_YET_REACHED` | Permanent C5 reference exists; active promotable ansatz remains none | Preserve reference/provenance only | Reference existence is not a novelty or model PASS certificate | Reach frozen downstream C5 quotient after prerequisites |
| Candidate Gravity current lineage | `BLOCKED / IN_DEVELOPMENT` | Numerical support advancing; retained physical blocker remains Iteration 421; no robust comparator-subtracted residual | May learn from prior validated gates under anti-leakage protocol | Do not call KG full-funnel PASS or new physics | Close support → assemble BASE/HALF → reevaluate blocker → complete quotient chain |

## Minimum record required before upgrading any row

A row may leave `UNTESTED/PENDING_PROVENANCE_MAPPING` only when the repository contains:

1. exact representative/model definition or frozen equivalence-class definition;
2. exact parameter/kinematic/regime scope;
3. gate definition and frozen thresholds/rules;
4. reproducible code or exact analytical derivation where applicable;
5. result artifact/record and commit provenance;
6. controlled status;
7. explicit statement of what the result does **not** imply for the wider family;
8. learning/holdout contamination record if the result influences KG design.

## Funnel-depth reporting rule

Do not report a universal percentage such as “X% of existing models are wrong” until both numerator and denominator are preregistered and scientifically meaningful. A parameter realization, a benchmark representative, a comparator equivalence class, and an entire theory family are different units and must not be mixed.

Preferred reporting units are:

- number of preregistered representatives tested;
- number of frozen gates reached per representative;
- scoped status per gate;
- comparator-equivalence/identifiability class;
- unresolved/blocked fraction.

## Interaction with current Candidate Gravity authority

Current Candidate Gravity readiness is not promoted by creating this matrix. The existing mass-support program and physical blocker remain authoritative. No comparator family is declared exhausted.

**MODEL_READINESS remains 24%.**
