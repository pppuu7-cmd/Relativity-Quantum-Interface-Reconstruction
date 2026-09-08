# RQIR Paper I — claims/evidence matrix

Date: 2026-09-08
Status: submission control document

This matrix separates analytic claims, constructive numerical evidence, externally anchored comparisons and explicit non-claims. A claim is publication-ready only when every required evidence field in its row is frozen.

| ID | Claim | Evidence class | Required evidence | Current status | Submission action |
|---|---|---|---|---|---|
| C1 | A finite calibration map with a physical one-dimensional null direction `n` and `c(n) != 0` admits positive calibration-equivalent but response-distinct nearby states under the stated interior/linearity hypotheses. | Analytic | Explicit hypotheses; positivity argument; proof. | GREEN | Keep theorem narrow; no numerical dependence. |
| C2 | Matching declared mean/noise calibration coordinates need not determine an ordered response coordinate absent an additional physical identity. | Analytic/structural | CTP/Kubo/stochastic-gravity positioning; explicit conditional wording. | GREEN | Preserve non-novelty statement for established mean/noise/response decomposition. |
| C3 | The RQIR toy construction realizes a codimension-one calibration nullspace with a physical hidden direction. | Constructive numerical | Exact code revision; configuration; numerical-rank rule; singular-value/rank diagnostic; normalized null vector; clean rerun artifact. | AMBER | Bind Toy009/Toy010 to immutable clean-run artifact. |
| C4 | The paired toy states remain physical and calibration-equivalent. | Constructive numerical | Positivity diagnostics; preparation constraints; calibration residuals; same frozen run as C3. | AMBER | Freeze positivity/equality diagnostics in manifest. |
| C5 | The ordered/detector-aware response differs on the same hidden direction. | Constructive numerical | Response definition; detector transfer definition; value on frozen `n`; nonzero decision rule; same frozen run as C3/C4. | AMBER | Freeze response output and decision threshold/policy. |
| C6 | Calibration geometry can rotate the hidden direction according to the stated perturbative steering relation in its declared setting. | Analytic + constructive | Derivation/assumptions of `n'=-A^+A'n`; conditioning assumptions; optional frozen numerical illustration. | AMBER-GREEN | Add a compact derivation or citation/appendix note clarifying gauge/normalization assumptions. |
| C7 | Recent gravity-quantumness witness interpretations are comparator-class dependent. | Literature positioning | Current primary literature representing the competing positions; neutral wording. | GREEN/AMBER | Keep Aziz–Howl and Feng–Vedral–Marletto together; optionally add Tang et al. as explicitly non-peer-reviewed context. |
| C8 | Quantum clocks are among relevant gravity–quantum laboratory architectures. | Literature positioning | Canonical clock-interferometry reference. | AMBER | Add Roura 2020; optionally add Wakakuwa 2026 for current post-Newtonian context. |
| C9 | Any externally calibrated numerical target/comparison used in Paper I is authoritative. | External numerical | Source authority; convention; extraction rule; version/date; run provenance. | RED until instantiated | Do not promote any such number before authority binding. |
| C10 | RQIR-THM-001 or its exact conjunction is novel relative to prior literature. | Novelty | Targeted prior-art search beyond generic tomography/nullspace literature. | AMBER | Complete focused novelty audit and phrase claim as a narrow RQIR-specific conjunction unless stronger priority evidence is found. |

## Non-claims that must remain explicit

- No empirical evidence for quantized geometry is claimed.
- No claim is made that gravity necessarily couples to `D` or `chi^R`.
- No claim is made that the mean/noise/response decomposition is new.
- No claim is made that finite-measurement incompleteness or nullspaces are new linear algebra/quantum tomography.
- No claim is made that the finite toy models are relativistically complete.
- No claim is made that exact source separation implies detector-level identifiability after nuisance profiling.
- No claim is made that Paper I selects a unique microscopic theory of gravity.

## Immediate critical path

1. Freeze a clean Toy009/Toy010 rerun and immutable artifact manifest.
2. Close C3–C5 with the same artifact lineage.
3. Clarify the assumptions behind the calibration-steering derivative for C6.
4. Add Roura 2020 to close C8.
5. Complete the targeted prior-art search for C10.
6. Only then promote exact toy residuals/values into the manuscript and figures.
