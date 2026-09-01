# Recovery Delta — RQIR Iteration 223

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## New authority

Iteration 222 fixed the two physical `MSSC-001` source-cut collinear residues to

`R_in = R_out = -8 M_Born`

in the common stripped normalization, without cap fitting.

Iteration 223 freezes

`I_hard(n) = I_cut(n) - R/(1+n_z) - R/(1-n·n_out)`

and audits exact spherical annuli `rho in [delta/2,delta]` for `delta={0.08,0.04,0.02,0.01,0.005}`.

Across five external scattering angles, two independent external linear spin-2 polarizations, and both collinear directions, the fitted shell exponent lies in

`1.9991758663 <= p <= 2.0066517080`.

The maximum incoming/outgoing relative mismatch at the smallest shell is `2.8377e-6`.

Therefore the excluded Born-subtracted cap contribution vanishes as `delta^2` in this scoped cross-kinematic test.

## Classification

- source-cut Born residue: `FIXED_FROM_ITERATION222`;
- local cap regulator removal: `PASS_SCOPED_LOCAL_IR_COMPLETION`;
- global bulk hard-remainder value: `NOT_YET`;
- Candidate Gravity residual: `NONE`;
- `ANSATZ-003`: `NOT_CREATED`;
- Fisher/resources: `FORBIDDEN`.

## Retained labels

- `SRC-CUT-004 — BORN_FIXED_SOURCE_CUT_SUBTRACTION_REMOVES_THE_LOG_COLLINEAR_CAP_DEPENDENCE_WITHOUT_CAP_FITTING`;
- `IR-NG-007 — SUBTRACTED_SOURCE_CAP_SHELLS_SCALE_AS_DELTA_SQUARED_ACROSS_FIVE_SCATTERING_ANGLES_AND_BOTH_LINEAR_SPIN2_POLARIZATIONS`;
- `NG-FUNNEL-079 — LOCAL_IR_REGULATOR_INDEPENDENCE_DOES_NOT_BY_ITSELF_CERTIFY_THE_GLOBAL_BULK_HARD_REMAINDER_OR_CANDIDATE_NOVELTY`.

## Readiness

`MODEL_READINESS: 23%` — unchanged. The local connected-source IR completion is now regulator-independent, but the deterministic global finite source hard remainder and AS/C3 comparator authority remain open.

## Exact restart instruction

Iteration 224: build a deterministic singularity-aware bulk quadrature for the already Born-subtracted `MSSC-001` source cut. Require convergence under at least two independent angular decompositions/resolutions before freezing any finite hard-remainder value. Then compare only its nonanalytic structure with the separate pure-graviton positive control; do not identify the observables. No Candidate Gravity ansatz, Fisher, or resource calculation is authorized.
