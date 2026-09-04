# Candidate Gravity Recovery Delta — Iteration 411

Date: 2026-09-04

MODEL_READINESS: 24%

## Scope
Fail-closed raw consumption of the split analytic/spectral physical reductions for the two double-double `Tr(U1^2)` targets inherited from Iteration 410 structural PASS. Workflow colour alone is not authority. Both artifacts were downloaded and their scientific JSON plus authority audits were inspected directly.

## Index 11 — CONVERGED

- double-double global index: `11`
- class: `16`
- `q^2=-0.34`
- status: `CONVERGED`
- authoritative `D_s TrU1^2 double-double channel = +0.013050543643260309`
- mixed derivative at `h=5e-6`: `-0.013050543643260309`
- mixed derivative at `h/2=2.5e-6`: `-0.01305596497050016`
- scaled mass-step convergence error: `5.421327239850046e-06 < 2e-05`
- max direct original-integrand cross-check: `1.1526331104849685e-12 < 2e-06`
- max held-out polynomial error: `5.998077468732932e-16`
- minimum analytic uncut separation: `0.25855334940036967`
- minimum Kallen: `0.11558639999999996`

Provenance:
- run `33851983789`
- job `100956624748`
- artifact `9931076355`
- artifact digest `sha256:8551fba98b0f3f218960820a01369ca183da1234d22754bd5c647fa8909cf6f8`
- raw result SHA-256 `f8aea08be16636dcf5d83afaa29dd3059c734a1a3ad8f778f07ef53b3041abf1`
- authority-audit SHA-256 `ff8c98b7eed639ebde720da612c00e12ceb980ce9fef572a04630d24414f43eb`
- authority audit: PASS

Index 11 therefore replaces only its previous blocked entry.

## Index 2 — sole remaining physical blocker

- double-double global index: `2`
- class: `3`
- `q^2=-1`
- status: `BLOCKED_CONVERGENCE`
- diagnostic only, NOT authority: `D_s TrU1^2 double-double channel = +0.003560682203382001`
- mixed derivative at `h=5e-6`: `-0.003560682203382001`
- mixed derivative at `h/2=2.5e-6`: `-0.0036107242774472896`
- scaled mass-step convergence error: `5.0042074065288766e-05 > 2e-05`
- max direct original-integrand cross-check: `2.0658472996495925e-09 < 2e-06`
- max held-out polynomial error: `6.081289985471194e-16`
- minimum analytic uncut separation: `0.11857147221810008`
- minimum Kallen: `0.99996`

Provenance:
- run `33851983789`
- job `100956624953`
- artifact `9930938547`
- artifact digest `sha256:3c34f0110e3dbf97b7abf5dedf7b70bf918d4bb3a9e2b5572c7d1f92df7120c2`
- raw result SHA-256 `53a185ae9825cde0a273161b1ee093ede54103b52d513ea291a3bfc8e1381486`
- authority-audit SHA-256 `7cd59a6e7876549962438a30416f75f4920cea107f569bb5952c38cd50f3e3bd`
- authority audit: PASS

The fixed-mass analytic/spectral representation is not the blocker: denominator-affine, polynomial-heldout, radial, Kallen, uncut-separation and original-integrand checks all pass by wide margins. The remaining failure is isolated to auxiliary-mass step convergence.

## Consequence
The exact unresolved double-double physical set is now **`[2]` only**. Iteration 412 exact15 assembly remains blocked until index 2 is scientifically converged. No diagnostic value and no zero-fill may enter the q2 sum.

## Prospectively frozen next gate
Iteration 413 contract was frozen before the next numerical value is visible. It computes one additional central4×central4 level only, `h/4=1.25e-6`, preserving the physical `2e-5` threshold. Promotion requires:

1. scaled `|D(h/2)-D(h/4)| <= 2e-5`;
2. successive order-4 Richardson extrapolants from `(h,h/2)` and `(h/2,h/4)` agree within `2e-5`;
3. error contraction ratio is `<1`;
4. all fixed-mass heldout / affine-denominator / radial / direct-original checks pass at their frozen thresholds.

If PASS, the promoted channel value is the **direct `h/4` central4×central4 result**, not the Richardson extrapolate. If FAIL/BLOCKED, step shrinking stops and the next method is an independently validated auxiliary-mass spectral/Taylor reconstruction.

## Guardrails
No threshold weakening. No blind angular-grid escalation. No zero fill. No effective-action `-i/4` folding before complete `TrU1^2`. No source/Born subtraction. No `ANSATZ-003`. No Fisher/resources.

MODEL_READINESS: 24%
