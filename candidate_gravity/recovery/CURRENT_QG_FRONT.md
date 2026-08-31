# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Reference model:** `ANSATZ-PQG-EFT-001` v0.1, REFERENCE / NOT PROMOTABLE  
**Rejected discovery model:** `ANSATZ-RQIR-CTP-001` v0.1  
**Active discovery model:** `ANSATZ-RQIR-KL-002` v0.1, DRAFT / TESTING  
**Authoritative Candidate Gravity front:** **Iteration 140**

## Branch chronology

- Iterations 1–132: RQIR Papers I–III and Candidate Gravity testing infrastructure closed.
- Iteration 133: instantiated standard perturbative quantum-GR EFT as C5 reference.
- Iteration 134: passed its Newtonian/classical-GR normalization gate.
- Iteration 135: created first RQIR-driven causal spectral inverse-kernel ansatz.
- Iteration 136: rejected that ansatz analytically on the Lorentzian pole/residue gate.
- Iteration 137: audited major existing gravity model classes through the RQIR funnel and prepared an article-ready comparison section.
- Iteration 138: created the second RQIR-driven ansatz using a nonnegative Källén–Lehmann massless-plus-continuum spectral measure.
- Iteration 139: restored the linear conserved-source tensor structure and exposed the linked vDVZ `4/3` and traceless/NR `3/4` relations.
- Iteration 140: proved strictly below-threshold finite-order EFT degeneracy with C5 Wilson-coefficient freedom.

## Retained reference result — C5

`ANSATZ-PQG-EFT-001` remains the permanent perturbative-QG control.

- QG-001/QG-002/QG-003 PASS in the declared low-energy domain.
- QG-007 FAIL for novelty because the model is exactly comparator C5.

**CG-NG-003:** quantizing the weak-field metric within standard perturbative quantum-GR EFT does not itself create a new Candidate Gravity direction relative to C5.

## Rejected model result — Iteration 136

`ANSATZ-RQIR-CTP-001` v0.1 used a multiplicative inverse-kernel factor `1+beta F_R` with positive spectral input.

Although the Euclidean/spacelike kernel had no extra zero, for positive-frequency timelike

`y=p^2/M_*^2 in (0,1)`

the frozen form factor is

`F(y)=-y exp(1-y)E1(1-y)`.

It decreases continuously from `0` to `-infinity`. Therefore for every `beta>0`,

`1+beta F(y)=0`

has exactly one sub-threshold root. The dressed-pole residue factor is negative relative to the frozen GR pole convention because `F'(y)<0`.

**QG-004 FAIL — `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`.**

**CG-NG-004:** Euclidean no-extra-zero stability does not guarantee Lorentzian viability for a positive-beta Stieltjes-type inverse-kernel deformation.

The model is permanently REJECTED; its sign/shape is not retuned post hoc.

## Existing-model funnel audit — Iteration 137

Current landscape interpretation:

- semiclassical mean gravity: early C1 comparator; mean-only closure is insufficient for a full quantum-interface claim;
- stochastic gravity: strong C2 late comparator because CTP/influence-functional mean/noise/dissipation structure is already sophisticated;
- classical-channel/measurement-feedback gravity: C3 comparator capable of Newtonian interaction plus compulsory decoherence/noise;
- postquantum classical gravity: high-priority modern C3 comparator; stochastic metric and consistency properties are realization-dependent;
- perturbative quantum GR: C5 viable reference but novelty-degenerate;
- ghost-free nonlocal/form-factor gravity: serious quantum comparator that can pass early pole/positivity gates for specific fixed form factors;
- asymptotic safety: program-level prior; a concrete Lorentzian effective realization is required before finite RQIR testing.

Authority:

`candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`

and

`docs/CANDIDATE_GRAVITY_ARTICLE_FUNNEL_SECTION_ITERATION137.md`.

## Active model — `ANSATZ-RQIR-KL-002` v0.1

### Spectral definition

The active model uses a massless GR pole plus a smooth nonnegative continuum:

`rho_g(mu^2)=delta(mu^2)+(beta/M_*^2) exp(1-mu^2/M_*^2) Theta(mu^2-M_*^2)`.

