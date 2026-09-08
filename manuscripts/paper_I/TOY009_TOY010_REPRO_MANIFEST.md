# RQIR Paper I — Toy009/Toy010 reproducibility manifest

Date: 2026-09-08
Status: clean-run provenance gate / run pending at manifest creation
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
- Workflow head commit: `763757788397564d180cfd6b33c28db57412d74c`
- Trigger: push to `paper-I-v03-evidence-boundary`
- Runner: GitHub-hosted `ubuntu-latest`
- Python: 3.12, recorded by workflow in artifact
- NumPy: pinned to `2.1.3`
- Artifact name: `paper-i-toy009-toy010-certificate`
- Artifact retention: 90 days

At manifest creation the run status was `in_progress`. After completion this file must be updated with conclusion, artifact ID, file hashes and the exact observed numerical certificate.

## Source files and immutable blob IDs

### Toy009 source certificate

- Path: `analysis/toy009_detector_aware_source_search.py`
- Blob SHA on the paper branch: `6b08730688ca1ebf2d8986528df1603ee6e52b70`
- NP2 exploratory scan seed: `20260829`
- NP3 accepted-source scan seed: `314159`
- Expected accepted NP3 trial: `811`
- NP3 numerical rank threshold: `1e-10`
- Pair amplitude: `EPS = 0.08`
- Regression requirements include:
  - rank-24 codimension-one calibration construction;
  - exact accepted trial `811`;
  - calibration residual `< 1e-12`;
  - target mean difference `< 1e-12`;
  - target centered-noise difference `< 1e-12`;
  - non-degraded response-survival and normalized smallest singular value;
  - positive `rho+` and `rho-` enforced before acceptance.

### Toy010 calibration-steering certificate

- Path: `analysis/toy010_calibration_geometry_optimization.py`
- Blob SHA on the paper branch: `76d16b4b2da847a19f57a49a4dc08fe6ea1f3447`
- Fixed source: exactly the accepted Toy009 source reconstructed from seed `314159`, trial `811`
- Broad calibration-search seed: `2026082903`
- Refinement seed: `2026082904`
- Default clean run: verification of the already accepted Toy010 geometry; it does not rerun the 50,000-point search
- Numerical rank threshold: `1e-10`
- Regression requirements include:
  - `rank(A) = 24` in a 25-dimensional Hermitian parameterization;
  - maximum equality residual `< 1e-12`;
  - positive paired density matrices;
  - target mean equality within `1e-12`;
  - centered target-noise equality within `1e-12`;
  - detector-source D1 and D2 information strictly above Toy009;
  - response-survival `eta` strictly above Toy009;
  - normalized `smin` strictly above Toy009;
  - `eta = 0.60017429` within `2e-7`;
  - `smin = 0.002211009` within `2e-9`;
  - `S_eff(D1) = 2.8310544e-4` within `2e-10`;
  - `S_eff(D2) = 5.4370610e-4` within `2e-10`.

## Historical lineage

The clean run is not the first appearance of these constructions. It independently re-executes code whose provenance is traceable in repository history:

- `4e77c62fc3fe5e4a641316ca75423b7b4158400f` — Toy009 joint calibration geometry verification and scan;
- `039d6cf192007e1f8fe908e873d41bfe0149c174` — Toy009 calibration-geometry documentation;
- `191ddc907c382b565a9396bcbdc38a28c6a4eb45` — Toy010 calibration geometry optimizer and verifier;
- `4a218c3e48e033c1f80dada2b49df05ad4ace229` — Toy010 calibration-geometry documentation;
- `74ca697561c9446874abb5e5232aa6d93f099e01` — later exact Toy009/Toy014 calibration-span audit.

The Paper-I authority should be the clean workflow run at the paper-branch commit, while the older commits remain provenance/history rather than the sole evidence.

## Evidence promotion rule

C3–C5 may be promoted to GREEN only if the clean workflow concludes successfully and its artifact contains all of the following:

1. `commit_sha.txt` matching the workflow head commit;
2. `python_version.txt`;
3. `numpy_version.txt` equal to `2.1.3`;
4. `platform.txt`;
5. `toy009_stdout.txt` showing all Toy009 regression assertions completed without exception;
6. `toy010_stdout.txt` showing all Toy010 regression assertions completed without exception;
7. `SHA256SUMS.txt` covering the artifact files.

After promotion, the manuscript may quote frozen numerical diagnostics from the clean run. Machine-specific last digits should still be reported only to scientifically meaningful precision.

## Remaining optional strengthening

A later archival release or long-retention repository result file should copy the final certificate out of the 90-day Actions artifact if Paper I is submitted or posted as a preprint. The journal-facing reproducibility record should not depend permanently on a temporary Actions retention window.
