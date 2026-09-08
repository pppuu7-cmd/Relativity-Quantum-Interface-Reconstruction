# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **581**.
- Historical Iter421 `BLOCKED_CONVERGENCE` remains provenance only; the frozen Iter424 higher-precision decision is **5/5 PASS** and post-Iter580 unresolved physical set is `[]`.
- Physical index2 is promotable under the pre-existing Iter407 parent value rule `D_s=-d_base`; Iter424/580 introduced no new estimator.
- Frozen Iteration412 exact15 `Tr U1^2` assembly is now **raw-valid PASS**.
- Iter581 classification: `PASS_RAW_CONSUMED_FROZEN_ITER412_TRU1SQ_EXACT15`.
- Complete `Tr U1^2` operator coordinate is therefore closed q2-by-q2; effective-action weight has not yet been folded.

## Iter580 physical promotion authority
Frozen original Iter421 tensor11 residual at both MP80 and MP120: `1.341057348963658e-8 <= 2e-5`. Together with the four other frozen Iter424 clauses this gives **5/5 PASS**. Parent-dynamics BASE authority is

`D_s(index2,q^2=-1)=0.000334698712595841410717689701215249442611820995807647705078125`.

This is the value used by Iter581 because the pre-existing Iter407 rule stores the channel coordinate from the BASE-h derivative; no post-hoc QUARTER or extrapolated estimator is selected.

## Iter581 exact15 raw authority
Workflow:
- code commit `c59646d82b43630b27c2ac0ab4d590c3424122e7`;
- workflow/head `5e2ebad51937b0961367ac1711b8ae803c10312b`;
- run `34198120530`, job `101970364894`;
- artifact `10044688726`, `rqir-iter581-frozen-iter412-exact15`;
- artifact digest `sha256:0826bfa6cd3cfda786517723723e72d706539bf28878cc1b3bcb376b9755613d`.

Independent artifact download/audit:
- `iteration581_result.json` SHA-256 `77970170c5a10e42bb9b5f846204d9a34348436b674da7e1437977a02bdb47e4`;
- `iteration581_authority_audit.json` SHA-256 `fb5c15d09030d1ffc038555bb738bcd1a29123f6cbebf546089fc9250c3e17b3`;
- audit `failures=[]`, `raw_result_integrity_valid=true`;
- exact 15 unique double-double indices present;
- q2 counts exactly 5/5/5;
- no zero fill, blocked diagnostic value or symmetry substitution.

Raw-valid exact15 double-double sums:
- `q^2=-1`: `0.0020270703668429234`;
- `q^2=-0.34`: `0.01395828640784907`;
- `q^2=-0.14`: `0.0000979561714592546`.

Complete `D_s Tr U1^2` before the `-i/4` weight:
- `q^2=-1`: `-0.00023980872107801175`;
- `q^2=-0.34`: `0.013398451327883773`;
- `q^2=-0.14`: `0.000053572393143931426`.

## Existing Iter406 complete Tr U2 authority
Before the `+i/2` effective-action weight:
- `q^2=-1`: `+0.0005345424186332474`;
- `q^2=-0.34`: `-0.000734101259784574`;
- `q^2=-0.14`: `-0.001572666890130343`.

Distinct q2 buckets are never summed.

## Strict scientific classification
Iter581 closes an operator-coordinate prerequisite. It is **not** Candidate-Gravity consistency PASS, not an exact comparator identity, not model non-identifiability/near-degeneracy and not a novelty certificate.

Concrete upstream algebraic `Source/Ward/contact+K2` and robust comparator-subtracted residual remain absent. Therefore the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remains operationally BLOCKED. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden until a nonzero algebraic residual exists.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change from Iter580: **0 percentage points**. Exact15 closes a major operator prerequisite but no complete stable rubric sector.

## Exact next gate
Combine raw-valid Iter581 complete `Tr U1^2` with authoritative Iter406 complete `Tr U2` **q2-by-q2** using the already frozen effective-action combination

`D_s Gamma_{e=2, connection} = +(i/2) D_s Tr U2 - (i/4) D_s Tr U1^2`.

Raw-validate that assembly. Only then continue to the full `D_s Gamma_{e=2}` bookkeeping and concrete `Source/Ward/contact+K2`; Source/Born subtraction is allowed only in a matched observable after pole/cut-origin classification.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, tensor11 redefinition, u↔v substitution, smaller h, changed radii/nodes/precision, threshold weakening or ansatz tuning. Distinct q2 buckets remain separate. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed comparator quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
