# RECOVERY DELTA — Candidate Gravity Iteration 270

**Date:** 2026-09-02  
**Authoritative iteration:** 270  
**MODEL_READINESS: 24%**

## New exact routing gate

Starting from the Iteration-269 corrected physical orbit density and routed `Q1/Q2`, audit the projected same-parent identity

`A_{gamma delta}=K^j_{gamma delta} E_j`

in condensed-index/Fourier space.

For a polarized term `K_m[S] E_n[T]`, the contracted field-space index `j` carries momentum `q_j`. With the frozen Iteration-267 convention,

`p_out-p_in = k_S + q_j`,

and contraction with the EOM coefficient fixes

`q_j = k_T`.

Thus

`p_out-p_in = k_S+k_T`.

The contracted EOM momentum cannot be discarded before forming `A`. A finite matrix `K_m(p)` labelled only by orbit momentum and its explicit background subset is not a complete physical Fourier kernel for this contraction.

Freeze:

`PASS_EXACT_PROJECTED_A_CONTRACTED_FIELD_MOMENTUM_ROUTING`.

Guardrails:

`NO_DROP_CONTRACTED_EOM_MOMENTUM_IN_K_KERNEL`.

`NO_PREMATURE_LOCAL_MATRIX_K_TIMES_E_AS_PHYSICAL_A`.

## Reproducible checks

The routing enumerator preserves all earlier frozen projected/null-soft counts:

- `A1[s]`: 0 survivors;
- `A2[s,a]`: 2;
- `A2[s,b]`: 2;
- `A2[a,b]`: 3;
- `A3[s,a,b]`: 6.

The eight Iteration-266 forward `B3` representatives all have total support `k_s+k_a+k_b`, but their `A` factors must now be instantiated with an explicit contracted-field momentum route before numerical multiplication with the corrected Iteration-269 resolvents.

## Classification

This closes an implementation/provenance ambiguity. It is not a consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, novelty certificate or Candidate Gravity residual.

Retain `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION` and `BLOCKED_NOT_ZERO`.

No robust residual; `ANSATZ-003` not created; Fisher/resources and blind heavy integration forbidden.

## Readiness

`MODEL_READINESS: 24%`.

Change from Iteration 269: **0 percentage points**. The routed projected-`A` implementation contract is now exact, but comparator foundation remains `24/25`; explicit routed numerical `K/A/B3`, tensor reduction and source projection remain open, so no rubric category closes.

## Files

- `candidate_gravity/C5_VD_PROJECTED_A_FIELD_MOMENTUM_ROUTING_ITERATION270.md`
- `candidate_gravity/code/iteration270_vd_projected_a_field_momentum_routing.py`
- `candidate_gravity/results/iteration270_vd_projected_a_field_momentum_routing.json`
- `research_log/2026-09-02_iteration_270_vd_projected_a_field_momentum_routing.md`
- `recovery/RECOVERY_DELTA_ITERATION_270.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION270.md`

## Exact next gate — Iteration 271

Implement the physical routed kernel `K_m[S](p_out,p_in;q_j)` or an exactly equivalent representation from frozen affine `R`, `Gamma0/Gamma1/Gamma2` and the 2/4/7 primitive library. Contract it with certified `E1/E2/E3` to obtain numerical routed `A1/A2/A3`. Then evaluate the eight forward `+K` `B3[s,a,b]` representatives using corrected Iteration-269 `Q2`, reconstruct the seven endpoint-reversed partners in the real `-K` sector, and require every transpose regression to pass before freezing a nonzero physical `B3`. Tensor reduction remains forbidden until that certificate exists.
