# Post-479 raw-payload provenance gap delta

**Date:** 2026-09-06  
**Canonical anchor inspected:** Iteration 479  
**MODEL_READINESS:** 24% (unchanged)  
**Physical promotion:** none

## What was checked

The canonical current front was re-read after auto-research advanced to Iteration 479. The sole permitted heavy numerical gate remains manifest rank 11 `(u,v)=(+5e-6,+1e-5)` in Actions run `33989317870`; it was not duplicated.

The post-479 mass-support artifact registry result is internally complete for the currently certified support: ranks 0..10, 11 distinct coordinates, 15 occurrence-weighted source occurrences. Rank 10 is correctly retained as a composite 48+32 row certificate from two disjoint-z raw artifacts.

## Newly localized provenance gap

Workflow run `33992801364` (`RQIR post479 mass-support raw payload inventory`) completed with an **operational failure** in step `Download exact artifact ZIPs and verify upload digests`; the downstream inventory/schema steps were skipped. This is not a scientific failure and does not retract any existing mass-support certificate.

Static source audit also found that `post479_mass_support_raw_payload_inventory.py` currently records SHA-256 for each parsed JSON and receives `scientific_json_sha256` in the frozen expected-source registry, but does **not compare** the observed JSON SHA-256 against that expected canonical scientific JSON SHA-256. Therefore even a future PASS of the current inventory implementation would prove downloadability/list-shape presence, but would not yet bind the selected JSON payload to the canonical scientific JSON identity required for fail-closed assembly.

## Collision-safe diagnostic started

A lightweight, non-scientific-recomputation workflow was added at `.github/workflows/rqir-post479-artifact-digest-semantics-diagnostic.yml`, commit `ee5195626132c42057da49678d3ae32fae421572`, to diagnose one already-certified artifact (`9961449686`) and distinguish REST-download ZIP digest semantics from a genuine registry mismatch. Run `33993624602` is non-promoting and does not duplicate rank 11.

## Required closure before future full-F assembly

1. Resolve the operational ZIP/digest failure without regenerating scientific payloads.
2. Bind every certified source to the exact canonical `scientific_json_sha256`, not merely an arbitrary JSON list of the expected length.
3. Freeze semantic row-schema bindings for coordinate, z, phi, MP80/MP120 and radial-limit fields, including rank-10 48+32 disjoint-z union.
4. Preserve exact Iteration-455 support order and multiplicity; no `u<->v` deduplication.
5. Do not perform full-F/F_uv assembly until all 28 distinct mass coordinates are locally certified.

## Guardrails retained

- NO_ACTIVE_RANK11_DUPLICATION
- NO_REGENERATION_AS_PROVENANCE_SUBSTITUTE
- NO_SUPPORT_REORDERING
- NO_UV_SWAP_DEDUPLICATION
- NO_THRESHOLD_CHANGE
- NO_SMALLER_PHYSICAL_MASS_STEPS
- NO_ANGULAR_ESCALATION_FOR_PROMOTION
- NO_ZERO_FILL
- NO_PHYSICAL_DS_PROMOTION
- NO_ANSATZ003
- NO_FISHER_RESOURCES

This delta is collision-safe and does not claim a new authoritative iteration number.
