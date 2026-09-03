# Recovery Delta — Candidate Gravity Iteration 341

Date: 2026-09-03

MODEL_READINESS: 24%

## Scope

Physical same-parent first/second background expansion of the Vilkovisky `U2` vertex

`A_{i gamma} = (D_i R^k_gamma) epsilon_k`

using the explicit gravity `V1` formula of Giacchini, de Paula Netto & Shapiro, PRD 102, 106006 (2020), arXiv:2006.04217v4, Eqs. (54)-(55), specialized to the frozen RQIR convention `D=4`, `Lambda=0`, `a=-1/2`, standard linear split `g=eta+h` (`gamma1=1`, `gamma2=0`).

## Result

Freeze:

`PASS_U2_PHYSICAL_SAME_PARENT_V1_A1_A2_BACKGROUND_KERNELS_EQ55_EXACT_GEOMETRY_ORACLE__NY_ROUTING_REMAINS_BLOCKED`.

The executable polynomial expansion and an independent exact-geometry oracle agree for both first and second background orders. The oracle reconstructs exact metric/connection/curvature geometry at finite background amplitude, uses coordinate finite differences for the covariant curvature derivatives, and independently fits the amplitude expansion.

Validated numerical authority:

- `A0_max_abs = 0`;
- two physical first-order `A1` mode kernels, nonzero, `max_abs_A1_kernel = 0.018650374927342728`;
- three second-order `A2` partitions, nonzero, `max_abs_A2_kernel = 0.003959180245018564`;
- `A1_oracle_max_abs_error = 5.3656298154569626e-14` against frozen threshold `1e-9`;
- `A2_oracle_max_abs_error = 4.2452437485490657e-10` against frozen threshold `2e-7`.

Thus the physical `V1` blocker is no longer an unsupported placeholder: `A1/A2` are executable same-parent component authority in the exact Iteration-340 orientation

- `A` = field x ghost (`10x4`),
- `V1_L=A.T`,
- `V1_R=A`,
- `Hinv_VD=-K^{-1}`.

## Actions provenance

- run `33768093500`
- job `100690999759`
- head/workflow commit `1bfdd7c966d80968260ad3964dcd8335a60c4859`
- code commit `41ed1cfac94ac67ecfa2a7d891b11d096c075cd3`
- artifact `9898398784`, `iteration341-result`
- artifact digest `sha256:2da676041d893b4c85c029fe5f2aec9c7ea16ae0a4a00f9a6a72b88d53ea2888`
- scientific JSON SHA-256 `d345e932fbfd322f9ddf9c4d647df7d71144fd52010b7f56eeb5b0bf67291b23`
- exactly one top-level JSON object, sentinel `341`, `scientific_authority_pass=true`.

Scientific result is retained at `candidate_gravity/results/iteration341_u2_v1_a12_same_parent_geometry.json`.

## Remaining U2 blocker

Physical `Tr U2` numerator assembly remains BLOCKED only until the same-parent `N/Y` inverse-routing bridge is frozen. Primary Eq. (57), together with the already-frozen minimal ghost operator of Iteration 317, supplies the next route. Do not assemble `U2` before that bridge is independently validated.

## Guardrails

- Iteration-340 `A.T/A` orientation and `Hinv_VD=-K^-1` are binding.
- Unsupported remains BLOCKED, never zero-filled.
- No Source/Born subtraction.
- No ANSATZ-003, Fisher/resources or blind full-C5 calculation.

## Exact next gate

Iteration 342: close the same-parent `N/Y` inverse-routing bridge in the `a=-1/2` minimal ghost convention using the primary relations `hat N = Y N`, Eq. (57), and the frozen Iteration-317 ghost operator. Validate both the shifted inverse identity and the algebraic identities linking `N`, `Y` and `hat N^{-1}` before first-background-order `Tr U2` assembly.

MODEL_READINESS remains 24%. This closes a hard physical U2 component blocker but not an entire readiness rubric bucket and not a comparator-subtracted residual.
