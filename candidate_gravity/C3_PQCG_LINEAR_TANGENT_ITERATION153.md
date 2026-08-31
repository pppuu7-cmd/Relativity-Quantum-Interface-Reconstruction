# Iteration 153 — first fixed finite C3-PQCG tangent

**Status:** PASS_SCOPED for the supported linear stochastic rows; full C3 comparator remains BLOCKED.

## Purpose
After Iteration 152 validated the existing local C5 nonlinear columns, the next required step was to replace the broad C3 class-capability mask by one concrete finite stochastic classical-quantum realization.

Iteration 153 freezes `C3-PQCG-LIN-001`, a literature-anchored linearized covariant postquantum-classical stochastic metric block with two positive diffusion parameters `(D2,D0)` for spin-2 and spin-0 modes.

## Supported RQIR objects from one declared dynamics
From

`box h_s = J_s + xi_s`,

`<xi_s xi_s'> = 2 D_s delta_ss' delta^4`,

follow directly:

- `J`: external conserved source channel at this scoped level;
- `chi1R`: `G_R`, nonzero and independent of `(D2,D0)`;
- `N`: `2 D_s |G_R|^2` in each stochastic spin sector.

No independent post-Gaussian object is invented. A nonlinear hybrid interaction/noise functional has not yet been frozen, therefore `C3sym` and `chi2R_even/odd` remain BLOCKED.

## Finite tangent certificate
Using the frozen Iteration-149 spacelike momenta and Gaussian smearing, all 18 sampled momenta satisfy

`0.2278 <= k^2 <= 0.7473`.

The traced `N2` coordinate is

`N2 = A (5 D2 + D0)`,

with

`A = 258.83104475297773`.

For supported rows `(N2,chi1R)` and parameter order `(D2,D0)`, the finite tangent is

`V_C3,supported = [[1294.1552237648887, 258.83104475297773], [0,0]]`.

Certificate:

- shape `2x2` on supported rows only;
- rank `1/2`;
- singular values `[1319.7845479190407, 0]`.

## Scientific interpretation
This is **not a consistency FAIL** and not an exact identity between the two diffusion parameters. It is a protocol-level, regime-specific non-identifiability:

**C3-NG-001 — ONE_NOISE_COORDINATE_COLLAPSES_TWO_DIFFUSION_DIRECTIONS.**

With only the single frozen scalar `N2` coordinate, the linear C3 block identifies only `5 D2 + D0`. A second independent tensor/scalar noise projection would be required to separate `D2` from `D0` at this level.

A second retained guardrail is introduced:

**NG-FUNNEL-011 — PARTIAL_COMPARATOR_ROWS_ARE_NOT_ZERO_ROWS.**

When a fixed comparator has not yet derived a protocol coordinate, that row is BLOCKED and must not be inserted as a zero row into the quotient matrix. Therefore the numerical rank above is a rank certificate only for the supported linear stochastic sub-block; it is not a full C3 quotient certificate.

## Literature/novelty check
The comparator choice is materially supported by current literature: the covariant CQ path-integral formalism is explicitly diffeomorphism-compatible and completely positive, while the linearized postquantum classical-gravity analysis contains stochastic spin-2 and spin-0 metric modes. This makes it a substantially stronger C3 representative than a generic class mask, but its nonlinear ordered response has not yet been derived in this repository.

## Consequences for the funnel
- C3 broad mask: superseded for the supported linear stochastic rows by `C3-PQCG-LIN-001`.
- Full C3 tangent: `BLOCKED_NONLINEAR_COMPLETION`.
- C5 higher-local and loop/nonanalytic sectors: remain BLOCKED.
- Nonlinear C4: remains BLOCKED.
- Fisher/resources: forbidden.
- `ANSATZ-003`: not created.
