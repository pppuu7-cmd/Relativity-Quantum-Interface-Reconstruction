# C5 Vilkovisky polarized Einstein E2/E3 — Iteration 264

**Date:** 2026-09-02  
**Frozen parent:** 4D Einstein gravity, Lambda=0; Vilkovisky field-space convention a=-1/2 remains unchanged.  
**MODEL_READINESS: 24%**

## Purpose

Iteration 263 reduced the projected cubic numerator to E1/E2/E3 and K0/K1/K2. This iteration closes a scoped existence/consistency certificate for the physical multilinear Einstein EOM coefficients E2[x,y] and E3[s,a,b] using the exact Einstein tensor of one null-soft TT mode s and two distinct hard TT modes a,b.

For g=eta+t_s h_s+t_a h_a+t_b h_b, define the polarized coefficients by amplitude derivatives at zero:

E2[x,y] = d_x d_y G[g]|_0,

E3[x,y,z] = d_x d_y d_z G[g]|_0.

No factorial convention is inserted: these are multilinear derivatives, matching the polarized bookkeeping of Iterations 261-263.

## Frozen test family

The soft mode has k_s^2=0 and TT polarization, so E1[s]=0 to numerical precision. The hard modes are distinct spacelike TT directions with k_a^2=0.41 and k_b^2=0.4425.

Centered mixed finite differences of the exact nonlinear Einstein tensor give, at h=3e-4:

- ||E2[s,a]||_F = 0.7456115521460782, max component = 0.33052484055474385;
- ||E2[s,b]||_F = 0.7140951693123437, max component = 0.3421616284259116;
- ||E2[a,b]||_F = 0.6270097790259529, max component = 0.4093332795822131;
- ||E3[s,a,b]||_F = 0.5815260517855062, max component = 0.4644883431881889.

The values converge stably as h decreases from 1e-2 to 3e-4. The soft linear coefficient remains zero: max|E1[s]|=2.99e-18 at h=3e-4.

The cubic coefficient is symmetric under all six external-leg permutations within numerical error: max permutation residual 4.39e-10 at h=3e-4. Its output tensor symmetry residual is 1.57e-10.

## Scientific classification

Freeze:

`PASS_SCOPED_POLARIZED_EINSTEIN_E2_E3_NONZERO_AND_SYMMETRIC`

Guardrail:

`DO_NOT_ZERO_E2_OR_E3_FROM_E1_SOFT_ZERO`

This is stronger than the earlier existence-only mixed-soft-hard check: both E2 and the genuinely three-leg E3 are now directly extracted from the same exact Einstein dynamics with distinct external legs and verified to respect multilinear leg symmetry.

It is still not a complete symbolic tensor library, not the final C5 comparator coordinate, not a Candidate-vs-GR identity, and not a Candidate Gravity residual.

## Consequence for projected A3

For the physical null-soft A3[s,a,b], the K0 E3[s,a,b] contribution is demonstrably not forced to vanish by E1[s]=0. Likewise surviving K1 E2 partitions cannot be discarded by the linear soft equation alone. The Iteration-263 six-term projected A3 target is therefore genuinely nontrivial.

## Reproducibility

- `candidate_gravity/code/iteration264_polarized_einstein_e2_e3.py`
- `candidate_gravity/results/iteration264_polarized_einstein_e2_e3.json`

## Exact next gate

Use frozen Gamma0/Gamma1/Gamma2 with R0/R1 and P=partial R to construct physical K0/K1/K2 on the same three-leg family, then assemble projected A1/A2/A3 using the now-certified E1/E2/E3. In parallel construct polarized N1/N2 and Q1/Q2 from the same orbit metric. Then assemble the 15 surviving null-soft B3 terms. Tensor reduction remains forbidden until this physical numerator is explicitly nonzero.
