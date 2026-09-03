# RQIR Candidate Gravity Recovery Delta — Iteration 366

Date: 2026-09-03

MODEL_READINESS: 24%

## Scope

Physical normalized integration of the 18 timelike simple-simple cut channels inside repeated `(2,1,1)` `Tr U2` families. The unique double-pole group remains uncut and is retained directly; an auxiliary-mass derivative representation is used as an independent cross-check.

## Validated authority

- run `33801929554`
- job `100803251999`
- workflow/head commit `a7b12b674d9f648a2f2b24b981f9d061b5cad07c`
- code commit `f0e03cef68e7c209758349c8bd81e8c60e4e9c4c`
- artifact `9911685784`, `iteration366-result`
- artifact digest `sha256:2e05202456e9b5820d88b17e242d24864a8274a2d49950b5b856b058fe5f35b7`
- raw scientific JSON SHA-256 `df86388db9ecfd9a0df565cba050bea679267fbc5698bb6ba04030c66c38e0e6`
- exactly one top-level JSON object; sentinel `366`; authority audit `scientific_authority_pass=true`.

Freeze:

`PASS_U2_REPEATED_FAMILY_SIMPLE_SIMPLE_18_PHYSICAL_CUTS__ALL_CONVERGED__DIRECT_AUX_AGREE`

## Numerical result

Census:
- typed channels: `18`;
- `CONVERGED=18`;
- `BLOCKED_CONVERGENCE=0`;
- q2 buckets: `3`;
- max cut-shell absolute error: `1.5830329958809877e-16`;
- max scaled angular convergence error: `1.755966985998638e-08` under frozen `2e-5`;
- max direct-vs-aux scaled error: `1.3870141151275523e-11` under frozen `2e-8`;
- minimum sampled uncut absolute denominator: `0.12097829436145645`.

Normalized q2-resolved sums for this 18-channel sector:

- `D_s TrU2_repeat_simple(q^2=-1) = -6.812363349599648e-05`;
- `D_s TrU2_repeat_simple(q^2=-0.34) = -8.405976034846215e-05`;
- `D_s TrU2_repeat_simple(q^2=-0.14) = -7.069545900379072e-05`.

All stored imaginary parts are zero in this normalized `D_s` coordinate.

## Interpretation

This is a genuine nonzero physical contribution from the repeated-family simple-simple sector. It is not the full `Tr U2`: the 48 cut-through-double-pole channels are still being evaluated independently in Iteration 364. It is not yet the full eom-degree2 connection contribution because `Tr U1^2` remains open.

The Iteration-361 ordinary-simple cancellation remains separately frozen and must not be used to zero-fill this sector.

## Exact next gate

Once Iteration 364 is raw-artifact validated, combine only within each external q2 bucket:

`D_s TrU2_total(q2) = D_s TrU2_ordinary_simple_361(q2) + D_s TrU2_cut_through_double_364(q2) + D_s TrU2_repeat_simple_366(q2)`.

Do not fold the `+i/2` effective-action coefficient into the pure `Tr U2` closure. Do not include `Tr U1^2` in that sum.

In parallel, physically re-audit the old Iteration-310 `Tr U1^2` null-soft pruning on the current timelike fixture before using its historical 8 cyclic classes.

MODEL_READINESS: 24%
Change from Iteration 365: `0 pp`; a physical nonzero U2 sub-sector is closed, but the complete U2 and the eom-degree2 effective-action sector are not yet closed and no robust comparator-subtracted residual exists.
