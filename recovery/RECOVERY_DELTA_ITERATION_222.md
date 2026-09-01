# Recovery Delta — RQIR Iteration 222

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## New physical factorization

For the gauge-safe `MSSC-001` scalar+graviton cut from Iteration 221, determine each collinear residue locally before any angular integration:

`R = lim_(delta->0) (1-cos delta) I_cut`.

Across five frozen scattering angles and both plus/cross external spin-2 states,

`R_in = R_out = -8 M_Born`

in the stripped Iteration-219/221 normalization.

- max extrapolated error of `R/M_Born` from `-8`: `3.15e-6`;
- max incoming/outgoing mismatch: `3.54e-6`.

No cap-integral fit was used.

## Retained

- `SRC-CUT-003`;
- `IR-NG-006`;
- `NG-FUNNEL-078`.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

## Exact restart instruction

Iteration 223: define

`I_sub(n)=I_cut(n)-R/(1-n.n_in)-R/(1-n.n_out)`

with `R=-8 M_Born` fixed from Iteration 222. Map the local behavior around both singular directions for multiple azimuths. The required pass is that the residual is no worse than `O(1/delta)` so `sin(delta)d(delta) I_sub` is locally integrable. Do not yet call the full hard-remainder integral converged.
