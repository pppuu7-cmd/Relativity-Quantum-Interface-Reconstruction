# Recovery Delta — RQIR Iteration 213

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iteration 212 validated the pure-Einstein five-graviton MHV KLT tree engine and authorized its use inside a physical two-particle one-loop cut.

## New authoritative result

A real massless `2->3` family at `sqrt(s)=1` has been frozen with one outgoing positive-helicity soft graviton. The total-s cut uses

`M4(k1-,k2-,ell1+,ell2+) * M5(k3+,k4+,k5+,-ell1-,-ell2-)`.

For the frozen all-outgoing `--+++` sector, tree helicity selection makes the other three intermediate-helicity assignments vanish.

Kinematic mass-shell and momentum-conservation errors are at the `1e-16` scale.

The raw cut has a genuine IR endpoint problem. At `epsilon=0.01`, `theta^2 |I_cut(theta)|` approaches a nonzero constant (~`2639.6` by `theta=0.002`), proving `|I_cut|~theta^-2`. With `sin(theta)dtheta` this produces a logarithmic angular divergence.

Direct cap-regulated integrations for `delta` from `0.3` down to `0.025` grow approximately linearly with `log(1/delta)`. The magnitude fit on the six smallest caps has relative residual `1.19e-3`.

## Classification

- real physical five-point cut geometry: `PASS_SCOPED`;
- helicity reduction: `PASS_TREE_SELECTION`;
- raw cut: `IR_COLLINEAR_LOG_DIVERGENT`;
- raw cut -> Iteration-210 extractor: `FORBIDDEN_BEFORE_IR_SUBTRACTION_OR_INCLUSIVE_COMPLETION`.

## Retained results

- `C5-CUT-011 — REAL_FIVE_GRAVITON_TOTAL_S_CUT_REDUCES_TO_M4_MHV_TIMES_M5_MHV_IN_THE_FROZEN_HELICITY_SECTOR`;
- `IR-NG-002 — RAW_FIVE_GRAVITON_S_CHANNEL_CUT_HAS_THETA_MINUS_TWO_ENDPOINT_BEHAVIOR_AND_LOGARITHMIC_ANGULAR_CAP_DEPENDENCE`;
- `C5-CUT-012 — RAW_UNITARITY_CUT_MUST_BE_IR_SUBTRACTED_OR_INCLUSIVELY_COMPLETED_BEFORE_REGULAR_LOG_SOFT_EXTRACTION`;
- `NG-FUNNEL-070 — UNIVERSAL_LOOP_IR_LOGS_MUST_NOT_BE_MISIDENTIFIED_AS_LINKED_GRAVITY_RESIDUALS`.

## Readiness

`MODEL_READINESS: 23%`, unchanged. This exposes and localizes the physical IR blocker; it does not close the C5 RQIR comparator or produce a Candidate Gravity residual.

## Exact restart instruction

Resume at **Iteration 214 — universal gravitational IR subtraction for the frozen five-point cut**.

Use published gravitational soft/eikonal IR factorization, preferably tied to the Born amplitude as in Weinberg and the explicit graviton-graviton analysis of Donoghue–Torma. Derive the subtraction in the exact all-outgoing/cut normalization before examining the finite remainder. The subtraction coefficient may not be fitted from the cap-regulated numerical cut. Validate it against the observed endpoint coefficient and then test whether the subtracted angular integral is cap-independent. Only an IR-safe/subtracted cut may be passed through the Iteration-210 regular+log soft extractor.

Do not create `ANSATZ-003`. Fisher/resources remain forbidden.
