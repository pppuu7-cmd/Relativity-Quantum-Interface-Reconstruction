# RQIR7 Known-Models Benchmark — Backup and Recovery Method

Status: ACTIVE RECOVERY AUTHORITY
Date initialized: 2026-09-08
Repository: `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`
Benchmark branch: `rqir7-known-models-benchmark`
Branch base commit: `02ad31e89f1df0d5515779e6b7526e8eb5505667`
Current external Candidate Gravity authority observed at initialization: main commit `c4d932f85d8d2a7f12a62f728a42c6400d3bf797`, Candidate Gravity Iteration 562, MODEL_READINESS 24%.

## 1. Purpose

This file makes the known-model RQIR benchmark recoverable from a new chat/session without relying on chat memory, hidden state, or prior conversation summaries. All scientific state needed to resume must be reconstructible from repository artifacts named below.

## 2. Non-negotiable protocol rules

1. Apply exactly the already-frozen RQIR funnel/gates used by Candidate Gravity. Never weaken, retune, or reinterpret a gate after seeing a known-model result.
2. A missing required published object is `BLOCKED_MISSING_REQUIRED_OBJECT`, not a scientific failure.
3. A protocol-domain mismatch is `BLOCKED_PROTOCOL_MISMATCH`, not a scientific failure.
4. Tool/runner/repository failure is `OPERATIONAL_FAILURE`, not a scientific result.
5. Comparator identity/degeneracy is distinct from PASS and FAIL.
6. Never generalize the result of one concrete action/truncation/paper/realization to an entire research programme.
7. Never fill an unpublished propagator, source rule, vertex, Ward object, retarded object, or observable map with an arbitrary assumption.
8. Every status change must name the exact gate and the evidence that changed it.
9. `BLOCKED` never means invalidated.
10. Do not reconstruct frozen Q1–Q7 or comparator definitions from memory. Read literal repository authority. If the authority path cannot be recovered, record a blocker instead of guessing.

Allowed terminal/status vocabulary:
- `PASS_RQIR_GATE`
- `FAIL_RQIR_CONSISTENCY`
- `EXACT_COMPARATOR_IDENTITY`
- `OPERATIONALLY_DEGENERATE`
- `ROBUST_NONZERO_RESIDUAL`
- `BLOCKED_MISSING_REQUIRED_OBJECT`
- `BLOCKED_PROTOCOL_MISMATCH`
- `OPERATIONAL_FAILURE`

## 3. Authority precedence

When artifacts disagree, use this precedence:

`frozen RQIR protocol > immutable per-model result/evidence > latest immutable RECOVERY_DELTA > CURRENT_BENCHMARK_FRONT > narrative research_log`

Never silently repair a conflict. Record the discrepancy in a new recovery delta, identify which higher-authority artifact wins, and preserve the conflicting evidence for audit.

Candidate Gravity `main` is an external moving authority. The benchmark branch base SHA and the latest observed Candidate Gravity authority SHA are different concepts and MUST both be recorded.

## 4. Required artifact map

- `known_models_benchmark/README.md` — scope, queue, status ontology.
- `known_models_benchmark/protocol/FROZEN_RQIR_PROTOCOL_REFERENCE.md` — literal paths/hashes and recovered frozen definitions; unresolved items remain explicitly unresolved.
- `known_models_benchmark/protocol/BACKUP_AND_RECOVERY_METHOD.md` — this recovery method.
- `known_models_benchmark/models/<model>/audit.md` — human-readable gate-by-gate audit.
- `known_models_benchmark/models/<model>/result.json` — machine-readable result.
- `known_models_benchmark/matrices/benchmark_matrix.csv` — one row per concrete realization.
- `known_models_benchmark/logs/research_log.md` — chronological narrative log.
- `known_models_benchmark/recovery/CURRENT_BENCHMARK_FRONT.md` — concise current frontier.
- `known_models_benchmark/recovery/RECOVERY_DELTA_NNN.md` — immutable per-iteration recovery deltas.
- `known_models_benchmark/recovery/state.json` — machine-readable continuation state.
- `known_models_benchmark/recovery/RESTORE_FROM_NEW_CHAT.md` — shortest fresh-session recovery instructions.

## 5. Mandatory per-model data contract

For every concrete model/version/paper store:

- exact realization and citation
- action/equations
- validity regime
- degrees of freedom
- GR/classical limit
- propagator/poles/cuts
- ghosts/tachyons
- gauge/Ward structure
- causal/retarded structure
- source rule
- nonlinear vertices if published
- Q1–Q7 observable fingerprint
- mapping into frozen RQIR observables
- comparator span
- residual after quotient
- degeneracies
- missing information
- first blocking/failing gate
- final status

## 6. First benchmark queue

