# Recovery Delta — Candidate Gravity Iteration 340

Date: 2026-09-03

## Scope

Primary-authority audit of the physical `U2` contract before deriving the blocked `V1_1/V1_2` component kernels. Source: Giacchini, de Paula Netto & Shapiro, PRD 102, 106006 (2020), arXiv:2006.04217v4, Eqs. (14)-(17).

## Result

Eq. (17) fixes

`U2^alpha_beta = N^{alpha gamma} A_{i gamma} (Hinv_VD)^{ij} A_{j delta} N^{delta sigma} Y_{sigma beta}`,

with `A_{i gamma}=(D_i R^k_gamma) epsilon_k` and the paper convention `H * Hinv_VD = -1`.

If `A` is stored as `field x ghost`, the exact typed matrix order is

`N_left @ A.T @ Hinv_VD @ A @ N_right @ Y`.

Therefore the Iteration-309 placeholders are no longer orientation-ambiguous: `V1_L=A.T` (`ghost x field`) and `V1_R=A` (`field x ghost`). The primary paper also fixes a sign that was not explicit in Iteration 339: when the Iteration-319 differential operator is denoted `K`, the Green object entering Eq. (17) is `Hinv_VD=-K^{-1}`. Iteration 339's shifted inverse-routing identity remains algebraically correct for ordinary `K^{-1}`, but its interpretation as the actual Eq. (17) `U2` Green object must carry this one global minus sign. This is a scoped convention correction, not a Candidate Gravity consistency FAIL.

A reproducible exact-rational contraction check independently verifies the explicit-index Eq. (17) against `N @ A.T @ Hinv_VD @ A @ N @ Y` and verifies the global sign relative to using `+K^{-1}`.

Authority:

`PASS_U2_PRIMARY_AUTHORITY_V1_LEFT_RIGHT_ORIENTATION_AND_VD_GREEN_MINUS_SIGN__PHYSICAL_A1_A2_COMPONENTS_REMAIN_BLOCKED`.

## Status

- closed: primary definition of `V1` as `A_{i gamma}=(D_i R^k_gamma) epsilon_k`;
- closed: left/right orientation `A.T / A`;
- closed: Eq. (17) inverse sign bridge `Hinv_VD=-K^{-1}`;
- retained: Iteration-339 shifted momentum routing, with the above global sign applied at `U2` assembly;
- BLOCKED: physical same-parent background expansions `A1/A2`;
- BLOCKED: required `N/Y` inverse-routing bridge;
- forbidden: physical `Tr U2` numerator before both blockers close.

No ANSATZ-003, Fisher/resources, Source/Born subtraction or blind full-C5 work is authorized.

MODEL_READINESS: 24%

Change from Iteration 339: `0 pp`; an exact U2 convention/orientation ambiguity and a potentially dangerous global sign were closed, but no complete readiness rubric bucket and no robust comparator-subtracted residual closed.

## Exact next gate

Iteration 341: derive the physical same-parent first and second background coefficients `A1/A2` of `A_{i gamma}=(D_i R^k_gamma) epsilon_k` in the frozen `D=4, Lambda=0, a=-1/2` convention, validate them against a direct geometry/functional finite-difference oracle in the exact `A.T / A` orientation, then separately close `N/Y` inverse routing before assembling `Tr U2`.
