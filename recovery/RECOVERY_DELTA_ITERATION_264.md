# RECOVERY DELTA — Candidate Gravity Iteration 264

**Date:** 2026-09-02  
**Authoritative iteration:** 264  
**MODEL_READINESS: 24%**

## Delta from Iteration 263

Iteration 263 reduced the physical projected cubic numerator to `E1/E2/E3` plus `K0/K1/K2`. Iteration 264 directly constructs the nonlinear Einstein EOM side of that library on a physical polarized three-leg TT family.

For `g=eta+t_s h_s+t_a h_a+t_b h_b`, multilinear amplitude derivatives of the exact Einstein tensor define `E2[x,y]` and `E3[x,y,z]` with no factorial convention. The soft leg is null and TT and satisfies `E1[s]=0` to numerical precision; the two hard legs are distinct spacelike TT modes.

At finite-difference step `3e-4`:

- `||E2[s,a]||_F = 0.7456115521460782`;
- `||E2[s,b]||_F = 0.7140951693123437`;
- `||E2[a,b]||_F = 0.6270097790259529`;
- `||E3[s,a,b]||_F = 0.5815260517855062`;
- `max|E3[s,a,b]| = 0.4644883431881889`.

The values converge stably over steps `1e-2 ... 3e-4`. All-six-leg permutation mismatch of `E3` is `4.39e-10` and output-tensor symmetry mismatch is `1.57e-10` at `3e-4`.

Freeze:

`PASS_SCOPED_POLARIZED_EINSTEIN_E2_E3_NONZERO_AND_SYMMETRIC`

Guardrail:

`DO_NOT_ZERO_E2_OR_E3_FROM_E1_SOFT_ZERO`

This establishes that the six surviving projected `A3[s,a,b]` partitions from Iteration 263 contain genuinely nontrivial Einstein-EOM input. In particular `K0E3` and surviving `K1E2` pieces are not eliminated by `E1[s]=0`.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

This remains operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 263: **0 percentage points**. The nonlinear Einstein EOM portion of the polarized physical numerator is now explicitly nonzero and symmetry-checked, but physical `K/A`, `Q` dressing, tensor reduction and the complete C5 comparator coordinate remain open. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Build physical `K0/K1/K2` from frozen `R0/R1`, `P=partial R`, and `Gamma0/Gamma1/Gamma2` on the same three-leg family, then assemble `A1/A2/A3` with the now-certified `E1/E2/E3`. Derive polarized `N1/N2` and `Q1/Q2` from the same orbit metric, then assemble all 15 surviving null-soft `B3[s,a,b]` terms. Tensor reduction remains forbidden until a nonzero physical numerator exists; Fisher/resources, blind heavy integration and `ANSATZ-003` remain forbidden.
