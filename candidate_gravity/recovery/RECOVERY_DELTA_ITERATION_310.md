# RQIR Candidate Gravity Recovery Delta — Iteration 310

Date: 2026-09-03

MODEL_READINESS: 24%

## Authority

Iteration 310 freezes the exact routing/cyclic-class contract for the eight surviving `Tr U1^2` classes in the active `e=2,c<=1` sector, reusing authoritative `U1 = N_L V2 N_R Y` primitives and applying cyclic trace equivalence only.

Freeze:

`PASS_E2C1_TRU1SQ_EIGHT_CYCLIC_CLASSES_MAPPED_TO_AUTHORITATIVE_U1_ROUTING_CONTRACT`

Validated Actions provenance:

- run `33706762120`
- head `552958d76a22c6963c98258bcf61e00d5a62def5`
- artifact `9875470186`, `iteration310-result`
- artifact digest `sha256:2af3ddb3eb78885713e8e8ca4642573b5334f04464a559199a96f8c196b08903`
- scientific JSON SHA-256 `1d8b776f65ad55eb3878114edebbbfdf0050c233cc0b5e16b7ed80d4358e839a`
- exactly one top-level JSON object, sentinel `310`, `scientific_gate_pass=true`.

## Exact result

The 16 ordered surviving `Tr U1^2` orientations from Iteration 308 reduce to exactly 8 cyclic classes. These are indexed by hard singleton first-order leg `{a,b}` times second-order extra site `{V2,N_L,N_R,Y}`. No reversal identification is used. Mixed soft-hard second-order `V2` is retained.

No new numeric U1 coefficients are introduced by this gate.

## Downstream

Physical U2 `V1_1/V1_2/H0/H1` remains BLOCKED pending same-parent component formulas. To avoid idle compute, independent determinant `e=0,c<=3` operator bookkeeping was launched as Iteration 311.

MODEL_READINESS: 24%

Change: `0 pp`.
