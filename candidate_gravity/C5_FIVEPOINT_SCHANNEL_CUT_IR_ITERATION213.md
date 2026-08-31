# RQIR Candidate Gravity — Iteration 213

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Objective

Move from the validated five-graviton tree engine to the first genuinely physical pure-Einstein one-loop cut geometry, while explicitly testing the infrared endpoint before any regular+log soft extraction.

## Frozen real 2->3 family

Set `sqrt(s)=1` with physical incoming momenta of energy `1/2` along the beam axis. Emit outgoing positive-helicity graviton 5 with energy `epsilon` in a fixed non-collinear direction. The remaining hard subsystem has momentum `P34=Q-k5`; construct gravitons 3 and 4 as a two-body decay in the `P34` rest frame at frozen angles and boost back to the CM frame.

Use all-outgoing momenta and helicities

`1-, 2-, 3+, 4+, 5+`.

Representative kinematic checks at `epsilon=0.04,0.01,0.001` preserve momentum conservation and masslessness at approximately `1e-16` or better.

## Total-s two-particle cut

Parameterize the cut pair in the CM frame by

\[
\ell_1=\frac12(1,\mathbf n),\qquad
\ell_2=\frac12(1,-\mathbf n),\qquad \mathbf n\in S^2.
\]

The left tree is

`M4(k1-,k2-,ell1+,ell2+)`,

and after crossing the cut states the right tree is

`M5(k3+,k4+,k5+,-ell1-,-ell2-)`.

For the frozen external MHV sector the complete physical intermediate-helicity sum collapses by tree selection rules: only `h1=h2=+` on the left is nonzero. At a generic cut angle the other three helicity assignments evaluate exactly to zero in the tree engine.

This is a useful simplification: the first physical cut is one `M4_MHV * M5_MHV` integrand rather than a large helicity sum.

## Endpoint diagnostic

At `epsilon=0.01` and fixed generic azimuth, evaluate the cut integrand near the beam endpoint. The product

\[
\theta^2 |I_{cut}(\theta)|
\]

for `theta=[0.1,0.05,0.02,0.01,0.005,0.002]` is

`[3142.89,2881.13,2728.85,2679.06,2654.36,2639.61]`.

It approaches a finite nonzero constant, demonstrating

\[
|I_{cut}|\sim \theta^{-2}.
\]

Since the two-body measure contains `sin(theta)dtheta ~ theta dtheta`, the raw angular cut is logarithmically divergent.

## Direct cap test

Integrate the raw complex cut over the sphere excluding caps `theta<delta` and `pi-theta<delta`, using a deterministic `100 x 128` Gauss-Legendre/azimuth grid.

For

`delta=[0.3,0.2,0.14,0.1,0.07,0.05,0.035,0.025]`,

the magnitude of the raw angular integral grows from about `3.77e4` to `1.164e5`.

A linear fit of the six smallest-cap values to

\[
A\log(1/\delta)+B
\]

has slope `3.22314e4` and relative fit residual `1.19e-3`.

Thus the expected logarithmic infrared/collinear endpoint contamination is numerically explicit.

## Scientific consequence

The raw physical five-point unitarity cut **must not** be passed to the Iteration-210 soft-log extractor. Its regulator/cap logarithm is universal loop IR structure, not a Candidate Gravity linked residual.

The next object must be either:

- an analytically IR-subtracted hard cut in the exact frozen convention; or
- an inclusive completion whose real-soft contribution cancels the virtual endpoint singularity.

Retain:

- `C5-CUT-011 — REAL_FIVE_GRAVITON_TOTAL_S_CUT_REDUCES_TO_M4_MHV_TIMES_M5_MHV_IN_THE_FROZEN_HELICITY_SECTOR`;
- `IR-NG-002 — RAW_FIVE_GRAVITON_S_CHANNEL_CUT_HAS_THETA_MINUS_TWO_ENDPOINT_BEHAVIOR_AND_LOGARITHMIC_ANGULAR_CAP_DEPENDENCE`;
- `C5-CUT-012 — RAW_UNITARITY_CUT_MUST_BE_IR_SUBTRACTED_OR_INCLUSIVELY_COMPLETED_BEFORE_REGULAR_LOG_SOFT_EXTRACTION`;
- `NG-FUNNEL-070 — UNIVERSAL_LOOP_IR_LOGS_MUST_NOT_BE_MISIDENTIFIED_AS_LINKED_GRAVITY_RESIDUALS`.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

The physical cut geometry and its dominant IR blocker are now explicit, but an IR-safe five-point cut has not yet been extracted.

## Next gate

Derive and preregister the universal gravitational IR subtraction for this exact total-s cut from the Born/eikonal soft structure. The subtraction may not be fitted from the cut data. Validate that the subtracted angular integral becomes cap-independent within a declared numerical error envelope, then evaluate it across the frozen finite-epsilon grid and only then perform the Iteration-210 regular+log extraction.
