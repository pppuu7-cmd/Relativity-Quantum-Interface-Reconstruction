# RQIR post503 — model-learning, anti-leakage, and transfer-control iteration

**Date:** 2026-09-06  
**Classification:** METHODOLOGY / PROVENANCE ADVANCE — NON_PROMOTING  
**Authority baseline at start/end of this log:** Iteration 503 current front unless a later race-created authoritative front supersedes it.

## Numerical-front reconciliation

At the live check used for this iteration:

- latest completed numerical mass-support authority: Iteration 503, frozen manifest rank20 `(-2.5e-6,+2.5e-6)`, multiplicity 1;
- rank20 raw-consumed classification: `PASS_RAW_CONSUMED_MANIFEST_RANK20_FULL_Z_MP80_MP120__NON_PROMOTING`;
- certified occurrence-weighted support: `25/32 = 78.125% = 2000/2560` row occurrences;
- authorized next coordinate: rank21 `(-2.5e-6,+5e-6)`, multiplicity 1;
- canonical rank21 run `34048058915`, job `101526571416`, remained `in_progress` on repeated checks during this methodology iteration;
- no duplicate heavy run was triggered;
- retained physical authority remained Iteration 421 `BLOCKED_CONVERGENCE`, unresolved physical set `[2]`;
- `MODEL_READINESS` remained `24%`.

A workflow being green/completed, if that occurs after this log, is not scientific PASS until the frozen raw-authority audit/artifact-consumption chain has completed.

## Question addressed

The Candidate Gravity architecture now explicitly treats existing models as a learning set for discovering reusable structural constraints, successful motifs, pathologies, equivalences, and non-identifiability. The methodological risk is circularity: if the same information is used both to build the candidate and later advertised as independent confirmation, apparent novelty is inflated.

This iteration freezes controls against that failure mode.

## Files frozen in this methodological branch

### 1. Candidate Gravity architectural doctrine

`candidate_gravity/recovery/KG_ARCHITECTURAL_PRINCIPLES.md`

Commit at initial creation: `3791fb36a585384c0980eef84044b7476ae6c96b`.

Core doctrine: Candidate Gravity is the minimal established/surviving core plus a minimal irreducible comparator-subtracted novel sector, with independent holdout evidence. It is neither “only new physics” nor a union of every successful existing model.

### 2. Model-learning / holdout anti-leakage protocol

`candidate_gravity/recovery/RQIR_MODEL_LEARNING_AND_HOLDOUT_PROTOCOL.md`

Commit: `bac191aa20aa1dc569eeac35270ffc893144a822`.

Frozen epistemic roles:

- `G_train` — source-model/comparator lessons permitted to affect KG design;
- `G_val` — frozen development checks;
- `G_novelty` — post-freeze comparator quotient/equivalence decision;
- `G_holdout` — independent confirmation not used to select/tune/repair the novel sector.

If a test result, trend, sign, target magnitude, preferred region, or pass/fail behavior influences KG construction, the overlapping test is contaminated for independent holdout use in that lineage. It cannot later be relabeled independent by renaming the candidate.

### 3. Existing-model benchmark scaffold

`candidate_gravity/recovery/RQIR_MODEL_BENCHMARK_MATRIX.md`

Commit: `80a158e5a435750a5b1e2612da28a9236a7a0012`.

A targeted repository search did not yield a trustworthy ready-made model-family → RQIR-status registry sufficient to assign scientific PASS/FAIL statuses to famous theory families. Therefore the matrix deliberately preregisters GR, EFT-like, higher-curvature, scalar-tensor, Lorentz-breaking, nonlocal, asymptotic-safety, C3, C4, and C5 targets conservatively as `UNTESTED`, `PENDING_PROVENANCE_MAPPING`, or reference-present/quotient-not-yet-reached as appropriate.

This negative finding is retained because assigning statuses from memory or reputation would create confirmation bias.

### 4. Learning-transfer hierarchy

`candidate_gravity/recovery/RQIR_LEARNING_TRANSFER_HIERARCHY.md`

Commit: `cdff8fc1ce652f9abdb16755c54ca267b5651ab2`.

