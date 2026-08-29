# RQIR Iteration 049 — Finite-Strength QND Energy-Pointer Metrology

**Date:** 2026-08-29  
**Scope:** Toy009 independent source-metrology channel after Iterations 047–048.  
**Status:** finite-resolution QND metrology/resource result; no hardware forecast and no new-physics claim.

## 1. Why this gate is needed

Iteration 047 showed that an ideal projective measurement of Toy009 energy populations carries finite hidden-amplitude Fisher,

`F_E^(alpha) ~= 0.0093918844`

per accepted plus-branch copy.

Iteration 048 then compared D2 branches by treating one energy-population cycle as an ideal projective measurement. A real QND energy detector has finite resolution. The energy levels therefore produce overlapping detector distributions and one cycle carries only a fraction of the projective Fisher.

This iteration replaces the idealized projective readout by a continuous finite-strength Gaussian pointer.

## 2. QND Gaussian-pointer model

For energy level `E_i in (1,2,3,4,6)`, one accepted detector record is summarized by

`y | i ~ Normal(r E_i, 1)`.

The hidden state populations are

`p_i(alpha)=1/5 + EPS alpha d_i`,

where `EPS=0.08` and `d_i=(Delta0)_ii`.

The dimensionless parameter `r` is the separation of adjacent unit-spaced energy levels in detector-noise standard deviations.

For a standard QND diffusive monitor of energy,

`r = 2 sqrt(eta_E kappa_E T_E)`,

where `kappa_E` is the measurement rate, `eta_E` the information efficiency and `T_E` the interrogation time.

The outcome Fisher is evaluated from the full Gaussian mixture,

`F_alpha(r)=int dy [partial_alpha p(y|alpha)]^2 / p(y|alpha)`.

As `r -> infinity`, it approaches the projective energy-population Fisher.

## 3. Exact-moment suppression at weak readout

The Toy009 hidden direction obeys both

`sum_i d_i = 0`

and

`sum_i E_i d_i = 0`.

The first relation is trace equality. The second is the exact equal-energy constraint already built into Toy009.

Therefore an arbitrarily weak linear energy pointer cannot see the hidden amplitude through either total probability or mean pointer shift. Its leading sensitivity comes from the energy-variance channel.

For small `r`,

`F_alpha(r) = 1/2 [EPS sum_i d_i E_i^2]^2 r^4 + O(r^6)`.

Numerically,

`boxed: F_alpha(r) ~= 0.0158603616 r^4`.

### RQIR-NG-024 — conserved-moment weak-readout suppression

> If a hidden source direction is exactly matched in normalization and mean energy, a weak linear QND energy pointer has no leading mean-shift information about that direction. In the present Toy009 channel its Fisher begins quartically in pointer separation, `F~r^4`.

This does not make energy metrology impossible; it means the metrology cannot be made arbitrarily weak while retaining a finite information rate.

## 4. Finite-strength information fractions

For the plus branch:

| adjacent-level separation `r` | `F_alpha(r)` | fraction of projective `F_E^(alpha)` |
|---:|---:|---:|
| 0.5 | `4.09369e-4` | 4.36% |
| 1 | `2.03700e-3` | 21.69% |
| 2 | `5.41101e-3` | 57.61% |
| 3 | `7.64360e-3` | 81.39% |
| 4 | `8.78343e-3` | 93.52% |
| 6 | `9.35504e-3` | 99.61% |

Thus near-projective Fisher requires several-sigma energy-level separation, but maximum Fisher **per copy** is not the same as maximum Fisher **per unit wall time**.

## 5. Throughput-optimal measurement is deliberately nonprojective

With negligible source reset/preparation overhead,

`T_E = r^2/(4 eta_E kappa_E)`.

The Fisher rate per accepted source stream is therefore

`R_E^(alpha) = 4 p_E eta_E kappa_E F_alpha(r)/r^2`.

Maximizing `F_alpha(r)/r^2` gives

`boxed: r_* ~= 0.8677465`.

At this optimum,

`F_alpha(r_*) ~= 0.0015568125`,

only

`boxed: 16.58%`

of the projective Fisher per accepted copy.

But the information rate is maximal:

`boxed: R_E,max^(alpha) ~= 0.0082700957 p_E eta_E kappa_E`.

### RQIR-RESOURCE-022 — finite-strength metrology throughput optimum

> When independent source copies can be prepared/reset cheaply, the wall-clock-optimal QND energy measurement need not resolve the energy level projectively. For Toy009, a sub-projective pointer with adjacent-level separation `r~0.87 sigma` maximizes Fisher per measurement time.

This replaces the implicit assumption in Iteration 048 that each metrology cycle should be projective.

## 6. Immediate D2 consequence

At the transparent 100-Hz D2 benchmark used in Iteration 048 (`p_C=0.5`, `1 ms` detector overhead), the best4 covariance floor is about

`T_4 ~= 5.864 h`.

Branch 0 and best4 differ in required source prior by

`Delta C_alpha ~= 4.50505`.

Therefore Branch 0 beats best4 whenever the actual independent energy-metrology Fisher rate exceeds

`boxed: R_E^(alpha) > 2.13404e-4 s^-1`.

At the zero-reset pointer optimum this becomes

`boxed: p_E eta_E kappa_E > 2.5804e-2 s^-1`.

Equivalently, the effective accepted information-measurement time scale

`1/(p_E eta_E kappa_E)`

must be shorter than about

`38.8 s`.

The best4-versus-best5 crossing is much weaker: best4 remains preferable provided

`R_E^(alpha) > 2.93e-6 s^-1`,

or at the zero-reset pointer optimum

`p_E eta_E kappa_E > 3.54e-4 s^-1`.

Thus the fifth covariance row remains difficult to justify unless independent energy metrology is extremely slow.

## 7. Important limitation

The zero-reset optimum is not yet a complete physical source protocol. A real massive-source metrology cycle also pays preparation/reset/readout overhead. If that overhead dominates, stronger and more nearly projective energy measurements may become throughput-optimal because they extract more Fisher before each reset.

That is the next resource gate.

## 8. Reproducibility

Code:

`analysis/qnd_energy_pointer_fisher_iteration049.py`

It reconstructs the Toy009 hidden populations, evaluates the full Gaussian-mixture Fisher using deterministic Gauss-Hermite quadrature, verifies the `r^4` weak-measurement law and finds the finite-strength throughput optimum.

## 9. Next gate

Add an explicit independent-source preparation/reset time `t_reset` and optimize

`R_E(r)=p_E F_alpha(r)/(r^2/(4 eta_E kappa_E)+t_reset)`.

This will determine when the optimal energy metrology should be weak, intermediate or nearly projective, and will provide a physically usable branch-selection boundary in the variables `(kappa_E, eta_E, p_E, t_reset)`.
