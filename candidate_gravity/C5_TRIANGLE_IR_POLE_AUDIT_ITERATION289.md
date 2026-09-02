# Candidate Gravity C5 — Iteration 289 triangle IR-pole audit

**Date:** 2026-09-02  
**MODEL_READINESS:** **24%**

## Purpose

Audit the epsilon asymptotics of the complete 210-monomial raised-triangle reduction produced by the Iteration-288 workflow before promoting any finite hard-channel coefficient.

## Critical correction to Iteration 288

The Iteration-288 workflow correctly reconstructed the three complete same-parent triangle numerators, passed loop reflection, and passed the scalar `l^2` cancellation calibration. However, its final ordinary polynomial extrapolation in `epsilon` is not valid for the actual numerator scans because those scans contain an explicit `1/epsilon` term.

For example, the `(0,0.21)` common-cut scan is

`[-3.38996, -6.33924, -12.24522, -24.06092]`

at

`epsilon=[0.02,0.01,0.005,0.0025]`.

This is manifestly Laurent-like rather than finite-polynomial behavior.

Therefore the raw Iteration-288 values `-31.4453`, `2.19568`, `-3.24474` are **not** finite physical cut coefficients and are superseded as such.

## Laurent audit

Write

`D_common(epsilon) = A/epsilon + B + O(epsilon)`.

Fit `epsilon D_common` and extract its intercept.

### Scalar `l^2` calibration

The calibration cancels the repeated propagator and should reduce to the finite ordinary one-null two-mass triangle. Its cubic Laurent residues are

- `(0,0.21)`: `-3.50e-8`;
- `(0,0.41)`: `-3.69e-8`;
- `(0.21,0.41)`: `-6.06e-8`.

Thus the calibration is consistent with zero IR residue while reproducing the exact finite triangle cut near `-3.3452481449`.

### Actual same-parent triangle numerators

The three residues are

- `A_(0,0.21) = -0.05908474654789776`;
- `A_(0,0.41) = +0.003959618177742245`;
- `A_(0.21,0.41) = -0.006164685444448067`.

Cubic vs quadratic residue extraction differs by at most `4.46e-7`.

Their sum is

`A_triangle,total = -0.061289813814603585`.

Since the two Iteration-287 hard-bubble discontinuity coefficients are finite at this stage, the currently reduced non-scaleless `B3` block retains the same nonzero common-cut pole residue.

Freeze:

`PASS_DETECTED_ROBUST_UNCANCELLED_TRIANGLE_COMMON_CUT_IR_POLE__FINITE_COEFFICIENT_BLOCKED`.

## Diagnostic finite terms

A formal Laurent finite coefficient can be extracted from the same four-point scans:

- triangle finite-part sum: `-0.3171725193424992`;
- adding the two Iteration-287 bubble coefficients gives the diagnostic value `-0.3395824187498212`.

These numbers are **not authoritative physical finite coefficients** while the total `1/epsilon` residue remains nonzero. They may change after the required source/Ward/contact and linked two-point completion.

## Scientific consequence

This is not a failure of Candidate Gravity and not a contradiction of the C5 calculation. It identifies the precise stage at which the partial `B3` block can no longer be interpreted independently.

The RQIR observable was frozen earlier as

`T_cut = D Gamma3_ret,soft - W[D K2]`.

The current calculation contains only a scoped same-parent C5 part of the three-point object. A physical finite comparator coordinate requires the missing source/Ward/contact pieces and the same-parent linked two-point contribution to be included before the finite hard-channel coefficient is frozen.

## Current blocker

`BLOCKED_LINKED_SOURCE_WARD_CONTACT_IR_POLE_CANCELLATION_BEFORE_FINITE_C5_T_CUT`.

## Next gate — Iteration 290

1. Identify all missing C5 terms required by source completion and the gravitational Ward identity in the same convention as the current `B3` block.
2. Isolate their `1/epsilon` hard-channel residues before computing finite terms.
3. Derive the linked `W[D K2]` pole contribution from the same parent dynamics.
4. Test whether the total pole cancels in `T_cut`.
5. Only after cancellation extract the finite triangle/bubble master coefficients and compare against the remaining comparator classes.

`ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.
