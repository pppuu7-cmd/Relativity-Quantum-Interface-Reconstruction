# Candidate Gravity Iteration 135 — first RQIR-driven causal spectral CTP ansatz

**Date:** 2026-08-31  
**Model:** `ANSATZ-RQIR-CTP-001` v0.1  
**Decision:** START / DRAFT_TESTING, not promoted to `QG001`

## Question

Can the first post-reference Candidate Gravity model be made genuinely RQIR-driven, so that mean/noise/ordered response are not independently fitted, while preserving a controlled GR infrared boundary and exposing a single falsifiable deformation direction?

## Construction

The model uses one causal CTP spin-2 kernel with

`K_R^(2)=K_GR,R^(2)[1+beta F_R]`,

`zeta=-(p^2+i0 p^0)/M_*^2`,

`F_R=zeta int_1^infty ds rho_hat(s)/(s+zeta)`,

`rho_hat(s)=exp(1-s)Theta(s-1)`.

The same spectral object controls the absorptive response and, under the v0.1 vacuum spectral relation, the Gaussian noise kernel. Consequently `response` and `noise` are not separate science parameters.

## First scoped theorem

For spacelike `x=-p^2/M_*^2>=0`,

`F_E(x)=x int_1^infty ds exp(1-s)/(s+x)`

and

`F_E(x)=x exp(1+x) E1(1+x)`.

Since `rho_hat` is nonnegative, normalized, and supported on `s>=1`,

`0 <= F_E(x) <= x/(1+x) < 1`.

Therefore for `beta>=0`,

`1+beta F_E(x) >= 1`.

**Scoped result CG-R135-002:** no extra zero of the Euclidean/spacelike multiplicative spin-2 kernel occurs for the frozen v0.1 parameter sign.

This is not a Lorentzian ghost-freedom theorem.

## Infrared behavior

At small `x`,

`F_E(x)=A1 x+O(x^2)`

with

`A1=e E1(1)=0.596347362323...`.

Hence the deformation vanishes at the massless GR pole and begins as a derivative-suppressed correction. This is a necessary ingredient for the classical/GR limit, but not yet the full Newtonian source-normalization proof.

## Reproducible audit

`analysis/candidate_gravity_rqir_ctp_iteration135.py` checks:

- unit normalization of the spectral shape;
- positivity of `F_E`;
- the analytic upper bound on a logarithmic spacelike grid;
- absence of a spacelike kernel zero for representative `beta>=0` values;
- agreement of the numerical infrared slope with `e E1(1)`.

Recorded output:

`results/candidate_gravity_rqir_ctp_iteration135.json`

Result: `PASS_SCOPED`.

## Why no promotion yet

The ansatz cannot be promoted because the high-value gates remain open:

1. Lorentzian analytic structure, branch cut and possible zeros on physical/unphysical sheets;
2. microscopic positivity/unitary dilation or an equally strong consistency certificate;
3. complete conserved-source tensor structure and nonlinear diffeomorphism/relational audit;
4. exact Newtonian source-to-potential normalization;
5. prior-art/comparator mapping against standard QG EFT, nonlocal/form-factor gravity, hidden-sector spectral models, and classical-quantum channels;
6. finite Paper-I RQIR discriminator that survives hard calibration constraints;
7. Paper-II profiled Fisher and Paper-III physical resources only after the previous items are nondegenerate.

## Comparator interpretation

The deep-infrared Taylor expansion is expected to be reproducible by ordinary higher-dimension gravitational EFT operators to finite order. Therefore low-energy nonzero `beta` alone is **not** a novelty discriminator against C5.

Any genuinely distinct content, if it exists, must come from the full causal spectral structure in the regime where the nonlocal shape is resolved and must survive the updated comparator registry.

## Literature guardrail

The construction is intentionally not advertised as new. Existing work on gravitational EFT and nonlocal/form-factor quantum gravity already establishes that momentum-dependent/nonlocal form factors and nonanalytic propagator corrections are part of the known landscape. The next iteration must use that literature as a comparator, not as retrospective justification for novelty.

## Frozen next step

**Iteration 136 target:** derive the Lorentzian continuation explicitly, compute the discontinuity across `p^2>=M_*^2`, search for zeros of `1+beta F_R` on the physical sheet over a frozen parameter box, and determine whether positive spectral input is sufficient for a scoped propagator-positivity statement.

No detector optimization is allowed before this analytic-structure gate.
