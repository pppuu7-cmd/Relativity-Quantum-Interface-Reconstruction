# Candidate Gravity — Iteration 174: fixed nonlocal cubic/CTP structural audit

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Comparator:** `QG-NL-EXP-001`  
**Decision:** nonlocal tree relation occupancy structurally closed in the current coarse CTP quotient; no Candidate Gravity residual

## 1. Starting point

Iteration 173 left the fixed PQCG ordered cubic completion honestly BLOCKED because the published conserved-diffusion linear completion does not uniquely fix the nonlinear MSR two-response-field vertex.

The next frozen gate is the nonlinear nonlocal comparator.

Use the already frozen covariant action

\[
S=\frac{M_{\rm Pl}^2}{2}\int d^4x\sqrt{-g}
\left[R+G_{\mu\nu}\mathcal F(\Box)R^{\mu\nu}\right]+S_m[g,\Psi],
\]

with

\[
\mathcal F(\Box)=\frac{e^{-\lambda\Box}-1}{\Box},\qquad \lambda=M^{-2}>0,
\]

and the source-completed metric convention inherited from Iterations 148–149.

The tree CTP prescription is the ordinary doubled closed action `S[g_+]-S[g_-]` in the frozen `h_±=r±a/2` convention. The entire form factor has no branch cut; retarded ordering belongs to the CTP response/inversion prescription rather than to an independently adjustable cubic form factor.

## 2. Why propagator-only information is insufficient

Expand around flat space:

\[
G=\kappa G^{(1)}+\kappa^2G^{(2)}+\cdots,
\]
\[
R=\kappa R^{(1)}+\kappa^2R^{(2)}+\cdots,
\]
\[
\sqrt{-g}=1+\kappa s^{(1)}+\cdots,
\]
\[
\mathcal F(\Box)=\mathcal F_0+\kappa\,\delta\mathcal F^{(1)}+\cdots.
\]

The quadratic nonlocal term contains only

\[
S_{\rm NL}^{(2)}\sim G^{(1)}\mathcal F_0R^{(1)}.
\]

The cubic term necessarily contains four structural pieces,

\[
S_{\rm NL}^{(3)}\sim
G^{(2)}\mathcal F_0R^{(1)}
+G^{(1)}\mathcal F_0R^{(2)}
+s^{(1)}G^{(1)}\mathcal F_0R^{(1)}
+G^{(1)}\delta\mathcal F^{(1)}R^{(1)}.
\]

The last term is invisible in a propagator-only parametrization.

Therefore a measured or frozen two-point kernel does **not** by itself define the nonlinear nonlocal comparator. A full covariant parent action is required.

This agrees with the fixed `NL-WNL-001` authority: weakly nonlocal gravity permits an independent higher-curvature interaction potential `V`, whose coefficients do not affect the quadratic propagator.

## 3. Exact Fréchet derivative for the exponential comparator

Use the identity

\[
\mathcal F(A)=-\int_0^\lambda d\alpha\,e^{-\alpha A}.
\]

The first operator variation is exactly

\[
\boxed{
\delta\mathcal F(A)=
\int_0^\lambda d\alpha\int_0^\alpha du\,
e^{-(\alpha-u)A}(\delta A)e^{-uA}
}.
\]

Between eigenmodes with eigenvalues `a,b`, the insertion coefficient becomes the divided difference

\[
\boxed{
\mathcal F^{[1]}(a,b)=
\frac{\mathcal F(a)-\mathcal F(b)}{a-b}
}
\]

with diagonal limit `F'(a)`.

The reproducible certificate checks six eigenvalue pairs, including the diagonal case, and finds

`max |integral - divided difference| = 0.0`

at floating-point precision.

Retain:

`NL-NG-003 — COVARIANT_NONLOCAL_CUBIC_VERTEX_CONTAINS_OPERATOR_FRECHET_VARIATION_NOT_VISIBLE_IN_PROPAGATOR_ONLY_REASONING`.

## 4. Does this fixed action require an independent cubic form factor?

For **this exact frozen comparator**, no.

