# Recovery Delta — Iteration 540

Date: 2026-09-07

## New exact diagnostic authority
While canonical QUARTER rank3 run `34115105768` remained in progress, no duplicate heavy run was launched. An independent exact BASE/HALF/QUARTER truncation-ratio diagnostic was closed.

For `X_h=D+A+B+C+O(h^10)`, `A=a h^4`, `B=b h^6`, `C=c h^8`, with `d1=BASE-HALF` and `d2=HALF-QUARTER`:

- `d1=(15/16)A+(63/64)B+(255/256)C`,
- `d2=(15/256)A+(63/4096)B+(255/65536)C`.

Pure-order exact ratios `d1/d2` are 16 (h^4), 64 (h^6), 256 (h^8).

For h^4+h^6 only, with `t=B/A` and nonzero `d2`:

`r=d1/d2=(16+64*(21/80)t)/(1+(21/80)t)`,

and

`t=(80/21)(r-16)/(64-r)`.

Exact cancellation points: `d1=0` at `B/A=-20/21`; `d2=0` at `B/A=-80/21`.

Same-sign A,B imply `16<=r<=64`; same-sign A,B,C imply `16<=r<=256`. A violation is a truncation-sign/cancellation diagnostic, not by itself a Candidate-Gravity consistency FAIL.

Classification:
`PASS_ITER424_THREE_LEVEL_STEP_RATIO_SIGN_STRUCTURE_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`.

Reproducible files:
- `candidate_gravity/code/iteration540_iter424_three_level_step_ratio_sign_contract.py`
- `candidate_gravity/results/iteration540_iter424_three_level_step_ratio_sign_contract.json`

Frozen Iteration-424 physical acceptance is unchanged. Physical unresolved set remains `[2]`. Comparator residual remains absent; `ANSATZ-003`, Fisher and resources remain BLOCKED.

`MODEL_READINESS: 24%`

Readiness change: 0 percentage points; no stable rubric sector closed.

Exact next gate: after rank3 terminal completion, fail-closed raw-consume run `34115105768`. Only raw-valid PASS authorizes frozen rank4 `(-1.25e-6,-1.25e-6)`.
