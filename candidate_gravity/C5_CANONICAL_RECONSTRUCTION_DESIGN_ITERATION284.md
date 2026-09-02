# C5 canonical reconstruction design — Iteration 284

## Scope
This iteration does **not** claim the p-dependent C5 numerator has been reconstructed. It closes the exact interpolation geometry that must precede that calculation.

The authoritative Iteration-282 rule is applied exactly: if a primitive branch has repeated denominator `(p+v)^2`, define `l=p+v`, hence substitute `p=l-v` in the **same primitive numerator before sector summation**. Because this is an affine translation of loop momentum, it cannot increase polynomial degree. Therefore the Iteration-283 ceilings remain frozen after canonicalization: degree <=4 for raised bubbles and degree <=6 for raised triangles.

## Full-rank finite bases
For a raised bubble, use Lorentz monomials

`(l^2)^a (l.q)^b`, with `2a+b<=4`.

This basis has exactly 9 elements. On the translation-closed physical kinematics, both non-scaleless bubble sectors have full train and held-out rank 9:

- bubble-a, `q^2=0.41`: train rank 9/9, held-out rank 9/9;
- bubble-b, `q^2=0.21`: train rank 9/9, held-out rank 9/9.

For a raised triangle, use

`(l^2)^a (l.q1)^b (l.q2)^c`, with `2a+b+c<=6`.

This basis has exactly 50 elements. For all three canonical raised-index sectors the external two-vector Gram determinant is nonzero (`det G=-0.01`), and deterministic independent train/held-out matrices both have full rank 50/50:

- triangle `(0,0.21)`: rank 50/50;
- triangle `(0,0.41)`: rank 50/50;
- triangle `(0.21,0.41)`: rank 50/50.

The raw condition numbers are recorded in the JSON result. They are diagnostics for numerical fitting, not physical degeneracy claims. In particular, full rank is certified, while coefficient extraction should use scaling/QR/SVD and held-out residuals rather than normal equations.

## Freeze

`PASS_EXACT_CANONICAL_SHIFT_DEGREE_PRESERVATION_AND_FULL_RANK_RECONSTRUCTION_DESIGN`

## Guardrail

`DO_NOT_INTERPRET_FULL_RANK_SAMPLING_AS_NUMERATOR_RECONSTRUCTION; ACTUAL SAME_PARENT PRIMITIVE NUMERATOR_ORACLE_VALUES_AND_HELD_OUT_RESIDUALS_ARE_STILL_REQUIRED`

Classification: exact reconstruction-design PASS only. It is not a Candidate Gravity consistency PASS, comparator identity, regime-specific non-identifiability, near-degeneracy, robust residual, or novelty certificate.

## Consequence
The next computation is now finite and non-ambiguous: evaluate the actual denominator-stripped primitive numerator oracle after the Iteration-282 canonical shifts, sum only within each canonical sector, solve the 9- or 50-dimensional coefficient problem with rank-revealing QR/SVD, and require held-out residuals consistent with the finite-difference/numerical envelope. Only then is tensor/IBP coefficient extraction authorized.
