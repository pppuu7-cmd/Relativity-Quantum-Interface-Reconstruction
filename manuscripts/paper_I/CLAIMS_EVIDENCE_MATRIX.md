# RQIR Paper I — claims/evidence matrix

Date: 2026-09-08
Status: submission control document / post-clean-run

This matrix separates analytic claims, constructive numerical evidence, externally anchored comparisons and explicit non-claims. A claim is publication-ready only when every required evidence field in its row is frozen.

| ID | Claim | Evidence class | Required evidence | Current status | Submission action |
|---|---|---|---|---|---|
| C1 | A finite calibration map with a physical one-dimensional null direction `n` and `c(n) != 0` admits positive calibration-equivalent but response-distinct nearby states under the stated interior/linearity hypotheses. | Analytic | Explicit hypotheses; positivity argument; proof. | GREEN | Keep theorem narrow; no numerical dependence. |
| C2 | Matching declared mean/noise calibration coordinates need not determine an ordered response coordinate absent an additional physical identity. | Analytic/structural | CTP/Kubo/stochastic-gravity positioning; explicit conditional wording. | GREEN | Preserve non-novelty statement for established mean/noise/response decomposition. |
| C3 | The RQIR toy construction realizes a codimension-one calibration nullspace with a physical hidden direction. | Constructive numerical | Exact code revision; configuration; numerical-rank rule; rank/conditioning diagnostic; clean rerun artifact. | GREEN | Clean run `34177686395`, artifact `10037815979`; retain stable archival copy before submission. |
| C4 | The paired toy states remain physical and calibration-equivalent. | Constructive numerical | Positivity diagnostics; preparation constraints; calibration residuals; same frozen run as C3. | GREEN | Toy009/Toy010 positivity and equality diagnostics independently reproduced in the clean run. |
| C5 | The ordered/detector-aware response differs on the same hidden direction. | Constructive numerical | Response definition; detector transfer definition; value on frozen hidden direction; same frozen run as C3/C4. | GREEN | Opposite nonzero ordered responses and detector-facing D1/D2 coordinates independently reproduced. |
| C6 | Calibration geometry can rotate the hidden direction according to the stated perturbative steering relation in its declared setting. | Analytic + constructive | Local constant-rank derivation; normalized null-vector gauge; pseudoinverse/conditioning assumptions; optional constructive rotation. | GREEN | Analytic derivation is in v0.4; Toy010 clean run gives a `37.714 deg` concrete null-direction rotation on a fixed source. |
| C7 | Recent gravity-quantumness witness interpretations are comparator-class dependent. | Literature positioning | Current primary literature representing competing positions; neutral wording. | GREEN | Keep Aziz–Howl and Feng–Vedral–Marletto together; Tang et al. may remain only as explicitly non-peer-reviewed context. |
| C8 | Quantum clocks are among relevant gravity–quantum laboratory architectures. | Literature positioning | Canonical clock-interferometry reference plus optional current post-Newtonian comparator. | GREEN | Roura 2020 and Wakakuwa 2026 are now cited. |
| C9 | Any externally calibrated numerical target/comparison used in Paper I is authoritative. | External numerical | Source authority; convention; extraction rule; version/date; run provenance. | RED until instantiated | Do not promote any external comparison number before authority binding. The internal Toy009/Toy010 certificate is not an external calibration claim. |
| C10 | The Paper-I novelty is the conjunction of physical source calibration quotient, positivity-preserving response-distinct pair, separate ordered-response discriminant, constructive detector-facing realization and calibration steering. | Novelty | Targeted prior-art search across incomplete tomography, positivity, retarded-response kernels and calibration/nuisance quotient geometry. | AMBER-GREEN | Targeted audit found close neighbors but no exact conjunction; retain narrow wording and perform final scholarly-database sweep before submission. |

## Frozen constructive certificate

Clean workflow run `34177686395` at commit `763757788397564d180cfd6b33c28db57412d74c` completed successfully under Python `3.12.14` and NumPy `2.1.3`. Artifact `10037815979` (`paper-i-toy009-toy010-certificate`) has digest `sha256:6363cfe9f5fad3ad7d04363921cc6d66e051ce7beaf9e22a3940a1b38c654b95`.

The full numerical authority record is frozen in `TOY009_TOY010_REPRO_MANIFEST.md`.

## Non-claims that must remain explicit

- No empirical evidence for quantized geometry is claimed.
- No claim is made that gravity necessarily couples to `D` or `chi^R`.
- No claim is made that the mean/noise/response decomposition is new.
- No claim is made that finite-measurement incompleteness, positivity-constrained tomography or nullspaces are new.
- No claim is made that kernels/invertibility of retarded response functions are new.
- No claim is made that quotient geometry for calibration or nuisance uncertainty is new.
- No claim is made that the finite toy models are relativistically complete.
- No claim is made that exact source separation implies detector-level identifiability after nuisance profiling.
- No claim is made that Paper I selects a unique microscopic theory of gravity.

## Immediate critical path

1. Promote rounded clean-run Toy009/Toy010 diagnostics into `main.tex` with stable provenance wording.
2. Copy the 90-day Actions certificate into a long-retention repository result/archival record before preprint or journal submission.
3. Perform the final database-oriented novelty sweep for C10 while preserving the conjunctive claim.
4. Run manuscript compilation/reference audit and resolve any BibTeX/LaTeX issues.
5. Produce the planned figures/tables from the frozen analytic/numerical claims.
6. Fix author metadata and journal-specific formatting only after the scientific/submission evidence layer is frozen.
