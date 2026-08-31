# RQIR Candidate Gravity — Iteration 207

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Objective

Before any heavy symbolic computation, determine whether the literature already supplies a directly reusable **gauge/parametrization-safe finite nonlocal curvature-cubic one-loop specialization of pure Einstein gravity** for the linked RQIR observable

\[
\mathcal T_{\rm cut}=\mathfrak D\Gamma^{(3)}_{\rm ret,soft}-\mathcal W[\mathfrak D K_2].
\]

The iteration is deliberately an authority/definition gate. A large CPT3 run is forbidden if the quantum operator itself is not physically frozen.

## Audited authority

### Generic third-order nonlocal CPT

Barvinsky, Gusev, Zhytnikov and Vilkovisky, arXiv:0911.1168, give the generic one-loop covariant perturbation theory through third order in generalized curvatures. This supplies the nonlocal three-point form-factor basis and generalized spectral representations needed in principle for causal expectation-value equations.

This result is a generic functional technology. It is **not** already the pure-Einstein Vilkovisky-DeWitt finite nonlocal cubic answer in the RQIR source convention.

### Vilkovisky unique effective action in 4D Einstein gravity

Giacchini, de Paula Netto and Shapiro, arXiv:2006.04217, explicitly evaluate the **divergent part** of the one-loop Vilkovisky unique effective action for quantum Einstein gravity and demonstrate the expected parametrization/conformal-gauge independence for the chosen configuration-space metric.

The key structural point for RQIR is that the Vilkovisky connection enters the off-shell Hessian. Therefore one may not infer that a finite nonlocal curvature-cubic vertex obtained from an ordinary gauge-fixed Hessian is already the unique/gauge-safe object.

The published calculation closes the divergent unique-action problem, but it does not provide the full finite nonlocal third-order form factors needed for `T_cut`.

### Complete one-loop pure-gravity integrands

Gomez, Jusinskas, Lopez-Arcos and Quintero Velez, arXiv:2411.07939, provide a compact recursion for complete one-loop N-graviton correlator integrands, including both graviton and ghost loops with the correct combinatorics.

This is potentially valuable as a computational engine or cross-check after the physical observable is frozen. It is not, by itself, a proof that the off-shell correlator is gauge/parametrization independent.

## Scientific result

No directly reusable published object was found in the audited authority satisfying all of:

1. pure Einstein graviton + ghost loop;
2. finite nonlocal curvature-cubic sector;
3. Vilkovisky-DeWitt/unique or otherwise explicitly gauge-safe off shell;
4. Lorentzian/in-in retarded continuation;
5. source-completed RQIR projection.

Therefore the correct classification is

`BLOCKED_C5_VD_NONLOCAL_CUBIC_SPECIALIZATION`.

This is **not** a consistency failure of perturbative quantum GR and not a zero C5 cut.

## Why heavy computation is not yet authorized

A calculation of generic CPT3 form factors for a convenient gauge-fixed graviton Hessian plus Faddeev–Popov ghosts could be mathematically correct in that gauge but still fail the RQIR requirement that the comparator column represent a physical gauge/parametrization-safe source response.

The missing Vilkovisky connection contribution is not known to be irrelevant to the finite curvature-cubic nonlocal sector. The fact that a given truncation of the connection terms suffices for a divergent calculation does not authorize the same truncation for the finite nonlocal three-point function.

Hence no heavy symbolic GitHub Action is started in this iteration.

## Retained results

- `C5-CUT-004 — GENERIC_CPT3_PLUS_GAUGE_FIXED_GRAVITON_GHOST_HESSIAN_IS_NOT_YET_A_PHYSICAL_OFFSHELL_RQIR_COMPARATOR`;
- `C5-CUT-005 — PUBLISHED_4D_VILKOVISKY_PURE_GRAVITY_RESULT_CLOSES_DIVERGENT_GAUGE_INDEPENDENCE_BUT_NOT_THE_REQUIRED_FINITE_NONLOCAL_CUBIC_SPECIALIZATION`;
- `NUM-NG-014 — DO_NOT_LAUNCH_HEAVY_SYMBOLIC_SPECIALIZATION_BEFORE_FREEZING_THE_GAUGE_SAFE_QUANTUM_OPERATOR`;
- `NG-FUNNEL-063 — OFFSHELL_LOOP_COMPARATOR_MUST_BE_GAUGE_PARAMETRIZATION_SAFE_BEFORE_NONANALYTIC_RESIDUAL_SUBTRACTION`.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

The blocker is narrower and the computational route is better specified, but the C5 RQIR nonanalytic comparator is not re-closed.

## Next gate

Freeze an independent **fully physical on-shell C5 nonanalytic positive control** using the one-loop four-graviton unitarity cut. Because massless gravity has infrared divergences, the anchor must be an IR-safe inclusive observable or an explicitly IR-subtracted hard quantity; a raw virtual amplitude is not sufficient. This anchor will not replace `T_cut`, but it can verify the expected local-counterterm-null nonanalytic sector without off-shell gauge ambiguity.
