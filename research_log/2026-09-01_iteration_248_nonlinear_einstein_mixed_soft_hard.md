# RQIR Research Log — Iteration 248

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

Iteration 247 showed that only the three-EOM (`e=3`) cubic Vilkovisky sector is guaranteed to vanish from the linear null-soft equation. Iteration 248 tests the first nonlinear obstruction explicitly.

A null-soft TT plane wave and a spacelike hard TT plane wave are inserted into the exact Einstein tensor. The mixed amplitude derivative `d^2G/(da db)|_0` is extracted by symmetric finite differences.

The mixed nonlinear Einstein tensor converges to a clearly nonzero value: Frobenius norm `~0.73165745`, maximum absolute component `~0.46268487` at the finest step. The frozen nullness, transversality and tracelessness checks pass.

Retain:

- `VD-NG-001 — LINEAR_NULL_SOFT_EOM_DOES_NOT_KILL_MIXED_NONLINEAR_EINSTEIN_RESPONSE`;
- `VD-GUARD-001 — DO_NOT_ZERO_E1_E2_VILKOVISKY_SECTORS_FROM_E1_SOFT_ZERO`.

Classification: `PASS_SCOPED_NONLINEAR_EINSTEIN_MIXED_SOFT_HARD_NONZERO`.

No Candidate Gravity residual is produced. `MODEL_READINESS: 24%` remains unchanged.

Next: Iteration 249 should contract the surviving nonlinear EOM building blocks with the declared Vilkovisky connection/kernel structure and apply the frozen TT/source/Ward projection before any causal-cut claim.
