# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending fixed post-Gaussian comparator quotient  
**Authoritative Candidate Gravity front:** **Iteration 157**

## Scientific state in one sentence

The fixed comparator funnel now contains a nonlinear classical-stochastic C3 block and a concrete nonlinear dRGT C4 block in addition to the scoped C5 quantum-GR EFT block. dRGT adds algebraic nonlinear-response directions beyond the currently implemented C5 `R^3` span, but a stricter common-EH/gain quotient exposes the mass direction as near-degenerate (`~0.13%–0.32%` residual) while `alpha3` retains a larger scoped residual (`~4.7%–6.9%`). This demonstrates that formal rank increase must be followed by conditioning/nuisance audits before any Candidate Gravity direction is promoted.

## Frozen model outcomes

### `ANSATZ-PQG-EFT-001`
REFERENCE / NOT PROMOTABLE. Exact C5 identity; retain `CG-NG-003`.

### `ANSATZ-RQIR-CTP-001` v0.1
REJECTED. QG-004 FAIL `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`; retain `CG-NG-004`.

### `ANSATZ-RQIR-KL-002` v0.1
REFERENCE / NOT PROMOTABLE. Exact Gaussian C4/KK mediator degeneracy; retain `CG-NG-005/006`.

## Frozen post-Gaussian protocol

Reduced coordinates after hard locks:

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Novelty pre-gate:

`rank([M,b]) > rank(M)`

or nonzero

`r_beta=(I-MM^+)b`,

