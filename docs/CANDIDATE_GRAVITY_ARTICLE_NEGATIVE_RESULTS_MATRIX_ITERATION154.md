# Candidate Gravity Article Scaffold — Funnel / Negative-Result Matrix

**Iteration:** 154  
**Status:** working article table; scoped claims only.

`FAIL` = frozen scientific/model failure. `BLOCKED` = missing comparator/observable implementation. `PASS_SCOPED` = only the explicitly tested subspace. `REGIME_NONIDENTIFIABLE` = a finite protocol collapses independent parameters without implying inconsistency.

| Construction | Furthest established point | Limiting / new result | Article-safe interpretation |
|---|---|---|---|
| C3 postquantum classical gravity, linear stochastic block | fixed `(D2,D0)` dynamics; one scalar `N2` noise coordinate | rank `1/2`; only `5D2+D0` visible | `C3-NG-001`: REGIME_NONIDENTIFIABLE, not FAIL |
| C3 postquantum classical gravity, nonlinear OM extension | same published covariant action; supported `(N2,C3sym_TT)` rows | `C3sym_TT=B D2^2`; tangent rank `2/2` for every `D2>0` | `C3-NG-002`: nonlinear symmetric cumulant lifts the linear diffusion degeneracy |
| symmetric gravitational non-Gaussianity as quantum witness | concrete classical PQCG comparator generates a nonzero TT bispectrum | `NG-FUNNEL-012` | nonzero `C3sym` and increased rank are not sufficient evidence for quantum spacetime |
| C3 ordered nonlinear rows | `chi2R_even/odd` not yet derived from the same stochastic realization | completion open | BLOCKED, never zero-filled |
| C4 Gaussian KL spin-2 | exact Gaussian direct-integral/tower identity | `CG-NG-006` | valid Gaussian comparator; no novelty |
| C5 perturbative GR EFT on-shell | 12x10 local tangent rank 10/10 | `NG-FUNNEL-006` | valid on-shell reference only |
| C5 source-completed finite probe layer | physical metric/source + six off-shell TT probes | `NG-FUNNEL-009` | probe PASS is not vertex PASS |
| C5 explicit local tree nonlinear response | EH TT baseline + two curvature-cubic columns | local `6x2` tangent rank `2/2`, `smin/smax=0.2294` | PASS_SCOPED_WARD_VALIDATED |
| naive off-shell longitudinal-null test | isolated EH 3-vertex nonzero | `NG-FUNNEL-010` | invalid gate, not a GR FAIL |
| source-completed EH Ward identity | action-level completed identity on six probes | worst relative residual `2.724e-6`, quadratic convergence | PASS_SCOPED |
| curvature-cubic Ward validation | all six probes/all three gauge-leg replacements | residuals at machine precision | PASS_SCOPED |
| C5 higher local directions | not implemented in off-shell response basis | missing explicit columns | BLOCKED, not zero |
| C5 loop/nonanalytic sector | causal need recognized | no finite implemented columns | BLOCKED, not zero |
| nonlinear C4 / massive spin-2 | not yet fixed | finite interacting realization missing | BLOCKED |
| nonlocal / asymptotic-safety comparators | program-level candidates known | no frozen finite tangent | BLOCKED; program labels are not comparators |

## New Iteration-154 quantitative C3 result

The published pure-gravity PQCG probability action

`S[g]=1/2 int sqrt(-g)[alpha R_mn R^mn-beta R^2]`

maps to the frozen diffusion convention through

`D2=1/(2alpha)`, `D0=1/[8(alpha-3beta)]`.

On the six TT probes the `R^2` cubic coefficient vanishes, while the Ricci-squared cubic coefficient generates

`C3sym_TT=B D2^2`, `B=-617.4340282011477`.

Together with

`N2=A(5D2+D0)`, `A=258.83104475297773`,

the supported tangent is

`[[5A,A],[2BD2,0]]`

with determinant `-2ABD2`, hence rank `2/2` for every `D2>0`.

## Retained rules/results

- `C3-NG-001`: one scalar `N2` coordinate collapses the two linear stochastic diffusion directions `(D2,D0)` to `5D2+D0`.
- `C3-NG-002`: a nonlinear symmetric cumulant derived from the same stochastic action lifts that scoped degeneracy.
- `NG-FUNNEL-011`: partial comparator rows that are not derived are BLOCKED and must never be zero-filled into a quotient matrix.
- `NG-FUNNEL-012`: a concrete classical covariant Onsager–Machlup gravity model generates nonzero gravitational post-Gaussian rank; symmetric non-Gaussianity is therefore not a quantum-spacetime certificate.

## Current funnel

C3 has advanced from a one-dimensional linear noise tangent to a two-dimensional supported `(N2,C3sym_TT)` tangent without adding phenomenological freedom. This makes C3 a stronger comparator against any future model whose claimed novelty is based on a gravitational bispectrum.

However the ordered `chi2R` sector of the same C3 realization remains BLOCKED, as do nonlinear C4, nonlocal/AS finite tangents, C5 higher local directions and C5 loop/nonanalytic directions.

Therefore full comparator quotient closure is still unavailable. Fisher/resources and `ANSATZ-003` promotion remain inadmissible.
