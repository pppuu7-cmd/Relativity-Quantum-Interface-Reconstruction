# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 338**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority.

## Authoritative state

- Iteration 246 closes generic connection `e=3,c=0`; do not reopen it.
- Iteration 307 freezes the complete eight-family `e=1,c=2` weight-completed actual `Tr U1` normalized cut.
- Iterations 308-310 freeze `e=2,c<=1` bookkeeping/typed U2 contract/U1^2 routing; physical U2 `V1_1/V1_2/H0/H1` remains BLOCKED.
- Iteration 312 freezes exact cubic `log det` topology.
- Iterations 314-319 derive/validate physical ghost and graviton components in common convention `D=4, Lambda=0, a=-1/2`.
- Iterations 320-324 establish common-background trace closure and freeze explicit ordered shifted propagators `G0(p+Q)`.
- Iterations 325, 327 and 330 remain preserved scoped gate-design FAILs; none is a Candidate Gravity consistency FAIL.
- Iteration 328 proves signed-affine triangle denominator equivalence only; denominator equivalence is not numerator equivalence.
- Iteration 329 closes the one-common-background H/N blocker and validates all 19 full-cubic routed insertion requests at correct `p+Q_before_insertion`.
- Iteration 331 freezes the physical cubic determinant integrand-family reconstruction into `1 singleton + 3 bubbles + 1 signed-affine triangle` with route-specific transported numerators.
- Iteration 332 validates that exact construction on the rank-2 closed timelike fixture `q1=(1,0,0,0)`, `q2=(-0.4,0.1,0.1,0)`, `q3=(-0.6,-0.1,-0.1,0)`, with `q_i^2=(-1,-0.14,-0.34)` in signature `(-,+,+,+)`.
- Iteration 333 validates the first direct-timelike determinant cut-origin reduction after analytically stripping the free denominators before shell evaluation. All three bubble families are NONZERO at two-particle cut level; the signed-affine triangle family is NONZERO from its `q^2=-0.14` and `q^2=-0.34` channels. The `q^2=-1` triangle channel remains numerical-convergence BLOCKED, not causally singular.
- Iteration 334 independently strengthens only that blocked `q^2=-1` triangle channel with Fibonacci-sphere N=96,192,384 plus phase-shifted N=384. It remains `BLOCKED_TRIANGLE_Q2_MINUS1_HIGHRES_DISCONTINUITY_RESOLUTION` because the frozen convergence-to-sample ratio is `2.2111065687680303e-4 > 2e-5`; the third propagator is analytically bounded away from zero.
- Iteration 335 remains the active independent product-quadrature resolution of the same sole unresolved `q^2=-1` triangle channel. Original run `33753368856`, job `100641862178`, was cancelled during the scientific step at the workflow time limit before sentinel/schema audit and before artifact upload; therefore it has **no scientific authority** and is not a PASS/FAIL of the model or gate. The workflow timeout only was increased from 45 to 180 minutes in commit `f997817d853b34f8e89349143261bd9685ab4af2`; formulas, fixture, quadrature configurations, numerator, routing and frozen convergence threshold `2e-5` are unchanged. Replacement run `33759144658` is queued/in progress; do not duplicate it.
- Iteration 336 independently freezes the exact geometric 4D massless two-particle phase-space normalization in signature `(-,+,+,+)`: `dPhi2=dOmega/(32*pi^2)`, `int dPhi2=1/(8*pi)`, hence a normalized sphere mean converts as `int dPhi2 F = mean/(8*pi)`. Validated run `33754035543`, job `100644020489`, artifact `9892688060`, digest `sha256:eaa23f7411d63f0d66216498b750a20609fa19a478662f9fde1f1e14bce0165e`, scientific JSON SHA-256 `5f84fd4616dcca8eb3bd5beeb396718a74caab9637f77758e4e63aa529f07e53`.
- Iteration 337 calibrates that geometric factor against the repository's Iteration-296 scalar-bubble convention and freezes the ordinary simple-cut bridge `D_s I[F] = -8*pi int(dPhi2 F) = -sphere_mean(F)`. Validated run `33756194728`, job `100651082826`, artifact `9893533178`, digest `sha256:aaeca20e2906d240417b6c9d301639068c62076f11281694525a5263d1096161`, scientific JSON SHA-256 `7d6ba8fd46c01fb9af79b21932daa49787587122c47e51af85d8d7997bad64`.
- Iteration 338 freezes the same-parent common determinant effective-action factor. With the physical route coordinate `C_det=(1/2)Tr_H-Tr_N`, the reduced one-loop convention gives `Gamma_det=+i*C_det`; this cross-checks the independently frozen Iteration-307 `Tr U1` coefficient `-i/2`. Validated run `33756324238`, job `100651503806`, artifact `9893580250`, digest `sha256:54eb5733ebfd08afeaccfbe7c775968436136f9ae05f5cbddfee96b53ca86da4`, scientific JSON SHA-256 `2a0a99466b08ce30ff639739079c97461078e80429b42e92f95c90367f902f6b`.

