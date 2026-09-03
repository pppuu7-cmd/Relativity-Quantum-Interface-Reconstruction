# RQIR Candidate Gravity Recovery Delta — Iteration 309

Date: 2026-09-03

MODEL_READINESS: 24%

## Authority

Iteration 309 freezes the typed operator/index contract and exact first-background Leibniz variation for the remaining `e=2,c<=1` U2 route, without inventing unsupported physical component kernels.

Freeze:

`PASS_E2C1_U2_TYPED_OPERATOR_INDEX_AND_FIRST_VARIATION_CONTRACT__PHYSICAL_COMPONENT_KERNELS_REMAIN_BLOCKED`

Validated Actions provenance:

- run `33706649537`
- job `100497090836`
- head `a4dd40dfc2e06744c631558bd11a9f437276947d`
- artifact `9875434395`, `iteration309-result`
- artifact digest `sha256:df67ff16cc42710d4260b50ed0f2eea28bfeb400a53244db8b38bea6cec08810`
- scientific JSON SHA-256 `13212ec8aa06c5d1d85e0f57bf1a030ca0169d01edcb6eda3744749385db9c8e`
- exactly one top-level JSON object, sentinel `309`, authority validator PASS.

## Exact contract

`U2 = N_L V1_L H V1_R N_R Y` with index typing

`(U2)^a_b = N_L^a_c (V1_L)^c_I H^I_J (V1_R)^J_d N_R^d_e Y^e_b`.

Ghost indices are `a,b,c,d,e`; symmetric-field indices are `I,J`. The left V1 orientation maps field to ghost (`S->G`), the right orientation ghost to field (`G->S`). No reversal quotient is assumed.

The first-background variation contains exactly six Leibniz terms, one for each site `N_L,V1_L,H,V1_R,N_R,Y`, matching the Iteration-308 survivor census of two rows per site and 12 surviving ordered U2 placements total.

Numerical contract audits:

- finite-difference relative residual `1.2814180793518664e-10` <= `5e-9`
- cyclic-trace absolute residual `8.526512829121202e-14` <= `1e-9`.

## Fail-closed blockers

The following physical component kernels remain BLOCKED and were not zero-filled:

- `V1_1` flat momentum kernel
- mixed `V1_2`
- flat graviton Green/projector `H0`
- first-background `H1`.

`N1/Y1` may only be reused after a same-parent routing check.

## Independent continuation

Because the U2 physical component extraction remains blocked, Iteration 310 was launched on the independent allowed `Tr U1^2` branch to map the eight cyclic classes onto authoritative U1 routing without new symmetry assumptions.

## Readiness

MODEL_READINESS: 24%

Change: `0 pp`. This closes an operator-contract prerequisite but no stable readiness-rubric block.
