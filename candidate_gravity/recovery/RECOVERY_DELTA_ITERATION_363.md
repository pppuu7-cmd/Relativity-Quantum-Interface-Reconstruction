# Recovery Delta — Candidate Gravity Iteration 363

Date: 2026-09-03

## Scope

Kinematic and analytic uncut-pole separation prerequisite for the 48 Iteration-359 timelike U2 channels whose cut passes through the unique double-pole momentum group. The one-auxiliary-mass simple-cut representation is probed at `mu^2={-1e-5,0,+1e-5}`. No physical repeated-pole discontinuity is integrated in this iteration.

## Raw Actions authority

- run: `33800789921`
- job: `100799511206`
- workflow: `rqir-iteration363-u2-repeated-pole-massive-cut-kinematic-separation`
- workflow head: `9bc367c42b2da7cc2279bfd4f4a3fd75029a7886`
- code commit: `a6a7678a86b1e0ed385d7bb773286dc09776de57`
- artifact: `9910973980` (`iteration363-result`)
- artifact digest: `sha256:f7e6059beb7028e20b4fd3e6857faef26ba3699b261297c911c43d1a85eb5bd8`
- raw scientific JSON SHA-256: `40cb8ebfbcd11d0106407f2ef5392cf00d3c01816b13d4cc4976c2f937ec8463`
- exactly one top-level JSON object; sentinel `363`; authority audit `scientific_authority_pass=true`.

## Result

Authority:

`PASS_U2_REPEATED_POLE_MASSIVE_SIMPLE_CUT_KINEMATIC_AND_UNCUT_SEPARATION__ALL_REGULAR`

Census:
- typed repeated-pole cut channels: `48`;
- `REGULAR=48`;
- `BLOCKED=0`;
- auxiliary-mass probes: `-1e-5`, `0`, `+1e-5`;
- minimum `rho^2` across all probes: `0.03499500017857143`;
- minimum analytically certified full-sphere uncut absolute squared momentum: `0.11857405797625284`;
- frozen uncut-separation threshold: `1e-10`.

The analytic full-sphere affine-range test, rather than sparse angular sampling, certifies that every uncut distinct momentum group remains away from its massless pole throughout the certified auxiliary-mass envelope.

## Interpretation

This closes the kinematic prerequisite for symmetric auxiliary-`mu^2` differentiation. It is not a nonzero discontinuity certificate, not a full `Tr U2` value, not a comparator residual and not a novelty statement.

The Iteration-361 ordinary-simple q2-resolved cancellation remains scoped to the ordinary-simple sector. Repeated-pole channels must still be integrated and cannot be zero-filled from that cancellation.

## Exact next gate

Evaluate the normalized simple-massive cut for all 48 channels at symmetric `mu^2` nodes within the certified envelope, apply the frozen negative auxiliary-mass derivative at zero, and require both angular convergence and an independent derivative-step check. Keep the three external `q^2` discontinuity variables separate.

If all 48 cut-through-double-pole channels converge, evaluate the remaining timelike simple-simple cuts in repeated `(2,1,1)` families where the unique double pole is left uncut, with a direct squared-denominator evaluation and an auxiliary-mass derivative cross-check.

No Source/Born subtraction. No `ANSATZ-003`. No Fisher/resources.

MODEL_READINESS: 24%

Change from Iteration 362: `0 pp`; a hard physical-integration prerequisite closed, but no complete readiness-rubric bucket and no robust comparator-subtracted residual closed.
