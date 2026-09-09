# RQIR Core v1.0 — Freeze Manifest

**Freeze date:** 2026-09-09  
**Status:** FROZEN / controlled-extension only  
**Scientific scope closed before freeze:** Papers I–III = 100% repository scientific readiness.

## 1. Purpose

RQIR Core v1.0 is the fixed methodological standard to be used for external benchmarking of known gravity and quantum-gravity frameworks, and later—if justified—for evaluation of any RQIR-derived Candidate Gravity model.

The purpose of the freeze is to prevent post-hoc movement of the evaluation criteria after benchmark outcomes are known.

## 2. Frozen core

The following are frozen in v1.0 unless a formally versioned methodological defect is demonstrated:

- operational-first observable hierarchy;
- baseline and residual discipline;
- source-calibration and identifiability rules;
- nuisance-geometry and covariance treatment;
- requirement that negative controls remain explicit;
- physical resource/experiment-architecture criteria;
- detector-facing estimability requirement;
- comparator/failure-state semantics;
- rule that `BLOCKED` is not evidence for `NEW_REQUIRED`;
- requirement that apparatus-only null directions may survive only when science-orthogonal;
- provenance and reproducibility requirements;
- separation of scientific closure from journal/submission administration.

## 3. Relationship to benchmarking

Known models and schools are to be evaluated outside the frozen core, in the KMQGB benchmarking programme. Model-specific formulae, adapters, mappings, approximations and numerical implementations belong to the benchmarking layer.

A model failing an RQIR v1.0 gate is not, by itself, evidence that the gate should be weakened or changed.

A model-specific representation problem is an adapter problem unless it demonstrates that a physically legitimate class of observables cannot be represented by the frozen RQIR interface at all.

## 4. Relationship to Candidate Gravity

Any future RQIR-derived Candidate Gravity model must be evaluated against the same frozen v1.0 criteria used for known models. Candidate-model performance must not be used to rewrite v1.0 retrospectively.

A new-gravity branch is not article-authorized merely because one or more existing models are `BLOCKED`. The Paper-IV terminal comparator decision must first support `NEW_REQUIRED` under the frozen framework.

## 5. Allowed maintenance without a new core version

The following do not change RQIR Core v1.0 and may be committed on `main`:

- typo and formatting fixes;
- journal/submission packaging for Papers I–III;
- additional reproducibility certificates that do not alter definitions or thresholds;
- benchmarking links and provenance references;
- model-specific adapters/results that are explicitly outside the core;
- bug fixes that restore the already-defined mathematics without changing its meaning, provided the regression impact is documented.

## 6. Changes requiring v1.1 or later

A new RQIR core version is required when a change modifies any frozen definition, admissible observable class, comparator semantics, identifiability criterion, resource criterion, failure-state interpretation, or scientific decision threshold.

Such a change requires:

1. a documented methodological defect, not merely an inconvenient benchmark result;
2. a minimal proposed correction;
3. an explicit old-vs-new semantic diff;
4. regression reruns over all already benchmarked models/schools;
5. a statement of which prior conclusions change;
6. a new version identifier (`v1.1`, `v2.0`, etc. as appropriate).

## 7. Frozen scientific authority

Immediately before the freeze, the repository recorded:

- Paper I scientific material: 100%;
- Paper II scientific material: 100%;
- Paper III strengthened apparatus-specific scientific material: 100%;
- Papers I–III collective repository scientific readiness: 100%.

The authoritative readiness document is `docs/PAPER_I_V_REPOSITORY_READINESS_AUDIT_2026-09-09.md`.

## 8. Governance rule

From this freeze forward, RQIR Core v1.0 is a measuring standard, not a moving research target.

Benchmark outcomes may motivate a future version, but they cannot silently alter v1.0. Any later Candidate Gravity model is judged by the same frozen standard unless a separately documented and regression-tested successor version has already been adopted independently of that candidate's desired outcome.
