# Candidate Gravity article / negative-results matrix — Iteration 270

**Authoritative iteration:** 270  
**MODEL_READINESS: 24%**

| Sector | Scoped result | Classification | Article-safe claim |
|---|---|---|---|
| Projected `A=K E` routing | For `K_m[S]E_n[T]`, contracted EOM momentum is part of kernel routing: `p_out-p_in=k_S+k_T` | exact implementation/provenance certificate | Physical projected Vilkovisky numerators require the condensed-index Fourier convolution; do not drop the momentum of the contracted field-space index. |
| Physical routed A | Direct same-parent `A=R(DR)E` gives nonzero `A1[a/b]`, mixed `A2`, and `||A3[s,a,b]||_F=2.2278189997`; `A1[s]` is numerical zero at `1e-9` | scoped physical coefficient certificate | The complete projected cubic A-layer exists and passes permutation/endpoint-transpose regressions at the finite-difference envelope. |
| Null-soft B3 bookkeeping | Physical implementation reproduces 19 generic terms -> 15 survivors; four `A1[s]` terms contribute only `||B19-B15||_F=2.56e-8` numerically | exact null-soft reduction realized | The frozen 19-to-15 reduction survives the explicit same-parent routed implementation. |
| B3 transpose classes | All 8 forward representatives are nonzero; direct 15-term sum and 8-class reconstruction agree to `2.78e-16`; worst endpoint-transpose residual `3.29e-7` | scoped implementation/physical regression PASS | The 15-to-8 transpose-class reduction and endpoint-reversal semantics survive explicit physical realization. |
| Physical C5 numerator | `||B3[s,a,b]||_F=2.2209140981`, `max|B3|=1.3471946832`, stable under step scans | `PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED` | The scoped physical routed finite-cubic C5 numerator is explicitly nonzero at the frozen generic point. This authorizes tensor reduction but is not the final comparator coordinate. |
| Remaining C5 work | tensor/master-integral reduction, nonanalytic hard-channel extraction, source/Ward/contact completion, Lorentzian projection, normalization | operational BLOCKED downstream of a nonzero numerator | The old `BLOCKED_NOT_ZERO` label is superseded for this scoped numerator; the current blocker is reduction/projection, not algebraic existence. |
| Candidate residual | none | absence of residual/novelty certificate | Do not create/promote `ANSATZ-003`; no Candidate Gravity discovery claim follows from nonzero B3 alone. |
| Fisher/resources | forbidden | hard workflow gate | Fisher/resource forecasts remain unauthorized until a robust residual survives the fixed comparator quotient. |

New/retained Iteration-270 certificates:

`PASS_EXACT_PROJECTED_A_CONTRACTED_FIELD_MOMENTUM_ROUTING`

`PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED`

Guardrails:

`NO_DROP_CONTRACTED_EOM_MOMENTUM_IN_K_KERNEL`

`NO_PREMATURE_LOCAL_MATRIX_K_TIMES_E_AS_PHYSICAL_A`

`NONZERO_B3 IS A C5 NUMERATOR CERTIFICATE ONLY; DO NOT PROMOTE TO FINAL COMPARATOR OR CANDIDATE RESIDUAL BEFORE TENSOR_REDUCTION_SOURCE_COMPLETION_AND_HARD_CHANNEL_PROJECTION`.

Current umbrella C5 blocker:

`BLOCKED_4D_EINSTEIN_VD_TENSOR_REDUCTION_SOURCE_PROJECTION_AND_LORENTZIAN_HARD_CHANNEL`.
