# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 151**

## Scientific state in one sentence

Iteration 151 closes the immediate Einstein-Hilbert `BLOCKED_WARD_TAKAHASHI_COMPLETION`: the correct cubic-order off-shell diffeomorphism identity is implemented directly from the same unreduced EH action and passes on all six frozen probes, with the nonzero isolated longitudinal cubic variation cancelled by the nonlinear Lie/source-contact variation of the quadratic action and residuals converging quadratically to zero.

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

Retained funnel rules include `NG-FUNNEL-001` through `NG-FUNNEL-010`.

- `NG-FUNNEL-010` remains retained: `k·Gamma3=0` is not the standalone off-shell gravitational Ward identity. The complete identity includes lower-order inverse-propagator/source-contact terms.

## C5 progress through Iteration 151

### Iteration 146 — local on-shell tangent

D=4 low-energy perturbative GR EFT, EH boundary, parity-even local tree four-graviton basis through dimension 12, 12 samples. `V_amp` shape `12x10`, rank `10/10`, `s_min/s_max=2.4548457953351053e-6`. Valid only in on-shell amplitude fingerprint space.

### Iteration 147 — retarded factorization

Tree causal response fixed as `chi2R_A;BC = - G_R Gamma3 G_R G_R` in the declared Minkowski interacting-vacuum in-in/retarded convention.

### Iteration 148 — source-completion gate

Field-redefinition regression established that coordinate off-shell response is not invariant without induced source/contact completion. Retain `NG-FUNNEL-008`.

### Iteration 149 — source-completed finite operational protocol

Frozen physical metric `g=eta+kappa h`, covariant conserved stress-tensor source, unreduced off-shell policy, six spacelike triplets, Gaussian windows `(tau,L)=(0.8,0.6)`, and TT spin-2 projectors. Projector/conservation checks pass at ~`1e-16`.

### Iteration 150 — first explicit local tree retarded-response block

Implemented the EH cubic trilinear coefficient directly from the unreduced `sqrt(-g) g Gamma Gamma` density and two covariant curvature-cubic directions. On the six frozen probes the local tangent has shape `6x2`, rank `2/2`, singular values `[4.83562189, 1.10930485]`, `s_min/s_max=0.22940272681473822`.

### Iteration 151 — source-completed EH off-shell Ward identity

Implemented the exact action-level cubic-order identity

`B3[L_xi,e2,e3] + B2[Lie_xi e2,e3] + B2[e2,Lie_xi e3] = 0`.

Across the three finite-difference step pairs the worst absolute residual decreases

`2.5767566e-5 -> 6.4418544e-6 -> 1.6104613e-6`,

with approximately 4x reduction per halving, and finest-step worst relative residual `2.7240026e-6`.

Scoped status:
- EH cubic TT block: **PASS_SCOPED**;
- EH source-completed off-shell Ward identity: **PASS_SCOPED**;
- first two curvature-cubic response columns: **PASS_SCOPED_TT_ONLY** pending their own completed Ward validation;
- local `V_C5^(chi2R)` rank certificate: **PASS_SCOPED (2/2)**;
- higher-dimension local columns: BLOCKED;
- loop/nonanalytic columns: BLOCKED;
- `N2`, `C3sym`: BLOCKED;
- Fisher/resources: forbidden;
- `ANSATZ-003`: not created.

Authorities:
- `analysis/c5_ward_identity_iteration151.py`;
- `results/c5_ward_identity_iteration151.json`;
- `candidate_gravity/C5_WARD_IDENTITY_ITERATION151.md`;
- `research_log/2026-08-31_iteration_151_c5_ward_identity.md`;
- `recovery/RECOVERY_DELTA_ITERATION_151.md`.

## Comparator program

### C3
Instantiate one fixed covariant classical-quantum stochastic action/parameterization. Unsupported post-Gaussian entries remain BLOCKED, never assumed zero.

### C4
`ANSATZ-RQIR-KL-002` remains the Gaussian control. Nonlinear C4 requires a separately frozen finite interacting massive-spin-2 realization.

### C5
The EH off-shell Ward/source-contact blocker is now closed. Before expanding or quotienting the local tangent, validate the two existing curvature-cubic directions under the same source-completed diffeomorphism identity.

### Nonlocal / asymptotic safety
Still require one fixed action/truncation each; program labels are not finite comparators.

## `ANSATZ-003` design state

Still intentionally **not frozen**. A concrete target must survive fixed C3/C4/C5/nonlocal/AS subtraction and leave a nonzero algebraic residual before Fisher/resources.

## Immediate next scientific priority — Iteration 152

1. validate `Tr(Ricci^3)` and cyclic `Riemann^3` under the same action-level source-completed diffeomorphism identity;
2. distinguish implementation/convention failures from genuine consistency failures;
3. if both pass, extend the finite local C5 tangent or proceed to the first fixed C3 comparator tangent;
4. keep unsupported higher-dimension and loop/nonanalytic columns explicitly BLOCKED;
5. no Fisher/resource work and no `ANSATZ-003` before a nonzero residual survives the concrete comparator quotient.
