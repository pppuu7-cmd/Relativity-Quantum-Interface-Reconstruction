# RQIR Recovery Delta — Iteration 122

**Date:** 2026-08-31  
**Parent front:** Iteration 121.

## External same-apparatus audit

Experimental component technologies now exist separately:

- multimode PSD/cross-spectrum acquisition and mode-orientation control;
- measured transfer-function force-sensitivity calibration;
- directional stochastic force sensing with finite spectral integration;
- feedback gain/phase control with reduced cross-talk;
- exact simultaneous fundamental/second-harmonic operation.

### EXPERIMENT-001

Song et al., Nature Communications 17, 8852 (2026), demonstrates a fundamental mechanical mode at 17.8 kHz and its second harmonic at 35.6 kHz simultaneously in the same measurement. Exact `f:2f` mechanical operation is therefore experimentally established as a platform class.

### NG-080

Do not splice sensitivity, cross-spectrum and harmonic-mode numbers from different experimental platforms into one Toy009/Toy014 apparatus forecast without a validated transduction and uncertainty map.

### RESOURCE-094

A numerical robust detector certificate still requires one compatible dataset containing:

1. simultaneous complex transfer at the retained two bands;
2. full PSD/cross-PSD matrix in one convention;
3. common-gain reference data sufficient for `R_c`;
4. seven mean-layer physical Fisher-rate matrices;
5. covariance-complement rates plus backaction model for shared records;
6. geometry/additive SI transduction and stability/reference data;
7. source-metrology throughput/acceptance/reset/visibility;
8. timing/control duty and drift/recertification data.

No audited publication supplies all eight categories in one compatible likelihood. The Iteration-121 parametric `u` interval therefore remains the correct public-data boundary.

## Readiness after Iteration 122

- Paper III scientific-content readiness: **95%**.
- Paper III submission readiness: **78%**.
- Repository readiness to begin Candidate Gravity: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Files

- `analysis/external_apparatus_evidence_matrix_iteration122.py`
- `docs/PAPER_III_EXTERNAL_APPARATUS_EVIDENCE_ITERATION122.md`
- `research_log/2026-08-31_iteration_122_external_apparatus_evidence.md`

## Next gate

Perform manuscript-facing literature/novelty closure and build a claim/evidence matrix separating theorem, deterministic toy regression, external experimental precedent and open apparatus inputs. Further numerical `u` work requires a RESOURCE-094-compatible same-apparatus dataset.
