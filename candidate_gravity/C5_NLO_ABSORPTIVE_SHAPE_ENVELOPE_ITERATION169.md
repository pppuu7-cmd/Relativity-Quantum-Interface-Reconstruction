# Candidate Gravity — Iteration 169: next-order C5 absorptive shape envelope

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Status:** conservative NLO C5 shape envelope frozen; no Candidate Gravity residual promoted

## Objective

Iteration 168 proved that the complete leading one-massless-loop curvature-squared C5 TT absorptive sector is one-dimensional and is removed exactly by the Iteration-167 constant-shape profile.

Iteration 169 asks the next required question before any candidate search:

> Which frequency shapes are already authorized by gravitational EFT at the next derivative/loop order?

## Power-counting authority

For gravity EFT, the energy order of a graph is controlled by

`P = 2 + 2 L + sum_v (d_v - 2)`,

where `L` is loop order and `d_v` the derivative order of inserted vertices. This is the standard gravitational analogue of Weinberg power counting.

References:

- C. P. Burgess, *Quantum Gravity in Everyday Life: General Relativity as an Effective Field Theory*, Living Rev. Rel. 7 (2004) 5;
- J. F. Donoghue, *The effective field theory treatment of quantum gravity*, arXiv:1209.3511;
- J. F. Donoghue and T. Torma, *On the power counting of loop diagrams in general relativity*, hep-th/9602121;
- M. H. Goroff and A. Sagnotti, Phys. Lett. B160 (1985) 81 and Nucl. Phys. B266 (1986) 709, establishing the genuinely new two-loop six-derivative order in pure gravity.

At `O(p^6)` the allowed sources are therefore:

1. tree six-derivative local operators;
2. one loop with one four-derivative insertion;
3. two-loop Einstein-Hilbert graphs.

The tree local terms are real and analytic away from isolated poles, hence contribute zero to the frozen off-pole absorptive observable.

## One-scale massless shape envelope

The frozen timelike block has one invariant `s=omega^2`. For a massless renormalized two-point function at this order, the conservative nonanalytic dependence is polynomial in the retarded logarithm through degree two:

`log_R(-s/mu^2)` and `log_R^2(-s/mu^2)`.

Power counting gives a six-derivative self-energy proportional to `s^3` times those logarithms. The physical linear response contains two EH propagators, so its correction scales as

`delta chi1R ~ s [a log_R(-s/mu^2) + b log_R^2(-s/mu^2)]`.

Taking the frequency-odd imaginary part yields the shape family

`A_odd^(p6)(s) in span { s, s log(s/mu^2) }`.

Changing `mu` only mixes these two directions. With `x=s/s_max`, the NLO shape envelope is therefore

`span { x, x log x }`.

This is a conservative envelope. It is not a claim that both coefficients are nonzero in every gauge, field content, or renormalization scheme.

## Combined profile

Iteration 167 already profiles the leading `O(p^4)` constant massless-loop shape. Iteration 169 therefore profiles

`B_NLO = [1, x, x log x]`.

On the eight frozen rows:

- rank = `3`;
- singular values = `[3.3352971464, 0.7871654345, 0.1823010356]`;
- `s_min/s_max = 0.0546581092`;
- condition number = `18.2955469`.

The orthogonal remainder has dimension

`8 - 3 = 5`.

The maximum profile-orthogonality error is `1.67e-16`.

## Higher-order capacity check

To verify that the NLO profile has not trivially erased all frequency dependence, project the target-independent NNLO-style test family

`[x^2, x^2 log x, x^2 log^2 x]`.

Its projected rank remains `3/3`.

Thus five open shape dimensions remain after the known leading and conservative NLO C5 envelopes are removed.

## Retained results

### C5-NG-006 — NEXT_ORDER_P6_MASSLESS_TT_ABSORPTIVE_ENVELOPE_IS_SPAN_X_XLOGX

At the frozen one-scale timelike conserved-TT linear-response protocol, the conservative next-order `O(p^6)` massless gravitational EFT absorptive shape is contained in `span{x,x log x}` after the leading constant `O(p^4)` shape.

### ABS-SHAPE-004 — PROFILING_CONSTANT_X_XLOGX_LEAVES_FIVE_TIMELIKE_SHAPE_DIMENSIONS

The eight-row protocol retains five independent frequency-shape dimensions after profiling the leading and NLO massless C5 envelopes.

### NG-FUNNEL-029 — ORDER_BY_ORDER_LOOP_SHAPE_ENVELOPES_MUST_BE_PROFILED_BEFORE_CANDIDATE_RESIDUAL

A sub-leading absorptive shape cannot be promoted merely because it survives the leading one-loop log. The authorized next EFT order must be profiled first.

## Current blockers

The five-dimensional remainder is **not** yet a Candidate Gravity residual.

Still BLOCKED, never zero-filled:

- finite-frequency `AS-LOR-SPEC-002` numerical spectral column;
- massive/hidden thresholds capable of entering the timelike window;
- diffusion/MSR-loop C3 absorptive response;
- C4 loop/helicity threshold completion;
- full nonlocal Lorentzian CTP loops;
- higher than `O(p^6)` C5 shapes.

A search for public source/data for the 2026 Lorentzian AS spectral computation found the published equations, numerical integration methods and tolerances, but no public production code or precision spectral table. Visual digitization of the published figure is explicitly rejected as an authoritative comparator column.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

The NLO C5 uncertainty is now structured and profiled, but comparator foundation remains `24/25` because finite-frequency AS and threshold/loop comparator completion are still open. Robust unique residual remains `0/20`.

No `ANSATZ-003`. No Fisher. No resource optimization.
