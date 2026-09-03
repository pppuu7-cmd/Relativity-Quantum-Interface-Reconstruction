# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 309**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority.

## Authoritative state

Iteration 307 freezes the complete eight-family `e=1,c=2` weight-completed `Tr U1` normalized cut at frozen `s=0.016`:

`D_s TrU1[e=1,c=2] = -0.5157080054161807`, with fitted combined cut `1/epsilon` residue `1.2896746939995822e-09`.

Iteration 308 freezes the `e=2,c<=1` cubic placement/null-soft map:

- `Tr U2`: 30 raw placements, 18 singleton-soft kills, 12 survivors = 2 at each `N_L,V1_L,H,V1_R,N_R,Y` site.
- `Tr U1^2`: 42 raw placements, 26 kills, 16 ordered survivors = 8 cyclic classes.
- mixed soft-hard `V1^(2)`/`V2^(2)` vertices are retained, never zero-filled.

Iteration 309 freezes the typed U2 operator/index and first-background-variation contract:

`(U2)^a_b = N_L^a_c (V1_L)^c_I H^I_J (V1_R)^J_d N_R^d_e Y^e_b`.

The exact first-background derivative has six site insertions, matching the Iteration-308 two-survivors-per-site census. Numerical typed-contract audits pass:

- finite-difference relative residual `1.2814180793518664e-10` <= `5e-9`
- cyclic-trace absolute residual `8.526512829121202e-14` <= `1e-9`.

Validated Iteration-309 provenance:

- run `33706649537`
- job `100497090836`
- head `a4dd40dfc2e06744c631558bd11a9f437276947d`
- artifact `9875434395`, digest `sha256:df67ff16cc42710d4260b50ed0f2eea28bfeb400a53244db8b38bea6cec08810`
- scientific JSON SHA-256 `13212ec8aa06c5d1d85e0f57bf1a030ca0169d01edcb6eda3744749385db9c8e`
- exactly one top-level JSON object, sentinel `309`, authority validator PASS.

Freeze:

`PASS_E2C1_U2_TYPED_OPERATOR_INDEX_AND_FIRST_VARIATION_CONTRACT__PHYSICAL_COMPONENT_KERNELS_REMAIN_BLOCKED`.

Physical `V1_1`, mixed `V1_2`, `H0`, `H1` remain BLOCKED; no e2c1 numerator reconstruction is authorized from Iteration 309 alone.

## Active C5 sectors

Iteration 246 already closes generic connection `e=3,c=0`; do not reopen it.

- connection `e=1,c<=2`: `Tr U1` normalized cut frozen by Iteration 307
- connection `e=2,c<=1`: active
- determinant `e=0,c<=3`: open.

## Running process

Independent non-duplicating Iteration 310 is active:

- workflow `rqir-iteration310-e2c1-tru1sq-routing-contract`
- run `33706762120`
- head `552958d76a22c6963c98258bcf61e00d5a62def5`
- code commit `8a3c9a86ead767f9551a8d56ae9d724e4199cf8e`
- last checked status: `in_progress`
- task: freeze the exact mapping of the eight surviving cyclic `Tr U1^2` classes onto authoritative `U1=N_L V2 N_R Y` primitive routing using cyclic trace equivalence only, with no reversal quotient and no invented coefficients.

Do not duplicate this run.

## Current blockers / downstream

1. Consume/validate Iteration 310 raw artifact; workflow status alone is insufficient.
2. Physical U2 `V1_1/V1_2/H0/H1` same-parent component extraction remains BLOCKED until explicit authoritative formulas are frozen.
3. If Iteration 310 passes, the independent `Tr U1^2` routing prerequisite is closed; no numeric coefficient may be inferred without its same-parent primitive/routing evaluation.
4. Then either resolve the U2 physical-component blocker or continue the nearest independent determinant `e=0,c<=3` operator/placement prerequisite if not already frozen.
5. Source/Ward/contact completion and matched `K2` bridge remain required before source/Born subtraction.
6. Only then perform the fixed comparator quotient.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

## Retained guardrails

- Unsupported comparator/kernel coordinates are `BLOCKED`, never zero-filled.
- Do not create `ANSATZ-003` until a concrete robust residual survives the fixed comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not promote weighted-B3 proxy residues to actual `Tr U1` authority.
- Source/Born subtraction only in a matched observable after pole/cut-origin classification.
- Do not accept green Actions without sentinel/schema/raw artifact audit.
- Do not accept failed Actions as scientific FAIL without schema-valid preserved diagnostics.
- No unproven left/right or reversal quotient for U2 or U1^2 classes.
- Mixed soft-hard EOM vertices are not zero-filled.
- Blind heavy full-C5 remains unauthorized.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Exact next gate

Consume Iteration 310. If PASS, freeze the eight `Tr U1^2` routing classes as a closed prerequisite. Then resolve/freeze same-parent physical `V1_1`, `V1_2`, `H0`, `H1` for the 12 U2 survivors; if that remains externally blocked, proceed only with the nearest independent determinant `e=0,c<=3` prerequisite rather than inventing unsupported kernels.
