# Candidate Gravity Article Scaffold — Funnel / Negative-Result Matrix

**Iteration:** 153  
**Status:** working article table; scoped claims only.

`FAIL` = frozen scientific/model failure. `BLOCKED` = missing comparator/observable implementation. `PASS_SCOPED` = only the explicitly tested subspace. `REGIME_NONIDENTIFIABLE` = a finite protocol collapses independent parameters without implying inconsistency.

| Construction | Furthest established point | Limiting result | Article-safe interpretation |
|---|---|---|---|
| C3 postquantum classical gravity, linear stochastic block | fixed `(D2,D0)` dynamics; supported `(N2,chi1R)` tangent | rank `1/2`; only `5D2+D0` visible | `C3-NG-001`: REGIME_NONIDENTIFIABLE, not FAIL |
| C3 unsupported post-Gaussian rows | `C3sym/chi2R/soft2/tensor/threshold` not yet derived | `NG-FUNNEL-011` | BLOCKED rows are not zero rows |
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

## New retained rules/results
- `C3-NG-001`: one scalar `N2` coordinate collapses the two linear stochastic diffusion directions `(D2,D0)` to `5D2+D0`.
- `NG-FUNNEL-011`: partial comparator rows that are not derived are BLOCKED and must never be zero-filled into a quotient matrix.

## Current funnel
The first concrete C3 block now exists, but only on the supported linear stochastic rows. Full C3 quotient closure is still unavailable because nonlinear ordered/cumulant coordinates are not derived. Existing local C5 `6x2` remains Ward-validated; higher local and loop/nonanalytic C5 remain BLOCKED. Nonlinear C4 remains open. Fisher/resources and `ANSATZ-003` promotion remain inadmissible.
