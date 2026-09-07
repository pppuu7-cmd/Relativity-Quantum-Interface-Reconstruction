# RQIR7 — Known Models / Quantum Gravity Benchmark

Purpose: audit concrete gravity and quantum-gravity realizations through the same frozen RQIR funnel used for Candidate Gravity.

Branch: `rqir7-known-models-benchmark`
Base main SHA: `02ad31e89f1df0d5515779e6b7526e8eb5505667`
Recovery entrypoint: `recovery/RESTORE_FROM_NEW_CHAT.md`

## First queue

| # | Concrete target | Control role | State |
|---|---|---|---|
| 1 | 4D Einstein–Hilbert GR, Lambda=0, weak-field Minkowski sector | null control | active audit |
| 2 | GR + low-energy quantum-gravity EFT, concrete Donoghue/Burgess realization | EFT/comparator control | queued |
| 3 | Semiclassical gravity, concrete realization | source/backreaction control | queued |
| 4 | Stochastic gravity, Einstein–Langevin/noise-kernel realization | fluctuation control | queued |
| 5 | concrete f(R) gravity | extra-DOF control | queued |
| 6 | concrete Brans–Dicke/scalar–tensor | extra-scalar control | queued |
| 7 | Stelle quadratic gravity | pathological-pole control | queued |
| 8 | concrete higher-curvature EFT/action | EFT positive control | queued |
| 9 | concrete string low-energy/scattering realization | QG/EFT control | queued |

## Status vocabulary

`PASS_RQIR_GATE`, `FAIL_RQIR_CONSISTENCY`, `EXACT_COMPARATOR_IDENTITY`, `OPERATIONALLY_DEGENERATE`, `ROBUST_NONZERO_RESIDUAL`, `BLOCKED_MISSING_REQUIRED_OBJECT`, `BLOCKED_PROTOCOL_MISMATCH`, `OPERATIONAL_FAILURE`.

BLOCKED is never scientific invalidation.

## Mandatory output table

Every concrete realization must ultimately populate: exact realization/paper; action/equations; regime; DOF; GR limit; poles/cuts; ghosts/tachyons; gauge/Ward; causal/retarded structure; source rule; nonlinear vertices; Q1–Q7 fingerprint; frozen-observable mapping; comparator span; quotient residual; degeneracies; missing objects; first blocking/failing gate; final status.
