# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 170**

## Scientific state in one sentence

The spacelike ordered-TT sector is finitely saturated by an authorized local C5 dimension-12 basis; the timelike conserved-TT absorptive sector escapes local-tree interpolation and can be profiled order-by-order against massless C5 loop shapes, but Iteration 170 proves a stronger limitation: **any positive physical linear TT Källén–Lehmann spectral response is exactly reproducible by an ordinary positive-norm C4 mediator direct integral**, so no two-point spectral shape alone can seed a gravity-specific Candidate Gravity residual.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged through Iterations 168, 169 and 170. Those iterations materially close false-positive comparator directions but do not produce a gravity-specific residual or parent dynamics.

## Mandatory provenance / nomenclature

1. Iteration 163 dRGT target mapping:
   - first target: `d/d log(m^2)`;
   - second target: `d/d alpha3`;
   - `alpha4`: cubic-TT blind because `L4[K]` starts quartic.

2. Iteration-166 onward `A_odd` is the frequency-odd imaginary part of **linear** `chi1R`, not post-Gaussian `chi2R_odd`.

Retain `PROVENANCE-CORR-001`.

## Frozen conceptual observable hierarchy

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Hard constraints precede profiling/Fisher. Unsupported comparator coordinates are BLOCKED, never zero-filled.

## Spacelike ordered-TT authority through Iteration 165

The 12-row spacelike protocol with target-independent local C5 completion through the frozen dimension-12 cutoff has

`C5 matrix = 12x12`, `rank=12/12`.

Corrected dRGT tangents are absorbed to machine precision on that finite protocol.

Retain:

- `C5-NG-003 — DIMENSION12_LOCAL_C5_CUBIC_SUBSET_SATURATES_ENRICHED_12ROW_TT_PROTOCOL`;
- `C4-NG-007 — ITERATION164_DRGT_RESIDUAL_ABSORBED_BY_TARGET_INDEPENDENT_DIMENSION12_C5_COMPLETION`;
- `NG-FUNNEL-022 — FINITE_PROTOCOL_RESIDUAL_MUST_SURVIVE_THEORY_AUTHORIZED_COMPARATOR_BASIS_COMPLETION`;
- `NG-FUNNEL-023 — ONCE_ONE_AUTHORIZED_COMPARATOR_SPANS_THE_FINITE_ROW_SPACE, ADDITIONAL_BLOCKED_COMPARATORS_CANNOT_RESTORE_A_RESIDUAL_IN_THAT_SAME_SPACE`.

Do not search for novelty by adding target-optimized spacelike rows inside this saturated sector.

## Timelike conserved-TT linear absorptive protocol — Iterations 166–167

Freeze eight timelike invariants

`s_i=0.004*i`, `i=1..8`,

with `k=(omega,0,0,0)`, all `s_i<0.04`, and conserved traceless source/detector

`T_0mu=0`, `T_ij=diag(1,-1,0)/sqrt(2)`.

Define

`A_odd(s)=[Im chi1R(+omega)-Im chi1R(-omega)]/(2*pi)`.

Source-map certificate: conservation, trace and projector errors vanish to numerical precision and `T:P2:T=1` within `2.22e-16`.

A real local Hermitian tree EFT is absorptively zero off pole. A target-independent constant profile removes the universal leading massless logarithmic onset and leaves seven frequency-shape dimensions.

Retain:

- `C5-NG-004 — LOCAL_HERMITIAN_TREE_EFT_CANNOT_SATURATE_OFF_POLE_ABSORPTIVE_BLOCK`;
- `ABS-SHAPE-001 — CONSERVED_TT_SOURCE_MAP_PRESERVES_TIMELIKE_SPECTRAL_SHAPE`;
- `ABS-SHAPE-002 — CONSTANT_LOG_NULL_QUOTIENT_LEAVES_SEVEN_SUBLEADING_SHAPE_DIMENSIONS`;
- `NG-FUNNEL-024 — ABSORPTIVE_NONANALYTICITY_ESCAPES_LOCAL_TREE_INTERPOLATION_BUT_NOT_QUANTUM_COMPARATOR_SUBTRACTION`;
- `NG-FUNNEL-026 — PROFILE_UNIVERSAL_IR_LOG_BEFORE_SUBLEADING_SPECTRAL_SHAPE_SEARCH`.

