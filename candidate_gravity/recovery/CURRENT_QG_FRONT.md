# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 310**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority.

## Authoritative state

Iteration 307 freezes the complete eight-family `e=1,c=2` weight-completed `Tr U1` normalized cut at frozen `s=0.016`:

`D_s TrU1[e=1,c=2] = -0.5157080054161807`, with fitted combined cut `1/epsilon` residue `1.2896746939995822e-09`.

Iteration 308 freezes `e=2,c<=1` placement/null-soft bookkeeping: `Tr U2` has 12 surviving ordered placements (2 at each `N_L,V1_L,H,V1_R,N_R,Y` site); `Tr U1^2` has 16 ordered survivors = 8 cyclic classes. Mixed soft-hard vertices are retained, never zero-filled.

Iteration 309 freezes the typed U2 index/variation contract

`(U2)^a_b = N_L^a_c (V1_L)^c_I H^I_J (V1_R)^J_d N_R^d_e Y^e_b`,

with finite-difference residual `1.2814180793518664e-10` and cyclic-trace residual `8.526512829121202e-14`. Physical `V1_1/V1_2/H0/H1` component kernels remain BLOCKED.

Iteration 310 freezes the exact routing contract for the eight surviving cyclic `Tr U1^2` classes, indexed by hard singleton first-order leg `{a,b}` times second-order extra site `{V2,N_L,N_R,Y}`. Only cyclic trace equivalence is used; no reversal quotient and no new numeric U1 coefficients are introduced.

Validated Iteration-310 provenance:

- run `33706762120`
- head `552958d76a22c6963c98258bcf61e00d5a62def5`
- artifact `9875470186`, digest `sha256:2af3ddb3eb78885713e8e8ca4642573b5334f04464a559199a96f8c196b08903`
- scientific JSON SHA-256 `1d8b776f65ad55eb3878114edebbbfdf0050c233cc0b5e16b7ed80d4358e839a`
- exactly one top-level JSON object, sentinel `310`, `scientific_gate_pass=true`.

Freeze:

`PASS_E2C1_TRU1SQ_EIGHT_CYCLIC_CLASSES_MAPPED_TO_AUTHORITATIVE_U1_ROUTING_CONTRACT`.

## Active sectors

Iteration 246 already closes generic connection `e=3,c=0`; do not reopen it.

- connection `e=1,c<=2`: `Tr U1` cut frozen by Iteration 307
- connection `e=2,c<=1`: U2 physical components BLOCKED; U1^2 routing frozen through Iteration 310
- determinant `e=0,c<=3`: active independent route.

## Running process

Iteration 311 is queued:

- workflow `rqir-iteration311-det-e0c3-cubic-logdet-contract`
- run `33706890915`
- head `5b7e33b01a9a3b724ffd662398b6ea7c331ff281`
- code commit `dc4ffeffa8e309d6ab86ae5a63251f79ccf944fa`
- last checked status: `queued`
- task: freeze the exact cubic operator/logdet topology for determinant `e=0,c<=3` using `H=H0+tH1+t^2H2+t^3H3+...`, without physical-component invention or heavy full-C5 integration.

Do not duplicate this run.

## Exact next gate

Consume/validate Iteration 311 artifact. If PASS, freeze same-parent determinant graviton/ghost `H1,H2,H3` component conventions and routing before scoped numerator/cut evaluation. If those physical components are unavailable, record them BLOCKED rather than zero-fill. In parallel, U2 physical `V1_1/V1_2/H0/H1` remains BLOCKED pending explicit same-parent formulas.

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
- Source/Born subtraction only in a matched observable after pole/cut-origin classification.
- Do not accept green Actions without sentinel/schema/raw artifact audit.
- Do not accept failed Actions as scientific FAIL without schema-valid preserved diagnostics.
- No unproven reversal quotient for U2 or U1^2 classes.
- Blind heavy full-C5 remains unauthorized.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.
