# Recovery Delta — Candidate Gravity Iteration 342

Date: 2026-09-03

MODEL_READINESS: 24%

## Scope

Same-parent `N/Y` inverse-routing bridge required by the physical Vilkovisky `U2` operator. The gate combines the primary relations of Giacchini, de Paula Netto & Shapiro (2020) with the already-frozen Iteration-317 minimal ghost operator `hat N = delta Box + R` in `D=4`, `Lambda=0`, `a=-1/2`.

The generic gauge-fixing convention together with the gravity gauge gives

`Y_lower=-g`, `Y_upper=-g^{-1}`,

and

`hat N = Y_upper N_lower`.

Therefore

`hat N^{-1} = N_upper Y_lower`,

`N_upper = hat N^{-1} Y_upper`.

## Result

Freeze:

`PASS_U2_SAME_PARENT_NY_INVERSE_ROUTING_BRIDGE_WITH_PHYSICAL_GHOST_N1__FIRST_BACKGROUND_TRU2_ASSEMBLY_AUTHORIZED_NEXT`.

The test uses the actual physical Iteration-317 `N1` kernel and a two-momentum block `{p,p+q}`. It validates both the shifted inverse identity

`Q1(q;p) = -Q0(p+q) N1(q;p) Q0(p)`

and the complete `N/Y` identities by independently inverting the block operators.

Key numerical residuals:

- flat parent identity: `1.3877787807814457e-17`;
- left shifted inverse identity: `4.440892098500626e-16`;
- right shifted inverse identity: `1.1102230246251565e-16`;
- direct two-momentum block inverse: `4.671944434071913e-15`;
- `Y_upper Y_lower = 1`: exact to reported precision (`0.0`);
- `N_upper = Q Y_upper`: `4.391615997560502e-15`;
- `N_upper Y_lower = Q`: `4.4267192589395986e-15`;
- explicit first-order left-N route: `4.506429307853555e-15`;
- Eq. (57) flat-sign calibration: `0.0`.

All are far below the frozen `1e-11`/`1e-12` thresholds.

## Actions provenance

- run `33768535939`
- job `100692511687`
- head/workflow commit `3009940a82eb74373ff6b4b433078e58abce65f4`
- code commit `45e9cb1d4f015193120291f167022ac0d96c052b`
- artifact `9898566243`, `iteration342-result`
- artifact digest `sha256:0900cebca21a189d610eaa7820ad84bc41c4115bd518aed016bf2d8b185697e8`
- scientific JSON SHA-256 `a247b6b27c38c92af10616653d6e0737cc0059572f0f68970810a2586c9fa2d9`
- exactly one top-level JSON object, sentinel `342`, `scientific_authority_pass=true`.

Scientific result is retained at `candidate_gravity/results/iteration342_u2_ny_inverse_routing_bridge.json`.

## Consequence

The two physical component blockers that remained after Iteration 340 are now closed:

- `A1/A2`: frozen executable by Iteration 341;
- `N/Y` inverse routing: frozen executable by Iteration 342.

Together with Iteration 339 shifted graviton inverse routing and Iteration 340 `A.T/A` orientation plus `Hinv_VD=-K^-1`, the first-background-order physical `Tr U2` assembly is now authorized.

This is not yet a `Tr U2` cut or Candidate residual.

## Exact next gate

Iteration 343: assemble the complete first-background-order physical `Tr U2` from the six typed Iteration-309 derivative sites, retaining explicit momentum routing at every operator factor. Independently validate the assembled trace against a direct finite-block derivative of the complete `U2` product before any Cutkosky integration or Source/Born subtraction.

Guardrails unchanged: no zero-fill, no Source/Born subtraction, no ANSATZ-003, no Fisher/resources, no blind full-C5.

MODEL_READINESS remains 24% because no full readiness bucket and no comparator-subtracted residual have closed yet.
