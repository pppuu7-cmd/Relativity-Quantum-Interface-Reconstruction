# RQIR Model-Learning and Holdout Protocol

**Status:** FROZEN METHODOLOGY / ANTI-LEAKAGE PROTOCOL  
**Date:** 2026-09-06  
**Scope:** RQIR-guided Candidate Gravity construction  
**Scientific effect:** methodology/provenance only; **NON_PROMOTING**. This file does not promote a physical residual, ansatz, comparator novelty claim, or `MODEL_READINESS` by itself.

This protocol operationalizes `KG_ARCHITECTURAL_PRINCIPLES.md`, especially KG-AP-002 and KG-AP-003. Its purpose is to let Candidate Gravity learn from existing models and prior RQIR results without converting design information into circular evidence for novelty.

## MLH-001 — Four disjoint scientific roles

Every gate, observable, benchmark, or comparator result used in KG construction must be assigned a role before it contributes to a claim:

1. **TRAINING / DESIGN (`G_train`)** — validated lessons from known models/comparators that may constrain the admissible KG design space.
2. **VALIDATION (`G_val`)** — frozen checks used during development to reject or repair a KG realization.
3. **NOVELTY / QUOTIENT (`G_novelty`)** — frozen comparator subtraction/equivalence analysis performed after candidate freeze to determine whether an irreducible residual exists.
4. **HOLDOUT (`G_holdout`)** — observables/checks not used to select, tune, repair, or rank the claimed novel sector and reserved for independent confirmation.

Conceptually,

\[
G_{\rm RQIR}=G_{\rm train}\cup G_{\rm val}\cup G_{\rm novelty}\cup G_{\rm holdout}.
\]

The role labels are about epistemic use, not merely file location. A calculation can be mathematically identical to a future holdout test yet cease to be holdout if its result was inspected and used in model construction.

## MLH-002 — Contamination / anti-leakage rule

A gate or observable is **contaminated for independent confirmation** if its outcome, target value, trend, sign, residual shape, preferred parameter region, or pass/fail behavior is used to choose or modify any of:

- operator content or field content;
- couplings, coefficients, priors, ranges, or constraints;
- pole/kernel/nonlocal structure;
- regulator, representation, subtraction, or projection choice;
- numerical support subset or reconstruction rule;
- observable definition;
- threshold or acceptance rule;
- candidate ranking/selection.

Once contaminated, that item may remain TRAINING or VALIDATION evidence but **must not be counted as independent HOLDOUT evidence for the same novelty claim**. A replacement holdout must be frozen before its result is inspected.

No after-the-fact relabeling from TRAINING/VALIDATION back to HOLDOUT is permitted.

## MLH-003 — Learning record required for every imported lesson

A structural lesson may influence KG only if it is recorded with the following minimum schema:

- `lesson_id`;
- source model family and exact representative/realization;
- exact repository provenance (commit/result/gate) or explicit `LITERATURE_HYPOTHESIS_ONLY`;
- tested gate and observable/regime;
- status from the controlled vocabulary;
- scope of the conclusion;
- reusable structural lesson;
- forbidden inference / non-generalization statement;
- whether use for KG training is allowed;
- holdout items contaminated by using the lesson;
- authority level and unresolved blockers.

Controlled status vocabulary:

- `SCOPED_PASS`;
- `SCOPED_FAIL`;
- `COMPARATOR_EQUIVALENT`;
- `NON_IDENTIFIABLE`;
- `BLOCKED`;
- `UNTESTED`.

A literature statement can seed a benchmark or hypothesis, but it is not an RQIR learning authority until the relevant frozen RQIR mapping/gate is reproduced or otherwise explicitly admitted under a stated evidence class.

## MLH-004 — Scope discipline

A result for one representative, parameter region, kinematic regime, gauge/representation, truncation, or observable must not be promoted to an entire theory family unless an explicit family-level coverage argument has been frozen and passed.

Therefore:

