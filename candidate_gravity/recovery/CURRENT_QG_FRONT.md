# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 312**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority.

## Authoritative state

Iteration 307 freezes the complete eight-family `e=1,c=2` weight-completed `Tr U1` normalized cut at frozen `s=0.016`:

`D_s TrU1[e=1,c=2] = -0.5157080054161807`, with fitted combined cut `1/epsilon` residue `1.2896746939995822e-09`.

Iteration 308 freezes `e=2,c<=1` placement/null-soft bookkeeping: `Tr U2` has 12 surviving ordered placements; `Tr U1^2` has 16 ordered survivors = 8 cyclic classes. Mixed soft-hard vertices are retained, never zero-filled.

Iteration 309 freezes the typed U2 index/variation contract

`(U2)^a_b = N_L^a_c (V1_L)^c_I H^I_J (V1_R)^J_d N_R^d_e Y^e_b`,

while physical `V1_1/V1_2/H0/H1` component kernels remain BLOCKED.

Iteration 310 freezes the exact routing contract for the eight surviving cyclic `Tr U1^2` classes, using cyclic trace equivalence only.

Iteration 311 is retained as a negative numerical-audit result: its schema-valid artifact failed the small-|t| degree-6 polynomial-fit cubic extraction. This failure is diagnosed as an ill-conditioned numerical audit and is not promoted as an analytic identity refutation.

Iteration 312 independently freezes the determinant `e=0,c<=3` exact cubic logdet operator topology under

`H(t)=H0+t H1+t^2 H2+t^3 H3+O(t^4)`:

`[t^3] log det H = Tr(G0 H3) - 1/2 Tr(G0 H1 G0 H2) - 1/2 Tr(G0 H2 G0 H1) + 1/3 Tr(G0 H1 G0 H1 G0 H1)`,

`G0=H0^{-1}`.

Validated Iteration-312 provenance:

- run `33710153241`
- job `100507684815`
- head/workflow commit `18dbff26a90266d3d21848263176d3015537e048`
- code commit `dec32a0bcc6069f35c3c7abc843d94e560be4a92`
- artifact `9876618078`, digest `sha256:5ca0bc6d200a0c8e48f4a799f695442970b9b4f53406fca7f515732ca7d43bca`
- scientific JSON SHA-256 `ec5ff14b1944cafb76f31faeb6f6e6861516efb90ff0f4f84ff68f742c121553`
- exactly one top-level JSON object, sentinel `312`, `scientific_gate_pass=true`.

Freeze:

`PASS_DETERMINANT_E0C3_EXACT_CUBIC_LOGDET_OPERATOR_TOPOLOGY_HIGH_PRECISION_AUDIT__PHYSICAL_COMPONENTS_REMAIN_BLOCKED`.

## Active sectors

Iteration 246 already closes generic connection `e=3,c=0`; do not reopen it.

- connection `e=1,c<=2`: `Tr U1` cut frozen by Iteration 307
- connection `e=2,c<=1`: U2 physical components BLOCKED; U1^2 routing frozen through Iteration 310
- determinant `e=0,c<=3`: exact cubic topology frozen through Iteration 312; same-parent physical graviton/ghost components are the active prerequisite.

## Running process

No determinant physical component numerator/cut computation is authorized until explicit same-parent `H1/H2/H3` and ghost `N1/N2/N3` formulas/routing have repository authority. Unsupported components must remain BLOCKED.

Iteration 313 is the exact next lightweight authority-inventory gate: inspect repository sources for those formulas/routing, emit exact provenance when present, otherwise a typed BLOCKED certificate and identify any independent permitted prerequisite. It must not infer formula authority from keyword presence alone.

## Exact next gate

Run/consume Iteration 313 repository-authority inventory. If authoritative same-parent determinant component formulas are present, freeze their conventions/routing before any scoped numerator/cut evaluation. If absent, record determinant physical layer BLOCKED rather than zero-fill and pursue only an independent prerequisite explicitly permitted by the then-current front. U2 physical `V1_1/V1_2/H0/H1` remains independently BLOCKED pending explicit same-parent formulas.

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