only after fixed comparator and nuisance directions are derived and exact hard constraints removed.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-014`.

## C3 status — fixed postquantum-classical gravity comparator

### Linear noise

`N2=A(5D2+D0)`, `A=258.83104475297773`.

One scalar noise coordinate gives rank `1/2` in `(D2,D0)`.

Retain `C3-NG-001 — ONE_NOISE_COORDINATE_COLLAPSES_TWO_DIFFUSION_DIRECTIONS`.

### Nonlinear symmetric cumulant

From the same published covariant PQCG Onsager–Machlup action

`S[g]=1/2 int sqrt(-g)[alpha R_mn R^mn-beta R^2]`,

with

`D2=1/(2alpha)`, `D0=1/[8(alpha-3beta)]`,

the six TT probes give

`C3sym_TT=B D2^2`, `B=-617.4340282011477`.

Hence

`V_C3=[[5A,A],[2BD2,0]]`,

which is rank `2/2` for every physical `D2>0`.

Retain:

- `C3-NG-002 — NONLINEAR_CUMULANT_LIFTS_LINEAR_DIFFUSION_DEGENERACY`;
- `NG-FUNNEL-012 — CLASSICAL_OM_ACTION_GENERATES_POST_GAUSSIAN_RANK`.

### Tree causal response

The same nonlinear Einstein drift gives the nonzero classical response

`chi2R=-G_R Gamma3_EH G_R G_R`.

After hard calibration of the common Newton/GR coupling,

`partial chi2R_tree/partial D2 = partial chi2R_tree/partial D0 = 0`.

Retain:

- `C3-NG-003 — TREE_ORDERED_RESPONSE_IS_COMMON_GR_BOUNDARY`;
- `NG-FUNNEL-013 — NONZERO_CAUSAL_NONLINEAR_RESPONSE_NOT_QUANTUM_CERTIFICATE`.

Still BLOCKED: diffusion-dependent stochastic/MSR-loop ordered corrections, exact `chi2R_odd` selector, non-TT tensor completion, threshold, full C3 quotient.

## C4 status — `C4-DRGT-001`

### Iteration 156 — fixed nonlinear dRGT tangent

Frozen action:

`S=M_Pl^2/2 int sqrt(-g)[R + m^2/2(L2[K]+alpha3 L3[K]+alpha4 L4[K])] + S_m[g]`,

`K=I-sqrt(g^{-1}eta)`, with `alpha0=alpha1=0`, `alpha2=1`.

Frozen point:

`m^2=0.04`, `alpha3=0`, `alpha4=0`.

On TT fields:

`V3_dRGT=m^2(3+alpha3)/8 Tr(H^3)`.

`alpha4` is blind at cubic TT order because `L4` starts quartically.

Tangent parameters `(log m^2,alpha3)` give

- rank `2/2`;
- singular values `[3.062684454379795,0.4175708275716087]`;
- `smin/smax=0.13634144772501477`.

Against only the existing two C5 local `R^3` columns, residual fractions are approximately `[0.1928,0.1365]` and combined rank rises from 2 to 4.

Retain:

- `C4-NG-001 — ALPHA4_CUBIC_TT_BLIND`;
- `C4-NG-002 — DRGT_EXPANDS_SCOPED_NONLINEAR_COMPARATOR_SPAN`.

### Iteration 157 — shared-boundary/gain quotient

Base span:

`M=[EH_common,C5_Ricci3,C5_Riemann3,response_gain_at_dRGT_reference]`.

Across raw coordinates plus three invertible row normalizations:

- base rank remains `4`;
- combined base+dRGT rank remains `6`;
- `log m^2` residual fraction range: `0.001256944940945903 ... 0.003203089011461978`;
- `alpha3` residual fraction range: `0.047221203241976296 ... 0.06942706305159267`.

Interpretation:

- `log m^2`: **NEAR_DEGENERATE_NOT_PROMOTABLE**;
- `alpha3`: **SCOPED_RESIDUAL_SURVIVES**;
- neither is a Candidate Gravity novelty certificate because C4/C5 remain incomplete.

Retain:

- `C4-NG-003 — COMMON_BOUNDARY_GAIN_NEARLY_ABSORBS_MASS_DIRECTION`;
- `NG-FUNNEL-014 — ALGEBRAIC_RANK_REQUIRES_CONDITIONING_AUDIT`.

C4 still BLOCKED: helicity-0/1 completion, Vainshtein/nonperturbative response, `N2/C3sym`, alpha4 higher-point direction, full C4 quotient.

Authorities:

- `candidate_gravity/comparators/C4-DRGT-001.md`;
- `analysis/c4_drgt_nonlinear_tangent_iteration156.py`;
- `results/c4_drgt_nonlinear_tangent_iteration156.json`;
- `analysis/c4_drgt_shared_boundary_quotient_iteration157.py`;
- `results/c4_drgt_shared_boundary_quotient_iteration157.json`;
- `candidate_gravity/C4_DRGT_SHARED_BOUNDARY_QUOTIENT_ITERATION157.md`;
- `recovery/RECOVERY_DELTA_ITERATION_157.md`.

Literature anchors:

- de Rham, *Massive Gravity*, Living Rev. Relativity 17, 7 (2014);
- Hassan & Rosen, arXiv:1106.3344;
- de Rham, Gabadadze & Tolley, arXiv:1107.3820, arXiv:1108.4521.

## C5 status retained

- on-shell local `V_amp`: `12x10`, rank `10/10`, on-shell only;
- tree retarded factorization fixed;
- source-completed six-probe protocol PASS_SCOPED;
- EH + `Ricci^3/Riemann^3` local response: `6x2`, rank `2/2`, Ward validated;
- higher local directions: BLOCKED;
- loop/nonanalytic directions: BLOCKED;
- C5 `N2/C3sym`: BLOCKED.

## Article material

Latest matrix:

`docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION157.md`.

The future model paper can now distinguish consistency FAIL, exact comparator identity, order/protocol blindness, and near-degeneracy after nuisance quotient using explicit calculations rather than generic discussion.

## `ANSATZ-003` design state

Still intentionally **not frozen**. No robust residual has yet survived the full fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.

Fisher/resources remain forbidden.

## Immediate next scientific priority — Iteration 158

Instantiate one fixed strong QG comparator outside the existing C3/C4/C5 blocks.

Preferred route:

1. freeze one explicit covariant nonlocal/form-factor gravity action with finite parameters;
2. derive its finite two-/three-point response on the same six-probe protocol;
3. apply the common EH/gain quotient and compare with the current C4+C5 span;
4. if a clean finite nonlocal map is unavailable without arbitrary choices, use one concrete asymptotic-safety vertex truncation instead;
5. never use a broad program/class label as a tangent block;
6. keep unavailable sectors BLOCKED;
7. no `ANSATZ-003`, Fisher or resources until a quantitatively robust residual survives the full fixed comparator funnel.
