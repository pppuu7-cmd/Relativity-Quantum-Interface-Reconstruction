# Candidate Gravity Current Front

**Updated:** 2026-09-07  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest validated structural authority: **Iteration 410**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`.
- Exact unresolved physical set: **`[2]`**.
- Latest completed BASE/HALF local mass-support authority: **Iteration 523**, `32/32 = 100% = 2560/2560` across 28 distinct coordinates.
- Latest assembled numerical authority: **Iteration 527**, raw-valid `PASS_RAW_CONSUMED_INDEPENDENT_BASE_HALF_MP80_MP120_ASSEMBLY__NON_PROMOTING`.
- Latest authoritative research iteration: **Iteration 528**.
- Active scientific prerequisite: **frozen Iteration-424 quarter-step (`h=1.25e-6`) direct-parent MP80/MP120 support**.

## Iteration 528 — exact Iteration-424 quarter-step prerequisite
The prospective Iteration-424 contract freezes mass steps `{5e-6,2.5e-6,1.25e-6}` and precision levels `{80,120}`. Iteration 527 closes only the BASE/HALF `h={5e-6,2.5e-6}` central4 assembly. For `h=1.25e-6`, the central4 support is `{-2.5e-6,-1.25e-6,+1.25e-6,+2.5e-6}^2`. Four coordinates with both entries in `{+-2.5e-6}` are exact overlaps with already raw-certified HALF support; 12 coordinates containing at least one `+-1.25e-6` entry remain unsupported and therefore BLOCKED, never zero-filled or inferred by `u<->v` symmetry.

Iteration 428 remains binding: an outer-only MP wrapper around binary64/numpy `F` is not a true 80/120-digit fixed-node evaluation. The allowed implementation is the direct-parent MP80/MP120 path established by the Iterations 447–523 precision-support program.

Quarter-step deterministic order is frozen as central4 4x4 u-major/v-major after removal only of exact HALF-overlap coordinates. The first new coordinate is `(-2.5e-6,-1.25e-6)`. Stage commit `499a433168142209f7c6eefbbd5101d0095c6536`; workflow commit `1a856438eea6825f7b65d1ab5eb6853782fd774b`.

Initial run `34094343153`, job `101654453787` failed operationally before scientific evaluation because the new stage bound the Iteration-527 raw-consumption schema using nonexistent top-level fields. This is **not** a scientific FAIL. Direct schema inspection showed the authority is encoded as `iteration=527`, exact classification `PASS_RAW_CONSUMED_INDEPENDENT_BASE_HALF_MP80_MP120_ASSEMBLY__NON_PROMOTING`, and `observed.scientific_authority_pass=true`. Binding was repaired in commit `fda4756f58aba6dce09f3c91cf44e8cce8afbade`, with no threshold or scientific-convention change.

Canonical repaired trigger/head: `25c4f3ff1c2bf9ef66e0e5db6ace6580da4bb08d`. Canonical repaired run: **`34094463024`**. Raw artifact must be inspected before any scientific PASS is assigned.

## Frozen Iteration-424 full acceptance after quarter support closes
Full physical reevaluation remains unchanged and requires all simultaneously:
1. physical mass-step discrepancy `<=2e-5`;
2. direct original-integrand cross-check `<=2e-6`;
3. tensor-degree-(1,1) fit residual `<=2e-5`;
4. identical fixed-node 80/120-digit agreement `|D_s(80)-D_s(120)|<=2e-6`;
5. finite outputs.

Only full PASS promotes physical index 2 and authorizes frozen exact15 continuation. A computed failing clause is a scoped scientific FAIL for this fallback route. A missing/uncomputed clause is operational BLOCKED.

## Retained Iterations 525–527 authority
Iteration 526 closed BASE/HALF historical provenance with 28 frozen coordinates backed by 29 exact artifact parts because rank 10 `(+5e-6,+5e-6)` is a genuine two-artifact z-partition. Iteration 527 raw-consumed run `34089957999`, job `101641252363`, artifact `10006477417`. Scientific `result.json` SHA-256 `8ac2949e795b201efbaa70b63fb3aeef9805eecc2e6c13362b9db38f52a9e451`; `authority_audit.json` SHA-256 `f2b762b4224d15e1baa32787cb35071e1a750c769c2e8ee61567e88fa83560d8`.

Frozen assembly: all 80 samples finite; BASE MP80↔MP120 `0.0 <= 2e-6`; HALF MP80↔MP120 `0.0 <= 2e-6`; BASE↔HALF mass-step `8.60575121785458117805036434436e-7 <= 2e-5`; row rank 2; Gram determinant `5948843/559872 > 0`; `ds=-d_base`; no Richardson promotion; no threshold weakening.

## Retained comparator and physical blockers
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`: concrete upstream algebraic `Source/Ward/contact+K2` target is absent. Robust comparator-subtracted residual is absent. Iteration 421 remains raw-valid `BLOCKED_CONVERGENCE` for physical index 2 until the frozen Iteration-424 route is actually closed.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**.

## Exact downstream chain
BASE/HALF local support **CLOSED at 523** → multipart provenance **CLOSED at 526** → BASE/HALF assembly **CLOSED at 527** → Iteration-424 quarter-step 12-new-coordinate MP support **ACTIVE at 528** → frozen Iteration-424 three-step physical reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No `u<->v` support substitution without exact frozen identity. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
