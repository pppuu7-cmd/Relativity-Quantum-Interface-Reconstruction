# RQIR Iteration 079 — Paper II Reference-Likelihood Regression Certificate

**Date:** 2026-08-30  
**Status:** scientific-scope closure/regression certificate for RQIR Paper II; physical rate conversion remains Paper III.

## 1. Purpose

Paper II has accumulated many source-specific and detector-specific Fisher calculations. The remaining scientific task was to freeze a compact set of likelihood invariants that every D1/D2 implementation must pass, so later apparatus changes cannot silently reintroduce discarded nuisance directions or change parameter coordinates.

Use a whitened local Gaussian likelihood with science score `s`, nuisance score matrix `J`, and independent nuisance/prior Fisher `P`. Then

`F_beta|theta = s^T s - s^T J (J^T J + P)^+ J^T s`.

When `P=0`, this is the squared norm of the part of `s` orthogonal to the nuisance-score span.

## 2. RQIR-STAT-001 — reference-likelihood certificate

A Paper-II detector likelihood is accepted only if it passes all of the following regressions.

### A. Schur/projection identity

With no nuisance prior,

`F_beta|theta = ||(I-P_J)s||^2`.

The deterministic regression gives agreement at the `~4e-15` level for the stored test problem.

### B. Nuisance-coordinate invariance

For any invertible nuisance reparameterization `theta=M phi`, use

`J_phi = J M`,  
`P_phi = M^T P M`.

The profiled `F_beta` is invariant. The stored regression agrees at `~3e-15`.

This prevents branch rankings from depending on arbitrary nuisance coordinates.

### C. Calibration monotonicity

If additional independent nuisance information is positive semidefinite, `P2-P1 >= 0`, then

`F_beta(P2) >= F_beta(P1)`.

A claimed loss of profiled science Fisher after adding genuinely independent calibration is therefore a sign of a coordinate/likelihood inconsistency, a changed experiment, or numerical failure.

### D. NG-005 exact amplitude obstruction

For normalized raw science Fisher `S=1` and a source-amplitude nuisance with identical detector score,

`F_beta|a(C_a=0)=0`,

and with independent preparation information

`F_beta|a = C_a/(1+C_a)`.

The regression verifies exactly the retained values

- `C_a=1 -> 0.5`;
- `C_a=4 -> 0.8`;
- `C_a=9 -> 0.9`;
- `C_a=19 -> 0.95`;
- `C_a=99 -> 0.99`.

Thus NG-005 is a structural local-identifiability obstruction, not a consequence of poor numerical conditioning.

### E. NG-006 exposure obstruction

If an unconstrained control nuisance score is exactly aligned with the science score, multiplying both by `sqrt(exposure)` leaves

`F_beta|theta=0`

for exposure factors from `1` through `1e6` in the regression. More data do not break an exact nuisance degeneracy.

### F. Two-band spectral-tilt identity

For two real whitened band amplitudes `(g2,g4)` and relative spectral-tilt nuisance score `(g2,-g4)`, profiling the tilt gives

`F_beta|tilt = 4 g2^2 g4^2/(g2^2+g4^2)`.

The deterministic test with `(0.3,0.7)` gives

`F=0.3041379310344828`,

matching the analytic expression to floating precision. This is the algebraic basis of the physical two-band `S_eff` metric used on the late D2 front.

### G. RQIR-NUM-001 threshold counterexample

Take science score

`s=(1,0)`

and nuisance score

`j=(1e-8,0)`.

The nuisance is weak in norm but exactly collinear with the science direction. Exact profiling gives

`F_beta|theta ~= 1.1e-16`,

i.e. zero to numerical precision.

If `j^T j=1e-16` is discarded by an arbitrary inverse threshold `1e-12`, the same calculation falsely returns

`F_beta=1`.

This is a minimal explicit counterexample proving why exact hard constraints must be eliminated analytically and why weak physical nuisance directions may not be deleted merely because their singular value is small.

## 3. Relation to D1/D2

The certificate is deliberately source-agnostic. Architecture-specific D1/D2 calculations must still include their actual detector covariance, centered-noise derivatives, spectral tilt, timing/geometry/additive columns, hard source constraints and calibration Fisher blocks.

The certificate does not replace Toy009/Toy010/Toy014 numerical likelihoods; it protects them against a common class of algebraic and numerical errors.

## 4. Paper-II scientific-scope decision

**Paper II scientific scope is closed at Iteration 079** for the architecture defined in `RQIR_ARTICLE_SERIES_ARCHITECTURE.md`.

The retained logical chain is now:

`exact null -> noisy nuisance likelihood -> F_beta|theta -> NG-005/NG-006 -> independent source/calibration information -> detector-level D1/D2 profiling`.

Conversion of `C_a`, `gamma`, detector information and controls into shots, PSD/SNR, coherence and wall-clock time belongs to Paper III and is not an unresolved Paper-II theorem.

Remaining pre-submission work is manuscript integration, literature/novelty positioning, figure/table production and independent reruns.

## 5. Reproducibility

Run

`python analysis/paper12_reference_regression_iteration079.py`.

The script asserts all seven certificate items and exits only after printing `PASS`.
