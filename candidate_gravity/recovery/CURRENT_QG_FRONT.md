# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 167**

## Scientific state in one sentence

The 12-row spacelike ordered-TT sector remains saturated by an authorized local C5 dimension-12 basis, but the new timelike **linear** absorptive sector escapes local-tree interpolation; Iteration 167 now supplies a conserved-TT source map and a target-independent seven-dimensional shape quotient that removes the universal leading C5/AS constant-log onset to machine precision, leaving only sub-leading frequency shape as a possible next discriminator.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged in Iteration 167. The source/shape map is now cleaner, but no comparator-subtracted sub-leading residual exists yet.

## Mandatory provenance corrections / nomenclature

1. Iteration 163 used correct dRGT tangent arrays but mislabeled them. Correct mapping:
   - first target: `d/d log(m^2)`;
   - second target: `d/d alpha3`;
   - `alpha4`: cubic-TT blind because `L4[K]` starts quartic.

2. The Iteration-166/167 `A_odd` observable is the frequency-odd imaginary part of **linear** `chi1R`, not the post-Gaussian second-order coordinate `chi2R_odd`.

Retain:

`PROVENANCE-CORR-001 — ITERATION163 TARGET LABELS ARE DLOGM2 AND DALPHA3; ALPHA4 REMAINS CUBIC_TT BLIND`.

## Frozen RQIR observable hierarchy

Conceptual coordinates remain

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

The new timelike spectral block refines `chi1R`; it does not replace the post-Gaussian coordinates.

Hard constraints precede profiling/Fisher. Unsupported comparator coordinates are BLOCKED, never zero-filled.

## Historical spacelike ordered-TT result through Iteration 165

The authoritative spacelike ordered-response protocol contains 12 frozen TT rows. Iteration 165 completed a target-independent local C5 cubic subset through the already frozen dimension-12 cutoff.

Result:

`C5 matrix = 12x12`, `rank=12/12`.

Both corrected dRGT tangents are absorbed to machine precision on that finite protocol.

Retain:

`C5-NG-003 — DIMENSION12_LOCAL_C5_CUBIC_SUBSET_SATURATES_ENRICHED_12ROW_TT_PROTOCOL`.

`C4-NG-007 — ITERATION164_DRGT_RESIDUAL_ABSORBED_BY_TARGET_INDEPENDENT_DIMENSION12_C5_COMPLETION`.

`NG-FUNNEL-022 — FINITE_PROTOCOL_RESIDUAL_MUST_SURVIVE_THEORY_AUTHORIZED_COMPARATOR_BASIS_COMPLETION`.

`NG-FUNNEL-023 — ONCE_ONE_AUTHORIZED_COMPARATOR_SPANS_THE_FINITE_ROW_SPACE, ADDITIONAL_BLOCKED_COMPARATORS_CANNOT_RESTORE_A_RESIDUAL IN THAT SAME SPACE`.

Do not search for novelty by adding target-optimized spacelike rows inside this saturated sector.

## Timelike absorptive block — Iteration 166

Freeze eight timelike invariants

`s_i=0.004*i`, `i=1..8`,

with zero spatial momentum, paired positive/negative frequencies and all `s_i<0.04`, below the frozen dRGT TT pole.

Define

`A_odd(s)=[Im chi1R(+omega)-Im chi1R(-omega)]/(2*pi)`.

For a real local Hermitian tree EFT evaluated away from isolated poles,

`A_odd^local-tree=0`.

A leading massless-loop logarithm produces a constant normalized absorptive shape.

Retain:

`C5-NG-004 — LOCAL_HERMITIAN_TREE_EFT_CANNOT_SATURATE_OFF_POLE_ABSORPTIVE_BLOCK`.

`NG-FUNNEL-024 — ABSORPTIVE_NONANALYTICITY_ESCAPES_LOCAL_TREE_INTERPOLATION_BUT_NOT_QUANTUM_COMPARATOR_SUBTRACTION`.

## Conserved-TT source map — Iteration 167

Use

`k=(omega,0,0,0)`

and external source/detector tensor

`T_0mu=0`,

`T_ij=diag(1,-1,0)/sqrt(2)`.

Across all eight rows:

- conservation error `0`;
- trace error `0`;
- spin-2 projector error `0`;
- `T:P2:T=1` within `2.22e-16`.

Thus the scoped linear source-to-source TT response preserves the propagator spectral shape up to a frequency-independent common gain.

Retain:

`ABS-SHAPE-001 — CONSERVED_TT_SOURCE_MAP_PRESERVES_TIMELIKE_SPECTRAL_SHAPE`.

This does not close nonlinear detector/source completion.

## Constant-log-null quotient — Iteration 167

Let `x=s/s_max=i/8`. QR factorization of

`[1,x,x^2,...,x^7]`

defines the constant direction plus a seven-dimensional orthonormal complement `Q_shape`.

Certificate:

- shape dimension `7`;
- `max |Q_shape^T 1| = 2.22e-16`;
- orthonormality error `4.44e-16`;
- projected leading-C5-log norm `3.80e-16`;
- projected leading-AS-IR-log norm `1.44e-16`.

