# Recovery Delta — Iteration 375

**Date:** 2026-09-04  
**MODEL_READINESS:** 24% (`+0 pp`)  
**Classification:** `PASS_TRU1SQ_SIMPLE_DOUBLE_AND_DOUBLE_DOUBLE_AUXMASS_DISTRIBUTIONAL_ORACLE`

## Scope
Method validation only for the 36 simple-double and 15 double-double timelike `Tr U1^2` channels frozen by Iteration 372. No physical repeated-cut `Tr U1^2` value is evaluated here.

Frozen same-`i0` identities:

\[
D_1^{-2}D_2^{-1}=-\partial_{\mu_1^2}\big[(D_1+\mu_1^2)^{-1}D_2^{-1}\big]_{\mu_1^2=0},
\]

\[
D_1^{-2}D_2^{-2}=+\partial_{\mu_1^2}\partial_{\mu_2^2}\big[(D_1+\mu_1^2)^{-1}(D_2+\mu_2^2)^{-1}\big]_{0,0}.
\]

The plus sign in the double-double case is the product of the two single-double minus signs.

## Raw validated result
- run: `33813067035`
- job: `100839109162`
- workflow head: `6f01b300fec1cb9bd6e0cd3d1eb475422001b183`
- artifact: `9915525281`
- artifact digest: `sha256:0ba79d4f8fced6714d7483a253fc14df49251f8e892e7f93ae62d618b3841599`
- raw scientific JSON SHA-256: `f9bd2f186f55338bd73783ff9cd575f9176be29b316529af2f18053ee72209d6`
- sentinel/schema audit: PASS, one top-level JSON, expected iteration 375, `scientific_authority_pass=true`.

Maximum observed errors under prospectively frozen thresholds:
- regulated simple-double direct vs auxiliary derivative: `1.7408297026122455e-13` < `1e-8`;
- regulated double-double direct vs mixed auxiliary derivative: `3.7337533065340267e-10` < `2e-9`;
- simple-double cubic `epsilon -> 0` extrapolation: `8.446889955493475e-06` < `2e-5`;
- double-double cubic `epsilon -> 0` extrapolation: `1.1110216624476976e-05` < `3e-5`;
- exact shifted-delta auxiliary oracle: `1.6468437724626028e-10` < `2e-9`.

## Consequence
The derivative sign/order/normalization machinery required by the repeated-cut `Tr U1^2` sector is methodically validated. This does **not** authorize ordinary-simple substitution. The next physical prerequisite is exact timelike kinematic separation under symmetric auxiliary-mass probes for all 51 repeated-cut channels, keeping pole orientation and the three `q^2` coordinates separate.

## Guardrails
- same `i0` on all auxiliary-mass shifts;
- repeated poles are never ordinary simple cuts;
- distinct `q^2` discontinuity variables are never summed;
- unsupported is `BLOCKED`, never zero-filled;
- no source/Born subtraction;
- no `ANSATZ-003`, Fisher/resources, or blind full-C5.

MODEL_READINESS: 24%
