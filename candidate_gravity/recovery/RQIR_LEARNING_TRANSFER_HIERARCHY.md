# RQIR Learning-Transfer Hierarchy

**Status:** FROZEN METHODOLOGY / NON_PROMOTING  
**Date:** 2026-09-06  
**Purpose:** define how lessons from existing models may constrain Candidate Gravity without overgeneralization or novelty leakage.

This file refines `RQIR_MODEL_LEARNING_AND_HOLDOUT_PROTOCOL.md`. It does not change any physical/numerical authority, thresholds, support order, or readiness.

## LTH-001 — Transfer is not automatic

A PASS/FAIL/equivalence result for another model becomes a hard Candidate Gravity design constraint only if the assumptions that make the result necessary are shown to apply to Candidate Gravity.

Let a source result be

\[
A_s \Longrightarrow C_s,
\]

where `A_s` is the complete assumption set and `C_s` is the conclusion. A hard transfer to KG is licensed only after an explicit applicability map establishes

\[
A_{\rm KG} \supseteq A_s
\]

for every assumption used by the argument, or an equivalent proof of applicability. Shared vocabulary, similar operators, or membership in a broad theory family is not enough.

## LTH-002 — Four transfer strengths

### `T0 — HYPOTHESIS_ONLY`
Literature claim, heuristic analogy, unreplicated calculation, or repository note lacking a frozen scoped RQIR authority.

Allowed use: choose a future benchmark or formulate a question.  
Forbidden use: exclude KG structures, promote readiness, or count as evidence for novelty.

### `T1 — SCOPED_EMPIRICAL`
A frozen/reproduced result exists for a particular representative, parameter region, observable, or kinematic regime, but no theorem/class-wide coverage licenses generalization.

Allowed use: prioritize searches, identify likely pathologies, define diagnostics, or motivate validation gates.  
Forbidden use: hard-delete the corresponding region of KG design space solely by analogy or claim the whole source family succeeds/fails.

### `T2 — CLASS_CONDITIONAL`
A frozen result is proved or exhaustively certified for a well-defined equivalence/model class under explicit assumptions.

Allowed use: hard-constrain KG **only if** KG is proven to lie inside the covered class and the assumptions are preserved. Otherwise downgrade the transfer to `T1`.

### `T3 — NECESSARY / STRUCTURAL`
A model-independent necessary condition or theorem with explicit assumptions is frozen, and applicability to KG is established.

Allowed use: intersect the Candidate Gravity admissible design space with the condition before candidate freeze.

Examples of the kind of requirement that could reach this tier when proved applicable include exact conservation/Ward requirements, exact representation identities, or genuine no-go conditions. The tier is earned by proof/provenance, not by the topic label.

## LTH-003 — Safe design-space update

Let `S_0` be the pre-learning Candidate Gravity design space. Only applicable `T3` constraints and applicable `T2` class-conditional constraints may perform hard exclusion:

\[
S_{\rm admissible}
=
S_0\cap\bigcap_{g\in T3} A_g
\cap\bigcap_{k\in T2,\;KG\in C_k} A_k.
\]

`T1` and `T0` information may affect search order or diagnostics, but must not silently alter the hard admissible set.

This prevents a scoped failure in one existing model from being converted into an unsupported universal no-go.

## LTH-004 — PASS transfer is equally restricted

A successful source model does not imply that its mechanism is necessary or optimal for KG. Therefore source-model PASS results obey the same transfer hierarchy as FAIL results.

In particular:

- a `T1 SCOPED_PASS` may identify a viable motif;
- it cannot force that motif into KG;
- if two successful models are comparator-equivalent in the relevant observable, KG should learn the minimal equivalence-class structure rather than copy both formulations.

This implements the architectural rule that KG is not a union of successful theories.

## LTH-005 — Equivalence lessons

A comparator-equivalence result can be used as a novelty-design warning, but it may only become a hard exclusion from the claimed novel sector if the equivalence proof covers the proposed KG structure and the same frozen observable/quotient definition.

Otherwise the lesson remains scoped and must be retested after candidate freeze.

A known equivalence may reduce redundant parameterization of the established core; it must not be used to preselect the sign, magnitude, or detailed shape of the future irreducible residual.

## LTH-006 — Learning does not consume holdout silently

Whenever a `T0–T3` lesson influences model construction, the learning ledger must record which observables/gates/results were inspected. Any overlapping confirmation test is contaminated for that candidate lineage under `RQIR_MODEL_LEARNING_AND_HOLDOUT_PROTOCOL.md`.

Higher transfer strength does not exempt a result from this anti-leakage rule.

## LTH-007 — Required transfer record

Before a source lesson hard-constrains KG, record:

- source representative/equivalence class;
- source status and gate;
- exact provenance;
- transfer tier `T0/T1/T2/T3`;
- complete assumptions used by the source result;
- KG applicability argument;
- resulting permitted design action;
- explicit forbidden generalization;
- contaminated validation/holdout items.

If any required element for `T2/T3` is missing, downgrade to `T1` or `T0`; do not infer the missing piece.

## LTH-008 — Relationship to novelty

The learning hierarchy constructs the **admissible** KG space. It does not certify the **novel** KG sector.

After candidate freeze, novelty remains a separate question:

\[
\Delta O_{KG}=O_{KG}-\Pi_{known}O_{KG}.
\]

A nonzero diagnostic residual is not enough. The residual must survive the frozen comparator quotient, robustness, consistency and independent holdout chain before a new-physics claim becomes eligible.

## Current authority impact

This hierarchy is methodological/provenance authority only. It does not close the retained Iteration-421 physical blocker, does not certify a new mass-support rank, does not create `ANSATZ-003`, and does not open Fisher/resources.

**MODEL_READINESS remains 24%.**
