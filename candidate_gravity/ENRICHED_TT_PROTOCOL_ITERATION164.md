# Candidate Gravity — Iteration 164: target-independent TT protocol enrichment

**Date:** 2026-08-31  
**MODEL_READINESS: 23%**

## Purpose

Iteration 163 saturated the six frozen TT ordered-response rows with the fixed matrix

`M6=[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full,dRGT_shared_reference]`.

That is a finite-protocol statement only.  Iteration 164 tests its stability by adding six new rows **before examining target residuals**.

## Provenance correction to Iteration 163

The two numerical target arrays used in Iteration 163 were incorrectly labelled `dRGT_alpha3` and `dRGT_alpha4`.

They are exactly the two Iteration-156 tangent columns

`[d/d log(m^2), d/d alpha3]`.

The underlying arrays and therefore the six-row saturation result are unchanged.  The correction is semantic/provenance, not numerical.  `alpha4` remains cubic-TT blind because the dRGT `L4[K]` interaction starts at quartic order.

Retain:

`PROVENANCE-CORR-001 — ITERATION163 TARGET LABELS ARE DLOGM2 AND DALPHA3; ALPHA4 REMAINS CUBIC_TT BLIND`.

## Row freeze

The first six rows are unchanged.  Six additional spacelike `(q,r,p=q+r)` triplets are generated with deterministic RNG seed `164031`:

- `q0,r0 ~ Uniform[0.08,0.24]`;
- each spatial component `~ Uniform[-0.68,0.68]`;
- accept only if `0.18 <= p^2,q^2,r^2 <= 1.05`;
- require `|cos(q_spatial,r_spatial)| <= 0.82`;
- require `max(p^2,q^2,r^2)/min(...) <= 4`.

The first six accepted proposals are frozen; acceptance occurs after 16 proposals.  Polarization seeds are `2000+3*i+leg`.  No dRGT target value enters row generation or acceptance.

## Enriched comparator quotient

The 12x6 comparator matrix is

`M12=[EH,Ricci^3,Riemann^3,Ricci^2_full,Ricci Box Ricci_full,dRGT_shared_reference]`.

It has rank `6` under all four fixed conditioning audits.  Unlike the six-row case, it no longer fills the observable row space.

For the correctly labelled targets:

- adding `d/d log(m^2)` raises raw rank `6 -> 7`;
- adding `d/d alpha3` raises raw rank `6 -> 7`;
- adding both raises raw rank `6 -> 8`.

Residual fractions across the four fixed normalizations are:

| target | min | max | classification |
|---|---:|---:|---|
| `d/d log(m^2)` | `7.4567e-4` | `4.7412e-3` | nonzero but near-degenerate |
| `d/d alpha3` | `6.7428e-3` | `9.1427e-2` | scoped residual survives local enriched TT quotient |

Raw residual fractions are `1.4785e-3` and `3.9035e-2`, respectively.

Progressively adding the target-independent new rows gives combined rank `7` after the first row and `8` from the second row onward.  Thus the loss of six-row saturation is not produced by selecting one exceptional row after seeing the targets.

## Scientific classification

Retain:

- `C4-NG-005 — SIX_ROW_SATURATION_DOES_NOT_PERSIST_UNDER_TARGET_INDEPENDENT_TT_ROW_ENRICHMENT`;
- `C4-NG-006 — DRGT_DLOGM2_DIRECTION_IS_NEAR_DEGENERATE_AFTER_ENRICHED_LOCAL_C5_QUOTIENT`;
- `NG-FUNNEL-021 — PROTOCOL_SATURATION_MUST_BE_TESTED_FOR_STABILITY_UNDER_PRE_FROZEN_ROW_ENRICHMENT`.

The `d/d alpha3` residual is **not** a Candidate Gravity novelty certificate.  The enriched C3 diffusion-dependent, weakly-nonlocal full causal, asymptotic-safety retarded, full C5 non-TT/loop, and dRGT helicity sectors are not yet all instantiated on these rows.  Unsupported comparator components remain BLOCKED rather than zero-filled.

The Iteration-163 six-row saturation remains a valid historical scoped result; it is superseded only as a statement about protocol stability.

## Readiness

`MODEL_READINESS: 23%`, up from `22%`.

Accounting:

- comparator foundation `23/25` (+1 for a target-independent enriched protocol and recomputed C4/C5 quotient);
- robust unique residual `0/20` (unchanged: full enriched comparator quotient not closed);
- parent dynamics `0/20`;
- consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

No `ANSATZ-003`; no Fisher; no resource optimization.

## Next gate

Iteration 165 must attack the **missing enriched comparator columns**, not design a candidate around the temporary `alpha3` residual.  First reuse exact boundary results where valid (the C3 tree ordered response is the common EH column after Newton calibration), then attempt the strongest derivable nonlocal / asymptotic-safety causal completion on the 12 frozen rows.  If a comparator remains causally underdetermined, record the blocker rather than filling it with zero.  Only after the fixed enriched C3/C4/C5/nonlocal/AS quotient is available may any residual be promoted.
