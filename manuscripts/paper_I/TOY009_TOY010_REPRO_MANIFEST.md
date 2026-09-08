# RQIR Paper I — Toy009/Toy010 reproducibility manifest

Date: 2026-09-08
Status: VERIFIED clean-run certificate
Paper branch: `paper-I-v03-evidence-boundary`

## Purpose

This manifest binds the constructive numerical evidence used by Paper I to exact repository code and an independent GitHub Actions rerun. It is intentionally separate from the analytic proof of RQIR-THM-001.

The constructive evidence addresses claims C3–C5 in `CLAIMS_EVIDENCE_MATRIX.md`:

- C3: codimension-one calibration nullspace with a physical hidden direction;
- C4: positive calibration-equivalent paired states with matched declared mean/noise coordinates;
- C5: nonzero ordered response and detector-aware response on that same hidden direction.

## Clean-run authority

- Workflow: `.github/workflows/paper-i-toy009-toy010-verification.yml`
- Workflow run ID: `34177686395`
- Workflow conclusion: `success`
- Workflow head commit: `763757788397564d180cfd6b33c28db57412d74c`
- Trigger: push to `paper-I-v03-evidence-boundary`
- Job ID: `101910259909`
- Runner: GitHub-hosted Ubuntu 24.04.4 (`ubuntu-24.04` image)
- Python: `3.12.14`
- NumPy: `2.1.3`
- Artifact name: `paper-i-toy009-toy010-certificate`
- Artifact ID: `10037815979`
- Artifact size: 2569 bytes
- Artifact digest: `sha256:6363cfe9f5fad3ad7d04363921cc6d66e051ce7beaf9e22a3940a1b38c654b95`
- Artifact created: `2026-09-08T01:45:23Z`
- Artifact expires: `2026-12-07T01:45:02Z`

All workflow steps completed with conclusion `success`, including both numerical verifier steps, file hashing and artifact upload.

## Source files and immutable blob IDs

### Toy009 source certificate

- Path: `analysis/toy009_detector_aware_source_search.py`
- Blob SHA on the paper branch: `6b08730688ca1ebf2d8986528df1603ee6e52b70`
- NP2 exploratory scan seed: `20260829`
- NP3 accepted-source scan seed: `314159`
- Accepted NP3 trial: `811`
- NP3 numerical rank threshold: `1e-10`
- Pair amplitude: `EPS = 0.08`

### Toy009 clean-run observations

The clean run reproduced:

- NP3 non-degraded candidates: `1`;
- accepted NP3 trial: `811`;
- D1 gain vs Toy007: `1.2218350306685808`;
- D2 gain vs Toy007: `1.4035829922637177`;
- response-survival fraction `eta_R = 0.5688230045520649`;
- normalized `smin = 0.0015122241664651812`;
- condition number `3033.407565001411`;
- source radii `(1.0, 1.60090005, 1.77911036, 2.60900799, 5.90723562)`;
- `eig(rho+) = (0.12, 0.1729648, 0.19540869, 0.24623746, 0.26538905)`;
- `eig(rho-) = (0.13461095, 0.15376254, 0.20459131, 0.2270352, 0.28)`;
- maximum equality residual `2.220446049250313e-16`;
- target mean difference `8.673617379884035e-19`;
- target centered-noise difference `1.734723475976807e-18`;
- ordered responses `D+ = -0.012084964253358131`, `D- = +0.012084964253358133`.

Thus the clean run independently reproduced codimension-one calibration behavior, positive paired states, calibration equality at floating-point precision and a nonzero opposite ordered-response split.

### Toy010 calibration-steering certificate

- Path: `analysis/toy010_calibration_geometry_optimization.py`
- Blob SHA on the paper branch: `76d16b4b2da847a19f57a49a4dc08fe6ea1f3447`
- Fixed source: exactly the accepted Toy009 source reconstructed from seed `314159`, trial `811`
- Broad calibration-search seed: `2026082903`
- Refinement seed: `2026082904`
- Default clean run: verification of the already accepted Toy010 geometry; it does not rerun the 50,000-point search
- Numerical rank threshold: `1e-10`

### Toy010 clean-run observations

The clean run reproduced:

