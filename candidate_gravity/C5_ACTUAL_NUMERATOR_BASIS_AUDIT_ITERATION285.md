# Candidate Gravity C5 — Iteration 285 actual numerator oracle and basis correction

**Date:** 2026-09-02  
**MODEL_READINESS:** **24%**

## Question

Iteration 284 certified that the proposed 9-dimensional raised-bubble basis and 50-dimensional raised-triangle basis are full-rank on deterministic loop-momentum samples. That result was only a sampling-geometry certificate. The unresolved question was whether the **actual same-parent denominator-stripped numerator** belongs to those bases.

## Actual primitive numerator oracle

The frozen Iteration-270/273 dynamics was expanded branch-by-branch before any master fitting:

- `Q0(p)=-eta/p^2` is split into its exact matrix numerator `-eta` and scalar denominator;
- `Q1=-Q0 N1 Q0` is retained as one primitive branch;
- `Q2` is split into its two sequential `N1 Q0 N1` branches and one `-N2` contact branch;
- the 15 surviving null-soft Leibniz terms then give the exact 23 primitive denominator branches already counted in Iterations 271/282.

Summing `primitive numerator / exact Q0 denominator product` reproduces the direct translation-closed object with

- `tr B3 = 0.9605914097678994`;
- `||B3||_F = 1.3106212324929962`;
- matrix residual against the direct Q1/Q2 sum `1.32e-12`.

Thus the oracle is the same frozen parent dynamics, not a surrogate fit.

Freeze:

`PASS_EXACT_DENOMINATOR_STRIPPED_SAME_PARENT_PRIMITIVE_NUMERATOR_ORACLE`.

## Canonical orientation

For the closed non-scaleless branches the repeated propagator is already `p^2`. Bubble branches occur with simple denominator shifts `+q` and `-q`. The latter are mapped by the legitimate loop reflection `p=-l`, so every canonical bubble denominator is represented as

`(l^2)^2 (l+q)^2`.

The three raised-triangle sectors similarly occur in opposite pairs of simple shifts and are related by the same reflection. No numerator is summed before applying the same loop-variable transformation as its denominators.

## Critical audit of the Iteration-283/284 9/50 bases

The exact degree ceilings remain correct:

- raised bubbles: degree `<=4`;
- raised triangles: degree `<=6`.

However, the previous **minimal scalar basis count** used only denominator vectors:

- bubble: `(l^2)^a (l.q)^b`, `2a+b<=4` -> 9 columns;
- triangle: `(l^2)^a(l.q1)^b(l.q2)^c`, `2a+b+c<=6` -> 50 columns.

This implicitly assumed that denominator topology exhausts the external structures entering the numerator. The actual same-parent numerator also contains the fixed null-soft momentum and TT polarization tensors. Therefore this reduction is not valid a priori.

The held-out oracle test falsifies it decisively.

### Bubble-a

9-column topology-only basis:

- rank `9/9`;
- held-out max error `10.3296193378`;
- held-out relative max error `0.9481450100`.

Full coordinate polynomial basis of total degree `<=4` (70 monomials):

- rank `70/70`;
- held-out max error `1.0128e-8`;
- held-out relative max error `9.30e-10`.

### Bubble-b

9-column topology-only basis:

- rank `9/9`;
- held-out max error `5.9224798595`;
- held-out relative max error `0.6811050545`.

Full degree-`<=4` 70-monomial basis:

- rank `70/70`;
- held-out max error `1.9334e-8`;
- held-out relative max error `2.22e-9`.

### Raised triangle `(0,0.41)` sector

50-column topology-only basis:

- rank `50/50`;
- held-out max error `54.2356922813`;
- held-out relative max error `33.2055942841`.

Full coordinate polynomial basis of total degree `<=6` (210 monomials):

- rank `210/210`;
- held-out max error `3.5559e-10`;
- held-out relative max error `8.87e-11`.

Therefore full rank of the proposed 9/50 sampling matrices did **not** establish numerator completeness.

## Corrected theorem

Freeze:

`C5-NG-018 — DENOMINATOR_TOPOLOGY_DOES_NOT_EXHAUST_SAME_PARENT_NUMERATOR_TENSOR_DEPENDENCE`.

At fixed external kinematics, the actual scalar orbit-trace numerator is a finite polynomial with the already-certified degree ceilings, but the basis must retain dependence induced by all frozen external momenta and polarization tensors. A denominator-only scalar basis can be dramatically incomplete.

Freeze:

`PASS_ACTUAL_NUMERATOR_ORACLE_AND_FAIL_TOPOLOGY_ONLY_9_50_BASIS_WITH_COMPLETE_70_210_RECONSTRUCTION_CERTIFICATES`.

## What is superseded and what is retained

Superseded:

- the claim in Iterations 283-284 that dimensions 9 and 50 are sufficient reconstruction bases for the actual numerator.

Retained:

- translation closure;
- 23-branch denominator census;
- no box master after closure;
- raised bubble/triangle topology;
- canonical repeated-index sector classification;
- exact numerator degree ceilings `4/6`;
- affine loop-shift degree preservation;
- nonzero spacelike and timelike B3/orbit trace;
- scalar master cut support.

## Scientific status

This is a correction of the reconstruction layer, not a Candidate Gravity residual and not a consistency failure of the parent dynamics. It prevents an invalid tensor/IBP reduction from being performed on an incomplete numerator basis.

`MODEL_READINESS = 24%`, unchanged.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Exact next gate — Iteration 286

1. Apply the validated full degree-`<=6` reconstruction to the remaining triangle sectors `(0,0.21)` and `(0.21,0.41)` with held-out residuals.
2. Preserve the already validated 70-monomial reconstructions for bubble-a and bubble-b.
3. Convert the complete fixed-kinematics polynomial coefficients into an IBP/tensor-moment representation, or construct an explicitly complete covariant basis including the soft momentum and TT polarization tensors and cross-check it against the 70/210 oracle.
4. Only after this completeness check extract hard-channel logarithmic/discontinuity coefficients.
5. Source/Ward/contact completion, comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream.
