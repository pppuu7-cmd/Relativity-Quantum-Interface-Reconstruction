# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator tangents  
**Authoritative Candidate Gravity front:** **Iteration 154**

## Scientific state in one sentence
Iteration 154 upgrades the concrete C3 comparator from a rank-1 linear noise block to a **rank-2/2 supported `(N2,C3sym_TT)` nonlinear stochastic block** derived from the same published covariant PQCG Onsager–Machlup action; this proves concretely that a nonzero gravitational symmetric bispectrum and increased post-Gaussian rank can arise in a classical stochastic spacetime and therefore are not quantum-spacetime certificates.

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

Novelty pre-gate remains

`rank([M,b])>rank(M)`

or nonzero

`r_beta=(I-MM^+)b`,

but only after every included comparator row is actually derived from a fixed realization.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-012`.

## C3 progress

### Iteration 153 — linear stochastic block

Concrete comparator: `C3-PQCG-LIN-001`.

Frozen scoped dynamics:

`box h_s=J_s+xi_s`,

`<xi_s xi_s'>=2D_s delta_ss' delta^4`, `s=2,0`.

On the Iteration-149 finite spacelike probe/smearing layer:

`A=258.83104475297773`,

`N2=A(5D2+D0)`.

The supported `(N2,chi1R)` parameter tangent for `(D2,D0)` was rank `1/2`, because `chi1R` does not vary with the two diffusion constants in that scoped parameterization.

Retained:

`C3-NG-001 — ONE_NOISE_COORDINATE_COLLAPSES_TWO_DIFFUSION_DIRECTIONS` = **REGIME_SPECIFIC_NON_IDENTIFIABILITY**, not consistency FAIL.

`NG-FUNNEL-011 — PARTIAL_COMPARATOR_ROWS_ARE_NOT_ZERO_ROWS`.

### Iteration 154 — nonlinear Onsager–Machlup extension

Active scoped comparator: `C3-PQCG-NL-001`.

The same published covariant CQ gravity family contains the pure-gravity stochastic probability action

`S[g]=1/2 int sqrt(-g) [alpha R_mn R^mn - beta R^2]`.

Literature anchors:

- Oppenheim & Weller-Davies, Phys. Rev. X 16, 031007 (2026), DOI `10.1103/2rcd-dzcf`;
- Oppenheim & Sajjad, arXiv:`2605.05375`;
- Grudka et al., arXiv:`2402.17844`.

Quadratic covariance matching to the Iteration-153 convention gives

`D2=1/(2 alpha)`,

`D0=1/[8(alpha-3 beta)]`.

No new phenomenological noise/cubic kernel was added.

### New supported `C3sym` row

For a classical probability action `S=S2+S3+...`, the leading connected three-point function is

`<h1 h2 h3>_c = -C1 C2 C3 Gamma3`.

Because the metric is classical, this is already the fully symmetric third cumulant.

On all six frozen TT probes:

- `R^(1)=0` on every leg;
- therefore the `R^2` cubic TT coefficient is analytically zero;
- `R_mn R^mn` has a nonzero cubic TT coefficient.

Direct unreduced covariant evaluation gives the six `alpha=1` Ricci-squared cubic coefficients

`[0.13859380655232462,0.10545702593041664,0.3612771529305377,0.1435006301577732,-0.0938503383460591,0.011015086130857252]`.

Maximum Richardson-extrapolated numerical residual for the analytically zero `R^2` cubic TT direction:

`7.19528079232966e-11`.

After three stochastic propagators and the frozen window factors,

`C3sym_TT=B D2^2`,

with

`B=-617.4340282011477`.

Combining with the Iteration-153 noise coordinate,

`V_C3 = d(N2,C3sym_TT)/d(D2,D0)`

`     = [[5A,A],[2 B D2,0]]`.

Its determinant is

`det(V_C3)=-2 A B D2`.

For every physical stochastic interior point `D2>0`, the supported tangent is therefore **rank 2/2**.

At normalized `D2=1` only for conditioning diagnostics:

- singular values `[1798.6530445678386,177.70085794811004]`;
- `smin/smax=0.0987966292247353`.

The generic rank statement does not depend on this normalization.

### New retained C3/funnel results

`C3-NG-002 — NONLINEAR_CUMULANT_LIFTS_LINEAR_DIFFUSION_DEGENERACY`:

a third symmetric cumulant derived from the same stochastic dynamics separates the spin-2 diffusion direction and lifts the supported comparator tangent from rank 1 to rank 2.

`NG-FUNNEL-012 — CLASSICAL_OM_ACTION_GENERATES_POST_GAUSSIAN_RANK`:

a nonzero gravitational symmetric bispectrum, even when it improves finite-rank identifiability, is not evidence by itself for quantum spacetime. A concrete covariant classical stochastic gravity realization generates it from its own nonlinear Onsager–Machlup action.

Authorities:

- `candidate_gravity/comparators/C3-PQCG-NL-001.md`;
- `analysis/c3_pqcg_nonlinear_bispectrum_iteration154.py`;
- `results/c3_pqcg_nonlinear_bispectrum_iteration154.json`;
- `candidate_gravity/C3_PQCG_NONLINEAR_BISPECTRUM_ITERATION154.md`;
- `research_log/2026-08-31_iteration_154_c3_pqcg_nonlinear_bispectrum.md`;
- `recovery/RECOVERY_DELTA_ITERATION_154.md`.

### C3 blockers after Iteration 154

Supported:

- `N2`;
- `C3sym_TT`.

Still BLOCKED:

- `chi2R_even/odd`: `BLOCKED_ORDERED_RESPONSE_COMPLETION`;
- `soft2`;
- non-TT `tensor_geo` completion;
- threshold coordinate;
- full C3 quotient.

Blocked rows are not zeros.

## C5 status retained

- local on-shell `V_amp`: rank `10/10`, on-shell amplitude space only;
- tree retarded factorization fixed;
- source-completed six-probe protocol PASS_SCOPED;
- EH + two curvature-cubic local response tangent: `6x2`, rank `2/2`, `PASS_SCOPED_WARD_VALIDATED`;
- higher-dimension local columns: BLOCKED;
- loop/nonanalytic columns: BLOCKED;
- `N2`, `C3sym` C5 sectors: BLOCKED.

## Other comparator program

### C4
`ANSATZ-RQIR-KL-002` remains the Gaussian control. Nonlinear C4 still requires a separately frozen finite interacting massive-spin-2 realization.

### Nonlocal / asymptotic safety
Still require one fixed action/truncation each; program labels are not finite comparators.

## Article material

Latest working matrix:

`docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION154.md`.

Iteration 154 materially strengthens the article case against using symmetric gravitational non-Gaussianity as a standalone quantum-gravity witness: the effect is now demonstrated in a fixed classical stochastic comparator, not merely argued abstractly.

## `ANSATZ-003` design state
Still intentionally **not frozen**. No algebraic novelty residual has yet survived the full fixed comparator quotient.

No Fisher/resource work is allowed.

## Immediate next scientific priority — Iteration 155

Attempt the **ordered nonlinear C3 response** from the same full CQ gravity realization.

1. start from the published stochastic Einstein / Onsager–Machlup dynamics, not a new phenomenological kernel;
2. freeze the stochastic-calculus and source-response convention required for a causal second functional derivative;
3. map the resulting response, if uniquely defined, to the existing finite `chi2R_even/odd` protocol;
4. do not assume the order-sensitive/odd component is zero merely because the metric is classical;
5. determine which parts are fixed by `(D2,D0,G_N)` and which require additional published parameters;
6. if the published realization does not uniquely fix the ordered map, record `BLOCKED_ORDERED_C3_SPECIFICATION` and move to the first fixed nonlinear C4 comparator rather than inventing columns;
7. retain C5 higher-local and loop/nonanalytic sectors as BLOCKED;
8. no Fisher/resources and no `ANSATZ-003` before a nonzero residual survives fixed C3/C4/C5/nonlocal/AS quotienting.
