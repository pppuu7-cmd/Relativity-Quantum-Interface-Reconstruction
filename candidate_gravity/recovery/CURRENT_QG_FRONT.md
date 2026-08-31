# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 168**

## Scientific state in one sentence

The 12-row spacelike ordered-TT sector remains saturated by an authorized local C5 dimension-12 basis; the eight-row timelike conserved-TT linear absorptive sector escapes local-tree interpolation, and Iteration 168 proves that the **complete leading one-massless-loop curvature-squared C5 two-point sector** is only a one-dimensional constant absorptive shape that is already annihilated by the Iteration-167 quotient, while next-order C5 nonanalytic shapes, massive thresholds, and finite-frequency Lorentzian asymptotic-safety remain blockers.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged in Iteration 168. The leading C5 loop ambiguity is narrowed, but no comparator-subtracted residual exists.

## Mandatory provenance corrections

1. Iteration 163 dRGT target mapping:
   - first target: `d/d log(m^2)`;
   - second target: `d/d alpha3`;
   - `alpha4`: cubic-TT blind because `L4[K]` starts quartic.

2. Iteration-166 onward `A_odd` is the frequency-odd imaginary part of **linear** `chi1R`, not post-Gaussian `chi2R_odd`.

Retain `PROVENANCE-CORR-001`.

## Frozen observable hierarchy

Conceptual coordinates remain

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Hard constraints precede profiling/Fisher. Unsupported comparator coordinates are BLOCKED, never zero-filled.

## Spacelike ordered-TT authority through Iteration 165

The 12-row spacelike protocol with target-independent local C5 completion through the frozen dimension-12 cutoff has

`C5 matrix = 12x12`, `rank=12/12`.

Corrected dRGT tangents are absorbed to machine precision on that finite protocol.

Retain:

`C5-NG-003 — DIMENSION12_LOCAL_C5_CUBIC_SUBSET_SATURATES_ENRICHED_12ROW_TT_PROTOCOL`.

`C4-NG-007 — ITERATION164_DRGT_RESIDUAL_ABSORBED_BY_TARGET_INDEPENDENT_DIMENSION12_C5_COMPLETION`.

`NG-FUNNEL-022 — FINITE_PROTOCOL_RESIDUAL_MUST_SURVIVE_THEORY_AUTHORIZED_COMPARATOR_BASIS_COMPLETION`.

`NG-FUNNEL-023 — ONCE_ONE_AUTHORIZED_COMPARATOR_SPANS_THE_FINITE_ROW_SPACE, ADDITIONAL_BLOCKED_COMPARATORS_CANNOT_RESTORE_A_RESIDUAL_IN_THAT_SAME_SPACE`.

Do not search for novelty by adding target-optimized spacelike rows inside this saturated sector.

## Timelike absorptive protocol — Iterations 166-167

Freeze eight timelike invariants

`s_i=0.004*i`, `i=1..8`,

with `k=(omega,0,0,0)` and all `s_i<0.04`, below the frozen dRGT TT pole.

Use conserved traceless source/detector

`T_0mu=0`, `T_ij=diag(1,-1,0)/sqrt(2)`.

Define

`A_odd(s)=[Im chi1R(+omega)-Im chi1R(-omega)]/(2*pi)`.

Source-map certificate: conservation, trace and projector errors are zero to numerical precision; `T:P2:T=1` within `2.22e-16`.

A target-independent QR quotient profiles the constant vector from the eight-row space, leaving seven shape dimensions. The leading C5 massless log and leading AS IR log project to norms below `4e-16`.

Retain:

`C5-NG-004 — LOCAL_HERMITIAN_TREE_EFT_CANNOT_SATURATE_OFF_POLE_ABSORPTIVE_BLOCK`.

`ABS-SHAPE-001 — CONSERVED_TT_SOURCE_MAP_PRESERVES_TIMELIKE_SPECTRAL_SHAPE`.

`ABS-SHAPE-002 — CONSTANT_LOG_NULL_QUOTIENT_LEAVES_SEVEN_SUBLEADING_SHAPE_DIMENSIONS`.

`NG-FUNNEL-024 — ABSORPTIVE_NONANALYTICITY_ESCAPES_LOCAL_TREE_INTERPOLATION_BUT_NOT_QUANTUM_COMPARATOR_SUBTRACTION`.

`NG-FUNNEL-026 — PROFILE_UNIVERSAL_IR_LOG_BEFORE_SUBLEADING_SPECTRAL_SHAPE_SEARCH`.

## C5 leading massless one-loop authority — Iteration 168

Freeze the C5 quantum order in this channel to:

- Einstein-Hilbert tree response;
- renormalized local curvature-squared counterterms;
- leading one-massless-loop curvature-squared nonlocal form factors;
- retarded logarithmic branch `log_R(-Box/mu^2)` with arbitrary positive `mu`.

The covariant nonlocal family is

`R log R`, `Ricci log Ricci`, `Riemann log Riemann` (equivalently other curvature-squared bases).

For the frozen TT rows, reproducible linearized-curvature contractions give

