# RQIR research log — Iteration 253

Date: 2026-09-02

Recovered the factual authoritative front at Iteration 252 from recent commits/recovery, despite `CURRENT_QG_FRONT.md` still showing 251. No active GitHub Actions runs were present.

Before differentiating the remaining `delta[R.(D R)] E^(2)` kernel, audited the exact Ward identity of the same Vilkovisky parent. Gauge invariance `E_j R^j_delta=0` and the torsion-free field-space derivative imply

`R^i_gamma (D_i R^j_delta) E_j = -R^i_gamma R^j_delta (D_i E_j)`.

Thus the complete `A_gamma_delta[E]` is symmetric in `gamma,delta`. However, at total cubic background order, with `K=R.(D R)=K0+tK1+t^2K2+...` and `E=tE1+t^2E2+t^3E3+...`, the constrained object is

`K0 E3 + K1 E2 + K2 E1`,

not `K1 E2` alone. A reproducible SymPy bookkeeping certificate returns `partition_match=true`.

Freeze `PASS_SCOPED_CUBIC_WARD_PARTITION_AUDIT` and `NO_STANDALONE_CUBIC_WARD_FAIL_FROM_E2K1_PARTITION`.

This prevents a false consistency FAIL from testing only the Iteration-252 middle partition. The explicit `delta[R.(D R)] E^(2)` term is still required, but its immediate checks must be local/index-orientation/TT checks; a final Ward/symmetry certificate waits for same-parent `K0E3` and `K2E1` assembly.

Umbrella C5 status remains `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`, `BLOCKED_NOT_ZERO`.

MODEL_READINESS: 24%

Change from Iteration 252: 0 percentage points. The Ward target was corrected and sharpened, but no physical comparator coordinate or robust residual closed.

Next gate: derive explicit `delta[R(DR)]E2`, combine with both `delta Nhat^-1` placements and `delta Y^up`, and prepare the missing sibling cubic partitions before any final Ward PASS/FAIL or heavy integration.
