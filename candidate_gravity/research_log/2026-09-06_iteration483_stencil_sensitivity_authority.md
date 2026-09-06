# RQIR Candidate Gravity — Iteration 483 stencil-sensitivity authority

Date: 2026-09-06

The sole heavy numerical authority candidate remains frozen manifest rank 12 `(u,v)=(+1e-5,-1e-5)`, run `33997856739`, job `101391409387`, still in progress on the scientific MP stage. No duplicate heavy run was launched and no workflow-green state was promoted without raw artifact inspection.

Iteration 483 adopts the already committed post-482 central4 stencil-sensitivity audit as non-promoting research authority. For `c=(1/12,-2/3,+2/3,-1/12)`, the mixed-derivative absolute stencil-weight total is `9/4`. Current raw-certified BASE ranks `0..11` carry `17/18 = 94.444444%` of BASE stencil-L1 sensitivity, while current HALF certification carries only `1/81 = 1.234568%` of HALF stencil-L1 sensitivity. The four future HALF inner-inner ranks `19,20,23,24` alone carry `64/81 = 79.012346%` of HALF absolute stencil weight.

This demonstrates that occurrence-weighted support coverage (`16/32 = 50%`) and derivative-sensitivity coverage are materially different diagnostics. It strengthens the retained requirement for complete local support certification followed by independent BASE/HALF MP80/MP120 assembled closure. It does not authorize source reordering, early assembly promotion, estimator changes, threshold changes, or physical promotion.

Result provenance: `candidate_gravity/results/post482_stencil_sensitivity_weight_audit.json`, commit `be4c7bf93b06f78859464bd626341383656ba788`. Recovery provenance: `candidate_gravity/recovery/ITERATION483_RECOVERY_DELTA.md`, commit `ff77683733254fca36101ed0002e083b3c22b20d`.

Classification: `PASS_OCCURRENCE_COVERAGE_DISTINCT_FROM_ASSEMBLY_SENSITIVITY_COVERAGE__NON_PROMOTING`.

**MODEL_READINESS: 24% (unchanged).**
