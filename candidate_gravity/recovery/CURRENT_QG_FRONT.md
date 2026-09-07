# Candidate Gravity Current Front

**Updated:** 2026-09-07  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest validated physical/operator authority: **Iteration 411**.
- Latest raw-valid physical blocker: **Iteration 421 — `BLOCKED_CONVERGENCE`**, unresolved double-double index 2 / class 3 / `q^2=-1`; exact unresolved physical set `[2]`.
- BASE/HALF local mass support: **Iteration 523**, `32/32 = 100% = 2560/2560` across 28 distinct coordinates.
- Independent BASE/HALF MP80/MP120 assembly: **Iteration 527**, raw-valid `PASS_RAW_CONSUMED_INDEPENDENT_BASE_HALF_MP80_MP120_ASSEMBLY__NON_PROMOTING`.
- QUARTER exact support manifest: **Iteration 529** — 16-grid, 4 exact HALF-overlap corners, 12 new coordinates required.
- Three-level exact Gram/full-rank: **Iteration 530**.
- Three-level exact normalized stencil conditioning: **Iteration 531**, scale-free `kappa_2 ≈ 1.0437827450`.
- Full 12-rank QUARTER successor order prospectively frozen: **Iteration 532**.
- Three-level central4 truncation/convergence diagnostic prospectively frozen: **Iteration 533**.
- QUARTER rank1 raw-consumed numerical authority: **Iteration 534**, `PASS_RAW_CONSUMED_ITER424_QUARTER_SUPPORT_RANK1_MP80_MP120__NON_PROMOTING`.
- Rank2 canonical launch authority: **Iteration 535**.
- Exact three-level h4/h6 error-component inversion diagnostic: **Iteration 536**.
- Exact h4/h6 inversion conditioning audit: **Iteration 537**, `kappa_2 ≈ 42.7789181466` in the stated unscaled `[A,B]` coefficient convention.
- Latest authoritative research iteration: **Iteration 537**.

## Active heavy computation
Exactly one active QUARTER computation is authorized and running:
- rank: **2/12** new coordinates;
- coordinate: `u=-2.5e-6`, `v=+1.25e-6`;
- run: `34102627559`;
- job: `101680313500`;
- head/trigger commit: `1046545619a9ae564eb7e611708e4e3db7b5eb42`;
- live state at Iteration-537 inspection: run still `in_progress`; raw audit/artifact are not yet scientific authority.

No duplicate rank1/rank2 heavy Action is authorized.

## Iteration 534 — rank1 is genuine raw authority
Run `34094463024`, job `101654832475`, artifact `10010910464`, artifact digest `sha256:26ad590859e09f5fec5fa305f2a4b220d7b01858bb1fe8e60b01d8d2b6474005`, source head `25c4f3ff1c2bf9ef66e0e5db6ace6580da4bb08d`.

`result.json` SHA-256 `fc63881cc09c0e6082b05f11f401a82239488e61537d5c9d47b2cb70bb138b3c`; `authority_audit.json` SHA-256 `6ae8733caa78aaa2ae84c015f48335757c23cb809ea4fd0fb3cd1857d7bb7f8a`. Result hash exactly matches the artifact authority audit.

Frozen rank1 coordinate `(-2.5e-6,-1.25e-6)`:
- sample count `80/80`;
- all finite;
- max scaled MP80↔MP120 discrepancy `2.67210524913693857468296510677e-80 <= 1e-30`;
- max radial Richardson scaled error `2.5593700156479497761768907837e-15 <= 5e-4`.

Therefore rank1 is raw-consumed PASS. New QUARTER-support closure is **1/12 = 8.333333333333334%**. Including four exact HALF-overlap corners, authoritative full QUARTER-grid coordinate coverage is **5/16 = 31.25%**. This does not promote physical index 2.

Machine-readable authority: `candidate_gravity/results/iteration534_iter424_quarter_rank1_raw_consumption.json`.

## Iteration 535 — rank2 launched without scientific drift
Rank2 stage `candidate_gravity/code/post534_iter424_quarter_support_rank2_full_z_mp_stage.py` binds Iteration-534 raw PASS and validates the Iteration-532 rank sequence before selecting `(-2.5e-6,+1.25e-6)`.

Workflow `.github/workflows/rqir-post534-iter424-quarter-rank2-full-z-mp.yml` preserves unchanged direct-parent evaluation, `h=1.25e-6`, MP80/MP120, z nodes `[-0.86,-0.43,0,0.43,0.86]`, 16 phi nodes, radial h values `[0.002,0.001,0.0005]`, MP threshold `1e-30`, radial threshold `5e-4`, no zero-fill and no physical promotion.

Workflow green alone will not be accepted. The raw artifact must be consumed before rank2 authority is assigned. Raw-valid rank2 PASS permits only prospectively frozen rank3 `(-1.25e-6,-2.5e-6)`.

## Iteration 536 — exact h4/h6 truncation-error decomposition
Under the already frozen smooth central4 expansion, write `X_h=D+A+B+C+O(h^10)` with `A=a h^4`, `B=b h^6`, `C=c h^8`, and define `d1=BASE-HALF`, `d2=HALF-QUARTER`.

Exact component diagnostics are
- `Ahat=(-16 d1+1024 d2)/45 = A-(17/64)C+O(h^10)`;
- `Bhat=(256 d1-4096 d2)/189 = B+(425/336)C+O(h^10)`;
- `R3=(BASE-80 HALF+1024 QUARTER)/945 = D+C/1344+O(h^10)`.

