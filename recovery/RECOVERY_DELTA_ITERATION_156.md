# Recovery Delta — RQIR Iteration 156

**Date:** 2026-08-31  
**Authoritative change:** first fixed nonlinear C4 comparator instantiated from standard dRGT massive gravity; its scoped TT tree tangent has rank `2/2` and expands the currently implemented C5 local nonlinear span from rank 2 to rank 4.

## Previous front

Iteration 155 established that the fixed PQCG comparator has a nonzero tree causal nonlinear response, but this response is a common GR-boundary contribution and adds zero `(D2,D0)` rank. Diffusion-dependent ordered C3 corrections remain BLOCKED.

## Fixed C4 realization

`C4-DRGT-001` uses

`S=M_Pl^2/2 int sqrt(-g)[R + m^2/2(L2[K]+alpha3 L3[K]+alpha4 L4[K])] + S_m[g]`,

`K=I-sqrt(g^{-1}eta)`,

with `alpha0=alpha1=0`, `alpha2=1`, Minkowski reference metric and minimal matter coupling.

Literature-established dRGT ghost freedom is treated as comparator authority, not a new project proof.

Frozen point:

`m^2=0.04`, `alpha3=0`, `alpha4=0`.

Tangent parameters:

`(log m^2,alpha3)`.

## Cubic TT structure

For TT `H=eta h`,

`L2^(3)=3/4 Tr(H^3)`,

`L3^(3)=1/4 Tr(H^3)`,

so

`V3_dRGT=m^2(3+alpha3)/8 Tr(H^3)`.

`alpha4` is blind at cubic TT order because `L4` begins quartically.

## Numerical tangent

On the same six frozen spacelike TT probes:

`rank(V_C4)=2/2`.

Singular values:

`[3.062684454379795,0.4175708275716087]`.

`smin/smax=0.13634144772501477`.

## Comparison to existing local C5 block

The current Ward-validated C5 local response block contains two columns (`Ricci^3`,`Riemann^3`).

Projecting the dRGT tangent onto this C5 span leaves nonzero residuals:

- residual norms approximately `[0.57999745,0.09656019]`;
- residual fractions approximately `[0.19275682,0.13647969]`.

The combined matrix `[V_C5_local,V_C4_dRGT]` has rank **4** with singular values

`[5.62719921,1.53092825,0.39407597,0.06156025]`.

This only proves independence from the **implemented two-column local C5 R^3 span**, not from full C5 EFT.

## New retained results

### `C4-NG-001 — ALPHA4_CUBIC_TT_BLIND`

The cubic TT protocol cannot identify `alpha4`. Classification: regime/order-specific non-identifiability.

### `C4-NG-002 — DRGT_EXPANDS_SCOPED_NONLINEAR_COMPARATOR_SPAN`

At the frozen reference point, `(log m^2,alpha3)` gives two independent nonlinear-response directions and expands the currently implemented C5+C4 rank from 2 to 4.

Classification: positive comparator result, not Candidate Gravity novelty.

## Blocked sectors

- helicity-0/helicity-1 finite RQIR completion: BLOCKED;
- Vainshtein/nonperturbative completion: BLOCKED;
- C4 `N2/C3sym`: BLOCKED;
- alpha4 higher-point direction: BLOCKED_AT_CUBIC_ORDER;
- full C4 quotient: BLOCKED;
- C5 higher local and loop/nonanalytic: BLOCKED;
- C3 diffusion-dependent ordered response: BLOCKED.

`ANSATZ-003`: NOT_CREATED.  
Fisher/resources: FORBIDDEN.

## New files

- `analysis/c4_drgt_nonlinear_tangent_iteration156.py`
- `results/c4_drgt_nonlinear_tangent_iteration156.json`
- `candidate_gravity/comparators/C4-DRGT-001.md`
- `research_log/2026-08-31_iteration_156_c4_drgt_nonlinear_tangent.md`
- `recovery/RECOVERY_DELTA_ITERATION_156.md`

## Literature anchors

- de Rham, *Massive Gravity*, Living Rev. Relativity 17, 7 (2014).
- Hassan & Rosen, arXiv:1106.3344.
- de Rham, Gabadadze & Tolley, arXiv:1107.3820; arXiv:1108.4521.

## Exact restart instruction — Iteration 157

Before interpreting the C4 residual as a robust comparator-space enlargement, complete a shared-boundary quotient audit:

1. include the common EH response direction explicitly;
2. project out overall gain/common normalization consistently;
3. verify the dRGT residual rank is stable under reasonable coordinate normalization of the six-probe observable vector;
4. if robust, proceed to one fixed nonlocal/form-factor action or one fixed asymptotic-safety truncation;
5. if the rank collapses, record the degeneracy and update the comparator matrix;
6. no `ANSATZ-003`, Fisher or resource optimization yet.