## C5 leading one-massless-loop authority — Iteration 168

At the curvature-squared one-loop order,

`Sigma_TT(s)=C_TT s^2 log_R(-s/mu^2)`

for the full leading massless TT family. With two EH propagators,

`delta chi1R_TT ~ C_TT log_R(-s/mu^2)`.

The odd absorptive shape is therefore constant. The full leading curvature-squared massless one-loop family has rank `1` before profiling and projects below `3.76e-16` after the Iteration-167 constant quotient.

Retain:

- `C5-NG-005 — LEADING_MASSLESS_ONE_LOOP_TT_ABSORPTIVE_SPAN_IS_ONE_DIMENSIONAL_CONSTANT_SHAPE`;
- `ABS-SHAPE-003 — ITERATION167_CONSTANT_QUOTIENT_REMOVES_COMPLETE_LEADING_MASSLESS_ONE_LOOP_CURVATURE_SQUARED_C5_TT_SECTOR`;
- `NG-FUNNEL-028 — HIGHER_LOOP_AND_HIGHER_DERIVATIVE_LOOP_SHAPES_ARE_TRUNCATION_UNCERTAINTY_NOT_ZERO_COLUMNS`.

## C5 next-order absorptive envelope — Iteration 169

Gravity EFT power counting at the next `O(p^6)` order permits:

- tree six-derivative local terms — absorptively zero off pole;
- one loop with one four-derivative insertion;
- two-loop Einstein-Hilbert graphs.

For the frozen one-scale massless two-point problem, a conservative next-order odd-absorptive shape envelope is

`span{s, s log(s/mu^2)}`.

With `x=s/s_max`, profile

`[1, x, x log x]`.

Eight-row certificate:

- rank `3`;
- condition number `18.2955469`;
- residual shape dimension `5`;
- orthogonality error `1.67e-16`.

The target-independent higher-order capacity family `[x^2,x^2 log x,x^2 log^2 x]` retains rank `3/3`.

Retain:

- `C5-NG-006 — NEXT_ORDER_P6_MASSLESS_TT_ABSORPTIVE_ENVELOPE_IS_SPAN_X_XLOGX`;
- `ABS-SHAPE-004 — PROFILING_CONSTANT_X_XLOGX_LEAVES_FIVE_TIMELIKE_SHAPE_DIMENSIONS`;
- `NG-FUNNEL-029 — ORDER_BY_ORDER_LOOP_SHAPE_ENVELOPES_MUST_BE_PROFILED_BEFORE_CANDIDATE_RESIDUAL`.

## General linear-spectral C4 no-go — Iteration 170

For any physical conserved-traceless TT response with positive Källén–Lehmann measure,

`chi_R^TT = Z0 D_R(0) + int dmu2 rho_TT(mu2) D_R(mu2)`, with `rho_TT>=0`,

introduce independent positive-norm massive spin-2 mediator fields with coupling density `sqrt(rho_TT)`.

Their direct-integral retarded response is exactly the same two-point function. With a matching Gaussian state/covariance, the Hadamard/noise kernel and complete Gaussian CTP influence functional are also identical. This generalizes the exact Iteration-141 `KL-002` C4 identity from one frozen spectral density to arbitrary positive TT spectral measures.

Consequences in the current linear TT sector:

- positive poles, continua, thresholds and branch cuts are C4-reproducible;
- arbitrary positive finite-frequency spectral shape is C4-reproducible;
- a vector in the five-dimensional Iteration-169 C5-null remainder is **not** a gravity-specific residual merely because it survives C5 or AS subtraction;
- spectral negativity is not a novelty certificate: it triggers physical-observability, gauge, positivity, ghost and unitarity gates.

