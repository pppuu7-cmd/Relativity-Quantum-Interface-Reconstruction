# RQIR Iteration 052 — QND Ramsey-Ancilla Fisher-Rate Budget

**Date:** 2026-08-29  
**Scope:** independent Toy009 source metrology after Iterations 049–051.  
**Status:** physical rate conversion for a controlled-phase ancilla proxy; no hardware forecast and no new-physics claim.

## 1. Why Iteration 051 is not yet a resource optimum

Iteration 051 optimized Fisher **per accepted Ramsey shot**.  For ideal visibility the best per-copy point is near

`phi ~= 2.41867`, `F_alpha ~= 0.00389041`,

about 41.4% of the projective energy-population Fisher.

But if the controlled phase is accumulated dynamically, larger phase takes longer.  The experimental objective is therefore Fisher per unit wall time, not Fisher per copy.

## 2. Controlled-phase rate model

Let the QND source-energy/ancilla interaction accumulate phase at rate

`phi = Omega_E T`.

For accepted-copy probability `p_E` and negligible reset overhead,

`R_E^(alpha)(phi) = p_E Omega_E F_alpha(phi)/phi`.

Thus the apparatus-independent dimensionless rate coefficient is

`c_R = max_phi F_alpha(phi)/phi`.

The same source populations and optimized equatorial ancilla quadrature as Iteration 051 are retained.  No new source geometry is introduced.

## 3. Rate-optimal Ramsey point

The numerical optimum is

`boxed: phi_rate ~= 1.092306912`,

with

`boxed: F_alpha(phi_rate) ~= 0.002756370099`.

This is about

`boxed: 29.35%`

of the ideal projective energy-population Fisher per accepted copy.

The maximum throughput coefficient is

`boxed: c_R ~= 0.002523439217`,

so

`boxed: R_E,max^(alpha) = 0.002523439217 p_E Omega_E`.

### RQIR-RESOURCE-024 — Ramsey per-copy optimum is not the rate optimum

> When source metrology is implemented by a finite controlled phase, maximizing Fisher per accepted copy over-rotates the ancilla from the wall-clock viewpoint.  The correct design objective is `F_alpha(phi)/T`, which shifts the optimum from `phi~2.42` to `phi~1.09` in the current Toy009 source.

This is the Ramsey analogue of the pointer-strength/reset tradeoff of RESOURCE-023.

## 4. Direct conversion to the current D2 branch thresholds

Iteration 050 expressed the D2 source-amplitude branch boundaries directly in source-metrology Fisher rate:

- Branch0 beats best4 for `R_E > 2.13404e-4 s^-1`;
- best4 beats best5 for `R_E > 2.93122e-6 s^-1`.

For the ideal-visibility Ramsey rate above, the corresponding controlled-phase-rate thresholds are

`Omega_04 = 2.13404e-4 / (p_E c_R)`,

`Omega_45 = 2.93122e-6 / (p_E c_R)`.

For the transparent `p_E=0.5` benchmark:

- `boxed: Omega_04 ~= 0.16914 s^-1`;
- `boxed: Omega_45 ~= 2.323e-3 s^-1`.

At the Branch0/best4 boundary the rate-optimal interaction time is

`T_int = phi_rate/Omega_04 ~= 6.46 s`.

Therefore, **ignoring reset and visibility loss**, a QND Ramsey source-metrology implementation with accepted-copy probability one half only needs a controlled source-energy phase accumulation rate of order `0.17 rad s^-1` in the present dimensionless energy coordinate for Branch0 to beat best4 on source-amplitude closure.

This is now a concrete apparatus target rather than an abstract `C_alpha` or `gamma`.

## 5. Relation to the finite Gaussian pointer

The zero-reset Gaussian energy pointer of Iteration 049 gave

`R_E = 0.00827010 p_E eta_E kappa_E`.

The Ramsey coefficient cannot be compared numerically to `kappa_E` without specifying the physical Hamiltonian that maps `Omega_E` and `kappa_E` to the same hardware coupling/noise normalization.  The useful result is instead that **both candidate source-metrology protocols now expose one measurable rate parameter**:

- pointer: `eta_E kappa_E` plus reset;
- Ramsey ancilla: controlled phase rate `Omega_E`, visibility and reset.

A physical source realization can therefore be scored against the same Fisher-rate boundaries without reopening the Toy009/Toy010 nuisance geometry.

## 6. Important consistency point

The Ramsey interaction is QND with respect to the isolated Toy009 source Hamiltonian only if the interaction has the form of a controlled function of `H` (or an experimentally equivalent commuting observable).  As established by NG-023, this does **not** authorize strong Ramsey readout on the science copy: the current use remains independent/sacrificial source metrology.

The apparatus Hamiltonian must also pass conservation/Bianchi and stress-energy accounting before any gravitational interpretation.

## 7. Reproducibility

Code:

`analysis/qnd_ramsey_rate_budget_iteration052.py`

Regression values:

- `phi_rate = 1.092306912`;
- `F_alpha = 0.002756370099`;
- `F_alpha/F_projective = 0.293484246`;
- `c_R = 0.002523439217`;
- at `p_E=.5`, `Omega_04 = 0.16913742 s^-1`, `Omega_45 = 0.002323194 s^-1`, `T_int,04 = 6.4581 s`.

## 8. Next gate

Add source reset/preparation time and finite Ramsey visibility to the rate objective,

`R_E = p_E F_alpha(phi,V)/(t_reset + phi/Omega_E)`,

then solve the Branch0/best4 boundary in the physical coordinates `(Omega_E, V, p_E, t_reset)`.  This is the shortest path from Toy010/RQIR-NG-005 to a source-realization requirement.
