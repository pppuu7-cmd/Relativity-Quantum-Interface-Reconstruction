# RQIR Iteration 032 — D2 Native Covariance Completion

**Date:** 2026-08-29  
**Scope:** corrected hard-constrained Toy009/Iteration-011 D2 inference layer.  
**Status:** calibration-observable consistency/resource result; no new-physics claim.

## 1. Why this iteration was necessary

Iteration 026 introduced a `native-replace` D2 branch in which the 14 potential-mean rows were replaced by force-gradient mean rows. However, its eight covariance/noise rows remained the old potential-operator rows.

Iterations 030–031 subsequently established a stricter physical rule: a detector-native D2 calibration must transform the *actual measured observable family* consistently. In particular, a force detector does not directly provide an undeclared absolute-potential observable.

Therefore the Iteration-026 `native-replace` branch is mathematically valid as a **hybrid force-mean / potential-covariance protocol**, but it must not be treated as a fully force-native D2 benchmark.

This iteration rebuilds the covariance rows from the force operator itself and then checks a fully complementary relational-potential + force calibration.

## 2. Common corrected Fisher basis

All calculations use the same source and detector baseline as Iterations 015, 026 and 031:

- exact trace+energy elimination;
- 23-dimensional allowed source tangent space;
- fixed Toy009 hidden source direction;
- 22 orthogonal source nuisances;
- corrected D2 two-band detector response;
- `gamma_mean = 2.414e6`;
- `gamma_cov = 0.929e6`;
- detector-only `F_beta = 1` normalization.

The eight force-covariance rows use the exact same time/probe pattern as the old covariance bundle, but with the force-gradient operators `G(y)` in place of the potential operators.

## 3. Fully force-native replacement

The fully native branch is now

`14 force means + 8 force covariances`.

On the 23-dimensional hard-constrained source space its rank is still

`22/23`.

So converting the covariance family consistently does **not** remove the exact source null.

The new exact-null diagnostics are

- overlap with the old Toy009 hidden direction: `~0.95003346`;
- alignment of the null detector response with the beta signal: `~0.99003961`.

At the current corrected calibration scale and with no independent preparation prior,

`F_beta|theta ~= 0.0194450`.

This is lower than the old hybrid `native-replace` value `~0.03892` from Iteration 026. Therefore the old value was partly a consequence of retaining covariance information from a different observable family.

However, the resource frontier changes nontrivially rather than simply worsening:

- at `lambda=1`, 90% retention requires `C_a* ~= 8.29464`;
- with very strong preparation metrology, the minimum calibration multiplier falls to `lambda ~= 0.1537665`.

For comparison, the old hybrid force-mean/potential-covariance branch had approximately `C_a* ~= 12.97` at `lambda=1` and strong-preparation threshold `lambda ~= 0.353`.

Thus a smaller `F_beta(C_a=0)` does not imply a uniformly worse resource frontier. The relevant nuisance orientation changes when the covariance observable family changes.

## 4. New consistency rule

### RQIR-CAL-011 — mean/covariance observable-family consistency

When a detector-native calibration observable is changed, its covariance/noise calibration cannot be silently inherited from a different operator family. Mean and covariance observables must be derived from the same declared physical readout, or the protocol must be explicitly labeled hybrid.

Consequently, Iterations 026–029 remain correct for the *declared mixed protocol* they mathematically implement, but their `native-replace` phase-diagram region is not yet the fully force-native D2 phase diagram.

## 5. Relational-potential + force complementary calibration

Iteration 031 supplies finite-reference relational-potential means and covariances. Add the 14 direct force means.

With only the relational covariance bundle, the complementary branch is already full rank `23/23`, but at `y_ref=-4` its current-scale no-preparation Fisher is only

`F_beta|theta ~= 0.819539`.

Now also include the eight force-covariance rows. The combined branch is

`14 relational-potential means + 14 force means + 8 relational covariances + 8 force covariances`.

It remains full rank `23/23`, and at the current calibration scale gives:

