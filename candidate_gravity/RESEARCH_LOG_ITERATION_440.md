# RQIR Candidate Gravity — Research Log Iteration 440

## Prospective precision closure

Iteration 440 was allocated uniquely before inspecting its numerical result. It is the deepest-first parent precision gate after raw-valid Iterations 438 and 439.

## Frozen object

Evaluate the exact Iteration-270 signed finite-difference assembly

`Acoef = sum_sigma [prod(sigma) A_finite(sigma*h)] / (2h)^n`

for all seven nonempty subsets of `LEGS=('s','a','b')`, with `M=POS`, `p=P0`, and unchanged parent amplitude steps `h1=1e-4`, `h2=5e-4`, `h3=1e-3`.

The arbitrary-precision `A_finite` implementation is exactly the raw-valid Iteration-438 arithmetic core. No dynamics, routing, normalization, amplitudes, momenta, or step sizes changed.

## Frozen acceptance before result

- precision levels exactly 80 and 120 decimal digits;
- maximum scaled `Acoef(80)-Acoef(120)` discrepancy `<=1e-30` over all seven subsets;
- all outputs finite;
- exact census: 26 signed nodes and seven subsets.

Binary64-vs-120-digit `Acoef` discrepancy was diagnostic only and had no pass/fail ceiling.

## Raw result

Run `33904321843`, job `101125537041`, artifact `9948876125`, digest `sha256:244e52df6a951a21d5ea20638fdf0d15875a07f6b0b3c77355d5b336cf4b479d`; raw scientific JSON SHA-256 `36ff8634a6bafae0281e99110739416d4a8a6313a62c918a9d12bfebffb6f964`.

Classification: `PASS_ITER270_ACOEF_ASUB_80_120_DIGIT_ARITHMETIC_CLOSURE__NON_PROMOTING`.

Observed:
- max 80-vs-120 scaled discrepancy `1.4149749985220297e-75`, far below `1e-30`;
- exact 26-node / 7-subset census;
- all values finite;
- diagnostic max binary64-vs-120 discrepancy `1.890704312519492e-10`, attained in `(s,a,b)`.

## Scientific consequence

Arithmetic precision of the frozen `Acoef/Asub` signed assembly is closed. The remaining parent uncertainty is finite-difference truncation / representation rather than 80/120-digit arithmetic. Iteration 441 therefore compares the unchanged central stencil to a same-spacing fourth-order tensor-product derivative oracle using only `±h, ±2h` nodes and no smaller h.

## Scope discipline

This PASS does not certify finite-difference truncation, Iterations 368/370, 379/374, 407, frozen Iteration 424, or physical index-2 `D_s`.

No smaller amplitude step, no physical mass-step change, no threshold weakening, no zero fill, no `ANSATZ-003`, no Fisher/resources.

MODEL_READINESS: 24%
