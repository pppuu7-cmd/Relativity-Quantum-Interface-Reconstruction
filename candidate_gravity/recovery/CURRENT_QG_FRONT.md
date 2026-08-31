# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 145**

## Scientific state in one sentence

RQIR has eliminated propagator-only novelty, nonlinearity-only novelty and soft-theorem modification alone as sufficient design principles; it has also shown that broad theory-class capability masks are too unconstrained for a meaningful novelty quotient. The next Candidate Gravity must survive **fixed finite C3/C4/C5/nonlocal/asymptotic-safety tangent matrices** in a symmetry-locked ordered post-Gaussian protocol.

## Frozen model outcomes

### `ANSATZ-PQG-EFT-001`

REFERENCE / NOT PROMOTABLE.

- QG-001/QG-002/QG-003 PASS in the declared low-energy regime.
- QG-007 FAIL due exact C5 identity.

Retained `CG-NG-003`.

### `ANSATZ-RQIR-CTP-001` v0.1

REJECTED.

- Euclidean/spacelike no-zero result PASS_SCOPED.
- Lorentzian continuation forces exactly one extra below-threshold timelike zero for every frozen `beta>0`.
- The additional pole has opposite residue sign in the declared spin-2 convention.

QG-004 FAIL: `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`.

Retained `CG-NG-004`.

### `ANSATZ-RQIR-KL-002` v0.1

REFERENCE / NOT PROMOTABLE.

Scoped results that passed:

- nonnegative Källén–Lehmann spectral measure;
- retarded causal superposition;
- no isolated added continuum pole;
- linear massive-spin-2 conserved-source tensor structure;
- NR `4/3` vDVZ-type factor;
- linked traceless-vs-NR factor `3/4`.

Comparator failures:

1. `CG-NG-005`: strictly below threshold, the added continuum is analytic and finite-order-degenerate with local C5 EFT Wilson coefficients.
2. `CG-NG-006`: at the complete linear-Gaussian level, the positive KL continuum is exactly a direct integral/tower of ordinary positive-norm massive spin-2 quantum mediators. Matching `D_R` and `D_H` gives an identical Gaussian CTP influence functional.

QG-007 FAIL: `EXACT_GAUSSIAN_C4_KK_DEGENERACY`.

No detector/Fisher/resource optimization can repair this exact identity.

## Iterations 142–144 retained design constraints

### Iteration 142 — nonlinear comparator sweep

Known nonlocal gravity, asymptotic-safety vertex expansions, nonlinear massive spin-2 gravity and postquantum classical gravity already contain nonlinear/higher-point structures.

Retained:

- `NG-FUNNEL-001`: nonlinearity alone is not sufficient;
- `NG-FUNNEL-002`: symmetric higher cumulants must be separated from ordered nonlinear response;
- `NG-FUNNEL-003`: Ward/soft locking is necessary but not sufficient for novelty versus C5/covariant QG comparators.

Authority:

`candidate_gravity/landscape/RQIR_NONLINEAR_COMPARATOR_AUDIT_ITERATION142.md`.

### Iteration 143 — post-Gaussian Model→RQIR contract

Future post-Gaussian candidates must derive from one parent dynamics:

- fully symmetrized connected third cumulant `C3_sym`;
- second-order ordered/causal susceptibility `chi^(2)R` built from nested commutators or equivalent CTP components;
- Ward/soft/constraint relations tying higher-point response to the same universal gravitational coupling.

Authority:

`candidate_gravity/POST_GAUSSIAN_MODEL_TO_RQIR_CONTRACT.md`.

### Iteration 144 — finite post-Gaussian quotient

For finite observables `y`, exact hard constraints `H y=h` are eliminated first. Candidate and comparator tangents are projected into `null(H)`.

With

`b=Q_H^T v_beta`,

`M=Q_H^T[V_nuis,V_C3,V_C4,V_C5,V_NL,V_AS,...]`,

the algebraic novelty pre-gate is

`rank([M,b]) > rank(M)`.

Equivalent residual:

`r_beta=(I-MM^+)b`.

Authorities:

- `candidate_gravity/POST_GAUSSIAN_FINITE_QUOTIENT_TEMPLATE.md`;
- `analysis/post_gaussian_quotient_validator_iteration144.py`.

## Iteration 145 — soft locks and class-envelope saturation

### Frozen finite protocol

Full coordinate vector:

`y=(norm,N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft0,soft1,soft2,tensor_geo,threshold)`.

Hard locks:

`norm`, `soft0`, `soft1`.

Reduced coordinates:

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Reduced dimension: `8`.

Authority:

`candidate_gravity/POST_GAUSSIAN_PROTOCOL_ITERATION145.md`.

