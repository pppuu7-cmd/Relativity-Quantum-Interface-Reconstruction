# RQIR Candidate Gravity — Iteration 309

Date: 2026-09-03

MODEL_READINESS: 24%

Iteration 309 closes the typed operator/index and first-background-variation contract for the active `e=2,c<=1` U2 route.

Validated run `33706649537`, job `100497090836`, artifact `9875434395`, scientific JSON SHA-256 `13212ec8aa06c5d1d85e0f57bf1a030ca0169d01edcb6eda3744749385db9c8e`; sentinel 309 and authority schema PASS.

Frozen index contract:

`(U2)^a_b = N_L^a_c (V1_L)^c_I H^I_J (V1_R)^J_d N_R^d_e Y^e_b`.

The exact first-background derivative contains six ordered site insertions, matching Iteration 308's 12 surviving U2 rows with two rows per site. The numerical typed-contract checks pass with finite-difference relative residual `1.2814180793518664e-10` and cyclic-trace absolute residual `8.526512829121202e-14`.

Classification:

`PASS_E2C1_U2_TYPED_OPERATOR_INDEX_AND_FIRST_VARIATION_CONTRACT__PHYSICAL_COMPONENT_KERNELS_REMAIN_BLOCKED`.

The physical `V1_1`, mixed `V1_2`, `H0`, and `H1` component formulas are not supplied by this gate and remain BLOCKED rather than zero-filled. Therefore no e2c1 numerator reconstruction is authorized from Iteration 309 alone.

To avoid idle compute without violating prerequisites, Iteration 310 was launched on the independent `Tr U1^2` branch to freeze the exact mapping of the eight cyclic classes onto authoritative U1 primitive routing.

MODEL_READINESS: 24% — unchanged.
