# RECOVERY DELTA — ITERATION 528

Date: 2026-09-07
MODEL_READINESS: 24%

## Authority retained
- Physical/operator authority: Iteration 411.
- Raw-valid physical blocker: Iteration 421 `BLOCKED_CONVERGENCE`, unresolved set `[2]` (double-double index 2 / class 3 / `q^2=-1`).
- BASE/HALF local precision support: Iteration 523, `32/32 = 100% = 2560/2560` for the Iteration-407 BASE/HALF central4 support.
- Independent BASE/HALF assembled numerical authority: Iteration 527, raw-valid `PASS_RAW_CONSUMED_INDEPENDENT_BASE_HALF_MP80_MP120_ASSEMBLY__NON_PROMOTING`.
- No robust comparator-subtracted residual exists; ANSATZ-003/Fisher/resources remain BLOCKED.

## Why Iteration-424 is not yet directly computable from the 527 assembly
Frozen Iteration 424 requires fixed mass steps `{5e-6, 2.5e-6, 1.25e-6}` at 80 and 120 decimal digits. The `h=1.25e-6` central4 support is `{-2.5e-6,-1.25e-6,+1.25e-6,+2.5e-6}^2`. Four exact coordinates with both entries in `{+-2.5e-6}` are already certified by HALF support, but 12 coordinates containing `+-1.25e-6` are not. Unsupported remains BLOCKED; they may not be zero-filled or inferred by `u<->v` symmetry.

Iteration 428 also forbids treating an outer-only MP wrapper around the historical binary64 `F` as true Iteration-424 high precision. The allowed implementation is the direct-parent MP80/MP120 path already established during the Iterations 447–523 precision-support program.

## Iteration-528 action
Frozen deterministic quarter-step source order: central4 4x4 u-major/v-major after removal only of exact HALF-overlap coordinates. There are 12 new coordinates. First new coordinate: `(-2.5e-6,-1.25e-6)`.

Created:
- stage commit `499a433168142209f7c6eefbbd5101d0095c6536`;
- workflow commit `1a856438eea6825f7b65d1ab5eb6853782fd774b`;
- first trigger commit `ca4834015d7f4de178b67af7b5695f007be508a1`.

Initial run `34094343153`, job `101654453787` was an operational FAIL before scientific evaluation: prerequisite schema binding looked for nonexistent top-level Iteration-527 keys and returned `('iteration527_assembly_prerequisite_not_passed', None)`. Artifact `10007996294` contains only the failed empty/diagnostic result surface; it is not scientific authority.

The raw-consumption schema was checked directly. Correct binding is `iteration=527`, exact classification `PASS_RAW_CONSUMED_INDEPENDENT_BASE_HALF_MP80_MP120_ASSEMBLY__NON_PROMOTING`, and `observed.scientific_authority_pass=true`. The stage was repaired in commit `fda4756f58aba6dce09f3c91cf44e8cce8afbade` with no scientific threshold or convention change. Trigger commit `25c4f3ff1c2bf9ef66e0e5db6ace6580da4bb08d` launched repaired run `34094463024`.

## Active gate / continuation
Canonical active gate: repaired Iteration-424 quarter-support rank1 full-z/full-phi/full-radial direct-parent MP80/MP120 run `34094463024`, target `u=-2.5e-6, v=-1.25e-6`.

Fail-closed thresholds remain: MP80↔MP120 scaled discrepancy `<=1e-30` at the raw sample layer, inherited radial Richardson threshold unchanged, exactly 80 samples, all finite. Workflow success is not scientific PASS until raw artifact and `authority_audit.json` are inspected.

If raw-valid PASS: raw-consume rank1 and advance only to the next deterministic untested quarter coordinate. If BLOCKED: localize the first failing z/phi/radial sample with frozen conventions. After all 12 new quarter coordinates are raw-closed, execute the full frozen Iteration-424 three-step physical reevaluation and require all five original clauses simultaneously.

No blind full-grid retry, no threshold weakening, no physical promotion, no ANSATZ-003, no Fisher/resources.
