# Candidate Gravity Newtonian / Classical-GR Limit — Iteration 134

**Date:** 2026-08-31  
**Model:** `ANSATZ-PQG-EFT-001` v0.1

## Goal

Validate QG-003 for the reference perturbative-QG EFT branch using the model's own Einstein-Hilbert normalization rather than assuming the accepted limit by name.

## Classical equation

The core gravitational action is

`S_g = (2/kappa^2) int d^4x sqrt(-g) R`,

with `kappa^2=32 pi G`.

At leading classical order its field equation is the Einstein equation

`G_mn = 8 pi G T_mn`.

For signature `(-,+,+,+)` and a weak static metric

`g_00 = -(1+2 Phi)`,

with nonrelativistic matter `T_00 ~= rho`, the linearized 00 component is

`G_00 ~= 2 nabla^2 Phi`.

Therefore

`2 nabla^2 Phi = 8 pi G rho`,

hence

`nabla^2 Phi = 4 pi G rho`.

For `rho=M delta^3(r)` and `Phi -> 0` at infinity,

`Phi(r) = -G M/r`.

Thus the attractive Newtonian acceleration is `a=-grad Phi` with magnitude `GM/r^2`.

## Normalization regression

`analysis/candidate_gravity_newtonian_limit_iteration134.py` checks:

1. `(8 pi G)/2 = 4 pi G`;
2. `kappa^2/4 = 8 pi G` for `kappa^2=32 pi G`;
3. the point-source potential/acceleration relation.

Using `G=6.67430e-11 SI`, `M=1`, `r=2`, the deterministic regression values are

- `4 pi G = 8.387172739141742e-10`;
- `Phi = -3.33715e-11`;
- `|a| = 1.668575e-11`.

## Gate result

**QG-003 = PASS** for this reference model/version within its declared low-energy domain:

- classical leading action is GR;
- static weak-field limit is Newtonian gravity with the correct normalization.

This PASS does not imply UV completion and does not repair QG-007, which remains FAIL because the branch is exactly comparator C5 at theory-class level.

## Cross-gate note

The contracted Bianchi identity and covariant stress conservation are structurally inherited from diffeomorphism-invariant Einstein-Hilbert dynamics, but the full quantum Ward/BRST and renormalized stress-tensor audit has not yet been performed. `conservation_bianchi_ward` therefore advances only to PARTIAL.

## Next useful gate

For this reference/control branch, QG-004/QG-005/QG-006 can be audited to validate the pipeline. For discovery work, however, a genuinely distinct `ANSATZ-*` is now higher value because QG-007 is permanently failed for this reference version.
