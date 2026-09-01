# Candidate Gravity — Iteration 228: C3 PQCG ordered metric-CTP authority re-audit

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Purpose

Re-audit `BLOCKED_C3_CTP_ORDERED_COMPLETION` from the current repository authority, explicitly including the final published 2026 Phys. Rev. X covariant classical-quantum path-integral paper rather than relying only on the linearized stochastic/MSR-JD treatment.

No C3 zero-fill, no Candidate Gravity ansatz, and no Fisher/resource step is allowed in this iteration.

## Authority checked

1. J. Oppenheim and Z. Weller-Davies, *Covariant Path Integrals for Quantum Fields Backreacting on Classical Space-Time*, Phys. Rev. X **16**, 031007 (published 15 July 2026), DOI `10.1103/2rcd-dzcf`.
2. J. Oppenheim and M. Sajjad, *Stochastic modes in postquantum classical gravity*, arXiv:`2605.05375` (6 May 2026).
3. Repository structural certificate from Iteration 173 and authority reconciliation from Iteration 189.

## Material correction to the old blocker statement

Iteration 173 correctly proved a structural fact: a fixed nonlinear drift plus only a **linear** diffusion/noise Hessian does not determine the cubic two-response-field vertex if the field dependence of the diffusion kernel is unspecified.

However, the final 2026 PRX paper supplies more nonlinear parent information than the Iteration-189 wording credited to the literature. In its gravity construction:

- the CQ protoaction uses Einstein-Hilbert plus matter dynamics;
- the diffusion part is written covariantly in terms of the Einstein residual;
- the action is explicitly stated to admit an MSR representation via Hubbard-Stratonovich auxiliary fields;
- and, crucially, Eq. (26) gives a metric-dependent generalized Wheeler-DeWitt tensor density

`D0^{munurhosigma}(g) = [1/(8 D2)] (-g)^(-1/2) [g^{murho} g^{nusigma} + g^{musigma} g^{nurho} - 2 beta g^{munu} g^{rhosigma}]`

(up to index-placement convention as printed).

Therefore the broad statement "the nonlinear metric dependence of the diffusion kernel is absent from published authority" is too strong for this declared parent family. Once Eq. (26), `beta`, `D2`, metric parametrization and index convention are frozen, its ordinary metric variation is not a free `lambda`-type coefficient.

This is a real comparator-authority improvement and must be retained.

## Why the RQIR ordered nonlinear column is nevertheless still BLOCKED

The 2026 stochastic-modes paper explicitly linearizes around Minkowski space. Its Appendix A establishes OM/MSR-JD/SDE consistency at the level used for the two-point response analysis, and it also identifies a crucial issue: the ultralocal generalized DeWitt covariance is not conserved. The paper explains that naive JD/MSR use of that non-conserved kernel can give a different propagator from the diffeomorphism-invariant OM action, and restores linear-level equivalence by treating the conserved sector/projection carefully.

That is enough to invalidate the old *reason* for the blocker, but not enough to produce the required six-row nonlinear ordered RQIR object. The remaining authority gap is now narrower:

1. **C3-MISS-1 — nonlinear conserved response kernel/projection.** A full nonlinear conserved diffusion/response completion compatible with the Bianchi identity and the chosen Eq.-(26) parent must be fixed. Ordinary variation of the non-conserved DeWitt tensor alone is not sufficient authority for the physical ordered response field vertex.
2. **C3-MISS-2 — nonlinear gauge/constraint completion.** The response auxiliary-field sector must be reduced/projected consistently on metric configurations modulo diffeomorphisms, including the nonlinear constraint sector; the 2026 MSR/JD construction used for explicit propagators is linearized.
3. **C3-MISS-3 — ordered metric-source map.** RQIR needs an explicit same-parent map from the physical MSR/JD response functional to the ordered/retarded metric-source observable used in the linked cut/soft quotient, including Ward/source completion.
4. **C3-MISS-4 — common parameter convention.** `beta`, `D2`, Einstein normalization, metric perturbation convention, source normalization and any regularization/pole prescription must remain one declared convention across `K2`, the nonlinear response vertex and the soft observable.
5. **C3-MISS-5 — six-row nonlinear extraction.** Only after items 1–4 are fixed may the ordered finite-soft `O(k_soft^2)` rows be evaluated in the frozen RQIR protocol.

## Classification

`BLOCKED_C3_CTP_ORDERED_COMPLETION`

More precisely:

`BLOCKED_NONLINEAR_CONSERVED_RESPONSE_AND_ORDERED_SOURCE_COMPLETION`

This is **operational/scientific authority BLOCKED**, not a consistency FAIL of PQCG, not an exact comparator identity, not evidence for a zero C3 column, and not Candidate Gravity novelty.

## New retained results

- `C3-NG-007 — PRX2026_FIXES_A_METRIC_DEPENDENT_GENERALIZED_DEWITT_PARENT_KERNEL_SO_THE_OLD_GENERIC_FREE_LAMBDA_ARGUMENT_IS_NOT_THE_FINAL_C3_BLOCKER`.
- `C3-NG-008 — LINEAR_OM_MSR_EQUIVALENCE_WITH_CONSERVED_PROJECTION_DOES_NOT_YET_CERTIFY_THE_NONLINEAR_ORDERED_METRIC_RESPONSE`.
- `REL-NG-008 — A_NONCONSERVED_DEWITT_KERNEL_MAY_NOT_BE_VARIED_AND_USED_DIRECTLY_AS_A_PHYSICAL_NONLINEAR_RQIR_RESPONSE_COLUMN`.
- `C3-BLOCK-002 — FIVE_EXPLICIT_NONLINEAR_CONSERVED_RESPONSE_AND_ORDERED_SOURCE_INGREDIENTS_REMAIN_FOR_C3`.
- `NG-FUNNEL-084 — NARROWING_A_COMPARATOR_BLOCKER_IS_AUTHORITY_PROGRESS_NOT_A_NOVELTY_CERTIFICATE`.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 227. The C3 blocker is materially narrowed and one previously claimed missing ingredient is corrected, but the ordered C3 comparator coordinate itself is still not available. Comparator foundation remains `24/25`; robust unique residual remains `0/20`.

## Exact next gate

Iteration 229 should test whether the nonlinear **conserved** response kernel can be constructed uniquely from the declared PRX Eq.-(26) parent plus Bianchi/gauge projection without introducing a new model choice. Start analytically at first order in the metric perturbation around Minkowski and ask whether conservation fixes the longitudinal completion of `delta D2[g]`. If multiple conserved completions survive with the same linear two-point authority, certify underdetermination and keep C3 blocked. If unique, derive the corresponding cubic response vertex before any RQIR soft-row evaluation.
