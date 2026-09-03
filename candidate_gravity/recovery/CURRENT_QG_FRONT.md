# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 339**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority.

## Authoritative state

- Iteration 246 closes generic connection `e=3,c=0`; do not reopen it.
- Iteration 307 freezes the complete eight-family `e=1,c=2` weight-completed actual `Tr U1` normalized cut.
- Iterations 308-310 freeze `e=2,c<=1` bookkeeping, the typed `U2` contract and `Tr U1^2` routing. The old physical `U2` blocker listed `V1_1/V1_2/H0/H1` as missing.
- Iteration 312 freezes exact cubic `log det` topology.
- Iterations 314-319 derive/validate physical ghost and graviton components in common convention `D=4, Lambda=0, a=-1/2`.
- Iterations 320-324 establish common-background trace closure and explicit ordered shifted propagators `G0(p+Q)`.
- Iterations 325, 327 and 330 remain preserved scoped gate-design FAILs; none is a Candidate Gravity consistency FAIL.
- Iteration 328 proves signed-affine triangle denominator equivalence only; denominator equivalence is not numerator equivalence.
- Iteration 329 closes the one-common-background H/N blocker and validates all 19 full-cubic routed insertion requests at correct `p+Q_before_insertion`.
- Iteration 331 freezes the physical cubic determinant integrand-family reconstruction into `1 singleton + 3 bubbles + 1 signed-affine triangle` with route-specific transported numerators.
- Iteration 332 validates that construction on the rank-2 closed timelike fixture `q1=(1,0,0,0)`, `q2=(-0.4,0.1,0.1,0)`, `q3=(-0.6,-0.1,-0.1,0)`, with `q_i^2=(-1,-0.14,-0.34)` in signature `(-,+,+,+)`.
- Iteration 333 validates the first direct-timelike determinant cut-origin reduction after analytically stripping the free denominators before shell evaluation. All three bubble families are NONZERO at two-particle cut level; the signed-affine triangle family is NONZERO from its `q^2=-0.14` and `q^2=-0.34` channels. The `q^2=-1` triangle channel remains numerical-convergence BLOCKED, not causally singular.
- Iteration 334 independently strengthens only that blocked `q^2=-1` triangle channel with Fibonacci-sphere N=96,192,384 plus phase-shifted N=384. It remains `BLOCKED_TRIANGLE_Q2_MINUS1_HIGHRES_DISCONTINUITY_RESOLUTION` because the frozen convergence-to-sample ratio is `2.2111065687680303e-4 > 2e-5`; the third propagator is analytically bounded away from zero.
- Iteration 335 is the active independent product-quadrature resolution of the same sole unresolved `q^2=-1` triangle channel. Original run `33753368856`, job `100641862178`, was cancelled during the scientific step at the workflow time limit before sentinel/schema audit and artifact upload, so it has no scientific authority. The workflow timeout only was raised from 45 to 180 minutes in commit `f997817d853b34f8e89349143261bd9685ab4af2`; formulas, fixture, quadrature configurations, numerator, routing and frozen convergence threshold `2e-5` are unchanged. Replacement run `33759144658` remains in progress and must not be duplicated.
- Iteration 336 freezes exact geometric 4D massless two-particle phase-space normalization: `dPhi2=dOmega/(32*pi^2)`, `int dPhi2=1/(8*pi)`, hence `int dPhi2 F = sphere_mean(F)/(8*pi)`.
- Iteration 337 calibrates the repository simple-cut convention: `D_s I[F] = -8*pi int(dPhi2 F) = -sphere_mean(F)` for ordinary two-simple-line cuts.
- Iteration 338 freezes the common determinant effective-action factor. With `C_det=(1/2)Tr_H-Tr_N`, the reduced one-loop convention gives `Gamma_det=+i*C_det`, hence `D_s Gamma_det=-i*sphere_mean` for ordinary simple two-particle determinant channels.
- Iteration 339 independently narrows the old physical `U2` blocker. It disambiguates the Iteration-319 graviton differential operator as `K` from the field-space Green operator denoted `H` in the Iteration-309 `U2` contract and freezes the routed inverse identities `G0(p)=K0(p)^-1` and `G1(q;p)=-G0(p+q) K1(q;p) G0(p)` on the actual physical Iteration-319 `K1`. The same-parent graviton Green `H0/H1` part of `U2` is therefore closed; physical `V1_1/V1_2` remains BLOCKED, and any required N/Y inverse-routing bridge remains unclosed.

