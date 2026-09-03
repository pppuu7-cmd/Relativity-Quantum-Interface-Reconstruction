# RQIR Candidate Gravity Recovery Delta — Iteration 312

Date: 2026-09-03

MODEL_READINESS: 24%

## Iteration 311 disposition

Iteration 311 run `33706890915` preserved a schema-valid raw diagnostic artifact but did **not** pass its scientific numerical audit. The failed degree-6 small-|t| polynomial fit is retained as a negative numerical-audit result; it is not promoted as a refutation of the exact cubic logdet identity.

- artifact `9875518186`, `iteration311-result`
- scientific JSON SHA-256 `4c15e2004277be89e942d6913448a2df6f9ae38df75f30c8e3e171fe5e357841`
- authority schema/sentinel valid, `scientific_authority_pass=false`
- disposition: `NUMERICAL_AUDIT_FAILED_DUE_TO_ILL_CONDITIONED_SMALL_T_POLYFIT__NOT_SCIENTIFIC_IDENTITY_REFUTATION`

No frozen gate was weakened post hoc. The identity was re-audited independently at high precision in Iteration 312.

## Iteration 312 authority

Iteration 312 freezes the exact cubic determinant/logdet operator topology for `e=0,c<=3` under

`H(t)=H0+t H1+t^2 H2+t^3 H3+O(t^4)`

with

`[t^3] log det H = Tr(G0 H3) - 1/2 Tr(G0 H1 G0 H2) - 1/2 Tr(G0 H2 G0 H1) + 1/3 Tr(G0 H1 G0 H1 G0 H1)`,

`G0=H0^{-1}`.

Cyclic trace equivalence gives the reduced mixed term `-Tr(G0 H1 G0 H2)`; no reversal quotient is assumed.

Freeze:

`PASS_DETERMINANT_E0C3_EXACT_CUBIC_LOGDET_OPERATOR_TOPOLOGY_HIGH_PRECISION_AUDIT__PHYSICAL_COMPONENTS_REMAIN_BLOCKED`

Validated Actions provenance:

- run `33710153241`
- job `100507684815`
- head `18dbff26a90266d3d21848263176d3015537e048`
- code commit `dec32a0bcc6069f35c3c7abc843d94e560be4a92`
- workflow commit `18dbff26a90266d3d21848263176d3015537e048`
- artifact `9876618078`, `iteration312-result`
- artifact digest `sha256:5ca0bc6d200a0c8e48f4a799f695442970b9b4f53406fca7f515732ca7d43bca`
- scientific JSON SHA-256 `ec5ff14b1944cafb76f31faeb6f6e6861516efb90ff0f4f84ff68f742c121553`
- exactly one top-level JSON object, sentinel `312`, `scientific_gate_pass=true`.

The independent 80-digit symmetric-stencil + Richardson audit has absolute cubic residual approximately `3.56e-11`, below the frozen `1e-9` threshold.

## Blocked physical layer

This topology gate does not supply same-parent physical component kernels. Therefore:

- determinant graviton `H1/H2/H3`: `BLOCKED`
- determinant ghost `N1/N2/N3`: `BLOCKED`
- U2 physical `V1_1/V1_2/H0/H1`: `BLOCKED`
- source/contact completion: `BLOCKED_DOWNSTREAM`

Unsupported components are not zero-filled.

## Exact next gate

Inventory the repository authority for same-parent determinant graviton/ghost component formulas and frozen routing. Promote only explicit authoritative formulas with path/commit provenance; otherwise emit a typed BLOCKED certificate and identify any independent currently permitted prerequisite. No scoped numerator/cut evaluation is authorized before this component gate.

MODEL_READINESS: 24%

Change: `0 pp`.
