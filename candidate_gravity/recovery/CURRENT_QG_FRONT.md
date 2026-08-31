# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 152**

## Scientific state in one sentence
Iteration 152 closes the validation blocker on the two existing local curvature-cubic C5 columns: because both `R^3` operators have no flat-background quadratic term, their cubic completed diffeomorphism identity reduces to linearized gauge invariance, and both columns pass on all six frozen probes and all three gauge-leg replacements at machine precision.

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

## C5 progress through Iteration 152
- Iteration 146: local on-shell `V_amp`, shape `12x10`, rank `10/10`, valid only in on-shell amplitude space.
- Iteration 147: tree causal factorization `chi2R = -G_R Gamma3 G_R G_R` fixed.
- Iteration 148: source-completion/field-redefinition gate established.
- Iteration 149: physical metric/source convention and six off-shell TT probes frozen.
- Iteration 150: explicit EH + two curvature-cubic local response columns; local tangent shape `6x2`, rank `2/2`, singular values `[4.83562189,1.10930485]`, `smin/smax=0.22940272681473822`.
- Iteration 151: EH source-completed action-level Ward identity PASS_SCOPED.
- Iteration 152: both existing curvature-cubic columns pass their correct operator-specific completed diffeomorphism identities.

### Iteration 152 numerical certificate
Across all six probes and all three gauge-leg replacements:
- max `|R^(1)[L_xi]| = 2.220446049250313e-16`;
- max `|Riemann^(1)[L_xi]| = 5.551115123125783e-17`;
- max `|B3_Ricci3| = 2.4454568146171362e-17`;
- max `|B3_Riemann3| = 7.549184413398274e-17`.

Scoped status:
- EH cubic TT block: **PASS_SCOPED**;
- EH source-completed off-shell Ward identity: **PASS_SCOPED**;
- `Tr(Ricci^3)` Ward identity: **PASS_SCOPED**;
- cyclic `Riemann^3` Ward identity: **PASS_SCOPED**;
- existing local `V_C5^(chi2R)` rank certificate: **PASS_SCOPED_WARD_VALIDATED (2/2)**;
- higher-dimension local columns: BLOCKED;
- loop/nonanalytic columns: BLOCKED;
- `N2`, `C3sym`: BLOCKED;
- Fisher/resources: forbidden;
- `ANSATZ-003`: not created.

Authorities:
- `analysis/c5_curvature_cubic_ward_iteration152.py`;
- `results/c5_curvature_cubic_ward_iteration152.json`;
- `candidate_gravity/C5_CURVATURE_CUBIC_WARD_ITERATION152.md`;
- `research_log/2026-08-31_iteration_152_c5_curvature_cubic_ward.md`;
- `recovery/RECOVERY_DELTA_ITERATION_152.md`.

## Comparator program
### C3
Immediate next target: instantiate one fixed finite covariant classical-quantum stochastic action/parameterization and derive its supported post-Gaussian tangent from one dynamics. Unsupported entries remain BLOCKED, never assumed zero.

### C4
`ANSATZ-RQIR-KL-002` remains the Gaussian control. Nonlinear C4 requires a separately frozen finite interacting massive-spin-2 realization.

### C5
The existing explicit local tree `6x2` block is now Ward-validated. Higher local directions and loop/nonanalytic sectors remain explicitly BLOCKED; no claim of full C5 quotient closure.

### Nonlocal / asymptotic safety
Still require one fixed action/truncation each; program labels are not finite comparators.

## `ANSATZ-003` design state
Still intentionally **not frozen**. A concrete target must survive fixed C3/C4/C5/nonlocal/AS subtraction and leave a nonzero algebraic residual before Fisher/resources.

## Immediate next scientific priority — Iteration 153
1. instantiate the first fixed finite C3 comparator tangent rather than a broad capability mask;
2. freeze one explicit covariant classical-quantum stochastic action, parameter convention, state/noise prescription and map to the frozen reduced post-Gaussian coordinates;
3. derive all supported `J/N/chiR/C3/chi2R/soft/Ward` objects from that same dynamics and mark unsupported objects BLOCKED;
4. maintain higher local and loop/nonanalytic C5 directions as BLOCKED rather than zero;
5. no Fisher/resource work and no `ANSATZ-003` before a nonzero residual survives the concrete comparator quotient.
