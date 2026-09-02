# RECOVERY DELTA — Candidate Gravity Iteration 270

**Date:** 2026-09-02  
**Authoritative iteration:** 270  
**MODEL_READINESS: 24%**

## Authoritative result

Iteration 270 contains two compatible sub-results, both downstream of the Iteration-269 corrected orbit-density convention.

First, projected `A=K E` was audited in condensed-index/Fourier space. For `K_m[S] E_n[T]`, the contracted field/EOM index carries momentum `q_j=k_T`, so the physical orbit support is

`p_out-p_in = k_S + q_j = k_S+k_T`.

Freeze `PASS_EXACT_PROJECTED_A_CONTRACTED_FIELD_MOMENTUM_ROUTING` with guardrails `NO_DROP_CONTRACTED_EOM_MOMENTUM_IN_K_KERNEL` and `NO_PREMATURE_LOCAL_MATRIX_K_TIMES_E_AS_PHYSICAL_A`.

Second, and more strongly, the exact same-parent parent object `A=R(DR)E` was evaluated directly at finite amplitudes with explicit Fourier endpoints, thereby retaining the full `K0E3+K1E2+K2E1` content without a local-matrix shortcut. The routed physical coefficients satisfy:

- `||A1[s]||_F = 1.00e-9` (consistent with exact null-soft zero);
- `||A1[a]||_F = 0.3538909325`;
- `||A1[b]||_F = 0.4373675400`;
- `||A2[s,a]||_F = 0.7472217396`;
- `||A2[s,b]||_F = 0.7529980727`;
- `||A2[a,b]||_F = 0.6505045916`;
- `||A3[s,a,b]||_F = 2.2278189997`.

`A3` permutation residual is `1.36e-10`; endpoint-reversed transpose residuals are `<=3.92e-7`.

The exact 19-term cubic Leibniz realization reduces to the frozen 15 null-soft survivors; the four `A1[s]` terms contaminate only at `||B19-B15||_F=2.56e-8`. All eight Iteration-266 forward transpose-class representatives are nonzero. Seven partners were checked through endpoint reversal / real `-K`, with worst representative transpose residual `3.29e-7`.

The direct 15-term sum and the 8-class reconstruction agree to `2.78e-16`. Full endpoint-transpose residual is `3.25e-7`.

Physical routed cubic numerator at the frozen generic loop momentum:

`||B3[s,a,b]||_F = 2.2209140981`,

`max|B3[s,a,b]| = 1.3471946832`.

Step scans keep the Frobenius norm stable at `2.2209140...2.2209142`, excluding numerical near-zero.

Freeze:

`PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED`.

Guardrail:

`NONZERO_B3 IS A C5 NUMERATOR CERTIFICATE ONLY; DO NOT PROMOTE TO FINAL COMPARATOR OR CANDIDATE RESIDUAL BEFORE TENSOR_REDUCTION_SOURCE_COMPLETION_AND_HARD_CHANNEL_PROJECTION`.

## Classification and blocker update

This is **not** a Candidate Gravity residual, not an exact comparator identity, not a consistency FAIL, not regime-specific non-identifiability and not near-degeneracy. It is a scoped algebraic nonzero certificate for the physical routed C5 numerator.

The old `BLOCKED_NOT_ZERO` status is superseded for this scoped null-soft `B3` target: the numerator is explicitly nonzero. The remaining umbrella blocker is now

`BLOCKED_4D_EINSTEIN_VD_TENSOR_REDUCTION_SOURCE_PROJECTION_AND_LORENTZIAN_HARD_CHANNEL`.

Scoped tensor/master-integral reduction is now authorized. Blind heavy full-C5 expansion is still forbidden.

No robust residual exists; `ANSATZ-003` remains not created. Fisher/resources remain forbidden.

## Readiness

`MODEL_READINESS: 24%`.

Change from Iteration 269: **0 percentage points** under the frozen rubric. This is a major internal C5 milestone, but comparator foundation remains `24/25` until the nonzero numerator is converted into the actual physical C5 comparator coordinate. Robust unique residual remains `0/20`.

## Authority files

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

Perform a scoped tensor/master-integral reduction of the certified routed `B3[s,a,b]` numerator at the frozen null-soft kinematics. Preserve the raised bubble/triangle topology bounds from Iterations 245/250. Extract the regular/log/nonanalytic hard-channel structures needed for the linked `T_cut` coordinate before source projection. Then complete source/Ward/contact and Lorentzian hard-channel projection. Do not launch Fisher/resources, create `ANSATZ-003`, or broaden into a blind heavy full-C5 run.
