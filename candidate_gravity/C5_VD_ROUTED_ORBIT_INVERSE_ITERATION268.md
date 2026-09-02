# RQIR Candidate Gravity — Iteration 268

## Physical routed orbit-metric / inverse-resolvent kernel layer

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Starting point

Iteration 267 froze the condensed-index Fourier support rule for the eight independent null-soft cubic `B3[s,a,b]` representatives and prohibited treating operator transpose as a raw same-routing matrix transpose. The next required ingredient is an explicitly routed physical orbit-metric inverse.

This iteration constructs that layer using the same frozen `D=4`, `Lambda=0`, `a=-1/2`, linear covariant-metric split and the same three physical TT modes used in Iteration 264.

## Routed physical orbit metric

For a background Fourier insertion `x`, the physical orbit-metric kernel obeys

`N1[x] : p -> p+k_x`.

For a mixed pair `[x,y]`,

`N2[x,y] : p -> p+k_x+k_y`.

The kernels are not modeled independently. They are extracted from the same finite-amplitude curved minimal vector operator

`Nhat^alpha_beta = delta^alpha_beta Box + R^alpha_beta`

and the exact Iteration-252 factorization

`N_orb = W^-1 Nhat`.

The finite-amplitude multi-mode background automatically produces the correct mixed Fourier coefficient when differentiated with respect to the selected mode amplitudes.

## Exact routed inverse recursion

Writing `Q0(p)=N0(p)^-1`, coefficient matching of the convolution identity `N Q = I` gives

`Q1[x](p) = -Q0(p+k_x) N1[x](p) Q0(p)`.

For distinct legs `x,y`,

`Q2[x,y](p) = Q0(p+k_x+k_y) * [`

`  N1[x](p+k_y) Q0(p+k_y) N1[y](p)`

`+ N1[y](p+k_x) Q0(p+k_x) N1[x](p)`

`- N2[x,y](p)`

`] * Q0(p)`.

This is the routed version of the Iteration-259 inverse recursion. The intermediate and endpoint `Q0` factors are evaluated at their actual orbit momenta.

## Numerical physical certificate

Using loop momentum

`p=(0.7,-0.4,0.5,0.9)`

and the frozen `s,a,b` TT modes, the routed first-order inverse kernels are nonzero:

- `||Q1[s]||_F = 1.581115582762809`;
- `||Q1[a]||_F = 2.6872621928253255`;
- `||Q1[b]||_F = 2.370195667857029`.

The exact first-order inverse residual

`N0(p+k_x) Q1[x](p) + N1[x](p) Q0(p)`

is at most `2.22e-16`.

The mixed routed second-order kernels are also explicitly nonzero:

- `||Q2[s,a]||_F = 1.8134643518040645`;
- `||Q2[s,b]||_F = 3.0273925479532595`;
- `||Q2[a,b]||_F = 1.247422437428577`.

Their exact second-order convolution residual is below `8.89e-16`. Mixed-leg exchange agrees within the finite-difference envelope, with worst observed mismatch `2.66e-10`.

## Why the Iteration-267 routing guardrail is physical

If one incorrectly replaces the left endpoint `Q0(p+k_x)` by `Q0(p)` and uses

`Q1_wrong = -Q0(p) N1[x](p) Q0(p)`,

the first-order inverse identity fails macroscopically:

- soft leg residual: `0.5413765563`;
- hard-a residual: `0.2259660188`;
- hard-b residual: `0.9129651253`.

Therefore the Iteration-267 prohibition

`NO_FIXED_PLUS_K_MATRIX_TRANSPOSE_AS_KERNEL_TRANSPOSE`

has a direct companion at the inverse-resolvent level:

`Q0` cannot be frozen at one loop momentum throughout a routed composite kernel.

Freeze:

`PASS_SCOPED_PHYSICAL_ROUTED_N1_N2_Q1_Q2_KERNEL_LAYER`.

Guardrail:

`Q0 MUST BE EVALUATED AT EACH ROUTED ENDPOINT/INTERMEDIATE MOMENTUM; SAME-p RESOLVENT INSERTION IS FALSE`.

## Scientific meaning

This is a genuine physical C5 numerator-library advance. It closes the routed `N/Q` side needed by the eight Iteration-267 `B3` representatives. It is not yet the complete `B3` numerator because routed physical `K0/K1/K2 -> A1/A2/A3` still has to be instantiated at matching endpoint/intermediate momenta.

No tensor reduction, source projection or Lorentzian discontinuity is authorized yet.

Retain

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`,

`BLOCKED_NOT_ZERO`.

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 267: **0 percentage points**. The physical routed inverse-resolvent half of the cubic kernel is now explicit and internally exact, but the complete C5 comparator coordinate has not yet closed. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate — Iteration 269

Construct the matching routed physical `K0/K1/K2` kernels from the frozen affine generator and `Gamma0/Gamma1/Gamma2` library, contract them with the already-certified physical `E1/E2/E3` to obtain routed `A1/A2/A3`, and instantiate the eight forward `+K` `B3[s,a,b]` representatives using the routed `Q0/Q1/Q2` layer from this iteration. Reconstruct the seven transpose partners only by endpoint-reversed / `-K` kernel transpose. Determine whether the assembled physical `B3[s,a,b]` is explicitly nonzero before any tensor reduction. Do not create `ANSATZ-003`; do not run Fisher/resources or blind heavy integration.
