# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 171**

## Scientific state in one sentence

Standalone propagator, finite spacelike TT shape and positive timelike spectral-shape novelty routes are now closed as promotion mechanisms: local C5 saturates the frozen spacelike protocol, positive linear TT spectra are exactly C4-mediator reproducible, and Iteration 171 therefore moves the search to **source-completed, two-point-amputated CTP three-point relations**, where external-leg spectral dressing is calibrated away before any novelty test.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iterations 168–171. These iterations eliminate false-positive routes and sharpen comparator conditioning but do not yet produce a robust Candidate Gravity residual or parent dynamics.

## Mandatory provenance / nomenclature

1. Iteration 163 dRGT target mapping: first `d/d log(m^2)`, second `d/d alpha3`; `alpha4` remains cubic-TT blind.
2. Iteration-166 onward `A_odd` is the frequency-odd imaginary part of **linear** `chi1R`, not post-Gaussian `chi2R_odd`.
3. Iteration-171 CTP vertices use `h_±=r±a/2` and factorial-normalized `Gamma_arr/2!`, `Gamma_aaa/3!` conventions.

Retain `PROVENANCE-CORR-001`.

## Frozen conceptual observable hierarchy

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Hard constraints precede profiling/Fisher. Unsupported comparator coordinates are BLOCKED, never zero-filled.

## Spacelike ordered-TT authority through Iteration 165

The target-independent local C5 completion through the frozen dimension-12 cutoff gives a `12x12` matrix of rank `12/12` on the 12 frozen spacelike TT rows and absorbs the corrected dRGT tangents to machine precision.

Retain:

- `C5-NG-003 — DIMENSION12_LOCAL_C5_CUBIC_SUBSET_SATURATES_ENRICHED_12ROW_TT_PROTOCOL`;
- `C4-NG-007 — ITERATION164_DRGT_RESIDUAL_ABSORBED_BY_TARGET_INDEPENDENT_DIMENSION12_C5_COMPLETION`;
- `NG-FUNNEL-022` and `NG-FUNNEL-023`.

Do not search for novelty by adding target-optimized rows in this saturated sector.

## Timelike conserved-TT linear absorptive authority — Iterations 166–169

Eight timelike rows `s_i=0.004*i`, `i=1..8`, use `k=(omega,0,0,0)` and conserved traceless `T_ij=diag(1,-1,0)/sqrt(2)`.

Define

`A_odd=[Im chi1R(+omega)-Im chi1R(-omega)]/(2*pi)`.

A local Hermitian tree EFT is absorptively zero off pole. The full leading massless one-loop curvature-squared C5 TT family is a single constant shape. At the next conservative `O(p^6)` massless order, the allowed odd-absorptive shape envelope is contained in `span{x,x log x}` with `x=s/s_max`.

Profiling `[1,x,x log x]` leaves five finite frequency-shape dimensions.

Retain:

- `C5-NG-004 — LOCAL_HERMITIAN_TREE_EFT_CANNOT_SATURATE_OFF_POLE_ABSORPTIVE_BLOCK`;
- `C5-NG-005 — LEADING_MASSLESS_ONE_LOOP_TT_ABSORPTIVE_SPAN_IS_ONE_DIMENSIONAL_CONSTANT_SHAPE`;
- `C5-NG-006 — NEXT_ORDER_P6_MASSLESS_TT_ABSORPTIVE_ENVELOPE_IS_SPAN_X_XLOGX`;
- `ABS-SHAPE-001` through `ABS-SHAPE-004`;
- `NG-FUNNEL-024`, `026`, `028`, `029`.

## General positive linear-spectral C4 identity — Iteration 170

For any physical conserved-traceless TT response with positive Källén–Lehmann measure,

`chi_R^TT = Z0 D_R(0) + int dmu2 rho_TT(mu2) D_R(mu2)`, `rho_TT>=0`,

an exact direct integral of independent positive-norm massive spin-2 mediators with coupling density `sqrt(rho_TT)` reproduces the same retarded two-point kernel. With matching Gaussian covariance/state it also reproduces the Gaussian Hadamard kernel and full Gaussian CTP influence functional.

This generalizes the Iteration-141 exact `KL-002` C4 identity to arbitrary positive TT spectral measures.

Consequences:

- poles, positive continua, thresholds, branch cuts and arbitrary positive finite-frequency spectral shapes are C4-reproducible at linear-Gaussian level;
- the five-dimensional Iteration-169 C5-null remainder is not gravity-specific by itself;
- spectral negativity is not a novelty certificate and instead triggers physical-observability/gauge/positivity/ghost/unitarity gates.

Retain:

- `C4-NG-008 — POSITIVE_LINEAR_TT_SPECTRAL_RESPONSE_IS_EXACTLY_REPRESENTABLE_BY_ORDINARY_MEDIATOR_CONTINUUM`;
- `ABS-SHAPE-005 — FINITE_FREQUENCY_LINEAR_SPECTRAL_SHAPE_CANNOT_CERTIFY_GRAVITY_SPECIFIC_NOVELTY_AGAINST_C4`;
- `NG-FUNNEL-030 — LINEAR_SPECTRAL_RESIDUAL_REQUIRES_A_LINKED_NONLINEAR_OR_POST_GAUSSIAN_GRAVITY_RELATION_FOR_PROMOTION`.