Iteration-337 authority:
`PASS_REPOSITORY_NORMALIZED_SIMPLE_TWO_PARTICLE_CUT_CONVERSION__DET_OUTER_EFFECTIVE_ACTION_FACTOR_REMAINS_BLOCKED`.

Iteration-338 authority:
`PASS_SAME_PARENT_DETERMINANT_EFFECTIVE_ACTION_OUTER_PLUS_I_PREFactor__TRU1_MINUS_I_OVER_2_CROSSCHECK`.

Combined consequence for an ordinary two-simple-line determinant channel with normalized angular mean `m`:

`D_s C_det = -m`,

`D_s Gamma_det = -i*m`.

This freezes the ordinary simple-cut sign, loop-normalized discontinuity conversion and common determinant outer effective-action factor in the repository convention. It does not authorize raised cut propagators, overlapping singular cuts, a full finite DR remainder, source/Ward/contact completion or matched `K2` subtraction.

## Active sectors

- connection `e=1,c<=2`: actual `Tr U1` cut frozen by Iteration 307.
- connection `e=2,c<=1`: physical U2 `V1_1/V1_2/H0/H1` remains independently BLOCKED; no zero-fill.
- determinant `e=0,c<=3`: singleton is scoped scaleless/local DR-zero-cut; all three bubbles have NONZERO direct-timelike discontinuities; triangle family is NONZERO with two certified channels and one numerical-convergence BLOCKED channel. For ordinary simple two-particle channels, geometric phase space, repository-normalized `D_s` conversion and the common determinant `+i` effective-action factor are now all frozen through Iterations 336-338.

## Active computation / exact next gate

**Iteration 335 replacement run `33759144658` is active** on the sole unresolved triangle `q^2=-1` channel. It changes only the operational workflow timeout relative to the cancelled no-artifact run. Parent dynamics, timelike fixture, route-specific physical numerators, cut surface, quadrature configurations and frozen convergence threshold `2e-5` remain unchanged. Already-certified bubbles and the other two triangle channels are not recomputed.

If the replacement Iteration 335 raw artifact passes the unchanged threshold, freeze the complete channel-resolved determinant absorptive vector and assemble the normalized determinant `e=0,c<=3` discontinuity using the Iteration-337/338 conversion `D_s Gamma_det = -i*sphere_mean` with family provenance. If it remains scientifically BLOCKED, derive a symbolic/analytic angular reduction; do not weaken thresholds.

Iteration-297 evanescent/regulator warning remains binding for the full finite DR remainder. Source/Born subtraction remains forbidden until the normalized determinant contribution enters matched-observable origin accounting. After determinant channel closure, the next matched-observable work is source/Ward/contact completion plus the linked `K2` subtraction in the frozen comparator coordinate; no Candidate residual may be declared before that subtraction is executable.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change through Iteration 338: `0 pp`. Exact geometric cut normalization, repository-normalized simple-cut conversion and the common determinant effective-action prefactor close hard prerequisites but do not close a full readiness bucket and do not produce a comparator-subtracted residual.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped gate-design results remain preserved. Denominator equivalence is not numerator equivalence. Family-level nonzero discontinuity is not the normalized observable coefficient. Do not double-apply the determinant internal `1/2` graviton weight or `-1` ghost weight. Do not double-apply the connection-sector `Tr U1` coefficient `-i/2`. The Iteration-337 bridge is limited to ordinary two-simple-line cuts in the frozen branch/loop convention. Do not create `ANSATZ-003` before a concrete robust comparator-subtracted residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a robust nonzero residual survives comparator subtraction. Source/Born subtraction only after normalized cut/origin classification in a matched observable. Full finite DR remainder remains subject to Iteration-297 evanescent/scheme authority. Blind heavy full-C5 remains unauthorized; closed C5 `e=3` authority is not reopened.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.