At the Gaussian two-point level this yields:

- nonnegative spectral weight;
- retarded causal superposition;
- no isolated additional continuum pole;
- a branch cut beginning at `p^2=M_*^2`.

### Linear tensor completion

For conserved sources:

massless GR:

`T.T'-(1/2)TT'`,

massive continuum:

`T.T'-(1/3)TT'`.

Hence for two nonrelativistic sources the continuum/GR tensor ratio is

`4/3`.

The static potential is

`Phi(r)=-GM/r [1+(4/3)beta W(M_*r)]`,

with

`0<W(u)<=exp(-u)`.

For a traceless probe the continuum/massless tensor ratio is `1`, so after NR calibration the relative continuum response is fixed at `3/4`.

These linked tensor relations are candidate fingerprint components, not novelty claims.

### C5 infrared degeneracy

For Euclidean `x=q^2/M_*^2`, the continuum function

`C(x)=int_1^infty ds rho_hat(s)/(s+x)`

has the convergent expansion

`C(x)=sum_{n>=0}(-x)^n A_(n+1)`

for `|x|<1`.

Therefore at any fixed finite derivative order strictly below threshold, the beta contribution lies in the local gravitational EFT Wilson-coefficient span.

**CG-NG-005:** a gapped positive spectral continuum is not distinguishable from C5 plus local Wilson-coefficient freedom in a strictly below-threshold finite-order EFT measurement.

Consequently deep-IR detector/Fisher optimization is forbidden as scientifically non-identifying.

## Active gate state

For `ANSATZ-RQIR-KL-002`:

- QG-001 PARTIAL;
- QG-002 PASS;
- QG-003 PARTIAL;
- QG-004 PASS_SCOPED;
- QG-005 PARTIAL with linear tensor structure closed, nonlinear constraints open;
- QG-006 PARTIAL;
- QG-007 PARTIAL_NEGATIVE: C5 deep-IR distinctness failed, threshold/cross-channel distinction open;
- QG-008 BLOCKED_REGIME until a threshold-resolved/cross-channel finite map is built;
- QG-009/QG-010 BLOCKED.

## Canonical authorities — active branch

Read:

1. `candidate_gravity/models/ANSATZ-RQIR-KL-002/MODEL.md`;
2. `candidate_gravity/models/ANSATZ-RQIR-KL-002/GATE_STATUS.yaml`;
3. `candidate_gravity/models/ANSATZ-RQIR-KL-002/ASSUMPTIONS_LEDGER.md`;
4. `candidate_gravity/models/ANSATZ-RQIR-KL-002/DERIVATION_MAP.md`;
5. `candidate_gravity/models/ANSATZ-RQIR-KL-002/COMPARATOR_STATUS.md`;
6. `docs/CANDIDATE_GRAVITY_POSITIVE_SPECTRAL_ITERATION138.md`;
7. `docs/CANDIDATE_GRAVITY_TENSOR_ITERATION139.md`;
8. `docs/CANDIDATE_GRAVITY_C5_IR_DEGENERACY_ITERATION140.md`;
9. `analysis/candidate_gravity_positive_spectral_iteration138.py`;
10. `analysis/candidate_gravity_tensor_projector_iteration139.py`;
11. `analysis/candidate_gravity_c5_ir_degeneracy_iteration140.py`;
12. corresponding JSON result files.

## Immediate next scientific priority

**Iteration 141: C5-excess and strongest-continuum comparator gate.**

Before Paper-I/Fisher work:

1. freeze a declared perturbative order for the C5 retarded/spectral baseline;
2. redefine the scientifically tested direction as **excess spectral weight over C5**, so `beta=0` is exactly the chosen C5 reference, not only tree GR;
3. compare threshold support/tensor structure against hidden/KK/DGP-like massive-spin-2 continua and nonlocal/form-factor gravity;
4. determine whether the linked `4/3` NR, `3/4` traceless, threshold absorption and noise relations contain any residual direction outside those comparator families;
5. only if such a direction exists, construct the finite RQIR Paper-I quotient.

Do not spend detector optimization resources on a direction still contained in the comparator span.