Retain:

- `C4-NG-008 — POSITIVE_LINEAR_TT_SPECTRAL_RESPONSE_IS_EXACTLY_REPRESENTABLE_BY_ORDINARY_MEDIATOR_CONTINUUM`;
- `ABS-SHAPE-005 — FINITE_FREQUENCY_LINEAR_SPECTRAL_SHAPE_CANNOT_CERTIFY_GRAVITY_SPECIFIC_NOVELTY_AGAINST_C4`;
- `NG-FUNNEL-030 — LINEAR_SPECTRAL_RESIDUAL_REQUIRES_A_LINKED_NONLINEAR_OR_POST_GAUSSIAN_GRAVITY_RELATION_FOR_PROMOTION`.

## Comparator implications

### C3 postquantum-classical

Supported tree response remains the common GR boundary; symmetric non-Gaussian rank from the same OM action is known. Diffusion/MSR ordered loop corrections remain BLOCKED.

### C4

The fixed dRGT nonlinear comparator remains scoped. More generally, Iteration 170 closes the **positive linear spectral** novelty route against ordinary mediator continua. This does not close nonlinear C4 self-interaction relations.

### C5

Local and leading/NLO massless linear spectral envelopes are calibrated comparator layers, not candidate novelty. Higher-loop shapes may matter for precision characterization but cannot by themselves overcome the C4 two-point identity.

### Nonlocal gravity

Entire tree form factors and their positive spectral two-point realizations cannot provide gravity-specific novelty alone. Nonlinear/source-completed CTP relations remain the meaningful comparator target.

### Asymptotic safety

`AS-LOR-SPEC-002` remains a useful Lorentzian spectral comparator. Reproducing its finite-frequency curve is no longer a prerequisite for deciding whether a **linear** spectral residual can seed Candidate Gravity, because Iteration 170 already defeats that promotion route under positive spectral assumptions. AS multi-point/nonlinear relations remain relevant.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.

Fisher/resources remain FORBIDDEN.

The two-point spectral kernel must now be treated as calibrated/shared data rather than the novelty carrier.

## Iteration authorities

### Iteration 169

- `analysis/c5_nlo_absorptive_shape_envelope_iteration169.py`;
- `results/c5_nlo_absorptive_shape_envelope_iteration169.json`;
- `candidate_gravity/C5_NLO_ABSORPTIVE_SHAPE_ENVELOPE_ITERATION169.md`;
- `research_log/2026-08-31_iteration_169_c5_nlo_absorptive_shape.md`;
- `recovery/RECOVERY_DELTA_ITERATION_169.md`.

### Iteration 170

- `analysis/linear_spectral_c4_no_go_iteration170.py`;
- `results/linear_spectral_c4_no_go_iteration170.json`;
- `candidate_gravity/LINEAR_SPECTRAL_C4_NO_GO_ITERATION170.md`;
- `research_log/2026-08-31_iteration_170_linear_spectral_c4_no_go.md`;
- `recovery/RECOVERY_DELTA_ITERATION_170.md`;
- historical exact authority: `docs/CANDIDATE_GRAVITY_C4_GAUSSIAN_DEGENERACY_ITERATION141.md`.

## Immediate next scientific priority — Iteration 171

Freeze a **linked multi-point residual protocol**. Do not search for Candidate Gravity in a standalone two-point spectral shape.

Required order:

1. inherit a positive/calibrated TT two-point spectral kernel as shared non-novel data;
2. add one finite source-completed `C3sym` coordinate and one ordered `chi2R` coordinate from the same dynamics;
3. formulate relation-level observables that compare higher-point structure **conditioned on the same two-point kernel**, rather than treating each coordinate independently;
4. instantiate fixed C3/C4/C5 comparator relation blocks; preserve unsupported nonlocal/AS higher-point entries as BLOCKED;
5. impose Ward/soft/source-completion relations as hard locks;
6. only a residual in this linked multi-point quotient may earn robust-residual readiness points or motivate `ANSATZ-003`.
