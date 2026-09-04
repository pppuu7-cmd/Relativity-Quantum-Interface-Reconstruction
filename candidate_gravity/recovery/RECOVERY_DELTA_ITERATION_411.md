# Candidate Gravity Recovery Delta — Iteration 411

Date: 2026-09-04

MODEL_READINESS: 24%

## Fresh source-of-truth audit

At entry, `CURRENT_QG_FRONT.md` named Iteration 409 as latest validated Candidate Gravity physical/operator authority, with unresolved Tr(U1^2) double-double indices `[2,11]` and Iteration 410 active as a structure-only split recovery oracle. Latest recovery, recent commits, queued/in-progress Actions and newly completed relevant runs were checked before advancing the front.

## Iteration 410 raw structural authority

Run `33847425175` completed `success`, but workflow colour is not used as scientific authority. Both per-index artifacts were downloaded and raw-audited independently.

- Index 2: artifact `9928039298`, artifact digest `sha256:0f2d759480a688fb71db5542c20429f79beea1737708ec92665c82cb8ba7db2f`; raw scientific JSON SHA-256 `dbaea9b9d015d6df7ab465c0748596462949eb682a8a2a662f88b5d667e8d2c7`. Classification `PASS_TRU1SQ_BLOCKER2_ANALYTIC_AZIMUTH_STRUCTURE_SPLIT_RECOVERY`; class 3, q^2=-1; maximum denominator-affine scaled error `1.6653345369377348e-16`, Fourier tail `4.741306450460151e-16`, phase mean `8.279509890185555e-16`, held-out polynomial error `3.795791805871751e-16`.
- Index 11: artifact `9928100131`, artifact digest `sha256:efdeb91cf58ed05c7b06bf300823e20e9b1f46dcb8c01b8dec24112bef662114`; raw scientific JSON SHA-256 `2ecfc9d9812a8258803e20e6e402df3c93dac2f0245bf61e390517839605693b`. Classification `PASS_TRU1SQ_BLOCKER11_ANALYTIC_AZIMUTH_STRUCTURE_SPLIT_RECOVERY`; class 16, q^2=-0.34; maximum denominator-affine scaled error `2.7755575615628914e-16`, Fourier tail `1.726456434411605e-16`, phase mean `3.9310460268893177e-16`, held-out polynomial error `2.019326546254252e-16`.

Both structural gates therefore PASS at the frozen Iteration-410 thresholds. They certify executability only and promote no physical D_s value. Physical blockers `[2,11]` remain open until the physical reduction converges and raw authority is validated.

## Iteration 411 physical gate

The next authorized model gate has been created and launched as a two-job split physical reduction, one target per job. It specializes the already validated Iteration-407 analytic/spectral physical program only by target identity and iteration labels; the Iteration-379/389 physical integrand, central4 x central4 auxiliary-mass stencil, sign `D_s=-sphere_mean[d_u d_v G]`, held-out original-integrand cross-check, and all thresholds are unchanged.

Evaluator commit: `1e01f7f4abf3ee00daafcf3580019a74ada9a670`.
Workflow/head commit: `a50b25c408903112dc6962487b58478a7f34e3f3`.
Run: `33851983789`.
Launch state at recording: `queued`.

Iteration 411 is ACTIVE / NOT YET SCIENTIFIC AUTHORITY. Each target must be consumed fail-closed from its own raw artifact. `CONVERGED` removes only that index; `BLOCKED_CONVERGENCE` remains a physical blocker and is never zero-filled.

The older repaired Iteration-408 run may still be executing due to a race, but it is structural-only and superseded operationally by the already raw-validated Iteration 410; it must not duplicate or override Iteration 411 physical authority.

## Exact next gate

Raw-consume both Iteration-411 per-index artifacts. If both are `CONVERGED`, assemble exact 15/15 double-double q^2 sums, then complete `Tr U1^2` from Iteration 374 + Iteration 393 + complete double-double. Only after that may `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` be assembled q^2-by-q^2 using Iteration 406 TrU2. If either physical target remains BLOCKED, preserve that negative result and diagnose the fixed-mass/mass-step representation without threshold weakening or blind angular-grid escalation.

MODEL_READINESS: 24%

Change: `0 pp`; structural executability was closed for the two blockers, but no stable readiness-rubric bucket closes until the physical coordinate and downstream comparator quotient close.
