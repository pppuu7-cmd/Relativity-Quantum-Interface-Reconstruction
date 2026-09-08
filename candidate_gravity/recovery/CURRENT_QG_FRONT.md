# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **604**.
- Frozen Iter424 is **5/5 PASS**; Iter581 exact15 is raw-valid PASS; Iter582 q2-resolved `D_s Gamma_{e=2}` assembly is PASS/non-residual.
- Iter583–590 freeze the same-parent MSSC source contacts, exact fixture binding, K1/K2 normalization and complete cubic family census `K3 + 6 K1/K2 + 6 K1^3`.
- Iter591–594 establish analytic structure and the complete 13-family routed same-action cubic source object; it is finite/nonzero/permutation-symmetric but NON_WARD.
- Iter595–596 freeze the full five-class nonlinear diffeomorphism Ward contract.
- Iter601 derives the correct endpoint realization from the frozen Fourier rule and raw-validates all 12 Iter587 one-leg anchors.
- Iter602 is a preserved negative frozen result: 9/12 rows show no threshold failure; `s/xi0`, `s/xi1`, `s/xi2` fail and also fail the frozen FD-convergence criterion.
- Iter603 is independently raw-consumed diagnostic-only authority: those same three rows are strongly finite-lattice-radius sensitive; Iter602 remains historical FAIL and Iter603 is not a model PASS.
- **Iter604 is independently raw-consumed PASS for the prospective finite-lattice boundary/convergence contract. It is contract-only/non-residual and does not change readiness.**

## Iter601 endpoint covariance authority
Frozen Fourier rule: `Delta_xi phi(k)=int xi(l)(k-l)_rho phi(k-l)`.
For `p_r=p_c+q`: right endpoint `R_rc = xi . p_c`; left dual-row endpoint `L_rc = - xi . p_r`; Green covariance identity `Delta G - R G - G L = 0`.
Raw Iter601: run `34239749577`, job `102106569680`, artifact `10061419511`; max corrected one-leg anchor residual `6.88338845912217e-15 <= 2e-11`.

## Iter602 preserved negative authority
Run `34240030976`, job `102107522186`, artifact `10061578531`, digest `sha256:09f7ef6a98327abff416d46b32a99bfec599a9b68d04edacd91c019ce3436d56`, raw result SHA-256 `2897821038b495562d316c56ea40bf051b969a258ece5a2ee2bddc944981d138`.
All 12 one-leg anchors and the Iter594 13-family assembly prerequisite pass. Only `s/xi0=0.006096828631513357`, `s/xi1=0.0035599485158516048`, `s/xi2=0.0035599485212443388` fail the Ward threshold, and all three simultaneously fail the frozen last-FD-step convergence condition.

## Iter603 diagnostic authority
Run `34240339709`, job `102108562629`, head `fcd8f27a6d72bb139bf3fc0f05eb1a74f51efbcf`, artifact `10061784026`, digest `sha256:fb1755978a482279325a711e2995e58c3040a64721deb529bf59a16baf3326e6`; raw result SHA-256 `44d1266cffaf4d4579f10a3eb0e72efe0dcd90a5f4a429eeabcc7f00ebd67d3d`.
Changing only `LAT_R=3,4,5` gives `s/xi0: 1.9380e-2 -> 1.0197e-3 -> 1.5197e-11`, `s/xi1: 1.0434e-2 -> 6.1059e-4 -> 3.5861e-12`, `s/xi2: 1.0434e-2 -> 6.1059e-4 -> 3.2330e-12`. At R5 every other row is `<=5.64e-12`. Condition estimates remain `~1e18`, so no radius is promoted post-hoc.

## Iter604 prospective lattice contract authority
Canonical run `34242971065`, head `e745984401f6e572f8077a2e4ecff222f73c4728`, artifact `10062757495`, digest `sha256:5457f02b088800b849afce2d21e099435e99cb3f450173f3d6da8e686b4a8895`; raw `result.json` SHA-256 `f6c926e16f8205dc6c4fc3e8c67afcf0b2dd91eff09aab8371fd6eb0687fa909`; raw audit SHA-256 `98bc03c661f4b219e26e5e19aef48af2048f0624f89eba038c6eecd3e4c1d639`, `failures=[]`.
Frozen before production: `R=4,5,6`; unchanged FD steps `(2e-2,1e-2,5e-3)`; unchanged Ward threshold `2e-6`; unchanged final FD threshold `2e-5`; separate `|W_R6-W_R5|<=2e-6`; all 12 one-leg anchors `<=2e-11` at R5/R6; Iter594 assembly cross-check `<=2e-5`; all 13 source families retained. Radius/FD failure is `BLOCKED_CONVERGENCE`; converged above-threshold row is `FAIL_WARD`. No condition-number waiver.

## Active gate — Iter605
Production evaluator commit `06e2e8ad4b4a6b4c0cfbf5c7c1f83575eac71ca6`; workflow launch commit `88c617a767554f8817b33ae7ce5df7717e2e9d2b`. Iter605 evaluates all 12 frozen Ward rows at R4/R5/R6, recomputes the 12 one-leg anchors at R5 and R6, inherits the already-closed complete 13-family assembly prerequisite, and applies exactly the Iter604 classification logic. Scientific FAIL/BLOCKED is still uploaded as a valid raw result.

## Frozen nonlinear Ward convention
Use `f(x)=int exp(-ik.x) f(k)` and stripped generator `Delta_xi=i delta_xi`. All five classes remain mandatory: gauge-leg linear contraction, spectator-u Lie derivative, spectator-v Lie derivative, left endpoint transformation, right endpoint transformation. Exact Iter588 fixture, all 13 source families, symmetric scalar route `p=-q_g/2`, `p'=+q_g/2`, normalization and thresholds remain unchanged.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets distinct: `q^2=-1.0: +0.0003272233895861266 i`; `q^2=-0.34: -0.00371666346186323 i`; `q^2=-0.14: -0.0007997265433511544 i`. No Source/Born subtraction has been performed.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

## Exact next gate
Terminal Iter605 -> independent fail-closed raw artifact consumption. If all rows, anchors, radius stability and assembly prerequisites PASS, then and only then proceed to the full-observable source-to-Iter582/native-linked map. If any row is `BLOCKED_CONVERGENCE` or `FAIL_WARD`, preserve it and localize without weakening Iter604.

Until full source-level Ward closure: no Source/Born subtraction; no source-to-Iter582 mapping; no comparator quotient; no `ANSATZ-003`; no Fisher/resources.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc estimator, altered normalization, changed q2 grouping, threshold weakening, ansatz tuning or unproved internal repartition.
