# Recovery Delta — Iteration 299

Date: 2026-09-03

Classification: `PASS_EXACT_EVANESCENT_POLE_SENSITIVITY_PROMOTION_RULE__FINITE_SAME_PARENT_REMAINDER_STILL_BLOCKED`

MODEL_READINESS: 24%

## Frozen result

Let `delta=D-4`. If a dimensionally regulated numerator and master are expanded as

`N=N0+delta N1+delta^2 N2+...`

and

`M=sum_k A_k delta^k`,

then the coefficient of `delta^r` in `N M` is

`C_r=sum_j N_j A_{r-j}`.

Consequences:

- simple pole: `C_-1=N0 A_-1`, while `C_0=N0 A_0+N1 A_-1`;
- double pole: `C_-2=N0 A_-2`, `C_-1=N0 A_-1+N1 A_-2`, `C_0=N0 A_0+N1 A_-1+N2 A_-2`;
- therefore the highest Laurent pole is protected from positive-`delta` numerator orders, but finite terms across a nonzero pole are not;
- with double/higher poles, subleading poles can also be evanescent-sensitive;
- if the relevant discontinuity is pole-free, the pole-times-evanescent mechanism does not obstruct its finite cut coefficient at that order, although other same-parent/scheme/source requirements can remain.

The current 4D numerator oracle must not zero-fill evanescent coefficients invisible at `D=4`.

## Validated provenance

- run: `33700556512`
- job: `100478719987`
- artifact: `9873345427`
- artifact digest: `sha256:e01b2e24de344944675819c3af1cd3b6d8f2a41ddff5dba9c592b1173ac428f1`
- head SHA: `ae442b799fd1834e9a41cc20012b667cccddac88`
- scientific result SHA-256: `735c4806e3780434410a343bfea0e8497a7d2e00b51f2967cc008a31004a47f9`
- schema validator: PASS
- top-level JSON count: 1
- iteration sentinels: `[299]`

## Guardrails

`FOUR_DIMENSIONAL_ORACLE_ABSENCE_OF_EVANESCENT_TERMS_IS_NONIDENTIFIABILITY_NOT_ZERO`

`DO_NOT_PROMOTE_FINITE_REMAINDER_ACROSS_A_NONZERO_POLE_WITHOUT_REQUIRED_D_DIMENSIONAL_NUMERATOR_COEFFICIENTS_OR_EXPLICIT_SCHEME_CONVERSION`

`LEADING_HIGHEST_LAURENT_POLE_IS_INSENSITIVE_TO_POSITIVE_DELTA_NUMERATOR_ORDERS`

## Next permitted gate

Audit the corrected fail-closed Iteration-296 bubble result under this theorem. Promote only schema-validated coefficients whose Laurent order is protected. Full same-parent finite comparator authority remains unavailable until a D-dimensional numerator continuation or explicit scheme conversion is frozen.
