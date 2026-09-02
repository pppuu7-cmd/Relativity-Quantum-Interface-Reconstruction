# RECOVERY DELTA — Candidate Gravity Iteration 265

**Date:** 2026-09-02  
**Authoritative iteration:** 265  
**MODEL_READINESS: 24%**

## Delta from Iteration 264

Iteration 264 certified nonzero physical polarized `E2/E3`. Iteration 265 closes the remaining exact bookkeeping for the projected same-parent `K0/K1/K2` library before any physical tensor reduction.

Retain frozen dynamics:

`K = R (P + Gamma R)`,

with affine `R=R0+R1[h]`, background-independent `P=partial R`, and `Gamma` polarized only through `Gamma2` for this cubic route.

Exact polarization gives:

- `K0`: 2 primitive contractions;
- `K1[x]`: 4 primitive contractions;
- `K2[x,y]`: 7 primitive contractions.

No `R2`, `R3`, or `Gamma3` enters physical projected `A3`.

With frozen `E1[s]=0`,

`A3[s,a,b] = K0E3[s,a,b] + K1[s]E2[a,b] + K1[a]E2[s,b] + K1[b]E2[s,a] + K2[s,a]E1[b] + K2[s,b]E1[a]`,

so the physical projected cubic target has exactly

`2 + 3*4 + 2*7 = 28`

primitive contractions before further tensor/momentum/source-projection cancellations.

Freeze:

`PASS_EXACT_POLARIZED_K0_K1_K2_PRIMITIVE_LIBRARY_2_4_7`

`PASS_EXACT_NULLSOFT_PROJECTED_A3_PRIMITIVE_COUNT_28`

Guardrail:

`NO_R2_R3_GAMMA3_IN_PHYSICAL_PROJECTED_A3`

A reproducible noncommuting-matrix regression confirms the polarized formulas by centered finite differences; at `h=1e-4`, `K1` mismatch is `2.6320710944e-7` and mixed `K2` mismatch is `2.3047781283e-7`, with quadratic convergence from larger steps.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

This remains operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 264: **0 percentage points**. The projected `K` vertex space is now exact and finite, but physical contracted `A/B3`, orbit-metric dressing, tensor reduction and the final C5 comparator coordinate remain open. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Instantiate the 2/4/7 `K0/K1/K2` primitives as physical condensed-index/Fourier kernels on the frozen three-leg family, contract them with certified `E1/E2/E3` to obtain explicit physical `A1/A2/A3`, derive physical polarized `N1/N2` and `Q1/Q2` only from the same orbit metric/exact recursion, and then assemble the 15 surviving null-soft `B3[s,a,b]` terms. Tensor reduction remains forbidden until a nonzero physical `B3` exists; Fisher/resources, blind heavy integration and `ANSATZ-003` remain forbidden.
