# RQIR research log — 2026-09-05 — post447 class-3 phi/sample MP stage

- Accepted latest repo race state rather than duplicating work.
- Raw-consumed spectral-algebra MP PASS: run `33924198609`, job `101189000423`, artifact `9957221889`; max 80/120 discrepancy `2.44054108444388552441376805074e-80 <= 1e-30`; non-promoting and parent sample generation still unclosed.
- Accepted independent actual-cut parent MP pilot PASS: run `33926910105`, job `101197313961`, artifact `9957177323`; max 80/120 discrepancy `4.82848380400305053290438160355e-81`; binary64-vs-MP120 diagnostic `6.95379333966267071268483411462e-16`; non-promoting.
- Actions were idle after those completions, so anti-idle required a new scientifically admissible gate.
- Added `post447_class3_phi_sample_mp_stage.py` and workflow `rqir-post447-class3-phi-sample-mp-stage.yml`.
- Prospectively frozen staged coverage: index 2/class 3/q2=-1, `u=v=+5e-6`, z `{-0.86,0,+0.86}`, all 16 phi nodes, radial Richardson `{2e-3,1e-3,5e-4}` with both signs, direct parent recomputation at 80/120 digits, threshold `1e-30`, inherited radial threshold unchanged.
- Code commit `732483920d9563aa53f5761b26d8dd7d1f1feebd`; launch commit `8257cda2607fde9ec73245719b00671a17b43aeb`; run `33928248369` queued at launch.
- Physical/operator authority remains Iteration 411; physical blocker authority remains Iteration 421; unresolved physical set remains `[2]`.
- `MODEL_READINESS: 24%`; readiness change 0 pp.