- `R^(1)=0`;
- `Ricci^(1):Ricci^(1)=s^2/4`;
- `Riemann^(1):Riemann^(1)=s^2`;
- `Weyl^(1):Weyl^(1)=s^2/2`.

Therefore every nonzero leading massless curvature-squared one-loop TT self-energy has

`Sigma_TT(s) = C_TT s^2 log_R(-s/mu^2)`.

With two EH propagators,

`delta chi1R_TT ~ C_TT log_R(-s/mu^2)`.

Thus the frequency-odd absorptive shape is constant. The normalized curvature-log shape family has pre-profile rank `1`; after the Iteration-167 constant quotient its maximum projected norm is `3.76e-16`.

Retain:

`C5-NG-005 — LEADING_MASSLESS_ONE_LOOP_TT_ABSORPTIVE_SPAN_IS_ONE_DIMENSIONAL_CONSTANT_SHAPE`.

`ABS-SHAPE-003 — ITERATION167_CONSTANT_QUOTIENT_REMOVES_COMPLETE_LEADING_MASSLESS_ONE_LOOP_CURVATURE_SQUARED_C5_TT_SECTOR`.

Critical nonclaim: this is **not** the full quantum C5 response.

Explicitly BLOCKED, not zero:

- two-loop massless self-energy shapes;
- one-loop shapes with higher-derivative EFT insertions;
- massive thresholds;
- nonlinear/post-Gaussian source response.

Retain:

`NG-FUNNEL-028 — HIGHER_LOOP_AND_HIGHER_DERIVATIVE_LOOP_SHAPES_ARE_TRUNCATION_UNCERTAINTY_NOT_ZERO_COLUMNS`.

## Comparator status in seven-dimensional absorptive shape space

### C3 postquantum-classical

Supported tree response is absorptively zero away from its isolated massless pole.

BLOCKED: diffusion/MSR ordered loop corrections, thresholds, non-TT completion.

### C4 dRGT

Frozen tree TT pole at `m^2=0.04`; all timelike rows lie below it and have no supported tree continuum.

BLOCKED: loops/matter thresholds, helicity-0/1, Vainshtein/nonperturbative sector, C4 `N2/C3sym`.

### C5

- local Hermitian tree: exact off-pole absorptive zero;
- complete leading one-massless-loop curvature-squared TT sector: constant shape, profiled exactly to machine precision;
- two-loop / higher-derivative loop insertions: BLOCKED next-order truncation shapes;
- massive thresholds: BLOCKED separate threshold comparator;
- `N2/C3sym` from same CTP dynamics: BLOCKED.

### Entire-form-factor nonlocal comparator

Frozen entire tree form factors introduce no new branch cut away from the GR pole.

BLOCKED: Lorentzian CTP loops and nonlinear source-completed response.

### Lorentzian asymptotic safety

Comparator `candidate_gravity/comparators/AS-LOR-SPEC-002.md` uses Pawlowski, Reichert, Wessely, *Physics Letters B* 880 (2026) 140844, DOI `10.1016/j.physletb.2026.140844`, arXiv:2507.22169.

Leading IR constant onset is profiled. Published finite-frequency continuum is nonconstant, but the repository has no precision numerical spectral dataset and has not reproduced the spectral flow.

Status:

`AS finite-frequency shape = BLOCKED_NUMERICAL_SPECTRAL_DATA_OR_CONTROLLED_REPRODUCTION_REQUIRED`.

Retain:

`AS-NG-004 — LORENTZIAN_AS_LEADING_IR_LOG_IS_COLLINEAR_WITH_C5_MASSLESS_LOOP_SHAPE`.

`NG-FUNNEL-027 — PUBLISHED_SPECTRAL_CURVE_IS_NOT_A_NUMERICAL_COMPARATOR_COLUMN_WITHOUT_DATA_OR_CONTROLLED_REPRODUCTION`.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.

Fisher/resources remain FORBIDDEN.

## Iteration-168 authorities

- `analysis/c5_massless_one_loop_shape_iteration168.py`;
- `results/c5_massless_one_loop_shape_iteration168.json`;
- `candidate_gravity/C5_MASSLESS_ONE_LOOP_SHAPE_ITERATION168.md`;
- `research_log/2026-08-31_iteration_168_c5_massless_one_loop_shape.md`;
- `recovery/RECOVERY_DELTA_ITERATION_168.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION168.md`.

## Immediate next scientific priority — Iteration 169

Freeze a **target-independent next-order C5 truncation envelope** in the same seven-dimensional absorptive shape quotient before testing any candidate.

Required order:

1. derive the low-energy nonanalytic scaling allowed by two-loop pure-EH TT self-energy;
2. derive the scaling introduced by one-loop graphs with already-authorized higher-derivative EFT insertions, without inventing Wilson coefficients;
3. convert those allowed `s^n log(-s)` structures into finite shape columns on the eight frozen rows and compute their rank after the constant quotient;
4. keep massive thresholds as a separate BLOCKED comparator unless a concrete mass spectrum/protocol is frozen;
5. only if shape dimensions remain after this controlled C5 truncation envelope should finite-frequency Lorentzian AS or a Candidate Gravity residual be tested there.
