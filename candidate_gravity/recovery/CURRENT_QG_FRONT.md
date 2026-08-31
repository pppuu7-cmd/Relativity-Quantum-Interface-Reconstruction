# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld  
**Authoritative Candidate Gravity front:** **Iteration 166**

## Scientific state in one sentence

The local-C5 finite-interpolation saturation found through Iteration 165 can be escaped by changing observable type: an off-pole timelike **odd absorptive** retarded response is exactly blind to any real local Hermitian tree derivative tower, but its first nonzero massless-log direction is already occupied by standard perturbative C5 and by the leading IR Lorentzian asymptotic-safety continuum, so the next viable target is sub-leading source-completed frequency dependence after that universal log direction is removed.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- parent dynamics/ANSATZ `0/20`;
- candidate consistency `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

`MODEL_READINESS = 24%` remains unchanged in Iteration 166. The new causal sector materially narrows comparator structure but the final comparator-foundation point is not awarded while the common source-completed absorptive quotient is incomplete.

## Mandatory provenance correction retained

Iteration 163 used correct dRGT tangent arrays but mislabeled them. Correct Iteration-156 mapping:

- first target: `d/d log(m^2)`;
- second target: `d/d alpha3`;
- `alpha4`: cubic-TT blind because `L4[K]` starts quartic.

Retain:

`PROVENANCE-CORR-001 — ITERATION163 TARGET LABELS ARE DLOGM2 AND DALPHA3; ALPHA4 REMAINS CUBIC_TT BLIND`.

## Frozen RQIR observable hierarchy

Reduced conceptual coordinates remain

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Hard constraints precede profiling/Fisher. Unsupported comparator coordinates are BLOCKED, never zero-filled.

## Historical spacelike ordered-TT result through Iteration 165

The authoritative real ordered-response protocol contains 12 frozen spacelike TT rows.

Iteration 165 completed a target-independent local C5 cubic subset through the already frozen dimension-12 cutoff:

- EH;
- Ricci^3;
- cyclic Riemann^3;
- full `Ricci^2` response tangent including propagator insertion;
- full `Ricci Box Ricci` tangent;
- mixed `Ricci Ricci Riemann` cubic invariant;
- `Box^n`, `n=1,2,3`, descendants of Ricci and Riemann cubic chains.

Result:

`C5 matrix = 12x12`, `rank=12/12`.

Both corrected dRGT tangents are absorbed to machine precision on that finite protocol.

Retain:

`C5-NG-003 — DIMENSION12_LOCAL_C5_CUBIC_SUBSET_SATURATES_ENRICHED_12ROW_TT_PROTOCOL`.

`C4-NG-007 — ITERATION164_DRGT_RESIDUAL_ABSORBED_BY_TARGET_INDEPENDENT_DIMENSION12_C5_COMPLETION`.

`NG-FUNNEL-022 — FINITE_PROTOCOL_RESIDUAL_MUST_SURVIVE_THEORY_AUTHORIZED_COMPARATOR_BASIS_COMPLETION`.

`NG-FUNNEL-023 — ONCE_ONE_AUTHORIZED_COMPARATOR_SPANS_THE_FINITE_ROW_SPACE, ADDITIONAL_BLOCKED_COMPARATORS_CANNOT_RESTORE_A_RESIDUAL IN THAT SAME SPACE`.

Do not search for novelty by adding more target-optimized rows inside this saturated sector.

## New Iteration-166 timelike absorptive pre-protocol

Freeze eight positive timelike invariants

`s_i = 0.004*i`, `i=1..8`,

with zero spatial momentum, paired positive/negative frequencies and all `s_i<0.04`, below the frozen dRGT TT pole.

Define

`A_odd(s)=[Im chi_R(+omega)-Im chi_R(-omega)]/(2*pi)`.

Use the retarded logarithmic branches

`log(-s-i0)=log(s)-i*pi`,

`log(-s+i0)=log(s)+i*pi`.

### Exact/scoped local-tree result

For a real local Hermitian tree EFT evaluated away from isolated poles,

`A_odd^local-tree=0`.

This is analytic/causal and does not depend on the number of local Wilson coefficients. Therefore the local finite-polynomial interpolation mechanism responsible for Iteration-165 saturation cannot saturate this absorptive block.

Retain:

`C5-NG-004 — LOCAL_HERMITIAN_TREE_EFT_CANNOT_SATURATE_OFF_POLE_ABSORPTIVE_BLOCK`.

### C5 massless-loop positive control

A leading nonanalytic inverse-kernel term

`K_R=s[1+ell*s log(-s-i0)]`

gives at first order

`d chi_R/d ell = -log(-s-i0)`

and normalized

`A_odd=1`.

Eight-row rank: `1`.

A generic shape-capacity stress family `x^n A_odd`, `n=0..3`, has rank `4/4`; it is not interpreted as four independently fixed C5 loop parameters.

## New Lorentzian asymptotic-safety comparator

Separate comparator record:

`candidate_gravity/comparators/AS-LOR-SPEC-002.md`.

Primary authority: Pawlowski, Reichert & Wessely, arXiv:2507.22169 (2025), supported by Fehre et al. arXiv:2111.13232.

Published TT spectral structure uses a Källén–Lehmann representation with a massless pole plus positive scattering continuum. In the controlled IR,

`G_hh^ph = z_spec^-1 [1/p^2 - A_h log(p^2) + ...]`,

`A_h = 61/(60*pi) = 0.32361505095352056`,

`z_spec ~= 1.486`.

The unnormalised IR continuum onset is `61/30 ~= 2.0333333333`.

After gain profiling, the leading AS IR absorptive vector is exactly collinear with the leading C5 massless-log shape on the Iteration-166 benchmark:

`rank([C5_log,AS_IR])=1`,

relative AS residual after C5-log projection `=1.715e-16`.

Retain:

`AS-NG-004 — LORENTZIAN_AS_LEADING_IR_LOG_IS_COLLINEAR_WITH_C5_MASSLESS_LOOP_SHAPE`.

This is a leading-IR shape statement, not a finite-frequency AS=C5 identity.

## New funnel guardrails

`NG-FUNNEL-024 — ABSORPTIVE_NONANALYTICITY_ESCAPES_LOCAL_TREE_INTERPOLATION_BUT_NOT_QUANTUM_COMPARATOR_SUBTRACTION`.

`NG-FUNNEL-025 — BARE_TT_SPECTRAL_COEFFICIENT_IS_NOT_YET_A_SOURCE_COMPLETED_RQIR_OBSERVABLE`.

The second guardrail is mandatory because the AS coefficient above is tied to a TT fluctuation-field/gauge/normalisation convention. RQIR must eventually construct a conserved-source/detector transfer including all source and vertex pieces required for a physical operational observable.

## Comparator status in the new absorptive block

### C3 postquantum-classical

Supported tree causal response is the common EH boundary and is absorptively zero away from its isolated massless pole.

BLOCKED: diffusion/MSR-loop ordered corrections, full threshold/absorptive response, non-TT completion.

### C4 dRGT

Frozen `m^2=0.04`, `alpha3=alpha4=0` reference retained. On the chosen `s<0.04` rows the supported tree TT propagator does not hit its isolated massive pole and has no continuum absorptive piece.

BLOCKED: loops/matter thresholds, helicity-0/1 completion, Vainshtein/nonperturbative sector, C4 `N2/C3sym`.

Do not infer those blocked sectors are zero.

### C5

- local tree: exact off-pole absorptive zero;
- leading massless-loop log shape: supported;
- exact source-completed finite-frequency coefficient in the RQIR convention: BLOCKED;
- full `N2/C3sym` from the same CTP map: BLOCKED.

### Entire-form-factor nonlocal comparators

The frozen entire tree form factors do not themselves generate a branch cut away from the GR pole.

BLOCKED: full Lorentzian CTP/loop absorptive completion and nonlinear source-completed response.

### Asymptotic safety

`AS-FRG-TT-001` remains the Euclidean action/vertex comparator with nonlinear real-time mapping blocked.

`AS-LOR-SPEC-002` supplies a genuinely Lorentzian two-point spectral positive control: continuum and leading IR log supported; source-completed finite-frequency RQIR amplitude and nonlinear ordered response remain blocked.

## Candidate state

There is still **no robust Candidate Gravity residual**.

`ANSATZ-003`: NOT CREATED.

Fisher/resources remain FORBIDDEN.

A nonzero absorptive signal alone may not motivate the candidate because it is already standard C5/AS physics.

## Iteration-166 authorities

- `analysis/timelike_absorptive_protocol_iteration166.py`;
- `results/timelike_absorptive_protocol_iteration166.json`;
- `candidate_gravity/TIMELIKE_ABSORPTIVE_PROTOCOL_ITERATION166.md`;
- `candidate_gravity/comparators/AS-LOR-SPEC-002.md`;
- `recovery/RECOVERY_DELTA_ITERATION_166.md`;
- `research_log/2026-08-31_iteration_166_timelike_absorptive.md`.

## Immediate next scientific priority — Iteration 167

Do not build a candidate around the universal constant-log absorptive onset.

Required order:

1. construct a conserved-source/source-completed timelike response rather than using a bare TT propagator coefficient;
2. derive the leading perturbative-C5 massless-loop nonanalytic direction in that exact physical source convention, with source/vertex completion sufficient for gauge invariance;
3. map `AS-LOR-SPEC-002` into the same normalized source-response language in the controlled IR;
4. remove/profile the universal constant-log direction;
5. identify the first target-independent **sub-leading frequency-shape coordinate** and test it against C5 + Lorentzian AS before any candidate evaluation;
6. keep C3/C4/nonlocal unsupported loop sectors BLOCKED unless a theorem-level threshold argument makes them irrelevant in the frozen window;
7. only a residual surviving that stronger causal/nonanalytic quotient may earn robust-residual readiness points or reopen `ANSATZ-003`.
