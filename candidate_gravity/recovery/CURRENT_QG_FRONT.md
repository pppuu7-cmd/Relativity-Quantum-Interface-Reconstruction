# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral comparator control:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none after Iteration 141  
**Authoritative Candidate Gravity front:** **Iteration 141**

## Scientific state in one sentence

RQIR has now eliminated two naive routes to a new gravity model: an inverse-kernel spectral deformation failed Lorentzian consistency, while a positive KL continuum survived consistency but proved exactly equivalent at Gaussian level to an ordinary mediator continuum. The next model must therefore contain a derived nonlinear/non-Gaussian gravity-specific relation.

## Frozen model outcomes

### `ANSATZ-PQG-EFT-001`

REFERENCE / NOT PROMOTABLE.

- QG-001/QG-002/QG-003 PASS in the declared low-energy regime.
- QG-007 FAIL due exact C5 identity.

Retained result `CG-NG-003`.

### `ANSATZ-RQIR-CTP-001` v0.1

REJECTED.

- Euclidean/spacelike no-zero result passed.
- Lorentzian sub-threshold analysis forces exactly one extra timelike zero for every frozen `beta>0`.
- Relative residue sign is opposite to the massless GR pole convention.

QG-004 FAIL: `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`.

Retained result `CG-NG-004`.

### `ANSATZ-RQIR-KL-002` v0.1

REFERENCE / NOT PROMOTABLE.

Scoped physics that passed:

- nonnegative Källén–Lehmann spectral measure;
- retarded causal spectral superposition;
- no isolated added continuum pole;
- linear conserved-source massive-spin-2 tensor structure;
- NR continuum/GR tensor factor `4/3`;
- linked traceless-vs-NR factor `3/4`.

Comparator failures:

1. **C5 deep-IR degeneracy** — below threshold, the continuum has a convergent local derivative expansion and lies in the finite-order EFT Wilson-coefficient span (`CG-NG-005`).
2. **Exact Gaussian C4/KK degeneracy** — the KL continuum is exactly representable as a direct integral/tower of positive massive spin-2 quantum mediators. With linear stress coupling, identical `D_R` and `D_H` imply identical Gaussian CTP influence functionals (`CG-NG-006`).

Therefore QG-007 FAIL: `EXACT_GAUSSIAN_C4_KK_DEGENERACY`.

No Fisher/resource optimization may be used to rescue this exact identity.

## Existing-model funnel audit

First-wave audited classes:

- semiclassical mean gravity — early C1 comparator;
- stochastic gravity — strong C2 comparator;
- classical-channel/measurement-feedback gravity — C3 control;
- postquantum classical gravity — high-priority modern C3 comparator;
- perturbative quantum GR — C5 reference;
- ghost-free nonlocal/form-factor gravity — serious quantum comparator;
- asymptotic safety — requires a concrete effective realization before finite RQIR testing.

Authorities:

- `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_FUNNEL_SECTION_ITERATION137.md`.

## Why the next ansatz must be nonlinear/non-Gaussian

A model specified only by a Gaussian two-point propagator/noise kernel can be represented by an ordinary Gaussian mediator environment whenever its spectral measure is positive. RQIR therefore cannot certify gravity-specific novelty from `J/N/chi` at the Gaussian linear level alone if an allowed C4 mediator reproduces the complete influence functional.

The next candidate must derive at least one additional gravity-specific object from the same dynamics, for example:

- connected gravitational three-point response/cumulant;
- nonlinear stress-energy self-coupling fixed by diffeomorphism/Ward bootstrap;
- a constraint/relational identity tying higher response to the two-point sector;
- a universal self-coupling relation not independently tunable like a hidden mediator interaction.

## Canonical authorities for the latest negative results

- `docs/CANDIDATE_GRAVITY_LORENTZIAN_ITERATION136.md`;
- `docs/CANDIDATE_GRAVITY_C5_IR_DEGENERACY_ITERATION140.md`;
- `docs/CANDIDATE_GRAVITY_C4_GAUSSIAN_DEGENERACY_ITERATION141.md`;
- `analysis/candidate_gravity_lorentzian_iteration136.py`;
- `analysis/candidate_gravity_c5_ir_degeneracy_iteration140.py`;
- `analysis/candidate_gravity_gaussian_c4_equivalence_iteration141.py`;
- corresponding JSON results.

## Immediate next scientific priority — Iteration 142

Before inventing `ANSATZ-003`, audit existing **nonlinear/nonlocal gravity models** against the exact requirement exported by `CG-NG-006`.

Priority comparator tests:

1. a fixed ghost-free entire-form-factor/nonlocal gravity model — determine whether its nonlinear vertices are fixed by the same covariant action and whether RQIR higher connected response adds information beyond a mediator continuum;
2. a concrete asymptotic-safety effective form-factor realization — test whether a Lorentzian higher-point object can be frozen operationally;
3. nonlinear massive-gravity/KK examples — identify which self-coupling/constraint relations remain distinguishable from generic hidden spin-2 mediators;
4. modern postquantum classical gravity — determine which higher stochastic cumulants/constraint relations can mimic nonlinear quantum-gravity signatures.

Only after this comparator sweep should the next RQIR-driven nonlinear ansatz be frozen.
