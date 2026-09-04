# Candidate Gravity Recovery Delta — Iteration 393

Date: 2026-09-04

MODEL_READINESS: 24%

## Authority

Iteration 393 consumes the complete preserved Iteration-381 raw manifest and closes the full 36-channel physical simple-double `Tr U1^2` operator-coordinate sub-sector. No channel is extrapolated or zero-filled.

Freeze:

`PASS_TRU1SQ_SIMPLE_DOUBLE_FULL36_RAW_MANIFEST_ASSEMBLY__ALL_CONVERGED`

Validated Actions provenance:

- run `33820949571`
- workflow head `0bcd6aab9f2e644c9abdef7f7d4640bfa2eceb83`
- artifact `9918228922` (`iteration393-result`)
- artifact digest `sha256:f642776e365eaa0301913c49c17f1e89048f43ce32dc828580164dfae0bbe5a7`
- raw scientific JSON SHA-256 `8eec56bd5d0d48e36c4490407bcc88c9d2ee3d3e59d976a9a0e1ad5f16d86226`
- sentinel/schema authority audit: PASS.

## Exact census

- 36/36 unique channel indices `0..35` present exactly once;
- 12/12 raw chunks accounted for;
- 36/36 channels CONVERGED;
- all frozen threshold checks PASS;
- exactly 12 channels in each distinct q2 bucket.

The q2-resolved normalized simple-double operator coordinate is

- `q^2=-1`: `D_s Tr U1^2 = -0.002329411286740447`;
- `q^2=-0.34`: `D_s Tr U1^2 = -0.0005948791870822445`;
- `q^2=-0.14`: `D_s Tr U1^2 = -7.368142632096214e-05`.

Numerical envelope:

- maximum scaled convergence error `1.2832512405556301e-08`;
- maximum radial Richardson scaled error `9.7822954164134e-15`;
- maximum cut-shell error `1.9796472878401243e-16`;
- minimum sampled uncut denominator `0.1209736845785128`.

The effective-action factor `-i/4` is **not folded** here. Distinct q2 coordinates remain separate.

## Classification boundary

This is a complete physical sub-sector PASS for the simple-double piece of `Tr U1^2`. It is not yet complete `Tr U1^2`, not Candidate Gravity consistency PASS/FAIL, not comparator identity, not non-identifiability, not near-degeneracy, not novelty certificate and not a candidate residual.

## Readiness

MODEL_READINESS: 24%

Change: `0 pp`. A large operator sub-sector is now complete, but the 15 double-double channels still prevent complete `Tr U1^2`; no stable readiness bucket or comparator-subtracted residual closes yet.

## Exact next gate

Consume Iteration 389 only after exactly 15 unique double-double raw channel records are scientifically resolved. Then assemble complete `Tr U1^2` q2-by-q2 as Iteration-374 simple-simple + Iteration-393 simple-double + complete double-double, still without the `-i/4` effective-action weight.
