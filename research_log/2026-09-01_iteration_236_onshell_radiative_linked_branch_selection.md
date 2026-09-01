# Research log — RQIR Candidate Gravity Iteration 236

Date: 2026-09-01

MODEL_READINESS: 24%

Started from repository authority: `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, Iteration-235 recovery delta/research log, recent commits, and current Actions state. Authoritative front was Iteration 235; GitHub Actions reported no workflow runs.

## Scientific action

After AS was frozen for the current funnel, searched for an executable same-parent physical branch for the unchanged linked nonanalytic target

`T_cut = D Gamma3_ret,soft - W[D K2]`.

The strongest branch is minimally coupled GR with two massive spinless scalars and one emitted graviton. Georgoudis–Heissenberg–Vazquez-Holm, JHEP 06 (2023) 126, arXiv:2303.07006, provides a one-loop `2 -> 3` radiative amplitude together with the one-loop `2 -> 2` elastic amplitude entering its soft limit, fixed analytic continuation, explicit unitarity cuts, and soft-region terms carrying nonanalytic dependence. The paper explicitly checks that the leading soft behavior factorizes onto the one-loop four-point amplitude and that the relevant imaginary pieces match unitarity cuts.

Independent amplitude/waveform work by Brandhuber et al. (arXiv:2303.06111) and later Georgoudis–Heissenberg–Russo work (arXiv:2312.07452, 2402.06361) confirms that this radiative massive-scalar branch is calculationally executable and that its soft/nonanalytic structure can be handled with controlled IR/frame prescriptions.

## Hard guardrail

This is not yet the frozen RQIR observable. The published object is an on-shell/time-ordered S-matrix amplitude. A physical unitarity cut plus Weinberg soft factorization does not automatically establish the exact retarded/source-completed identity required by `D Gamma3_ret,soft - W[D K2]`.

Classification:

`EXECUTABLE_ONSHELL_LINKED_BRANCH_IDENTIFIED`

plus

`BLOCKED_ONSHELL_TO_RETARDED_SOURCE_COMPLETED_OBSERVABLE_IDENTITY_MAP`.

New labels: `REL-CUT-016`, `REL-NG-016`, `REL-BLOCK-001`, `NG-FUNNEL-092`.

No heavy computation was launched because observable identity is a hard prerequisite. No Candidate Gravity residual. No `ANSATZ-003`. No Fisher/resources.

MODEL_READINESS: 24%

Readiness change: 0 percentage points. Branch selection is now materially narrowed to an executable same-parent amplitude chain, but comparator foundation remains `24/25` until an exact LSZ/CTP/retarded/source-Ward map is established. Robust unique residual remains `0/20`.

Next gate: Iteration 237 must prove or disprove observable identity between the same-parent `2 -> 3` unitarity discontinuity and the frozen retarded three-point discontinuity after LSZ, while deriving `W[D K2]` from the same one-loop `2 -> 2` amplitude and identical IR/source conventions. If extra arbitrary completion is required, classify `ON_SHELL_PROXY_NOT_OBSERVABLE_IDENTICAL` and do not populate `T_cut`.