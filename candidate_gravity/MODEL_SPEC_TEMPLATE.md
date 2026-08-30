# Candidate Gravity Model Specification Template

**Model ID:** `ANSATZ-*` or `QGxxx`  
**Version:** 0.1  
**Status:** DRAFT / TESTING / ADMISSIBLE / REJECTED / FROZEN

## 1. Physical state space

State precisely:

- Hilbert/algebraic/state space;
- gravity variables;
- matter variables;
- physical vs gauge/constraint variables;
- boundary/asymptotic data;
- superselection sectors if present.

## 2. Dynamics

Provide one primary dynamical definition:

- action, Hamiltonian + constraints, master equation, channel, influence functional, path integral, or equivalent;
- `H_matter`, `H_grav`, `H_int` when Hamiltonian language is valid;
- coupling constants and dimensions;
- initial/boundary conditions;
- whether evolution is closed, open, stochastic, hybrid or emergent.

No detector-facing kernel may be inserted independently of this dynamics without being labeled phenomenological and outside the model core.

## 3. Constraint / gauge structure

List all constraints and demonstrate or reference:

- closure/consistency;
- gauge transformations;
- physical/relational observables;
- gauge fixing only where used for computation;
- proof that claimed RQIR observables are gauge/relationally meaningful.

## 4. Domain of validity and scales

Declare:

- weak-field / perturbative expansion parameter;
- energy, length and time scales;
- UV/IR cutoffs if any;
- EFT ordering/power counting;
- renormalization prescription/domain;
- conditions under which truncations are controlled.

## 5. Required limits

Derive or state the exact task needed to derive:

- Newtonian/static weak-field limit;
- appropriate classical GR limit;
- ordinary QM limit when gravitational backreaction is negligible;
- flat-space QFT limit where applicable;
- semiclassical/stochastic/coarse-grained limit where applicable.

## 6. Probability / consistency structure

Specify and test the applicable condition:

- Hermiticity/unitarity for closed quantum dynamics;
- positivity / complete positivity for channels/open systems;
- normalized probabilities;
- causal support/microcausality/channel causality;
- conservation/Bianchi/Ward identities.

## 7. Source observables derived from the model

Derive in one consistent convention:

- `J = <T>` or the declared first-moment source object;
- centered symmetrized noise `N`;
- commutator/ordered response `D` and/or retarded response `chi^R`;
- higher connected correlators required by the model;
- CTP/influence functional or equivalent parent object when available.

State smearing, operator ordering and renormalization explicitly.

## 8. First model-specific discriminator

Identify the earliest observable level at which the model differs from each applicable comparator.

For each claimed difference record:

- observable;
- parameter direction;
- baseline comparator;
- exact/approximate nature of difference;
- whether calibration/nuisance freedom can reproduce it.

## 9. RQIR propagation

Link to:

- Paper-I finite-discriminant analysis;
- Paper-II detector likelihood and `F_beta|theta`;
- Paper-III physical resource certificate.

The model is not experimentally discriminating until all three levels are addressed.

## 10. Falsification / rejection conditions

List concrete conditions that reject the model or current version, including:

- inconsistency of constraints;
- violation of positivity/unitarity/causality;
- failure of required limits;
- exact degeneracy with comparator classes;
- zero profiled Fisher;
- divergent/undefined physical resource requirement.

## 11. Open assumptions

Every unresolved assumption must also appear in `ASSUMPTIONS_LEDGER.md` for the model.

## 12. Authority map

List canonical derivations, code, tests, literature authorities and recovery state. Do not cite chat history as authority.
