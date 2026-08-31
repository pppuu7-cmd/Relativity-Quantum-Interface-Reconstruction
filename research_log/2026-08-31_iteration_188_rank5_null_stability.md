# RQIR Research Log — Iteration 188

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

Audited the unique left-null functional of the currently supported conditioned span `span(V4,S_cond)`.

The comparator rank is robustly `5/6`, but the one-dimensional complement is geometrically fragile as a future witness: 94.67% of its squared norm lies on one frozen row. Fixed-seed perturbations at the inherited soft2 error scale rotate the null direction by median `3.13°`, p95 `9.30°`, max `16.83°`.

This is not a residual discovery. It is a protocol-design result.

Retain `NUM-NG-004`, `REL-NG-006`, `NG-FUNNEL-043`.

`MODEL_READINESS: 24%` — unchanged.

Next independent action: freeze a target-independent withheld row extension before any candidate is evaluated.
