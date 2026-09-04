# RQIR Candidate Gravity — Research Log Iteration 441

## Prospective representation/truncation gate

Iteration 441 is allocated before inspecting its result. Iteration 440 closed 80/120-digit arithmetic precision of the frozen two-point-per-axis `Acoef/Asub` assembly; the remaining question is finite-difference truncation/representation error.

## Independent oracle without smaller h

For every nonempty subset of `LEGS=('s','a','b')`, compare the exact frozen Iteration-270 central two-point-per-axis mixed derivative against a tensor-product fourth-order first-derivative stencil using the **same base spacings**:

- one leg: `h1=1e-4`;
- two legs: `h2=5e-4`;
- three legs: `h3=1e-3`.

The fourth-order one-axis rule is

`f'(0) ~= [f(-2h)-8 f(-h)+8 f(+h)-f(+2h)]/(12h)`.

For n legs, use the tensor product of these one-axis rules. This adds only `±2h` amplitude nodes; it does not reduce any frozen spacing and does not change parent dynamics.

## Frozen acceptance before result

- high-order stencil evaluated independently at 80 and 120 decimal digits;
- max scaled 80-vs-120 high-order derivative discrepancy `<=1e-30`;
- max scaled frozen central-vs-high-order derivative discrepancy `<=2e-5` across all seven subsets;
- all outputs finite;
- exact high-order node census: `124` evaluations per precision level (`12 + 48 + 64`).

The `2e-5` ceiling is frozen prospectively to ensure this parent representation error cannot exceed the already frozen physical convergence tolerance. It is not relaxable after result inspection.

## Scope

PASS closes only the Iteration-270 `Acoef/Asub` finite-amplitude stencil representation at the frozen spacings. It does not certify 368/370, 379/374, 407, Iteration 424, or physical index-2 `D_s`.

No smaller amplitude step, no physical mass-step change, no threshold weakening, no zero fill, no `ANSATZ-003`, no Fisher/resources.

MODEL_READINESS: 24%
