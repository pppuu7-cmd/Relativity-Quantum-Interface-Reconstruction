# Recovery Delta — Candidate Gravity Iteration 360

Date: 2026-09-03

## Scope

New-version replacement for the operationally failed Iteration 358. Physics scope, fixture, 12-family/36-channel census and thresholds are unchanged. The only implementation correction is use of an explicit Minkowski bilinear product instead of calling the inherited norm-only `mdot(x)` with two arguments.

This gate classifies on-shell numerator regularity and full-cut-sphere uncut-denominator separation for the ordinary-simple U2 sector only. It does not integrate a discontinuity. Repeated-pole families remain outside this gate.

## Raw Actions authority

- authoritative run: `33794699218`
- job: `100779450303`
- artifact: `9908776209` (`iteration360-result`)
- artifact digest: `sha256:00f42a4443af1cf8b4e361e1a35360f32e2a336b8f5feef7b7f9dc63bd35237b`
- scientific JSON SHA-256: `3b484378b3566e9303f430818433ae3814167805d2a92b042e69da7ca5dd50f8`
- workflow head: `93371e102a492d2fd3bfbe372241734b47aef392`

The raw artifact contains exactly one Iteration-360 result object. The independent authority audit reports the expected sentinel `360`, one top-level object and `scientific_authority_pass=true`.

## Result

Authority:

`PASS_U2_ORDINARY_SIMPLE_CHANNEL_ON_SHELL_REGULARITY_AND_UNCUT_DENOMINATOR_CLASSIFICATION_V2`.

Census:
- ordinary-simple families: `12`;
- typed timelike pair channels: `36`;
- `REGULAR`: `36`;
- `ZERO`: `0`;
- `BLOCKED`: `0`;
- maximum cut-shell absolute error: `3.434752482434078e-16`;
- minimum analytically certified absolute uncut denominator squared momentum over all cut spheres: `0.11857864376269048`.

Every ordinary-simple channel therefore passes the prerequisite for normalized channel-resolved simple-cut integration. The uncut-pole separation is an analytic full-sphere range certificate, not a sampled nonzero assertion. Finite numerator sampling is used only as a regularity cross-check and never as a zero certificate.

Frozen thresholds remain:
- timelike pair classification: `q^2 < -2e-12`;
- uncut denominator separation: `min |r^2| > 1e-10`;
- cut-shell closure: `<= 2e-10`.

Iteration 358 remains preserved as `OPERATIONAL_FAIL_ITERATION358_MD0T_ARITY__NO_PHYSICS_GATE_EVALUATED`; it carries no scientific FAIL/PASS.

## Exact next gate

For only these 36 `REGULAR` ordinary-simple channels, compute the channel-resolved normalized `D_s Tr U2` coordinate using the frozen repository simple-cut bridge of Iteration 337, `D_s I[F] = -sphere_mean(F)`, with the physical ghost/graviton denominator signs retained explicitly. Keep different external timelike invariants channel-resolved rather than summing different `q^2` cuts into one observable coordinate.

The 30 repeated-pole families remain governed by Iteration 359 and require the frozen first auxiliary-mass derivative/distributional route; ordinary simple Cutkosky substitution remains forbidden for them.

Do not fold the connection effective-action coefficient into the stored `Tr U2` coordinate unless separately and explicitly reported: Iteration 308 freezes the contribution as `+(i/2) Tr U2 -(i/4) Tr U1^2`.

MODEL_READINESS: 24%

Change from Iteration 359: `0 pp`. A hard ordinary-simple U2 integration prerequisite closed, but no complete readiness-rubric bucket and no robust comparator-subtracted residual closed.
