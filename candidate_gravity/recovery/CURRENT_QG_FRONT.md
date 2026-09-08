# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **608**.
- Frozen Iter424 is **5/5 PASS**; Iter581 exact15 raw-valid PASS; Iter582 q2-resolved `D_s Gamma_{e=2}` assembly PASS/non-residual.
- Iter583–594 establish same-parent MSSC contacts, exact routing/normalization, the complete 13-family cubic source object and analytic-origin bookkeeping.
- Iter595–596 freeze the full five-class nonlinear diffeomorphism Ward contract; Iter601 closes endpoint covariance; Iter602 remains preserved historical negative authority; Iter603 diagnoses finite-radius sensitivity; Iter604 freezes the convergence contract.
- Iter605 is independently raw-consumed PASS for full source-level nonlinear Ward consistency.
- Iter606 is independently raw-consumed PASS for the prospective source-to-Iter582/native-linked mapping contract.
- Iter607 is independently raw-consumed `BLOCKED_ITER607_EXPLICIT_DISTRIBUTIONAL_SOURCE_TO_NATIVE_LINKED_PROJECTOR_ABSENT`: missing scalar-pole distribution -> native `Y/T_cut` projector is a mapping blocker, not model FAIL and never zero-fill.
- **Iter608 is independently raw-consumed PASS for the universal scalar-pole distribution kernel only.** It is non-residual; the concrete MSSC->native pullback/Jacobian and native normalization/sign remain blocked.

## Iter608 distribution authority
Run `34250726949`, head `ad00230b9eb7d48c9eae04726256b2bf64d51f32`, artifact `10065869899`, digest `sha256:126d9a5fe82a19eefd3826201348891f6896f9494d5f0a307da4d63fbfeb18c5`; raw result SHA-256 `2cbd3b8d09dd4d6d5297006802c3f4451df4e19bf9bef96d24906274032471ff`; raw audit SHA-256 `72b9a57e5b0904bd1c6ceca889af0096bd8d21d15d17c53d0044f10cfe1bb95e`; `PASS_RAW_AUDIT_ITER608_SCALAR_POLE_KERNEL`, `failures=[]`.

Frozen convention: `x=m^2-p^2`, Feynman `+i0`, `Disc F=F(x+i0)-F(x-i0)`, hence `Disc[1/(m^2-p^2+i0)] = -2*pi*i*delta(m^2-p^2)`. For simple real roots, `delta(f(z))=sum_i delta(z-z_i)/abs(f'(z_i))`.

Still blocked exactly: (1) concrete internal MSSC `p_j^2(q^2)` relation for each retained source family; (2) root/Jacobian support in the native linked variable; (3) native `Y=(K2,S_soft2_full)/T_cut` normalization/sign binding to Iter582 without Born subtraction. All 13 source families and q2 buckets `[-1.0,-0.34,-0.14]` remain distinct. `zero_fill=false`. Source/Born subtraction `NOT_PERFORMED`.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`:
- `q^2=-1.0`: `+0.0003272233895861266 i`
- `q^2=-0.34`: `-0.00371666346186323 i`
- `q^2=-0.14`: `-0.0007997265433511544 i`

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

## Exact next gate — Iter609
Derive and prospectively freeze the concrete internal-momentum-to-native-cut kinematic pullback `p_j^2(q^2)` and the corresponding simple-root Jacobian/support from the already frozen MSSC fixture and native observable definition, family by family as required. Do not invent a native normalization/sign. If the repository authority does not determine the pullback uniquely, classify that point `BLOCKED`; never zero-fill or choose a post-hoc estimator. Only after the kinematic pullback/Jacobian is raw-valid may the native `Y/T_cut` normalization/sign binding be closed and the matched projection rerun.

Until the full matched source-to-Iter582/native-linked map is raw-valid: no Source/Born subtraction; no fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient; no `ANSATZ-003`; no Fisher/resources.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc estimator, altered normalization, changed q2 grouping, threshold weakening, ansatz tuning or unproved internal repartition. K1^3 is retained in the full same-parent response; it cannot be deleted merely because it is meromorphic away from scalar poles. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Closed C5 null-soft e=3 authority is not reopened.
