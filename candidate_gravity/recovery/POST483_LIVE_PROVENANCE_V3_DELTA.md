# RQIR post-483 live provenance v3 recovery delta

Date: 2026-09-06

**MODEL_READINESS:** 24% (unchanged)  
**Physical promotion:** none

## Closure

The complete currently certified mass-support prefix, frozen manifest ranks `0..11`, has been revalidated against live GitHub Actions artifact state using a historical-schema-aware fail-closed sweep.

The repository historically used four coordinate layouts (`frozen`, `mass_coordinate`, `coordinate`, `frozen_coordinate`) and several provenance layouts (top-level fields, nested `provenance`, rank-11 `source`, and the rank-10 composite correction overlay). V1/V2 incomplete discovery was caused only by those schema transitions.

V3 result:

- complete live-bound ranks: `0..11`;
- missing ranks: none;
- ambiguous ranks: none;
- live binding mismatches: `0`;
- every artifact is unexpired;
- every recovered workflow run ID matches the authority record;
- for every raw artifact, current GitHub metadata digest equals an independently REST-downloaded ZIP SHA-256 and equals the recorded canonical digest;
- rank-10 part 2 uses the frozen post-482 correction overlay: artifact `9959560285` canonical digest `sha256:ac18e784e54414c89e08830d917679ffe0403028abc5ecf6e4e2cdd289158909`, while its scientific JSON SHA remains `2467e807b8b5f1c8a93a83a1e5be2107d2c5ae3d8747bb2f5f586b16501d1c03`.

Classification: `PASS_ALL_CERTIFIED_RANK0_11_LIVE_METADATA_AND_ZIP_BINDINGS_V3__NON_PROMOTING`.

This closes the live artifact-provenance ambiguity for all presently certified local mass-support nodes. It does not add a physical coordinate, does not evaluate missing ranks, and does not authorize full-F assembly before all 28 distinct coordinates are certified.

## Current numerical gate

Frozen manifest rank 12 `(u,v)=(+1e-5,-1e-5)` remains the sole heavy mass-support run. Do not duplicate it. Raw-consume fail-closed after completion.

## Parallel diagnostic

A separate lightweight workflow is assembling the exact class-3 spectral contribution from all currently certified BASE ranks `0..11`, leaving ranks `12..15` explicitly absent rather than zero-filled. Its result is diagnostic-only and cannot be promoted to a BASE derivative authority unless the missing row is later supplied by raw-certified nodes.

Guardrails retained: no result-payload rewrite, no support reorder, no threshold change, no zero fill, no physical D_s promotion, no ANSATZ-003, no Fisher/resources.