| `y_ref` | `F_beta|theta`, `C_a=0`, `lambda=1` | `C_a*` for 90% at `lambda=1` | `lambda` for 90% with `C_a=0` |
|---:|---:|---:|---:|
| -4 | `0.8994327` | `0.06708` | `1.00632` |
| -5 | `0.8979191` | `0.24414` | `1.02321` |
| -7.5 | `0.8958650` | `0.48368` | `1.04624` |
| -10 | `0.8945406` | `0.63797` | `1.06115` |
| -20 | `0.8908886` | `1.04773` | `1.10249` |
| -100 | `0.8834706` | `1.78809` | `1.18752` |
| -1000 | `0.8804627` | `2.05486` | `1.22241` |

The finite reference therefore does not merely add a mean-calibration cost. When its covariance information is combined with detector-native force covariance, the nuisance geometry becomes much better constrained.

This does **not** yet establish a cheaper experiment: the combined branch has sixteen covariance rows rather than eight, and their physical Fisher rates have not yet been assigned.

## 6. Covariance-row value audit

At `y_ref=-4`, starting from relational-potential means + force means + the eight relational covariance rows, the baseline is

`F_beta|theta ~= 0.819539`, `C_a* ~= 5.82122`.

Adding the best force-covariance rows one at a time gives strong diminishing returns. The best subsets are:

| added force-cov rows | best indices | `F_beta|theta` | `C_a*` for 90% |
|---:|---|---:|---:|
| 0 | `()` | `0.819539` | `5.82122` |
| 1 | `(0)` | `0.848981` | `4.41774` |
| 2 | `(0,1)` | `0.867019` | `2.91031` |
| 3 | `(0,1,3)` | `0.884004` | `1.62375` |
| 4 | `(0,1,3,7)` | `0.894857` | `0.58896` |
| 8 | all | `0.899433` | `0.06708` |

The four-row subset `(0,1,3,7)` captures most of the nuisance-suppression gain. With no source prior it reaches 90% at only `lambda ~= 1.05755` if all retained row weights are scaled together.

The row indices correspond to the stored covariance pattern:

- `0`: probe-0 self covariance at the target time;
- `1`: probe-0/probe-1 cross covariance at `TIMES[1]`;
- `3`: probe-1/probe-0 cross covariance at the target time;
- `7`: probe-0/probe-1 cross covariance at `TIMES[6]`.

This is a local Toy009 row-selection result, not a universal optimal design.

## 7. New design result

### RQIR-CAL-012 — covariance complementarity can dominate nuisance closure

In the current finite Toy009 D2 model, a small targeted set of detector-native force-covariance observables removes most of the remaining profiled nuisance penalty after relational-potential + force mean calibration.

This means covariance/noise calibration is not merely a secondary precision layer. Its **orientation in nuisance space** can be as important as adding more mean rows.

The correct future resource objective must therefore optimize which covariance observables are measured, not assume a fixed eight-row covariance bundle.

## 8. What is corrected and what is retained

Retained:

- RQIR-NG-005 for the original NP3 exact-null branch;
- RQIR-NG-010: force-mean replacement can rotate rather than remove the exact null;
- RQIR-CAL-009: complementary observables can close the finite hard-constrained tangent space;
- RQIR-NG-011/012: finite-reference relational calibration has its own null/resource tradeoffs.

Corrected interpretation:

- Iteration-026 `native-replace` is a mixed force-mean/potential-covariance protocol, not a fully force-native one;
- the old Iteration-028 phase diagram should not yet be interpreted as the final physical D2 branch map until covariance families receive consistent native rates.

No previous numerical result is deleted; its protocol label is narrowed.

## 9. Reproducibility

Code:

`analysis/d2_native_covariance_completion_iteration032.py`

Regression guards check the fully force-native rank/null geometry, `F_beta`, `C_a*`, strong-preparation threshold, the relational+force full-covariance result at `y_ref=-4`, and the best four-row covariance subset.

## 10. Next gate

Attach physical Fisher rates to the **force-covariance** and **relational-covariance** rows using one common D2 force-PSD/bandwidth/duty model. Then optimize over

`(y_ref, lambda, C_a, covariance-row subset)`

and compare against the fully force-native replacement branch on equal wall-clock footing.

Only after this covariance-rate closure should the D2 resource phase diagram be promoted to an SI-time apparatus comparison.
