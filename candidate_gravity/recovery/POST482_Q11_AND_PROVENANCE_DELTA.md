# RQIR post-482 Q11/provenance recovery delta

Date: 2026-09-06

**MODEL_READINESS:** 24% (unchanged)  
**Physical promotion:** none

## Active heavy authority candidate

Frozen Iteration-455 manifest rank 12 remains the sole active heavy numerical gate: `(u,v)=(+1e-5,-1e-5)`, run `33997856739`, job `101391409387`. At this recovery snapshot its main `manifest-rank12 full-z MP stage` is still in progress. Do not duplicate it. Raw-consume fail-closed only after completion and artifact upload.

## New stencil-sensitivity map

For each central4 mixed derivative, `c=(1/12,-2/3,+2/3,-1/12)` and `W_ij=c_i c_j`; total absolute stencil weight is `9/4`.

Occurrence coverage `16/32=50%` is not derivative-sensitivity coverage. Raw-certified BASE ranks `0..11` already carry exactly `17/18=94.444444%` of BASE absolute stencil weight. By contrast, the only currently certified HALF coordinates are shared-corner ranks `5,6,9,10`, carrying only `1/81=1.234568%` of HALF absolute stencil weight. HALF inner-inner ranks `19,20,23,24` together carry `64/81=79.012346%` of HALF absolute stencil weight and remain untested. This is diagnostic only and does not authorize source reordering.

## Rank-10 part-2 provenance correction

Historical raw-consumption records for artifact `9959560285` stored artifact digest `sha256:84509a60d16e660e52c7873261694249e1167f1d95d6a34bd5e91e4026199c54`. A fresh fail-closed diagnostic redownloaded the exact artifact from run `33932061794` and established:

- GitHub metadata digest: `sha256:ac18e784e54414c89e08830d917679ffe0403028abc5ecf6e4e2cdd289158909`;
- independent REST downloaded ZIP SHA-256: the same `sha256:ac18e...`;
- redownloaded `result.json` SHA-256: `2467e807b8b5f1c8a93a83a1e5be2107d2c5ae3d8747bb2f5f586b16501d1c03`, exactly equal to the historical scientific JSON SHA.

Therefore the old artifact-digest field is stale/incorrect, while the scientific payload is unchanged. Correction overlay: `candidate_gravity/results/post482_rank10_part2_provenance_correction.json`. Historical payloads are not rewritten.

## Direct BASE-Q11 raw quartet

The four already-certified shared coordinates ranks `5,6,9,10` form the complete BASE inner-inner quartet. Using exact Actions raw artifacts and the corrected rank-10 part-2 artifact digest, a collision-safe workflow assembled all 80 common `(z,phi)` rows at MP80 and MP120:

`Q11_sample = (4/9)/BASE_H^2 * (F_rank5 - F_rank6 - F_rank9 + F_rank10)`.

Result: `PASS_BASE_Q11_RAW_SAMPLE_LAYER_MP80_MP120__NON_PROMOTING`.

Observed:

- sample count: `80`;
- maximum scaled MP80↔MP120 discrepancy: `1.013005112755547897451223474824036399342e-69`;
- maximum quartet cancellation condition proxy: `9.7696380503509034e10`;
- minimum absolute raw quartet numerator at MP120: `5.4213945288064483e-16`.

Despite nearly `1e11` cancellation conditioning, MP80/MP120 agreement remains about 63 orders of magnitude below the retained assembled comparison scale `2e-6`. The conditioning magnitude is consistent with loss of roughly eleven decimal digits from an 80-digit calculation, leaving far more precision than needed at this raw sample layer.

This materially weakens the hypothesis that the Iteration-421 `~2e-5` blocker is caused by arithmetic cancellation in the dominant BASE inner-inner raw sample quartet. The unresolved mechanism is pushed downstream toward full `F(u,v)` assembly, BASE/HALF mass-step consistency, or extrapolation/representation closure. This remains non-promoting because the raw sample quartet is not the full spectral/azimuth/z assembled `F(u,v)` derivative.

## Next scientific order

1. Continue the already-running rank-12 gate; do not duplicate it.
2. If rank 12 raw-consumes PASS, advance only to frozen rank 13 `(u,v)=(+1e-5,-5e-6)`.
3. Retain exact source order through rank 27; no symmetry shortcuts.
4. After all 28 distinct coordinates are locally raw-certified, perform independent BASE and HALF full-`F(u,v)` MP80/MP120 assemblies and only then compare retained mass-step discrepancy.
5. No physical `D_s`, ANSATZ-003, Fisher/resources, or model-readiness increase before the corresponding frozen gates close.
