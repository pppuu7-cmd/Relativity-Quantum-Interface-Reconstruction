# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 270**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–267 fixed physical multilinear polarization, null-soft 19-to-15 reduction, project-before-expand `A=K E`, physical `Gamma2`, nonzero Einstein `E2/E3`, exact `K0/K1/K2` 2/4/7 primitive library, the 28-primitive null-soft `A3` target, the exact 15-to-8 `B3` transpose-class reduction, and condensed-index/Fourier endpoint routing. Iteration 268 instantiated exact routed inverse recursion. Iteration 269 corrected the primary orbit-density orientation:

`Y^up = g^-1/sqrt(|g|)`,

`Y_down = sqrt(|g|) g`,

`N_orb = Y_down Nhat`,

restoring second-order routed endpoint transpose for physical `N2/Q2`.

## Iteration 270 — routed projected A and explicit nonzero physical B3

A preliminary routing audit freezes the exact condensed-index requirement for

`A_{gamma delta}=K^j_{gamma delta} E_j`:

for a polarized term `K_m[S] E_n[T]`, the contracted field/EOM index carries `q_j=k_T`, hence

`p_out-p_in = k_S + q_j = k_S+k_T`.

Freeze `PASS_EXACT_PROJECTED_A_CONTRACTED_FIELD_MOMENTUM_ROUTING` with guardrails `NO_DROP_CONTRACTED_EOM_MOMENTUM_IN_K_KERNEL` and `NO_PREMATURE_LOCAL_MATRIX_K_TIMES_E_AS_PHYSICAL_A`.

The stronger same-iteration calculation then evaluates the exact same-parent parent object

`A=R(DR)E`

directly at finite background amplitudes with explicit Fourier bra/input momenta, using the frozen `D=4`, `Lambda=0`, DeWitt `a=-1/2`, affine diffeomorphism generator, field-space Christoffel and Einstein-action covector. This automatically retains the complete `K0E3+K1E2+K2E1` content without a local-matrix shortcut.

Physical routed A-layer values:

- `||A1[s]||_F = 1.00e-9`, consistent with exact null-soft zero;
- `||A1[a]||_F = 0.3538909325`;
- `||A1[b]||_F = 0.4373675400`;
- `||A2[s,a]||_F = 0.7472217396`;
- `||A2[s,b]||_F = 0.7529980727`;
- `||A2[a,b]||_F = 0.6505045916`;
- `||A3[s,a,b]||_F = 2.2278189997`.

`A3` permutation residual is `1.36e-10`; A-layer endpoint-reversed transpose residuals are `<=3.92e-7`.

The explicit physical implementation reproduces the exact 19-term cubic Leibniz structure and null-soft 19-to-15 reduction. The four `A1[s]` terms contribute only `||B19-B15||_F=2.56e-8` numerically. All eight Iteration-266 independent forward representatives are explicitly nonzero. The seven partners are reconstructed/checked through endpoint reversal in the real `-K` sector; worst representative transpose residual is `3.29e-7`.

The direct 15-term sum and eight-class reconstruction agree to

`2.78e-16`.

Full endpoint-transpose residual is

`3.25e-7`.

At the frozen generic loop momentum, the physical routed cubic numerator is

`||B3[s,a,b]||_F = 2.2209140981`,

`max|B3[s,a,b]| = 1.3471946832`.

Step scans keep `||B3||_F` in the range `2.22091404...2.22091422`, excluding numerical near-zero.

Freeze:

`PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED`.

Guardrail:

`NONZERO_B3 IS A C5 NUMERATOR CERTIFICATE ONLY; DO NOT PROMOTE TO FINAL COMPARATOR OR CANDIDATE RESIDUAL BEFORE TENSOR_REDUCTION_SOURCE_COMPLETION_AND_HARD_CHANNEL_PROJECTION`.

## Blocker update

For this scoped null-soft physical `B3` target, the old `BLOCKED_NOT_ZERO` state is superseded: algebraic nonzero existence is now certified. The remaining C5 umbrella blocker is

`BLOCKED_4D_EINSTEIN_VD_TENSOR_REDUCTION_SOURCE_PROJECTION_AND_LORENTZIAN_HARD_CHANNEL`.

A scoped tensor/master-integral reduction of the already-certified numerator is now authorized. Blind heavy full-C5 expansion is not authorized.

This result is **not** a consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, novelty certificate, final C5 comparator coordinate or Candidate Gravity residual.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 269: **0 percentage points**. Explicit nonzero physical `B3` is a major C5 milestone and removes the algebraic-zero blocker, but comparator foundation remains `24/25` until tensor/master-integral reduction, hard-channel extraction, source/Ward/contact completion and Lorentzian projection produce the actual physical C5 comparator coordinate. Robust unique residual remains `0/20`.

## Retained program guardrails

- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction; the present nonzero C5 numerator alone is insufficient.
- `e+c<=3` remains the frozen finite-`R^3` truncation rule.
- Iteration 269 density correction supersedes only the old second-order density/N2/Q2 numerical representative, not earlier topology/polarization/K/E results.
- Endpoint transpose always means the full condensed-index kernel endpoint reversal / real `-K` sector, never a raw same-routing matrix transpose.

## Retained comparator state

### C3
`BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` — not zero and not consistency FAIL.

### C4
Standalone positive two-point spectral/cut information remains mediator-degenerate.

### C5
`BLOCKED_4D_EINSTEIN_VD_TENSOR_REDUCTION_SOURCE_PROJECTION_AND_LORENTZIAN_HARD_CHANNEL`.

The scoped physical numerator is explicitly nonzero; remaining blockage is reduction/projection/comparator-coordinate construction.

### Other routes
Asymptotic-safety, nonlocal and proxy routes retain their frozen blockers; no proxy replaces the frozen comparator identity.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full C5 run: NOT AUTHORIZED.  
Scoped tensor reduction of certified B3: AUTHORIZED.

## Iteration 270 authority files

- `candidate_gravity/C5_VD_PROJECTED_A_FIELD_MOMENTUM_ROUTING_ITERATION270.md`
- `candidate_gravity/code/iteration270_vd_projected_a_field_momentum_routing.py`
- `candidate_gravity/results/iteration270_vd_projected_a_field_momentum_routing.json`
- `candidate_gravity/C5_VD_PHYSICAL_B3_NONZERO_ITERATION270.md`
- `candidate_gravity/code/iteration270_vd_physical_b3_nonzero.py`
- `candidate_gravity/results/iteration270_vd_physical_b3_nonzero.json`
- `research_log/2026-09-02_iteration_270_vd_projected_a_field_momentum_routing.md`
- `research_log/2026-09-02_iteration_270_vd_physical_b3_nonzero.md`
- `recovery/RECOVERY_DELTA_ITERATION_270.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION270.md`

## Exact next gate — Iteration 271

Perform a scoped tensor/master-integral reduction of the certified routed `B3[s,a,b]` numerator at the frozen null-soft kinematics. Preserve the raised bubble/triangle topology bounds from Iterations 245/250. Extract the regular/log/nonanalytic hard-channel structures needed for the linked `T_cut` coordinate before source projection. Then perform source/Ward/contact completion and Lorentzian hard-channel discontinuity projection. Do not launch Fisher/resources, create `ANSATZ-003`, or broaden into a blind heavy full-C5 run.