### NG-FUNNEL-004 — SOFT_LOCK_NOT_NOVELTY

For a future candidate retaining the standard massless-GR/diffeomorphism boundary:

- leading soft behavior is a consistency lock;
- tree-level subleading soft behavior is likewise a protected lock in the declared local-EFT setting;
- local EFT operators can contribute new subsubleading soft-graviton terms.

Therefore `soft0/soft1` are not novelty coordinates and `soft2` must be included explicitly in the finite C5 EFT comparator tangent.

Literature anchors frozen in the Iteration-145 protocol:

- Cachazo & Strominger, arXiv:1404.4091;
- Elvang, Jones & Naculich, arXiv:1611.07534.

### NG-FUNNEL-005 — CLASS_ENVELOPE_SATURATION

A deliberately over-complete diagnostic represented broad C3/C4/C5 theory classes by independent per-coordinate capability axes.

Reproducible authority:

- `analysis/post_gaussian_class_envelope_iteration145.py`;
- `results/post_gaussian_class_envelope_iteration145.json`.

Result:

- C3 capability rank: `7`;
- C4 capability rank: `7`;
- C5 capability rank: `8`;
- combined reduced rank: `8/8`.

Every one-coordinate candidate tangent has zero residual against this intentionally unconstrained envelope.

**Interpretation:** this is not a no-go theorem. It proves that broad theory-class labels cannot be used as comparator tangent matrices because doing so discards each theory's internal parameter relations and Ward identities. From now on comparator blocks must be derivatives of fixed finite realizations/truncations.

## Representative comparator program now frozen

### C3 — postquantum classical gravity

Use a fixed covariant classical–quantum stochastic action/parameterization. Current anchors include arXiv:2402.17844 and arXiv:2605.05375. Unsupported post-Gaussian coordinates remain `BLOCKED`, never zero by assumption.

### C4 — quantum mediator / nonlinear massive spin-2

`ANSATZ-RQIR-KL-002` remains the exact Gaussian continuum control. A nonlinear C4 tangent requires a separately frozen finite massive-spin-2/dRGT-style realization.

### C5 — perturbative quantum GR EFT

Use the C5 reference boundary augmented to the declared post-Gaussian order:

- Einstein-Hilbert tree nonlinearities;
- required loop/nonanalytic contributions at the same order;
- finite local diffeomorphism-invariant EFT operator basis through the first order capable of changing selected `soft2`/finite-momentum coordinates.

### Nonlocal gravity

Use one fixed covariant nonlocal action, not the class label.

### Asymptotic safety

Use one fixed vertex truncation with finite parameterization. A suitable authority class is Pawlowski & Tränkle, arXiv:2309.17043, with momentum-dependent three-/four-graviton vertices and reconstructed effective action.

## Article material

Current article scaffolds:

- `docs/CANDIDATE_GRAVITY_ARTICLE_FUNNEL_SECTION_ITERATION137.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION145.md`.

The article-safe distinction remains mandatory:

- genuine consistency rejection;
- exact comparator/novelty failure;
- regime-specific non-identifiability;
- comparator-instantiation blocking;
- absence of a novelty certificate.

Do not call the latter categories global falsification of an existing theory.

## `ANSATZ-003` design state

Still intentionally **not frozen**.

It may not be created merely by adding:

- a new propagator;
- a nonzero third cumulant;
- a generic nonlinear vertex;
- a leading/subleading soft modification;
- an order-sensitive response coordinate without fixed comparator subtraction.

Minimum eventual package remains:

1. one parent dynamics generating lower- and higher-point sectors;
2. exact C5 boundary at `beta=0`;
3. no unsupported two-point novelty claim;
4. derived symmetric post-Gaussian object;
5. derived ordered nonlinear response;
6. Ward/soft lock;
7. fixed C3/C4/C5/nonlocal/AS comparator subtraction;
8. nonzero finite RQIR residual before Fisher/resources.

## Immediate next scientific priority — Iteration 146

Instantiate the first **physical finite C5 post-Gaussian tangent**.

Required order:

1. freeze perturbative/EFT order and renormalization convention;
2. freeze finite kinematics for the Iteration-145 observable protocol;
3. derive Einstein-Hilbert tree contribution to nonlinear response/soft locks;
4. add the finite local EFT directions capable of modifying `soft2` and finite-momentum response;
5. include loop/nonanalytic columns or explicitly label them `BLOCKED` where not yet derived;
6. produce the first actual `V_C5`, its rank, SVD tolerance and authority map;
7. only then instantiate C3 and nonlinear C4 representative tangents.

No Fisher/resource work and no `ANSATZ-003` promotion before this comparator foundation is finite.