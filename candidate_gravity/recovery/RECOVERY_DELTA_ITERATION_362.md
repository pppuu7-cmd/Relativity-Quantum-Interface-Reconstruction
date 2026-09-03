# Recovery Delta — Candidate Gravity Iteration 362

Date: 2026-09-03

## Raw Actions authority

- run: `33800631629`
- job: `100799000169`
- artifact: `9910904000` (`iteration362-result`)
- artifact digest: `sha256:7721ae5f7df7070b7a74dcba16e1271ead8c7ab0e3dbf542c3a513f806a0c7cf`
- scientific JSON SHA-256: `2f326362a1ddbaef069f859df5f72fdab31fa0ec7df12395460e0219e28eeb44`
- workflow head: `160acc4351a5e0e2d42569fb8f6b702b7dbe25a7`

Authority: `PASS_U2_REPEATED_POLE_AUXILIARY_MASS_DERIVATIVE_DISTRIBUTIONAL_ORACLE`.

All 4 smooth-test oracles pass. Maximum scaled auxiliary-derivative error is `9.825899614424007e-11` under the fixed `2e-8` threshold. The independent direct finite-eta squared-pole discontinuity with Richardson extrapolation has maximum scaled error `2.3002016237729086e-4` under the fixed `2e-3` threshold.

This validates the Iteration-359 sign/normalization bridge for one double pole with the same i0 prescription. It does not yet evaluate any physical repeated-pole U2 channel.

Exact next gate: classify all 48 repeated-pole timelike channels under the auxiliary massive-simple representation, including full-sphere analytic separation of any uncut denominator. Only channels passing this prerequisite may advance to symmetric-mu2 normalized-cut differentiation.

MODEL_READINESS: 24%
