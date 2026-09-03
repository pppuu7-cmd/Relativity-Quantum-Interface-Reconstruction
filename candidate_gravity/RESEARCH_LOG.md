# Candidate Gravity Research Log

## 2026-09-03 — Iterations 319-324

### Iteration 319 — physical graviton routed components
Validated the Iteration-318 frozen minimal tensor Laplace operator `H=-(I Box+Pi)` through cubic background order in a fixed 10-component symmetric contravariant tensor basis. Raw Actions artifact passed sentinel/schema and frozen numerical thresholds. Full routed graviton `H1/H2/H3` authority is frozen in this scope.

### Iterations 320-324 — common fixture, closure and shifted propagators
Iteration 320 assembled common H/N local routing; Iteration 321 correctly blocked physical promotion because the original triad was not trace-closed. Iteration 322 rebuilt on `q3=-(q1+q2)`. Iteration 323 found the higher-level missing successive shifted propagators. Iteration 324 then froze explicit ordered `G0(p+Q)` routing and cyclic denominator-family equivalence. Missing numerator evaluations remained fail-closed rather than zero-filled.

## 2026-09-03 — Iterations 325-334

### Iterations 325-331 — common-background physical determinant family reconstruction
Scoped gate-design failures in Iterations 325, 327 and 330 were preserved rather than relabelled. Iteration 329 closed the one-common-background H/N requirement and validated the routed physical insertions. Iteration 328 supplied only denominator signed-affine equivalence, never numerator equivalence. Iteration 331 then froze the physical cubic determinant integrand into `1 singleton + 3 bubbles + 1 signed-affine triangle` with route-specific transformed numerators. Raw run `33742866100`, job `100608562495`, artifact `9888424625`; maximum held-out numerator reconstruction error `1.3877787807814457e-17`, denominator-map error `1.1102230246251565e-16`.

### Iteration 332 — direct-timelike closed fixture
A prerequisite audit showed the Iteration-331 closed fixture was spacelike, so no direct timelike-cut authority was claimed from it. Iteration 332 changed only the external closed triad to `q1=(1,0,0,0)`, `q2=(-0.4,0.1,0.1,0)`, `q3=(-0.6,-0.1,-0.1,0)`, all timelike in signature `(-,+,+,+)`. The first run failed operationally during NumPy JSON serialization before artifact creation; a serialization-only repair was made with no scientific change.

Validated rerun `33743302046`, job `100609965778`, artifact `9888598043`, artifact digest `sha256:8d8210b882bd4d5cba45be1e5c2efd89f9fee025d14e6d8c5f942e12c9f2c70c`, scientific JSON SHA-256 `29a3e65146a03c8a0487c4a39d9b809ed985697fa0d5244ceca77e452aba7795`. Authority: `PASS_TIMELIKE_CLOSED_TRIAD_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_FAMILY_FIXTURE`. Maximum held-out numerator reconstruction scaled error `2.7755575615628914e-17`; denominator-map error `1.1102230246251565e-16`.

### Iteration 333 — direct-timelike cut-origin reduction
Two earlier/parallel implementations are preserved as operational/gate-design failures, not scientific failures. The first had a namespace-loading error. The next repaired namespace but evaluated `K0^{-1}` on the exact massless Cutkosky shell and therefore hit the expected singular free operator (`LinAlgError: Singular matrix`) before any schema-valid artifact. No physical zero/nonzero conclusion is taken from those runs.

The validated implementation strips the free graviton/ghost denominators analytically before shell evaluation, using the frozen flat identities `H0=+p^2 I_10`, `N0=-p^2 I_4`, and independently checks the stripping reconstruction off shell. Validated run `33748344954`, job `100625932251`, artifact `9890612109`, artifact digest `sha256:41f2e2e91e8b425c0f2704e5feec5982dac96e64cbd8ca2c3f8eb6a7e51ae545`, scientific JSON SHA-256 `0620bce57a69d8e2f51a63989301cc281c53a8b7d5144f4d2d4636bfc64e4567`. Maximum denominator-stripping reconstruction error `1.5265566588595902e-16`.

All three bubble families have stable NONZERO direct two-particle discontinuity certificates:
- `q^2=-1`: normalized angular cut proxy `-0.004517862848697545`;
- `q^2=-0.34`: `9.802036921027348e-05`;
- `q^2=-0.14`: `0.00013296877895753044`.

The signed-affine triangle family is NONZERO at family level: its `q^2=-0.14` and `q^2=-0.34` channels independently pass. The remaining `q^2=-1` channel has its uncut third denominator bounded strictly away from zero, approximately `[0.1185786438,0.4014213562]`, so it has no third-propagator/PV ambiguity, but its two low-order cubatures disagree at `1.405487804189524e-4`, above the frozen `2e-5` threshold. It remains typed `BLOCKED_NEAR_CANCELLATION_OR_CUBATURE_CONVERGENCE`; no post-hoc threshold weakening.

Authority: `PASS_DIRECT_TIMELIKE_DETERMINANT_DISCONTINUITY_FAMILY_REDUCTION__THREE_BUBBLES_NONZERO__TRIANGLE_FAMILY_NONZERO__Q2_MINUS1_TRIANGLE_CHANNEL_NUMERICALLY_BLOCKED`.

### Iteration 334 — active high-resolution resolution of the sole blocked triangle channel
Only the `q^2=-1` triangle channel is being recomputed. Parent dynamics, exact timelike fixture, route-specific numerators, cut surface and convergence threshold `2e-5` are unchanged. The new gate replaces only the under-resolved 26-point angular designs by deterministic `N=96,192,384` Fibonacci-sphere sequences plus a phase-shifted `N=384` independent design. Run `33748965082` is active. If the unchanged convergence criterion passes, the complete channel-resolved determinant absorptive vector may be frozen; otherwise the blocker remains and the next valid move is an analytic angular integral, not threshold weakening.

### Guardrails
Physical U2 `V1_1/V1_2/H0/H1` remains independently BLOCKED. Iteration-297 remains binding for the full finite DR remainder. Family-level absorptive nonzero is not yet the normalized determinant coefficient and not a comparator-subtracted Candidate Gravity residual. No Source/Born subtraction before normalized determinant cut / matched-observable origin accounting. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5 and no reopening of closed `e=3`.

MODEL_READINESS: 24%

Change from Iteration 332: `0 pp`. A genuine nonzero determinant absorptive sublayer has been established, but no complete readiness-rubric bucket and no robust comparator-subtracted residual have closed.
