# RQIR Candidate Gravity — Iteration 223

## Born-fixed connected-source hard-remainder cap audit

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Iteration 222 established, prospectively across five scattering angles and both independent external linear spin-2 polarizations, the common local relation

`R_in = R_out = -8 M_Born`

for the two logarithmic collinear residues of the physical `MSSC-001` scalar+graviton source cut in the frozen stripped normalization.

Iteration 223 uses that relation as fixed input. No cap fit is used.

Define the pointwise Born-fixed hard kernel

`I_hard(n) = I_cut(n) - R/(1+n_z) - R/(1-n·n_out)`,

with `R=-8 M_Born`.

For each collinear direction, integrate `I_hard` over the exact spherical annulus `rho in [delta/2,delta]`. The frozen shell sequence is

`delta = {0.08, 0.04, 0.02, 0.01, 0.005}`.

Across all 20 endpoint tests (five external angles × two external polarizations × two collinear directions), the fitted small-shell power lies in

`1.9991758663 <= p <= 2.0066517080`.

Thus the excluded Born-subtracted cap contribution vanishes as `delta^2` in this scoped cross-kinematic audit. The largest incoming/outgoing mismatch at the smallest shell is `2.84e-6` relative.

## Classification

- Born-fixed local subtraction: `PASS_FROM_ITERATION222`.
- Local cap-regulator independence: `PASS_SCOPED_LOCAL_IR_COMPLETION`.
- Global finite bulk hard-remainder value: `NOT_EVALUATED_THIS_GATE`.
- Candidate novelty: none.

The result is stronger than merely observing pointwise softening: although the subtracted kernel can retain an azimuth-dependent `1/rho` term, its cap-shell integral is demonstrably quadratic after the complete angular average. This is a regulator-independence statement for the declared source cut, not a proof that the full bulk quadrature is already numerically closed.

## Retained scoped results

- `SRC-CUT-004 — BORN_FIXED_SOURCE_CUT_SUBTRACTION_REMOVES_THE_LOG_COLLINEAR_CAP_DEPENDENCE_WITHOUT_CAP_FITTING`.
- `IR-NG-007 — SUBTRACTED_SOURCE_CAP_SHELLS_SCALE_AS_DELTA_SQUARED_ACROSS_FIVE_SCATTERING_ANGLES_AND_BOTH_LINEAR_SPIN2_POLARIZATIONS`.
- `NG-FUNNEL-079 — LOCAL_IR_REGULATOR_INDEPENDENCE_DOES_NOT_BY_ITSELF_CERTIFY_THE_GLOBAL_BULK_HARD_REMAINDER_OR_CANDIDATE_NOVELTY`.

## Readiness

`MODEL_READINESS: 23%` — unchanged from Iteration 222. The source-cut IR coefficient and local regulator removal are now fixed, but comparator foundation is not fully closed because the deterministic global hard remainder, AS real-time relation and C3 ordered completion remain unresolved.

## Exact next gate

Construct a deterministic singularity-aware bulk quadrature for the already Born-subtracted `MSSC-001` source cut. Require convergence under independent angular decompositions before using the finite value. Only after that should its nonanalytic dependence be compared with the separate pure-graviton positive control; the two observables must not be identified or subtracted from one another by fiat.
