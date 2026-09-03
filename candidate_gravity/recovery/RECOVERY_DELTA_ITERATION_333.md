# Recovery Delta — Iteration 333

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%  
**Scientific status:** PASS for direct-timelike determinant discontinuity family reduction, with one triangle channel retained as typed numerical BLOCKED.

## Validated provenance

- validated workflow: `rqir-iteration333-det-direct-timelike-discontinuity-family-reduction`
- run: `33748344954`
- job: `100625932251`
- artifact: `9890612109` (`iteration333-result`)
- artifact digest: `sha256:41f2e2e91e8b425c0f2704e5feec5982dac96e64cbd8ca2c3f8eb6a7e51ae545`
- scientific JSON SHA-256: `0620bce57a69d8e2f51a63989301cc281c53a8b7d5144f4d2d4636bfc64e4567`
- scientific exit code: `0`
- sentinel/schema, upload and final scientific enforcement: PASS.

## Preserved operational predecessors

A parallel/earlier Iteration-333 implementation first failed on namespace loading (`KeyError: ETA`) and, after a namespace-only repair, run `33748383810` reached the exact Cutkosky shell but attempted `np.linalg.inv(K0)` there. Since the cut explicitly imposes a massless free denominator `p^2=0`, the matrix is singular and the run terminated with `LinAlgError: Singular matrix` before a schema-valid artifact could be emitted. This is an operational/gate-design failure, not a Candidate Gravity consistency FAIL and not a zero/nonzero discontinuity result.

The validated Iteration-333 implementation removes the free `K0` denominators analytically before evaluating the shell. It independently verifies the stripping identity against the off-shell frozen physical integrand at held-out momenta.

## Frozen result

Free-denominator stripping validation:

- maximum scaled reconstruction error: `1.5265566588595902e-16` versus frozen `2e-8` threshold;
- flat graviton `H0=+p^2 I_10` maximum identity error: `5.551115123125783e-17`;
- flat ghost `N0=-p^2 I_4` maximum identity error: `0`.

All three canonical determinant bubble families have direct two-particle timelike NONZERO discontinuity certificates on the exact Iteration-332 fixture:

- `q^2=-1`: normalized cut proxy `-0.004517862848697545`;
- `q^2=-0.34`: normalized cut proxy `9.802036921027348e-05`;
- `q^2=-0.14`: normalized cut proxy `0.00013296877895753044`.

The signed-affine triangle family is also NONZERO at family level because two independent timelike two-line channels pass:

- `q^2=-0.14`: NONZERO; third denominator exact range approximately `[-0.7414213562,-0.4585786438]`;
- `q^2=-0.34`: NONZERO; third denominator exact range approximately `[-0.5414213562,-0.2585786438]`.

The remaining `q^2=-1` triangle channel has third denominator range approximately `[0.1185786438,0.4014213562]`, so there is no third-propagator crossing or causal/PV ambiguity. It remains `BLOCKED_NEAR_CANCELLATION_OR_CUBATURE_CONVERGENCE` solely because the two frozen low-order angular cubatures disagree at `1.405487804189524e-4`, above the unchanged `2e-5` threshold. It is not promoted post hoc.

Authority:
`PASS_DIRECT_TIMELIKE_DETERMINANT_DISCONTINUITY_FAMILY_REDUCTION__THREE_BUBBLES_NONZERO__TRIANGLE_FAMILY_NONZERO__Q2_MINUS1_TRIANGLE_CHANNEL_NUMERICALLY_BLOCKED`.

This is family/channel absorptive authority only. Universal phase-space normalization is not yet assembled into the normalized determinant `e=0,c<=3` cut. The full finite DR remainder remains subject to Iteration-297 evanescent/scheme authority.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 332: `0 pp`. A genuine absorptive determinant sublayer is now nonzero, but no complete readiness-rubric bucket and no robust comparator-subtracted Candidate Gravity residual close. The result therefore does not justify increasing model readiness.

## Exact next gate

Iteration 334: resolve only the `q^2=-1` triangle channel with an independent higher-resolution angular quadrature while keeping the Iteration-333 convergence threshold `2e-5` unchanged. If it passes, freeze the complete channel-resolved determinant absorptive vector and proceed to exact phase-space normalization / normalized determinant-cut assembly. If it remains blocked, preserve the blocker and derive an analytic angular integral rather than weakening thresholds.

No Source/Born subtraction yet. No `ANSATZ-003`. No Fisher/resources. Physical U2 remains independently BLOCKED. No blind heavy full-C5 and no reopening of closed `e=3`.