- `SCOPED_FAIL` is not “the whole theory is false”;
- `BLOCKED` is neither PASS nor FAIL;
- `COMPARATOR_EQUIVALENT` is a novelty failure for the claimed effect, not necessarily a physical inconsistency;
- `NON_IDENTIFIABLE` means the tested observable/regime does not separate the candidates;
- `UNTESTED` must remain visibly untested.

Negative and null results are retained; no cherry-picking of only useful lessons is allowed.

## MLH-005 — What KG is allowed to learn

KG may reuse validated **structural constraints** that define the surviving admissible model space, including where applicable:

- conservation / Ward structure;
- analyticity and causal restrictions;
- pole/ghost/positivity restrictions;
- support and representation consistency;
- required IR / GR limits;
- known comparator equivalences and degeneracies;
- numerical conditioning lessons;
- identifiability failures that rule out useless parameterizations.

KG must not learn a target answer for the irreducible residual. In particular, the sign, magnitude, functional shape, or preferred parameter values of a reserved novelty/holdout signal must not be used to design the novel sector.

## MLH-006 — Candidate freeze before novelty credit

Before a KG realization is eligible for a novelty claim, freeze and provenance-hash at least:

1. parent dynamics / operator basis;
2. admitted comparator basis and quotient/projection rule;
3. parameter priors/ranges and selection rule;
4. representation/regulator/subtraction conventions;
5. observables used for novelty testing;
6. numerical thresholds and stability criteria;
7. designated holdout set;
8. code/data commit identifiers needed for reproduction.

A later repair triggered by seeing novelty or holdout results creates a new candidate version. Previously inspected holdout information remains contaminated for that lineage and cannot be reset merely by renaming the candidate.

## MLH-007 — Novelty decision contract

Novelty is not credited because KG was designed to satisfy known gates. A candidate novel sector requires a concrete nonzero comparator-subtracted residual under the frozen comparator quotient and must survive the applicable robustness checks.

If the residual vanishes within the frozen quotient/equivalence definition, classify the claimed effect as `COMPARATOR_EQUIVALENT / NOVELTY_FAIL`.

If numerical or analytical authority is insufficient, classify it as `BLOCKED`, never zero-fill or infer novelty from diagnostics.

This protocol does not alter the existing rule: `ANSATZ-003` remains uncreated until a concrete robust comparator-subtracted residual exists; Fisher/resources remain closed until their frozen prerequisites are met.

## MLH-008 — Holdout success is necessary evidence, not automatic discovery

A successful independent holdout does not by itself establish new physics. Any final claim must also satisfy the applicable consistency, Ward/conservation, positivity/causality, comparator-exhaustion, robustness, identifiability, and experimental interpretation gates.

Conversely, a failed genuine holdout is retained as an adverse result and cannot be removed by redefining the holdout after inspection.

## MLH-009 — Benchmark-matrix population rule

The companion benchmark matrix must be populated from explicit RQIR provenance, not from memory or reputation of a model family. Famous theories may appear as `UNTESTED / PENDING_PROVENANCE_MAPPING` until the repository contains a scoped representative and frozen gate result.

The matrix is intended to answer two different questions separately:

- what structural lessons are available for KG design;
- how far each tested realization has actually travelled through the RQIR funnel.

Those questions must never be collapsed into a single unsupported percentage of “models that are wrong”.

## MLH-010 — Recovery / non-retroactivity

Future iterations must preserve this anti-leakage protocol unless an explicit replacement is committed with a reason, compatibility analysis, and a statement of which earlier learning/holdout assignments become invalid.

No future iteration may retroactively convert information already used to construct KG into independent evidence for the same claimed novelty.

## Current interaction with authority

At adoption, current numerical support progress and the Iteration-421 physical blocker remain unchanged. This methodology is **NON_PROMOTING** and contributes **0 percentage points** to the stable readiness rubric.

**MODEL_READINESS remains 24%.**
