# RQIR Research Log — Iteration 161

**Date:** 2026-08-31  
**MODEL_READINESS: 23%**

## Starting point

Iteration 160 refined the full asymptotic-safety comparator blocker to the missing Lorentzian retarded/in-in Green-function prescription for nonlocal operators.

Iteration 161 isolates the local IR derivative expansion of the same primary-source action, for which this nonlocal causal ambiguity is absent.

## Primary-source IR action

The reconstructed AS form factors are expanded at small `Delta` as

`f_Ricci2 ~= g_Ricci2 + c1 Delta`,

`f_R2 ~= g_R2 + c2 Delta`.

Published rounded values:

- `g_Ricci2 ~= -0.40`;
- `g_R2 ~= 1.9`;
- `c1 = 344.09`;
- `c2 = -136.75`.

This gives a local action built from

`R`, `R_mn R^mn`, `R^2`, `R_mn Box R^mn`, `R Box R`.

## Result 1 — exact structural C5 inclusion in strict IR

The Iteration-149 C5 off-shell convention is a complete unreduced local diffeomorphism-invariant covariant EFT basis through dimension 12, including Ricci/EOM-redundant operators.

Every operator in the AS local IR action is therefore an allowed C5 local Wilson direction.

Retained:

`AS-NG-003 — LOCAL_IR_AS_SUBSET_OF_C5_EFT`.

In the controlled local IR regime, the selected AS truncation has no action-level novelty relative to the C5 local EFT family.

This is a comparator degeneracy, not a consistency failure of asymptotic safety.

## Result 2 — current six probes cannot use the local IR surrogate

Created:

- `analysis/as_ir_c5_embedding_iteration161.py`;
- `results/as_ir_c5_embedding_iteration161.json`.

Taylor coefficients derived directly from the Appendix-H fits are

- `g_Ricci2=-0.40129099999999995`;
- `c1=344.0672259121935`;
- `g_R2=1.87751`;
- `c2=-136.7511182955081`,

consistent with the source's rounded Appendix-G coefficients.

Comparing the first-order IR expansion to the full fits on all 18 individual legs of the six Iteration-149 probes gives relative errors:

- Ricci-squared form factor: `1666.969 ... 69310.077`;
- R-squared form factor: `45.023 ... 384.894`.

Therefore the frozen probes with `k^2 ~= 0.23 ... 0.75 M_Pl^2` are not in a controlled first-order IR Taylor regime for these fits.

Classification:

`FAIL_DOMAIN_OF_VALIDITY` for using the local IR expansion as a numerical replacement for the blocked full AS comparator on the current protocol.

## New funnel result

`NG-FUNNEL-018 — LOCAL_LIMIT_DEGENERACY_DOES_NOT_COMPLETE_NONLOCAL_COMPARATOR`.

A local derivative expansion may prove comparator degeneracy in its controlled regime but cannot be extrapolated to finite momentum to fill a blocked nonlocal retarded response.

## Readiness change

`MODEL_READINESS: 23%`, up from 22%.

Updated stable accounting:

- comparator foundation `20/25`;
- robust unique residual `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

The +1 point is awarded only because a genuine comparator sector is now classified: strict local-IR AS is inside C5 EFT and the current protocol is quantitatively shown not to be in that IR surrogate regime.

## Next gate — Iteration 162

Strengthen C5 itself by explicitly deriving source-completed six-probe retarded columns for

- `R_mn R^mn`;
- `R^2`;
- `R_mn Box R^mn`;
- `R Box R`.

The structural C5 inclusion is already exact at action level; Iteration 162 should turn it into an explicit finite ordered-response/rank certificate and test protocol saturation.
