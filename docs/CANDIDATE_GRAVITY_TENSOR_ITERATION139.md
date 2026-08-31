# Candidate Gravity Iteration 139 — conserved-source tensor completion

**Date:** 2026-08-31  
**Model:** `ANSATZ-RQIR-KL-002` v0.1  
**Decision:** retain; linear tensor gate PASS_SCOPED, nonlinear completion remains open

## Question

Does the positive spectral continuum remain physically meaningful after restoring the standard conserved-source tensor structure rather than treating every spectral component as a scalar denominator?

## Linear tensor amplitudes

For conserved sources in four dimensions, massless GR exchange has the trace structure

`T_mn T'^mn - (1/2) T T'`.

A positive massive Fierz–Pauli spin-2 spectral component has

`T_mn T'^mn - (1/3) T T'`.

Therefore the minimal linear tensor completion of `KL-002` is

`A ~ [T.T'-(1/2)TT']/p^2`

`    + beta int ds rho_hat(s) [T.T'-(1/3)TT']/(p^2-M_*^2 s)`

with the appropriate retarded prescription.

## Nonrelativistic result

For two nonrelativistic sources the common source contractions give

massless coefficient `1/2`,

massive spin-2 coefficient `2/3`.

Hence

`(2/3)/(1/2)=4/3`.

The scalarized Iteration-138 potential is therefore updated to

`Phi(r)=-GM/r [1+(4/3) beta W(M_*r)]`.

The long-range correction still obeys

`|delta Phi/Phi_GR| <= (4/3) beta exp(-M_*r)`.

## Traceless-probe relation

If one conserved probe is traceless, the trace term vanishes for both the massless and massive amplitudes. The tensor coefficient ratio in that channel is therefore `1`, not `4/3`.

If beta is calibrated by a nonrelativistic force channel, the corresponding traceless-probe continuum effect is fixed at relative factor

`1/(4/3)=3/4`.

This becomes a new cross-channel RQIR relation that cannot be independently tuned within v0.1.

## Interpretation

The `4/3` factor is the standard linear vDVZ signature of massive spin-2 exchange. It is not a new-theory claim. Its role here is to prevent the spectral ansatz from hiding tensor/helicity information inside a scalar transfer function.

The continuum is gapped, so the vDVZ factor does not by itself invalidate the model: at distances large compared with `M_*^-1` the massive sector is Yukawa-suppressed. However, any parameter region that makes the continuum experimentally relevant must satisfy corresponding short-range/PPN/lensing constraints.

## Nonlinear warning

Massive-gravity theories can invoke nonlinear Vainshtein screening, but no such mechanism belongs to `KL-002` v0.1. Importing it now would materially change the dynamics and must define a new model version with its own constraint/ghost audit.

The nonlinear continuum completion therefore remains a QG-005 blocker even though the linear conserved-source tensor structure is now explicit.

## Reproducibility

- `analysis/candidate_gravity_tensor_projector_iteration139.py`
- `results/candidate_gravity_tensor_projector_iteration139.json`

Result: `PASS_SCOPED_LINEAR_TENSOR_WITH_VDVZ_SIGNATURE`.

## New design value

The candidate fingerprint is now richer than a generic Yukawa force:

1. NR force amplitude: fixed `4/3` continuum tensor factor;
2. traceless-probe channel: fixed `3/4` relation after NR calibration;
3. threshold absorption/noise: fixed by the same positive spectral density.

A later RQIR quotient should test these linked channels jointly.
