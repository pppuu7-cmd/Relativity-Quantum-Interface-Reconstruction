# Paper III sidecar: atom-interferometer nuisance/covariance closure audit

## Status

**Structural gate:** `PASS_WITH_CALIBRATION_REQUIREMENT`  
**Branch:** `paper-iii-nuisance-covariance-audit`  
**Authority note:** this is a Paper-III sidecar and does **not** replace or renumber the authoritative Candidate-Gravity Iteration-657 gate.

The numerical coordinates in this audit are synthetic and dimensionless. They are used to test identifiability and resource-closure logic; they are **not** a sensitivity forecast for a named apparatus.

## Forward model

We audit a generic phase observable

\[
\mu_i=\phi_0+(1+\kappa)\,\theta\,g_i+d_1 t_i+d_2 t_i^2,
\]

where `theta` is the target RQIR amplitude, `kappa` is a multiplicative scale-factor error, `phi0` is a phase offset, and `d1,d2` are drift nuisance parameters. The data covariance is

\[
\Sigma_{ij}=\sigma_w^2\delta_{ij}+\sigma_c^2\rho^{|i-j|},
\]

so offset/drift profiling and correlated noise are treated simultaneously rather than by independent error bars.

For additive nuisance basis `B=(1,t,t^2)` the science information remaining after profiling is

\[
q=g^T\Sigma^{-1}g-g^T\Sigma^{-1}B
(B^T\Sigma^{-1}B)^{-1}B^T\Sigma^{-1}g.
\]

## Result 1 — multiplicative scale is structurally degenerate with target amplitude

At the fiducial point `theta=1, kappa=0`,

\[
\partial_\theta\mu=g,\qquad \partial_\kappa\mu=g.
\]

The two Fisher columns are identical. Science data alone therefore have a one-dimensional null direction and cannot identify the absolute target amplitude separately from the apparatus scale.

This is not cured by more science shots.

It is also not cured merely by adding a second science configuration with a different signal shape if both channels still depend on the same product `(1+kappa)*theta`: after stacking both configurations, the `theta` and `kappa` Jacobian columns remain globally proportional. The numerical rank test in the companion script verifies this explicitly.

## Result 2 — finite scale calibration produces a hard precision floor

With a Gaussian scale prior `sigma_kappa`, the profiled target information is

\[
F_{\theta,\mathrm{prof}}=\frac{q}{1+q\sigma_\kappa^2}
\]

for `theta=1`, hence

\[
\mathrm{Var}(\theta)=\frac{1}{q}+\sigma_\kappa^2.
\]

This identity is verified numerically by the full joint Fisher matrix including phase offset, linear drift, quadratic drift, and correlated covariance.

Consequences:

- if the requested fractional precision is below `sigma_kappa`, no finite number of science shots closes the resource requirement;
- as the requested precision approaches the scale floor from above, required science resource diverges;
- once the statistical term falls below the scale term, the experiment becomes calibration-limited rather than statistics-limited.

For the synthetic `sigma_kappa=2%` audit, a `<=2%` target precision is therefore impossible from science data alone at finite resource.

## Result 3 — correlated noise makes modulation geometry part of resource closure

The audit uses `sigma_w=0.35`, `sigma_c=1`, and `rho=0.92`. After simultaneous projection of offset plus linear/quadratic drift:

| N | q slow | q lock-in | lock-in / slow | statistical sigma, lock-in | sigma incl. 2% scale |
|---:|---:|---:|---:|---:|---:|
| 64 | 2.726576 | 386.807737 | 141.866 | 5.0845% | 5.4638% |
| 128 | 2.532963 | 776.750312 | 306.657 | 3.5881% | 4.1078% |
| 256 | 3.242302 | 1556.502288 | 480.061 | 2.5347% | 3.2287% |
| 512 | 5.168179 | 3115.924700 | 602.906 | 1.7915% | 2.6850% |

The large gain is model-specific and must not be generalized numerically to a real apparatus. The structural conclusion is robust: correlated-noise covariance and drift projection act on the *shape* of the modulation vector, so a resource forecast that uses only a scalar white-noise level can be qualitatively wrong.

In this synthetic audit, by `N=512` the science channel has moved into a **calibration-limited** regime: the statistical contribution is below the 2% scale floor. A 3% target precision has finite resource closure, while a 2% or tighter target does not.

## Result 4 — an independent known-reference channel restores identifiability

A calibration observable with known amplitude `A_ref`, depending on scale but not on `theta`, contributes independent Fisher information on `kappa`. In the synthetic test with `A_ref=5` and the same `N=512` lock-in geometry,

- effective scale uncertainty becomes `0.3527%`;
- target uncertainty becomes `1.8258%`.

Thus the previously impossible `<2%` target becomes resource-closable once genuinely independent scale information is supplied.

The key requirement is **independence of parameter dependence**, not simply a second science configuration.

## Paper-III consequence

The correct experimental classification is not a single sensitivity number. Each apparatus configuration must be assigned to one of at least three regimes:

1. `NON_IDENTIFIABLE` — target lies in the nuisance tangent space and no independent calibration closes it;
2. `STATISTICALLY_LIMITED` — target is identifiable and science information dominates the uncertainty;
3. `CALIBRATION_LIMITED` — target is identifiable, but additional science exposure cannot beat the calibration floor.

This gives Paper III a stronger methodological statement: **resource closure is conditional on nuisance-space geometry and calibration identifiability, not only on signal-to-noise scaling.**

## What remains before apparatus-specific closure

This sidecar closes the structural Fisher/identifiability question only. A publication-grade atom-interferometer implementation still needs:

- apparatus-specific phase transfer function and physical units;
- declared scale-factor origin and calibration observable/prior;
- laser phase, vibration, timing and common-mode covariance channels as applicable;
- covariance-estimation uncertainty rather than assuming `Sigma` known exactly;
- heteroskedastic / configuration-dependent noise if present;
- phase nonlinearity / fringe wrapping where the linearized phase model is insufficient;
- correlations between science and calibration data;
- coverage or posterior checks beyond local Fisher curvature;
- a reproducible parameter table tied to a concrete experimental architecture.

Until those items are supplied, this result must not be called a complete apparatus forecast.

## Reproduction

Run:

```bash
python analysis/paper_III_atom_interferometer_nuisance_covariance_audit.py
```

Expected terminal classification:

```text
science-only theta/kappa identifiability: NON_IDENTIFIABLE
two science configurations, same scale: NON_IDENTIFIABLE
finite scale prior calibration-floor identity: PASS
correlated-noise + offset/drift simultaneous profiling: PASS
independent known-reference scale calibration: IDENTIFIABLE
Paper III nuisance/covariance structural gate: PASS_WITH_CALIBRATION_REQUIREMENT
```
