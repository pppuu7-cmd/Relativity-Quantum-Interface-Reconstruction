# RQIR Iteration 484 — rank12 raw PASS, rank13 launched

Date: 2026-09-06

The canonical rank12 Actions run `33997856739` / job `101391409387` completed and its raw artifact `9979716360` was downloaded and independently checked. Scientific `result.json` SHA-256 is `a7512548da32e8a5545241d179532dc8b92aec69e5e91d4e4cd40429e83fc8e1`; artifact digest is `sha256:ade9b2fbdb7f5ef623dc63c8d757db356c7426f20b6ac2ae5f09528884ce7112`.

Frozen rank12 `(u,v)=(+1e-5,-1e-5)`, multiplicity 1, passes the unchanged local numerical gate: `80/80` finite, max MP80↔MP120 scaled discrepancy `2.07719600745524401993175741985e-80 <= 1e-30`, max radial Richardson scaled error `2.56858312184114196282042364589e-15 <= 5e-4`.

Classification: `PASS_RAW_CONSUMED_MANIFEST_RANK12_FULL_Z_MP80_MP120__NON_PROMOTING`.

Certified occurrence-weighted support is now `17/32 = 53.125% = 1360/2560` row occurrences. No physical promotion follows from this local certificate.

At the anti-idle checkpoint Actions had no useful queued or in-progress RQIR run, so the exact next frozen Iteration-455 coordinate was advanced: rank13 `(u,v)=(+1e-5,-5e-6)`, multiplicity 1. New stage/workflow preserve five training-z, NPHI16, radial `{0.002,0.001,0.0005}`, direct MP80/120, and all frozen thresholds.

Canonical rank13 run `34003038811`, job `101405200967`, is now active from head `3eb81dee858b86e825939b9fabac65b57f8a1ee5`. It is not scientific PASS until raw-consumed fail-closed.

Physical/operator authority remains Iteration 411; blocker authority remains Iteration 421 with unresolved set `[2]`. Robust comparator-subtracted residual, `ANSATZ-003`, Fisher and resource work remain BLOCKED. MODEL_READINESS remains 24%.
