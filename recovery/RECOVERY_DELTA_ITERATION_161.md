# Recovery Delta — RQIR Iteration 161

**Date:** 2026-08-31  
**MODEL_READINESS: 23%**  
**Authoritative change:** strict local-IR asymptotic-safety sector classified as a C5-EFT subset; using that IR expansion on the current six probes is forbidden by a quantitative domain audit.

## New authorities

- `candidate_gravity/ASYMPTOTIC_SAFETY_IR_C5_AUDIT_ITERATION161.md`;
- `analysis/as_ir_c5_embedding_iteration161.py`;
- `results/as_ir_c5_embedding_iteration161.json`;
- `research_log/2026-08-31_iteration_161_as_ir_c5_embedding.md`;
- `recovery/RECOVERY_DELTA_ITERATION_161.md`.

## Scientific result A — local IR AS is inside C5 EFT

The primary-source local IR action contains

- `R`;
- `R_mn R^mn`;
- `R^2`;
- `R_mn Box R^mn`;
- `R Box R`.

Iteration 149 froze the C5 off-shell family as a complete unreduced local covariant EFT basis through dimension 12, explicitly including Ricci/EOM-redundant directions. Hence every AS IR operator is already a C5 local EFT direction.

Retained:

`AS-NG-003 — LOCAL_IR_AS_SUBSET_OF_C5_EFT`.

Classification:

`EXACT_STRUCTURAL_DEGENERACY_WITH_LOCAL_C5_EFT_FAMILY` in the **strict controlled IR derivative-expansion regime**.

Do not call this a failure of asymptotic safety.

## Scientific result B — local IR expansion is invalid on the current six probes

The Appendix-H fit Taylor coefficients are

- `g_Ricci2=-0.40129099999999995`;
- `c1=344.0672259121935`;
- `g_R2=1.87751`;
- `c2=-136.7511182955081`.

On the 18 legs of the six frozen Iteration-149 probes, first-order IR-vs-full-fit relative errors are

- Ricci2: `1666.9691403682948 ... 69310.07731333924`;
- R2: `45.02312154387796 ... 384.89448594867974`.

Thus the local IR truncation is not a valid numerical surrogate for the full AS form factors at `k^2 ~= 0.23 ... 0.75 M_Pl^2`.

Classification:

`FAIL_DOMAIN_OF_VALIDITY` for that surrogate use only.

The full nonlocal AS retarded tangent remains

`BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`.

## New guardrail

`NG-FUNNEL-018 — LOCAL_LIMIT_DEGENERACY_DOES_NOT_COMPLETE_NONLOCAL_COMPARATOR`.

A scoped local-limit degeneracy cannot be extrapolated outside its controlled regime and cannot fill missing nonlocal real-time response data.

## Readiness

`MODEL_READINESS: 23%` — up by one point from Iteration 160.

Accounting:

- comparator foundation `20/25`;
- robust unique residual `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

Reason for +1: strict local-IR AS comparator content is now genuinely classified relative to C5 and its domain boundary is quantitatively certified.

## Exact restart instruction

Resume at **Iteration 162**.

Implement source-completed local C5 retarded columns for the four curvature-squared/derivative operators appearing in the AS IR action:

1. `R_mn R^mn`;
2. `R^2`;
3. `R_mn Box R^mn`;
4. `R Box R`.

Use the same metric variable, conserved source, six triplets, projectors, Gaussian windows and CTP/retarded convention frozen in Iterations 147–149.

Then compute their six-probe rank/SVD and quotient against EH/gain plus existing `Ricci^3/Riemann^3` columns. Verify source-completed Ward identities. If the finite protocol saturates, record protocol saturation rather than false novelty/non-identifiability.

Do not use the AS IR coefficients as a surrogate for the full nonlocal AS response and do not create `ANSATZ-003` yet.
