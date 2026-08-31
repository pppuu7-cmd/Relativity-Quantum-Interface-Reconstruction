# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 150**

## Scientific state in one sentence

Iteration 150 closes `BLOCKED_VERTEX_IMPLEMENTATION` for the first explicit local tree TT sub-block: the unreduced Einstein-Hilbert cubic response and two covariant curvature-cubic directions are now computed on the six frozen Iteration-149 probes, giving a scoped `6x2` local C5 tangent of rank `2/2`; the next blocker is the complete off-shell gravitational Ward-Takahashi/source-contact identity, not the existence of a cubic vertex.

## Frozen model outcomes

### `ANSATZ-PQG-EFT-001`
REFERENCE / NOT PROMOTABLE. QG-001/QG-002/QG-003 PASS in the declared low-energy regime; QG-007 FAIL due exact C5 identity. Retain `CG-NG-003`.

### `ANSATZ-RQIR-CTP-001` v0.1
REJECTED. Lorentzian continuation has an extra below-threshold timelike pole with opposite residue sign. QG-004 FAIL: `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`. Retain `CG-NG-004`.

### `ANSATZ-RQIR-KL-002` v0.1
REFERENCE / NOT PROMOTABLE. Positive KL measure and causal retarded superposition, but exact Gaussian C4 direct-integral/tower degeneracy. QG-007 FAIL: `EXACT_GAUSSIAN_C4_KK_DEGENERACY`. Retain `CG-NG-005/006`.

## Frozen post-Gaussian protocol

Full coordinates:
`y=(norm,N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft0,soft1,soft2,tensor_geo,threshold)`.

Hard locks: `norm`, `soft0`, `soft1`.

Reduced coordinates:
`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Novelty pre-gate after exact hard-constraint reduction:
`rank([M,b]) > rank(M)` or nonzero `r_beta=(I-MM^+)b`.

Retained funnel rules include `NG-FUNNEL-001` through `NG-FUNNEL-010`. New in Iteration 150:

- `NG-FUNNEL-010`: `k·Gamma3=0` is not the standalone off-shell gravitational Ward identity. A complete Ward-Takahashi/Slavnov-Taylor check must include inverse-propagator and source/contact terms in the same field/source convention.

## C5 progress through Iteration 150

### Iteration 146 — local on-shell tangent

D=4 low-energy perturbative GR EFT, EH boundary, parity-even local tree four-graviton basis through dimension 12, 12 samples. `V_amp` shape `12x10`, rank `10/10`, `s_min/s_max=2.4548457953351053e-6`. Valid only in on-shell amplitude fingerprint space.

### Iteration 147 — retarded factorization

Tree causal response fixed as `chi2R_A;BC = - G_R Gamma3 G_R G_R` in the declared Minkowski interacting-vacuum in-in/retarded convention.

### Iteration 148 — source-completion gate

Field-redefinition regression established that coordinate off-shell response is not invariant without induced source/contact completion. Retain `NG-FUNNEL-008`.

### Iteration 149 — source-completed finite operational protocol

Frozen physical metric `g=eta+kappa h`, covariant conserved stress-tensor source, unreduced off-shell policy, six spacelike triplets, Gaussian windows `(tau,L)=(0.8,0.6)`, and TT spin-2 projectors. Projector/conservation checks pass at ~`1e-16`.

### Iteration 150 — first explicit local tree retarded-response block

Implemented the EH cubic trilinear coefficient directly from the unreduced `sqrt(-g) g Gamma Gamma` density for three off-shell plane-wave modes. No on-shell/EOM-reduced amplitude chart is used.

Added two explicit covariant curvature-cubic directions in the same metric convention:

1. `Tr(Ricci^3)`;
2. cyclic `Riemann^3`.

On the six frozen probes:

- local tangent shape: `6x2`;
- rank: **2/2**;
- singular values: `[4.83562189, 1.10930485]`;
- `s_min/s_max = 0.22940272681473822`;
- max EH permutation asymmetry: `8.13e-14`;
- max final finite-difference halving-step change before Richardson extrapolation: `9.22e-6`.

Scoped status:

- EH cubic TT block: **PASS_SCOPED**;
- first two curvature-cubic columns: **PASS_SCOPED**;
- local `V_C5^(chi2R)` rank certificate: **PASS_SCOPED (2/2)**;
- complete off-shell Ward/source-contact validation: **BLOCKED_WARD_TAKAHASHI_COMPLETION**;
- higher-dimension local columns: BLOCKED;
- loop/nonanalytic columns: BLOCKED;
- `N2`, `C3sym`: BLOCKED;
- Fisher/resources: forbidden;
- `ANSATZ-003`: not created.

Authorities:

- `analysis/c5_cubic_response_iteration150.py`;
- `results/c5_cubic_response_iteration150.json`;
- `candidate_gravity/C5_CUBIC_RESPONSE_ITERATION150.md`;
- `research_log/2026-08-31_iteration_150_c5_cubic_response.md`;
- `recovery/RECOVERY_DELTA_ITERATION_150.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION150.md`.

## Comparator program

### C3
Instantiate one fixed covariant classical-quantum stochastic action/parameterization. Unsupported post-Gaussian entries remain BLOCKED, never assumed zero.

### C4
`ANSATZ-RQIR-KL-002` remains the Gaussian control. Nonlinear C4 requires a separately frozen finite interacting massive-spin-2 realization.

### C5
The first explicit local TT retarded-response sub-block now exists. Before extending or quotienting it, the exact off-shell Ward-Takahashi/source-contact identity must be implemented and passed.

### Nonlocal / asymptotic safety
Still require one fixed action/truncation each; program labels are not finite comparators.

## `ANSATZ-003` design state

Still intentionally **not frozen**. A concrete target must survive fixed C3/C4/C5/nonlocal/AS subtraction and leave a nonzero algebraic residual before Fisher/resources.

## Immediate next scientific priority — Iteration 151

1. derive the correct off-shell gravitational Ward-Takahashi identity for the exact EH sub-block in the frozen `g=eta+kappa h` convention;
2. implement the inverse-propagator and source/contact terms required by that identity;
3. validate the completed identity numerically on the same six probes;
4. if PASS, extend the local C5 tangent beyond the first two curvature-cubic directions or proceed to the first fixed C3 comparator tangent;
5. keep unsupported higher-dimension and loop/nonanalytic columns explicitly BLOCKED.

No Fisher/resource work and no `ANSATZ-003` before a nonzero algebraic residual survives the concrete comparator quotient.
