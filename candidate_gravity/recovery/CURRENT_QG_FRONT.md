# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 149**

## Scientific state in one sentence

Iteration 149 closes the Iteration-148 source/observable ambiguity at the protocol level by fixing the physical metric, conserved stress-tensor source map, unreduced off-shell EFT policy, six finite spacelike momentum triplets, Gaussian windows and transverse-traceless spin-2 projectors. The first numerical C5 retarded tangent is now `BLOCKED_VERTEX_IMPLEMENTATION`: the remaining missing object is the explicit unreduced Einstein-Hilbert + local-EFT cubic response, not the source convention.

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

## Frozen post-Gaussian protocol

Full coordinates:

`y=(norm,N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft0,soft1,soft2,tensor_geo,threshold)`.

Hard locks: `norm`, `soft0`, `soft1`.

Reduced coordinates:

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Candidate novelty pre-gate after exact hard-constraint reduction:

`rank([M,b]) > rank(M)`

or nonzero

`r_beta=(I-MM^+)b`.

Retained funnel rules:

- `NG-FUNNEL-001`: nonlinearity alone is not sufficient;
- `NG-FUNNEL-002`: symmetric higher cumulants must be separated from ordered nonlinear response;
- `NG-FUNNEL-003`: Ward/soft locking is necessary but not sufficient;
- `NG-FUNNEL-004`: `soft0/soft1` are consistency locks, not novelty coordinates;
- `NG-FUNNEL-005`: broad C3/C4/C5 capability masks are not physical finite tangents;
- `NG-FUNNEL-006`: on-shell amplitude tangent is not automatically a CTP/retarded RQIR tangent;
- `NG-FUNNEL-007`: on-shell four-point kinematics do not fix the off-shell retarded three-point protocol;
- `NG-FUNNEL-008`: an on-shell/EOM-reduced EFT basis is not automatically a basis-independent off-shell response basis;
- `NG-FUNNEL-009`: a Ward-safe source-completed projector/probe layer is not itself a nonlinear-vertex/rank certificate.

## C5 progress through Iteration 149

### Iteration 146 — local on-shell tangent

- D=4 low-energy perturbative GR EFT;
- Einstein-Hilbert boundary;
- parity-even local tree four-graviton basis through dimension 12;
- 12 frozen on-shell samples;
- `V_amp` shape `12 x 10`, rank **10/10**;
- `s_min/s_max = 2.4548457953351053e-6`.

Valid only in on-shell amplitude fingerprint space.

### Iteration 147 — retarded factorization

Tree-level causal response fixed as

`chi2R_A;BC(p;q,r)=-(2pi)^4 delta4(p-q-r) G_R(p) Gamma3 G_R(q) G_R(r)`

in the declared Minkowski interacting-vacuum in-in/retarded convention.

### Iteration 148 — off-shell source-completion gate

Field-redefinition regression proved that coordinate off-shell response changes under local field redefinitions while the same physical observable is restored only after induced source/contact completion. Hence the Iteration-146 EOM-reduced basis could not be used directly off shell.

### Iteration 149 — source-completed finite operational protocol

Frozen choices:

- physical metric `g_mn=eta_mn+kappa h_mn`;
- conserved source from covariant `S_m[g,Psi]`;
- Iteration-146 EOM reduction is undone off shell;
- same low-energy local tree order, represented in a complete unreduced covariant basis before projection;
- six fixed spacelike triplets with `p=q+r`, all away from the massless pole;
- Gaussian windows `(tau,L)=(0.8,0.6)`;
- D=4 transverse-traceless spin-2 projectors on all legs.

Regression:

- max longitudinal contraction `1.2533377113932431e-16`;
- max trace `2.636779683484747e-16`;
- max idempotence error `3.3306690738754696e-16`.

Status:

- source/observable convention: FROZEN;
- finite off-shell probe set: PASS_SCOPED;
- Ward/projector regression: PASS_SCOPED;
- local `V_C5^(chi2R)` rank: **BLOCKED_VERTEX_IMPLEMENTATION / NOT_COMPUTED**;
- `N2`, `C3sym`: BLOCKED;
- loop/nonanalytic columns: BLOCKED;
- no Fisher/resource work is admissible;
- no `ANSATZ-003` is frozen.

Authorities:

- `analysis/c5_source_completed_protocol_iteration149.py`;
- `results/c5_source_completed_protocol_iteration149.json`;
- `candidate_gravity/C5_SOURCE_COMPLETED_PROTOCOL_ITERATION149.md`;
- `research_log/2026-08-31_iteration_149_c5_source_completed_protocol.md`;
- `recovery/RECOVERY_DELTA_ITERATION_149.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION149.md`.

## Representative comparator program

### C3

Instantiate one fixed covariant classical–quantum stochastic action/parameterization. Unsupported post-Gaussian response entries remain `BLOCKED`, never assumed zero.

### C4

`ANSATZ-RQIR-KL-002` remains the Gaussian control. A nonlinear C4 tangent requires a separately frozen finite interacting massive-spin-2 realization.

### C5

The on-shell local tangent, causal tree factorization and source-completed finite probe protocol are now fixed. The next missing object is the explicit unreduced EH + local-EFT cubic vertex contracted in this protocol.

### Nonlocal / asymptotic safety

Still require one fixed action/truncation each; program labels are not finite comparators.

## `ANSATZ-003` design state

Still intentionally **not frozen**.

A concrete target must survive fixed C3/C4/C5/nonlocal/AS comparator subtraction and leave a nonzero algebraic residual before Fisher/resources.

## Immediate next scientific priority — Iteration 150

Implement and validate the first **unreduced EH + local-EFT cubic response block** in the Iteration-149 metric/source convention.

Required order:

1. implement the Einstein-Hilbert cubic graviton vertex without using the on-shell EOM-reduced amplitude chart;
2. add the lowest nontrivial local curvature-cubic directions in the same field convention;
3. contract with the six frozen triplets, TT projectors and Gaussian windows;
4. perform longitudinal-replacement/Ward null regressions;
5. verify source-completion/field-coordinate covariance on the implemented sub-block;
6. compute the first scoped `V_C5^(chi2R)` rank/SVD certificate;
7. keep unsupported higher-dimension and loop/nonanalytic directions explicitly BLOCKED;
8. only after a real C5 retarded tangent exists move to fixed C3 and nonlinear C4 tangents.

No Fisher/resource work and no `ANSATZ-003` promotion before a nonzero algebraic residual survives the concrete comparator quotient.
