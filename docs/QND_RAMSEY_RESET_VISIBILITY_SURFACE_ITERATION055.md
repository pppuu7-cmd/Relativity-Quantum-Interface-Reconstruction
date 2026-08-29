# RQIR Iteration 055 — QND Ramsey reset/visibility resource surface

**Status:** physical-resource refinement of source metrology; not a new-physics claim.

## Purpose

The current D2 ambiguity is no longer abstract: after RQIR-NG-005 the hidden source amplitude must be supplied by independent source metrology unless complementary calibration removes the detector-relevant null. Iterations 047–051 built energy-population and Ramsey-QND channels. Iteration 055 adds the missing physical overheads that determine Fisher **per wall-clock second** rather than per accepted copy.

For Ramsey phase `phi = Omega_E T`, acceptance `p_E`, visibility `V`, and fresh-source/reset overhead `t_reset`, use

`R_alpha(phi) = p_E F_alpha(phi,V) / (t_reset + phi/Omega_E)`.

This is an independent/sacrificial source-metrology campaign. It does **not** relax RQIR-NG-023: QND relative to the isolated source Hamiltonian is not equivalent to nondemolition of the ordered-response science resource.

## Exact D2 rate boundaries

Using the centered D2 source-amplitude requirements already established,

- Branch0: `C_alpha = 4.55511`;
- best4: `C_alpha = 0.05006143859980483` plus `T4 = 5.864018521 h` covariance floor;
- best5: no source prior plus `T5 = 10.608109160 h` covariance floor.

The branch comparison can be written directly in terms of physical source-metrology Fisher rate `R_alpha`:

`T0 = C0/R_alpha`,

`T4,total = T4 + C4/R_alpha`,

`T5,total = T5`.

Therefore the exact crossovers are

- Branch0 ↔ best4: `R_alpha = 2.1340355145e-4 s^-1`;
- best4 ↔ best5: `R_alpha = 2.9312161645e-6 s^-1`.

These thresholds are independent of how the Ramsey apparatus realizes that rate. All apparatus details enter only through `R_alpha(p_E,V,Omega_E,t_reset)`.

## New resource result

### RQIR-RESOURCE-026 — source reset is a first-class Fisher resource

Per-copy Fisher is insufficient for architecture choice. A finite reset/preparation overhead changes both the optimal Ramsey phase and the branch winner. The correct optimization variable is

`max_phi p_E F_alpha(phi,V)/(t_reset + phi/Omega_E)`.

Consequences:

1. increasing `t_reset` can only reduce the optimized source-metrology rate at fixed `Omega_E,p_E,V`;
2. reduced visibility can only reduce the optimized rate;
3. when reset dominates, longer/stronger Ramsey interactions become relatively less expensive because the fixed overhead is already paid;
4. when interaction time dominates, the optimum shifts toward the Fisher-per-time rather than Fisher-per-copy point;
5. branch selection must therefore be reported in the four-dimensional physical surface `(p_E,V,Omega_E,t_reset)`, not as one universal cycle-time number.

## Relation to detector-level Fisher

This gate does not modify the centered detector Jacobian or the profiled `F_beta|theta` itself. It supplies the physical rate at which the independent source prior `C_alpha` can be accumulated. Thus NG-005 remains intact and the D1/D2 detector-level calculation remains properly separated from source preparation metrology.

## Reproducibility

Implementation:

`analysis/qnd_ramsey_reset_visibility_surface_iteration055.py`

The script imports the accepted Iteration-051 Ramsey likelihood, optimizes the physical Fisher rate, prints a representative resource surface and verifies monotonicity/regression conditions plus the exact Branch0/best4/best5 rate boundaries.

## Next gate

Run the same wall-clock treatment for the finite-resolution Gaussian QND energy pointer of Iteration 049 and compare Ramsey versus pointer readout at equal source preparation/reset assumptions. The useful quantity is the lower envelope in physical rate/coupling space, not the nominal per-copy Fisher. Only after this comparison should one freeze a source-metrology architecture.
