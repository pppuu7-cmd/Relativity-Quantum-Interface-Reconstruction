# Candidate Gravity — Iteration 206: C5 linked-cut authority and specialization map

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Question

Iteration 205 froze a linked nonanalytic target

`T_cut = D Gamma3_ret,soft - W[D K2]`

which kills the unbounded local analytic derivative tower exactly. The next requirement is a standard perturbative-QG C5 positive control.

Does existing one-loop effective-action technology provide a controlled route to the required three-point nonanalytic/retarded object, or is the causal three-point sector fundamentally unavailable?

## Generic third-order nonlocal authority exists

Barvinsky, Gusev, Zhytnikov and Vilkovisky compute the one-loop effective action for a generic covariant differential operator through third order in background curvatures. Their construction:

- builds a complete nonlocal third-order curvature-invariant basis at that order;
- calculates the third-order form factors;
- supplies integral and generalized spectral representations;
- interprets the effective action as covariant one-loop vertices in gravitating-field models.

Authority: arXiv:0911.1168, *Covariant Perturbation Theory (IV). Third Order in the Curvature*.

Therefore the C5 problem is not blocked by lack of a generic cubic nonlocal formalism.

## Causal / in-in continuation exists in principle

Barvinsky–Vilkovisky's expectation-value formalism shows that, for the relevant in-vacuum initial-value problem, Lorentzian causal effective equations can be obtained from Euclidean effective equations by a special analytic continuation / retarded prescription. Later reviews describe this as an Euclidean version of Schwinger–Keldysh for expectation values.

Thus the project must no longer state a broad `NO_CAUSAL_COMPLETION` blocker for the one-loop C5 effective action.

The remaining problem is specialization and physical projection.

## New hard guardrail: off-shell gauge / parametrization dependence

The RQIR observable is off shell before physical source completion. Ordinary quantum-GR effective actions are generally dependent on the quantum gauge fixing and parametrization away from the equations of motion.

Modern explicit studies of the Vilkovisky–DeWitt / unique effective action in 4D quantum Einstein gravity confirm that the ordinary off-shell object is gauge/parametrization dependent, while the unique effective action can be made independent of these choices (for the declared configuration-space metric prescription).

Authorities:

- Giacchini, de Paula Netto, Shapiro, arXiv:2006.04217;
- Giacchini, de Paula Netto, Shapiro, arXiv:2009.04122.

Therefore **an arbitrary background-gauge `Gamma3` is not an authorized RQIR comparator column**.

A physical C5 cut must proceed by one of two routes:

1. construct the relevant Vilkovisky–DeWitt/unique effective action nonlocal third-order object and then project it to the RQIR source observable; or
2. construct the explicitly gauge-invariant/source-completed retarded observable so that gauge/field-parametrization dependence cancels before comparison.

This is consistent with the existing RQIR source-contact discipline of Iterations 148–149.

## Remaining specialization chain

The generic formalism does not itself hand us the required pure-gravity column. The remaining steps are:

1. specify the gauge/field-space convention appropriate for a gauge-independent physical result;
2. specialize the generic one-loop operator to the pure Einstein graviton fluctuation Hessian plus Faddeev–Popov ghosts;
3. combine graviton and ghost contributions into the actual 4D C5 nonlocal form factors;
4. impose RQIR's fixed physical/source-completed metric convention;
5. perform the in-vacuum/retarded continuation;
6. take the frozen timelike discontinuity;
7. evaluate `D Gamma3_ret,soft` and the same-parent `W[D K2]` on the fixed rows;
8. only then obtain the standard C5 positive-control column/rank for `T_cut`.

## Retained results

### `C5-CUT-001 — THIRD_ORDER_NONLOCAL_ONE_LOOP_FORM_FACTOR_AND_SPECTRAL_FORMALISM_EXISTS_FOR_GRAVITATING_FIELDS`

The third-order one-loop nonlocal sector is formally calculable and spectrally representable.

### `C5-CUT-002 — CAUSAL_IN_VACUUM_EFFECTIVE_EQUATIONS_HAVE_A_CONTROLLED_EUCLIDEAN_TO_LORENTZIAN_CONTINUATION_ROUTE`

The causal mean-field continuation is not the fundamental missing ingredient.

### `C5-CUT-003 — OFFSHELL_QUANTUM_GRAVITY_VERTEX_REQUIRES_GAUGE_PARAMETRIZATION_SAFE_UNIQUE_OR_PHYSICAL_SOURCE_PROJECTION`

An ordinary gauge-dependent off-shell effective vertex may not be treated as a physical RQIR comparator.

### `NG-FUNNEL-062 — C5_LINKED_CUT_BLOCKER_IS_NOW_PURE_GRAVITY_GRAVITON_GHOST_SPECIALIZATION_PLUS_GAUGE_SAFE_SOURCE_COMPLETED_RQIR_PROJECTION`

This replaces the broader older blocker with a precise implementation task.

## Current status

- generic third-order nonlocal one-loop formalism: ✅ supported;
- spectral representation: ✅ supported;
- causal in-vacuum continuation principle: ✅ supported;
- gauge-safe pure-gravity graviton+ghost specialization: 🟡 BLOCKED;
- source-completed RQIR cut column: 🟡 BLOCKED;
- local analytic C5 tower: ✅ exact null under the Iteration-205 discontinuity;
- Candidate Gravity residual: ❌ none.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

This iteration materially narrows the C5 cut task but does not yet restore the comparator-foundation point lost in Iteration 202.

## Next gate

Iteration 207 should decide the **gauge-safe pure-gravity specialization route** before any heavy tensor calculation:

- audit whether the Barvinsky–Vilkovisky third-order nonlocal coefficients already include a directly usable pure-gravity/unique-effective-action specialization;
- if not, freeze the fluctuation/ghost operators and unique-effective-action connection terms needed to generate one;
- identify the minimal subset of third-order nonlocal invariants that can contribute to the frozen null-soft TT cut, so the heavy calculation is reduced before implementation.

Run C4/AS/C3 cut-authority searches independently. No `ANSATZ-003`, Fisher or resources.
