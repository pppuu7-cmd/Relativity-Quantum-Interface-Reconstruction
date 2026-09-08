# Candidate Gravity — Iteration 596 pre-result nonlinear Ward contract

Date: 2026-09-08

Status: **PROSPECTIVELY FROZEN BEFORE FULL CUBIC WARD EVALUATION**.

This artifact fixes the exact Ward target that was operationally missing in Iter595. It does **not** evaluate the Iter594 13-term cubic source response and therefore cannot be a nonlinear-Ward PASS/FAIL, Candidate-Gravity consistency result, comparator identity, residual, or novelty certificate.

## Parent authority

- MSSC-001 scalar action and K1 Ward identity: Iter218 / Iter587.
- Exact three-mode source fixture and singleton/pair routing: Iter588.
- Same-action K1/K2 normalization: Iter589.
- Complete cubic inverse-kernel family identity: Iter590.
- Full routed 13-term source assembly: Iter594.
- Iter595 authority audit: a gauge-leg-only substitution is not the full nonlinear Ward identity.

No Source/Born subtraction is performed here.

## Fourier and stripped-i convention

Use MSSC signature `eta=(+---)` and

`f(x) = integral_k exp(-i k.x) f(k)`.

Thus `partial_mu -> -i k_mu`. Every term in the infinitesimal diffeomorphism variation contains one common factor `-i`; the Ward contract below divides that common factor out once and calls the resulting real tensor rule the **stripped-i convention**. This convention changes no relative sign between gauge-leg, spectator, and scalar-endpoint terms.

For one gauge parameter mode `xi(q)`, define the linear metric variation

`R0(q,xi)_{mu nu} = q_mu xi_nu + q_nu xi_mu`.

For a spectator graviton mode `h(k)`, the nonlinear Lie-derivative contribution is

`R1[q,xi] h(k)_{mu nu}`
` = (k.xi) h_{mu nu}`
` + q_mu xi^rho h_{rho nu}`
` + q_nu xi^rho h_{mu rho}`,

and carries output momentum `k+q`.

This is exactly the stripped Fourier transform of

`xi^rho partial_rho h_{mu nu} + h_{rho nu} partial_mu xi^rho + h_{mu rho} partial_nu xi^rho`.

No additional `O(h^2)` metric term is introduced: for `g=eta+h`, the Lie derivative `L_xi g` is affine in `h` at fixed `xi`, so `R=R0+R1[h]` is sufficient for the cubic recursion.

## Scalar/source endpoint operator

The MSSC scalar transforms as a scalar, `delta_xi phi = xi^rho partial_rho phi`. In the same stripped-i convention define the endpoint operator `E_{q,xi}` by its action on the free propagator for `p' = p+q`:

`E_{q,xi} G0 = (p.xi) G0(p) - (p'.xi) G0(p')`.

This is not an adjustable counterterm. It is the two scalar-endpoint transformation inherited from the same scalar action.

The sign is frozen by the Iter587 one-leg reduction below.

## Master Ward identity

Let `G[h]=K[h]^{-1}` denote the same MSSC scalar two-point response used in Iter590/594. Diffeomorphism covariance is frozen in the functional form

`D G[h] . (R0 + R1[h]) + E G[h] = 0`.

Take two independent source derivatives with respect to spectator modes `h_a(k_a)` and `h_b(k_b)` and then set `h=0`. The **full cubic nonlinear Ward target** is

`W3(q,xi; a,b) =`

`D^3 G[ R0(q,xi), h_a, h_b ]`
`+ D^2 G[ R1[q,xi] h_a, h_b ]`
`+ D^2 G[ h_a, R1[q,xi] h_b ]`
`+ E_{q,xi} ( D^2 G[h_a,h_b] )`
`= 0`.

This is the prospectively frozen target for the next numerical/scalar-routing audit.

### Meaning of the four terms

1. `D^3G[R0,a,b]` is the complete Iter594 object with the gauge leg inserted and therefore retains **K3 + all six K1/K2 + all six K1^3 chains**.
2. `D^2G[R1 a,b]` is the nonlinear diffeomorphism action on spectator `a`.
3. `D^2G[a,R1 b]` is the nonlinear diffeomorphism action on spectator `b`.
4. `E D^2G[a,b]` is the transformation of the two scalar/source endpoints of the full quadratic response.

No one of these four terms may be dropped, repartitioned, or projected family-by-family before testing `W3=0`.

## Exact one-leg reduction to Iter587

With both spectators removed, the master identity reduces to

`D G[R0] + E G0 = 0`.

Write `K0(p)=m^2-p^2`, `G0(p)=1/K0(p)`, `p'=p+q`. Iter587 gives

`q_mu V^{mu nu} xi_nu = K0(p') (p.xi) - K0(p) (p'.xi)`.

Because `K1(R0)=q_mu V^{mu nu} xi_nu` under the frozen Iter589 normalization and

`D G[R0] = -G0(p') K1(R0) G0(p)`, one gets exactly

`D G[R0] = -(p.xi) G0(p) + (p'.xi) G0(p')`.

Therefore

`D G[R0] + E G0 = 0`

identically. The spectator-free limit is thus **exactly the Iter587 inverse-propagator Ward identity**, not a newly fitted sign convention.

## Exact Iter588 fixture binding

For each choice of gauge singleton `g in {s,a,b}`:

- `q = q_g` from the exact Iter588/Iter368 fixture;
- `{a,b} = {s,a,b} \ {g}` are the two spectators;
- `q + k_a + k_b = 0` is inherited exactly from the fixture;
- choose a fixed, nonzero real test vector `xi` **before evaluation**. The next implementation must use the same `xi` for all algebraic families in a given gauge-leg test and must report the choice explicitly; changing `xi` after seeing residuals is forbidden.
- `R1[q,xi]h_a` carries momentum `k_a+q=-k_b`, and `R1[q,xi]h_b` carries momentum `k_b+q=-k_a`, so both quadratic spectator terms close on the same three-mode fixture without a new momentum split parameter.

The numerical implementation must test all three gauge-singleton choices and may not keep only the best one.

## Classification and guardrails

Classification of this pre-result freeze:

`PASS_PRE_RESULT_FULL_NONLINEAR_WARD_RECURSION_CONTRACT__ITER587_REDUCTION_EXACT__NON_WARD_NON_RESIDUAL`

This means only that the previously missing target is now well-defined before seeing its value.

It is **not**:
- a nonlinear Ward PASS or FAIL;
- Candidate-Gravity consistency PASS/FAIL;
- an exact comparator identity;
- regime-specific non-identifiability;
- near-degeneracy;
- a novelty certificate;
- a comparator-subtracted residual.

`Source/Born subtraction = NOT_PERFORMED`.

`ANSATZ-003 = FORBIDDEN`.

`Fisher/resources = FORBIDDEN`.

The fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remains `OPERATIONAL_BLOCKED` until the full source Ward gate closes and the complete source observable is mapped to Iter582/native-linked coordinates.

## Exact next gate

Implement this frozen recursion on the exact Iter588 fixture using the same MSSC inverse kernel and parameter convention as Iter589/594. Evaluate **all four terms** of `W3` for all three gauge-singleton choices, retain K3 and K1^3, verify routing closure and the Iter587 one-leg anchor in the same code path, and classify the result without changing `xi`, thresholds, routing, normalization, or family content after seeing the output.
