# RQIR Candidate Gravity Entry Criteria

**Recovered from prior RQIR planning discussions:** 2026-08-30  
**Status:** future-work entry checklist only. This document does **not** open a Candidate Gravity branch, does not modify Papers I–III, and contains no new-physics claim.

## Purpose

RQIR is an operational reconstruction / identifiability / resource framework, not itself a theory of quantum gravity. A future candidate-gravity model should be admitted only as a separate branch once a concrete dynamical model exists and can be propagated through the mature RQIR pipeline.

The article architecture already reserves a later Paper IV for this purpose. This checklist makes the previously discussed entry gates explicit so they are not lost in chat history.

## Minimal candidate object

A candidate model should specify, at minimum, a coherent set

`M_QG={H_phys, gravity variables, H_matter, H_grav, H_int, constraints/gauge structure, observables}`

or an equivalent covariant/influence-functional/channel formulation.

The source hierarchy `J=<T>`, `N`, `chi^R`, higher correlators and detector transfer must be **derived consistently from the same model** rather than assigned independently to fit an RQIR discriminator.

## QG-001 — physical state space

Specify the physical state/Hilbert space or algebraic state space, including which variables are gauge/constraint variables and which are physical observables.

Pass condition: no undefined kinematic degrees of freedom are later treated as measurable detector variables.

## QG-002 — matter–gravity interaction

Specify the interaction/dynamical law coupling quantum matter to the gravitational sector.

A weak-field reference may be written schematically as

`H_int = -(1/2) integral d^3x h_mn T^mn`,

but using this form does not by itself define a new model. The gravity-sector dynamics and constraints must also be specified.

## QG-003 — controlled Newtonian / GR limit

Demonstrate a controlled regime reproducing the accepted classical gravitational limit. In the appropriate weak/static regime this must reduce to Newtonian gravity; in the broader classical regime it must be compatible with the relevant GR equations/observables.

This is not merely dimensional matching of a potential.

## QG-004 — Hermiticity / unitarity / positivity

For closed quantum dynamics, establish Hermiticity/unitarity as appropriate. For open/channel/hybrid descriptions, establish the corresponding positivity / complete-positivity / probabilistic consistency condition required by the declared framework.

## QG-005 — constraint and gauge consistency

Demonstrate closure/consistency of the relevant gravitational constraints or the relational/gauge-invariant observable construction. Coordinate gauge artifacts must not become RQIR signal channels.

## QG-006 — semiclassical and ordinary-QM limits

Show how ordinary quantum mechanics is recovered when gravitational backreaction is negligible and how the appropriate semiclassical/stochastic limit emerges when quantum gravitational information channels are coarse-grained or suppressed.

## QG-007 — first model-specific discriminator

Derive, rather than postulate, the first source/interface observable that differs from the declared semiclassical/stochastic/full-QFT baselines. Identify whether the distinction appears in `J`, `N`, `chi^R`, a higher correlator, causal structure, or another explicitly defined observable.

No claim proceeds if the candidate difference is exactly reproducible by an already-admitted baseline nuisance/model class.

## QG-008 — RQIR finite-discriminant propagation

Propagate the candidate through the mature Paper-I finite-discriminant machinery. Toy009/Toy010 may be used as regression/diagnostic constructions, but the candidate must supply its own derived response map.

Pass condition: the candidate creates a declared detector/source direction not removed by the exact calibration constraints.

## QG-009 — statistical identifiability

Build the detector likelihood and require positive nuisance-profiled information

`F_beta|theta > 0`

after exact hard constraints, source-amplitude calibration, detector/systematic nuisance profiling and the relevant model-degeneracy alternatives.

Passing a mathematical nullspace test without this gate is insufficient.

## QG-010 — physical resource / measurability gate

Propagate the candidate through Paper III:

- detector PSD/cross-PSD and transfer;
- calibration Fisher matrices;
- source preparation/metrology;
- coherence, reset, acceptance and shot counts;
- controls/recertification/duty;
- final-significance wall clock and robust uncertainty.

A candidate that is identifiable only with undefined or divergent physical resources has not passed the experimental RQIR gate.

## Mandatory cross-cutting consistency gates

The QG-001…010 checklist does not supersede the broader mature RQIR consistency requirements. A serious candidate must also address, as applicable:

- diffeomorphism / relational consistency;
- conservation, Bianchi and Ward identities;
- causal support / microcausal or channel-causality structure;
- positivity/unitarity/CP;
- controlled GR/Newtonian and flat-space QFT limits;
- EFT power counting;
- stress-energy renormalization;
- classical/stochastic/hybrid/full-QFT degeneracy;
- detector measurability.

## Entry rule

Do **not** call a branch a quantum-gravity model merely because it contains a quantized mediator, a CTP kernel or a modified response function. Candidate Gravity begins only when one dynamical construction supplies the required state space, dynamics, constraints, limits and derived RQIR observables together.

Until then, Papers I–III remain reconstruction/identifiability/resource papers, and Paper III apparatus closure remains the active research front.
