# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 308**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority.

## Current scientific state

Iteration 307 freezes the complete eight-family `e=1,c=2` weight-completed `Tr U1` normalized cut at frozen `s=0.016`:

- bubble subsector `-0.010850153804447154`
- triangle subsector `-0.5048578516117335`
- complete `D_s TrU1[e=1,c=2] = -0.5157080054161807`
- fitted combined cut `1/epsilon` residue `1.2896746939995822e-09`.

Iteration 308 freezes the exact cubic-background placement/null-soft pruning map for the remaining connection `e=2,c<=1` sector:

- `U1 = N_L V2 N_R Y`
- `U2 = N_L V1_L H V1_R N_R Y`
- EOM-degree-2 connection contribution `+(i/2) Tr U2 -(i/4) Tr U1^2`.

For `Tr U2`: 30 raw ordered placements, 18 exact singleton-soft kills, 12 survivors = 2 at each extra site `N_L,V1_L,H,V1_R,N_R,Y`.

For `Tr U1^2`: 42 raw ordered placements, 26 exact singleton-soft kills, 16 ordered survivors = 8 cyclic trace classes.

Mixed soft-hard `V1^(2)`/`V2^(2)` terms remain retained and are not zero-filled.

Validated Iteration-308 provenance:

- run `33703692659`
- job `100488195810`
- head `2bfd7ac2cdab22aeca3f443aa329d012ab7ecb3b`
- artifact `9874425140`, digest `sha256:bfbdb7e04859109b79f337132a29d94624fa226d089dbee9f95410a8c0dc53e3`
- scientific JSON SHA-256 `7623aa20ab729d2fe13a3da8f8d464431d32fc431b042c94a712a169f125db5b`
- one top-level JSON object, sentinel `308`, validator PASS.

Freeze:

`PASS_E2C1_CUBIC_BACKGROUND_PLACEMENT_AND_NULLSOFT_PRUNING_AUDIT__EXACT_V1_H_KERNEL_IMPLEMENTATION_REMAINS`.

## Active C5 sectors

Iteration 246 already proves generic connection `e=3,c=0` null-soft; do not reopen it.

- connection `e=1,c<=2`: complete `Tr U1` normalized cut frozen by Iteration 307
- connection `e=2,c<=1`: current active route
- determinant `e=0,c<=3`: open.

## Running process

Iteration 309 is the active non-duplicating prerequisite gate:

- workflow `rqir-iteration309-e2c1-u2-typed-contract`
- run `33706649537`
- head `a4dd40dfc2e06744c631558bd11a9f437276947d`
- code commit `3a34e8ebbb6210218867efbf70078fec6ae26245`
- status when recorded: `queued`
- task: freeze the typed ghost/field index contract for `U2=N_L V1_L H V1_R N_R Y` and the exact six-site first-background Leibniz expansion, with fail-closed artifact preservation.

This gate deliberately does not invent physical `V1_1`, `V1_2`, `H0` or `H1` coefficients. Unsupported physical components remain `BLOCKED`, not zero-filled.

## Current blockers / downstream

1. Consume and validate Iteration 309 raw artifact; workflow status alone is insufficient.
2. If the typed/index/variation contract passes, extract/freeze same-parent physical `V1_1`, mixed `V1_2`, flat graviton Green/projector `H0`, and first-background `H1` in frozen `D=4, Lambda=0, a=-1/2` conventions.
3. Validate transpose/routing identities against the Iteration-309 contract before any `e=2,c<=1` numerator reconstruction.
4. Map the 8 cyclic `Tr U1^2` classes onto authoritative U1 primitive kernels without extra symmetry quotients.
5. Only then perform scoped numerator reconstruction/cut reduction for `e=2,c<=1`.
6. Then close determinant `e=0,c<=3`.
7. Source/Ward/contact completion and matched `K2` bridge remain required before source/Born subtraction.
8. Only then perform the fixed comparator quotient.

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
- Hidden evanescent coefficients are not zero; Iterations 301/304 are cut-protection statements only.
- Do not accept green Actions without sentinel/schema/raw artifact audit.
- Do not accept failed Actions as scientific FAIL without schema-valid preserved diagnostics.
- No unproven left/right or reversal quotient for U2 placements.
- Mixed soft-hard EOM vertices are not zero-filled.
- Blind heavy full-C5 remains unauthorized.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Exact next gate

Consume Iteration 309. If its typed contract passes, freeze the same-parent physical `V1_1`, `V1_2`, `H0` and `H1` component formulas and routing identities required by the 12 Iteration-308 U2 survivors; reuse authoritative U1 primitives for the 8 cyclic `Tr U1^2` classes only after their routing contract is checked.
