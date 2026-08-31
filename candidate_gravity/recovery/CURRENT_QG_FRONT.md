# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 173**

## Scientific state in one sentence

Standalone propagator/amplitude/spectral novelty routes are closed; the search now lives in source-completed, two-point-amputated CTP relation space, and the fixed PQCG comparator has reached a documented nonlinear MSR boundary because its published linear conserved-diffusion completion does not uniquely determine diffusion-dependent cubic ordered relation vertices.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged. Iteration 173 sharpens a comparator blocker but does not close a new rubric block or produce a residual surviving all fixed comparator families.

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

Retain `C5-NG-004` through `C5-NG-006`, `C4-NG-008`, `ABS-SHAPE-001` through `ABS-SHAPE-005`, and `NG-FUNNEL-024/026/028/029/030`.

## Linked/amputated CTP authority — Iterations 171–173

Condition nonlinear comparison on the same measured two-point CTP matrix and compare amputated/source-completed three-point kernels using

`G3_abc = - G_aa' G_bb' G_cc' Gamma3_a'b'c'`.

Iteration 171 showed that external-leg dressing disappears after fixed-convention amputation to `1.11e-16`. For a symmetric closed-unitary cubic action,

`Gamma_aar=0`,

`Gamma_aaa=Gamma_arr/4`.

This is generic quantum C4/C5 structure, not a gravity witness.

### Iteration 172 finite relation-level matrix

Use six frozen amputated kinematic rows with raw coordinates per row

`(Gamma_arr,Gamma_aar,Gamma_aaa,WardLock)`.

A conservative generic closed-unitary C4/C5 comparator is allowed one independent cubic amplitude per row while preserving

`Gamma_aar=0`, `Gamma_aaa=Gamma_arr/4`, `WardLock=0`.

Add only the fixed supported C3 PQCG tree direction from Iteration 155.

Raw comparator matrix: `24x7`, rank `7/7`, `s_min/s_max=0.0126780602`.

Relation coordinates per row:

`R_aar=Gamma_aar`,

`R_unit=Gamma_aaa-Gamma_arr/4`,

`R_W=WardLock`.

All generic closed-unitary C4/C5 amplitude columns vanish exactly. The supported fixed C3 tree leaves one relation direction `R_unit=-B_EH/4`, norm `4.917063349196141`; supported relation rank is `1`.

Retain `CTP-NG-003`, `CTP-NG-004`, `NG-FUNNEL-032`.

### Iteration 173 fixed PQCG MSR audit

Recovered the exact Iterations 153–155 PQCG authority and audited it against the 2026 Oppenheim–Sajjad OM/JD/MSR analysis.

The published stochastic-mode analysis shows that the naive generalized-DeWitt JD/MSR functional does **not** reproduce the OM two-point function. A conserved diffusion matrix resolves that mismatch, but the explicit conserved-diffusion SDE is linearized. The nonlinear covariant field dependence needed for the diffusion-dependent cubic two-response-field vertex is not fixed by the current comparator authority.

Structural underdetermination certificate:

`S=t*(L*h+g*h^2/2-J)-1/2*t*(D0+lambda*h)*t`.

At `h=t=0`, the linear Hessian is

`[[0,L],[L,-D0]]`,

independent of `lambda`, whereas the cubic vertices are

`Gamma_t_h_h=g`,

`Gamma_t_t_h=-lambda`,

`Gamma_t_t_t=0`.

Therefore the fixed linear covariance plus nonlinear drift do not determine the two-response-field cubic vertex. In addition, the PQCG classical MSR response field is not automatically identical to the RQIR metric CTP `a` field, so no missing `Gamma_aar/Gamma_aaa` column is authorized without an explicit same-convention map.

Status:

`BLOCKED_C3_CTP_ORDERED_COMPLETION`.

Retain:

- `C3-NG-005 — LINEAR_NOISE_PLUS_NONLINEAR_DRIFT_DO_NOT_FIX_ORDERED_MSR_CUBIC_VERTEX`;
- `NG-FUNNEL-033 — OM_TO_MSR_CUBIC_COMPLETION_REQUIRES_NONLINEAR_CONSERVED_DIFFUSION_AND_EXPLICIT_CTP_MAP`.

This is operational underdetermination, **not** a consistency FAIL of PQCG, not a zero column, not an exact comparator identity, and not a novelty certificate.

The supported Iteration-172 C3 tree relation direction remains authoritative. The remaining relation-space complement is still not promotable.

## Current comparator implications

### C3 postquantum-classical

Supported: `N2`, nonlinear `C3sym`, common-EH tree causal response, and the corresponding one relation-level classical tree direction. Full diffusion/MSR ordered metric-CTP cubic completion is `BLOCKED_C3_CTP_ORDERED_COMPLETION` because a nonlinear conserved diffusion kernel plus explicit MSR-to-CTP map are not fixed.

### C4

Fixed dRGT tree remains a scoped comparator. Generic positive linear spectra are exactly C4-reproducible. Generic closed quantum cubic self-interaction occupies the exact closed-unitary relation subspace. Loop/helicity/noise completion remains BLOCKED.

### C5

EH/local tree shares the same closed-unitary CTP relation. Local TT comparator saturation and leading absorptive loop envelopes remain authoritative. C5 loop/noise three-point CTP completion remains BLOCKED.

### Nonlocal / asymptotic safety

Two-point form-factor/spectral information is calibrated external-leg data after amputation. Nonlinear real-time source-completed CTP vertex relations remain the next relevant comparator target and are BLOCKED where not derived.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.

Fisher/resources remain FORBIDDEN.

A future residual must be a linked multi-point/CTP/tensor/Ward relation that survives the fixed C3/C4/C5/nonlocal/AS comparator quotient. A WardLock violation is a consistency FAIL, not novelty.

## Current authorities

### Iteration 172
- `analysis/ctp_relation_comparator_iteration172.py`;
- `results/ctp_relation_comparator_iteration172.json`;
- `candidate_gravity/CTP_RELATION_COMPARATOR_ITERATION172.md`;
- `research_log/2026-08-31_iteration_172_ctp_relation_comparator.md`;
- `recovery/RECOVERY_DELTA_ITERATION_172.md`.

### Iteration 173
- `analysis/c3_pqcg_msr_completion_audit_iteration173.py`;
- `results/c3_pqcg_msr_completion_audit_iteration173.json`;
- `candidate_gravity/C3_PQCG_MSR_COMPLETION_AUDIT_ITERATION173.md`;
- `research_log/2026-08-31_iteration_173_pqcg_msr_completion_audit.md`;
- `recovery/RECOVERY_DELTA_ITERATION_173.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION173.md`.

## Immediate next scientific priority — Iteration 174

Freeze one concrete **covariant nonlinear nonlocal gravity action** with declared form-factor and Lorentzian prescription before inspecting any candidate residual.

Required order:

1. recover the existing nonlocal comparator authority and its two-point form factors;
2. derive the source-completed cubic vertex from the same covariant action, rather than inferring it from the propagator alone;
3. test whether the two-point form factors uniquely determine the amputated cubic real-time relation or whether independent cubic form factors enter;
4. if independent form-factor data or an unprovided retarded continuation are required, record `BLOCKED_NONLOCAL_CTP_CUBIC_COMPLETION`, never zero-fill;
5. only after the fixed nonlocal relation audit proceed to the asymptotic-safety real-time relation completion;
6. do not create `ANSATZ-003` and do not run Fisher/resources until a nonzero algebraic residual survives the full fixed comparator quotient.
