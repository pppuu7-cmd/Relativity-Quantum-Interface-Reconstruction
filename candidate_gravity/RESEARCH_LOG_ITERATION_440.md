# RQIR Candidate Gravity — Research Log Iteration 440

## Prospective precision closure

Iteration 440 is allocated uniquely before inspecting its numerical result. It is the next deepest-first parent precision gate after raw-valid Iterations 438 and 439.

## Frozen object

Evaluate the exact Iteration-270 signed finite-difference assembly

`Acoef = sum_sigma [prod(sigma) A_finite(sigma*h)] / (2h)^n`

for all seven nonempty subsets of `LEGS=('s','a','b')`, with `M=POS`, `p=P0`, and the unchanged parent amplitude steps:

- one leg: `h1=1e-4`;
- two legs: `h2=5e-4`;
- three legs: `h3=1e-3`.

The arbitrary-precision `A_finite` implementation is exactly the already raw-valid Iteration-438 arithmetic core. No dynamics, routing, normalization, amplitudes, momenta, or step sizes are changed.

## Frozen acceptance before result

- precision levels exactly 80 and 120 decimal digits;
- maximum scaled `Acoef(80)-Acoef(120)` discrepancy `<=1e-30` over all seven subsets;
- all outputs finite;
- exact census: 26 signed nodes and seven subsets.

Binary64-vs-120-digit `Acoef` discrepancy is recorded diagnostically and is not itself a pass/fail ceiling for this gate. This avoids turning the Iteration-439 cancellation amplification into an unfrozen post-hoc physical threshold.

## Scope discipline

A PASS certifies arithmetic closure of the signed `Acoef/Asub` assembly only. It does not certify finite-difference truncation, alternate-step stability, Iterations 368/370, 379/374, 407, frozen Iteration 424, or physical index-2 `D_s`.

No smaller amplitude step, no physical mass-step change, no threshold weakening, no zero fill, no `ANSATZ-003`, no Fisher/resources.

MODEL_READINESS: 24%
