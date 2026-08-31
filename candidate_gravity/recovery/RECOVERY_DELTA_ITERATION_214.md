# Recovery Delta — RQIR Candidate Gravity Iteration 214

Date: 2026-09-01

MODEL_READINESS: 23%

## New authority

Iteration 214 closes the **leading IR endpoint subtraction** for the physical pure-Einstein five-graviton total-s cut of Iteration 213.

Frozen external convention: real massless `2->3`, all-outgoing `--+++`, fifth positive-helicity graviton soft, total-s two-particle cut with the unique surviving MHV helicity product.

Define

`A_N = lim_(theta->0) (1-cos theta) I_cut`,

`A_S = lim_(theta->pi) (1+cos theta) I_cut`.

Result in the frozen KLT/sign convention:

`A_N(epsilon)=A_S(epsilon)=-2 i M5_tree(epsilon)`.

Endpoint extrapolation relative errors are approximately `1.46e-11...1.49e-11` for epsilon `0.04, 0.01, 0.001` on both sides.

At epsilon `0.01`:

- `M5_tree = 645.5150777243653 - 124.71057541525806 i`;
- `A = -249.42115083051613 - 1291.0301554487305 i`;
- raw two-endpoint halving-shell prediction `8 pi A log 2 = -4345.0882294083885 - 22490.63446934122 i`.

Direct raw shell errors relative to the prediction decrease to `4.8257e-5` at the smallest tested halving shell.

Freeze the canonical leading subtraction

`I_sub = I_cut - A/(1-cos theta) - A/(1+cos theta)`.

The magnitude of the excluded two-cap halving shells scales as `delta^2.0033844483`; therefore the cap dependence vanishes in the regulator limit after azimuthal integration.

## Guardrail

Do not conflate endpoint regulator independence with convergence of the full sphere integral. Large but finite outgoing-hard-leg peaks remain a numerical bulk quadrature problem. They are not additional `theta^-2` IR poles on the frozen singularity map.

## Files

- `analysis/c5_cut_klt_common.py`
- `analysis/c5_fivepoint_ir_subtraction_iteration214.py`
- `results/c5_fivepoint_ir_subtraction_iteration214.json`
- `candidate_gravity/C5_FIVEPOINT_IR_SUBTRACTION_ITERATION214.md`
- `research_log/2026-09-01_iteration_214_fivepoint_ir_subtraction.md`

## Retained labels

- `C5-CUT-013 — FIVE_GRAVITON_BEAM_ENDPOINT_COEFFICIENT_EQUALS_MINUS_2I_TIMES_EXTERNAL_BORN_M5_IN_THE_FROZEN_KLT_CONVENTION`
- `IR-NG-003 — RAW_HALVING_CAP_SHELL_TENDS_TO_8PI_A_LOG2_WITH_A_MINUS_2I_M5`
- `IR-NG-004 — AFTER_CANONICAL_LEADING_POLE_SUBTRACTION_THE_CAP_DEPENDENCE_VANISHES_AS_DELTA_SQUARED_AFTER_AZIMUTHAL_INTEGRATION`
- `NG-FUNNEL-071 — REGULATOR_INDEPENDENCE_MUST_BE_PROVED_FROM_ENDPOINT_SHELLS_NOT_FROM_A_GLOBAL_FIT_DOMINATED_BY_BULK_PEAKS`

## Next gate — Iteration 215

Construct a deterministic bulk quadrature that resolves the finite outgoing-hard-leg peaks without modifying the subtraction convention. Then evaluate the IR-subtracted finite cut on the frozen Iteration-210 12-point epsilon grid and apply the regular+log extractor. No Candidate Gravity ansatz, Fisher, or resource calculation is authorized.
