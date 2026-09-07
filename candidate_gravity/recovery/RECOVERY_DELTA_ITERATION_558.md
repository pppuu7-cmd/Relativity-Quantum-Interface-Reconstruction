# RECOVERY DELTA — ITERATION 558

Date: 2026-09-07

## New exact assembly-integrity authority
The frozen central4 x central4 mixed auxiliary-mass stencil now has an explicit exact moment/null/norm contract.

Machine-readable authority: `candidate_gravity/results/iteration558_iter424_central4_tensor_moment_norm_contract.json`.

Key exact checks:
- single-axis nodes `[-2,-1,+1,+2]`, integer weights `[1,-8,8,-1]`;
- moments k=0..6: `[0,12,0,0,0,-48,0]`;
- tensor integer outer matrix `[[1,-8,8,-1],[-8,64,-64,8],[8,-64,64,-8],[-1,8,-8,1]]`;
- every row and column sum exactly zero;
- tensor coefficient matrix symmetric under exchange;
- mixed L1 norm `9/(4h^2)`, L2/Frobenius norm `65/(72h^2)`, max coefficient magnitude `4/(9h^2)`.

Use these as fail-closed assembly checks after QUARTER support closure. They do not authorize missing-node inference, threshold weakening or physical promotion.

## Active heavy process unchanged
Rank9 remains the sole heavy process:
- run `34160111095`;
- job `101859912600`;
- coordinate `(u,v)=(+1.25e-6,+1.25e-6)`;
- head `7be4b22384c6680d669e88c0fb7990ba53ceff3e`.

At the last inspection setup/dependencies were complete and the full-z MP80/MP120 stage was running. Do not duplicate it.

Only raw-valid rank9 PASS may authorize rank10 `(+1.25e-6,+2.5e-6)`.

MODEL_READINESS: 24%
