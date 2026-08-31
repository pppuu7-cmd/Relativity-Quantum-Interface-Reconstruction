# RQIR Candidate Gravity — Iteration 208

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Objective

Establish a fully physical standard-QG nonanalytic positive control that avoids the off-shell gauge/parametrization ambiguity exposed in Iteration 207.

The chosen control is the one-loop on-shell four-graviton amplitude of four-dimensional pure Einstein gravity.

## Why this observable is useful

For an on-shell S-matrix element, ordinary gauge-fixing and field-parametrization dependence cancel. The nonanalytic part is constrained by unitarity: in an `s`-channel cut, the discontinuity is determined by a two-particle phase-space integral of products of tree Einstein-gravity amplitudes, summed over physical intermediate graviton helicities.

Schematically,

\[
\operatorname{Disc}_s\mathcal M_4^{(1)}
\propto
\sum_{\lambda_1,\lambda_2}
\int d\Phi_2\,
\mathcal M^{\rm tree}_{12\to\ell_1\ell_2}
\left(\mathcal M^{\rm tree}_{34\to\ell_1\ell_2}\right)^*,
\]

with the exact identical-state normalization to be fixed in any future executable implementation.

Any local analytic counterterm contributes an analytic polynomial/rational Taylor piece in the declared channel and therefore has zero branch discontinuity inside its analytic domain:

\[
\operatorname{Disc}_s P(s,t)=0.
\]

This makes the cut a direct positive control for the same local-analytic-null principle used by the RQIR `T_cut` protocol.

## Literature authority

Dunbar and Norridge (`hep-th/9408014`) computed all one-loop four-graviton amplitudes with arbitrary internal particle content and explicitly discussed unitarity constraints. Their result includes the pure-gravity amplitude.

Donoghue and Torma (`hep-th/9901156`) analysed the infrared structure of graviton-graviton scattering in the low-energy quantum EFT of GR. At one-loop order `O(E^4)` the pure-GR prediction depends only on Newton's constant. They identify the remaining dimensional pole in the virtual result as infrared and show that the physical cross section is finite and model-independent once soft-graviton bremsstrahlung is included.

## Mandatory infrared rule

A raw one-loop virtual graviton amplitude is **not** by itself an operational RQIR anchor because massless gravity contains infrared divergences.

Therefore freeze the following rule:

- formal unitarity/discontinuity statements may be used as theory checks with an explicitly declared regulator;
- a physical comparator observable must use either an inclusive soft-emission-completed quantity or a separately preregistered IR-subtracted hard amplitude;
- regulator-dependent virtual poles may never be interpreted as Candidate Gravity residuals.

## Scientific classification

### `C5-CUT-006 — PURE_EINSTEIN_ONE_LOOP_FOUR_GRAVITON_UNITARITY_CUT_IS_A_GAUGE_INVARIANT_NONANALYTIC_POSITIVE_CONTROL`

A standard-QG nonanalytic benchmark exists that is physical on shell and immune to arbitrary local analytic Wilson interpolation at the level of the branch discontinuity.

### `IR-NG-001 — RAW_VIRTUAL_GRAVITON_CUT_IS_NOT_AN_OPERATIONAL_ANCHOR_WITHOUT_IR_COMPLETION_OR_SUBTRACTION`

The virtual cut alone is not the final observable because of universal gravitational IR structure.

### `C5-NG-021 — AT_DECLARED_ONE_LOOP_LOW_ENERGY_ORDER_THE_PHYSICAL_GRAVITON_SCATTERING_RESULT_IS_MODEL_INDEPENDENT_AND_FIXED_BY_NEWTONS_CONSTANT`

This gives an unusually clean standard-QG low-energy positive control.

### `NG-FUNNEL-064 — ONSHELL_NONANALYTIC_POSITIVE_CONTROL_DOES_NOT_REPLACE_THE_OFFSHELL_SOURCE_COMPLETED_LINKED_CUT`

The on-shell S-matrix benchmark is not identical to the RQIR source-completed `T_cut`; the latter remains blocked at the Vilkovisky/nonlocal cubic specialization.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

The physical C5 nonanalytic sector is better anchored, but the comparator used in the actual RQIR quotient is still incomplete.

## Next gate

Audit whether loop-corrected soft-graviton/IR-factorization relations provide a controlled bridge from the gauge-invariant four-point cut to the soft linked sector. The bridge must explicitly account for four-dimensional infrared corrections to subleading soft relations. No inference about `T_cut` is allowed merely from the tree soft theorem.
