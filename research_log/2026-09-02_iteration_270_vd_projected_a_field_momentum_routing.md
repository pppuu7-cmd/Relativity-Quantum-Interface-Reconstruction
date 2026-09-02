# RQIR research log — Iteration 270

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Continued from authoritative Iteration 269 after verifying the corrected orbit-density convention, recovery state, recent commits and zero active GitHub Actions.

The next physical target is the eight-representative routed `B3[s,a,b]`. Before evaluating it numerically, the projected identity `A_{gamma delta}=K^j_{gamma delta} E_j` was audited in condensed-index/Fourier space.

The key result is exact: the contracted field-space index `j` carries a spacetime momentum. For a polarized factor `K_m[S] E_n[T]`, translational support is

`p_out-p_in = k_S + q_j`,

while contraction with `E[T]` fixes `q_j=k_T`. Therefore the physical support is `k_S+k_T`, and the momentum of the contracted EOM index must remain an explicit routing label until contraction.

A `K_m` represented only as a local finite matrix depending on the incoming orbit momentum and its explicit background subset `S` is under-specified for physical `A`. Multiplying such matrices could produce an apparently nonzero `B3` while silently dropping the field-space Fourier convolution.

A reproducible enumeration certificate verifies the frozen null-soft projected counts: `A1[s]=0`, `A2[s,a]=2` survivors, `A2[s,b]=2`, `A2[a,b]=3`, and `A3[s,a,b]=6`. All eight forward `B3` transpose-class representatives retain total support `k_s+k_a+k_b` provided this contracted EOM momentum is preserved.

Freeze `PASS_EXACT_PROJECTED_A_CONTRACTED_FIELD_MOMENTUM_ROUTING`.

Guardrails: `NO_DROP_CONTRACTED_EOM_MOMENTUM_IN_K_KERNEL` and `NO_PREMATURE_LOCAL_MATRIX_K_TIMES_E_AS_PHYSICAL_A`.

Classification: implementation/provenance gate only. This is not a consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, novelty certificate or Candidate Gravity residual.

`MODEL_READINESS: 24%` — change from Iteration 269: **0 percentage points**. A mandatory physical-routing ambiguity has been eliminated, but comparator foundation remains `24/25`, robust unique residual remains `0/20`, and explicit routed numerical `A/B3` plus tensor/source projection are still open.

C5 retains `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION` and `BLOCKED_NOT_ZERO`. `ANSATZ-003` is not created. Fisher/resources and blind heavy integration remain forbidden.

Exact next gate: implement `K_m[S](p_out,p_in;q_j)` (or an equivalent representation retaining the contracted field momentum) from the frozen affine `R`, `Gamma0/Gamma1/Gamma2` and 2/4/7 primitive library; contract with certified `E1/E2/E3` to obtain physical routed `A1/A2/A3`; then evaluate the eight forward `B3` representatives with corrected Iteration-269 `Q2` and reconstruct seven partners via endpoint reversal / real `-K` sector. Only after all transpose regressions pass may explicit nonzero `B3` be frozen.
