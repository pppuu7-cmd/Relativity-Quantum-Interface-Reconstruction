# RQIR Research Log — Iteration 156

**Date:** 2026-08-31  
**Comparator:** `C4-DRGT-001`  
**Topic:** first fixed nonlinear massive-spin-2 comparator

## Starting point

Iteration 155 closed the tree-level C3 ordered-response question as far as the currently fixed PQCG realization allows: a nonzero classical causal Einstein response exists but is a common GR-boundary contribution, while diffusion-dependent ordered corrections remain BLOCKED. The frozen decision was therefore to move to a concrete nonlinear C4 realization rather than invent C3 loop columns.

## Fixed model

Use standard dRGT massive gravity with Minkowski reference metric:

`S=M_Pl^2/2 int sqrt(-g)[R + m^2/2(L2[K]+alpha3 L3[K]+alpha4 L4[K])] + S_m[g]`,

`K=I-sqrt(g^{-1}eta)`,

with `alpha0=alpha1=0`, `alpha2=1` and minimal matter coupling to `g`.

The dRGT family is used as a literature-established ghost-free nonlinear massive-spin-2 comparator; RQIR does not claim to re-prove its full Hamiltonian constraint structure.

Literature anchors:

- de Rham, Living Rev. Relativity 17, 7 (2014), standard metric action and `L_n` definitions;
- Hassan & Rosen, arXiv:1106.3344, nonlinear Hamiltonian constraint and BD-ghost removal;
- de Rham, Gabadadze & Tolley, arXiv:1107.3820, arXiv:1108.4521.

## Frozen reference point

`m^2=0.04`, `alpha3=0`, `alpha4=0` in protocol units.

Tangent parameters:

`(log m^2,alpha3)`.

The same six spacelike TT triplets, deterministic polarization seeds, physical metric convention and Gaussian windows `(tau,L)=(0.8,0.6)` are retained from the C5 protocol.

## Cubic TT derivation

On TT fields `Tr H=0` for `H=eta h`.

Using

`K=1/2 H - 3/8 H^2 + 5/16 H^3 + ...`,

and standard dRGT normalizations,

`L2^(3)=3/4 Tr(H^3)`,

`L3^(3)=1/4 Tr(H^3)`.

Therefore

`V3_dRGT=m^2(3+alpha3)/8 Tr(H^3)`.

`L4` begins at fourth order, so `alpha4` is invisible in this cubic TT protocol.

## Full tree response

The response combines the EH cubic vertex, the dRGT potential vertex and massive TT propagators `1/(k^2+m^2)`.

At the frozen reference point:

`R=[0.41598902695785883,-1.0421653262124124,-9.30686701147015,-12.449001654539147,4.0683399477607995,-2.3313492002174723]`.

## C4 tangent

`V_C4=dR/d(log m^2,alpha3)` has rank **2/2**.

Singular values:

`[3.062684454379795,0.4175708275716087]`.

`smin/smax=0.13634144772501477`.

## Comparator-span test

Against the existing Ward-validated local C5 two-column `Ricci^3/Riemann^3` tangent:

- dRGT residual norms after C5 projection: approximately `[0.57999745,0.09656019]`;
- residual fractions: approximately `[0.19275682,0.13647969]`;
- combined `[V_C5_local,V_C4_dRGT]` rank: **4**;
- combined singular values: `[5.62719921,1.53092825,0.39407597,0.06156025]`.

Thus the fixed nonlinear C4 realization genuinely expands the **currently implemented scoped** comparator span.

This is not a distinction from the full C5 EFT because higher local and loop/nonanalytic C5 columns remain BLOCKED.

## Retained results

### `C4-NG-001 — ALPHA4_CUBIC_TT_BLIND`

`alpha4` cannot be identified in the cubic TT protocol because `L4` starts at quartic order. This is regime/order-specific non-identifiability, not a failure of dRGT.

### `C4-NG-002 — DRGT_EXPANDS_SCOPED_NONLINEAR_COMPARATOR_SPAN`

At the frozen nonzero-mass point, `(log m^2,alpha3)` yields two independent nonlinear-response directions and raises the combined implemented C5+C4 rank from 2 to 4.

This is a positive comparator result: it narrows the space available to a future Candidate Gravity model.

## Blockers

- helicity-0/1 finite response completion: BLOCKED;
- Vainshtein/nonperturbative completion: BLOCKED;
- C4 `N2/C3sym`: BLOCKED;
- alpha4 higher-point observable: BLOCKED_AT_CUBIC_ORDER;
- full C4 quotient: BLOCKED.

No Fisher/resources and no `ANSATZ-003`.

## Next scientific gate — Iteration 157

Before adding another model, test whether the dRGT residual directions remain independent after adding the **common EH direction** and after reasonable reparameterization/normalization of the six-probe observable space. Then choose the higher-leverage next comparator:

1. if dRGT residual independence is robust, freeze one concrete nonlocal/form-factor action or asymptotic-safety truncation;
2. if it collapses under a correct shared-boundary quotient, record the scoped degeneracy and repair the comparator matrix;
3. do not use broad program labels as tangent columns;
4. keep all still-unimplemented C3/C5 sectors BLOCKED.
