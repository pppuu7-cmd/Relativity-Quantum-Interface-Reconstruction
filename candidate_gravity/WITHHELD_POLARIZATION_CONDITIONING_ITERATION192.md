# Candidate Gravity — Iteration 192: withheld-v1 polarization conditioning audit

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

Before evaluating any cubic comparator on the preregistered v1 withheld rows, the raw TT projector norms were audited along the soft path.

Eleven rows pass. `W05` does not: its partner raw norm changes sign between the soft limit and the frozen positive soft steps, with `n(0)=-6.149186e-4` and `n(0.000625)=+2.930728e-3`. Therefore the normalized polarization crosses a projector zero before the soft limit and its cubic soft extrapolation is invalid.

The row is not silently dropped or reseeded. The seed-independent K2 result of Iteration 191 remains valid.

Retain `NUM-NG-006`, `PROTO-NG-002`, `NG-FUNNEL-047`.

`MODEL_READINESS: 24%` — unchanged.
