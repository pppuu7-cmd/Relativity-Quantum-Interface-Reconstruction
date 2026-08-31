# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 175**

## Scientific state in one sentence

Standalone propagator/amplitude/spectral novelty routes are closed; Iterations 171–175 move the search to source-completed, two-point-amputated CTP tensor relations, and Iteration 175 replaces the too-coarse scalar `WardLock` by a soft Ward decomposition in which the two-point-determined longitudinal cubic piece is projected as shared consistency structure while the independent linearized-Riemann/transverse three-point form factor defines the next finite comparator space.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iteration 175. Recent iterations remove false-positive routes and sharpen comparator geometry but do not yet produce a full comparator-subtracted residual or parent dynamics.

## Mandatory provenance / nomenclature

1. Iteration 163 dRGT mapping: first target `d/d log(m^2)`, second `d/d alpha3`; `alpha4` remains cubic-TT blind.
2. Iteration-166 onward `A_odd` is the frequency-odd imaginary part of **linear** `chi1R`, not post-Gaussian `chi2R_odd`.
3. Iteration-171 onward metric CTP vertices use `h_±=r±a/2` and factorial-normalized `Gamma_arr/2!`, `Gamma_aaa/3!` conventions.
4. Retain `PROVENANCE-CORR-001`.

## Frozen conceptual observable hierarchy

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Hard constraints precede profiling/Fisher. Unsupported comparator coordinates are BLOCKED, never zero-filled.

## Spacelike TT authority — through Iteration 165

The target-independent local C5 completion through the frozen dimension-12 cutoff gives a `12x12` matrix of rank `12/12` on the 12 frozen spacelike TT rows and absorbs corrected dRGT tangents to machine precision.

Retain `C5-NG-003`, `C4-NG-007`, `NG-FUNNEL-022`, `NG-FUNNEL-023`.

Do not search for novelty by adding target-optimized rows in that saturated sector.

## Timelike linear absorptive authority — Iterations 166–170

Eight timelike conserved-TT rows use `A_odd=[Im chi1R(+omega)-Im chi1R(-omega)]/(2*pi)`.

Local Hermitian tree EFT is absorptively zero off pole. Leading massless one-loop C5 is a constant shape; the conservative next `O(p^6)` massless envelope is `span{x,x log x}`. Profiling `[1,x,x log x]` leaves five finite shape dimensions, but Iteration 170 closes standalone positive linear spectral shape as gravity-specific novelty: any positive Källén–Lehmann TT kernel is exactly reproducible by an ordinary positive-norm C4 mediator continuum, with matched Gaussian covariance reproducing the Gaussian CTP layer.

Retain `C5-NG-004` through `C5-NG-006`, `C4-NG-008`, `ABS-SHAPE-001` through `ABS-SHAPE-005`, `NG-FUNNEL-024/026/028/029/030`.

## Linked/amputated CTP authority — Iterations 171–175

Condition nonlinear comparison on the same measured two-point CTP matrix and compare amputated/source-completed three-point kernels using

`G3_abc = - G_aa' G_bb' G_cc' Gamma3_a'b'c'`.

Iteration 171 showed that external-leg dressing disappears after fixed-convention amputation to `1.11e-16`. For a symmetric closed-unitary cubic action,

`Gamma_aar=0`,

`Gamma_aaa=Gamma_arr/4`.

This is generic quantum structure, not a gravity witness.

### Iteration 172 finite relation-level matrix

Use six frozen amputated kinematic rows with raw coordinates per row

`(Gamma_arr,Gamma_aar,Gamma_aaa,WardLock)`.

The conservative generic closed-unitary C4/C5 comparator is allowed one independent cubic amplitude per row while preserving

`Gamma_aar=0`, `Gamma_aaa=Gamma_arr/4`, `WardLock=0`.

Add the supported fixed C3 PQCG tree direction from Iteration 155.

Raw comparator matrix: `24x7`, rank `7/7`, `s_min/s_max=0.0126780602`.

Relation coordinates:

`R_aar=Gamma_aar`,

`R_unit=Gamma_aaa-Gamma_arr/4`,

`R_W=WardLock`.

All generic closed-unitary C4/C5 amplitude columns vanish exactly. The supported fixed C3 tree leaves one relation direction `R_unit=-B_EH/4`, norm `4.917063349196141`; supported relation rank `1`.

Retain `CTP-NG-003`, `CTP-NG-004`, `NG-FUNNEL-032`.

### Iteration 173 fixed PQCG MSR audit

