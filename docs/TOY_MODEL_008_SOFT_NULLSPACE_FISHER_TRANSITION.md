# RQIR Toy Model 008 — Soft Nullspace and Fisher Transition

**Date:** 2026-08-29  
**Labels:** `NUM`, `DRV`, `OPEN`  
**Purpose:** test whether forcing the Toy 007 calibration to near-tomographic exact rank is actually the best experiment-design strategy, and connect finite-rank operator geometry to covariance-weighted statistical identifiability.

## 1. Main numerical result

A deterministic 300-design scan of two-probe finite calibrations was performed on the same physical five-site Newtonian source used by Toys 005–007.

For each proposed probe geometry and six calibration times, a greedy selector added independent symmetrized auto/cross-kernel controls. At each target rank `20..24`, the exploratory score

\[
J_{\rm scan}=\eta_R\sqrt{s_{\min}}
\]

was evaluated, where

\[
\eta_R=\frac{\|P_{\ker A}r\|}{\|r\|}
\]

is the surviving exact response fraction and `s_min` is the smallest nonzero singular value of the calibration matrix after row normalization.

The best designs found in this scan were:

| rank | nullity | eta_R | s_min | condition number |
|---:|---:|---:|---:|---:|
| 20 | 5 | 0.696801 | 5.68468e-3 | 750.57 |
| 21 | 4 | 0.677521 | 5.43696e-3 | 803.96 |
| 22 | 3 | 0.638991 | 2.48186e-3 | 1801.88 |
| 23 | 2 | 0.607629 | 1.38924e-3 | 3271.43 |
| 24 | 1 | 0.473850 | 1.56388e-3 | 2965.14 |

Reproducibility: `analysis/rank_conditioning_scan.py`.

This scan does **not** establish a global optimum. It establishes a reproducible counterexample to the idea that `nullity = 1` is automatically the best finite design.

---

## 2. Immediate interpretation

Within this particular design family and score,

\[
\boxed{
\text{more exact calibration rank does not monotonically improve the operator-space design score.}
}
\]

The rank-20 design leaves five exact state directions unconstrained but retains both:

- a larger response projection;
- substantially better conditioning.

This suggests that the Toy 007 objective

\[
\dim\ker A=1
\]

was too restrictive as an experiment-design target.

However, this operator-space result is **not yet the final statistical conclusion**. Exact nullity and experimental identifiability are different questions.

---

## 3. Why the apparent paradox appears

Toy 006 showed that sufficiently complete time-dependent density calibration can become state tomography. Toy 007 then found a rank-24/25 middle ground with one exact response-bearing hidden state direction.

This can tempt one to reason:

> extra calibration is bad because it destroys the hidden state pair.

That statement is correct only if the research objective is **to preserve two distinct source states with exactly identical calibration values**.

A real inference problem instead asks whether an interface parameter can be distinguished from uncertain source, apparatus and detector parameters after finite-noise calibration.

These are not the same optimization problem.

---

## 4. Exact-null saturation result

Let

\[
A\delta\theta=0
\]

be an exact calibration with

\[
\operatorname{rank}A=p-1,
\qquad
\ker A=\operatorname{span}\{n\}.
\]

Adding one exact row `a^T` with

\[
a^Tn\neq0
\]

forces

\[
\delta\theta=0.
\]

Thus a one-dimensional exact null pair is destroyed by any genuinely independent additional exact constraint.

This result is catalogued as `RQIR-NG-004` in `STATISTICAL_IDENTIFIABILITY.md`.

---

## 5. Toy 007 concrete rank closure

For the accepted Toy 007 design,

\[
r_{obs}=24,
\qquad
\eta_R\approx0.457682.
\]

The response waveform reaches a nearby maximum around

\[
t\approx3.64030.
\]

Adding the probe-0 mean operator at that time has a nonzero projection on the old exact null vector and therefore raises the exact rank to 25.

So the original exact source-state pair no longer exists.

But the resulting full-rank matrix is extremely poorly conditioned because that new row is almost orthogonal to the old null vector.  The previously observed condition number of order `10^5` is therefore not paradoxical: rank closure can be mathematically exact while statistically weak.

---

## 6. Statistical re-formulation

Let `beta` be the RQIR parameter of interest and `theta` collect nuisance coordinates.  For local Gaussian data,

\[
\mu(\beta,\theta)
=\mu_0+s\,\delta\beta+J\,\delta\theta.
\]

The nuisance-profiled Fisher information is

