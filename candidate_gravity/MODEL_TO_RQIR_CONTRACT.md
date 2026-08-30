# Candidate Gravity → RQIR Contract

This contract is the mandatory interface between a concrete dynamical model and the closed RQIR Papers I–III machinery.

## Contract principle

All contract outputs must be derived from the **same declared model dynamics and parameter convention**. They may not be independently tuned to improve an RQIR discriminator.

## A. Model identity

Required:

- model ID/version;
- parameter vector and physical units;
- declared domain of validity;
- exact/perturbative approximation order;
- state preparation and boundary conditions.

## B. Source hierarchy

The model must supply, where applicable:

1. first moment/source expectation `J`;
2. centered symmetrized noise `N`;
3. ordered/commutator response `D` and/or retarded susceptibility `chi^R`;
4. higher connected correlators required at the claimed order;
5. parent CTP/influence/channel object or explicit reason why another representation is fundamental.

For every object specify:

- operator ordering;
- spacetime smearing;
- renormalization/subtraction;
- causal prescription;
- gauge/relational status;
- approximation error.

## C. Conservation and causality contract

Provide explicit checks/references for:

- stress-energy conservation / Ward identity;
- Bianchi compatibility where gravitational equations require it;
- causal support of retarded kernels;
- microcausality or declared channel-causality analogue;
- positivity/spectral conditions where applicable.

## D. Comparator contract

For every applicable comparator in `BASELINE_COMPARATORS.md`, specify one of:

- `DISTINCT` — derived observable difference exists;
- `DEGENERATE` — current RQIR observable set cannot distinguish;
- `NOT_APPLICABLE` — with reason;
- `BLOCKED` — derivation missing.

No `DISTINCT` claim is accepted without an explicit observable and nuisance/calibration audit.

## E. Paper I contract — operational discriminant

Supply a finite source/detector response map in the same parameter coordinates as calibration constraints.

Minimum pass data:

- calibration map `A` or declared nonlinear generalization;
- candidate difference direction;
- physical-state admissibility;
- detector/source response;
- proof or numerical certificate that the difference survives the exact calibration quotient.

## F. Paper II contract — statistical identifiability

Supply the detector likelihood or local score/Fisher objects needed to compute

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Must include applicable nuisance families:

- source amplitude/preparation;
- transfer gain/phase;
- spectral/covariance nuisance;
- timing/geometry/additive controls;
- comparator-model directions.

Exact hard constraints are eliminated before profiling.

## G. Paper III contract — physical resource closure

Supply or parameterize:

- detector PSD/cross-PSD and transfer;
- calibration Fisher-rate matrices;
- source-metrology Fisher rate;
- acceptance/reset/coherence/dead time;
- control drift/floor/reference Fisher;
- backaction/shared-record likelihood where credit is claimed;
- robust uncertainty set.

The output is a resource certificate or conditional threshold surface. Missing apparatus inputs remain symbolic; they are never fabricated.

## H. Output package

Every model version must produce:

- `MODEL.md`;
- `GATE_STATUS.yaml`;
- `DERIVATION_MAP.md`;
- `ASSUMPTIONS_LEDGER.md`;
- `COMPARATOR_STATUS.md`;
- reproducible analysis/tests;
- recovery delta for every material scientific change.

## Contract failure rules

The model is `BLOCKED` if an object required for the claimed discriminator cannot be derived consistently from the declared dynamics.

The model is `REJECTED` if a mandatory consistency gate fails without a controlled modification that defines a new model version.
