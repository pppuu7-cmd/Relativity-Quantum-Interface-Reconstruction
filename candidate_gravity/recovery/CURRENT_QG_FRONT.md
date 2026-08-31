# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending post-Gaussian design closure  
**Authoritative Candidate Gravity front:** **Iteration 144**

## Scientific state in one sentence

RQIR has eliminated propagator-only novelty and nonlinearity-only novelty as sufficient design principles. The next Candidate Gravity must expose a **symmetry-locked ordered nonlinear/non-Gaussian response**, derived with the lower-point sector from one dynamics and surviving C3/C4/C5/nonlocal/asymptotic-safety comparator subtraction.

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

## Iteration 142 — nonlinear comparator sweep

The strongest existing nonlinear classes were checked against the design requirement exported by `CG-NG-006`.

### Weakly nonlocal / form-factor gravity

A fixed covariant nonlocal action can simultaneously define the propagator and momentum-dependent nonlinear graviton vertices. Therefore `Gamma^(3) != 0` or a momentum-dependent cubic vertex is not a unique candidate signature.

### Asymptotic safety

Concrete functional-RG vertex expansions already compute momentum-dependent graviton `Gamma^(2)`, `Gamma^(3)` and `Gamma^(4)` objects, and effective actions can be reconstructed from multi-graviton correlation functions. A future candidate must compare against a frozen concrete truncation, not only tree GR.

### dRGT / nonlinear massive spin-2

Nonlinear spin-2 self-interactions can be highly constrained and ghost-free rather than arbitrary. Nonlinearity alone therefore does not distinguish gravity-specific physics from strong massive-spin-2 comparators.

### Postquantum classical gravity

Classical–quantum path-integral theories generate stochastic nonlinear dynamics, decoherence/diffusion, constraints and potentially non-Gaussian classical metric statistics. A nonzero symmetric bispectrum is not by itself evidence for a quantum metric.

Authority:

`candidate_gravity/landscape/RQIR_NONLINEAR_COMPARATOR_AUDIT_ITERATION142.md`.

Retained design results:

- `NG-FUNNEL-001`: nonlinearity alone is not sufficient;
- `NG-FUNNEL-002`: symmetric higher cumulants must be separated from ordered nonlinear response;
- `NG-FUNNEL-003`: Ward/soft locking is necessary to reduce generic mediator freedom but is not by itself sufficient for novelty versus C5/covariant QG comparators.

## Iteration 143 — post-Gaussian Model→RQIR contract

The interface has been extended beyond `J`, two-point `N` and linear `chi^R`.

Future candidates whose novelty is post-Gaussian must additionally derive from the same parent dynamics:

### Fully symmetrized connected third cumulant

`C3_sym(A,B,C)=(1/6) sum_{pi in S3}<delta A_pi1 delta A_pi2 delta A_pi3>_c`.

This can be reproduced by a classical non-Gaussian random field and is therefore not sufficient alone.

### Second-order causal/ordered susceptibility

`chi^(2)R_{A;BC}(t;t1,t2)`

is defined by the appropriately time-ordered sum of nested commutators such as

`(-i/hbar)^2 theta(t-t1)theta(t1-t2)<[[A(t),B(t1)],C(t2)]>`

plus the exchanged source ordering.

The candidate must also expose the corresponding independent CTP/Keldysh three-point components and their causal/normalization structure.

### Ward / soft / constraint lock

The higher-point objects must satisfy a diffeomorphism Ward/Slavnov–Taylor identity, constraint-algebra relation, relational identity, or controlled soft-graviton consistency relation that ties them to the same universal gravitational coupling.

Authority:

`candidate_gravity/POST_GAUSSIAN_MODEL_TO_RQIR_CONTRACT.md`.

## Iteration 144 — finite post-Gaussian quotient infrastructure

A model-independent finite quotient has now been specified before choosing `ANSATZ-003`.

For a finite observable vector

`y=(mean, two-point symmetric, linear response, third symmetric cumulant, second-order ordered response, Ward/soft tests, ...)`,

exact hard constraints are represented by

`H y=h`.

Candidate and comparator tangents are projected into `null(H)` before any profiling.

With reduced candidate direction

`b=Q_H^T v_beta`

and combined nuisance/comparator matrix

`M=Q_H^T[V_nuis,V_C3,V_C4,V_C5,V_NL,V_AS,...]`,

the algebraic novelty pre-gate is

`rank([M,b]) > rank(M)`.

The residual

`r_beta=(I-MM^+)b`

must exceed the numerical/modeling error bound. Symmetric and ordered residual components are recorded separately so that a purely classical-cumulant residual is not mistaken for an ordered quantum signature.

Authorities:

- `candidate_gravity/POST_GAUSSIAN_FINITE_QUOTIENT_TEMPLATE.md`;
- `analysis/post_gaussian_quotient_validator_iteration144.py`.

This is an algebraic pre-Fisher gate only; it does not prove physical consistency or resource feasibility.

## Existing-model/article material

Article scaffolds now exist:

- `docs/CANDIDATE_GRAVITY_ARTICLE_FUNNEL_SECTION_ITERATION137.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION143.md`.

The article matrix distinguishes:

- genuine consistency rejection;
- exact comparator/novelty failure;
- regime-specific non-identifiability;
- operational/model-instantiation blocking.

Do not call the latter categories global falsification of an existing theory.

## Current model-design specification for `ANSATZ-003`

Do **not** freeze the third ansatz until all of the following can be stated in one model definition:

1. **One parent dynamics** generating `Gamma^(2)`, `Gamma^(3)` and matter coupling.
2. **Exact C5 boundary:** `beta=0` returns a frozen perturbative-QG baseline at the same order.
3. **No two-point novelty claim:** Gaussian sector is treated as comparator-degenerate unless separately proved distinct.
4. **Derived higher connected object:** at least one `C3`/higher structure not independently tunable from lower-point dynamics.
5. **Ordered nonlinear response:** a nested-commutator/causal second-order susceptibility or equivalent CTP vertex.
6. **Ward/soft lock:** higher response tied to universal stress-energy coupling by the same gravity symmetry/constraints.
7. **Strong comparator subtraction:** C5 higher EFT/loops, fixed nonlocal gravity, concrete asymptotic-safety vertices, nonlinear massive/KK spin-2, and postquantum classical higher statistics/response.
8. **Finite RQIR quotient:** only the residual direction outside calibration/nuisance/comparator span proceeds to Fisher/resources.

## Immediate next scientific priority — Iteration 145

Begin constructing `ANSATZ-003` only in the **residual post-Gaussian space** defined by Iteration 144:

1. freeze a concrete C5 higher-point baseline order and finite observable protocol;
2. instantiate first comparator tangent matrices for C3/C4/C5;
3. identify which Ward/soft-locked ordered component is not automatically inside those spans;
4. choose the minimal covariant parent dynamics capable of generating exactly that residual rather than adding arbitrary new kernels;
5. reject the proposed dynamics before promotion if its formal tangent is already contained in a known nonlocal/asymptotic-safety/massive-spin-2 comparator family.

This reverses the usual workflow: **first identify the residual observable direction, then construct the minimal dynamics that can generate it**.
