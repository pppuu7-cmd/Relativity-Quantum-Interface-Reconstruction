# RQIR Iteration 100 — Single-Platform Cross-Spectral Apparatus Audit

**Date:** 2026-08-30  
**Status:** Paper-III external apparatus-certificate audit; partial positive closure plus explicit remaining cuts. Not a hardware forecast and not a new-physics claim.

## 1. Purpose

Iteration 099 formalized the primitive apparatus certificate and showed that the absolute Toy009/Toy014 NG-030 decision is data-underdetermined rather than algebra-underdetermined. The next admissible gate is therefore to populate that certificate with the strongest information available from **one experimental platform**, without stitching best-in-class numbers across unrelated experiments (NG-040).

This iteration audits Gosling, Pontin, Iacoponi, Barker and Monteiro, *Physical Review Research* **6**, 013129 (published 31 January 2024), DOI `10.1103/PhysRevResearch.6.013129`, "Sensing directional noise baths in levitated optomechanics".

Primary public sources:

- APS article: `https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.6.013129`
- public manuscript mirror indexed by CNR/IRIS: `https://iris.cnr.it/bitstream/20.500.14243/536721/1/PhysRevResearch.6.013129.pdf`

The paper is used only as an apparatus-method anchor. It does not implement RQIR.

## 2. What this one platform actually demonstrates

The experiment traps a single silica nanoparticle, cools all three center-of-mass directions and detects orthogonal in-plane motion. A deliberately applied directional stochastic Coulomb force is used to create correlated force components.

The same experiment measures

- ordinary displacement PSDs `S_xx(omega)` and `S_yy(omega)`;
- the displacement cross-correlation spectrum `S_xy(omega)`;
- a force-domain susceptibility relation connecting the measured cross-spectrum to a directional force spectrum;
- a calibrated force-orientation extraction.

The published model contains

`S_xx(omega) ~= |chi_x(omega)|^2 S_ff^th [1+beta^2 cos^2 Psi]`,

`S_yy(omega) ~= |chi_y(omega)|^2 S_ff^th [1+beta^2 sin^2 Psi]`,

`S_xy(omega) ~= Re[chi_x^*(omega) chi_y(omega)] S_ff^th beta^2 cos Psi sin Psi`.

The paper explicitly discusses force sensing through both PSD and cross-correlation spectra and shows that the cross-correlation can isolate the directed stochastic component. It also emphasizes that imprecision noise and the susceptibility gain limit useful frequency bands.

This is stronger for RQIR than a paper quoting only one scalar ASD: a non-diagonal spectral likelihood is experimentally measurable in one levitated platform.

## 3. RQIR-APP-004 — a same-platform cross-spectrum is a real apparatus primitive

A same-platform measured spectral matrix

`S(omega) = [[S_xx,S_xy],[S_yx,S_yy]]`

with calibrated susceptibility is a valid primitive from which an ordinary correlation coefficient

`rho(omega)=S_xy/sqrt(S_xx S_yy)`

can be constructed when the entries refer to the same physical coordinate convention, acquisition window and stationary likelihood.

This closes an important *methodological* part of APP-003: off-diagonal spectral covariance need not be assumed or synthesized from separate papers.

It also supports NG-036/NG-037 operationally: the cross term is measurable and can materially change the profiled two-channel Fisher rate.

## 4. Critical coordinate mismatch: spatial x-y covariance is not automatically RQIR f,2f covariance

RQIR D2 currently requires the spectral matrix for two **temporal science harmonics** in an exact factor-two relation, conventionally `f` and `2f`, after mapping them into one input-referred force coordinate.

The Gosling platform instead demonstrates a spectral matrix across two spatial mechanical coordinates `x` and `y` at the same Fourier frequency variable. Its cross-spectrum has gain

`Re[chi_x^* chi_y]`.

Therefore the experimentally measured `S_xy` cannot simply be renamed the RQIR `f,2f` cross-PSD.

A valid RQIR insertion still requires an explicit physical map proving that the two retained temporal harmonics are read out in a common force basis with known transfer functions/windows and with a corresponding two-band cross-covariance.

### RQIR-NG-053 — channel covariance is coordinate-specific

