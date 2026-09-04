# Post-447 Cut-Momentum Precision Scope Recovery Delta

**Date:** 2026-09-05  
**MODEL_READINESS:** 24% (unchanged)  
**Authority:** source/provenance scope audit; non-promoting; collision-safe unnumbered stage  
**Raw-valid run:** 33926682904  
**Job:** 101196626813  
**Artifact:** 9957039217  
**Artifact digest:** `sha256:1e7258b6d48203f26e86425078a5c7a38f89e5a9c31aec08a2f4166b280e4fe3`  
**Raw scientific JSON SHA-256:** `fa8dc82596c09604d5b215f57bb56d7f62d395615f1e9b31212b44572f345118`

## Why this audit was needed

Multiple automatic RQIR research channels have already closed substantial pieces of the parent precision chain through Iterations 436-447. Those PASS results are retained. Direct source comparison nevertheless shows that the strongest 80/120-digit parent gates 436-440 are evaluated at explicitly frozen Iteration-270 representative momenta (`P0` and its prescribed shifts), while Iteration 446 performs its 80/120-digit post-parent products only after the parent matrices have already been computed on the representative Iteration-368 `PROBES`.

The active physical fixed-mass function in Iteration 407 instead generates loop momenta continuously from the cut geometry,

`p(z,phi,u,v) = -a + alpha(u,v) q + rho(u,v) n(z,phi)`

(with radial deformations inside the stripped-limit construction). Therefore representative-input multiprecision closure does not by itself prove continuous arbitrary-precision provenance for every physical cut sample.

## Raw-valid result

Classification:

`PASS_REPRESENTATIVE_PARENT_MP_DOES_NOT_YET_EQUAL_CONTINUOUS_CUT_MOMENTUM_MP__NON_PROMOTING`

This result **does not invalidate** Iterations 436-446. It narrows their logical scope:

- certified: parent arithmetic on the explicitly frozen representative inputs/nodes actually tested;
- not yet certified: arbitrary-precision recomputation of `Q0/Q1/Acoef/Asub` and the complete traced stripped numerator at every actual Iteration-407 `p(z,phi,u,v)` sample.

This distinction is consistent with Iteration 447, which already states that full Iteration-407 / full-`F(u,v)` precision is not closed.

## Consequence for the next numerical gate

Do not construct the next phi/sample-generation gate by taking binary64 parent matrices and merely recasting them to `mpmath`. The next true continuous-precision sample gate must generalize the already validated multiprecision parent implementations so that `Q0`, `Q1`, `Acoef/Asub`, and the traced class-3 numerator are evaluated directly at the same physical cut momenta used by index 2.

Prospectively retained conditions:

- target: double-double index 2 / class 3 / `q^2=-1`;
- precision levels: 80 and 120 decimal digits;
- preserve parent dynamics and exact class-3 routing;
- preserve `h1=1e-4`;
- preserve radial Richardson nodes `{2e-3, 1e-3, 5e-4}`;
- preserve physical mass nodes, numerator, sign and normalization;
- no smaller/adaptive `h`;
- no physical threshold weakening;
- no angular-grid escalation as a rescue;
- no zero fill.

## Relationship to the active spectral gate

The existing repaired Iteration-407 spectral-algebra workflow run `33924198609` must not be duplicated. It operates over frozen parent phi samples and can only close the interpolation / affine-log recurrence / terminal spectral algebra layer. Even if it passes, sample-generation precision remains a separate gate.

## Iteration-number collision policy

The repository has already experienced race-created iteration-number collisions in the automatic research channels. This stage therefore deliberately has no new authoritative integer ID. Future parallel diagnostic stages should remain collision-safe until a canonical raw-consumption step assigns or reserves an authoritative identifier.

## Physical authority

Index 2 remains unpromoted. Iteration 421 remains the raw-valid physical `BLOCKED_CONVERGENCE` authority. Iteration 412 exact15 remains blocked. `ANSATZ003` and Fisher/resource claims remain forbidden.
