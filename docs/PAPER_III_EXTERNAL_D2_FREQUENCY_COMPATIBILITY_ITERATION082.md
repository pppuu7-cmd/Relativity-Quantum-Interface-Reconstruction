# RQIR Iteration 082 — External D2 Apparatus Frequency-Compatibility Gate

**Date:** 2026-08-30  
**Status:** externally anchored Paper-III feasibility gate; negative/conditional result, not an apparatus forecast and not a new-physics claim.

## 1. Question

Can a published record-class levitated-force sensitivity be inserted directly into the current RQIR D2 two-band Fisher model and thereby close the absolute detector-rate normalization left open by Iteration 081?

**No, not without an additional frequency-transfer/PSD model.**

The reason is structural rather than merely numerical: the current RQIR discriminator deliberately requires usable information in two separated source harmonics (`n=2` and `n=4`), while the externally anchored force sensitivity is reported for a narrow mechanical resonance near `193.8 kHz`.

## 2. External apparatus anchor

Liang et al., *Fundamental Research* **3**, 57–62 (2023), DOI `10.1016/j.fmre.2022.09.021`, report an optically levitated silica-nanosphere force sensor with:

- nominal nanoparticle diameter around `150 nm`; one reported high-vacuum particle diameter `142.60 +/- 5.54 nm`;
- natural resonance around `193.8 kHz` for a reported particle/run;
- feedback-cooled damping rate `19.60 +/- 6.54 Hz` at `7.9e-9 mbar` in the cited high-vacuum data;
- force sensitivity `6.33 +/- 1.62 zN/sqrt(Hz)` and a best single measured sensitivity `4.34 zN/sqrt(Hz)`;
- Allan-optimal stability time about `2751 s`;
- stable force resolution `166.40 +/- 55.48 yN` at that time.

These numbers are experimental detector anchors. They are **not** RQIR source parameters and do not establish sensitivity at arbitrary frequencies.

The 2026 Kamba et al. levitated nano-accelerometer independently demonstrates that quantum/quench techniques can improve acceleration readout by about two orders of magnitude, but its publication likewise does not supply the full RQIR two-band matrix PSD/calibration likelihood required by RQIR-APP-001.

## 3. Current RQIR two-band requirement

The mature D2 detector likelihood retains source harmonics

`f_2 = 2 f_gap`,

`f_4 = 4 f_gap`,

because profiling the free relative spectral-tilt nuisance gives

`S_eff = 4 P_2 P_4/(P_2+P_4)`.

Therefore if either whitened band power tends to zero,

`S_eff -> 0`.

A detector normalization measured at only one narrow resonance is insufficient unless the transfer and PSD at the other retained band are also known.

For the late physical source front:

- Toy014 stored `S_eff,014 = 1.6356852494e-4`;
- `S_eff,014/S_eff,009 = 0.28301465746`;
- hence `S_eff,009 = 5.7795071961e-4` under the same equal-ASD source-kernel normalization.

These are source/detector-shape quantities, not an absolute measured force PSD.

## 4. Frequency incompatibility with a single 193.8-kHz resonance

Take the published resonance central value

`f_res = 193.8 kHz`.

### Put RQIR `n=2` on resonance

Then

`f_gap = f_res/2 = 96.9 kHz`,

and the second retained band is

`f_4 = 387.6 kHz`.

Its separation from the measured resonance is `193.8 kHz`.

Using the reported `19.60 Hz` damping rate as a linewidth-scale proxy, the other RQIR band is approximately

`193800/19.60 ~= 9888`

linewidths away.

### Put RQIR `n=4` on resonance

Then

`f_gap = 48.45 kHz`,

and

`f_2 = 96.9 kHz`.

That second band is about

`96900/19.60 ~= 4944`

linewidths away.

The reported fractional linewidth scale is only

`19.60/193800 ~= 1.01e-4`.

Thus the published on-resonance sensitivity cannot be assumed at both RQIR harmonics.

## 5. RQIR-NG-033 — single-resonance two-band incompatibility

> A narrowband detector sensitivity measured at one mechanical resonance cannot, by itself, normalize a two-band RQIR Fisher discriminator whose identifiability requires finite whitened information in both `n=2` and `n=4` bands.

Directly substituting a record on-resonance ASD for both RQIR bands would over-credit detector Fisher and can falsely evade the spectral-tilt degeneracy.

This is independent of how small the quoted ASD is.

## 6. Admissible ways to close the detector layer

At least one of the following is required.

### A. Genuine two-band detector

Provide two mechanical modes or two simultaneous channels with measured

- complex transfer at `2 f_gap` and `4 f_gap`;
- full PSD/cross-PSD at both bands;
- same-time gain/timing calibration and uncertainty.

### B. Broadband force sensor

Demonstrate a calibrated equivalent-force PSD over a bandwidth spanning both retained harmonics, not merely an on-resonance sensitivity.

### C. Sequential retuning

Retune a narrowband sensor between the two RQIR harmonics and write one joint likelihood containing

- separate acquisition times;
- retuning/relock duty;
- gain drift between settings;
- timing/reference drift;
- calibration transfer uncertainty;
- source reproducibility across the two campaigns.

The old simultaneous two-band spectral-tilt formula cannot be imported unchanged if the bands are acquired in separate apparatus configurations.

## 7. Allan-stability consequence

The external apparatus also supplies a valuable real stability boundary:

- white-noise-like force averaging was demonstrated for long runs;
- Allan analysis identified an optimal stability scale around `2751 s`;
- the reported stable force resolution was `166.40 +/- 55.48 yN`.

Therefore Paper III must distinguish at least two detector inputs:

1. short-time/locally stationary PSD entering matched-filter Fisher;
2. long-time stability/recertification model entering duty and campaign segmentation.

This experimentally supports the existing RQIR-NG-007/DRIFT logic: a long-time stability floor cannot be replaced by naive `1/sqrt(T)` extrapolation of the best short-time ASD.

## 8. Consequence for Toy009 versus Toy014

No robust Toy009/Toy014 wall-clock winner can yet be extracted from this single external sensor because the detector source-specific rate ratio depends on the transfer/PSD at **both** harmonics.

The stored same-kernel ratio

`q_s(014/009)=3.53338589945`

remains a valid internal source comparison only under the declared common detector kernel. An actual narrowband apparatus may change that ratio if its transfer/noise weights the two source spectra differently.

Therefore NG-030 robust dominance remains open.

## 9. Scientific decision

Iteration 082 advances Paper III by replacing one generic missing-data statement with a concrete experimentally anchored incompatibility test.

The next admissible apparatus gate is **not** to search for a smaller single-number force ASD. It is to obtain or model a detector with calibrated transfer/noise at both retained RQIR bands, or to derive the correct sequential-retuning likelihood and its drift/calibration cost.

A particularly useful next search is for published dual-mode/broadband levitated sensors with tabulated PSD around two frequencies separated by a factor of two; otherwise construct a parameterized two-mode apparatus envelope around the measured Liang et al. stability data without calling it a forecast.

## 10. External references used for this gate

- T. Liang et al., *Fundamental Research* **3**, 57–62 (2023), DOI `10.1016/j.fmre.2022.09.021`.
- M. Kamba et al., *Phys. Rev. Lett.* **137**, 050801 (2026), DOI `10.1103/js43-kq48`.

## 11. Reproducibility

Run

`python analysis/external_d2_frequency_compatibility_iteration082.py`.

The script verifies the resonance-placement arithmetic, linewidth separations, and stored Toy009/Toy014 `S_eff` relation. It intentionally refuses to convert the published resonance ASD into absolute RQIR hours without a second-band transfer/PSD.
