# Research Log — Candidate Gravity Iteration 297

Date: 2026-09-03

Authoritative input: Iteration 295 direct timelike weight-completed `Tr U1` all-family numerator reconstruction. Iteration-296 bubble DR Action was active during this independent audit and was not duplicated.

## Result

Static audit of `candidate_gravity/code/iteration296_timelike_tru1_bubble_dr_laurent.py` shows that it reconstructs/evaluates the numerator in four loop-momentum components and uses a four-dimensional Minkowski Laplacian, while scalar loop integration is analytically continued to `D=4-2 epsilon`.

This implements a specific 4D-numerator/D-dimensional-measure prescription. The repository does not yet contain an authoritative same-parent D-dimensional continuation of the numerator algebra or an explicit finite conversion map from this prescription to the comparator convention.

Four-dimensional loop samples do not identify evanescent `mu^2=-l_{[-2 epsilon]}^2` numerator structures. Therefore absence of such structures in the Iteration-295 4D oracle is not an exact-zero statement. They may affect finite rational/local terms after dimensional integration even when invisible on 4D samples.

Frozen classification:

`PASS_SCOPED_DR_NUMERATOR_CONTINUATION_INTERFACE_AUDIT__FULL_FINITE_REMAINDER_BLOCKED_BY_EVANESCENT_SCHEME_AUTHORITY`

Guardrail:

`DO_NOT_PROMOTE_4D_ORACLE_DR_FINITE_REMAINDER_TO_SCHEME_INDEPENDENT_SAME_PARENT_RESULT_WITHOUT_EVANESCENT_CONTINUATION_OR_EXPLICIT_SCHEME_CONVERSION`

The active Iteration-296 discontinuity calculation is not invalidated. When it completes, its cut/log result may be accepted only with the explicit 4D-numerator/D-measure prescription label until the regulator-conversion issue is closed.

This is operational/regulator BLOCKED for the full finite remainder; it is not a consistency FAIL, comparator identity, near-degeneracy, or novelty certificate.

## Readiness rubric

- comparator foundation: 24/25
- unique residual discovery: 0/20
- frozen parent dynamics/ANSATZ: 0/20
- consistency/positivity/Ward/causality: 0/15
- identifiability/Fisher: 0/10
- resource/experiment closure: 0/10

MODEL_READINESS: 24%

Change from Iteration 295: 0 percentage points. The audit prevents an overclaim but closes no additional model-readiness block.

## Next gate

Audit the active Iteration-296 bubble Action result when complete; retain its discontinuity in the declared 4D-numerator/D-measure scheme. Before promoting a complete DR finite hard remainder, establish a same-parent D-dimensional numerator continuation or explicit scheme-conversion/counterterm map. Then reduce the timelike triangle families in the same convention and combine all eight `e=1,c=2` families.
