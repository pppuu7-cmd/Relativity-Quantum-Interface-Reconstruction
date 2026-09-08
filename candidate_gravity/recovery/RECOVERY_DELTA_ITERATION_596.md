# Recovery Delta — Iteration 596

Date: 2026-09-08

## Authoritative change
Iteration 596 prospectively freezes and raw-validates the nonlinear Ward contract required by Iter595 before any full cubic Ward numerical classification.

Canonical provenance:
- contract commit: `ff3777613e85a23fc2f13c474cffc21bf155cae2`;
- audit-code commit: `741d67d3992689e9e63c83c43936ebc084711d7f`;
- workflow/head commit: `ad06a639b7d8e31fee1111e1c84c8b2018b416d0`;
- run `34230071486`, job `102073684316`;
- artifact `10057381903`, digest `sha256:cb066bda0040be91eb63ffe41e5e53ed336231d97a2ef3f69eb28847d8806ecd`;
- raw `result.json` SHA-256 `314d23356df4d1ce1213b6783d2e5420ef496ea41932bb9462f005b972907868`;
- raw authority audit SHA-256 `829ac0d5e07bbc8da613877b329a81b0a3fae166b7c44d915c7d40916051f674`.

Independent raw consumption found `failures=[]` and classification
`PASS_PROSPECTIVE_FULL_NONLINEAR_WARD_CONTRACT_FREEZE_AND_ONE_LEG_REDUCTION__NON_RESIDUAL`.

## Frozen contract
Fourier convention is `f(x)=int exp(-ik.x)f(k)` with stripped generator `Delta_xi=i delta_xi`. The later full cubic Ward target must contain all five classes:
1. gauge-leg linear contraction;
2. spectator-u nonlinear Lie derivative;
3. spectator-v nonlinear Lie derivative;
4. left scalar/source endpoint transformation;
5. right scalar/source endpoint transformation.

The exact Iter588 fixture is inherited, not retyped. Raw audit gives zero momentum-closure error and max q2 map error `5.551115123125783e-17`. Spectator-free reduction reproduces the exact Iter587 coefficients at `s={1,0.34,0.14}` to <= `1.1102230246251565e-16`.

No K3, K1/K2 placement or K1^3 chain may be removed family-by-family. Source/Born subtraction and source-to-Iter582 mapping remain NOT_PERFORMED.

## Classification boundary
This is a pre-result contract/reduction PASS only. It is not a nonlinear Ward PASS/FAIL, not Candidate-Gravity model PASS/FAIL, not a comparator identity and not a robust comparator-subtracted residual.

`ANSATZ-003`, Fisher and resources remain forbidden.

MODEL_READINESS: 24%

## Exact next gate
Evaluate the full same-parent Iter594 13-family cubic Green-function response for all three cyclic gauge-leg choices on the exact Iter588 fixture under the frozen Iter596 recursion, including both spectator Lie-derivative terms and both scalar endpoint terms. Raw-consume the artifact before classification. Only full source-level Ward closure may unlock source-to-Iter582/native-linked mapping and then the fixed comparator quotient.
