# ANSATZ-RQIR-CTP-001 — RQIR-constrained causal spectral CTP gravity

**Version:** 0.1  
**Status:** DRAFT / TESTING  
**Purpose:** first genuinely RQIR-driven Candidate-Gravity ansatz after the perturbative-QG reference branch. It is a weak-field, low-energy effective model, not a UV completion and not yet a novelty claim.

## 1. Construction principle

RQIR Papers I–III require `J`, `N`, and ordered/retarded response to come from one declared dynamics rather than being tuned independently. This ansatz therefore takes a single causal CTP kernel in the physical spin-2 sector as the primitive low-energy object. Its dispersive response and quantum noise are tied to the same positive spectral density.

The model is deliberately minimal: one new scale `M_*`, one dimensionless amplitude `beta`, and one frozen dimensionless spectral shape. If this structure is exactly degenerate with an existing comparator class after nuisance profiling, the ansatz is rejected or retained only as a control.

## 2. State space and regime

Background split:

`g_mn = eta_mn + kappa h_mn`, `kappa = sqrt(32 pi G)`.

Matter is initially the same real scalar QFT used by the C5 reference branch. The resolved gravitational variables are the gauge-fixed linearized metric perturbations, with detector claims restricted to conserved-source / gauge-invariant or relational combinations.

The effective state description is Gaussian in the resolved spin-2 sector at v0.1. A microscopic unitary dilation for the nonlocal kernel is not yet part of the model; that is a QG-004/QG-005 task, not an assumption to be silently imported.

## 3. Primary CTP dynamics

Use Keldysh variables

`h_r = (h_+ + h_-)/2`, `h_a = h_+ - h_-`.

The weak-field CTP effective action is

`Gamma_CTP = Gamma_EH+matter[h_+,phi_+] - Gamma_EH+matter[h_-,phi_-]`

`            + 1/2 int h_a Pi_R h_r + i/4 int h_a Pi_H h_a + O(h^3)`.

All tensor contractions and spacetime integrals are implicit in the compact notation above.

On the conserved-source spin-2 sector,

`Pi_R^{mn,ab}(p) = P2^{mn,ab}(p) Pi_R^(2)(p)`.

The dimensionless causal form factor is defined by

`zeta(p) = -(p^2 + i 0 p^0)/M_*^2`,

`F_R(p) = zeta(p) int_1^infty ds rho_hat(s)/(s + zeta(p))`,

with the frozen v0.1 shape

`rho_hat(s) = exp(1-s) Theta(s-1)`,

so `rho_hat >= 0` and `int_1^infty rho_hat(s) ds = 1`.

The spin-2 retarded inverse kernel is parameterized as

`K_R^(2)(p) = K_GR,R^(2)(p) [1 + beta F_R(p)]`,

with

`beta >= 0`, `M_* > 0`.

The exact overall sign convention for `K_GR,R` is inherited from the frozen linearized-GR convention used in the reference branch; the model-specific object is the multiplicative factor `1 + beta F_R`.

The v0.1 quantum-noise kernel is not independent. In the vacuum/KMS-zero-temperature branch it is tied to the same causal kernel by the bosonic spectral relation

`Pi_H^(2)(p) = -2 sgn(p^0) Im Pi_R^(2)(p)`

up to the frozen RQIR Hadamard/noise normalization convention. Before QG-008 this sign/factor convention must be cross-checked against the repository definition of `N`.

## 4. Why this is not just three fitted RQIR functions

For fixed `(beta, M_*)`, the same `rho_hat` determines:

- the dispersive shift of the retarded spin-2 response;
- the absorptive part above the spectral threshold;
- the associated Gaussian quantum noise through the spectral relation.

Therefore a future RQIR fit is not allowed to vary response and noise independently.

## 5. Linearized Ward structure

`P2` is transverse on the conserved-source sector. Hence, at the declared linearized level,

`p_m Pi_R^{mn,ab} = 0`

and similarly for the noise kernel. This is the first Ward-compatibility target. It is not a proof of nonlinear diffeomorphism consistency.

Bare coordinate components of `h_mn` are not promoted to physical observables.

## 6. IR and threshold structure

For spacelike momentum define `x = -p^2/M_*^2 >= 0`. Then

`F_E(x) = x int_1^infty ds exp(1-s)/(s+x)`

and analytically

`F_E(x) = x exp(1+x) E1(1+x)`.

Because the spectral density is positive, normalized, and supported on `s >= 1`,

