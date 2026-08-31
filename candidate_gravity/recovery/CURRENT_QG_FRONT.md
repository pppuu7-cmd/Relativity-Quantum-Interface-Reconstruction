# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 153**

## Scientific state in one sentence
Iteration 153 instantiates the first concrete finite C3 comparator block, `C3-PQCG-LIN-001`: on the supported linear stochastic `(N2,chi1R)` rows its `(D2,D0)` tangent has rank `1/2`, proving a regime-specific protocol degeneracy `N2 proportional to 5D2+D0`; all undriven post-Gaussian rows remain BLOCKED rather than being zero-filled.

## Frozen model outcomes
### `ANSATZ-PQG-EFT-001`
REFERENCE / NOT PROMOTABLE. QG-001/QG-002/QG-003 PASS in the declared low-energy regime; QG-007 FAIL due exact C5 identity. Retain `CG-NG-003`.

### `ANSATZ-RQIR-CTP-001` v0.1
REJECTED. QG-004 FAIL: `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`. Retain `CG-NG-004`.

### `ANSATZ-RQIR-KL-002` v0.1
REFERENCE / NOT PROMOTABLE. Positive KL measure but exact Gaussian C4 direct-integral/tower degeneracy. QG-007 FAIL. Retain `CG-NG-005/006`.

## Frozen post-Gaussian protocol
Reduced coordinates after hard locks:
`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Novelty pre-gate remains `rank([M,b])>rank(M)` or nonzero `r_beta=(I-MM^+)b`, but only after all included comparator rows are actually derived.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-011`.

## C3 progress through Iteration 153
Concrete comparator: `C3-PQCG-LIN-001`.

Frozen scoped dynamics:
`box h_s=J_s+xi_s`, `<xi_s xi_s'>=2D_s delta_ss' delta^4`, `s=2,0`.

Literature anchors: Oppenheim & Weller-Davies, PRX 16 031007 (2026); Oppenheim & Sajjad, arXiv:2605.05375; Grudka et al., arXiv:2402.17844.

Supported rows only: `(N2,chi1R)`; parameter vector `(D2,D0)`.

On the Iteration-149 finite spacelike probe/smearing layer:
- `A=258.83104475297773`;
- `N2=A(5D2+D0)`;
- supported tangent `[[1294.1552237648887,258.83104475297773],[0,0]]`;
- rank `1/2`;
- singular values `[1319.7845479190407,0]`.

Scoped interpretation:
- `C3-NG-001 — ONE_NOISE_COORDINATE_COLLAPSES_TWO_DIFFUSION_DIRECTIONS`: **REGIME_SPECIFIC_NON_IDENTIFIABILITY**, not consistency FAIL;
- `NG-FUNNEL-011 — PARTIAL_COMPARATOR_ROWS_ARE_NOT_ZERO_ROWS`;
- `C3sym`, `chi2R_even/odd`, `soft2`, `tensor_geo`, `threshold`: **BLOCKED_NONLINEAR_COMPLETION**;
- full C3 quotient: BLOCKED.

Authorities:
- `candidate_gravity/comparators/C3-PQCG-LIN-001.md`;
- `analysis/c3_pqcg_linear_tangent_iteration153.py`;
- `results/c3_pqcg_linear_tangent_iteration153.json`;
- `candidate_gravity/C3_PQCG_LINEAR_TANGENT_ITERATION153.md`;
- `research_log/2026-08-31_iteration_153_c3_pqcg_linear_tangent.md`;
- `recovery/RECOVERY_DELTA_ITERATION_153.md`.

## C5 status retained
- local on-shell `V_amp`: rank `10/10`, on-shell amplitude space only;
- tree retarded factorization fixed;
- source-completed six-probe protocol PASS_SCOPED;
- EH + two curvature-cubic local response tangent: `6x2`, rank `2/2`, PASS_SCOPED_WARD_VALIDATED;
- higher-dimension local columns: BLOCKED;
- loop/nonanalytic columns: BLOCKED;
- `N2`, `C3sym` C5 sectors: BLOCKED.

## Other comparator program
### C4
`ANSATZ-RQIR-KL-002` remains Gaussian control. Nonlinear C4 requires a separately frozen finite interacting massive-spin-2 realization.

### Nonlocal / asymptotic safety
Still require one fixed action/truncation each; program labels are not finite comparators.

## `ANSATZ-003` design state
Still intentionally **not frozen**. No algebraic novelty residual has survived the full fixed comparator quotient.

## Immediate next scientific priority — Iteration 154
1. attempt a literature-grounded nonlinear C3 extension from the same covariant CQ path-integral family, freezing one explicit nonlinear drift/backreaction or non-Gaussian noise term;
2. derive at least one genuine `chi2R` or `C3sym` column from that same dynamics and test whether it adds rank beyond the linear `N2` direction;
3. if that cannot be instantiated without unsupported conventions, record `BLOCKED_NONLINEAR_C3_SPECIFICATION` and move to the first fixed nonlinear C4 comparator rather than inventing C3 columns;
4. retain C5 higher-local/loop sectors as BLOCKED;
5. no Fisher/resources and no `ANSATZ-003` before a nonzero residual survives fixed comparator quotienting.
