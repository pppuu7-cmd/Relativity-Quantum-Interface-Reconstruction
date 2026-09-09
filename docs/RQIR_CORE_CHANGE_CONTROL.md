# RQIR Core Change Control

Current frozen core: **RQIR Core v1.0**.

## Decision rule

A proposed change is classified as one of three types.

### A. Maintenance — no core version change

Allowed when the change does not alter scientific meaning: editorial corrections, submission packaging, reproducibility metadata, links, provenance annotations, or implementation fixes that restore already-defined mathematics.

### B. Adapter/benchmark extension — no core version change

Allowed when a known model or school needs a model-specific mapping into the frozen RQIR observables, baselines or comparator interfaces. The adapter lives outside the core and must not change the core to improve the model's outcome.

### C. Core change — new version required

Required when the change alters an observable class, residual definition, admissibility condition, nuisance/identifiability rule, resource gate, comparator semantics, failure-state interpretation, threshold, or other scientific decision rule.

## Core-change acceptance test

A core change may be accepted only if all of the following are true:

1. a concrete methodological defect is demonstrated;
2. the defect is not merely that a benchmark model fails;
3. the smallest sufficient correction is stated;
4. effects on all prior benchmark results are enumerated;
5. all prior benchmarks are rerun under the candidate successor version;
6. the old v1.0 result remains recoverable;
7. the successor receives a new version number.

## Anti-retrofitting rule

No benchmark result—known theory or future Candidate Gravity—may be used to silently tune RQIR Core v1.0 after seeing the outcome.

If a future Candidate Gravity motivates a methodological correction, the correction must be justified independently, versioned, and regression-tested on the known-model benchmark set before the candidate is re-evaluated.

## Versioning

- `v1.x`: backward-compatible methodological clarification/extension that preserves the meaning of existing v1.0 gates for previously admissible cases.
- `v2.0+`: change that alters core semantics, terminal decisions, or admissibility in a way that can change prior scientific conclusions.

The freeze manifest is `docs/RQIR_CORE_V1_FREEZE_MANIFEST_2026-09-09.md`.
