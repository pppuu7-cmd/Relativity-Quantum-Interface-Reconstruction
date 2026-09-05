# Iteration 461 Recovery Delta

Date: 2026-09-05

## Authority consumed
Run `33951807833`, job `101267895504`, artifact `9966351908`, artifact digest `sha256:7fc24cc6edbe18a8f90d17373668b15b0c6a749be1519365619d1778859630ad` was raw-consumed fail-closed. The artifact's `authority_audit.json` reports scientific JSON SHA-256 `0c5be48463f88f44a409c2ef39d5b05a12ebb7aefd9e3229675ddfe7d74bbda6` and `scientific_authority_pass=true`.

At Iteration-455 distinct rank 3, `u=-1e-5, v=+1e-5`, all five frozen training-z, NPHI16, radial Richardson `{2e-3,1e-3,5e-4}`, direct MP80/120: `80/80` rows finite; max scaled MP80↔MP120 discrepancy `2.84726346368330895235928706892e-80 <= 1e-30`; max radial Richardson scaled error `2.56867316198372145008474049021e-15 <= 5e-4`.

Classification: `PASS_NEXT_MASS_NODE_FULL_Z_MP80_MP120__NON_PROMOTING`. This closes only this fixed-mass precision certificate and does not promote physical index 2.

Certified occurrence-weighted precision coverage becomes `6/32 = 18.75%`, i.e. `480/2560` row occurrences. `MODEL_READINESS: 24%`, change 0 pp.

## Next authorized gate
Only Iteration-455 distinct rank 4 is authorized: `u=-5e-6, v=-1e-5`, under unchanged five-z/NPHI16/full-Richardson/direct-MP80/120 conventions and unchanged thresholds. No blind remaining-grid sweep. If BLOCKED, localize the first failing z/phi/radial sample at exactly rank 4. If PASS, raw-consume before launching any later coordinate.

## Retained blockers
Physical/operator authority remains Iteration 411; Iteration 421 remains raw-valid physical blocker for unresolved set `[2]`. Exact15/full `Tr U1^2`, comparator-subtracted residual, `ANSATZ-003`, Fisher/resources remain BLOCKED. Unsupported is never zero-filled.
