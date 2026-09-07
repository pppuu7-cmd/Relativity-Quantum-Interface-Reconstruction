# Model Audit — 4D Einstein–Hilbert General Relativity

Benchmark ID: RQIR7-M01-GR-EH-MINK
Role: null control
State: ACTIVE / NOT YET TERMINAL
Scope: four-dimensional Einstein–Hilbert gravity, Lambda=0, weak-field expansion about Minkowski spacetime, ordinary conserved matter stress tensor.

## Concrete realization

Action:

\[
S[g,\psi]=\frac{M_{\rm Pl}^2}{2}\int d^4x\sqrt{-g}\,R + S_m[g,\psi].
\]

This audit does not claim to cover arbitrary cosmological constant, nontrivial global topology, matter anomalies, quantum GR loops, or every nonperturbative GR sector. Those require separate realizations if relevant to frozen RQIR observables.

## Evidence table

| Field | Evidence-level result | RQIR interpretation | State |
|---|---|---|---|
| Action/equations | Einstein–Hilbert action; Einstein field equations | intended classical GR baseline candidate | supported |
| Validity regime | classical GR; here restricted to weak-field Minkowski sector | matches first null-control realization | frozen scope |
| Physical DOF | two physical radiative tensor polarizations/helicities after gauge constraints in 4D linearized GR | no extra scalar/vector physical pole expected | supported |
| Propagator/poles | gauge-fixed linearized theory has the massless graviton pole; gauge-dependent components are not extra physical modes | positive control for recognizing gauge artifacts vs physical poles | supported; exact RQIR pole convention still to map |
| Ghost/tachyon | no additional higher-derivative physical ghost/tachyon is introduced by Einstein–Hilbert action with conventional sign | null-control expectation | supported within stated perturbative scope |
| Gauge/Ward | diffeomorphism invariance; Bianchi identity enforces compatibility with covariantly conserved source | should satisfy frozen source/Ward consistency if conventions align | supported; literal gate mapping open |
| Causal/retarded structure | harmonic/generalized-harmonic formulations cast Einstein equations into a hyperbolic wave system; linearized gravitational perturbations admit retarded Green-function solutions | causal response object exists | supported |
| Source rule | metric couples to matter stress-energy; linearized field equation sourced by conserved stress-energy | candidate match to GR source baseline | supported |
| Nonlinear vertices | expansion of Einstein–Hilbert action generates the standard infinite hierarchy of graviton self-interaction vertices | required objects exist in principle/order by order | supported; exact frozen vertex order open |
| GR/classical limit | realization is GR itself | identity limit | exact |
| Q1–Q7 fingerprint | literal Q1–Q7 definitions not yet pinned from frozen repo authority | must not infer from memory | OPEN BLOCKER TO FINALIZATION |
| Frozen observable map | exact frozen mapping not yet pinned | cannot declare complete funnel | OPEN |
| Comparator span | expected to contain classical GR baseline, but literal basis/path/hash not yet recovered | exact identity remains provisional | OPEN |
| Quotient residual | expected zero if literal comparator contains this exact realization in the tested domain | not yet a measured/frozen result | PROVISIONAL ZERO ONLY |

## Causal evidence

Living Reviews sources document that harmonic gauge reduces Einstein's equations to a wave/hyperbolic system and that linearized gravitational equations can be solved with retarded Green functions. These facts establish the existence of an appropriate causal-response structure for this realization; they do not by themselves prove a particular RQIR comparator identity.

## Source / gauge evidence

Diffeomorphism invariance and the contracted Bianchi identity supply the structural conservation identity associated with the Einstein equation. The exact frozen RQIR Ward/source normalization and contact-term convention must still be read from repository authority before this row can be marked gate-complete.

## Comparator decision rule for this control

If and only if the literal frozen comparator contains the same Einstein–Hilbert weak-field baseline in the tested domain and the quotient definition removes it exactly, finalize:

- comparator relation: exact identity;
- quotient residual: zero by frozen construction;
- final status: `EXACT_COMPARATOR_IDENTITY`;
- benchmark rollup: blue/null-control degeneracy, not FAIL.

If the required frozen protocol cannot be mapped to this realization, use the applicable BLOCKED status rather than guessing. If a nonzero residual appears, first audit protocol/domain/comparator mismatch before any scientific FAIL claim.

## Current first blocker

`FROZEN_PROTOCOL_LITERAL_MAPPING`: exact repository authority for Q1–Q7, comparator span, quotient definition, and acceptance conditions has not yet been pinned into `protocol/FROZEN_RQIR_PROTOCOL_REFERENCE.md`.

This blocker prevents terminal status but is NOT evidence against GR.

## Authoritative scientific sources currently used

1. O. Sarbach and M. Tiglio, *Continuum and Discrete Initial-Boundary Value Problems and Einstein's Field Equations*, Living Reviews in Relativity 15, 9 (2012), harmonic formulation / well-posed hyperbolic reductions: https://link.springer.com/article/10.12942/lrr-2012-9
2. E. Poisson, *The Motion of Point Particles in Curved Spacetime*, Living Reviews in Relativity 7, 6 (2004), linearized gravitational equations and retarded gravitational Green functions: https://link.springer.com/article/10.12942/lrr-2004-6
3. C. P. Burgess, *Quantum Gravity in Everyday Life: General Relativity as an Effective Field Theory*, Living Reviews in Relativity 7, 5 (2004), Einstein gravity as the low-energy gravitational EFT baseline: https://link.springer.com/article/10.12942/lrr-2004-5

Additional primary/reference sources should be attached when exact frozen propagator/vertex/Q1–Q7 conventions are recovered.
