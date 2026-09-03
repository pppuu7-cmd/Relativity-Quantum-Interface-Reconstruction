# RQIR Candidate Gravity Recovery Delta — Iteration 380

Date: 2026-09-04

MODEL_READINESS: 24%

## Authority

Iteration 380 closes the sole determinant triangle channel that remained numerically BLOCKED at `q^2=-1` after Iteration 333, without changing the parent numerator, propagator routing, or the frozen `2e-5` convergence criterion.

Freeze:

`PASS_DET_TRIANGLE_Q2_MINUS1_ANALYTIC_AZIMUTH_REDUCTION_NONZERO_DISCONTINUITY`

Validated Actions provenance:

- run `33814113932`
- job `100842299850`
- workflow head `c24850b08f5617868b366d7ec47b68a6cb9cdf40`
- artifact `9916838615`, `iteration380-result`
- artifact digest `sha256:198d91e9ef7a5a09cdbaca11eb4c02135462fe831f01fbf3c54c7daf7820df63`
- scientific JSON SHA-256 `217e1fabe4f97967ee82c31101ecce3aeac27826599b516f779a9db84f098ef4`
- exactly one top-level JSON object, sentinel `380`, `scientific_authority_pass=true`.

## Scientific result

For the frozen `q^2=-1`, cut pair `(0,2)`, uncut propagator `1` channel, the third denominator is exactly affine on the cut sphere,

`D3(z)=0.26 + 0.14142135623730953 z`,

with exact range

`[0.11857864376269048, 0.40142135623730957]`.

The azimuthally averaged physical triangle numerator is held-out validated by a degree-six representation:

- train scaled max error `6.104210088813152e-16`;
- held-out scaled max error `7.4395060457410295e-16`;
- independent phase-shift scaled error `1.526052522203288e-16`.

The analytic one-dimensional reduction gives the normalized angular mean

`m_triangle(q^2=-1) = 0.006875651912582228`.

A direct sparse quadrature of the original, unreduced integrand gives

`0.006875651912566607`,

with scaled disagreement `8.354002293824815e-13`, maximum cut-shell error `1.6653345369377348e-16`, and minimum sampled uncut denominator magnitude `0.12118636387567519`.

This is therefore a NONZERO two-particle discontinuity certificate. The old Iteration-333 `q^2=-1` numerical BLOCKED status is superseded only for this channel.

## Normalization consequence

Iterations 337 and 338 remain the normalization authority:

`D_s C_det = -m`,

`Gamma_det = +i C_det`,

hence

`D_s Gamma_det = -i m`.

No graviton/ghost determinant weights are to be applied again; they are already internal to the Iteration-331 route coordinate.

## Scope boundary

Iteration 380 does **not** close:

- the Iteration-297 finite-dimensional/evanescent remainder warning;
- Source/Ward/contact completion;
- matched `K2` subtraction;
- the comparator quotient;
- any comparator-subtracted residual.

It also does not authorize `ANSATZ-003`, Fisher information, or resource claims.

## Readiness

MODEL_READINESS remains 24%. The determinant ordinary two-particle triangle obstruction is removed, but no complete readiness rubric bucket is newly closed.

## Exact next gate

Assemble, without summing distinct `q^2` variables, the complete channel-resolved ordinary-simple determinant absorptive vector from the three Iteration-333 bubble means and the two previously converged Iteration-333 triangle means plus the Iteration-380 `q^2=-1` triangle mean. Apply the frozen Iterations-337/338 conversion `D_s Gamma_det=-i*sphere_mean` only after retaining family provenance. Keep the Iteration-297 finite-DR warning explicit.
