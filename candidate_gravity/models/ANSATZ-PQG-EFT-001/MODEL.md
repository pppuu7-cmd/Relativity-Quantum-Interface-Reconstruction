# ANSATZ-PQG-EFT-001 — perturbative quantum GR EFT reference

**Version:** 0.1  
**Status:** REFERENCE / TESTING  
**Purpose:** first real Candidate-Gravity branch object used to exercise the frozen QG gate process. This is deliberately a standard low-energy perturbative quantum-gravity EFT reference, not a new theory claim.

## 1. Physical state space — QG-001 target

Background split

`g_mn = eta_mn + kappa h_mn`, with `kappa = sqrt(32 pi G)`.

Matter is a real scalar field `phi` of mass `m`.

Perturbative kinematic state space is the tensor product of the matter Fock space and the gauge-fixed graviton Fock/BRST space about asymptotically Minkowski boundary conditions. Physical states are the BRST cohomology / equivalently the positive-norm transverse physical graviton sector after the linearized diffeomorphism constraints are imposed. Gauge components of `h_mn` are not detector observables.

Declared physical observables are gauge-invariant asymptotic scattering data and, for the weak-field RQIR limit, relationally specified smeared matter stress-energy observables and gauge-invariant detector response combinations. A bare coordinate component `h_mn(x)` is not by itself promoted to an RQIR observable.

## 2. Primary dynamics — QG-002 target

Core low-energy action

`S = integral d^4x sqrt(-g) [ 2 R/kappa^2 - 1/2 g^mn partial_m phi partial_n phi - 1/2 m^2 phi^2 ] + S_GF + S_ghost + S_EFT`.

`S_GF` is a declared covariant gauge-fixing term, `S_ghost` the associated Faddeev-Popov/BRST ghost action, and `S_EFT` contains higher-curvature and higher-dimension operators allowed by diffeomorphism invariance, ordered by powers of `E/M_Pl` and curvature over `M_Pl^2`.

Expanding to first order in `h_mn` gives the universal matter-gravity interaction

`S_int^(1) = -(kappa/2) integral d^4x h_mn T^(mn)`

(up to the stated index/sign convention), so the source hierarchy is not inserted by hand: it originates from the same stress tensor that appears in the covariant action.

Evolution is closed and unitary within the perturbative EFT domain before tracing out sectors. Open-system influence functionals used by RQIR arise only after explicit partial tracing/coarse graining.

## 3. Constraint / gauge structure

Gauge symmetry is perturbative diffeomorphism invariance. The gauge-fixed representation is computational only. BRST physical-state conditions remove gauge/ghost states from the physical spectrum. A later RQIR-facing derivation must express detector/source objects in gauge-invariant or relational form before a QG-005 PASS can be recorded.

**Current state:** structure specified; full RQIR observable gauge audit not yet completed.

## 4. Domain of validity

- weak field: `|kappa h| << 1`;
- perturbative momenta/energies well below the Planck scale;
- curvatures small in Planck units;
- asymptotically Minkowski reference branch for this version;
- EFT predictions retained only to an explicitly declared order in `kappa`, loops and higher-dimension operators.

This is not a UV completion.

## 5. Required limits

Tasks retained for later gates:

- tree-level static exchange -> Newtonian potential;
- coherent/classical graviton limit -> linearized GR;
- `kappa -> 0` -> ordinary scalar QFT/QM sector;
- flat-background limit -> ordinary relativistic QFT;
- coarse-grained matter influence functional -> semiclassical/stochastic structures where appropriate.

No QG-003/QG-006 PASS is claimed in this iteration merely because these limits are standard expectations.

## 6. Probability / consistency structure

The underlying gauge-fixed EFT is treated as a standard perturbative quantum field theory with BRST physical-state projection. Unitarity/positivity is asserted only inside the EFT perturbative domain and requires the usual order-by-order gauge/renormalization consistency. QG-004 and cross-gates remain NOT_TESTED until repository derivations are attached.

## 7. RQIR source hierarchy from the same dynamics

At linearized order the matter stress tensor generates the gravitational source. For a declared matter state `rho_m`:

`J_mn(x) = Tr[rho_m T_mn(x)]`.

Centered symmetrized noise:

`N_mn,ab(x,y) = 1/2 <{delta T_mn(x), delta T_ab(y)}>`.

Retarded response:

`chi^R_mn,ab(x,y) = -i theta(x0-y0) <[T_mn(x),T_ab(y)]>`

with units restored by `hbar` where required by convention.

Higher connected stress-tensor correlators come from the same Schwinger-Keldysh/CTP generating functional of the matter sector coupled to the metric perturbation. Renormalization and smearing conventions must be frozen before these are propagated into an RQIR numerical discriminator.

## 8. Comparator result — first negative gate

This ansatz is deliberately the standard low-energy perturbative quantum-gravity EFT class represented by comparator **C5** in `candidate_gravity/BASELINE_COMPARATORS.md`.

Therefore there is no model-specific discriminator against C5:

`ANSATZ-PQG-EFT-001 == C5` at the declared theory-class level.

Hence **QG-007 = FAIL (REFERENCE_DEGENERACY_C5)** for promotion as an independently new Candidate Gravity model.

This is an intended negative result, not a failure of the infrastructure. The ansatz is retained as a reference/control model for future candidates.

## 9. RQIR propagation status

- Paper-I hierarchy mapping: structurally defined, numerical finite discriminator not yet instantiated for this model;
- Paper-II `F_beta|theta`: not run because there is no independent beta direction versus C5;
- Paper-III resources: not run for a nonexistent C5-distinguishing beta direction.

A future new candidate must differ from this reference at a derived observable level before consuming detector-optimization resources.

## 10. Falsification / rejection conditions

For this reference version, reject any claimed extension if it:

- treats gauge components as physical detector signals;
- violates perturbative BRST/gauge consistency;
- fails its declared low-energy GR/Newtonian/QFT limits;
- introduces `J`, `N`, `chi^R` independently rather than deriving them from the action;
- claims novelty while remaining exactly within comparator C5.

## 11. Literature anchors

- J. F. Donoghue, *General relativity as an effective field theory: The leading quantum corrections*, Phys. Rev. D 50, 3874 (1994), arXiv:gr-qc/9405057.
- J. F. Donoghue, *The effective field theory treatment of quantum gravity*, arXiv:1209.3511.
- B. L. Hu and E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Rev. Relativity / arXiv:0802.0658, for the CTP/noise-kernel/stochastic comparator mapping.

These are prior-art/reference anchors, not evidence of a new RQIR model.

## 12. Iteration-133 authority

See:

- `candidate_gravity/models/ANSATZ-PQG-EFT-001/GATE_STATUS.yaml`;
- `candidate_gravity/models/ANSATZ-PQG-EFT-001/ASSUMPTIONS_LEDGER.md`;
- `candidate_gravity/models/ANSATZ-PQG-EFT-001/DERIVATION_MAP.md`;
- `analysis/candidate_gravity_reference_ansatz_iteration133.py`;
- `docs/CANDIDATE_GRAVITY_REFERENCE_ANSATZ_ITERATION133.md`.
