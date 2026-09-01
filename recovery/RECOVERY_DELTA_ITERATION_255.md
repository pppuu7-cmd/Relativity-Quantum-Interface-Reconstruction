# RECOVERY DELTA — Candidate Gravity Iteration 255

**Date:** 2026-09-02  
**Authoritative iteration:** 255  
**MODEL_READINESS: 24%**

## Delta from Iteration 254

The remaining genuinely new `K1E2` geometric vertex, `deltaGamma`, has been derived in the same frozen parent convention and independently validated.

Primary-authority convention lock:
- physical-space affine connection: `Tscript = Gamma + T`;
- the derivative in published `U1,U2`, `D_i R^j_alpha`, is explicitly formed with configuration-space Christoffel `Gamma`;
- do **not** replace it by `Gamma+T`.

Frozen simple split (`D=4`, `Lambda=0`, `a=-1/2`, `gamma1=1`, `gamma2..6=0`) gives published Christoffel coefficients

`c1=-1, c2=1/4, c3=1/4, c4=-1/8`.

For `delta g=h`, `H=g^-1 h g^-1`, the first variation follows by differentiating the same compact Christoffel tensor. See `candidate_gravity/C5_VD_FIELDSPACE_CHRISTOFFEL_VARIATION_ITERATION255.md` for the explicit formula.

Independent Lorentzian TT 10x10 field-space reconstruction:
- base Christoffel max mismatch `1.81e-10`;
- first variation max mismatch `5.82e-8`;
- analytic input-pair symmetry residual `0.0`.

Freeze:
`PASS_SCOPED_FIELDSPACE_CHRISTOFFEL_FIRST_VARIATION_AND_TT_VALIDATION`.

Retain umbrella blocker:
`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`
`BLOCKED_NOT_ZERO`.

This is operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or absence/presence of a novelty certificate.

The Iteration-253 Ward guardrail is unchanged: only the complete cubic `K0E3+K1E2+K2E1` can receive a final Ward PASS/FAIL.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 254: **0 percentage points**. Comparator foundation `24/25`; unique residual `0/20`; no new rubric block closed.

## Exact next gate

Complete `E^(2)K^(1)` assembly for `Tr U1`: two `delta(Nhat^-1)` placements + `deltaW` + explicit `deltaR` pieces + new `deltaGamma`, in one condensed-index convention; run local/index/TT checks before tensor integration. In parallel construct minimal `K0E3` and `K2E1` siblings so the first cubic Ward certificate applies only to their complete sum.