`0 <= F_E(x) <= x/(1+x) < 1`.

Therefore for `beta >= 0`,

`1 + beta F_E(x) >= 1`,

so the v0.1 ansatz has no extra zero of the Euclidean spin-2 kernel on the entire spacelike axis. This is only a scoped Euclidean result; Lorentzian pole/branch-cut unitarity remains open.

At small `x`,

`F_E(x) = A1 x + O(x^2)`,

`A1 = int_1^infty ds exp(1-s)/s = e E1(1) ~= 0.5963473623`.

Thus the deformation vanishes continuously in the IR and the GR pole/residue is unchanged at `p^2 = 0` at this order.

The first nonanalytic threshold occurs at timelike `p^2 = M_*^2` from the support edge of `rho_hat`.

## 7. Required limits

### beta -> 0

Exact return to the perturbative quantum-GR reference kernel.

### |p^2|/M_*^2 -> 0

`F_R -> 0`; classical linearized GR and the C5 quantum-GR propagator are recovered at leading order. The first correction is derivative-suppressed.

### kappa -> 0

Gravity decouples and the matter sector reduces to ordinary relativistic QFT.

### Newtonian/static limit

Target: the massless GR pole and its residue are unchanged, with finite-range/derivative corrections suppressed by powers of momentum over `M_*`. A full source-to-potential normalization audit is still required before QG-003 can PASS.

## 8. RQIR source hierarchy

Matter stress-energy objects remain

`J_mn(x) = <T_mn(x)>`,

`N_mn,ab(x,y) = 1/2 <{delta T_mn(x),delta T_ab(y)}>`,

`chi_T^R = -i theta(x0-y0) <[T(x),T(y)]>`.

The model-specific gravitational transfer is the CTP spin-2 kernel above. The detector-facing response is obtained only after propagating the same source hierarchy through this transfer law. No model-specific detector kernel is inserted by hand.

The first candidate difference direction is

`beta = 0`  : C5 reference,

`beta > 0`  : causal spectral deformation.

At first order,

`delta D_R^(2) = - beta D_GR,R^(2) F_R D_GR,R^(2) K_GR,R^(2) + O(beta^2)`,

or equivalently the exact multiplicative propagator relation

`D_R^(2) = D_GR,R^(2) / [1 + beta F_R]`

within the scoped spin-2 Gaussian sector.

## 9. First discriminator target

The earliest intended fingerprint is a linked pair:

1. a frequency/momentum-dependent ordered-response distortion fixed by `F_R`;
2. an absorptive/noise feature at the same `M_*` fixed by the same spectral density.

A response-only or noise-only distinction is insufficient. RQIR must test whether the joint fingerprint survives exact source calibration, detector nuisance profiling, and applicable stochastic/classical-channel comparators.

## 10. Comparator warning

This ansatz is **not** presently claimed novel. Nonlocal/form-factor gravity, standard EFT nonanalyticities, hidden-sector spectral representations, and other quantum-gravity constructions may reproduce all or part of this structure.

In particular, at energies far below `M_*`, the analytic expansion is expected to be degenerate with higher-dimension operators in ordinary gravitational EFT to finite order. Any novelty can only be assessed after an explicit comparator/prior-art audit in the regime where the full spectral shape matters.

## 11. Rejection conditions

Reject or supersede v0.1 if any of the following occurs:

- a Lorentzian ghost/negative-norm pole is unavoidable in the declared domain;
- no consistent causal/positive dilation exists for the chosen kernel;
- the linearized Ward identity fails after the complete tensor structure is restored;
- the Newtonian/GR/QFT limits fail;
- `beta` is exactly removable by allowed calibration/nuisance transformations;
- the full observable fingerprint is exactly degenerate with an existing comparator class;
- the required physical resource diverges or is undefined for every admissible parameter region.

## 12. Authority and next derivations

Current authority:

- this file;
- `GATE_STATUS.yaml`;
- `ASSUMPTIONS_LEDGER.md`;
- `DERIVATION_MAP.md`;
- `COMPARATOR_STATUS.md`;
- `analysis/candidate_gravity_rqir_ctp_iteration135.py`;
- `docs/CANDIDATE_GRAVITY_RQIR_CTP_ITERATION135.md`.

Next priority is not detector optimization. It is: Lorentzian analytic-structure audit, full conserved-source tensor propagator, and explicit C5/nonlocal-form-factor comparator mapping.