The available conserved-diffusion PQCG authority is linearized. Linear covariance plus nonlinear drift do not uniquely determine the two-response-field cubic MSR vertex; the classical MSR response field is also not automatically identical to the RQIR metric CTP `a` field.

Status:

`BLOCKED_C3_CTP_ORDERED_COMPLETION`.

Retain:

- `C3-NG-005 — LINEAR_NOISE_PLUS_NONLINEAR_DRIFT_DO_NOT_FIX_ORDERED_MSR_CUBIC_VERTEX`;
- `NG-FUNNEL-033 — OM_TO_MSR_CUBIC_COMPLETION_REQUIRES_NONLINEAR_CONSERVED_DIFFUSION_AND_EXPLICIT_CTP_MAP`.

This is operational underdetermination, not a consistency FAIL, zero column, exact comparator identity, or novelty certificate.

### Iteration 174 fixed nonlocal cubic/CTP audit

Use `QG-NL-EXP-001`:

`S = Mpl^2/2 int sqrt(-g) [R + G_mn F(Box) R^mn] + S_m`,

`F(Box)=(exp(-lambda Box)-1)/Box`.

Its cubic nonlocal action contains

`G2 F0 R1 + G1 F0 R2 + sqrtg1 G1 F0 R1 + G1 (delta F)_1 R1`.

The exact operator variation follows from

`F(A)=-int_0^lambda exp(-alpha A)dalpha`,

so

`delta F(A)=int_0^lambda dalpha int_0^alpha du exp(-(alpha-u)A)(delta A)exp(-uA)`.

Between eigenmodes its coefficient is the divided difference `[F(a)-F(b)]/(a-b)`; six reproducible checks, including the diagonal limit, give zero numerical discrepancy.

Therefore propagator-only information misses a genuine cubic operator insertion and a full covariant parent action is required.

For the exact frozen `QG-NL-EXP-001` action, tree cubic structure is fixed in principle; for a broad weakly-nonlocal class, the same two-point kernel does not fix the cubic sector because independent higher-curvature potentials/form-factor structures may enter.

However, in the Iteration-172 coarse relation coordinates, any closed-unitary cubic action obeys `Gamma_aar=0`, `Gamma_aaa=Gamma_arr/4`, and a source-completed diffeomorphism-invariant parent action has `WardLock=0`. Hence the full arbitrary nonlocal tree amplitude is annihilated exactly:

- raw six-row generic amplitude rank `6`;
- relation rank `0`;
- max relation entry `0.0`.

This is not a zero raw cubic vertex. It proves the coarse relation map is too weak.

Retain:

- `NL-NG-003 — COVARIANT_NONLOCAL_CUBIC_VERTEX_CONTAINS_OPERATOR_FRECHET_VARIATION_NOT_VISIBLE_IN_PROPAGATOR_ONLY_REASONING`;
- `CTP-NG-005 — CLOSED_UNITARY_DIFFEO_INVARIANT_NONLOCAL_TREE_ACTION_IS_ANNIHILATED_BY_CURRENT_COARSE_CTP_RELATION_MAP`;
- `NG-FUNNEL-034 — ZERO_WARD_LOCK_PLUS_GENERIC_UNITARY_RA_RELATION_CANNOT_DISTINGUISH_QUANTUM_GRAVITY_FAMILIES`.

### Iteration 175 tensor/soft Ward decomposition

The scalar `WardLock` coordinate is now demoted to a consistency check. Freeze instead the 1PI soft decomposition

`Gamma3_soft = W[K2] + Rlin_soft : B3 + higher-soft-order`.

`W[K2]` is the Ward/covariantization-determined part fixed by the same quadratic inverse kernel and source convention. It is exact shared structure and must be projected before novelty ranking.

`Rlin_soft:B3` is the first separately gauge-invariant transverse/nonminimal three-point structure not fixed by the two-point kernel alone.

Tensor certificate with null `k=(1,0,0,1)`:

- pure-gauge polarization: `max |Rlin|=5.55e-17`, norm `1.36e-16`;
- normalized TT plus polarization: `max |Rlin|=0.35355339059327373`, norm `2` to floating-point precision.

Under `k -> a k`, TT Riemann norm scales as `a^2`: ratios `0.25`, `4`, `9.000000000000002` for `a=0.5,2,3`; maximum scaling error `1.78e-15`.

Therefore the independent gauge-invariant three-point structure enters at sub-subleading `O(k^2)` order.

Define for each of the six frozen amputated rows

`B_T(i)=P_T[Gamma_arr(i)-W_i[K2]]`.

