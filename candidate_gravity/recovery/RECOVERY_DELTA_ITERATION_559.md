# RECOVERY DELTA — ITERATION 559

Date: 2026-09-07

## New exact assembly bookkeeping authority
The frozen 4x4 QUARTER central4 support grid decomposes into exactly 10 exchange orbits under `u<->v`: 4 diagonal singleton orbits and 6 off-diagonal pair orbits.

Machine-readable authority: `candidate_gravity/results/iteration559_iter424_quarter_exchange_orbit_closure_map.json`.

Current state before rank9 completion:
- fully closed exchange orbits: `7/10`;
- their integer stencil-coefficient sum: `-64`;
- rank9 diagonal orbit coefficient: `+64`.

Therefore a raw-valid rank9 PASS would give `8/10` complete exchange orbits with completed-orbit coefficient sum exactly zero. Only the two off-diagonal orbits ranks6/11 (`+16`) and ranks10/12 (`-16`) would remain incomplete; their combined integer coefficient sum is also exactly zero.

This is bookkeeping/assembly integrity only. It does not authorize rank reordering, skipped coordinates, or u↔v support substitution.

## Active heavy process
Rank9 remains the sole heavy run:
- run `34160111095`;
- job `101859912600`;
- coordinate `(u,v)=(+1.25e-6,+1.25e-6)`;
- head `7be4b22384c6680d669e88c0fb7990ba53ceff3e`.

On terminal completion, raw-consume fail-closed. Only raw-valid PASS authorizes frozen rank10 `(+1.25e-6,+2.5e-6)`.

MODEL_READINESS: 24%