Iteration-337 authority:
`PASS_REPOSITORY_NORMALIZED_SIMPLE_TWO_PARTICLE_CUT_CONVERSION__DET_OUTER_EFFECTIVE_ACTION_FACTOR_REMAINS_BLOCKED`.

Iteration-338 authority:
`PASS_SAME_PARENT_DETERMINANT_EFFECTIVE_ACTION_OUTER_PLUS_I_PREFactor__TRU1_MINUS_I_OVER_2_CROSSCHECK`.

Iteration-339 authority:
`PASS_E2C1_U2_GRAVITON_GREEN_H0_H1_SAME_PARENT_ROUTING_BRIDGE__V1_KERNELS_REMAIN_BLOCKED`.

Validated Iteration-339 provenance: run `33759581615`, job `100662270347`, artifact `9894856112`, digest `sha256:9e8593512de6fbef0238b0c1001950a34183d5f6484b179dd34c9e0f46528b05`, scientific JSON SHA-256 `9cdbedc4897d4ed8be746ac0d2ac4fc3c73251b36dce23f7a243322ab779e318`.

## Active sectors

- connection `e=1,c<=2`: actual `Tr U1` cut frozen by Iteration 307.
- connection `e=2,c<=1`: typed `U2` contract and `Tr U1^2` routing frozen; same-parent graviton Green `H0/H1` now frozen by Iteration 339. Physical `V1_1/V1_2` remains BLOCKED; any required N/Y inverse-routing bridge is not yet closed. No physical `U2` numerator is authorized and no zero-fill is allowed.
- determinant `e=0,c<=3`: singleton is scoped scaleless/local DR-zero-cut; all three bubbles have NONZERO direct-timelike discontinuities; triangle family is NONZERO with two certified channels and one numerical-convergence BLOCKED channel. For ordinary simple two-particle channels, geometric phase space, repository-normalized `D_s` conversion and the common determinant `+i` effective-action factor are frozen through Iterations 336-338.

## Active computation / exact next gates

**Primary active determinant computation:** Iteration 335 replacement run `33759144658` is still in progress on the sole unresolved triangle `q^2=-1` channel. It changes only the operational timeout relative to the cancelled no-artifact run. Parent dynamics, timelike fixture, route-specific physical numerators, cut surface, quadrature configurations and frozen convergence threshold `2e-5` remain unchanged. Already-certified bubbles and the other two triangle channels are not recomputed.

If Iteration 335 passes the unchanged threshold, freeze the complete channel-resolved determinant absorptive vector and assemble normalized determinant `e=0,c<=3` discontinuity using the Iteration-337/338 conversion `D_s Gamma_det=-i*sphere_mean` with family provenance. If it remains scientifically BLOCKED, derive a symbolic/analytic angular reduction; do not weaken thresholds.

**Independent U2 next gate:** derive and freeze same-parent physical `V1_1` and `V1_2` kernels in the exact Iteration-309 left/right index orientation. Separately bridge any required N/Y inverse routing before physical `U2` numerator assembly. The Iteration-339 Green bridge does not authorize a numerator by itself.

Iteration-297 evanescent/regulator warning remains binding for the full finite DR remainder. Source/Born subtraction remains forbidden until normalized determinant contribution enters matched-observable origin accounting. After determinant channel closure, matched-observable work remains source/Ward/contact completion plus linked `K2` subtraction in the frozen comparator coordinate; no Candidate residual may be declared before that subtraction is executable.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change through Iteration 339: `0 pp`. The U2 graviton-Green `H0/H1` blocker was genuinely removed, but no complete readiness bucket and no robust comparator-subtracted residual have closed.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped gate-design results remain preserved. Denominator equivalence is not numerator equivalence. Family-level nonzero discontinuity is not the normalized observable coefficient. Do not double-apply determinant internal `1/2` graviton weight or `-1` ghost weight. Do not double-apply connection-sector `Tr U1` coefficient `-i/2`. The Iteration-337 bridge is limited to ordinary two-simple-line cuts in the frozen branch/loop convention. In the U2 branch, the differential operator `K` must not be confused with the field-space Green operator `G`/Iteration-309 `H`; first-order Green routing requires the shifted left factor `G0(p+q)`. Do not create `ANSATZ-003` before a concrete robust comparator-subtracted residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a robust nonzero residual survives comparator subtraction. Source/Born subtraction only after normalized cut/origin classification in a matched observable. Full finite DR remainder remains subject to Iteration-297 evanescent/scheme authority. Blind heavy full-C5 remains unauthorized; closed C5 `e=3` authority is not reopened.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.
