# RQIR Candidate Gravity Entry Criteria

**Updated:** 2026-08-31  
**Status:** canonical entry checklist for the post-Paper-III Candidate Gravity branch. Papers I–III are scientifically closed; this file does not itself instantiate a model or make a new-physics claim.

## Infrastructure authority

Before creating a concrete model, use:

- `candidate_gravity/README.md`;
- `candidate_gravity/MODEL_SPEC_TEMPLATE.md`;
- `candidate_gravity/MODEL_TO_RQIR_CONTRACT.md`;
- `candidate_gravity/GATE_STATUS_TEMPLATE.yaml`;
- `candidate_gravity/BASELINE_COMPARATORS.md`;
- `candidate_gravity/ASSUMPTIONS_LEDGER_TEMPLATE.md`;
- `candidate_gravity/DERIVATION_MAP_TEMPLATE.md`;
- `candidate_gravity/recovery/RECOVERY_GUIDE.md`.

A future model must derive the RQIR hierarchy from one coherent dynamics rather than assigning `J`, `N`, `chi^R` or higher correlators independently.

## Minimal candidate object

A model must specify at minimum

`M_QG={physical state space, gravity variables, matter variables, dynamics, interaction, constraints/gauge structure, observables, parameter domain}`

or a fully equivalent covariant/channel/influence-functional definition.

## QG-001 — physical state space

Specify the physical Hilbert/algebraic/state space, gauge/constraint variables and physical observables.

**Pass:** no undefined kinematic degree of freedom is later treated as a detector observable.

## QG-002 — matter–gravity dynamics

Specify the action/Hamiltonian/channel/influence-functional law, including the matter, gravity and interaction sectors where that decomposition is meaningful.

**Pass:** the claimed source/interface observables are derived from this dynamics.

## QG-003 — controlled Newtonian / GR limit

Derive the accepted classical gravitational limit in the appropriate controlled regime.

**Pass:** Newtonian/static behavior and the relevant GR limit follow with a stated approximation/error domain, not merely dimensional matching.

## QG-004 — unitarity / positivity / CP

Establish the probability-consistency property appropriate to the framework: unitarity for closed quantum dynamics or positivity/complete positivity for open/channel/hybrid descriptions.

## QG-005 — constraint and gauge consistency

Demonstrate closure/consistency of constraints or a valid relational/gauge-invariant observable construction.

**Pass:** a coordinate/gauge artifact cannot become an RQIR signal channel.

## QG-006 — ordinary-QM / semiclassical limits

Recover ordinary QM when gravitational backreaction is negligible and the relevant semiclassical/stochastic/coarse-grained limit when quantum-gravitational information channels are suppressed.

## QG-007 — first model-specific discriminator

Derive the earliest observable difference relative to the mandatory comparator registry. State whether it lies in `J`, `N`, `chi^R`, a higher correlator, causal structure or another declared observable.

**Pass:** the difference is not exactly reproducible by the admitted comparator+nuisance/calibration class.

## QG-008 — Paper-I finite-discriminant propagation

Propagate the model through the closed Paper-I machinery using the model's own response map.

**Pass:** a physical candidate direction survives the exact calibration quotient.

## QG-009 — Paper-II statistical identifiability

Build the detector likelihood and require

`F_beta|theta > 0`

after exact hard constraints, source calibration, detector/systematic nuisances and comparator-model directions are profiled.

## QG-010 — Paper-III physical resource / measurability closure

Propagate the candidate through the closed Paper-III resource framework:

- detector PSD/cross-PSD and transfer;
- calibration Fisher rates;
- source metrology;
- acceptance/reset/coherence/dead time;
- controls/recertification;
- backaction/shared-record rules;
- robust final-significance wall clock.

**Pass:** the claimed discriminator has finite/defined physical resource requirements or a clearly stated conditional apparatus threshold surface.

## Mandatory cross-cutting gates

As applicable, the candidate must also address:

- gauge/relational consistency;
- conservation/Bianchi/Ward identities;
- causal support / microcausality / channel causality;
- positivity/spectral structure;
- flat-space QFT limit;
- EFT power counting;
- stress-energy smearing/renormalization;
- semiclassical/stochastic/classical-channel/hybrid/full-QFT/perturbative-QG degeneracy;
- detector measurability.

These states are recorded in `GATE_STATUS.yaml` for each model.

## Promotion rule

A speculative construction begins as `ANSATZ-*`.

Promotion to a numbered `QGxxx` model requires at least QG-001 and QG-002 PASS with repository authorities and no unresolved foundational contradiction in gauge/conservation/causality.

A model is not called RQIR-discriminating until QG-007, QG-008 and QG-009 pass. It is not experimentally closed until QG-010 passes.

## Epistemic discipline

Do not call a construction a quantum-gravity theory merely because it contains a quantized mediator, CTP kernel, stochastic metric or modified response function. The repository records the weakest claim supported by the gate/comparator state.
