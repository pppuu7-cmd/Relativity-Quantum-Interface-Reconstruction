# Iteration 173 — fixed PQCG diffusion/MSR ordered CTP completion audit

**Date:** 2026-08-31  
**Comparator:** `C3-PQCG-NL-001`  
**Status:** `BLOCKED_C3_CTP_ORDERED_COMPLETION`  
**MODEL_READINESS: 24%**

## Question

Can the missing diffusion-dependent ordered cubic `r/a` relation of the fixed postquantum-classical gravity comparator be derived uniquely from the same dynamics and parameter convention already authoritative in Iterations 153–155?

## Starting authority

Iteration 153 fixes the linear stochastic spin-2/spin-0 covariance convention `(D2,D0)`. Iteration 154 fixes a nonlinear Onsager–Machlup pure-gravity action and obtains a nonzero symmetric classical third cumulant. Iteration 155 fixes the common Einstein-drift tree causal response but explicitly leaves diffusion/MSR ordered corrections blocked.

No new diffusion kernel, discretization prescription, or response-field/CTP identification may be introduced ad hoc.

## Literature audit

The 2026 Oppenheim–Sajjad stochastic-mode analysis is decisive for this gate.

1. It explicitly compares Onsager–Machlup and Janssen–De Dominicis / Martin–Siggia–Rose formulations.
2. For the ultra-local generalized DeWitt diffusion choice, the naive JD/MSR response functional does **not** reproduce the same two-point function as the OM action.
3. The paper traces the mismatch to the non-conserved diffusion tensor and then introduces an alternative **conserved diffusion matrix** that restores the linearized consistency.
4. The explicit conserved-diffusion SDE displayed there is linearized, `G^(1)_mn = xi_mn`; the paper does not provide the unique nonlinear covariant conserved kernel required to derive the full cubic response-field sector around the same background.
5. The tensor TT response-field sector avoids the linear gauge complication, but that does not fix the nonlinear field dependence of the diffusion kernel nor a unique map from the classical MSR response field to the RQIR metric CTP `a` leg.

Relevant published anchors:

- J. Oppenheim and M. Sajjad, *Stochastic modes in postquantum classical gravity*, arXiv:2605.05375 (2026), Appendix A, especially the JD/MSR comparison and conserved-diffusion discussion.
- J. Oppenheim and Z. Weller-Davies, *Covariant Path Integrals for Quantum Fields Backreacting on Classical Space-Time*, Phys. Rev. X 16, 031007 (2026), DOI `10.1103/2rcd-dzcf`.

## Structural underdetermination certificate

To isolate what the existing authority can and cannot determine, consider one projected stochastic mode with response functional

`S = t (L h + g h^2/2 - J) - 1/2 t (D0 + lambda h) t`.

Here `t` is an MSR response field. This is **not** asserted to be the tensorial PQCG action; it is a minimal algebraic witness for the information content of the fixed lower-order data.

At background `h=t=0`,

`H_linear = [[0,L],[L,-D0]]`,

which is independent of `lambda`. Therefore all values of `lambda` share the same linear response/noise Hessian.

At cubic order,

`Gamma_(t h h) = g`,

`Gamma_(t t h) = -lambda`,

`Gamma_(t t t) = 0`.

Thus the nonlinear drift fixes the one-response-field cubic vertex `g`, while the linear covariance does not fix the two-response-field cubic vertex. A nonlinear field-dependent conserved diffusion completion is needed to determine it.

This reproduces exactly the conceptual gap exposed by the literature audit: the fixed Iteration-153 linear noise plus Iteration-155 Einstein drift do not determine the diffusion-dependent ordered cubic response-field vertex.

Reproducible authority:

- `analysis/c3_pqcg_msr_completion_audit_iteration173.py`;
- `results/c3_pqcg_msr_completion_audit_iteration173.json`.

## Why no `Gamma_aar` or `Gamma_aaa` column is entered

The RQIR relation matrix uses amputated metric CTP vertices `(Gamma_arr,Gamma_aar,Gamma_aaa)`. The published PQCG construction has a single classical metric plus quantum `+/-` matter histories; its MSR auxiliary field is not automatically identical to the metric CTP `a` field used for a closed quantum metric comparator.

Therefore even the formal MSR response-field vertices cannot be inserted into the RQIR CTP matrix without an explicit same-convention mapping. Assigning

`Gamma_aar = 0`, or `Gamma_aaa = 0`,

from Gaussian-noise intuition alone would be a zero-fill of unsupported coordinates and would violate `NG-FUNNEL-011`.

## Classification

### `C3-NG-005 — LINEAR_NOISE_PLUS_NONLINEAR_DRIFT_DO_NOT_FIX_ORDERED_MSR_CUBIC_VERTEX`

The currently fixed PQCG linear covariance and Einstein nonlinear drift do not uniquely determine the diffusion-dependent two-response-field cubic vertex. This is **operational underdetermination / BLOCKED**, not a consistency FAIL of PQCG.

### `NG-FUNNEL-033 — OM_TO_MSR_CUBIC_COMPLETION_REQUIRES_NONLINEAR_CONSERVED_DIFFUSION_AND_EXPLICIT_CTP_MAP`

A nonlinear OM probability action cannot be converted into an RQIR ordered CTP comparator by simply introducing an auxiliary response field. The same two-point authority, conserved diffusion convention, nonlinear kernel and CTP/MSR identification must be fixed first.

## Consequence for Iteration 172 relation matrix

The supported C3 tree relation direction from Iteration 172 remains valid because it came directly from the fixed Einstein drift. No additional C3 diffusion-dependent relation column is authorized by the current parent dynamics.

The Iteration-172 complement remains **not a novelty certificate**. The correct status is

`BLOCKED_C3_CTP_ORDERED_COMPLETION`.

This blocker does not justify weakening the C3 comparator or setting the missing entries to zero.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 172.

Comparator foundation is better audited, but no robust residual has been created and no Candidate Gravity parent dynamics exists. The rubric therefore receives no additional model-readiness credit.

## Next gate

Move to the next fixed relation-level comparator rather than inventing C3 columns: audit a nonlinear source-completed real-time nonlocal comparator with a declared covariant form-factor action. Determine whether its amputated cubic relation is fixed by the same form factors or whether independent cubic form factors enter. If independent data are required, record the precise nonlocal blocker; only then proceed to asymptotic-safety real-time relation completion.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN.