A target-independent capacity family `(x,x^2,x^3)` retains rank `3/3` in this quotient.

Retain:

`ABS-SHAPE-002 — CONSTANT_LOG_NULL_QUOTIENT_LEAVES_SEVEN_SUBLEADING_SHAPE_DIMENSIONS`.

`NG-FUNNEL-026 — PROFILE_UNIVERSAL_IR_LOG_BEFORE_SUBLEADING_SPECTRAL_SHAPE_SEARCH`.

A fourth finite-difference null of cubic envelopes is available as a diagnostic but is not primary because its white-noise amplification is `sqrt(70) ~= 8.37`.

## Lorentzian asymptotic-safety comparator

`candidate_gravity/comparators/AS-LOR-SPEC-002.md` is separate from the Euclidean `AS-FRG-TT-001` comparator.

Primary self-consistent source is now published as:

Pawlowski, Reichert, Wessely, *Self-consistent graviton spectral function in Lorentzian quantum gravity*, **Physics Letters B 880 (2026) 140844**, DOI `10.1016/j.physletb.2026.140844`, arXiv:2507.22169.

Published properties include a massless pole, positive continuum, IR constant onset, finite-frequency decrease and UV `1/[lambda^2 log^3(lambda^2)]` decay.

Controlled IR:

`G_hh^ph=z_spec^-1[1/p^2-A_h log(p^2)+...]`,

`A_h=61/(60*pi)`, `z_spec~=1.486`.

The leading AS IR constant is exactly removed by the Iteration-167 quotient. However the finite-frequency AS continuum is not constant and therefore may populate the seven-dimensional shape space.

The repository has no precision numerical AS spectral dataset and has not reproduced the spectral flow. Therefore:

`AS finite-frequency shape = BLOCKED_NUMERICAL_SPECTRAL_DATA_OR_CONTROLLED_REPRODUCTION_REQUIRED`.

Retain:

`AS-NG-004 — LORENTZIAN_AS_LEADING_IR_LOG_IS_COLLINEAR_WITH_C5_MASSLESS_LOOP_SHAPE`.

`NG-FUNNEL-025 — BARE_TT_SPECTRAL_COEFFICIENT_IS_NOT_YET_A_SOURCE_COMPLETED_RQIR_OBSERVABLE`.

`NG-FUNNEL-027 — PUBLISHED_SPECTRAL_CURVE_IS_NOT_A_NUMERICAL_COMPARATOR_COLUMN_WITHOUT_DATA_OR_CONTROLLED_REPRODUCTION`.

## Current comparator status in the absorptive shape space

### C3 postquantum-classical

Supported tree response: absorptively zero away from its isolated massless pole.

BLOCKED: diffusion/MSR ordered loop corrections, thresholds, non-TT completion.

### C4 dRGT

Frozen tree TT pole at `m^2=0.04`; all Iteration-167 rows lie below it and have no supported tree continuum.

BLOCKED: loops/matter thresholds, helicity-0/1, Vainshtein/nonperturbative sector, C4 `N2/C3sym`.

### C5

- local Hermitian tree: exact off-pole absorptive zero;
- leading massless one-loop logarithmic shape: constant and profiled;
- complete one-loop massless source-response family: Iteration-168 target;
- higher-loop / higher-derivative-insertion absorptive shapes: BLOCKED until power-counting/truncation convention is frozen;
- `N2/C3sym` from the same CTP dynamics: BLOCKED.

### Entire-form-factor nonlocal comparator

Frozen entire tree form factors have no new branch cut away from the GR pole.

BLOCKED: full Lorentzian CTP/loops and nonlinear source-completed response.

### Asymptotic safety

Leading IR Lorentzian shape profiled; finite-frequency spectral shape BLOCKED pending data/reproduction.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.

Fisher/resources remain FORBIDDEN.

## Iteration-167 authorities

- `analysis/absorptive_shape_quotient_iteration167.py`;
- `results/absorptive_shape_quotient_iteration167.json`;
- `candidate_gravity/ABSORPTIVE_SHAPE_QUOTIENT_ITERATION167.md`;
- updated `candidate_gravity/comparators/AS-LOR-SPEC-002.md`;
- `recovery/RECOVERY_DELTA_ITERATION_167.md`;
- `research_log/2026-08-31_iteration_167_absorptive_shape_quotient.md`.

## Immediate next scientific priority — Iteration 168

Freeze the perturbative C5 loop/power-counting order in the same conserved-TT linear absorptive channel.

Required order:

1. derive the complete leading one-loop massless nonlocal quadratic-curvature structure in the flat conserved-TT channel;
2. determine whether every allowed massless one-loop two-point absorptive contribution is constant and therefore exactly annihilated by `Q_shape`;
3. identify higher-loop and higher-derivative-insertion contributions as explicit next-order comparator shapes or truncation uncertainty, rather than silently zeroing them;
4. do not use a visually digitized AS plot as a precision tangent;
5. only after this C5 power-counting gate is closed should a sub-leading Candidate Gravity residual be sought.
