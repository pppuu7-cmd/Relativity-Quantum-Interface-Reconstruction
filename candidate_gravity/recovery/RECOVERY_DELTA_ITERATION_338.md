# RQIR Candidate Gravity Recovery Delta — Iteration 338

Date: 2026-09-03

MODEL_READINESS: 24%

## Authority

Iteration 338 closes the common outer one-loop effective-action prefactor for the physical determinant coordinate already constructed by Iterations 312/319/324/329/331.

Freeze:

`PASS_SAME_PARENT_DETERMINANT_EFFECTIVE_ACTION_OUTER_PLUS_I_PREFactor__TRU1_MINUS_I_OVER_2_CROSSCHECK`

Validated Actions provenance:

- run `33756324238`
- job `100651503806`
- head/workflow commit `cb4ba0dd7ff433a3f879e33a071c8570cb4aec5c`
- code commit `68bfb781b20fed40459112635f5ce0896f61b1d7`
- artifact `9893580250`, `iteration338-result`
- artifact digest `sha256:54eb5733ebfd08afeaccfbe7c775968436136f9ae05f5cbddfee96b53ca86da4`
- scientific JSON SHA-256 `2a0a99466b08ce30ff639739079c97461078e80429b42e92f95c90367f902f6b`
- exactly one top-level JSON object, sentinel `338`, `scientific_authority_pass=true`.

## Same-parent algebra

The frozen/recovered reduced one-loop convention is

`Gamma1 = +(i/2) Tr ln H - i Tr ln N -(i/2)(Tr U1 - Tr U2) -(i/4) Tr U1^2 + O(epsilon^3)`.

Iteration 330/331 builds the physical determinant route coordinate as

`C_det = (1/2) Tr_H - Tr_N`

with the cubic `logdet` topology weights already internal to the route construction.

Therefore the common outer determinant factor is

`Gamma_det = +i * C_det`,

hence

`D_s Gamma_det = +i * D_s C_det`.

This exactly reproduces the independently frozen Iteration-307 connection coefficient `-i/2` for `Tr U1`; the graviton, ghost and `Tr U1` algebraic closure errors are all zero in the scientific artifact.

## Combined normalization consequence with Iteration 337

For an ordinary two-simple-line determinant cut whose normalized angular mean is `m`, Iteration 337 gives

`D_s C_det = -m`.

Iteration 338 therefore gives

`D_s Gamma_det = -i*m`.

This is the normalized determinant effective-action discontinuity conversion in the frozen repository convention. The internal determinant weights `1/2` for the graviton and `-1` for the ghost must not be applied again.

## Scope boundary

Still not frozen:

- the unresolved Iteration-335 `q^2=-1` triangle numerical-convergence result;
- the full finite DR remainder under the Iteration-297 evanescent/scheme warning;
- source/Ward/contact completion;
- matched `K2` subtraction;
- the complete comparator quotient and any comparator-subtracted residual.

No `ANSATZ-003`, Fisher or resource calculation is authorized by this normalization result alone.

## Readiness

MODEL_READINESS remains 24%. This closes another hard determinant prerequisite but does not close a rubric bucket because no robust comparator-subtracted residual yet exists.

## Exact next gate

When Iteration 335 resolves, assemble the complete channel-resolved determinant `D_s Gamma_det` using the frozen `-i * sphere_mean` conversion for each ordinary simple-cut channel, retaining family provenance and the unchanged convergence threshold. If Iteration 335 remains BLOCKED, replace only its angular integration by a symbolic/analytic reduction rather than weakening the threshold.
