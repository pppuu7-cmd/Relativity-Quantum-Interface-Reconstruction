# Candidate Gravity Recovery Delta — Iteration 412

Date: 2026-09-04

MODEL_READINESS: 24%

## Source-of-truth entry state

`CURRENT_QG_FRONT.md`, latest recovery material, recent commits, and current Actions were re-read before this step. Latest validated physical/operator authority remains Iteration 409; latest validated structural authority remains Iteration 410. Iteration-411 run `33851983789` is still active with both physical jobs (indices 2 and 11) executing the frozen analytic/spectral reduction; no raw Iteration-411 artifact exists yet, so no physical promotion is allowed.

## Prospective exact15 preassembly freeze

Iteration 412 freezes the downstream double-double and complete `Tr U1^2` assembly logic *before* Iteration-411 results can be inspected. This prevents post-result selection, zero-filling, or accidental use of the old diagnostic `BLOCKED_CONVERGENCE` values.

New reproducible code:

`candidate_gravity/code/iteration412_tru1sq_exact15_and_complete_preassembly.py`

Commit: `8d0aa6bf3a47d9e7f7616b74a672b912b77976ac`.

The contract requires:

- exactly 15 unique frozen double-double indices `0..14`;
- exactly five records in each frozen q2 bucket (`-1`, `-0.14`, `-0.34`);
- `scientific_gate_pass=true` for every input;
- physical channel status exactly `CONVERGED` for every input;
- finite `D_s_TrU1sq_double_double_channel` coordinates;
- no duplicate index, no missing index, no zero fill, and no diagnostic blocked value in any sum.

The frozen q2 map is Iteration-402 authority: indices `0..4 -> q^2=-1`, `5..9 -> q^2=-0.14`, `10..14 -> q^2=-0.34`.

Only after exact 15/15 closure does the script add the already-authoritative operator coordinates:

- Iteration 374 simple-simple: `(+6.253219881951187e-05, +3.5044107116946374e-05, +2.9297648005638963e-05)` for q2 `(-1,-0.34,-0.14)` respectively;
- Iteration 393 simple-double: `(-0.002329411286740447, -0.0005948791870822445, -7.368142632096214e-05)` for the same q2 ordering.

The output remains a `Tr U1^2` operator coordinate. The effective-action factor `-i/4` is explicitly not folded. Distinct q2 buckets remain separate.

## Scientific classification

Iteration 412 is a prospective methodological/assembly-contract PASS, not a new physical numerical result, not a Candidate residual, not a comparator identity, and not a consistency certificate. It does not supersede Iteration 409 physical authority or Iteration 410 structural authority. It becomes numerically executable only after raw-valid physical records for indices 2 and 11 exist.

## Exact next gate

1. Raw-consume both Iteration-411 artifacts fail-closed.
2. If both are `CONVERGED`, materialize the authoritative targeted records and run the already-frozen Iteration-412 exact15 assembly against all 15 raw-authority channel records.
3. Raw-validate the resulting complete `Tr U1^2` operator coordinate.
4. Only then assemble q2-by-q2 `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` using Iteration 406 `Tr U2`.
5. Source/Ward/contact + matched K2 and fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain downstream. `ANSATZ-003` remains forbidden; Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Change: `0 pp`. The exact assembly is now prospectively frozen, which reduces methodological degrees of freedom, but no new stable readiness-rubric bucket closes until physical 15/15 `Tr U1^2` and the downstream comparator-subtracted residual are obtained.
