# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator quotient  
**Authoritative Candidate Gravity front:** **Iteration 155**

## Scientific state in one sentence

The first fixed C3 comparator is now nonlinear enough to demonstrate from one published classical-spacetime dynamics all of: Gaussian metric noise, a nonzero symmetric gravitational bispectrum, and a nonzero tree causal nonlinear Einstein response. The symmetric cumulant lifts the `(D2,D0)` comparator tangent to rank `2/2`, whereas the tree causal response is a common hard-calibrated GR-boundary contribution and adds zero diffusion rank. Diffusion-dependent/order-sensitive C3 response remains BLOCKED, so the next active comparator target is a fixed nonlinear C4 realization.

## Frozen model outcomes

### `ANSATZ-PQG-EFT-001`
REFERENCE / NOT PROMOTABLE. QG-007 FAIL due exact C5 identity. Retain `CG-NG-003`.

### `ANSATZ-RQIR-CTP-001` v0.1
REJECTED. QG-004 FAIL: `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`. Retain `CG-NG-004`.

### `ANSATZ-RQIR-KL-002` v0.1
REFERENCE / NOT PROMOTABLE. Positive KL Gaussian spin-2 continuum but exact C4 direct-integral/tower degeneracy. Retain `CG-NG-005/006`.

## Frozen post-Gaussian protocol

Reduced coordinates after hard locks:

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Novelty pre-gate:

`rank([M,b]) > rank(M)`

or equivalently nonzero

`r_beta=(I-MM^+)b`,

