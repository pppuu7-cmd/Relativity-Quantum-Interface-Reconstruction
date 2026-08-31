# Candidate Gravity Article Scaffold — Funnel / Negative-Result Matrix

**Iteration:** 155  
**Status:** working article table; scoped claims only.

`FAIL` = frozen scientific/model failure. `BLOCKED` = missing comparator/observable implementation. `PASS_SCOPED` = only the explicitly tested subspace. `REGIME_NONIDENTIFIABLE` = finite protocol degeneracy without inconsistency.

| Construction | Furthest established point | Limiting / new result | Article-safe interpretation |
|---|---|---|---|
| C3 PQCG linear stochastic block | fixed `(D2,D0)`; scalar `N2` | rank `1/2`, only `5D2+D0` visible | `C3-NG-001`: REGIME_NONIDENTIFIABLE |
| C3 PQCG nonlinear symmetric block | same covariant OM action; `(N2,C3sym_TT)` | rank `2/2` for every `D2>0` | `C3-NG-002`: classical non-Gaussian cumulant lifts scoped diffusion degeneracy |
| symmetric gravitational non-Gaussianity as quantum witness | fixed classical stochastic comparator has nonzero bispectrum | `NG-FUNNEL-012` | `C3sym != 0` is not a quantum-spacetime certificate |
| C3 PQCG tree causal nonlinear response | same nonlinear Einstein drift; six-probe `chi2R` fingerprint nonzero | response independent of `(D2,D0)` after hard GR normalization; adds rank 0 | `C3-NG-003`: common GR-boundary response |
| nonzero nonlinear causal response as quantum witness | fixed classical stochastic spacetime has nonzero tree response | `NG-FUNNEL-013` | `chi2R != 0` alone is not a quantum-spacetime certificate |
| C3 diffusion-dependent/order-sensitive response | stochastic/MSR-loop correction and exact odd selector not derived | implementation/specification open | BLOCKED, never zero-filled |
| C4 Gaussian KL spin-2 | exact Gaussian direct-integral/tower identity | `CG-NG-006` | valid Gaussian comparator; no novelty |
| C5 perturbative GR EFT on-shell | 12x10 local tangent rank 10/10 | on-shell only | `NG-FUNNEL-006` |
| C5 explicit local nonlinear response | EH + two curvature-cubic columns | local `6x2`, rank `2/2`, Ward validated | PASS_SCOPED |
| C5 higher local / loop nonanalytic | not implemented in same off-shell response basis | missing columns | BLOCKED, not zero |
| nonlinear C4 / massive spin-2 | not yet frozen | finite interacting realization missing | next comparator target |
| nonlocal / asymptotic-safety | program-level classes known | no frozen finite tangent | BLOCKED; program labels are not finite comparators |

## New Iteration-155 result

The same PQCG realization that generated the classical symmetric bispectrum also has the tree causal response

`chi2R = -G_R Gamma3_EH G_R G_R`.

Its frozen six-probe values are

`[0.30003001285313774,-1.461790494216445,-12.034873790942026,-14.434681522564402,4.867521776975717,-2.7789127642722273]`.

Thus a classical stochastic metric can have a nonzero nonlinear causal response.

With the Newton/GR coupling treated as a hard common calibration, however,

`d chi2R_tree / d(D2,D0)=0`.

The result therefore contributes no additional diffusion tangent direction, even though the physical response itself is nonzero.

## Retained rules/results through Iteration 155

- `C3-NG-001`: one `N2` coordinate collapses `(D2,D0)` to `5D2+D0`.
- `C3-NG-002`: same-dynamics `C3sym_TT` lifts the supported comparator rank to `2/2`.
- `C3-NG-003`: tree ordered response is a common GR-boundary response and adds zero `(D2,D0)` rank.
- `NG-FUNNEL-011`: unsupported comparator rows are BLOCKED, not zeros.
- `NG-FUNNEL-012`: classical covariant stochastic gravity generates gravitational post-Gaussian rank.
- `NG-FUNNEL-013`: nonzero causal nonlinear gravitational response alone is not a quantum-metric certificate.

## Current article implication

The candidate paper can now make a stronger funnel statement than merely saying classical models can have noise. One concrete classical-spacetime comparator reproduces, from one dynamics:

1. Gaussian metric noise;
2. a nonzero symmetric gravitational third cumulant;
3. a nonzero nonlinear causal Einstein response.

Therefore a promotable candidate must rely on the **linked residual ordered structure after common-GR and stochastic-comparator subtraction**, not on any one of those features in isolation.

The diffusion-dependent/order-sensitive C3 response remains BLOCKED. The next finite comparator target is nonlinear C4.
