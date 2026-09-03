# Recovery Delta — Iteration 377

**Date:** 2026-09-04  
**MODEL_READINESS:** 24% (`+0 pp`)  
**Classification:** `PASS_TRU1SQ_REPEATED_CUT_MASS_PROBE_KINEMATIC_SEPARATION__REGULAR_51__BLOCKED_0`

## Scope
Physical kinematic-separation prerequisite only for all repeated-cut `Tr U1^2` channels. No repeated-cut discontinuity is integrated in this gate.

Authoritative inputs: Iteration 372 topology (`36` simple-double + `15` double-double) and Iteration 375 auxiliary-mass derivative identities.

Probe contract: every double cut group uses `mu^2={-1e-5,0,+1e-5}`; a simple cut group remains massless. Double-double channels use the full Cartesian 3x3 probe grid. The uncut denominator range is minimized analytically over the full two-particle cut sphere, not by angular point sampling.

## Validated result
- channels: `51`
- simple-double: `36`
- double-double: `15`
- `REGULAR=51`
- `BLOCKED=0`
- channels per q2: `17` for each of `-1.0`, `-0.34`, `-0.14`
- minimum analytic uncut absolute denominator: `0.11857147221810005` > frozen `1e-10`
- maximum cut-shell absolute error: `1.2622654386573035e-16` < frozen `2e-12`
- maximum q2 absolute error: `5.551115123125783e-17` < frozen `1e-12`
- minimum Kallen function over all probes: `0.019594400000000005` > frozen `1e-12`

## Provenance
- run: `33813366983`
- job: `100840032070`
- workflow head: `e8de37295817456a36acc6289898342804a143ac`
- artifact: `9915623215`
- artifact digest: `sha256:f6f1860a74a6d84c24023b2a7e8c1d131f9133e2eba00ed743d098d225946c4b`
- raw scientific JSON SHA-256: `e27aa368470c4c0091cf72956b4ef13302f8a6cc979519c199aa2a63444ae2a5`
- sentinel/schema audit: PASS; expected iteration 377; one top-level JSON; `scientific_authority_pass=true`.

## Consequence
The 51 repeated-cut channels may proceed to physical derivative integration without ordinary-simple substitution. The next numerical stage should be resource-aware: simple-double and double-double sectors should be separated, with symmetric auxiliary-mass derivative(s), independent step-size and angular convergence tests, and q2 buckets preserved separately.

## Guardrails
Same `i0`; repeated poles are not ordinary simple cuts; no q2 summation; unsupported=`BLOCKED`; no source/Born subtraction; no `ANSATZ-003`; no Fisher/resources; no blind full-C5.

MODEL_READINESS: 24%