- `rank(A) = 24` in the 25-dimensional Hermitian parameterization;
- second calibration probe `y1 = -3.764531439702698`;
- calibration times `(0, 2.99076642, 3.58392890, 2.86845279, 4.17773776, 4.88882082, 4.99774842)`;
- D1 gain vs Toy009: `1.6788124819619106`;
- D2 gain vs Toy009: `1.5840571474984675`;
- D1 gain vs Toy007: `2.0512319003847272`;
- D2 gain vs Toy007: `2.2233556710026283`;
- response survival `eta = 0.600174291803509`;
- normalized `smin = 0.002211008959816202`;
- condition number `2084.230664281075`;
- null-vector rotation angle `37.714026817452954 deg`;
- `eig(rho+) = (0.12225859, 0.17604178, 0.18369839, 0.23800124, 0.28)`;
- `eig(rho-) = (0.12, 0.16199876, 0.21630161, 0.22395822, 0.27774141)`;
- maximum equality residual `4.440892098500626e-16`;
- target mean values `0.5478597316180662` and `0.5478597316180662`;
- target centered-noise values `0.01326059175459401` and `0.013260591754594014`;
- ordered responses `D+ = +0.013285909568428681`, `D- = -0.01328590956842869`;
- `S_eff(D1) = 2.8310544e-4` within the frozen regression tolerance;
- `S_eff(D2) = 5.4370610e-4` within the frozen regression tolerance.

This establishes a concrete calibration-steering example on a fixed source: the calibration redesign rotates the one-dimensional null direction by approximately `37.7 deg`, improves conditioning, and changes the surviving ordered/detector-aware response while retaining positivity and declared calibration equality.

## Certificate file hashes

The workflow generated the following SHA-256 records:

- `commit_sha.txt`: `5bf4eb51f698961ad593b65f5a002df626a80c048200ba39b3471ba941d62932`
- `numpy_version.txt`: `eb01a4e8e8922406f15a22cadc3fae28d4f513afe11b4734788eb2ea73cf034e`
- `platform.txt`: `45e9d6c8002853d2f9d6fb7bd22261836b1d8e49400cf2a020e33567755cc387`
- `python_version.txt`: `4c3569f5da09975434dd9fd9a91fadbc4367a91d8f3c3fab59e9241ab9ee4bd8`
- `toy009_stdout.txt`: `8e6d39b9c96c0096f97d56dbca1e33e1aab179a670f074a72fd0e5255ad701bc`
- `toy010_stdout.txt`: `f74cce97f6c9014895f09792415d981b5be947938649a7cdf7032bbab4d43cec`

## Historical lineage

The clean run is not the first appearance of these constructions. It independently re-executes code whose provenance is traceable in repository history:

- `4e77c62fc3fe5e4a641316ca75423b7b4158400f` — Toy009 joint calibration geometry verification and scan;
- `039d6cf192007e1f8fe908e873d41bfe0149c174` — Toy009 calibration-geometry documentation;
- `191ddc907c382b565a9396bcbdc38a28c6a4eb45` — Toy010 calibration geometry optimizer and verifier;
- `4a218c3e48e033c1f80dada2b49df05ad4ace229` — Toy010 calibration-geometry documentation;
- `74ca697561c9446874abb5e5232aa6d93f099e01` — later exact Toy009/Toy014 calibration-span audit.

The Paper-I numerical authority is the successful clean workflow run at the paper-branch commit; the older commits provide provenance/history and independent regression lineage.

## Evidence promotion decision

The promotion requirements are satisfied:

1. clean workflow conclusion is `success`;
2. `commit_sha.txt` matches the workflow head commit;
3. Python and NumPy versions are recorded, with NumPy pinned to `2.1.3`;
4. both verifier scripts completed without exceptions;
5. artifact file hashes were generated;
6. the complete certificate artifact was uploaded successfully.

**Decision: C3, C4 and C5 are promotable to GREEN.**

The manuscript may now quote the frozen diagnostics above. Machine-specific last digits should still be rounded to scientifically meaningful precision in the journal text.

## Remaining strengthening before submission

The current Actions artifact expires after 90 days. Before preprint or journal submission, copy the final certificate into a long-retention repository result file or archival release. The manuscript should cite the stable repository path/commit rather than depending permanently on the temporary Actions artifact URL.