1. General Relativity — 4D Einstein–Hilbert, Lambda=0, weak-field Minkowski sector (null control).
2. GR + low-energy quantum-gravity EFT — concrete Donoghue/Burgess-type low-energy EFT realization.
3. Semiclassical gravity — concrete expectation-value/backreaction realization.
4. Stochastic gravity — concrete Einstein–Langevin/noise-kernel realization.
5. f(R) gravity — concrete action/parameter realization.
6. Scalar–tensor / Brans–Dicke — concrete realization.
7. Quadratic / Stelle gravity — concrete fourth-derivative realization.
8. Higher-curvature gravity — concrete EFT/action realization, not a class label.
9. String-theory low-energy/scattering corrections — concrete amplitude/effective-action realization, not 'string theory as a whole'.

Later expansion: nonlocal gravity; asymptotic safety; massive gravity; bigravity; Hořava–Lifshitz; concrete LQG/spinfoam realizations; group field theory; CDT; causal sets; emergent/hybrid gravity; collapse-based quantum-classical gravity; noncommutative-geometry gravity.

## 7. Controls

The suite must demonstrate correct recognition of:
- null control: GR / exact comparator baseline if literal identity is verified;
- positive controls: known extra DOF/poles;
- pathological controls: known ghost/positivity/causality problems.

Candidate Gravity must not be interpreted until the benchmark can reliably distinguish these cases under the same frozen funnel.

## 8. Checkpoint procedure after every significant research iteration

1. Re-read frozen protocol authority and current benchmark state.
2. Re-check the latest Candidate Gravity `main` authority SHA/iteration without rebasing the benchmark silently.
3. Gather authoritative published evidence for the current concrete realization.
4. Update the model `audit.md`.
5. Update the model `result.json`.
6. Update `benchmark_matrix.csv`.
7. Append `research_log.md`.
8. Create a NEW immutable `RECOVERY_DELTA_NNN.md`; never overwrite an older delta.
9. Replace `CURRENT_BENCHMARK_FRONT.md` with the new frontier.
10. Replace `state.json` with the new continuation state.
11. Verify that percentages, completed count, rollup counts, and next actions agree across all artifacts.

## 9. Fresh-chat restoration procedure

A new chat/session must perform these steps in order:

1. Open this repository and use branch `rqir7-known-models-benchmark`.
2. Read this file completely.
3. Read `recovery/CURRENT_BENCHMARK_FRONT.md`.
4. Read `recovery/state.json`.
5. Read the latest `recovery/RECOVERY_DELTA_NNN.md`.
6. Read `protocol/FROZEN_RQIR_PROTOCOL_REFERENCE.md` and verify every referenced frozen authority path/hash that is needed for the next gate.
7. Read the current model's `audit.md` and `result.json`.
8. Verify the benchmark branch HEAD and separately fetch current Candidate Gravity `main` HEAD/front.
9. Execute the `next_actions` field from `state.json` in order.
10. Do not redo completed work unless the recovery check finds corruption, evidence conflict, changed external source, or an explicitly reopened gate.

A minimal prompt in a new chat can therefore be: **'Продолжай RQIR7 из репозитория; восстановись строго по known_models_benchmark/protocol/BACKUP_AND_RECOVERY_METHOD.md.'** No other chat context should be required.

## 10. Git/SHA recording convention

A file cannot know the SHA of the commit that will contain itself before that commit exists. Therefore `state.json` records:
- `base_main_sha`: immutable benchmark branch base;
- `candidate_gravity_authority.sha`: latest observed moving `main` authority;
- `state_written_from_branch_sha`: benchmark branch HEAD immediately before writing that state.

After writes complete, fetch the resulting benchmark branch HEAD. The next recovery delta records that resulting HEAD as the prior/checkpoint SHA. This avoids circular self-hashing claims.

## 11. Scientific citation discipline

- Prefer original papers, peer-reviewed journals, arXiv versions of original/review papers, and established Living Reviews.
- Record exact realization/version and validity regime.
- Separate source facts from RQIR interpretation.
- For a disputed/ambiguous claim, preserve competing interpretations and do not upgrade to FAIL/PASS without gate-level evidence.
- For a model family, benchmark each concrete realization separately.

## 12. Current recovery checkpoint at initialization

Benchmark readiness: 10% before this backup iteration.
Current model: 4D Einstein–Hilbert GR, Lambda=0, weak-field Minkowski sector.
Current model check: 40% before this backup iteration.
Completed: 0/9.
Rollup: PASS 0; FAIL 0; BLOCKED 0; DEGENERATE 0 final.

Known GR scientific evidence already being checked: Einstein equations admit hyperbolic harmonic formulations; linearized gravitational response admits retarded Green functions; the realization is the intended null control. Exact `EXACT_COMPARATOR_IDENTITY` remains provisional until literal frozen comparator/Q1–Q7 containment is recovered from repository authority.

## 13. Immediate continuation targets

1. Recover literal frozen Q1–Q7 definitions and comparator span from repository authority; do not infer them.
2. Complete GR gate-by-gate audit.
3. If exact Einstein–Hilbert baseline identity is proved, freeze GR as `EXACT_COMPARATOR_IDENTITY` with zero quotient residual; otherwise record the exact blocker.
4. Start concrete GR + low-energy quantum-gravity EFT benchmark.
5. Audit repository tree for prior asymptotic-safety/FRG/Reuter comparator work before creating any duplicate audit.
