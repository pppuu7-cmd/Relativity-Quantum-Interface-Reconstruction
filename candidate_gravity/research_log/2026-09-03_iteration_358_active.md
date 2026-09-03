# Candidate Gravity Research Log — Iteration 358 (active)

Date: 2026-09-03

Iteration 358 is the exact next gate authorized by Iteration 357. It evaluates only the 12 ordinary-simple U2 families and their 36 typed timelike two-line channels. The 30 repeated-pole families remain excluded from ordinary Cutkosky substitution and are not evaluated or zero-filled.

Method: for each simple channel, parameterize the exact massless two-particle cut sphere in signature `(-,+,+,+)`. For every uncut propagator, compute the analytic affine range of its squared momentum over the full cut sphere, rather than relying on sampled zero tests. The already stripped physical traced numerator is evaluated on deterministic on-shell directions only as a regularity cross-check; finite sampling is never used to assert an identically zero numerator.

Inherited guards: Iteration-356 timelike tolerance `2e-12`; uncut denominator separation guard `1e-10` matching the Iteration-355 stripped flat-pole safety scale; cut-shell closure threshold `2e-10`. No threshold weakening.

Initial code commit: `43254a83c9ca374bc141c423ae74cac8276ba4b8`. Workflow commit: `11d80102bc739cc3220deb8eeec3a41e52d0ba6f`. Trigger-only commit: `e5dd24c442ff3b11b6bca240fe2b04acebea01b9`.

Run `33794527084`, job `100778886976`, failed during the scientific Python step before sentinel/schema audit and before artifact upload. The failure is implementation-only: the frozen parent `mdot` is a one-argument quadratic form, while the first Iteration-358 implementation mistakenly called it as a two-argument bilinear product. No scientific PASS/FAIL is assigned to that run and no threshold/physics change follows from it.

Repair commit `f80e10ca6d868ea0fd2878454b5d4b3cc2107f3d` introduces only the Minkowski bilinear helper by polarization of the frozen quadratic form, `B(a,b)=(mdot(a+b)-mdot(a)-mdot(b))/2`. Replacement run: `33794678777`, job `100779381741`.

Scientific authority remains Iteration 357 until the raw Iteration-358 artifact and authority audit are validated. A green workflow alone will not be promoted.

MODEL_READINESS: 24%