> A measured off-diagonal spectral covariance in one channel basis does not determine the off-diagonal covariance required in another channel basis unless the transfer map, normalization and acquisition likelihood between those bases are explicitly supplied.

This is the cross-spectral analogue of NG-040. It prevents a real `x-y` covariance measurement from being over-credited as a complete `f,2f` science likelihood.

## 5. APP-003 certificate status after this audit

For this single platform:

| primitive cut | status | reason |
|---|---|---|
| same-platform PSD + cross-spectrum capability | **CLOSED** | measured `S_xx,S_yy,S_xy` in one levitated experiment |
| force-domain susceptibility/calibration relation | **PARTIAL** | calibrated directional-force relation exists, but not in the RQIR source-force normalization |
| exact temporal `f,2f` input-referred force matrix | **OPEN** | published `x-y` spectral matrix is a different coordinate structure |
| seven RQIR calibration Fisher blocks/rates | **OPEN** | not supplied for the seven source/calibration layers |
| Toy009/Toy014 source-preparation metrology | **OPEN** | no RQIR hidden-amplitude Ramsey/pointer preparation throughput |
| campaign duty/control/characterization-rate envelope | **OPEN** | no joint RQIR timing/additive/gain recertification certificate |

Hence Iteration 100 improves the experimental grounding of the spectral-matrix requirement but does **not** close RESOURCE-045 or NG-030.

## 6. Relation to shot noise and integration time

The cited experiment explicitly treats finite integration as a spectral-estimation resource: force-spectrum fluctuations decrease with increasing number of independent averaged blocks, and the manuscript gives an illustrative block duration `T_b=3.3 ms` in its force-sensing discussion.

For RQIR this supports the physical interpretation already used in Iterations 084–089:

- spectral-matrix uncertainty is shot/block-count limited before systematic floors;
- longer integration can reduce white statistical uncertainty;
- imprecision and susceptibility determine the useful bandwidth;
- a floor or coordinate mismatch cannot be repaired merely by more blocks.

No RQIR `R_beta` is inferred from the `3.3 ms` block value because the RQIR force template, temporal `f,2f` mapping and nuisance columns are not the same likelihood.

## 7. New engineering requirement

The nearest useful apparatus measurement is now more specific than "measure a cross-PSD":

1. inject or calibrate two force tones/templates at `f` and `2f` in the **same source-force coordinate**;
2. measure the complex transfer function at both bands;
3. estimate the joint spectral covariance/cross-PSD of the two demodulated band estimators with one acquisition convention;
4. propagate that same transduction through the seven calibration-layer Fisher blocks;
5. only then combine source preparation/reset/visibility and duty through the Iteration-099 certificate.

This would directly supply `R0,a2,a4,rho` rather than merely demonstrating generic multimode covariance capability.

## 8. Scientific decision

The single-platform literature audit has produced a **partial positive apparatus result**:

- full/off-diagonal spectral information is experimentally accessible in a levitated force-sensing platform;
- calibrated force-domain cross-spectral inference is experimentally real;
- therefore RQIR's full spectral-matrix requirement is not merely formal.

But it also gives a new guardrail:

- spatial multimode covariance cannot be substituted for temporal `f,2f` covariance without an explicit transfer map.

The absolute Toy009/Toy014 winner remains unresolved. Toy015 remains unjustified because the current missing cuts are still primarily detector/calibration/source-throughput certificate cuts rather than a demonstrated source-geometry bottleneck.

## 9. Reproducibility

Run

`python analysis/single_platform_cross_spectral_audit_iteration100.py`.

The script checks the force cross-spectrum susceptibility factor, spectral-matrix positivity/correlation normalization, the conditional RQIR two-band Fisher law, and the APP-003 closure matrix.

## 10. Next admissible gate

Search the same experimental family and its linked data/method papers for an explicit **tunable two-frequency transfer calibration** or raw/public spectral data from which a common `f,2f` force-coordinate matrix can be reconstructed. If no such same-platform dataset exists, stop the literature substitution route and derive the minimum injected-calibration protocol and required block counts/uncertainty targets needed to close the `R0,a2,a4,rho` cut experimentally.
