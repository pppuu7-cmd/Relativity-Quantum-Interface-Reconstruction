# RQIR Research Log — Iteration 145

**Date:** 2026-08-31  
**Branch:** Candidate Gravity / post-Gaussian design  
**Promotion decision:** no `ANSATZ-003` frozen

## Starting point

Iteration 144 supplied the finite post-Gaussian quotient

`rank([M,b]) > rank(M)`

with separate symmetric and ordered residual sectors. The immediate task was to instantiate the first finite protocol/comparator structure before writing a third candidate dynamics.

## Literature audit used in this iteration

### Soft-graviton structure

- Cachazo & Strominger, arXiv:1404.4091: universal leading soft-graviton pole and tree-level evidence for universal subleading soft factor.
- Elvang, Jones & Naculich, arXiv:1611.07534: local EFT operators can add graviton soft terms at subsubleading order, while the subleading graviton theorem is not modified by local operators in the analysed 4D EFT setting.

### Strong comparator realizations retained for later finite tangents

- Grudka et al., arXiv:2402.17844: covariant postquantum-classical gravity, stochastic action/renormalisation structure.
- Oppenheim & Sajjad, arXiv:2605.05375: explicit stochastic metric modes and two-point spectra in postquantum classical gravity.
- Pawlowski & Tränkle, arXiv:2309.17043: momentum-dependent three-/four-graviton vertices and reconstructed effective action in an asymptotic-safety truncation.
- Koshelev, Kumar & Starobinsky, arXiv:2305.18716: covariant nonlocal-gravity action landscape with ghost-free/nonlocal structure in controlled backgrounds; use only a fixed action when promoted to an RQIR comparator.

## Result 1 — soft theorem is a lock, not novelty

The first protocol now separates

- `soft0` — leading soft consistency;
- `soft1` — subleading soft consistency;
- `soft2` — subsubleading soft-sensitive coordinate.

For a future candidate retaining the standard massless-GR/diffeomorphism boundary:

- `soft0` and `soft1` are hard consistency locks;
- a candidate direction is not allowed to claim novelty by violating those locks while simultaneously claiming the same GR boundary;
- `soft2` is measurable but must be included in the C5 EFT tangent space because local EFT operators can alter subsubleading soft behavior.

Retained result:

**NG-FUNNEL-004 — SOFT_LOCK_NOT_NOVELTY.**

A soft-graviton relation alone is not the desired residual. Its useful role is to lock higher-point response to the same gravitational symmetry/coupling.

## Result 2 — first finite post-Gaussian protocol

Frozen full coordinate vector:

`y = (norm, N2, chi1R, C3sym, chi2R_even, chi2R_odd, soft0, soft1, soft2, tensor_geo, threshold)`.

Hard locks:

`norm`, `soft0`, `soft1`.

Reduced vector:

`z = (N2, chi1R, C3sym, chi2R_even, chi2R_odd, soft2, tensor_geo, threshold)`.

Reduced dimension: `8`.

## Result 3 — class-envelope saturation

Before selecting concrete comparator models, broad class labels C3/C4/C5 were represented conservatively by independent per-coordinate capability axes.

This is intentionally an over-complete diagnostic, not a physical tangent calculation.

Reproducible script:

`analysis/post_gaussian_class_envelope_iteration145.py`

Recorded result:

`results/post_gaussian_class_envelope_iteration145.json`

Ranks:

- C3 capability envelope: `7`;
- C4 capability envelope: `7`;
- C5 capability envelope: `8`;
- combined reduced span: `8/8`.

All one-coordinate hypothetical candidate tangents have zero residual against this deliberately broad envelope.

## Interpretation

This does **not** imply that every Candidate Gravity model is observationally degenerate.

It demonstrates that allowing a broad theory class to vary every coordinate independently removes precisely the internal correlations, Ward identities and fixed parameter relations that make a model falsifiable.

Therefore comparator blocks must be derivatives of fixed finite realizations:

`V_C = partial y / partial theta_C`

with an explicit action/truncation/state/renormalization convention.

Retained result:

**NG-FUNNEL-005 — CLASS_ENVELOPE_SATURATION.**

A class-label capability envelope is too broad for a meaningful post-Gaussian novelty quotient. Fixed representative comparator tangents are mandatory.

## Consequence for `ANSATZ-003`

The third ansatz remains intentionally withheld.

It may not be frozen until at least:

1. a finite C5 post-Gaussian baseline is instantiated;
2. a finite C3 realization and finite nonlinear C4 realization are instantiated or explicitly marked blocked where their higher response is not derived;
3. the candidate target is a finite-momentum ordered nonlinear component linked by Ward/soft identities to lower-point dynamics;
4. the formal candidate tangent is outside the concrete comparator span before Fisher/resources.

## Next authoritative scientific action — Iteration 146

Instantiate the C5 post-Gaussian tangent first because every viable `ANSATZ-003` must have an exact C5 boundary at `beta=0`.

Iteration 146 should:

1. freeze perturbative order and local EFT operator order;
2. freeze a finite source/response kinematic protocol for the coordinates above;
3. derive the Einstein-Hilbert tree contribution to the nonlinear response/soft locks;
4. add the first finite EFT directions that can modify `soft2`/finite-momentum response;
5. label loop/nonanalytic entries as explicit columns or BLOCKED rather than assuming zero;
6. produce the first actual `V_C5`, its rank and authority map.
