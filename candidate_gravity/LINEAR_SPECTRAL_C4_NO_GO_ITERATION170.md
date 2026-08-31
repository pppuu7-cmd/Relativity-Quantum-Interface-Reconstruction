# Candidate Gravity — Iteration 170: general linear-spectral C4 no-go

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Status:** linear positive-spectral branch closed for gravity-specific promotion; no `ANSATZ-003`

## Question

Iterations 166–169 constructed an increasingly strict timelike conserved-TT absorptive-shape quotient. After removing local tree C5, the complete leading massless one-loop C5 shape, and a conservative next-order `O(p^6)` C5 envelope, five frequency-shape dimensions remain.

Before investing in finite-frequency asymptotic-safety reproduction or detailed threshold scans, ask the stronger question:

> Can any positive residual in a **single linear TT two-point response** be gravity-specific against comparator C4?

## General spectral statement

For a physical conserved-traceless TT source-response channel admitting a positive Källén–Lehmann representation,

\[
\chi_R^{TT}(s)=\frac{Z_0}{s+i0\,\mathrm{sgn}\omega}
+\int_0^\infty d\mu^2\,
\frac{\rho_{TT}(\mu^2)}{s-\mu^2+i0\,\mathrm{sgn}\omega},
\qquad \rho_{TT}(\mu^2)\ge0.
\]

The standard Källén–Lehmann representation follows from the Hilbert-space spectral decomposition under the usual QFT assumptions; unitarity gives non-negative physical spectral densities. For spinning operators the decomposition is resolved into little-group spin components with non-negative spectral weights.

Literature anchors:

- G. Källén, *On the definition of the renormalization constants in quantum electrodynamics*, Helv. Phys. Acta 25 (1952) 417;
- H. Lehmann, *On the properties of propagation functions and renormalization constants of quantized fields*, Nuovo Cim. 11 (1954) 342;
- M. Loparco, J. Penedones, K. Salehi Vaziri, Z. Sun, *The Källén–Lehmann representation in de Sitter spacetime*, arXiv:2306.00090, including arbitrary spin, positivity and the Minkowski flat-space limit.

## Exact C4 direct-integral construction

Introduce independent positive-norm massive spin-2 mediator fields `H_(mu^2)` and couple their TT components linearly to the same conserved-traceless source with coupling density

\[
g(\mu^2)=\sqrt{\rho_{TT}(\mu^2)}.
\]

Define schematically

\[
h_{\rm eff}^{TT}=\sqrt{Z_0}\,h_0^{TT}
+\int^{\oplus}d\mu^2\,\sqrt{\rho_{TT}(\mu^2)}\,H_{\mu^2}^{TT}.
\]

Because the fields are independent,

\[
D_R^{\rm eff}=Z_0D_R^{(0)}
+\int d\mu^2\,\rho_{TT}(\mu^2)D_R^{(\mu^2)},
\]

which is exactly the spectral response above.

This is not an approximation and does not depend on the detailed shape of `rho_TT`.

The same construction, with a Gaussian mediator state chosen to match the candidate covariance, reproduces the corresponding Gaussian Hadamard/noise kernel and therefore the full linear-Gaussian CTP influence functional, as already demonstrated for the special `KL-002` continuum in Iteration 141.

Authority inside this repository:

`docs/CANDIDATE_GRAVITY_C4_GAUSSIAN_DEGENERACY_ITERATION141.md`.

## Consequence for thresholds and branch cuts

A branch cut is simply continuous spectral support. A threshold is the lower endpoint or change of support/weight in that spectral measure.

Therefore, within the frozen physical TT two-point sector:

- arbitrary positive continuum shape;
- multiple thresholds;
- narrow positive poles;
- broad positive spectral bands;
- finite-frequency nonanalytic shape

are all reproducible by an ordinary C4 direct integral/tower of positive-norm mediators with the same spectral measure.

Thus even a nonzero vector in the five-dimensional Iteration-169 C5-null shape space is **not** a gravity-specific residual if it is only a positive linear spectral response.

## What if the spectral density is not positive?

Failure of positivity does not automatically certify new quantum gravity.

It triggers a different gate:

1. is the quantity a physical gauge-invariant/source-completed observable or only a gauge-dependent field correlator?
2. does the sign violation indicate a negative-norm state, ghost, instability or other loss of unitarity?
3. is there a valid generalized spectral representation compatible with a positive physical Hilbert space?

A candidate may not use spectral negativity as a novelty certificate before those consistency questions are passed.

## Retained results

### C4-NG-008 — POSITIVE_LINEAR_TT_SPECTRAL_RESPONSE_IS_EXACTLY_REPRESENTABLE_BY_ORDINARY_MEDIATOR_CONTINUUM

Iteration 141 generalizes from one frozen spectral density to every positive physical TT Källén–Lehmann measure: the linear response has an exact ordinary-mediator direct-integral representation.

### ABS-SHAPE-005 — FINITE_FREQUENCY_LINEAR_SPECTRAL_SHAPE_CANNOT_CERTIFY_GRAVITY_SPECIFIC_NOVELTY_AGAINST_C4

Surviving C5/AS spectral shape alone is not enough. Thresholds and branch cuts do not repair the C4 identity.

### NG-FUNNEL-030 — LINEAR_SPECTRAL_RESIDUAL_REQUIRES_A_LINKED_NONLINEAR_OR_POST_GAUSSIAN_GRAVITY_RELATION_FOR_PROMOTION

A promotable residual must involve more than a single two-point spectrum. It must be linked, by the same parent dynamics, to a nonlinear/ordered or higher-cumulant gravitational relation that cannot be independently reproduced by the C4 mediator family.

## Implication for research direction

The finite-frequency Lorentzian-AS spectral curve remains scientifically useful as a comparator and article result, but reproducing it is **no longer a prerequisite for deciding whether a linear spectral residual can seed `ANSATZ-003`**. C4 already defeats that promotion route in full generality under positive spectral assumptions.

The next Candidate Gravity search should return to the post-Gaussian contract and seek a linked package such as

\[
(\chi_R^{(1)},\ C_{3,\rm sym},\ \chi_R^{(2)},\ \text{Ward/soft relation})
\]

from one parent dynamics, with a residual outside fixed C3/C4/C5/nonlocal/AS **multi-point** comparator spans.

## Numerical illustration

`analysis/linear_spectral_c4_no_go_iteration170.py` represents one positive discrete spectral measure both as a KL sum and an explicit mediator tower on the eight frozen timelike rows. The maximum floating-point difference is `2.84e-14`.

This numerical equality is illustrative only. The scientific equivalence follows algebraically from the direct-integral representation.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

A major false-positive branch is now closed, but no robust Candidate Gravity residual and no parent dynamics exist yet. Comparator foundation remains `24/25` because the required **multi-point** comparator quotient is not fully instantiated.

No Fisher. No resource optimization. No `ANSATZ-003`.
