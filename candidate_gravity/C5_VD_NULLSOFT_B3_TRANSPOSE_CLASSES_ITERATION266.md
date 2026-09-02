# Candidate Gravity C5 — null-soft B3 transpose-class reduction (Iteration 266)

**Date:** 2026-09-02  
**Authoritative parent before this iteration:** Iteration 265  
**Frozen convention:** D=4, Lambda=0, DeWitt a=-1/2, same-parent VD dynamics.

## Result

Iteration 261 established that the physical polarized cubic weighted numerator `B3[s,a,b]=[U1 W]_3` has 19 leg-resolved terms, of which four vanish exactly because the frozen null-soft leg obeys `A1[s]=0`, leaving 15 surviving terms. Iteration 260 established exact coefficientwise weighted symmetry for complete same-parent `U1 W`, and Iterations 257-262 fixed symmetric same-parent `Qn` and `An` coefficients with exact inverse recursion.

Those prior exact facts imply a further nontrivial reduction of the physical evaluation burden.

For the surviving null-soft target, the 15 terms split into transpose classes:

1. `Q0 A3[s,a,b] Q0` — self-transpose;
2. `Q1[s] A2[a,b] Q0` paired with `Q0 A2[a,b] Q1[s]`;
3. `Q1[a] A2[s,b] Q0` paired with `Q0 A2[s,b] Q1[a]`;
4. `Q1[b] A2[s,a] Q0` paired with `Q0 A2[s,a] Q1[b]`;
5. `Q2[s,b] A1[a] Q0` paired with `Q0 A1[a] Q2[s,b]`;
6. `Q2[s,a] A1[b] Q0` paired with `Q0 A1[b] Q2[s,a]`;
7. `Q1[s] A1[a] Q1[b]` paired with `Q1[b] A1[a] Q1[s]`;
8. `Q1[s] A1[b] Q1[a]` paired with `Q1[a] A1[b] Q1[s]`.

Therefore the 15 surviving terms contain only

`1 + 7 = 8`

independent transpose representatives.

Equivalently,

`B3[s,a,b] = Q0 A3[s,a,b] Q0 + Sum_{r=1}^7 (X_r + X_r^T)`.

This is an exact consequence of the frozen same-parent symmetry, not a numerical approximation and not a new physical Ward gate. A future transpose mismatch is an implementation/convention regression.

## Freeze

`PASS_EXACT_NULLSOFT_B3_TRANSPOSE_CLASS_REDUCTION_15_TO_8`

Guardrail:

`NO_DOUBLE_EVALUATION_OF_TRANSPOSE_PAIRED_B3_TERMS`

## Scope

This result does **not** construct the missing physical condensed-index `K/A/N/Q` kernels, does not establish a nonzero physical `B3`, does not perform tensor reduction/source projection, and does not produce a Candidate Gravity residual.

The umbrella C5 status remains

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

with `BLOCKED_NOT_ZERO`.

The correct interpretation remains operational/derivational BLOCKED, not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

## Computational consequence

Iteration 267 should instantiate only the 8 independent representatives. The seven partner terms must be reconstructed by transpose rather than recomputed independently. This preserves exact same-parent Ward structure while reducing duplicated condensed-index/Fourier work.
