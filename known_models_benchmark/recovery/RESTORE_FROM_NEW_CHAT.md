# RQIR7 — Restore from a New Chat

This file is the shortest recovery entrypoint. It intentionally assumes no usable chat memory.

## Required order

1. Use repository `pppuu7-cmd/Relativity-Quantum-Interface-Reconstruction`.
2. Select branch `rqir7-known-models-benchmark`.
3. Read `known_models_benchmark/protocol/BACKUP_AND_RECOVERY_METHOD.md` completely.
4. Read `known_models_benchmark/recovery/CURRENT_BENCHMARK_FRONT.md`.
5. Read `known_models_benchmark/recovery/state.json`.
6. Read the highest-numbered immutable `known_models_benchmark/recovery/RECOVERY_DELTA_NNN.md`.
7. Read `known_models_benchmark/protocol/FROZEN_RQIR_PROTOCOL_REFERENCE.md`.
8. Read the current model's `audit.md` and `result.json`.
9. Fetch current `main` and `candidate_gravity/recovery/CURRENT_QG_FRONT.md` separately; do not confuse moving Candidate Gravity authority with the benchmark branch base.
10. Resume from `next_actions` in `state.json`.

## Hard constraints

- Never reconstruct frozen gates/Q1–Q7/comparator rules from chat memory.
- Never silently change a frozen gate.
- Never equate BLOCKED with FAIL.
- Never generalize a concrete realization to a whole model family.
- Never invent missing published objects.
- Every final status must be one of the RQIR7 allowed status strings documented in `BACKUP_AND_RECOVERY_METHOD.md`.

## Minimal new-chat instruction

`Продолжай RQIR7 из репозитория. Восстанови состояние строго по known_models_benchmark/recovery/RESTORE_FROM_NEW_CHAT.md и не опирайся на старый чат.`
