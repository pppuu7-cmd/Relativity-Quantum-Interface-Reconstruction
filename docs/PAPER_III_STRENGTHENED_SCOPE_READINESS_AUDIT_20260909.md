# RQIR Paper III — strengthened-scope readiness audit

**Date:** 2026-09-09  
**Branch:** `paper-iii-nuisance-covariance-audit`  
**Status:** working sidecar; does not replace the Candidate-Gravity authority chain or Iteration-657.

## 1. Why the repository can say both “100%” and “not ready”

Iteration 128 correctly certifies **100% scientific-content readiness under the original restricted Paper-III scope**. That checker deliberately keeps the following as conditional extensions rather than premises:

- measured same-apparatus rate matrices;
- measured geometry/additive-drift controls;
- measured covariance/backaction likelihood;
- numerical Toy009/Toy014 architecture ratio `u`;
- a measured architecture winner.

Iteration 124 is equally explicit that the detector-side Toy009/Toy014 section is interval-certifiable but **not yet numerically apparatus-closed**.

The present audit therefore uses a stronger target: a publication-grade Paper III with an explicit atom-interferometer nuisance/covariance case study. Under this stronger target, the old `100%` is not the relevant readiness metric.

## 2. Existing machinery that must not be rediscovered or claimed as new

The repository already contains substantial general nuisance/covariance machinery:

- Iteration 014: correlated calibration covariance plus slow-drift diagnostics;
- Iterations 015–016: hard-constraint and low-rank systematic Fisher audits;
- Iteration 023: colored-drift / Allan-cadence layer;
- Iterations 032–046: native and shared D2 covariance / backaction chain;
- Iterations 060–063: relational covariance and profiled spectral-tilt metrology;
- Iterations 085–089: correlated dual-band and robust campaign layer;
- Iteration 102: joint science-transfer profile;
- Iteration 113: likelihood-derived transfer covariance budget and Schur/LMI calibration certificate;
- Iteration 115: full-complex common-gain rate certificate;
- Iteration 119: full covariance endpoint partition;
- Iterations 123–128: Paper-III claim, manuscript, reproducibility, priority and scope-closure audits.

Therefore neither the Schur complement, Fisher profiling, correlated covariance, nor nuisance-aware design is a new Paper-III claim by itself. Iteration 123 already enforces this publication discipline.

## 3. What the new atom-interferometer sidecar actually adds

The sidecar `analysis/paper_III_atom_interferometer_nuisance_covariance_audit.py` integrates in one science time-series likelihood

`phase offset + multiplicative scale + linear/quadratic drift + correlated noise`.

For

`mu = phi0 + (1+kappa) theta g + d1 t + d2 t^2`

it verifies the exact science-only target/scale degeneracy and the calibration-floor identity

`Var(theta) = 1/q + sigma_kappa^2`  (at `theta=1`).

It also verifies that merely stacking different science modulation shapes does not remove a common multiplicative scale degeneracy, while a genuinely independent known-reference calibration channel does.

This is best interpreted as an **apparatus-facing integration/guardrail result**, not as a new general Fisher theorem.

## 4. External atom-interferometer sanity check

A useful real-world anchor is Chen et al., *Review of Scientific Instruments* **95**, 053201 (2024), DOI `10.1063/5.0198240`, “Self-calibrated atom-interferometer gyroscope by modulating atomic velocities.”

The experiment self-calibrates by controlling atomic velocity through laser-frequency detuning and thereby modulating the gyroscope scale factor. The published result reports an absolute Earth-rotation measurement with a relative uncertainty of 162 ppm. The full uncertainty discussion reports a scale-factor relative uncertainty of about 122 ppm and an absolute phase contribution of about 106 ppm; their quadrature combination is approximately 162 ppm.

This does not prove the RQIR model, but it is an important apparatus sanity check: practical atom-interferometer “self-calibration” supplies independent metrology for the scale coordinate rather than obtaining an absolute amplitude from repeated science shots with an otherwise free common scale.

Related literature also supports the need for explicit covariance/systematics treatment: atom-interferometer performance is known to depend on vibration/common-mode noise, phase/laser noise, wavefront effects, contrast, pulse fidelity, and scale-factor modeling. These ingredients should enter Paper III as apparatus nuisances, not as a single scalar sensitivity.

## 5. Strengthened-scope readiness rubric

This is an engineering/research-management rubric, not a repository authority theorem.

### Closed / sufficiently mature for the strengthened paper

- core RQIR interface-to-profiled-likelihood logic;
- detector/source physical Fisher-rate bridge;
- generic nuisance and covariance machinery;
- calibration/reference/common-gain profiling machinery;
- campaign/resource-closure machinery;
- claim/novelty guardrails and reproducibility manifest;
- structural atom-interferometer target/scale + drift + red-noise integration test.

### Still open for the strengthened paper

1. choose one concrete atom-interferometer architecture and freeze its observable definition;
2. write the physical phase transfer function in SI units and map every scale factor to independently measurable primitives;
3. specify the scale-calibration observable/prior with a defensible literature or apparatus value;
4. construct an apparatus-specific covariance model including the relevant laser/vibration/timing/common-mode channels;
5. include uncertainty in the covariance estimate itself, rather than treating `Sigma` as exact;
6. propagate science/calibration correlations and nonstationarity;
7. check nonlinear fringe likelihood / phase wrapping where the local phase approximation fails;
8. perform coverage or posterior validation beyond local Fisher curvature;
9. produce a single reproducible parameter table and case-study figure set;
10. package an actual `manuscripts/paper_III` directory and refresh the final literature/priority audit before submission.

## 6. Current readiness assessment

- **Original restricted Paper-III scientific scope:** `100%` by Iteration 128, with apparatus extensions explicitly conditional.
- **Strengthened apparatus-specific Paper III:** **about 55%**.
- **Current joint nuisance/covariance task:** **about 65%** complete: the structural identifiability/calibration-floor part is closed; apparatus-specific transfer/covariance/coverage remains open.

The 55% value is deliberately approximate. It should not be promoted by simply writing more manuscript text. It should rise only when the concrete apparatus transfer, calibration, covariance and nonlinear-validation gates close.

## 7. Next highest-value gate

Freeze a concrete differential atom-interferometer architecture and build the **SI-unit likelihood contract**:

`{raw observable -> phase estimator -> physical transfer -> scale primitives -> nuisance Jacobian -> covariance blocks -> calibration channel -> profiled Fisher/posterior -> wall-clock closure}`.

The most useful architecture is one with an explicit differential/common-mode channel and an independently calibratable scale coordinate, because it directly exercises the degeneracy exposed by the new sidecar rather than hiding it behind a prior.
