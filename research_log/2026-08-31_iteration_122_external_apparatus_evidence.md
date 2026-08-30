# RQIR Research Log — Iteration 122

**Date:** 2026-08-31

## Question

Does the current published levitated-optomechanics literature already contain enough compatible same-apparatus data to populate the Iteration-121 physical Fisher-rate certificate and produce a numerical robust Toy009/Toy014 detector ratio `u`?

## Result

Audited experimental literature establishes the major component technologies separately:

- multimode PSD/cross-spectrum acquisition and mode-orientation control (Pontin et al., PRR 2023);
- measured transfer-function force-sensitivity calibration (Fu et al., OLE 2022);
- directional stochastic force sensing with PSD/cross-spectrum and finite integration blocks (Gosling et al., PRR 2024);
- 3D feedback transfer/gain/phase control with strongly reduced cross-talk (Gosling et al., RSI 2026);
- exact simultaneous fundamental/second-harmonic operation at 17.8/35.6 kHz in the same measurement (Song et al., Nature Communications 2026).

Thus exact `f:2f` simultaneous mechanical operation is now experimentally demonstrated as a platform class (**EXPERIMENT-001**).

However, none of the audited publications exposes the complete compatible RQIR input vector in one apparatus/likelihood: force-calibrated full `f:2f` PSD/cross-PSD transfer matrix, phase-profiled common-gain `R_c`, seven mean-layer rates, eight covariance-complement rates/backaction model, source metrology, geometry/additive SI controls and duty/drift.

### NG-080

Do not splice sensitivity, harmonic-mode and cross-spectrum numbers from different platforms into one RQIR wall-clock forecast without a validated transduction/uncertainty map.

### RESOURCE-094

A minimum public dataset for numerical `u` must provide the eight categories listed in `docs/PAPER_III_EXTERNAL_APPARATUS_EVIDENCE_ITERATION122.md` under one compatible apparatus state or validated mapping.

## Readiness snapshot

Project-management estimates, not statistical quantities:

- Paper III scientific-content readiness: **95%**.
- Paper III submission readiness: **78%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Next gate

Shift from inventing additional abstract detector rates to manuscript-facing literature/novelty closure: build a claim/evidence matrix separating formal theorem, deterministic toy regression, experimental precedent and still-open apparatus inputs. Further numerical `u` work becomes admissible when a compatible same-apparatus dataset satisfies RESOURCE-094.
