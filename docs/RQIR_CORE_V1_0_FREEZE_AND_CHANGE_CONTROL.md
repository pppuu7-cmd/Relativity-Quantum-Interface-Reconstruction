# RQIR Core v1.0 — Freeze and Change-Control

**Freeze date:** 2026-09-09  
**Status:** `FROZEN_CORE_V1.0 / MAINTENANCE_CONTROLLED_EXTENSION`  
**Scientific prerequisite:** Papers I–III scientific/material layer is closed at 100% in the strict repository-readiness audit.

## 1. Purpose of the freeze

RQIR is now the model-independent operational/comparator standard used to test known gravity/quantum-gravity frameworks and, only later if scientifically authorized, a future Candidate Gravity.

The value of the standard now depends on it **not becoming a moving target after benchmark outcomes are observed**.

Therefore the following normative layers are frozen as **RQIR Core v1.0**:

- operational observable hierarchy and common-domain observable mapping rules;
- baseline/comparator discipline and residual definitions;
- identifiability, nuisance-profiling and covariance/whitening rules;
- detector-facing visibility and resource-closure rules;
- consistency/failure-state semantics;
- comparator-class and degeneracy discipline;
- fail-closed treatment of missing objects;
- terminal Paper-IV decision vocabulary and the rule that `BLOCKED` is not evidence for `NEW_REQUIRED`;
- reproducibility/provenance requirements needed to support Papers I–III.

The freeze is methodological. It does not assert that nature is described by any particular model and does not close Paper IV.

## 2. Repository roles after v1.0

### RQIR

Role: **independent judge / normative standard**.

Mode: `MAINTENANCE / CONTROLLED EXTENSION`.

Normal benchmark-specific formulas, adapters, model calculations and model verdicts do not belong in the frozen core.

### Known-Models-Quantum-Gravity-Benchmark (KMQGB)

Role: **active scientific proving ground for known models and schools**.

KMQGB may read RQIR Core v1.0 as a frozen external standard and may construct model-specific adapters from a framework's native objects into RQIR observables. It must not alter RQIR merely because a framework fails, is blocked, or is inconvenient to represent.

KMQGB supplies the growing evidence base for Paper IV.

### Future Candidate Gravity

Role: **separate model-development repository**, to be created/activated only under the accepted Paper-IV architecture.

A future in-house model must be tested against the **same pre-existing RQIR Core version** used on external frameworks. Candidate-specific results may not retroactively modify the judge.

## 3. Adapter vs core-extension rule

A framework-specific translation is a **KMQGB adapter** when the RQIR observable universe is adequate but the framework uses different native variables, representations, regulators, states or computational language.

Examples:

- mapping a spinfoam boundary amplitude to a relational transition observable;
- mapping a spectral/form-factor result to a detector-response block;
- translating a process-matrix quantity into a declared causal/process observable;
- converting framework-native correlation functions into an existing RQIR covariance/response interface.

These do **not** justify changing RQIR Core.

A core extension is admissible only when there is evidence that a physically legitimate observable/consistency object **cannot in principle be represented by the existing RQIR interface**, rather than merely being difficult to calculate.

## 4. Change-control gate for v1.1+

Every proposed core change must satisfy all of the following before merge:

1. **Defect statement:** identify the exact frozen Core-v1.0 rule/interface that is incomplete or internally inconsistent.
2. **Physical witness:** provide at least one physically admissible framework/observable demonstrating the defect.
3. **Adapter impossibility:** explain why a KMQGB adapter cannot represent the object without changing normative semantics.
4. **Outcome independence:** the change must not be motivated by making a favored model pass or by eliminating an unwanted residual.
5. **Version bump:** normative change creates a new explicit version (`v1.1`, `v1.2`, ...); Core v1.0 remains immutable historical authority.
6. **Regression scope:** list all previously terminal benchmark records affected by the change.
7. **Mandatory rerun:** rerun every affected benchmark under the new version before using cross-model conclusions.
8. **Delta report:** publish old/new verdict comparison and explain every changed terminal status.
9. **Candidate firewall:** no future Candidate Gravity fit/residual may be used as evidence that the judge should be modified.

A change failing any item remains outside Core and should be implemented, if useful, as a KMQGB adapter/experimental extension.

## 5. Version-lock requirement for every benchmark

Every post-freeze benchmark record must declare:

- `rqir_core_version`;
- exact RQIR authority commit or manifest used;
- adapter version/ref;
- observable/domain declaration;
- comparator registry version/ref;
- whether any non-core experimental extension was used.

Comparisons across models are valid only after version alignment or an explicit compatibility map.

## 6. Paper-IV / Paper-V firewall

Paper IV accumulates evidence from known frameworks and ends only after the frozen funnel supports one of:

- `EXISTING_SUFFICIENT`;
- `ADAPT_EXISTING`;
- `HYBRID_REQUIRED`;
- `NEW_REQUIRED`.

`BLOCKED_MISSING_REQUIRED_OBJECT`, `BLOCKED_PROTOCOL_MISMATCH`, a consistency failure in one framework, or absence of a computed residual is **not** evidence for `NEW_REQUIRED`.

Paper V / a genuinely new Candidate Gravity becomes scientifically authorized only if Paper IV returns `NEW_REQUIRED` under the frozen/declared RQIR version.

## 7. Frozen status at this point

- **RQIR Core:** `v1.0 — FROZEN`.
- **Papers I–III scientific/material layer:** `100% — CLOSED`.
- **RQIR repository:** `MAINTENANCE / CONTROLLED EXTENSION`.
- **Paper IV:** active; known-model benchmark evidence belongs primarily in KMQGB.
- **Candidate Gravity:** conditional/separate; never a reason to tune RQIR Core.

This document is normative governance for the post-Papers-I–III phase.