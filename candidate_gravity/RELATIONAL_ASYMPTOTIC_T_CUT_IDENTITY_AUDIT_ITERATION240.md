# Relational / asymptotic pure-gravity `T_cut` identity audit — Iteration 240

Date: 2026-09-01

MODEL_READINESS: 24%

## Scope

Start from authoritative Iteration 239 and test only the frozen next gate: whether a **gauge-safe relational or asymptotic pure-gravity observable** supplies an identity-preserving realization of

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`,

with both `Gamma3_ret[h,h,h]` and `K2[h,h]` derived from one parent dynamics, one parameter convention, one source/Ward/contact completion and one hard-channel discontinuity prescription.

No matter proxy, no observable redefinition, no `ANSATZ-003`, no Fisher/resources.

## Authority audited

### A. Relational / quantum-reference-frame effective actions

Aguilar-Gutierrez, Ferrero, Hoehn and Marchetti, *Relational path integral, effective actions and quantum frame covariance*, arXiv:2607.21463 (2026), construct a manifestly gauge-invariant path integral using frame-dressed relational observables. Their gauge-invariant effective actions are obtained by coupling sources to the **relational observables themselves**; locality is defined relative to a quantum reference frame, and different frame choices are related by quantum-frame transformations. The construction is equivalent to suitable Faddeev-Popov formulations when the chosen quantum reference frame is gauge-fixed.

This is strong authority that gauge-safe effective actions exist. However, its source variables are not the bare metric components `h_{mu nu}` used in frozen `Gamma3_ret` and `K2`. The relational field is schematically

`h_R(x) = h(X_R^{-1}(x)) + dressing/frame terms`,

so functional differentiation generates frame/dressing contributions already beyond linear order. Choosing a frame in which `h_R` numerically coincides with a particular gauge-fixed metric is a **frame/gauge choice**, not an observable-independent identity between relational derivatives and the frozen bare-metric/source-completed derivatives.

Therefore the relational effective action supplies a different, physically legitimate coordinate on theory space unless an explicit same-parent Jacobian/source-reduction identity is derived through cubic order, including retarded ordering, contact terms and hard-channel analytic continuation. No such executable identity was found in the audited authority.

### B. Nonlinear relational metric observables

Fröb and Lima, arXiv:2303.16218, explicitly construct nonlinear gauge-invariant metric observables by evaluating the metric in field-dependent synchronous coordinates. The dynamical coordinates are nonlocal functionals of the metric, and explicit gauge-invariant perturbations differ from the bare metric by coordinate-functional terms. They compute a gauge-invariant two-point function for the relational metric, but this does not provide the required one-loop causal cubic `h^3/h^2` linked discontinuity.

This independently confirms the structural point: gauge safety is achieved by changing the field variable to a dressed/relational one. At nonlinear order, functional valence in the elementary metric does not remain trivially identical under that change of variables.

### C. Asymptotic/null-infinity observables

Kozameh and Depaola, arXiv:2605.06961 and arXiv:2605.06001 (2026), formulate perturbative quantum gravity directly at null infinity in terms of Bondi shear/radiative data. The construction explicitly avoids bulk fields and off-shell propagators; intermediate gravitons are on shell and the natural observables are spectral-angular/Bondi data.

This is a gauge-safe pure-gravity observable framework, but precisely for that reason it is **not** the frozen bulk/source-completed `Gamma3_ret[h,h,h]` linked to an off-shell inverse kernel `K2[h,h]`. Its analytic structure is boundary/on-shell rather than the finite hard-channel bulk 1PI discontinuity used by frozen `D_s`.

Recent null-boundary work likewise emphasizes reduced null gravitational data and nonlocal boundary brackets rather than a same-parent bulk `h^3/h^2` 1PI pair. It therefore cannot be substituted without redefining the comparator coordinate.

## Identity test

For an admissible replacement `O` we require, through the order relevant to `T_cut`, an exact same-parent map

`delta^3 Gamma_rel / delta O^3  <->  Gamma3_ret[h,h,h]`

and

`delta^2 Gamma_rel / delta O^2  <->  K2[h,h]`,

with a single fixed Jacobian/dressing, one retarded prescription, one source/contact/Ward completion and the **same** hard-channel `Disc_s`.

The audited relational constructions fail this identity requirement because nonlinear field-dependent coordinates/dressings introduce extra Jacobian and contact terms that are frame dependent. The audited asymptotic constructions fail it because they replace bulk/off-shell source variables with boundary/on-shell radiative data and thus change analytic structure.

Gauge invariance / physicality is therefore not enough to populate the frozen comparator coordinate.

## Scientific conclusion

No currently published relational or asymptotic pure-gravity construction audited here provides an **identity-preserving executable map** back to the frozen native bulk metric coordinate `T_cut`.

Freeze the target status itself as

`OPERATIONALLY_NONEXECUTABLE_WITH_CURRENT_PUBLISHED_AUTHORITY`

with mandatory qualifier

`BLOCKED_NOT_ZERO`.

Retain the more specific parent blocker

`BLOCKED_T_CUT_NATIVE_H3_EXECUTABILITY_AT_GAUGE_SAFE_CUBIC_EFFECTIVE_ACTION_BOUNDARY`.

The reason is now stronger than Iteration 239: the two known routes to gauge safety split cleanly into

1. **relational/dressed bulk variables**, which require a nontrivial frame-dependent nonlinear source/Jacobian map before they could be identified with bare-metric `h^3/h^2`; and
2. **asymptotic/on-shell variables**, whose functional variables and analytic structure are not the frozen bulk 1PI coordinate.

Neither is an identity-preserving completion of `T_cut` under current published authority.

## New scoped labels

- `REL-NG-020 — RELATIONAL_GAUGE_SAFETY_CHANGES_NONLINEAR_SOURCE_VARIABLES_AND_REQUIRES_FRAME_DEPENDENT_JACOBIAN_COMPLETION`;
- `REL-CUT-020 — ASYMPTOTIC_NULL_INFINITY_GRAVITY_IS_PHYSICAL_BUT_USES_BOUNDARY_ONSHELL_ANALYTIC_STRUCTURE_NOT_FROZEN_BULK_T_CUT`;
- `REL-BLOCK-005 — OPERATIONALLY_NONEXECUTABLE_WITH_CURRENT_PUBLISHED_AUTHORITY`;
- `NG-FUNNEL-096 — GAUGE_SAFE_ROUTES_DO_NOT_YIELD_AN_IDENTITY_PRESERVING_H3_H2_LINKED_COORDINATE_WITHOUT_NEW_MODEL_CONVENTION`.

## Classification

This is an **operational BLOCKED / current-authority result**. It is not:
- a consistency FAIL of GR or quantum gravity;
- exact comparator identity;
- regime-specific non-identifiability;
- near-degeneracy;
- proof that `T_cut = 0`;
- Candidate Gravity novelty.

The negative result is scientifically useful because it closes the final audited shortcut without weakening or redefining the frozen observable.

## Candidate-state consequence

No robust Candidate Gravity residual exists. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No heavy computation is justified while the comparator coordinate is operationally unavailable.

MODEL_READINESS: 24%

Change from Iteration 239: 0 percentage points. Comparator foundation remains `24/25`; robust unique residual remains `0/20`. The status of the last linked-nonanalytic route is now frozen more sharply, but no readiness rubric component closes.

## Exact next gate

Iteration 241 should **not search for another proxy observable**. Audit the Candidate Gravity funnel itself under the newly frozen executability boundary and ask whether there exists any previously retained residual target that is both (i) algebraically nonzero before profiling and (ii) computable under already frozen comparator authority. If none exists, freeze the present Candidate Gravity program state as `NO_EXECUTABLE_RESIDUAL_TARGET_UNDER_CURRENT_COMPARATOR_AUTHORITY` and move the scientific effort to a clearly separated authority-improvement program (e.g. deriving the missing gauge-safe cubic unique action) rather than pretending a residual exists. Do not create `ANSATZ-003`; do not run Fisher/resources.