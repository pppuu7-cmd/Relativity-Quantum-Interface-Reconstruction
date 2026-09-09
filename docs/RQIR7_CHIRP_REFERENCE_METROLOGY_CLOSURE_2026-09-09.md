# RQIR7 — traceable Raman-chirp reference metrology closure

**Date:** 2026-09-09  
**Code authority:** `analysis/atom_gravimeter_chirp_reference_metrology_audit.py`

## Objective

Replace the earlier mechanical-shaker absolute-reference proxy with an acceleration-equivalent reference generated directly in the Raman frequency-difference chirp. The purpose is to close the strongest remaining Paper-III metrology architecture gate without pretending that an external shaker amplitude is known more accurately than the published apparatus supports.

## Physical relation

For a three-pulse Raman atom gravimeter with Raman difference-frequency chirp `alpha_nu` in Hz/s,

`Delta Phi = (k_eff g - 2 pi alpha_nu) T^2`.

Therefore a programmed differential chirp is equivalent to a known acceleration

`a_ref = 2 pi Delta(alpha_nu) / k_eff`.

This is superior to a mechanically injected absolute acceleration for the present RQIR resource-design purpose because it enters the same interferometer phase channel as acceleration, shares the same `T^2` factor, and does not require the absolute displacement/acceleration transfer of a shaker to be known.

The reference can be encoded shot-by-shot around the nominal gravity-compensation chirp rather than consuming separate calibration blocks.

## Metrology authorities

### Chirp-rate absolute measurement

H.-K. Zhang et al., *A method for the precise and absolute measurement of microwave chirp rates in cold-atom gravimeters*, AIP Advances 15 (2025), DOI `10.1063/5.0252751`, reports an absolute chirp-rate measurement method using commercial frequency/time instruments synchronized to an atomic clock, with measurement precision better than `1 mHz/s`. The same work demonstrates that chirp-rate errors map directly into cold-atom-gravimeter gravity errors.

### DDS stability

The earlier direct DDS study, *Review of Scientific Instruments* 86, 096108 (2015), DOI `10.1063/1.4930562`, reports relative chirp-rate instability `5.7e-11` at 1 s. This is not used to claim absolute accuracy; it is an independent stability authority showing that the programmed chirp itself is not a dominant short-term noise source at the RQIR resource scale.

### Optical wave-vector traceability

BIPM CIPM Recommendation 2 (2015) gives the `87Rb` D2 d/f crossover frequency

`384 227 981.9 MHz`

with estimated relative standard uncertainty `5e-10`. This anchors the optical scale used here to construct `k_eff ~= 4 pi/lambda` for counter-propagating Raman beams. The exact experimental Raman detuning/locking implementation must remain part of the final apparatus provenance, but this optical-scale uncertainty is negligible compared with the conservative differential-chirp term used below.

## Critical differential-metrology correction

The published `<1 mHz/s` chirp result applies to absolute measurement of the **full gravimeter chirp**, near `25.1 MHz/s`. The RQIR calibration signal is instead a small difference between two settings: a `1 micro-g` acceleration-equivalent reference requires only about `25.1373 Hz/s` of differential chirp.

It would therefore be incorrect to divide `1 mHz/s` by `25 MHz/s` and assign that tiny fractional uncertainty to the `25 Hz/s` reference difference.

The audit instead assigns a deliberately conservative

`u[Delta chirp] = 2 mHz/s`

directly to the differential chirp, allowing approximately `1 mHz/s`-class measurement of two settings plus margin.

This gives

`f_ref = 2 mHz/s / 25.1373 Hz/s = 7.956e-5`

or approximately

**`0.00796%` fractional reference uncertainty**.

Including the BIPM optical-scale uncertainty in quadrature leaves the result unchanged at the displayed precision.

## Numerical consequences

Using the BIPM Rb D2 anchor:

- `lambda ~= 780.2462916 nm`;
- `k_eff ~= 1.61056e7 1/m`;
- nominal gravity compensation chirp `~= 25.1373 MHz/s`;
- `1 micro-g` differential reference chirp `~= 25.1373 Hz/s`;
- conservative differential reference uncertainty `~= 7.956e-5 = 0.00796%`.

Compared with the earlier mechanical/seismometer proxy `f_ref ~= 1.0646%`, the chirp-reference architecture improves the absolute-reference uncertainty by approximately **134x**.

## Resource consequence

The earlier campaign design reserved six 30-s mechanical calibration blocks in a one-hour run, leaving `3420 s` science time and giving approximately `0.766 ng` statistical uncertainty.

A shot-coded chirp reference does not require those dedicated blocks. Scaling the already validated detector-facing physical-covariance forecast to the full `3600 s` science exposure gives

**`sigma_stat(1 h) ~= 0.747 ng`**.

For the conservative chirp-reference uncertainty:

- calibration floor at `theta=100 ng`: `~0.00796 ng`;
- calibration floor at `theta=1000 ng`: `~0.0796 ng`;
- statistical/calibration crossover: `theta_cross ~= 9.38e3 ng ~= 9.38 micro-g`.

Thus at the sub-micro-g science amplitudes relevant to the present RQIR resource examples, the absolute-reference term becomes negligible compared with the measured physical noise budget.

## Failure domain

This PASS has strict boundaries:

1. the differential chirp must be independently traceable to calibrated frequency/time standards at the assumed level;
2. the mapping from the programmed DDS/microwave chirp to the actual Raman difference-frequency chirp must be verified for the chosen hardware architecture;
3. `k_eff` must be bound to the actual Raman optical frequencies/directions used by the apparatus rather than only to a generic 780-nm value;
4. an unmeasured or merely commanded chirp value must **not** be treated as certified metrology;
5. historical SYRTE 2008 raw chirp records are not claimed to exist in the repository.

The 2025 chirp-metrology result is therefore a **transferable metrology authority for the experiment design**, not evidence that the historical 2008 dataset itself already contains this calibration.

## Decision

**TRACEABLE ABSOLUTE REFERENCE-METROLOGY ARCHITECTURE: PASS.**

**HISTORICAL SAME-APPARATUS REALIZATION CERTIFICATE: NOT CLAIMED.**

This is sufficient to remove the earlier 1% mechanical proxy as the limiting resource assumption for a Paper-III design/forecast. It does not by itself provide raw matched-campaign provenance.

## Readiness consequence

Paper III was `80%` after the mechanical end-to-end campaign ledger. The new chirp-reference construction closes the largest remaining *architecture-level* absolute-metrology blocker and also removes the 5% calibration-time penalty.

A conservative strengthened Paper-III readiness is therefore promoted to **88%**.

It is not promoted to 100% because three repository-level closure gates remain:

1. matched campaign/provenance certificate tying the chosen physical PSD, detector/contrast model, Raman/chirp mapping and reference authority into one explicit compatibility graph;
2. independent clean deterministic reproduction of the complete Paper-III chain;
3. final article-facing certificate/manifest/figures/tables/failure-domain package.

When these three gates pass, Paper III can be labelled `100% scientific material`; Papers I and II are already at that level, so the repository will then be `100% scientifically ready for Papers I–III` collectively.
