# Candidate Gravity C5 — Iteration 287 bubble tensor-moment pre-gate

**Date:** 2026-09-02  
**MODEL_READINESS:** **24%**  
**Status:** analytic reduction map frozen; exact same-parent coefficient workflow active; no physical linked residual yet

## Purpose

Iteration 286 closed actual-oracle polynomial reconstruction for every non-scaleless raised bubble and triangle sector. Iteration 287 begins coefficient-level dimensional-regularization reduction, starting with the two complete degree<=4 raised bubbles.

The canonical family is

\[
I[N](q)=\int\! d^D l\;\frac{N(l)}{(l^2)^2((l+q)^2)},\qquad D=4-2\epsilon.
\]

The loop integral is normalized by `i*pi^(D/2)`. The target coefficient is the coefficient multiplying `log_R(-q^2)`; with the frozen RQIR convention `D_q log_R(-q^2)=1`, this is also the normalized discontinuity coefficient before source/Ward/contact completion.

## Feynman-parameter reduction

Use

\[
\frac1{A^2B}=2\int_0^1 dx\,\frac{x}{[xA+(1-x)B]^3}
\]

and shift

\[
r=l+(1-x)q.
\]

Only even isotropic moments survive. At D=4 for the pole/log coefficient one needs ranks 0, 2 and 4 only because the reconstructed bubble numerator has total degree <=4.

For a monomial whose shifted term contains `R=2n` powers of `r` and `P` powers of the shift vector `-(1-x)q`, the coefficient of `log_R(-q^2)` follows from minus the `1/epsilon` residue of the Feynman-parameter integral.

### Rank 0

Only the scalar numerator (`P=0`) has the endpoint pole:

\[
D_q\, I[1]=\frac1{q^2}.
\]

### Rank 2

For an isotropic pair `r_mu r_nu`, after including `1/D`, the normalized log coefficient is

\[
-\frac{\eta_{\mu\nu}}{2(P+1)(P+2)}
\]

times the remaining shift-vector monomial.

### Rank 4

For `r_mu r_nu r_rho r_sigma`, after including `1/[D(D+2)]`, the normalized log coefficient is

\[
\frac{q^2}{2(P+2)(P+3)(P+4)}
(\eta_{\mu\nu}\eta_{\rho\sigma}+\eta_{\mu\rho}\eta_{\nu\sigma}+\eta_{\mu\sigma}\eta_{\nu\rho})
\]

times the remaining shift-vector monomial.

These formulas are implemented monomial-by-monomial for the complete 70-dimensional fixed-coordinate basis of Iteration 285.

## Independent algebraic checks

The implementation passes three exact/near-exact checks before it is allowed to touch the same-parent fitted coefficients:

1. scalar numerator:
   `D_q I[1] = 1/q^2`;
2. numerator `l^2`:
   cancellation reduces the raised bubble to the ordinary massless bubble and the normalized log coefficient is `-1`;
3. numerator `(l^2)^2`:
   cancellation reduces the integral to a shifted massless tadpole, hence the dimensional-regularization discontinuity is zero; direct tensor-moment summation gives approximately `-1.4e-17` in the frozen bubble-a check.

## Loop-reflection check

The canonicalization in Iteration 285 reflects primitive branches where needed. The reduction therefore also tests

`N(l), q  ->  N(-l), -q`

and requires the extracted log coefficient to be invariant to numerical precision.

## Active exact-oracle workflow

Authority code:

- `candidate_gravity/code/iteration287_bubble_tensor_moment_reduction.py`
- `.github/workflows/rqir-iteration287-bubble-reduction.yml`

GitHub Actions run id: `33678076428`.

At the time this pre-gate is frozen, the run is still evaluating the exact same-parent oracle. Therefore **no bubble-a/b numerical coefficient is authoritative yet** and the earlier exploratory `-0.64977` value remains superseded/unfrozen until the complete 70-monomial gate finishes.

## Classification

`PASS_ANALYTIC_BUBBLE_TENSOR_MOMENT_REDUCTION_MAP_AND_SCALELESS_SANITY_CHECKS`.

This is a method-level PASS only. It does not close Iteration 287 until the actual 70-monomial bubble-a/b coefficient vectors have been reduced and the workflow passes.

## Current blocker

`BLOCKED_WAITING_FOR_COMPLETE_ACTUAL_ORACLE_BUBBLE_COEFFICIENT_EVALUATION_WITHIN_ITERATION287`.

This blocker is computational, not a physics zero and not a Candidate Gravity failure.

## Next after coefficient PASS

1. freeze the two complete bubble log/discontinuity coefficients;
2. export the full fitted 70 coefficient vectors for reproducibility;
3. perform the analogous rank-0/2/4/6 reduction for all three 210-monomial raised triangles;
4. only then assemble the same-parent hard-channel discontinuity and proceed to source/Ward/contact completion and comparator subtraction.

No `ANSATZ-003`. No Fisher/resources.