Transfer strengths are frozen as:

- `T0 HYPOTHESIS_ONLY` — literature/analogy/unmapped result; may choose future benchmarks, cannot hard-constrain KG;
- `T1 SCOPED_EMPIRICAL` — reproduced/frozen result for a scoped realization; may prioritize search/diagnostics, cannot be generalized to a family;
- `T2 CLASS_CONDITIONAL` — class-wide result under explicit assumptions; hard transfer only when KG is shown to lie in the covered class;
- `T3 NECESSARY/STRUCTURAL` — model-independent necessary condition/theorem with applicability to KG established.

Only applicable T2/T3 constraints may hard-delete regions of KG design space. PASS and FAIL obey the same transfer restriction: a successful motif in another theory is not automatically necessary for KG.

### 5. Model-learning ledger

`candidate_gravity/recovery/RQIR_MODEL_LEARNING_LEDGER.md`

Commit: `b0d00a0c47a0362043799f88c320237e3339a61f`.

The ledger records source family, exact representative, provenance, gate, scoped status, transfer tier, assumptions, KG applicability, reusable rule, forbidden inference, contaminated tests, and authority. Initial rows are intentionally conservative. Famous-family names remain T0/pending until exact RQIR provenance is recovered/frozen. The current KG lineage has only scoped internal diagnostic learning authority while physical index2 remains blocked.

## Exact design-space rule

Let `S0` denote the pre-learning KG design space. Hard exclusion is licensed only by applicable structural/necessary constraints and class-conditional constraints whose assumptions are proven to cover KG:

`S_admissible = S0 ∩ (intersection applicable T3 conditions) ∩ (intersection applicable T2 conditions)`.

T0/T1 evidence may change search priority and diagnostics but must not silently change the admissible set.

This prevents both failure-mode overgeneralization (“one model failed, therefore KG must avoid the whole family”) and success-mode overgeneralization (“one model passed, therefore KG must copy its mechanism”).

## Novelty remains separate

Learning constructs the admissible model space; it does not certify a new-physics sector. After candidate freeze the novelty question remains a comparator-quotient problem, schematically

`Delta O_KG = O_KG - Pi_known O_KG`.

If the frozen quotient removes the claimed signal, classify the effect as comparator-equivalent / novelty failure. If authority is insufficient, classify `BLOCKED`. A nonzero diagnostic residual before the frozen quotient is not discovery.

## Scientific impact

✅ The idea “KG learns from other models” is now operational and auditable rather than informal.

✅ Training information and independent confirmation are separated by an explicit contamination rule.

✅ Source-model lessons have transfer strengths, preventing unsupported family-wide inference.

✅ Existing-model benchmark rows are provenance-gated rather than assigned from memory.

✅ Negative/null/scoped results remain usable learning information without becoming universal no-go claims.

🟡 Exact comparator-family definitions/provenance for C3/C4/C5/nonlocal/asymptotic-safety still need recovery/mapping before any row can receive a scientific outcome.

🟡 The active numerical support program remains unfinished and must retain frozen rank order.

❌ No robust comparator-subtracted residual exists yet.

❌ `ANSATZ-003` remains uncreated.

❌ Fisher/resources remain closed.

## Next authorized work

1. Do not duplicate rank21 while canonical run `34048058915` is active.
2. When rank21 terminates, require frozen raw-authority audit and artifact consumption before assigning PASS/BLOCKED.
3. If rank21 receives raw PASS, only rank22 `(+2.5e-6,-5e-6)` becomes the next heavy support gate.
4. In parallel, recover exact definitions/provenance for downstream comparator targets before upgrading any benchmark/learning-ledger row above T0.
5. After all 28 distinct support coordinates close, execute the already frozen independent BASE/HALF MP80/120 assembly, then reevaluate the Iteration-421 blocker before the downstream quotient chain.

## Readiness

Stable rubric unchanged:

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

**MODEL_READINESS = 24%.**  
**Change this iteration: 0 percentage points.**

Reason: this iteration materially strengthens methodology, anti-bias control, and future model-construction provenance, but it does not complete a stable-rubric physical component.