Classification: `PASS_ITER424_THREE_LEVEL_H4_H6_ERROR_COMPONENT_INVERSION_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

## Iteration 537 — h4/h6 inversion conditioning is distinct from stencil conditioning
For `[d1,d2]^T=M[A,B]^T`,

`M=[[15/16,63/64],[15/256,63/4096]]`,

with exact `det(M)=-2835/65536 != 0` and

`M^{-1}=[[-16/45,1024/45],[256/189,-4096/189]]`.

The exact unscaled Euclidean condition number in `[A,B]` coordinates is

`kappa_2(M)=sqrt((31064193+sqrt(962877176430849))/(31064193-sqrt(962877176430849))) ≈ 42.7789181466`.

Classification: `PASS_ITER424_H4_H6_INVERSION_CONDITIONING_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

This does not contradict Iteration 531: normalized stencil rows have `kappa_2≈1.04378`, while extracting separate h4/h6 truncation components from only two inter-level differences is a different, more sensitive coordinate-dependent inverse problem. No model-level near-degeneracy claim is made. This diagnostic cannot rescue or replace any frozen physical clause.

## Frozen Iteration-532 QUARTER order
1. `(-2.5e-6,-1.25e-6)` — **raw PASS at Iteration 534**
2. `(-2.5e-6,+1.25e-6)` — **running at Iteration 535**
3. `(-1.25e-6,-2.5e-6)`
4. `(-1.25e-6,-1.25e-6)`
5. `(-1.25e-6,+1.25e-6)`
6. `(-1.25e-6,+2.5e-6)`
7. `(+1.25e-6,-2.5e-6)`
8. `(+1.25e-6,-1.25e-6)`
9. `(+1.25e-6,+1.25e-6)`
10. `(+1.25e-6,+2.5e-6)`
11. `(+2.5e-6,-1.25e-6)`
12. `(+2.5e-6,+1.25e-6)`.

PASS advances only to the next listed rank. Scientific FAIL/BLOCKED stops advancement and localizes the concrete failure under unchanged science. Operational failure permits only minimal technical repair and rerun of the same rank. Result-dependent reordering/skipping, unsupported u↔v substitution, zero-fill, threshold weakening, mass-node changes and precision changes are forbidden.

## Three-level structural diagnostics retained
Iteration 530 exact Gram matrix:
`[[4225/5184,4/81,0],[4/81,4225/324,64/81],[0,64/81,16900/81]]`, exact row rank 3.

Iteration 531 normalized correlations: `rho(B,H)=64/4225`, `rho(B,Q)=0`, `rho(H,Q)=64/4225`; scale-free stencil-row condition number approximately `1.0437827450`. The three-level rows are not near-linearly dependent.

Iteration 533 exact central4 expansion begins
`D_h f = f' - h^4 f^(5)/30 - h^6 f^(7)/252 - h^8 f^(9)/4320 + O(h^10)`.
Prospectively frozen diagnostics after QUARTER assembly include the leading-h4 difference ratio 16, `R_BH=(16H-B)/15`, `R_HQ=(16Q-H)/15`, and `R_3=(B-80H+1024Q)/945`. Iterations 536–537 additionally give exact h4/h6 component inversion, h8 contamination coefficients, and the separate inversion-conditioning certificate. These are diagnostics only and can never replace or rescue the frozen physical gate.

## Frozen Iteration-424 physical acceptance
After all 12 new QUARTER coordinates and QUARTER assembly are raw-closed, physical index 2 requires all simultaneously:
1. physical mass-step discrepancy `<=2e-5`;
2. direct original-integrand cross-check `<=2e-6`;
3. tensor-degree-(1,1) fit residual `<=2e-5`;
4. fixed-node MP80/MP120 agreement `|D_s(80)-D_s(120)|<=2e-6`;
5. finite outputs.

Only full PASS promotes index 2 and authorizes frozen exact15 continuation. A computed failing clause is a scoped scientific FAIL for this fallback route; an uncomputed clause is BLOCKED.

## Retained comparator blocker
Iteration 504 remains `BLOCKED_FIXED_COMPARATOR_QUOTIENT_UPSTREAM_TARGET_NOT_ASSEMBLED__NON_PROMOTING`: the concrete upstream algebraic `Source/Ward/contact+K2` target and robust comparator-subtracted residual are absent. ANSATZ-003 remains uncreated; Fisher/resources remain forbidden.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iteration 537 closes a genuine diagnostic-conditioning subgate, but no additional model-level rubric sector is complete.

## Exact downstream chain
BASE/HALF support **CLOSED 523** → provenance **CLOSED 526** → BASE/HALF assembly **CLOSED 527** → QUARTER manifest **529** → Gram/conditioning/truncation diagnostics **530–533, 536–537** → rank1 **RAW PASS 534** → rank2 **RUNNING 535** → ranks3–12 in frozen order → QUARTER assembly → unchanged Iteration-424 five-clause physical reevaluation → exact15 → full `Tr U1^2` → `D_s Gamma_{e=2}` → Source/Ward/contact+K2 → fixed comparator quotient → robust nonzero residual.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative/scoped results are preserved. No blind heavy retry. No unsupported `u<->v` substitution. Exact coordinate overlap may share local precision certificates but never derivative weights. BASE-minus-HALF is derived and not an independent Fisher constraint. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated until a concrete residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
