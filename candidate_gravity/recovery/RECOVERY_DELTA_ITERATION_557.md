# RECOVERY DELTA — ITERATION 557

Date: 2026-09-07

## New exact diagnostic authority
For the frozen central4 x central4 mixed auxiliary-mass stencil, the coefficient matrix is symmetric under `u<->v`. Therefore the exchange-odd component of the **complete** fixed-mass grid cancels exactly from the mixed derivative, and the assembled derivative equals the derivative assembled from exchange-even pair averages.

Machine-readable authority: `candidate_gravity/results/iteration557_iter424_central4_exchange_even_projection_exact.json`.

This is diagnostic/provenance authority only. It does not permit missing-node inference or support substitution because Iterations 552–555 establish that `F(u,v)` and `F(v,u)` are generally different routed values. Both values remain required to construct the exchange-even average.

## Future assembly check
After all QUARTER nodes are raw-closed, independently assemble:
1. the ordinary full-grid central4 x central4 mixed derivative;
2. the same derivative from exchange-even pair averages.

They must agree algebraically; disagreement is an implementation/indexing/weight/orientation failure, not a scientific threshold failure.

## Active heavy process retained
Rank9 remains the sole authorized heavy successor after Iteration 556:
- coordinate `(u,v)=(+1.25e-6,+1.25e-6)`;
- run `34160111095`;
- job `101859912600`;
- head `7be4b22384c6680d669e88c0fb7990ba53ceff3e`.

Do not duplicate it. On terminal completion, raw-consume fail-closed before any rank10 launch.

MODEL_READINESS: 24%
