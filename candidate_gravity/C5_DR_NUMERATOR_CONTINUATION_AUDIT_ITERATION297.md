# RQIR Candidate Gravity — Iteration 297

## DR numerator-continuation audit after direct timelike TrU1 reconstruction

Date: 2026-09-03

### Scope

This iteration is an independent regulator/interface audit of the Iteration-296 bubble reducer while its numerical GitHub Actions run is still active. It does not duplicate that run and does not import any Iteration-289 weighted-kernel proxy coefficient.

The authoritative numerator input remains Iteration 295: the eight non-scaleless families of the actual weight-completed timelike `[Tr U1]_{sab}` were reconstructed from four-component loop-momentum samples at the frozen `s=0.016` point.

### Finding

The Iteration-296 reducer evaluates the reconstructed numerator as a polynomial in four loop-momentum components, applies the four-dimensional Minkowski Laplacian to that polynomial, but analytically continues the scalar loop measure and Gamma-function factors to

`D = 4 - 2 epsilon`.

That is a definite computational prescription, but the repository has not yet declared it as a regulator scheme nor supplied a same-parent `D`-dimensional continuation of the numerator algebra.

Four-dimensional numerator samples cannot by themselves determine evanescent numerator structures that vanish when the extra `(-2 epsilon)` loop components are set to zero. In a split notation these include terms proportional to powers of `mu^2 = -l_{[-2 epsilon]}^2`. Such terms can be invisible to the Iteration-295 reconstruction while contributing finite rational/local pieces after dimensional integration through `epsilon x (1/epsilon)` mechanisms.

Therefore the following distinction is frozen:

1. The direct timelike four-dimensional numerator reconstruction of Iteration 295 remains valid in its stated scope.
2. The Iteration-296 `+i0/-i0` cut/log calculation can be interpreted in the explicit **4D-numerator / D-dimensional-measure prescription** implemented by the code and can still be used as a scoped discontinuity test once its Action result is audited.
3. A full same-parent covariant DR finite remainder must not be claimed scheme-independent until one of the following is supplied:
   - an explicit `D`-dimensional continuation of the parent `N/A/Y` algebra and reconstruction of its evanescent terms; or
   - a declared four-dimensional-numerator regulator prescription together with the finite conversion/counterterm map needed for comparison to the fixed comparator convention.
4. No `mu^2` term may be set to zero merely because it is absent on the four-dimensional sampling oracle. Absence in the 4D oracle is non-identifiability of the evanescent sector, not an exact zero certificate.

### Classification

`PASS_SCOPED_DR_NUMERATOR_CONTINUATION_INTERFACE_AUDIT__FULL_FINITE_REMAINDER_BLOCKED_BY_EVANESCENT_SCHEME_AUTHORITY`

This is not a Candidate consistency FAIL, not an exact comparator identity, not a near-degeneracy, and not a novelty certificate. It is a regulator-interface BLOCKED result for the full finite remainder.

### Guardrail

`DO_NOT_PROMOTE_4D_ORACLE_DR_FINITE_REMAINDER_TO_SCHEME_INDEPENDENT_SAME_PARENT_RESULT_WITHOUT_EVANESCENT_CONTINUATION_OR_EXPLICIT_SCHEME_CONVERSION`

### Consequence for the active Iteration-296 run

Do not cancel or duplicate the active bubble Action. Audit its scalar calibration, branch conjugacy, Laurent stability and family cuts when it finishes. Its discontinuity result is admissible only with the prescription label above until the evanescent continuation question is closed.

### MODEL_READINESS

MODEL_READINESS: 24%

Change from Iteration 295: 0 percentage points. This iteration closes a regulator-interface ambiguity in the claim language but does not yet close comparator foundation `24/25` or produce a robust unique residual.

### Exact next gate

After the active Iteration-296 bubble run completes:

1. audit its raw epsilon scans and `+i0/-i0` calibration;
2. report bubble discontinuities explicitly as results in the 4D-numerator/D-measure prescription;
3. before promoting any full finite remainder, freeze either a same-parent D-dimensional numerator continuation or a conversion map for the chosen prescription;
4. continue the direct-timelike triangle reduction in exactly the same declared prescription;
5. only after all eight `e=1,c=2` families are combined continue active `e=2,c<=1` and determinant `e=0,c<=3`, then linked source/Ward completion and the fixed comparator quotient.
