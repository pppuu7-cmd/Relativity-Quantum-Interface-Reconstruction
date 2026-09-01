# RQIR Candidate Gravity — Iteration 249

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Purpose

Iteration 248 established that the mixed nonlinear Einstein response `G^(2)[h_s,h_h]` is nonzero for an explicit null-soft TT mode and a spacelike hard TT mode. Iteration 249 asks whether the same response is removed by the frozen TT contractions.

## Result

Using the same deterministic configuration and symmetric amplitude steps:

| step | soft-TT contraction | hard-TT contraction |
|---:|---:|---:|
| `1e-2` | `0.5742616679` | `-0.3445707495` |
| `3e-3` | `0.5741509147` | `-0.3444917857` |
| `1e-3` | `0.5741411794` | `-0.3444848451` |
| `3e-4` | `0.5741400721` | `-0.3444840556` |

Both contractions converge to finite nonzero values.

Therefore the nonlinear mixed Einstein EOM sector is not removed merely by the TT projection used in the null-soft protocol.

## Classification

`PASS_SCOPED_NONLINEAR_EINSTEIN_MIXED_RESPONSE_SURVIVES_TT_PROJECTION`.

Retain guardrail:

`DO_NOT_ASSUME_TT_PROJECTION_ELIMINATES_VD_E1_E2_NONLINEAR_EOM_SECTORS`.

This remains a scoped structural certificate, not a full Vilkovisky one-loop comparator column. The actual coefficients and discontinuity require the same-parent Vilkovisky connection/kernel, source/Ward completion and causal projection.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

## Next gate — Iteration 250

Use the Iterations 245–247 topology/order reduction plus the Iterations 248–249 nonlinear-EOM certificates to classify which surviving `e=1` and `e=2` cubic terms require genuinely new loop integrals versus algebraic/contact/source completions. The goal is to minimize the remaining gauge-safe C5 calculation before any heavy symbolic implementation.
