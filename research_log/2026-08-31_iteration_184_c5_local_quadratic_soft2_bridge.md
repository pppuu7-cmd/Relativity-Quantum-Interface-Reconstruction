# RQIR Research Log — Iteration 184

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

Iteration 183 requires source-completed soft2 cubic completions of local quadratic EFT directions before a nonlocal `K2` variation can be hard-calibrated and compared.

Computed on the six frozen null-soft TT rows using symmetric soft second derivatives plus two Richardson levels:

- EH soft2: `[1.5075719591,0.2125004724,2.8203238064,-1.9851779883,-0.1902862337,0.5362481602]`, max convergence error `1.66e-7`;
- `R_mn R^mn`: `[-1.7423297741,-0.1323560370,-3.3439158197,1.3579882480,0.2206726509,0.2169373627]`, max error `1.83e-7`;
- `R_mn Box R^mn`: `[1.5754151008,0.0489981406,2.5059613346,-0.6443314817,-0.2558359645,-0.3828535821]`, max error `2.92e-7`.

Source-completed Ward residuals fall by factor ~4 when the metric-amplitude differentiation step is halved:

- Ricci2: `4.000076`;
- RicciBoxRicci: `4.000001`.

Raw soft2 rank: Iteration-178 zero-K2 curvature-cubic rank 4 -> +EH rank 5 -> +Ricci2 rank 6/6. This is **not** conditioned comparator saturation because the six local quadratic `K2` columns already have rank 6/6; exact K2 calibration removes their independent parameter directions.

Retain:

- `C5-NG-011 — EH_AND_RICCI2_SOFT2_COLUMNS_COMPLETE_THE_RAW_SIX_ROW_LOCAL_C5_SOFT2_RANK_BUT_NOT_THE_HARD_CONDITIONED_SPAN`;
- `REL-NG-002 — RAW_CUBIC_ROW_SATURATION_BY_PARAMETERS_ELIMINATED_BY_EXACT_K2_CALIBRATION_IS_NOT_CONDITIONED_COMPARATOR_SATURATION`;
- `C5-NG-012 — HIGHER_QUADRATIC_DERIVATIVE_SOFT2_COLUMNS_MUST_BE_DERIVED_COVARIANTLY_AND_NOT_INFERRED_FROM_N0_N1`.

`MODEL_READINESS: 24%` — unchanged.

Next: derive covariant soft2 completions for `R_mn Box^n R^mn`, n=2,3,4, then form the K2-calibrated nonlocal combination.
