# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 146**

## Scientific state in one sentence

The broad-class novelty quotient is replaced by fixed comparator realizations. Iteration 146 produced the first finite rank-certified C5 local-EFT Wilson tangent at frozen kinematics, but also proved that an on-shell amplitude tangent is not yet the ordered CTP/retarded RQIR tangent; the full C5 post-Gaussian embedding is therefore operationally BLOCKED rather than falsely completed.

## Frozen model outcomes

### `ANSATZ-PQG-EFT-001`

REFERENCE / NOT PROMOTABLE.

- QG-001/QG-002/QG-003 PASS in the declared low-energy regime.
- QG-007 FAIL due exact C5 identity.
- Retain `CG-NG-003`.

### `ANSATZ-RQIR-CTP-001` v0.1

REJECTED.

- Euclidean/spacelike no-zero result PASS_SCOPED.
- Lorentzian continuation produces an extra below-threshold timelike pole with opposite residue sign.
- QG-004 FAIL: `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`.
- Retain `CG-NG-004`.

### `ANSATZ-RQIR-KL-002` v0.1

REFERENCE / NOT PROMOTABLE.

- positive Källén–Lehmann spectral measure and causal retarded superposition;
- linear massive-spin-2 conserved-source structure;
- deep-IR finite-order degeneracy with local C5 EFT (`CG-NG-005`);
- exact Gaussian direct-integral/tower C4 identity (`CG-NG-006`).

QG-007 FAIL: `EXACT_GAUSSIAN_C4_KK_DEGENERACY`.

## Frozen post-Gaussian protocol from Iterations 143–145

Full coordinates:

`y=(norm,N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft0,soft1,soft2,tensor_geo,threshold)`.

Hard locks:

`norm`, `soft0`, `soft1`.

Reduced coordinates:

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Reduced dimension: `8`.

Candidate novelty pre-gate after exact hard-constraint reduction:

`rank([M,b]) > rank(M)`

or equivalently nonzero

`r_beta=(I-MM^+)b`.

Retained funnel results:

- `NG-FUNNEL-001`: nonlinearity alone is not sufficient;
- `NG-FUNNEL-002`: symmetric higher cumulants must be separated from ordered nonlinear response;
- `NG-FUNNEL-003`: Ward/soft locking is necessary but not sufficient;
- `NG-FUNNEL-004`: `soft0/soft1` are consistency locks, not novelty coordinates;
- `NG-FUNNEL-005`: broad C3/C4/C5 capability masks saturate the 8D space and are therefore unusable as physical comparator tangents.

## Iteration 146 — first fixed finite C5 tangent

### Frozen C5 realization

- D=4 low-energy perturbative GR EFT;
- Einstein-Hilbert boundary;
- parity-even local tree-level four-graviton operator basis through dimension 12;
- explicit finite basis/amplitudes from de Rham, Jaitly & Tolley, arXiv:2212.04975;
- linear Wilson coordinates
  `theta_C5=(c3,c_plus,c_minus,e_plus,e_minus,f_plus,f_minus,g_plus,g_minus,j1)`;
- twelve frozen sub-cutoff kinematic/polarization points.

### Rank/SVD certificate

The analytic amplitude fingerprint matrix

`V_amp=d(M_Pl^2 A)/d theta_C5`

has shape `12 x 10` and rank **10/10**.

Singular values:

`3.77624716e-1, 7.94667137e-2, 9.08015595e-3, 9.16415267e-4, 4.72836512e-4, 2.33370720e-5, 1.72727839e-5, 2.13079285e-6, 1.03238331e-6, 9.27010447e-7`.

`s_min/s_max = 2.4548457953351053e-6`.

Authorities:

- `analysis/c5_tree_eft_tangent_iteration146.py`;
- `results/c5_tree_eft_tangent_iteration146.json`;
- `candidate_gravity/C5_FINITE_TANGENT_ITERATION146.md`.

### NG-FUNNEL-006 — ON_SHELL_TANGENT_NOT_RQIR_TANGENT

The above is a genuine finite physical local-EFT tangent, but it is an **on-shell S-matrix** tangent. The Iteration-145 quotient requires causal ordered `chi^(2)R`, `N2` and `C3sym` from one CTP/state convention.

Therefore the following are explicitly **BLOCKED**, not zero:

- direct `chi2R_even/odd` embedding;
- `N2` and `C3sym` rows;
- loop/nonanalytic C5 columns in the same RQIR convention.

Donoghue's low-energy gravitational EFT result makes the nonanalytic massless-loop sector physically mandatory at the perturbative orders where it enters; it may not be absorbed into arbitrary local Wilson directions.

This is an operational comparator-instantiation blocker, not a consistency FAIL of C5.

## Representative comparator program

### C3 — postquantum classical gravity

Use one fixed covariant classical–quantum stochastic action/parameterization. Unsupported post-Gaussian response entries remain `BLOCKED`, never assumed zero.

### C4 — nonlinear quantum mediator / massive spin-2

`ANSATZ-RQIR-KL-002` remains the Gaussian control. A nonlinear C4 tangent requires a separately frozen finite interacting massive-spin-2 realization.

### C5 — perturbative quantum GR EFT

Local tree-level tangent is now finite/rank-certified. Next required piece is the explicit retarded/CTP embedding at the frozen kinematics, followed by required loop/nonanalytic columns.

### Nonlocal gravity / asymptotic safety

Still require one fixed action/truncation each; program labels are not finite comparators.

## `ANSATZ-003` design state

Still intentionally **not frozen**.

It may not be created merely by adding a new propagator, nonzero third cumulant, generic nonlinear vertex, soft modification, or order-sensitive response coordinate. A concrete target must first survive fixed C3/C4/C5/nonlocal/AS comparator subtraction and leave a nonzero algebraic residual before Fisher/resources.

## Article material

Current article scaffolds include:

- `docs/CANDIDATE_GRAVITY_ARTICLE_FUNNEL_SECTION_ITERATION137.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION145.md`;
- Iteration-146 update should retain the new distinction `ON_SHELL_TANGENT_NOT_RQIR_TANGENT`.

Always distinguish consistency FAIL, exact comparator identity, regime-specific non-identifiability, comparator-instantiation BLOCKED and absence of novelty certificate.

## Immediate next scientific priority — Iteration 147

Derive the first **retarded C5 nonlinear-response embedding**.

Required order:

1. freeze one CTP state and real-time prescription;
2. derive a minimal finite retarded three-point/nonlinear-response sub-block from the same EH + local-EFT action;
3. normalize it into the Iteration-145 `chi2R` convention at the frozen finite kinematics;
4. verify the corresponding Ward/soft relation;
5. add loop/nonanalytic columns where derived, otherwise keep them explicitly `BLOCKED`;
6. only after this C5 retarded block exists, proceed to fixed C3 and nonlinear C4 tangents.

No Fisher/resource work and no `ANSATZ-003` promotion before a nonzero algebraic residual survives the concrete comparator quotient.
