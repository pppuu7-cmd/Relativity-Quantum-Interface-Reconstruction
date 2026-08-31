# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 147**

## Scientific state in one sentence

Iteration 147 froze one CTP/retarded prescription and derived the exact tree-level C5 nonlinear-response factorization `chi2R ~ G_R Gamma3 G_R G_R`, but proved that the Iteration-146 on-shell `(s,t,u,phi)` four-point protocol does not uniquely determine the off-shell three-point retarded projector/smearing coordinates; the first numerical `V_C5^(chi2R)` rank certificate is therefore operationally BLOCKED pending a new finite off-shell protocol.

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
- `NG-FUNNEL-005`: broad C3/C4/C5 capability masks saturate the 8D space and are unusable as physical comparator tangents;
- `NG-FUNNEL-006`: an on-shell amplitude tangent is not automatically the ordered CTP/retarded RQIR tangent;
- `NG-FUNNEL-007`: on-shell four-point kinematics do not uniquely fix the off-shell retarded three-point protocol.

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

This remains valid only in the on-shell amplitude fingerprint space.

## Iteration 147 — first retarded C5 embedding step

### Frozen real-time convention

- D=4 Minkowski;
- interacting in-vacuum;
- de Donder perturbative gauge;
- conserved physical source projections;
- linear source coupling `J_A h^A`;
- same EH + local EFT dynamics/order as Iteration 146;
- all response legs use the Schwinger–Keldysh/in-in retarded prescription.

### Derived tree-level kernel

For `K h + 1/2 V[h,h] + J=0`,

`h^(1)=-G_R J`,

and

`chi2R_A;BC(p;q,r)=-(2pi)^4 delta4(p-q-r) G_R,AA'(p) Gamma3^A'_{B'C'}(p,-q,-r) G_R^B'_B(q) G_R^C'_C(r)`.

This fixes the correct tree-level C5 ordered nonlinear-response object.

### NG-FUNNEL-007 — ON_SHELL_4PT_KINEMATICS_DO_NOT_FIX_OFF_SHELL_RETARDED_3PT

The Iteration-146 `(s,t,u,phi)` samples do not supply the off-shell virtualities/energy routing, three conserved tensor projectors, finite smearing/window normalization, or explicit `chi2R_even/odd` scalar contractions required for a numerical RQIR retarded tangent.

Therefore:

- `chi2R_even/odd`: **BLOCKED_PROTOCOL_UNDERSPECIFIED**;
- local-EFT retarded rank: **NOT_COMPUTABLE** yet;
- `N2`, `C3sym`: BLOCKED pending same-convention CTP derivations;
- loop/nonanalytic C5 columns: BLOCKED pending same-convention derivation;
- no Fisher/resource work is admissible;
- no `ANSATZ-003` is frozen.

Authorities:

- `analysis/c5_retarded_embedding_iteration147.py`;
- `results/c5_retarded_embedding_iteration147.json`;
- `candidate_gravity/C5_RETARDED_EMBEDDING_ITERATION147.md`;
- `research_log/2026-08-31_iteration_147_c5_retarded_embedding.md`;
- `recovery/RECOVERY_DELTA_ITERATION_147.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION147.md`.

## Representative comparator program

### C3 — postquantum classical gravity

Use one fixed covariant classical–quantum stochastic action/parameterization. Unsupported post-Gaussian response entries remain `BLOCKED`, never assumed zero.

### C4 — nonlinear quantum mediator / massive spin-2

`ANSATZ-RQIR-KL-002` remains the Gaussian control. A nonlinear C4 tangent requires a separately frozen finite interacting massive-spin-2 realization.

### C5 — perturbative quantum GR EFT

Local four-point tangent is finite/rank-certified. Tree-level retarded factorization is now fixed. The next missing item is the explicit finite off-shell projector/smearing protocol and cubic-vertex contraction.

### Nonlocal gravity / asymptotic safety

Still require one fixed action/truncation each; program labels are not finite comparators.

## `ANSATZ-003` design state

Still intentionally **not frozen**.

A concrete target must survive fixed C3/C4/C5/nonlocal/AS comparator subtraction and leave a nonzero algebraic residual before Fisher/resources.

## Immediate next scientific priority — Iteration 148

Build the first **finite off-shell C5 retarded-response certificate**.

Required order:

1. freeze sub-cutoff off-shell `(p,q,r)` points with `p=q+r`, away from propagator poles;
2. freeze explicit conserved tensor/source projectors and finite time/spatial smearing normalization;
3. define concrete `chi2R_even/odd` contractions;
4. evaluate the de-Donder Einstein–Hilbert cubic vertex and every local-EFT cubic vertex contributing at the frozen order;
5. perform the conserved-source Ward/gauge-artifact null test;
6. compute the first actual `V_C5^(chi2R)` rank/SVD certificate;
7. keep loop/nonanalytic rows BLOCKED unless derived in the same CTP convention;
8. only then proceed to fixed C3 and nonlinear C4 tangents.

No Fisher/resource work and no `ANSATZ-003` promotion before a nonzero algebraic residual survives the concrete comparator quotient.
