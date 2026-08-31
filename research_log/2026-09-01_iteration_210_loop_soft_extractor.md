# Research Log — RQIR Iteration 210

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Executable regular+log soft extraction gate completed.

Frozen 12-point geometric grid: `epsilon in [0.0003125, 0.04]`, dynamic range 128.

One-loop basis through `n=2`: `[1,L,z,zL,z^2,z^2L]`.

Results:

- matrix rank `6/6`;
- condition number `4264.620104`;
- synthetic regular+log coefficient recovery relative error `1.28e-14`;
- synthetic fit residual `4.19e-16`;
- equal-parameter-count pure-Taylor degree-five fit leaves relative residual `0.0190592` (~1.91%);
- deterministic `1e-8` relative input perturbation produces about `1.02e-5` relative coefficient error.

Thus the new loop-soft basis is numerically executable and distinguishable from a naive Taylor basis, but physical import requires an explicit error envelope.

No physical C5 cut imported yet. No Candidate Gravity residual. `ANSATZ-003` remains uncreated; Fisher/resources forbidden.
