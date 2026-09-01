# RQIR Candidate Gravity — Iteration 226

## MSSC-001 forward regular+log resolution gate

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

### Scope

Continue from the Iteration-225 numerically completed Born-subtracted connected scalar-source hard remainder. No Candidate Gravity residual or ansatz information enters this step. The Born-fixed subtraction `R=-8 M_Born` and the frozen relative numerical envelope `3e-7` are unchanged.

Use the natural dimensionless momentum-transfer coordinate

`z = -t/(4 p^2) = sin^2(theta_ext/2)`

and a comparator-only forward grid

`theta_ext = [0.13, 0.105, 0.085, 0.068, 0.054, 0.043, 0.034, 0.027]`.

For both linear spin-2 external polarizations, evaluate the same Iteration-225 singularity-adapted two-cell Voronoi hard-remainder integral with the two independent deterministic cubatures. The maximum A/B relative disagreement over all 16 rows is

`2.595262029909852e-7`,

which is below the frozen `3e-7` envelope.

### Frozen basis comparison

On each polarization compare equal-parameter six-column descriptions:

- 4D polyhomogeneous basis: `[1, L, z, zL, z^2, z^2L]`, `L=log(z)`;
- analytic control: Taylor degree 5 `[1,z,z^2,z^3,z^4,z^5]`.

The analytic control is not a claim that the amplitude is exactly analytic. It is a resolution diagnostic: if an equal-parameter analytic basis already lies inside the frozen numerical envelope, a log coefficient cannot be certified from these rows alone.

For `plus` on all eight rows:

- regular+log relative L2 residual: `1.73176347744811e-8`;
- Taylor-5 relative L2 residual: `5.180431884151699e-11`.

For `cross`:

- regular+log relative L2 residual: `6.991589330814055e-10`;
- Taylor-5 relative L2 residual: `1.6502718029550426e-12`.

Both Taylor residuals are far below the frozen `3e-7` row envelope.

### Envelope propagation to log coefficients

Propagate the frozen rowwise uncertainty conservatively through the linear pseudoinverse using

`Delta c_j <= sum_i |P_ji| (3e-7 |y_i|)`.

For `plus`, the absolute coefficient-to-bound ratios are

`|b0|/Delta b0 = 0.231864`,  
`|b1|/Delta b1 = 0.399726`,  
`|b2|/Delta b2 = 0.974572`.

For `cross` they are

`0.009189`, `0.015727`, `0.037700`.

Thus no fitted log coefficient is resolved above the frozen numerical envelope. The near-unity `plus b2` ratio is still below the preregistered resolution threshold and is not promoted.

### Comparison with the distinct pure-graviton positive control

Iteration 215 remains a separate on-shell pure-Einstein five-graviton observable. There the equal-parameter pure-Taylor residual was `9.496951084345664e-5`, or `2790.18` times its numerical envelope, while the regular+log representation was strongly preferred. That remains a scoped positive control for resolvable nonanalytic structure.

The `MSSC-001` result is different: on the present forward source window the nonanalytic coefficient is not identifiable. This observable mismatch is **not** a Candidate Gravity residual and the two observables are not identified.

### Classification

- source forward numerical gate: `PASS_WITHIN_FROZEN_3E-7_ENVELOPE`;
- source log structure: `REGIME_SPECIFIC_NON_IDENTIFIABILITY_NO_CERTIFICATE`;
- analytic-vs-log status: `NEAR_DEGENERACY_WITHIN_NUMERICAL_ENVELOPE`;
- exact analytic identity: `NOT_CLAIMED`;
- consistency FAIL: `NO`;
- Candidate Gravity novelty: `NONE`.

Retain:

- `SRC-CUT-007 — MSSC001_FORWARD_HARD_REMAINDER_IS_NUMERICALLY_STABLE_ON_A_FROZEN_TRANSFER_GRID`;
- `SRC-CUT-008 — MSSC001_FORWARD_LOG_COEFFICIENTS_ARE_NOT_RESOLVED_AGAINST_THE_FROZEN_3E-7_ENVELOPE`;
- `REL-NG-005 — PURE_GRAVITON_LOG_POSITIVE_CONTROL_AND_SOURCE_HARD_REMAINDER_HAVE_DIFFERENT_RESOLUTION_STATUS_AND_MUST_NOT_BE_IDENTIFIED`;
- `NG-FUNNEL-082 — SOURCE_CONTROL_NONANALYTIC_NONIDENTIFIABILITY_IS_NOT_CANDIDATE_NOVELTY`.

No `ANSATZ-003`. No Fisher/resources.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 225. This iteration classifies a source-comparator nonanalytic-resolution question but closes no additional stable rubric point. Comparator foundation remains `24/25`; robust unique residual remains `0/20`.

## Next gate

Return to the missing comparator authority rather than tuning the source window to manufacture a log signal. First re-audit asymptotic-safety Lorentzian/in-in nonlinear linked-cut authority under the same source-completed requirements. If still unavailable, retain `BLOCKED_AS_REALTIME_RELATION_COMPLETION` with exact provenance and move to the C3 ordered metric-CTP nonlinear completion. Neither may be zero-filled.
