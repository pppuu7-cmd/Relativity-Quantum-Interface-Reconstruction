# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **606**.
- Frozen Iter424 is **5/5 PASS**; Iter581 exact15 is raw-valid PASS; Iter582 q2-resolved `D_s Gamma_{e=2}` assembly is PASS/non-residual.
- Iter583–594 establish the same-parent MSSC contacts, exact routing/normalization, complete 13-family cubic source object and analytic-origin bookkeeping.
- Iter595–596 freeze the full five-class nonlinear diffeomorphism Ward contract.
- Iter601 closes endpoint covariance; Iter602 remains preserved historical negative authority; Iter603 diagnoses finite-lattice-radius sensitivity; Iter604 prospectively freezes the convergence contract.
- Iter605 is independently raw-consumed PASS for full source-level nonlinear Ward consistency under Iter604.
- **Iter606 is independently raw-consumed PASS for the prospective full-observable source-to-Iter582/native-linked mapping contract.** It is contract-only/non-residual and does not change readiness.

## Iter605 Ward authority
Run `34243453623`, head `88c617a767554f8817b33ae7ce5df7717e2e9d2b`, artifact `10063254435`, digest `sha256:ba5e2b96c87649044b2cf83258d2909f0b34794fd07abc5f4e4ab9dfc0a75eef`; raw result SHA-256 `83795f61703ee96d40d97c4ccadd818406094474f40c318f66639d53426e2d74`; audit `PASS_RAW_AUDIT_ITER605_PRODUCTION_WARD`, `failures=[]`. All 12 rows PASS; all 13 source families retained.

## Iter606 mapping-contract authority
Run `34250296480`, job `102142707926`, head `32745982fecc4806b7be04ac26bf3cad9fdccef0`, artifact `10065691200` (`rqir-iter606-source-to-iter582-mapping-contract`), digest `sha256:adf8682243953d43180a979bea083003d65d811a044264b5f27cfab9518e48a3`; raw result SHA-256 `97363bbdef0bb1443fbe81858c236b552bc0cbad29650bca4ff6cce3edfca94c`; raw audit SHA-256 `5c07980b26e4254bf37e0173b9675b768aa40033270d08dc3e81354ff348f1d2`; `PASS_RAW_AUDIT_ITER606_MAPPING_CONTRACT`, `failures=[]`.

Frozen before projection output: Iter582 q2 buckets `[-1.0,-0.34,-0.14]` remain distinct; exact Iter582 weights and all 13 same-parent MSSC source families are preserved; ordinary finite branch cut, scalar-pole distribution and local/contact origin must be classified separately; unsupported scalar-pole projection into native linked `Y=(K2,S_soft2_full)/T_cut` is `BLOCKED`, never zero-filled; K1^3 cannot be deleted merely because it is meromorphic away from scalar poles; no Source/Born subtraction, new normalization, estimator, threshold, q2 regrouping or unproved repartition.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`:
- `q^2=-1.0`: `+0.0003272233895861266 i`
- `q^2=-0.34`: `-0.00371666346186323 i`
- `q^2=-0.14`: `-0.0007997265433511544 i`

No Source/Born subtraction has been performed.

## Active gate — Iter607
Fail-closed full-observable source-to-Iter582/native-linked projection evaluator commit `f6ef6ad6f2da7e2dd8a2fbd4c710e09cc5fb107f`; workflow launch commit `6ff91b1d66bfd378f827560f673f89afbb28f6d7`.

Iter607 consumes Iter605+606 and checks whether repository authority contains an explicit scalar-pole distribution -> native `Y/T_cut` projector, including the kinematic pullback and normalization/sign prescription needed to bind distributional scalar poles to the frozen Iter582 coordinate. Missing authority is a valid `BLOCKED` result, never zero-fill. `BLOCKED` is uploaded as raw scientific output; provenance drift fails CI.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

## Exact next gate
Terminal Iter607 -> independent raw artifact consumption. If an explicit projector is present, execute the matched projection. If Iter607 returns `BLOCKED_ITER607_EXPLICIT_DISTRIBUTIONAL_SOURCE_TO_NATIVE_LINKED_PROJECTOR_ABSENT`, preserve it and derive/prospectively freeze that projector from the same MSSC parent kinematics and native observable definition before rerunning the projection. No Source/Born subtraction or comparator quotient before a raw-valid matched observable exists.

Until the full matched source-to-Iter582/native-linked map is raw-valid: no Source/Born subtraction; no comparator quotient; no `ANSATZ-003`; no Fisher/resources.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc estimator, altered normalization, changed q2 grouping, threshold weakening, ansatz tuning or unproved internal repartition. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Closed C5 null-soft e=3 authority is not reopened.
