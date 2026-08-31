# RQIR Research Log — Iteration 158

**Date:** 2026-08-31  
**Comparator:** `QG-NL-EXP-001`

## Starting point

Authoritative Iteration 157 had fixed C3, nonlinear dRGT C4, and scoped C5 blocks. The required next step was one concrete strong-QG comparator outside those classes, preferably a covariant nonlocal/form-factor model.

## Frozen model

Use

`S = M_Pl^2/2 int sqrt(-g) [R + G_mn F(Box) R^mn] + S_m[g,Psi]`,

with

`F(Box)=(exp(-Box/M^2)-1)/Box`, `lambda=1/M^2`.

The metric/source convention remains that of Iteration 149. The comparator is not a promotable ansatz.

Literature anchors checked in this iteration:

- Biswas, Koivisto & Mazumdar, arXiv:1302.0532 — flat-space propagator structure for covariant nonlocal gravity;
- Boos, Frolov & Zelnikov, arXiv:1802.09573 — explicit exponential ghost-free form factors in linearized gravity.

## Linear TT response

On the six frozen spacelike probes, `x=p^2>0`:

`chi_NL(x;lambda)=exp(-lambda x)/x`.

Freeze `lambda0=1`; tangent:

`d chi_NL/d lambda = -exp(-x)`.

## C5 local-EFT quotient

Through operator dimension 12 the linear TT C5 local quadratic sector supplies five spin-2 response directions proportional to

`1, x, x^2, x^3, x^4`.

Add conservative common response gain `1/x`.

Hence

`M_lin=[1/x,1,x,x^2,x^3,x^4]`.

On the six frozen rows:

- `rank(M_lin)=6/6`;
- singular values `[5.361740309851116, 0.9122735096188504, 0.09152031666598426, 0.003016262356184155, 0.00016461267514139312, 2.0503891667857544e-07]`;
- `smin/smax=3.8241112956843014e-08`;
- condition number `2.6149866535750397e7`.

Direct solve reconstruction errors:

- finite nonlocal response: `4.440892098500626e-16` max abs;
- lambda tangent: `1.1102230246251565e-16` max abs.

## New retained negative result

`QG-NL-NG-001 — SIX_PROBE_LINEAR_TT_SPACE_SATURATED_BY_LOCAL_EFT_PLUS_GAIN`.

The six-coordinate linear TT protocol is fully saturated by allowed C5 local quadratic directions plus common gain. No nonlocal linear tangent can produce an algebraic residual in this finite sector.

Classification: **REGIME-SPECIFIC NON-IDENTIFIABILITY / PROTOCOL SATURATION**.

It is not exact theory identity.

Retain guardrail:

`NG-FUNNEL-015 — FINITE_SAMPLE_SATURATION_IS_NOT_THEORY_IDENTITY`.

## BLOCKED

The same nonlocal action's cubic vertex and source-completed nonlinear Ward identity remain unimplemented. `chi2R`, `N2`, `C3sym`, non-TT/scalar completion and full nonlocal quotient are BLOCKED. These are not zero entries.

No `ANSATZ-003`; no Fisher/resources.

## Stable readiness rubric

`MODEL_READINESS: 20%`

New rule applied starting here. For continuity, Iteration 157 is reconstructed at 18% under the same rubric. Iteration 158 adds 2 points only to comparator foundation by fixing and testing a concrete nonlocal strong-QG block.

- comparator foundation: `20/25`;
- unique residual discovery: `0/20`;
- frozen parent dynamics/ANSATZ: `0/20`;
- consistency/positivity/Ward/causality: `0/15`;
- identifiability/Fisher: `0/10`;
- resource/experiment closure: `0/10`.

The score does not credit infrastructure volume and does not treat comparator residuals as Candidate Gravity residuals.

## Next gate — Iteration 159

Derive the first nonlinear/cubic `chi2R` block of `QG-NL-EXP-001` from the same covariant action, including form-factor variation and contact terms needed for diffeomorphism/Ward consistency. If no finite unambiguous implementation is available without additional arbitrary prescription, record `BLOCKED_NONLOCAL_VERTEX_SPECIFICATION` and switch to one explicit asymptotic-safety vertex truncation.
