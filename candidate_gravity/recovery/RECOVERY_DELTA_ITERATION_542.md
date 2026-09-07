# Recovery Delta — Iteration 542

Date: 2026-09-07

## Rank3 raw-consumed authority
Canonical QUARTER rank3 coordinate: `(-1.25e-6,-2.5e-6)`.

Provenance:
- run `34115105768`
- job `101719973617`
- artifact `10018745243`
- artifact digest `sha256:06744daefa9766aca586b679769eb9767cd0a898936ec7a1159e06759575a5dc`
- head `ec77639ef423249426ee9b5b560b0662521f56a9`
- result SHA-256 `5ff2918ca522e689f8c67dc0f007efe8fd4a0bc70a5aba2d62423dc3dc4b35e0`
- authority-audit SHA-256 `391a96fca3d9a404cada35b2a0723a820ae3464e729f7c753e7068655c795e71`

Raw validation:
- `80/80` finite
- max scaled MP80↔MP120 `2.24677866944927398508872509213e-80 <= 1e-30`
- max radial Richardson scaled error `2.55939921382769490570222562317e-15 <= 5e-4`
- artifact audit `scientific_authority_pass=true`

Classification: `PASS_RAW_CONSUMED_ITER424_QUARTER_SUPPORT_RANK3_MP80_MP120__NON_PROMOTING`.

QUARTER new-support closure becomes `3/12`; full 16-grid coordinate coverage including four exact HALF-overlap corners becomes `7/16 = 43.75%`. No physical index promotion occurs.

## Anti-idle successor
At the post-rank3 check there were `0 queued / 0 in_progress` RQIR runs. The next frozen Iteration-532 rank was therefore launched without changing science:
- rank4 coordinate `(-1.25e-6,-1.25e-6)`
- stage commit `c7c022bf4abda08b079efa596d2f88a2880d869d`
- workflow commit `a2bdee8b15515f918ceeb35e862b753cca552322`
- trigger/head commit `0cb2f04ada4092c4d173a50276fffb36415109cf`
- run `34126397439`
- job `101755969291`
- state at recovery write: `in_progress`

Frozen Iteration-424 thresholds, direct-parent observable, MP80/MP120 precision, z/phi/radial nodes and Iteration-532 successor order are unchanged. Workflow green is not authority; rank4 requires fail-closed raw artifact consumption.

Physical/operator authority remains Iteration 411. Blocker authority remains Iteration 421 `BLOCKED_CONVERGENCE`, unresolved `[2]`. Robust comparator-subtracted residual remains absent; `ANSATZ-003`, Fisher/resources remain BLOCKED.

`MODEL_READINESS: 24%`

Exact next gate: fail-closed raw-consume rank4 after terminal completion. Only raw-valid PASS authorizes frozen rank5 `(-1.25e-6,+1.25e-6)`; scientific FAIL/BLOCKED stops advancement, operational failure permits only minimal repair of rank4.
