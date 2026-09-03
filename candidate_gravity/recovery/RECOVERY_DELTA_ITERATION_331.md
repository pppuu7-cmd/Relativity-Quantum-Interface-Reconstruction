# RQIR Candidate Gravity — Recovery Delta Iteration 331

Date: 2026-09-03

## Authoritative result

`PASS_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION_V2_CLOSED_TARGET_EXCLUDED_FROM_NONZERO_PROPER_SUBINDEX_CHECK`

Validated run `33742866100`, job `100608562495`, artifact `9888424625`, artifact digest `sha256:ab86eeeb40dcf4d1e0f9d6529e7560147c1ca83a0da9cb33da1247ad02027f28`, scientific JSON SHA-256 `813b7a770d8bcdd9b90b29bfe1027e92e20f23cf13ad3d0b844381faae1c7c29`.

The raw artifact was inspected after completion. Sentinel/schema and scientific enforcement passed. Maximum held-out transformed-numerator reconstruction error is `1.3877787807814457e-17`; maximum denominator-map error is `1.1102230246251565e-16`.

## Preserved negative predecessor

Iteration 330 remains a scoped gate-design FAIL, not rewritten into a PASS. Its only failing assertion incorrectly demanded nonzero Fourier momentum for `TARGET=(1,1,1)`, even though the frozen physical trace is exactly closed with `q1+q2+q3=0`. Proper nonzero subindices remain nonzero. The physical route maps and held-out reconstruction in 330 had already passed; Iteration 331 changes only that logically incorrect meta-assertion and keeps parent dynamics, topology weights, loop maps, threshold `5e-10`, and held-out points unchanged.

## What is now frozen

The physical common-background cubic determinant integrand is canonicalized into:

- one singleton family, classified as scoped scaleless/local DR-zero-cut topology;
- three canonical bubble families, cut-capable topology only;
- one signed-affine triangle integration family, with route-specific transported numerators retained and validated.

Denominator equivalence is not used as numerator equivalence; transformed route-specific numerators were explicitly reconstructed and held-out validated.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 329: `0 pp`. A substantial determinant prerequisite closes, but no robust comparator-subtracted residual or complete readiness bucket closes.

## Exact next gate

Iteration 332: perform a scoped DR/direct-timelike discontinuity reduction of the three canonical bubble families and the signed-affine triangle family from Iteration 331. Certify each family as zero/nonzero/BLOCKED at the actual discontinuity level, retain the Iteration-297 evanescent/regulator warning for full finite DR claims, and classify pole/cut origin before any matched Source/Born subtraction.

No `ANSATZ-003`, Fisher/resources, threshold weakening, zero-fill, Source/Born subtraction, or blind heavy full-C5.