\[
\boxed{
F_{\beta|\theta}
=
F_{\beta\beta}
-
F_{\beta\theta}F_{\theta\theta}^{-1}F_{\theta\beta}.
}
\]

Equivalently, after whitening the data covariance,

\[
\boxed{
F_{\beta|\theta}
=\|(I-P_{J})\tilde s\|^2.
}
\]

The detector-level objective is therefore to make the interface signal waveform linearly/statistically distinct from the nuisance waveform span, not to preserve a particular exact source null pair.

See `docs/STATISTICAL_IDENTIFIABILITY.md`.

---

## 7. Calibration monotonicity resolves the paradox

Under the explicit assumptions that:

1. added calibration data are statistically independent of the target data;
2. they contain no direct dependence on `beta`;
3. they add positive-semidefinite Fisher information `C` to the nuisance block;
4. the nuisance Fisher block is positive definite in the domain used,

then

\[
F'_{\beta|\theta}
\ge
F_{\beta|\theta}.
\]

Therefore more `beta`-blind calibration cannot reduce local profiled Fisher information even though it may eliminate an exact state-difference null pair.

This is a major methodological correction for RQIR.

---

## 8. Toy 007 scalar Fisher demonstration

Take the accepted normalized Toy 007 calibration matrix

\[
A\in\mathbb R^{24\times25}
\]

and normalized response vector `r_hat`.

The response overlap with the exact null direction is

\[
|\hat r^Tn|\approx0.457682.
\]

For the illustrative scalar target model

\[
y_R=\beta+\hat r^T\theta+\epsilon_R,
\]

`beta` is locally unidentifiable with the rank-24 calibration because the nuisance displacement along `n` can exactly absorb a change in `beta`.

Adding any calibration row with nonzero overlap with `n` restores positive profiled information.

A coarse search over additional Newtonian mean-probe rows found examples with normalized null overlap above `0.2`, much larger than the tiny overlap of the previously used near-peak row.

This numerical demonstration is in

`analysis/toy007_fisher_calibration_demo.py`.

It is illustrative only; it is not yet a physical detector forecast because the data covariance and parameter scales are normalized.

---

## 9. New experiment-design hierarchy

RQIR should now use the following sequence:

### Stage A — algebraic existence

Find whether an operator/channel distinction exists at all.

### Stage B — physical embedding

Map it into an admissible stress-energy / Newtonian / relativistic source channel.

### Stage C — finite calibration geometry

Identify which source directions are weakly or strongly constrained by realistic calibration channels.

### Stage D — transfer law

Propagate source means, noise and response through gravity and detector response.

### Stage E — statistical identifiability

Build the joint likelihood/Fisher model and profile source, apparatus, environmental and detector nuisance coordinates.

### Stage F — model-class discrimination

Compare semiclassical, stochastic, classical-gravity+QFT, perturbative-QG and other interface classes in one observable likelihood.

This replaces the earlier implicit stopping point at Stage C.

---

## 10. Consequence for the matched-filter idea

The response-spectrum calculation found that two harmonics contain most of the Toy 007 response power.

The correct next question is no longer simply whether mean/noise are exactly matched at every time sample.  Instead ask whether the **multi-frequency interface signal vector** is outside the nuisance waveform span after whitening by the full covariance.

Thus a two-frequency or matched-filter protocol may remain powerful even though dense exact time calibration would tomographically identify the source state.

The relevant metric is

\[
F_{\beta|\theta},
\]

not exact waveform equality.

---

## 11. Status

### Closed

- `DRV`: exact null-pair saturation theorem.
- `NUM`: reproducible rank-20..24 design scan.
- `DRV`: calibration monotonicity under declared Fisher assumptions.
- `DRV`: exact-null and statistical-identifiability geometries are distinct.

### Open

- realistic covariance matrix for an actual gravitational detector;
- physical nuisance parameterization;
- multi-harmonic profiled Fisher calculation;
- source-preparation and apparatus stress-energy accounting;
- relativistic conservation/gauge embedding;
- comparison across competing gravity-interface classes.

---

## 12. Next target

Build `Protocol 002` as a **multi-frequency profiled-likelihood experiment**:

\[
\text{source calibration}
+\text{pump}
+\{2\omega_*,4\omega_*\}\text{ response readout}
\longrightarrow
F_{\beta|\theta}.
\]

The first version should include at least nuisance parameters for:

- source-state preparation;
- source energy scale;
- probe positions / gravitational coupling normalization;
- detector gain and phase offset;
- broadband and narrow-band phase noise.

The target output is the first RQIR detector-level discrimination significance after nuisance profiling.