Once the complete covariant parent action and the entire function `F` are declared, the tree cubic vertex is fixed in principle by the curvature expansion plus the Fréchet variation above. `QG-NL-EXP-001` contains no independently adjustable curvature-cubic potential by definition.

For the **broader weakly-nonlocal class**, yes: two-point data alone do not fix the cubic sector because independent higher-curvature potentials and/or additional covariant form-factor structures can be added without changing the same quadratic TT propagator.

This distinction must be preserved:

- exact frozen parent action -> tree cubic fixed in principle;
- propagator or theory-class label alone -> cubic not unique.

The 2015 Donà–Giaccari–Modesto–Rachwał–Zhu analysis is consistent with this distinction: Ricci/scalar form-factor theories can be field-redefinition equivalent to Einstein gravity for broad on-shell tree amplitudes, while changing the action content, especially Riemann-sector terms, changes amplitudes. RQIR remains off-shell/source-response sensitive, so on-shell amplitude equivalence does not erase the need for the source-completed cubic map.

## 5. Current CTP relation quotient annihilates the full nonlocal tree amplitude

Iteration 172 uses, per frozen kinematic row,

`(Gamma_arr,Gamma_aar,Gamma_aaa,WardLock)`

and maps to

`R_aar=Gamma_aar`,

`R_unit=Gamma_aaa-Gamma_arr/4`,

`R_W=WardLock`.

For any closed-unitary cubic action in the frozen `r/a` convention,

\[
\Gamma_{aar}=0,
\qquad
\Gamma_{aaa}=\frac14\Gamma_{arr}.
\]

For a source-completed diffeomorphism-invariant parent action, the exact Ward consistency coordinate is

\[
R_W=0.
\]

Therefore **independently of the detailed nonlocal cubic amplitude**,

\[
\boxed{R_{aar}=R_{unit}=R_W=0}.
\]

The six arbitrary row-amplitude basis has raw rank `6`, but after the Iteration-172 relation map its rank is exactly

\[
\boxed{0}.
\]

`max |relation entry| = 0.0`.

This is not a claim that the nonlocal cubic vertex vanishes. It is a statement that the **current relation coordinates quotient it away exactly**.

Retain:

`CTP-NG-005 — CLOSED_UNITARY_DIFFEO_INVARIANT_NONLOCAL_TREE_ACTION_IS_ANNIHILATED_BY_CURRENT_COARSE_CTP_RELATION_MAP`.

## 6. New methodological consequence

The present relation coordinates are now proven too coarse to distinguish among broad closed-unitary diffeomorphism-invariant quantum gravity families.

- C4 closed quantum mediator: `R_unit=0`;
- C5 closed quantum gravity tree: `R_unit=0`;
- fixed covariant nonlocal quantum gravity tree: `R_unit=0`;
- all source-completed diffeomorphism-invariant cases: `R_W=0`.

Therefore neither generic unitary `r/a` structure nor vanishing Ward violation can carry gravity-specific novelty.

Retain:

`NG-FUNNEL-034 — ZERO_WARD_LOCK_PLUS_GENERIC_UNITARY_RA_RELATION_CANNOT_DISTINGUISH_QUANTUM_GRAVITY_FAMILIES`.

## 7. What relation is needed next

The next comparator protocol must resolve the **Ward-determined longitudinal part** of the cubic vertex from the genuinely independent transverse/off-shell three-point form factors.

A useful next coordinate must compare the amputated cubic vertex to the same inverse two-point kernel at finite soft momentum, schematically

\[
R_{\rm soft/tensor}
=
\Gamma^{(3)}_{arr}
-\mathcal W[K^{(2)}],
\]

where `W` is the exact tensor Ward/Slavnov-Taylor map, not a scalar pass/fail flag.

The longitudinal Ward-determined part is consistency/shared structure. Candidate novelty, if any, must survive in the transverse relation sector after the same C3/C4/C5/nonlocal/AS comparison.

## 8. Readiness

`MODEL_READINESS: 24%` — unchanged.

A nonlocal tree comparator blocker has been structurally resolved at the level relevant to the current coarse relation quotient, but the result proves that quotient is too weak rather than producing a residual.

No `ANSATZ-003`. No Fisher. No resource optimization.
