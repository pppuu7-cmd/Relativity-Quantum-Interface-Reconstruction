# RQIR7 — Paper III end-to-end campaign certificate (proxy-metrology edition)

**Date:** 2026-09-09  
**Code authority:** `analysis/atom_gravimeter_end_to_end_campaign_certificate.py`

## Purpose

Consolidate the strengthened Paper-III chain into one campaign-level protocol and resource ledger rather than treating reference calibration, detector likelihood, physical covariance and duty cycle as separate idealized gates.

## Frozen experimentally realizable protocol

The calibration protocol is anchored to the procedure reported by Le Gouet et al. (Applied Physics B 92, 133-144, 2008; arXiv:0801.1270): the isolation platform is deliberately oscillated at selected frequencies while atomic and seismometer signals are recorded simultaneously, and the transfer function is inferred from their modulation-amplitude ratio and phase difference.

For the RQIR campaign ledger we freeze:

- wall-clock campaign: `3600 s`;
- calibration cadence: one block every `600 s`;
- calibration-block duration: `30 s`;
- reference acceleration amplitude: `1 micro-g`;
- six calibration blocks per hour;
- calibration time: `180 s`;
- science time: `3420 s`;
- science duty fraction: **0.95**.

This is a design protocol, not a claim that the source publication ran this exact cadence.

## Source-grounded reference uncertainty proxy

The same source reports a typical corrected sensitivity around `2e-8 g at 1 s`. For a `1 micro-g` calibration excitation, a 30-s block therefore gives an approximate statistical relative amplitude uncertainty

`f_stat = 2e-8 / (1e-6 sqrt(30)) = 0.365%`.

The paper also reports that the low-frequency scale-factor difference between two nominally identical seismometers was below 1%. We use **1% only as a conservative source-grounded proxy systematic floor**, not as a certified absolute uncertainty on the proposed injected acceleration.

The resulting campaign reference proxy is

`f_ref = sqrt((1.000%)^2 + (0.365%)^2) = 1.0646%`.

This distinction is critical: the protocol is physically realizable and the uncertainty scale is source-grounded, but Paper III cannot honestly claim full metrological closure until an actual absolute reference-transfer uncertainty is measured or independently certified.

## End-to-end resource result

The preceding detector-facing nonlinear probability-likelihood audit gives approximately `sigma_theta = 1.829 ng` for 600 s under the physical colored covariance. Using the already validated stationary `1/sqrt(time)` law and the explicit 3420-s science exposure yields

`science statistical sigma = 0.7661 ng`.

The full campaign law is then

`sigma_theta^2 = (0.7661 ng)^2 + (theta * 0.0106458)^2`.

Representative values:

| true theta | total sigma_theta |
|---:|---:|
| `1 ng` | `0.7662 ng` |
| `10 ng` | `0.7734 ng` |
| `50 ng` | `0.9329 ng` |
| `100 ng` | `1.3116 ng` |
| `1000 ng` | `10.673 ng` |

The statistical/reference crossover is

`theta_cross = 0.7661 / 0.0106458 = 71.96 ng`.

Thus the frozen campaign is statistics-dominated for small RQIR amplitudes and reference-calibration-dominated for sufficiently large amplitudes, exactly as required by the detector-facing calibration-floor law.

## Cadence cost stress

For the same 30-s calibration block, the one-hour science duty / statistical uncertainty is approximately:

| calibration period | science duty | sigma_stat |
|---:|---:|---:|
| `300 s` | `0.9000` | `0.787 ng` |
| `600 s` | `0.9500` | `0.766 ng` |
| `1800 s` | `0.9833` | `0.753 ng` |
| `3600 s` | `0.9917` | `0.750 ng` |

The reference protocol therefore does not create a serious exposure penalty. The dominant unresolved issue is its absolute metrological authority, not shot accounting.

## Decision

**PROTOCOL + DUTY-CYCLE + CALIBRATION-FLOOR LEDGER: PASS.**

Closed in this iteration:

- physically realizable reference-transfer procedure: PASS at protocol level;
- reference-block resource cost: PASS;
- science/calibration duty ledger: PASS;
- source-grounded statistical reference uncertainty: PASS;
- conservative source-grounded systematic proxy: PASS AS PROXY;
- detector-facing calibration/statistics crossover: PASS;
- end-to-end resource law: PASS.

Still open:

- certified absolute uncertainty of the injected acceleration reference: **OPEN**;
- actual shot-level calibration time series for the proposed campaign: **OPEN**;
- raw/digitized population and contrast evolution for a matched campaign: **OPEN**;
- raw cross-spectral campaign data beyond the coarse published Fig.-8 digitization: **OPEN if obtainable**;
- independent clean reproduction of the complete Paper-III chain and final article-facing manifest: **OPEN**.

## Readiness consequence

Paper III moves conservatively from **74% to 80% strengthened apparatus-specific readiness**. The large remaining 20% is intentionally reserved for real metrological authority, full reproducibility/provenance binding and final end-to-end article-facing certification rather than more toy variants.

The overall RQIR programme/model score should move only slightly, approximately **72% -> 73%**, because Paper IV remains the dominant later-program bottleneck.

## What exactly makes the first three papers 100% repository-ready?

On the current scientific-material scale:

- Paper I: already **100% scientific material**;
- Paper II: already **100% scientific material**;
- Paper III: now **80% strengthened apparatus-specific readiness**.

Therefore the repository becomes **100% scientifically ready for Papers I-III** when Paper III reaches scientific closure. That requires all of the following final gates, not a calendar deadline:

1. **Reference metrology authority** — replace the 1% proxy with a measured/certified absolute amplitude/transfer uncertainty for the realizable calibration protocol.
2. **Matched campaign provenance** — bind the physical PSD/cross-PSD, population/contrast evolution and calibration data to one compatible campaign; if raw data cannot be obtained, document the strongest reproducible source-traceable substitute and its limitations explicitly.
3. **Independent clean reproduction** — rerun the entire Paper-III chain from a clean environment and reproduce the source checks, covariance construction, detector likelihood, calibration floor and resource certificate deterministically.
4. **Final Paper-III artifact package** — freeze figures/tables, manifest, claims/failure-domain table and manuscript-facing results so no decisive scientific statement depends on an untracked notebook/manual calculation.

Only after these gates pass should Paper III, and therefore the repository for the **first three papers collectively**, be labelled **100%**.

If the user instead means *100% journal-submission package readiness*, Paper I and II also retain editorial/submission hardening tasks noted in the strict repository audit; those should be closed after or in parallel with the Paper-III scientific gates rather than being confused with missing science.
