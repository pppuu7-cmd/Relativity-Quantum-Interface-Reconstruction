# RQIR Recovery Delta — Iteration 100

**Date:** 2026-08-30  
**Parent front:** Iteration 099.

## What changed

The APP-003 primitive apparatus certificate was populated with a stronger single-platform spectral anchor: Gosling et al., *Phys. Rev. Research* 6, 013129 (2024).

Retain:

- same-platform displacement PSDs and x-y cross-correlation spectra are experimentally measured in a levitated nanoparticle force-sensing setup;
- the experiment provides a susceptibility-based force-domain cross-spectrum relation and calibrated force-direction inference;
- this experimentally validates the feasibility of an off-diagonal spectral likelihood in one platform.

### New labels

- **RQIR-APP-004:** same-platform measured cross-spectral covariance plus calibrated transfer is a legitimate apparatus primitive.
- **RQIR-NG-053:** spectral covariance is coordinate-specific. A measured spatial x-y cross-spectrum is not the RQIR temporal f,2f cross-PSD unless an explicit physical transfer, normalization and acquisition map connects the channel bases.

## Certificate status

Partially improved:

- same-platform PSD/cross-spectrum capability: CLOSED;
- generic force-domain susceptibility/calibration relation: PARTIAL.

Still open:

- exact temporal f,2f input-referred force spectral matrix and `R0,a2,a4,rho`;
- seven same-apparatus RQIR calibration Fisher blocks/rates;
- Toy009/Toy014 source-preparation throughput with reset/visibility/coherence;
- campaign duty/control and characterization-rate/floor envelope.

Absolute RESOURCE-045/NG-030 Toy009/Toy014 dominance therefore remains data-underdetermined. Do not start Toy015.

## Files

- `analysis/single_platform_cross_spectral_audit_iteration100.py`
- `docs/PAPER_III_SINGLE_PLATFORM_CROSS_SPECTRAL_AUDIT_ITERATION100.md`
- `research_log/2026-08-30_iteration_100_single_platform_cross_spectral_audit.md`

## Next admissible gate

Search the same experimental family/data for an explicit tunable two-frequency transfer calibration or public raw spectra from which a common force-coordinate f,2f matrix can be reconstructed. If unavailable, derive the minimum injected f,2f calibration protocol, block-count requirement and uncertainty target needed to close `R0,a2,a4,rho` experimentally rather than stitching external subsystems.