only after included comparator rows are actually derived from fixed finite realizations.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-013`.

## C3 — fixed postquantum-classical gravity comparator

### Iteration 153 — linear stochastic block

`C3-PQCG-LIN-001`:

`box h_s=J_s+xi_s`, `<xi_s xi_s'>=2D_s delta_ss' delta4`, `s=2,0`.

On the frozen finite probe/smearing layer:

`A=258.83104475297773`,

`N2=A(5D2+D0)`.

One scalar `N2` coordinate gives rank `1/2` for `(D2,D0)`.

Retained:

`C3-NG-001 — ONE_NOISE_COORDINATE_COLLAPSES_TWO_DIFFUSION_DIRECTIONS` = regime-specific non-identifiability.

### Iteration 154 — nonlinear symmetric cumulant

`C3-PQCG-NL-001` uses the same published covariant PQCG pure-gravity Onsager–Machlup action

`S[g]=1/2 int sqrt(-g)[alpha R_mn R^mn-beta R^2]`.

Quadratic covariance map:

`D2=1/(2alpha)`,

`D0=1/[8(alpha-3beta)]`.

On the six frozen TT probes, `R^(1)=0`, so the `R^2` cubic TT coefficient vanishes, while `R_mn R^mn` generates a nonzero classical connected third cumulant.

Aggregate:

`C3sym_TT=B D2^2`,

`B=-617.4340282011477`.

Together with the noise row,

`V_C3=[[5A,A],[2BD2,0]]`,

`det(V_C3)=-2ABD2`.

For every physical `D2>0`, the supported `(N2,C3sym_TT)` tangent is rank **2/2**.

Normalized `D2=1` SVD diagnostic:

`[1798.6530445678386,177.70085794811004]`,

`smin/smax=0.0987966292247353`.

Retained:

- `C3-NG-002 — NONLINEAR_CUMULANT_LIFTS_LINEAR_DIFFUSION_DEGENERACY`;
- `NG-FUNNEL-012 — CLASSICAL_OM_ACTION_GENERATES_POST_GAUSSIAN_RANK`.

### Iteration 155 — tree causal nonlinear response

The same nonlinear Einstein drift gives

`chi2R_A;BC = -G_R_AA' Gamma3_EH^A'_{B'C'} G_R^B'_B G_R^C'_C`.

Frozen six-probe response:

`[0.30003001285313774,-1.461790494216445,-12.034873790942026,-14.434681522564402,4.867521776975717,-2.7789127642722273]`.

Thus the classical stochastic spacetime comparator has a **nonzero causal nonlinear response**.

After the common Newton/GR coupling is hard-calibrated, however,

`partial chi2R_tree / partial D2 = partial chi2R_tree / partial D0 = 0`.

Therefore this tree response adds rank **0** to the `(D2,D0)` stochastic tangent: it is a common GR-boundary contribution, not a new diffusion direction.

Retained:

- `C3-NG-003 — TREE_ORDERED_RESPONSE_IS_COMMON_GR_BOUNDARY`;
- `NG-FUNNEL-013 — NONZERO_CAUSAL_NONLINEAR_RESPONSE_NOT_QUANTUM_CERTIFICATE`.

### C3 blockers after Iteration 155

Supported:

- `N2`;
- `C3sym_TT`;
- nonzero tree causal Einstein response as common GR boundary.

Still BLOCKED, never zero-filled:

- diffusion-dependent stochastic/MSR-loop ordered corrections;
- exact protocol-specific `chi2R_odd` selector/completion;
- `soft2`;
- non-TT `tensor_geo` completion;
- threshold coordinate;
- full C3 quotient.

Authorities:

- `candidate_gravity/comparators/C3-PQCG-NL-001.md`;
- `analysis/c3_pqcg_nonlinear_bispectrum_iteration154.py`;
- `results/c3_pqcg_nonlinear_bispectrum_iteration154.json`;
- `analysis/c3_pqcg_tree_ordered_response_iteration155.py`;
- `results/c3_pqcg_tree_ordered_response_iteration155.json`;
- `candidate_gravity/C3_PQCG_TREE_ORDERED_RESPONSE_ITERATION155.md`;
- `recovery/RECOVERY_DELTA_ITERATION_155.md`.

Literature anchors:

- Oppenheim & Weller-Davies, Phys. Rev. X 16, 031007 (2026), DOI `10.1103/2rcd-dzcf`;
- Oppenheim & Sajjad, arXiv:`2605.05375`;
- Grudka et al., arXiv:`2402.17844`.

## C5 status retained

- local on-shell `V_amp`: `12x10`, rank `10/10`, on-shell amplitude space only;
- tree retarded factorization fixed;
- source-completed six-probe protocol PASS_SCOPED;
- EH + two curvature-cubic local response tangent: `6x2`, rank `2/2`, `PASS_SCOPED_WARD_VALIDATED`;
- higher-dimension local columns: BLOCKED;
- loop/nonanalytic columns: BLOCKED;
- C5 `N2`/`C3sym` sectors: BLOCKED.

## Other comparator program

### C4
`ANSATZ-RQIR-KL-002` remains the exact Gaussian control. The next active target is a **fixed finite nonlinear interacting massive-spin-2 / dRGT-style realization**.

### Nonlocal / asymptotic safety
Still require one fixed action/truncation each. Program labels are not finite comparator matrices.

## Article material

Latest working matrix:

`docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION155.md`.

The article funnel can now state using a concrete classical-spacetime model, not merely an abstract argument, that neither gravitational symmetric non-Gaussianity nor nonzero nonlinear causal response alone certifies a quantum metric.

## `ANSATZ-003` design state

Still intentionally **not frozen**. No algebraic novelty residual has survived the full fixed comparator quotient.

Fisher/resources remain forbidden.

## Immediate next scientific priority — Iteration 156

Instantiate the first fixed nonlinear C4 comparator.

1. freeze one concrete ghost-free interacting massive-spin-2 / dRGT-style action and finite parameter vector rather than using the C4 class label;
2. retain the same physical source convention and six-probe finite response layer where compatible;
3. derive its tree `Gamma3` and retarded `chi2R` from the same action;
4. identify supported tensor/threshold coordinates and keep unavailable rows BLOCKED;
5. compare the finite nonlinear C4 tangent against the existing C5 `6x2` local response span and supported C3 rows;
6. do not treat Vainshtein/nonlinear completion as free nuisance freedom unless actually present in the frozen realization;
7. no Fisher/resources and no `ANSATZ-003` until a nonzero residual survives fixed C3/C4/C5/nonlocal/AS quotienting.