Finite-frequency Lorentzian-AS spectral reproduction remains useful for comparator characterization/article work but is no longer a prerequisite for deciding whether a standalone linear spectrum can seed `ANSATZ-003`.

## Linked/amputated CTP three-point protocol — Iteration 171

The two-point CTP kernel is now treated as measured/shared data. In the fixed source-completed metric convention, use the exact relation

`G3_abc = - G_aa' G_bb' G_cc' Gamma3_a'b'c'`

to compare amputated/source-completed three-point kernels rather than raw responses.

A six-row control with nontrivial momentum-dependent external-leg dressing changes the raw nonlinear response by `25.56%`, while the amputated cubic kernel is recovered with maximum error `1.11e-16`.

Retain:

`CTP-NG-002 — TWO_POINT_EXTERNAL_LEG_DRESSING_DISAPPEARS_AFTER_FIXED_CONVENTION_THREE_POINT_AMPUTATION`.

For any symmetric cubic closed-unitary action `S3=B(h,h,h)/3!`, the `r/a` transform gives

`S3[h+] - S3[h-] = 1/2 B(a,r,r) + 1/24 B(a,a,a)`.

Hence, in the frozen vertex normalization,

`Gamma_aar=0`,

`Gamma_aaa=Gamma_arr/4`.

This is generic closed quantum dynamics, not gravity-specific. It is shared by C5 quantum-gravity tree actions and ordinary quantum C4 cubic mediators.

Retain:

- `CTP-NG-001 — CLOSED_UNITARY_CUBIC_AAA_OVER_ARR_RATIO_IS_NOT_GRAVITY_SPECIFIC`;
- `NG-FUNNEL-031 — CANDIDATE_RESIDUAL_MUST_BE_A_LINKED_CTP_VERTEX_RELATION_AFTER_TWO_POINT_AMPUTATION`.

## Current comparator implications

### C3 postquantum-classical

Supported: `N2`, a nonlinear `C3sym` direction from the same OM action, and common-EH tree causal response. Full source-completed `r/a` vertex including diffusion/MSR ordered pieces remains BLOCKED.

### C4

Fixed dRGT tree nonlinear response remains a scoped comparator. Generic positive linear spectra are already closed by the direct-integral identity. A closed quantum C4 cubic self-interaction shares the generic `Gamma_aaa/Gamma_arr=1/4` CTP relation, so that relation is not a gravity witness. Loop/helicity/noise completion remains BLOCKED.

### C5

EH/local tree CTP structure shares the same closed-unitary relation. C5 loop/noise three-point components remain to be instantiated in the same finite source-completed protocol.

### Nonlocal / asymptotic safety

Their propagator/form-factor/spectral information becomes calibrated external-leg data after amputation. Their nonlinear real-time source-completed CTP vertex relations remain relevant and BLOCKED where not derived.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.

Fisher/resources remain FORBIDDEN.

The next novelty carrier must be a linked multi-point/CTP/tensor/Ward relation, not a raw two-point or raw three-point amplitude.

## Current authorities

### Iteration 169
- `analysis/c5_nlo_absorptive_shape_envelope_iteration169.py`;
- `results/c5_nlo_absorptive_shape_envelope_iteration169.json`;
- `candidate_gravity/C5_NLO_ABSORPTIVE_SHAPE_ENVELOPE_ITERATION169.md`;
- `recovery/RECOVERY_DELTA_ITERATION_169.md`.

### Iteration 170
- `analysis/linear_spectral_c4_no_go_iteration170.py`;
- `results/linear_spectral_c4_no_go_iteration170.json`;
- `candidate_gravity/LINEAR_SPECTRAL_C4_NO_GO_ITERATION170.md`;
- `recovery/RECOVERY_DELTA_ITERATION_170.md`;
- historical authority: `docs/CANDIDATE_GRAVITY_C4_GAUSSIAN_DEGENERACY_ITERATION141.md`.

### Iteration 171
- `analysis/linked_ctp_vertex_protocol_iteration171.py`;
- `results/linked_ctp_vertex_protocol_iteration171.json`;
- `candidate_gravity/LINKED_CTP_VERTEX_PROTOCOL_ITERATION171.md`;
- `research_log/2026-08-31_iteration_171_linked_ctp_vertex_protocol.md`;
- `recovery/RECOVERY_DELTA_ITERATION_171.md`.

## Immediate next scientific priority — Iteration 172

Construct the first finite **relation-level CTP comparator matrix**.

Required order:

1. use finite amputated coordinates `Gamma_arr`, `Gamma_aar`, `Gamma_aaa` in the frozen source convention;
2. treat the closed-unitary C4/C5 relation as comparator structure, not novelty;
3. add a Ward/source tensor-lock coordinate tying `Gamma_arr` to the same stress coupling/inverse propagator;
4. instantiate only the C3 relation pieces actually supported by the fixed PQCG realization and preserve the rest as BLOCKED;
5. compute rank/quotient in relation space before proposing any Candidate Gravity dynamics;
6. only a residual outside fixed C3/C4/C5/nonlocal/AS relation spans may earn robust-residual readiness points or motivate `ANSATZ-003`.
