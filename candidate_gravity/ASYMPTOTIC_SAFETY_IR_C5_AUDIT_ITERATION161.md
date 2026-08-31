# Candidate Gravity — Iteration 161: asymptotic-safety local-IR / C5 audit

**Date:** 2026-08-31  
**MODEL_READINESS: 23%**  
**Classification:** strict local-IR AS sector is C5-degenerate; current six-probe IR surrogate fails its domain

## Objective

Iteration 160 established that the genuinely nonlocal Lorentzian AS comparator remains blocked by an unfrozen retarded/in-in Green-function prescription.

Iteration 161 isolates a sector without that ambiguity: the **local infrared derivative expansion** explicitly written in the same AS source.

Two questions are separated:

1. Does the strict local-IR AS action contain a direction outside ordinary local gravitational C5 EFT?
2. Can that local IR expansion be used numerically as a surrogate for the full AS form factors on the six frozen RQIR probes?

Answers:

1. **No** — action-level local IR content is a subset of the frozen complete local C5 EFT family.
2. **No** — the first-order IR expansion is far outside its domain on the present six probes.

## 1. Published local IR action

Pawlowski & Tränkle Taylor-expand the curvature-squared form factors as

`f_Ricci2(Delta) ~= g_Ricci2 + c1 Delta`,

`f_R2(Delta) ~= g_R2 + c2 Delta`.

The source gives approximately, in Planck units,

- `g_Ricci2 ~= -0.40`;
- `g_R2 ~= 1.9`;
- `c1 = 344.09`;
- `c2 = -136.75`.

The resulting local IR action is

`Gamma_IR = (1/16pi) int sqrt(-g) [`

`  G_N^-1 R`

`  + g_Ricci2 R_mn R^mn`

`  + g_R2 R^2`

`  + c1 R_mn Box R^mn`

`  + c2 R Box R`

`]`.

## 2. Exact structural embedding into C5 EFT

Iteration 149 froze the C5 off-shell convention as a **complete unreduced local diffeomorphism-invariant covariant operator/source basis through dimension 12**, explicitly retaining Ricci/EOM-redundant directions required off shell.

Every operator in the AS local IR action is therefore already an allowed C5 local EFT operator:

- `R`;
- `R_mn R^mn`;
- `R^2`;
- `R_mn Box R^mn`;
- `R Box R`.

The AS calculation fixes particular coefficient values; C5 EFT allows the same structures as Wilson directions.

Therefore, in the strict regime where the AS local IR truncation is valid,

`AS_IR action subset C5_local_EFT`.

No detector optimization or Fisher analysis can turn this action-level inclusion into gravity-specific novelty relative to C5.

### Retained result

`AS-NG-003 — LOCAL_IR_AS_SUBSET_OF_C5_EFT`.

This is a **regime-specific exact structural comparator degeneracy**, not a failure of asymptotic safety.

## 3. The six frozen probes are not in the strict IR Taylor regime

A dangerous shortcut would be to use the local IR action above as a numerical surrogate for the blocked full nonlocal AS response on the current Iteration-149 probes.

Iteration 161 forbids this by direct calculation.

The Appendix-H analytic fits imply Taylor coefficients

- `g_Ricci2_fit = -0.40129099999999995`;
- `c1_fit = 344.0672259121935`;
- `g_R2_fit = 1.87751`;
- `c2_fit = -136.7511182955081`,

consistent with the source's rounded Appendix-G values.

The first-order IR approximations were compared against the full analytic fits on all 18 individual spacelike legs of the six frozen triplets.

Relative-error ranges are

`Ricci2: 1666.9691403682948 ... 69310.07731333924`,

`R2: 45.02312154387796 ... 384.89448594867974`.

Thus even the **best** leg differs by factors of order tens for `R^2` and thousands for the Ricci-squared form factor. The current probe invariants `k^2 ~= 0.23 ... 0.75 M_Pl^2` are not a controlled first-order Taylor regime for these fitted form factors.

Classification:

`FAIL_DOMAIN_OF_VALIDITY` for using the local IR expansion as a surrogate on the current six-probe protocol.

This is not an AS consistency FAIL. It is a protocol/regime mismatch.

Authority:

- `analysis/as_ir_c5_embedding_iteration161.py`;
- `results/as_ir_c5_embedding_iteration161.json`.

## 4. New funnel guardrail

### NG-FUNNEL-018 — LOCAL_LIMIT_DEGENERACY_DOES_NOT_COMPLETE_NONLOCAL_COMPARATOR

If a theory's strict local derivative expansion lies inside the baseline EFT comparator family, that establishes degeneracy only in the regime where the derivative expansion is controlled. It does **not** authorize using the local expansion at finite momenta where it fails, and it does not fill a blocked genuinely nonlocal retarded tangent.

This prevents two opposite errors:

- claiming novelty from an AS local IR correction that is already ordinary C5 EFT;
- claiming full AS/C5 identity by extrapolating the local IR action outside its validity domain.

## 5. AS status after Iteration 161

- strict deep-IR local action: `EXACT_STRUCTURAL_DEGENERACY_WITH_C5_EFT_FAMILY`;
- local IR coefficients: `FROZEN_FROM_PRIMARY_SOURCE`;
- local IR approximation on current six probes: `FAIL_DOMAIN_OF_VALIDITY`;
- full Euclidean nonlocal action: `SUPPORTED_SCOPED`;
- full Lorentzian retarded nonlocal response: `BLOCKED_AS_RETARDED_GREEN_FUNCTION_PRESCRIPTION`;
- full AS RQIR quotient: `BLOCKED`.

## 6. Readiness

`MODEL_READINESS: 23%` — increased from 22% by one point.

Reason: a real portion of comparator foundation is now classified rather than merely specified. The strict local-IR AS sector is proven to be inside C5 EFT, and its use outside that regime is quantitatively ruled out.

Updated accounting:

- comparator foundation `20/25`;
- robust unique residual `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

No readiness credit is awarded for the still-blocked full nonlocal AS tangent.

## Next scientific gate — Iteration 162

The highest-value next step is to close more of the **local C5 off-shell comparator basis** that currently exists only as an allowed operator family.

Specifically derive source-completed six-probe retarded columns for the curvature-squared/derivative operators that appear in the AS IR action:

- `R_mn R^mn`;
- `R^2`;
- `R_mn Box R^mn`;
- `R Box R`.

This will:

1. turn the structural AS/C5 inclusion into an explicit finite RQIR tangent certificate;
2. strengthen the C5 comparator independently of AS;
3. reveal whether the six-probe ordered protocol has enough rank to distinguish these off-shell local directions or is already saturated/degenerate.

Do not use the AS local IR coefficients as a surrogate for the nonlocal AS model on these probes.
