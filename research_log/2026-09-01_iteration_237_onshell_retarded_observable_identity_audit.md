# Research log — RQIR Candidate Gravity Iteration 237

Date: 2026-09-01

MODEL_READINESS: 24%

Started from repository authority: `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, Iteration-236 recovery delta/research log, recent commits and current Actions state. Authoritative front was Iteration 236; GitHub Actions reported no workflow runs.

## Scientific action

Audited the hard observable-identity gate for the executable massive-scalar GR radiative branch selected in Iteration 236.

The key question was whether the physical one-loop `2 -> 3` graviton-radiation unitarity discontinuity can be identified directly with the frozen retarded/source-completed nonlinear response entering

`T_cut = D Gamma3_ret,soft - W[D K2]`.

Fresh causal-response literature materially changes the status. Caron-Huot et al. (JHEP 01 (2024) 139, arXiv:2308.02125) formulate asymptotic radiation observables through generalized LSZ of response functions and as combinations of amplitudes and products of amplitudes. Biswas–Parra-Martinez (JHEP 07 (2025) 037) derive asymptotic in-in observables from amputated causal response functions in the Schwinger–Keldysh basis. Bini et al. (Phys. Rev. D 109, 125008 (2024)) explicitly show that the classical gravitational waveform contains a five-point amplitude term plus a distinct unitarity-cut term. Capatti–Zeng (Phys. Rev. D 111, 125002 (2025)) show how retarded causal flow emerges after the appropriate amplitude/cut combination in tested classical sectors.

## Result

A single in-out `2 -> 3` amplitude discontinuity is **not** the complete in-in/retarded radiation observable. The required observable contains extra cut/product-of-amplitudes contributions fixed by generalized LSZ / Keldysh ordering. Therefore the Iteration-236 shortcut fails the observable-identity gate.

Freeze:

`ON_SHELL_PROXY_NOT_OBSERVABLE_IDENTICAL`

with

`BLOCKED_CAUSAL_RESPONSE_COMPLETION_REQUIRED_BEYOND_SINGLE_2TO3_UNITARITY_DISCONTINUITY`.

New labels:
- `REL-NG-017`;
- `REL-CUT-017`;
- `REL-BLOCK-002`;
- `NG-FUNNEL-093`.

This is not a consistency FAIL of GR, not an exact comparator identity, not regime-specific non-identifiability, not near-degeneracy and not Candidate Gravity novelty. It is a negative result for the proposed proxy identity.

No heavy computation was launched because causal observable completion remains an upstream algebraic hard constraint. No Candidate Gravity residual. No `ANSATZ-003`. No Fisher/resources.

MODEL_READINESS: 24%

Readiness change from Iteration 236: 0 percentage points. The proxy question is resolved and the missing structure is now explicit, but comparator foundation remains `24/25` and robust unique residual remains `0/20`.

Next gate: Iteration 238 must attempt a **direct generalized-LSZ causal-response representation** of the frozen linked observable in the same massive-scalar GR parent. All retarded leg assignments, LSZ normalizations, hard-channel discontinuity, contact/source Ward terms and IR subtraction must arise from one Keldysh convention. If that completed causal observable is structurally different from the frozen `Gamma3_ret - W[K2]` relation, freeze the branch as comparator-incompatible rather than redefining the target.