# Recovery Delta — Iteration 509

**MODEL_READINESS: 24%**  
**Infrastructure: 100%**

## New numerical authority
Rank22 `(u,v)=(+2.5e-6,-5e-6)`, HALF local index 8, multiplicity 1, is raw-consumed PASS.

Canonical provenance: run `34053331578`, job `101540723619`, artifact `9996510520`, head `3c50345c19fff8e41b8333921ff25a6cbf7dbc38`, artifact digest `sha256:3370f13c34c2060616f6311f594107526948656c365dbcf623c4e3435a15fc17`, result SHA-256 `311c15e99d71dbf38529a248d5b2cd99c89d6d656e098d58370c61aa214feba0`, authority-audit SHA-256 `bf9b139e7dc810d55cf811f88169a6fcf032885a172449e6904cf3cfec544610`.

Observed `80/80` finite, max scaled MP80↔MP120 `3.83354568012384696441586399316e-80 <= 1e-30`, max radial Richardson scaled error `2.56445151996503781362143041011e-15 <= 5e-4`.

Certified occurrence-weighted support is now `27/32 = 84.375% = 2160/2560` rows.

Authority record: `candidate_gravity/results/post508_rank22_raw_consumption.json`.

## Active heavy gate
Only rank23 `(u,v)=(+2.5e-6,-2.5e-6)`, HALF local index 9, multiplicity 1, is authorized next. Canonical run `34058694183`, job `101555199703`, trigger head `c4cb2a2bf294c550260ce1163abd392a9a039707`. First live check: queued, `0%` execution. Do not duplicate.

If rank23 raw-valid PASS: support becomes `28/32 = 87.5%`, and only rank24 `(+2.5e-6,+2.5e-6)`, HALF local index 10, may follow. If BLOCKED: stop support progression and localize the failing sample without changing frozen dynamics, support order, thresholds, MP levels, radial hs, or angular grid.

## Nonclaims
Rank22 PASS is local numerical precision/provenance only. Physical index 2 remains unresolved under Iteration 421 `BLOCKED_CONVERGENCE`; assembled BASE/HALF closure, robust residual, Candidate-Gravity consistency, comparator novelty, ANSATZ-003, Fisher, and resources remain unpromoted.
