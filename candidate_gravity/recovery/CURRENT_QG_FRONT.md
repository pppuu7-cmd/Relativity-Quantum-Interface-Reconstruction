# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **582**.
- Historical Iter421 `BLOCKED_CONVERGENCE` remains provenance only; frozen Iter424 is **5/5 PASS** and post-Iter580 unresolved physical set is `[]`.
- Physical index2 was promoted only under the pre-existing Iter407 BASE-h parent value rule; no post-hoc estimator was introduced.
- Frozen Iteration412 exact15 `Tr U1^2` assembly is **raw-valid PASS** via Iter581.
- Complete connection-sector `D_s Gamma_{e=2}` effective-action operator coordinate is now assembled q2-by-q2 in Iter582 using unchanged frozen weights.
- Iter582 classification: `PASS_GAMMA_E2_Q2_RESOLVED_FROZEN_WEIGHT_ASSEMBLY__NON_RESIDUAL`.

## Iter581 exact15 raw authority
Workflow run `34198120530`, head `5e2ebad51937b0961367ac1711b8ae803c10312b`, artifact `10044688726` (`rqir-iter581-frozen-iter412-exact15`), artifact digest `sha256:0826bfa6cd3cfda786517723723e72d706539bf28878cc1b3bcb376b9755613d`.

Independent artifact inspection verified:
- scientific result SHA256 `77970170c5a10e42bb9b5f846204d9a34348436b674da7e1437977a02bdb47e4`;
- authority audit `PASS_RAW_AUTHORITY_AUDIT_ITER581_EXACT15`;
- failures `[]`, `raw_result_integrity_valid=true`;
- exact 15 unique double-double channels, q2 counts 5/5/5.

Complete `D_s Tr U1^2` before the `-i/4` weight:
- `q^2=-1.0`: `-0.00023980872107801175`;
- `q^2=-0.34`: `0.013398451327883773`;
- `q^2=-0.14`: `0.000053572393143931426`.

## Iter406 complete Tr U2 authority
Before the `+i/2` weight:
- `q^2=-1.0`: `+0.0005345424186332474`;
- `q^2=-0.34`: `-0.000734101259784574`;
- `q^2=-0.14`: `-0.001572666890130343`.

## Iter582 frozen effective-action assembly
Using, without alteration,

`D_s Gamma_e2(q^2) = +(i/2) D_s Tr U2(q^2) -(i/4) D_s Tr U1^2(q^2)`

strictly q2-by-q2 gives:
- `q^2=-1.0`: `D_s Gamma_e2 = +0.0003272233895861266 i`;
- `q^2=-0.34`: `D_s Gamma_e2 = -0.00371666346186323 i`;
- `q^2=-0.14`: `D_s Gamma_e2 = -0.0007997265433511544 i`.

Distinct q2 buckets remain separate. No Source/Born subtraction has been performed yet.

## Strict scientific classification
Iter581 and Iter582 close genuine operator-coordinate prerequisites. They are **not** Candidate-Gravity consistency PASS/FAIL, not exact comparator identity, not regime-specific model non-identifiability, not near-degeneracy, and not a novelty certificate.

A concrete algebraic `Source/Ward/contact+K2` object derived from the same parent dynamics/routing/numerator/sign/normalization convention is still absent. Therefore the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remains **operationally BLOCKED**. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change from Iter580/581: **0 percentage points**. Exact15 and the e=2 operator assembly close important upstream gates, but no complete additional model-level rubric sector has closed.

## Exact next gate
Derive the concrete algebraic `Source/Ward/contact+K2` object from the **same declared frozen dynamics and parameter convention** and map it to the Iter582 q2-resolved operator coordinate. Only after that object is explicit may the unchanged fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient be applied. If the comparator-subtracted algebraic residual is exactly zero or comparator-identical, preserve that as a negative scientific result rather than tuning an ansatz.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, altered normalization, changed q2 grouping, Source/Born subtraction before matched-observable pole/cut-origin classification, threshold weakening, or ansatz tuning. Distinct q2 buckets remain separate. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
