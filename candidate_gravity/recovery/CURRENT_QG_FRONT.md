# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **603**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` assembly is PASS, non-residual.
- Iter583–584 close the same-parent MSSC-001 quadratic K2 contact and mixed bilinear `K2(h1,h2)`.
- Iter586–590 freeze the timelike off-shell source completion, exact Iter368/582 fixture binding, K1/K2 normalization, and complete cubic family census `K3 + 6 K1/K2 + 6 K1^3`.
- Iter591–594 establish K3/K1^3 analytic structure and explicitly assemble the complete 13-family routed same-action cubic source object; it is finite/nonzero/permutation-symmetric but NON_WARD.
- Iter595–596 prospectively freeze the full nonlinear diffeomorphism Ward contract with five mandatory classes and exact Iter587 one-leg reduction.
- Iter597 is diagnostic only; Iter598 proves it used off-contract scalar probes. Iter599 corrects the scalar route but fails the one-leg matrix anchor; Iter600 blocks those Ward numbers as nonauthoritative.
- **Iter601 derives the correct endpoint matrix realization directly from the frozen Fourier rule and raw-validates all 12 Iter587 anchors.**
- **Iter602 reruns the full frozen nonlinear Ward gate with only the endpoint realization changed. It is a preserved negative frozen result: 9/12 rows show no threshold failure; `s/xi0`, `s/xi1`, `s/xi2` fail and simultaneously fail the frozen FD-convergence criterion.**
- **Iter603 independently raw-consumes the non-promoting radius diagnosis and shows that those same three rows are strongly finite-lattice-radius sensitive. Iter602 remains historical FAIL; Iter603 is not a model PASS.**

## Iter601 endpoint covariance authority
Frozen Fourier rule:
`Delta_xi phi(k)=int xi(l)(k-l)_rho phi(k-l)`.
For `p_r=p_c+q`:
- right/column endpoint `R_rc = xi . p_c`;
- left/dual-row endpoint `L_rc = - xi . p_r`;
- Green covariance identity `Delta G - R G - G L = 0`.

Raw Iter601: run `34239749577`, job `102106569680`, artifact `10061419511`; max corrected one-leg anchor residual `6.88338845912217e-15 <= 2e-11`.

## Iter602 frozen nonlinear Ward negative authority
Canonical provenance:
- evaluator commit `703eaf4635ed2b0ad82a2da51b350e1b51d9a8a2`;
- workflow/head `c3b5d0f796e32be0999e09224031e54b4d494742`;
- run `34240030976`, job `102107522186`;
- artifact `10061578531`, digest `sha256:09f7ef6a98327abff416d46b32a99bfec599a9b68d04edacd91c019ce3436d56`;
- raw result SHA-256 `2897821038b495562d316c56ea40bf051b969a258ece5a2ee2bddc944981d138`.

All 12 one-leg anchors and the Iter594 13-family assembly prerequisite pass. Only `s/xi0=0.006096828631513357`, `s/xi1=0.0035599485158516048`, `s/xi2=0.0035599485212443388` fail the Ward threshold, and all three simultaneously fail the frozen last-FD-step convergence condition. Classification remains:
`FAIL_RAW_CONSUMED_FULL_SOURCE_LEVEL_NONLINEAR_WARD_WITH_ITER601_ENDPOINT_REALIZATION__PRESERVED_NEGATIVE_RESULT`.

## Iter603 radius-diagnosis authority
Canonical provenance:
- run `34240339709`, job `102108562629`;
- head `fcd8f27a6d72bb139bf3fc0f05eb1a74f51efbcf`;
- artifact `10061784026`, digest `sha256:fb1755978a482279325a711e2995e58c3040a64721deb529bf59a16baf3326e6`;
- raw result SHA-256 `44d1266cffaf4d4579f10a3eb0e72efe0dcd90a5f4a429eeabcc7f00ebd67d3d`;
- raw audit `PASS_DIAGNOSTIC_RAW_AUDIT_ITER603`, `failures=[]`.

Changing only `LAT_R=3,4,5` gives:
- `s/xi0`: `1.9380e-2 -> 1.0197e-3 -> 1.5197e-11`;
- `s/xi1`: `1.0434e-2 -> 6.1059e-4 -> 3.5861e-12`;
- `s/xi2`: `1.0434e-2 -> 6.1059e-4 -> 3.2330e-12`.
At `R=5`, `s/xi3=5.62e-15` and every other row is `<=5.64e-12`. The `s`-sector kernel condition estimates remain `~1e18`, so no single enlarged radius is promoted post-hoc.

Classification:
`PASS_RAW_CONSUMED_DIAGNOSTIC_ITER602_S_ROWS_STRONGLY_LATTICE_RADIUS_SENSITIVE__NON_PROMOTING`.

## Active gate — Iter604
A prospective finite-lattice boundary/convergence contract has been frozen **before** any new production Ward rerun. It keeps the continuum identity, fixture, 13 source families, symmetric route, FD steps and original Ward/FD thresholds unchanged. The new nested-radius authority rule is `R=4,5,6`; production authority requires both `R=5` and `R=6` to satisfy the unchanged Ward and FD thresholds, plus `|W_R6-W_R5| <= 2e-6`, all 12 one-leg anchors `<=2e-11`, and the Iter594 assembly cross-check `<=2e-5`. Any radius/FD failure is fail-closed `BLOCKED_CONVERGENCE`; a converged above-threshold row is `FAIL_WARD`.

Contract file: `candidate_gravity/contracts/ITERATION604_FINITE_LATTICE_BOUNDARY_CONVERGENCE_CONTRACT.md`.
Contract commit: `ae534de1d5735fefc963fad0485195156930e4f4`.
Evaluator commit: `2db1e12f18ed9fbf00b95644ffcb267e2abb0697`.
Workflow launch commit: `e745984401f6e572f8077a2e4ecff222f73c4728`.

Iter604 is contract-only / non-residual. It cannot change MODEL_READINESS or erase Iter602.

## Frozen nonlinear Ward convention
Use `f(x)=int exp(-ik.x) f(k)` and stripped generator `Delta_xi=i delta_xi`. All five classes remain mandatory: gauge-leg linear contraction, spectator-u Lie derivative, spectator-v Lie derivative, left endpoint transformation, right endpoint transformation. The exact Iter588 fixture is inherited. No momentum split, gauge normalization, result-dependent polarization, family deletion, threshold weakening or post-hoc source repartition is permitted. Scalar route for gauge leg `g` is exactly `p=-q_g/2`, `p'=+q_g/2`.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets distinct:
- `q^2=-1.0`: `+0.0003272233895861266 i`;
- `q^2=-0.34`: `-0.00371666346186323 i`;
- `q^2=-0.14`: `-0.0007997265433511544 i`.
No Source/Born subtraction has been performed.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

## Exact next gate
Consume Iter604 raw contract artifact. If raw-valid PASS, launch Iter605 production rerun of the unchanged full source-level nonlinear Ward identity under the prospectively frozen `R=4,5,6` convergence contract. Only an independently raw-consumed Iter605 result may become new Ward authority; Iter602 remains preserved historical authority.

Until full source-level Ward closure:
- no Source/Born subtraction;
- no source-to-Iter582 mapping;
- no comparator quotient;
- no `ANSATZ-003`;
- no Fisher/resources.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Nonconvergent negative rows are preserved but not promoted into stable model-level claims. No post-hoc estimator, altered normalization, changed q2 grouping, threshold weakening, ansatz tuning or unproved internal repartition.
