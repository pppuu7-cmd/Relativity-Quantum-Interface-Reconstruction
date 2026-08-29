# RQIR Recovery Delta — Iteration 052

**Date:** 2026-08-29

Apply this delta after repository framework v2.6 and Iterations 049–051.

## New retained result

A QND Ramsey ancilla coupled through a controlled source-energy phase `phi=Omega_E T` must be optimized for Fisher per wall time, not Fisher per accepted shot.

At ideal Ramsey visibility and negligible source reset,

`R_E^(alpha)=p_E Omega_E F_alpha(phi)/phi`.

The Toy009 plus-branch rate optimum is

- `phi_rate=1.092306912`;
- `F_alpha=0.002756370099`;
- `F_alpha/F_energy-projective=0.293484246`;
- `max F_alpha/phi=0.002523439217`.

Therefore

`R_E,max^(alpha)=0.002523439217 p_E Omega_E`.

### RQIR-RESOURCE-024

Ramsey Fisher-per-copy and Fisher-per-time have distinct optima.  The per-copy optimum from Iteration 051 (`phi~2.41867`, `F_alpha~0.00389041`) must not be used directly as the wall-clock operating point.

## D2 branch conversion

Retain Iteration 050 physical source-metrology rate boundaries:

- Branch0/best4: `R_E=2.13404e-4 s^-1`;
- best4/best5: `R_E=2.93122e-6 s^-1`.

For Ramsey acceptance `p_E=.5` and ideal visibility/zero reset:

- Branch0 beats best4 when `Omega_E>~0.16913742 s^-1`;
- best4 beats best5 when `Omega_E>~0.002323194 s^-1`.

At the Branch0/best4 boundary the rate-optimal controlled interaction duration is `~6.4581 s`.

## Scope / negative guards

- This is not a hardware forecast; `Omega_E` is the controlled phase accumulation rate in the Toy009 dimensionless energy coordinate.
- Strong Ramsey source readout remains assigned to independent/sacrificial copies.  NG-023 remains active: QND with respect to isolated `H` does not guarantee preservation of the ordered-response science resource.
- A physical implementation must state its interaction Hamiltonian, visibility, acceptance, source reset/preparation time, and stress-energy/conservation bookkeeping.

## Next continuation step

Use

`R_E=p_E F_alpha(phi,V)/(t_reset+phi/Omega_E)`

and solve the Branch0/best4 and best4/best5 boundary surfaces in `(Omega_E,V,p_E,t_reset)`.  Then compare this Ramsey surface to the finite Gaussian pointer surface from Iterations 049–050 and choose the more favorable realizable source-metrology channel.