This gives a six-dimensional transverse relation space **before** comparator subtraction. It is not a novelty certificate: local C5 EFT, nonlinear C4, nonlocal gravity and asymptotic-safety vertices may populate it.

Retain:

- `SOFT-NG-001 — WARD_DETERMINED_SOFT_CUBIC_PART_IS_SHARED_STRUCTURE_FIXED_BY_THE_TWO_POINT_KERNEL`;
- `SOFT-NG-002 — LINEARIZED_RIEMANN_THREE_POINT_FORM_FACTOR_IS_GAUGE_INVARIANT_AND_ENTERS_AT_SUBSUBLEADING_K2_ORDER`;
- `NG-FUNNEL-035 — REPLACE_SCALAR_WARDLOCK_WITH_WARD_SUBTRACTED_TRANSVERSE_CUBIC_COORDINATES`.

## Current comparator implications

### C3 postquantum-classical

Supported: `N2`, nonlinear `C3sym`, common-EH tree causal response, and one relation-level classical tree direction. Full diffusion/MSR ordered metric-CTP cubic completion remains `BLOCKED_C3_CTP_ORDERED_COMPLETION`; no `B_T` column is authorized yet.

### C4

Fixed dRGT tree remains a scoped comparator. Generic positive linear spectra are exactly C4-reproducible. Generic closed quantum cubic structure is shared, but the new transverse `B_T` projection must be computed from a fixed C4 parent realization.

### C5

EH/local tree shares the generic closed-unitary relation. Local diffeomorphism-invariant EFT operators can populate sub-subleading transverse soft structure. The immediate next comparator gate is therefore a finite target-independent C5 `B_T` operator basis.

### Nonlocal

The exact frozen exponential parent action fixes its tree cubic structure in principle, including the Fréchet operator insertion. Its projection into the new `B_T` coordinates remains to be computed after the C5 basis is frozen.

### Asymptotic safety

Two-point spectral information is calibrated external-leg data after amputation. Real-time/source-completed three-point `B_T` completion remains BLOCKED and should follow the finite C5/C4/nonlocal transverse audits.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.

Fisher/resources remain FORBIDDEN.

A future residual must survive in the Ward-subtracted transverse multi-point tensor space after all fixed comparator directions are removed.

## Current authorities

### Iteration 172
- `analysis/ctp_relation_comparator_iteration172.py`;
- `results/ctp_relation_comparator_iteration172.json`;
- `candidate_gravity/CTP_RELATION_COMPARATOR_ITERATION172.md`;
- `recovery/RECOVERY_DELTA_ITERATION_172.md`.

### Iteration 173
- `analysis/c3_pqcg_msr_completion_audit_iteration173.py`;
- `results/c3_pqcg_msr_completion_audit_iteration173.json`;
- `candidate_gravity/C3_PQCG_MSR_COMPLETION_AUDIT_ITERATION173.md`;
- `recovery/RECOVERY_DELTA_ITERATION_173.md`.

### Iteration 174
- `analysis/nonlocal_ctp_cubic_structure_iteration174.py`;
- `results/nonlocal_ctp_cubic_structure_iteration174.json`;
- `candidate_gravity/NONLOCAL_CTP_CUBIC_STRUCTURE_ITERATION174.md`;
- `research_log/2026-08-31_iteration_174_nonlocal_ctp_cubic_structure.md`;
- `recovery/RECOVERY_DELTA_ITERATION_174.md`.

### Iteration 175
- `analysis/soft_ward_transverse_decomposition_iteration175.py`;
- `results/soft_ward_transverse_decomposition_iteration175.json`;
- `candidate_gravity/SOFT_WARD_TRANSVERSE_DECOMPOSITION_ITERATION175.md`;
- `research_log/2026-08-31_iteration_175_soft_ward_transverse_decomposition.md`;
- `recovery/RECOVERY_DELTA_ITERATION_175.md`.

## Immediate next scientific priority — Iteration 176

Instantiate a **finite target-independent C5 transverse soft comparator basis** in the six `B_T` rows.

Required order:

1. freeze the local diffeomorphism-invariant C5 EFT operator subset capable of modifying sub-subleading soft structure at the declared truncation order;
2. project its source-completed cubic vertices into the six Ward-subtracted transverse coordinates;
3. compute rank, SVD tolerance and authority map without target optimization;
4. only after C5 is finite add fixed C4 and nonlocal transverse columns;
5. preserve C3 ordered and AS real-time transverse entries as BLOCKED unless explicitly derived;
6. no `ANSATZ-003`, Fisher or resources until a nonzero residual survives the full transverse comparator quotient.
