# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 148**

## Scientific state in one sentence

Iteration 148 proved that the Iteration-146 on-shell/EOM-reduced C5 Wilson basis cannot by itself define a basis-independent off-shell `chi^(2)R` tangent: local field redefinitions change coordinate response functions, and physical equivalence is restored only after the induced observable/source contact map is included. The first numerical C5 retarded rank is therefore `BLOCKED_SOURCE_COMPLETION`, not zero and not a C5 consistency FAIL.

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

Hard locks: `norm`, `soft0`, `soft1`.

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
- `NG-FUNNEL-005`: broad C3/C4/C5 capability masks saturate the 8D space and are unusable as physical comparator tangents;
- `NG-FUNNEL-006`: an on-shell amplitude tangent is not automatically the ordered CTP/retarded RQIR tangent;
- `NG-FUNNEL-007`: on-shell four-point kinematics do not uniquely fix the off-shell retarded three-point protocol;
- `NG-FUNNEL-008`: an on-shell/EOM-reduced EFT basis is not automatically a basis-independent off-shell response basis; operational source/observable completion is mandatory.

## Iteration 146 — finite local C5 on-shell tangent

Frozen C5 realization:

- D=4 low-energy perturbative GR EFT;
- Einstein-Hilbert boundary;
- parity-even local tree-level four-graviton operator basis through dimension 12;
- linear Wilson coordinates `theta_C5=(c3,c_plus,c_minus,e_plus,e_minus,f_plus,f_minus,g_plus,g_minus,j1)`;
- twelve frozen sub-cutoff on-shell kinematic/polarization points.

Certificate:

- `V_amp` shape `12 x 10`;
- rank **10/10**;
- `s_min/s_max = 2.4548457953351053e-6`.

This remains valid only in on-shell amplitude fingerprint space.

## Iteration 147 — retarded C5 embedding

Frozen D=4 Minkowski interacting-vacuum, de Donder, conserved-source, in-in/retarded convention.

Derived tree response:

`chi2R_A;BC(p;q,r)=-(2pi)^4 delta4(p-q-r) G_R,AA'(p) Gamma3^A'_{B'C'} G_R^B'_B(q) G_R^C'_C(r)`.

`NG-FUNNEL-007` established that the old on-shell four-point samples do not fix the required off-shell response protocol.

## Iteration 148 — off-shell source/observable completion gate

A reproducible field-redefinition regression uses

`K phi + g/2 phi^2 + J=0`,

with `chi_phi=-g Gp Gq Gr` and local `phi=psi+a psi^2`.

The coordinate response changes by

`chi_psi-chi_phi=-2 a Gq Gr`,

while reconstructing the same physical observable adds the induced contact term `+2 a Gq Gr` and restores the original response.

Twelve deterministic off-shell points give:

- maximum reconstruction error `1.1102230246251565e-16`;
- minimum nonzero coordinate-response shift `0.11688546786387487`.

Therefore an off-shell C5 comparator must freeze the complete tuple

`(gravity action, field/metric convention, matter/source map, field-redefinition/contact completion, CTP state, renormalization/order, finite conserved probes/smearing)`.

Current C5 statuses:

- local on-shell amplitude tangent: PASS_SCOPED;
- tree retarded factorization: PASS_SCOPED;
- local off-shell `chi2R` rank: **BLOCKED_SOURCE_COMPLETION**;
- `N2`, `C3sym`: BLOCKED;
- loop/nonanalytic columns: BLOCKED;
- no Fisher/resource work is admissible;
- no `ANSATZ-003` is frozen.

Authorities:

- `analysis/c5_offshell_field_redefinition_iteration148.py`;
- `results/c5_offshell_field_redefinition_iteration148.json`;
- `candidate_gravity/C5_OFFSHELL_SOURCE_COMPLETION_ITERATION148.md`;
- `research_log/2026-08-31_iteration_148_c5_offshell_source_completion.md`;
- `recovery/RECOVERY_DELTA_ITERATION_148.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION148.md`.

## Representative comparator program

### C3 — postquantum classical gravity

Use one fixed covariant classical–quantum stochastic action/parameterization. Unsupported post-Gaussian response entries remain `BLOCKED`, never assumed zero.

### C4 — nonlinear quantum mediator / massive spin-2

`ANSATZ-RQIR-KL-002` remains the Gaussian control. A nonlinear C4 tangent requires a separately frozen finite interacting massive-spin-2 realization.

### C5 — perturbative quantum GR EFT

The local on-shell tangent is finite/rank-certified and the tree retarded factorization is fixed. A physical off-shell tangent now additionally requires source/observable completion under EFT field redefinitions.

### Nonlocal gravity / asymptotic safety

Still require one fixed action/truncation each; program labels are not finite comparators.

## `ANSATZ-003` design state

Still intentionally **not frozen**.

A concrete target must survive fixed C3/C4/C5/nonlocal/AS comparator subtraction and leave a nonzero algebraic residual before Fisher/resources.

## Immediate next scientific priority — Iteration 149

Build the first **source-completed finite off-shell C5 operational protocol**.

Required order:

1. freeze the physical metric variable and a conserved matter/source sector;
2. specify the EOM/field-redefinition convention and include all induced source/contact operators, or undo the reduction off shell;
3. freeze sub-cutoff off-shell `(p,q,r)` points with `p=q+r`, away from propagator poles;
4. freeze conserved tensor/source projectors and finite time/spatial smearing normalization;
5. define concrete `chi2R_even/odd` scalar contractions;
6. evaluate the EH plus source-completed local-EFT cubic response;
7. test field-redefinition covariance and Ward/gauge-artifact null directions;
8. compute the first basis-stable `V_C5^(chi2R)` rank/SVD certificate;
9. keep loop/nonanalytic rows BLOCKED unless derived in the same CTP convention;
10. only then proceed to fixed C3 and nonlinear C4 tangents.

No Fisher/resource work and no `ANSATZ-003` promotion before a nonzero algebraic residual survives the concrete comparator quotient.
