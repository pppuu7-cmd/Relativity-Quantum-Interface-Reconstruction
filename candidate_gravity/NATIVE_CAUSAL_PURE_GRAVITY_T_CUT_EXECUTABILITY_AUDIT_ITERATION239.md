# Native causal pure-gravity `T_cut` executability audit — Iteration 239

Date: 2026-09-01

MODEL_READINESS: 24%

## Scope

This iteration starts from authoritative Iteration 238 and tests only the frozen next gate: whether current published authority supplies an executable **native causal pure-gravity `h^3` response linked to the same-parent `h^2` metric kernel** in one convention suitable for

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`,

with `D_s F = Disc_s F/(2 pi i)`.

No matter-radiation proxy, no redefinition of `T_cut`, no `ANSATZ-003`, and no Fisher/resource calculation is permitted.

## Authority audit

### 1. Generic causal QFT technology exists

Meltzer, *Dispersion Formulas in QFTs, CFTs, and Holography*, arXiv:2103.15839, shows that momentum-space retarded correlators admit dispersion representations in terms of causal commutators. In particular a retarded three-point function has a controlled discontinuity in a selected energy variable, subject to the usual analyticity/subtraction assumptions.

Therefore the obstruction is **not** that nonlinear retarded three-point functions or their discontinuities are conceptually undefined.

### 2. Schwinger-Keldysh gravity technology exists, but the executable observables found are source/worldline responses

Jakobsen–Mogull–Plefka–Sauer, *All Things Retarded*, arXiv:2207.00569, derives purely retarded propagator rules in Schwinger-Keldysh worldline QFT for GR and computes causal radiation-reaction observables. Porto–Riva–Yang, arXiv:2409.05860, likewise uses an in-in EFT for nonlinear gravitational radiation reaction with diffeomorphism/Ward control.

These are strong causal-gravity authorities, but their directly computed observables are worldline/source quantities and radiation observables. They do not provide the native source-completed flat-space 1PI metric object `Gamma3_ret[h,h,h]` linked to the same-parent metric inverse kernel `K2[h,h]` required by frozen `T_cut`.

### 3. Euclidean-to-causal effective-equation technology does not independently close the cubic object

Barvinsky's Euclidean Schwinger-Keldysh prescription (e.g. arXiv:1112.4340; review arXiv:1408.6112) explains how nonlocal Euclidean effective actions generate causal equations for mean fields after the appropriate retarded continuation.

However, using that route for frozen `T_cut` first requires a gauge-safe, source-completed **finite cubic gravitational effective action** in one declared parent convention. The repository already established that the pure-Einstein Vilkovisky finite cubic map is blocked on the full EOM/connection insertion series (`BLOCKED_FULL_VD_EOM_INSERTION_SERIES_TO_FINITE_CPT3_MAP`). Hence Euclidean-to-retarded continuation is not an independent escape from C5; it inherits the missing cubic authority upstream.

### 4. Current BRST Schwinger-Keldysh progress is not yet a gravity specialization

Kaplanek–Mylova–Tolley, *Schwinger-Keldysh Path Integral for Gauge theories*, arXiv:2604.26941, provides a modern BRST-consistent SK construction, diagonal/retarded BRST symmetry and WT/ST identities for non-Abelian gauge theories with physical initial states.

This strengthens the general gauge-theory foundation but does **not** supply a diffeomorphism-gravity specialization with a computed one-loop nonlinear metric three-point response, shared `K2`, hard-channel discontinuity, and source/contact completion. It is therefore supporting methodology, not an executable RQIR comparator coordinate.

## Kinematic guardrail for an on-shell shortcut

The native pure-gravity three-point S-matrix is not a replacement for the required retarded off-shell/source-completed object. For three real massless external gravitons in 4D Minkowski space, momentum conservation forces the usual degenerate collinear real kinematics; nontrivial three-point amplitudes are naturally defined by complexified kinematics. Such a three-point on-shell object does not furnish the required finite-hard-channel branch cut/discontinuity of `T_cut`.

Therefore an on-shell `h+h->h` shortcut cannot simultaneously provide:
- physical real kinematics,
- the frozen hard-channel `Disc_s`, and
- the linked same-parent `K2` source/Ward completion.

The needed object is genuinely a causal/off-shell or source-completed response, not merely a standard on-shell 3-graviton amplitude.

## Scientific conclusion

The literature audit finds a **computability-boundary convergence**:

1. generic nonlinear retarded/dispersive technology exists;
2. causal GR calculations exist for source/worldline/radiation observables;
3. a native pure-metric `h^3` response suitable for frozen `T_cut` requires gauge-safe/source-completed cubic effective-action authority;
4. the currently audited routes either change observable valence or inherit the already frozen C5 cubic-authority gap;
5. no published executable flat-space same-parent package was found that simultaneously supplies `Gamma3_ret`, `K2`, common normalization, Ward/source contacts, physical IR prescription and controlled hard-channel discontinuity.

Freeze the operational status

`BLOCKED_T_CUT_NATIVE_H3_EXECUTABILITY_AT_GAUGE_SAFE_CUBIC_EFFECTIVE_ACTION_BOUNDARY`.

Also retain

`BLOCKED_NOT_ZERO`.

This means the current published comparator technology does not let RQIR evaluate the frozen linked coordinate without introducing an additional model/convention choice. It does **not** imply that the physical coordinate is zero or nonexistent.

## New scoped labels

- `REL-NG-019 — GENERIC_RETARDED_THREE_POINT_DISPERSION_EXISTS_BUT_DOES_NOT_SUPPLY_GAUGE_SAFE_GRAVITY_SPECIALIZATION`;
- `REL-CUT-019 — NATIVE_PURE_GRAVITY_T_CUT_EXECUTABILITY_CONVERGES_ON_MISSING_GAUGE_SAFE_CUBIC_EFFECTIVE_ACTION_AUTHORITY`;
- `REL-BLOCK-004 — BLOCKED_T_CUT_NATIVE_H3_EXECUTABILITY_AT_GAUGE_SAFE_CUBIC_EFFECTIVE_ACTION_BOUNDARY`;
- `NG-FUNNEL-095 — ONSHELL_THREE_GRAVITON_KINEMATICS_CANNOT_REPLACE_THE_REQUIRED_HARD_CHANNEL_RETARDED_LINKED_CUT`.

## Classification

This is an **operational BLOCKED / authority-boundary result**. It is not:
- a consistency FAIL of GR or QFT;
- an exact comparator identity;
- regime-specific non-identifiability;
- near-degeneracy;
- a zero comparator column;
- a Candidate Gravity novelty certificate.

## Candidate-state consequence

No robust Candidate Gravity residual exists. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No heavy calculation is justified because the missing gauge-safe cubic causal object is upstream of row extraction.

MODEL_READINESS: 24%

Readiness change from Iteration 238: 0 percentage points. Comparator foundation remains `24/25`; unique residual remains `0/20`. The linked target's present computability boundary is now sharper, but no rubric block closes.
