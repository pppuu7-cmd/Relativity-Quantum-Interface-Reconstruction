# RQIR Iteration 101 — Same-State Temporal `f,2f` Calibration Protocol

**Date:** 2026-08-30  
**Status:** Paper-III detector/calibration closure; derived engineering protocol after the Iteration-100 single-platform audit. Not a hardware forecast and not a new-physics claim.

## 1. Why this iteration is necessary

Iteration 100 established a partial positive apparatus result: one levitated platform can measure ordinary PSDs and a non-diagonal cross-spectrum in a calibrated force-sensing setting. The remaining mismatch is coordinate structure: Gosling et al. measure spatial `x-y` covariance as a function of Fourier frequency, while RQIR D2 needs the joint covariance of two temporal score channels centered at `f` and `2f` in one input-referred force coordinate.

A follow-up search of the same UCL experimental family found:

- Pontin et al., *Phys. Rev. Research* 5, 013013 (2023), demonstrate control of mechanical mode frequencies/orientations while measuring `S_xy(omega)`;
- Gosling et al., *Phys. Rev. Research* 6, 013129 (2024), explicitly discuss a harmonic drive near `149 kHz` and finite force-spectrum averaging with example block length `T_b=3.3 ms`.

These are useful same-family capabilities, but the public sources inspected do not provide one same-state dataset containing a calibrated two-tone `f,2f` transfer measurement together with the temporal two-band covariance required by APP-003. The admissible step is therefore to derive the minimum injected-calibration protocol rather than substitute another paper's numbers.

Primary external anchors:

- `https://doi.org/10.1103/PhysRevResearch.6.013129`
- `https://doi.org/10.1103/PhysRevResearch.5.013013`

## 2. Exact finite-window cross-band covariance

For one scalar detector time series `y(t)`, define two complex demodulated estimators over the same block:

`z_n = integral_0^T w(t) y(t) exp[-i omega_n t] dt`,

with `omega_2=2 pi f` and `omega_4=4 pi f`.

For stationary noise with two-sided output spectrum `S_y(nu)`, their covariance is

`C_24 = integral dnu/(2 pi) S_y(nu) W_2^*(nu) W_4(nu)`,

where `W_n` is the shifted Fourier transform of the acquisition window. Thus temporal `f,2f` covariance is a property of the **noise spectrum plus the finite acquisition filters**, not merely of the two center frequencies.

For white noise and a rectangular window, the normalized overlap is exactly

`c_24 = exp[-i pi f T] sinc(f T)`.

### RQIR-RESOURCE-053 — finite-window temporal covariance kernel

The correct same-record cross-band covariance is obtained from the overlap integral of the two finite-time filters against the measured spectral density. A scalar ASD at the two center frequencies is insufficient.

### RQIR-DESIGN-011 — integer-cycle white-noise orthogonality

If the input-referred noise is white over the relevant support and

`T = M/f`, `M` a nonzero integer,

then

`c_24=0`

exactly for a rectangular block. Therefore a temporal `f,2f` protocol can be designed so that ideal white noise contributes zero cross-band covariance without requiring two mechanical resonances in a `2:1` ratio.

This is an engineering design fact, not permission to set the experimental `rho` to zero.

## 3. RQIR-NG-054 — orthogonal Fourier bins are not a covariance certificate

For colored stationary noise the finite-record covariance need not vanish even when `fT` is an integer. The reason is spectral leakage through the finite window: the two filters sample overlapping neighborhoods of a non-flat spectrum.

The deterministic regression uses a finite AR(1) stationary covariance. With 64 samples and DFT bins `(3,6)`:

- white case: `|corr| < 1e-12`;
- colored case with lag coefficient `0.8`: `|corr| ~= 0.03655`.

Therefore:

> **RQIR-NG-054:** DFT-bin orthogonality or distinct center frequencies do not certify `rho=0` under colored, drifting, cyclostationary, feedback-modified, window-leaked or shared-nuisance noise. The same-state covariance must be measured or bounded from the actual acquisition likelihood.

This is the temporal counterpart of Iteration-100 NG-053.

## 4. Robust `rho` target from retained science rate

For fixed raw band rates,

`R_beta(r2,r4,rho) = 4 r2 r4 / [r2+r4+2 rho sqrt(r2 r4)]`.

Suppose nominal correlation is `rho0` and we require the robust upper correlation `rho_hi` to retain a fraction `q` of the nominal science rate. Solving

`R_beta(rho_hi) >= q R_beta(rho0)`

gives

`rho_hi <= {[(r2+r4+2 rho0 sqrt(r2 r4))/q]-(r2+r4)}/[2 sqrt(r2 r4)]`.

For balanced bands and nominal `rho0=0`, this becomes

`rho_hi <= 1/q - 1`.

At the transparent `q=0.90` benchmark:

`boxed{rho_hi <= 1/9 ~= 0.111111}`.

### RQIR-RESOURCE-054 — correlation-certification block count

For an ideal independent real bivariate Gaussian block with unknown marginal variances, profiling those variances gives per-block Fisher

`I_rho = 1/(1-rho^2)^2`.

Hence, around `rho0`,

`sigma_rho ~= (1-rho0^2)/sqrt(N)`.

Using `rho0=0`, the `q=0.90` bound above, and a normal `z=1.96` confidence margin gives

`N >= [1.96/(1/9)]^2`,

so

`boxed{N_rho >= 312 independent blocks}`.

Using Gosling's published `3.3 ms` force-spectrum block only as an **illustrative time scale**, 312 blocks would correspond to `1.0296 s` raw integration. This is not an RQIR apparatus forecast: real temporal `f,2f` blocks can be correlated, overlapped, drift-limited, or have different duration.

## 5. Same-state dual-tone transfer calibration

Inject a known force in the same science operating state,

`F_inj(t)=Re[A_2 exp(i omega_2 t)+A_4 exp(i omega_4 t)]`,

and demodulate the output with the same filters used for science. Let the complex transfer values be `chi_2,chi_4`.

The joint real calibration likelihood is a four-component Gaussian vector

`(Re z_2, Im z_2, Re z_4, Im z_4)`

with the full same-block covariance matrix retained. The Fisher matrix for transfer amplitude/phase is

`F_cal = J_chi^T Sigma_z^-1 J_chi` per block,

and the physical rate is

`R_cal,chi = p_cal F_cal/t_block`.

### RQIR-CAL-021 — calibration must use the science state and science filters

The transfer injection must be performed under the same feedback, trap, detector gain, window, sampling and operating state used by science, or linked to that state by a separately calibrated transfer model with uncertainty. Otherwise transfer uncertainty is a nuisance that must remain in the science likelihood.

This requirement is especially important because the UCL mode-control paper shows that optomechanical backaction can shift frequencies and rotate modes as operating conditions change.

## 6. Transfer-amplitude Fisher target

If both raw band rates are conservatively reduced by the same worst fractional transfer-amplitude error `epsilon_g`, then

`r_n^- = (1-epsilon_g)^2 r_n`,

and the whole two-band rate scales by the same factor. Retaining fraction `q` therefore requires

`epsilon_g <= 1-sqrt(q)`.

At `q=0.90`,

`boxed{epsilon_g <= 0.0513167}`

or about `5.13%` per band under this conservative common bound.

If one calibration block supplies matched fractional-transfer Fisher equal to `SNR_inj^2`, then a normal `z` confidence requirement gives

`N SNR_inj^2 >= [z/(1-sqrt(q))]^2`.

At `q=0.90`, `z=1.96`:

`boxed{N SNR_inj^2 >= 1458.80}`.

Transparent examples:

- injection SNR `10` per independent block -> at least `15` blocks;
- injection SNR `5` -> at least `59` blocks.

These are amplitude-calibration lower bounds only. Phase, cross-covariance, nonlinear response, drift and seven source-specific calibration layers can require more.

## 7. RQIR-NG-055 — a two-tone injection must pass a linearity/intermodulation gate

Simultaneously injecting `f` and `2f` is useful only if the detector/calibration chain is linear over the calibration amplitude range. Quadratic response, saturation, feedback mixing or actuator nonlinearities can generate apparent harmonics and cross-covariance that are not present in the weak science signal.

Therefore the protocol must include amplitude-scaling checks and, where possible, off-grid/intermodulation monitors. A high-SNR calibration that leaves the linear-response domain cannot be credited toward `R0,a2,a4,rho`.

## 8. What Iteration 101 closes

Closed algebraically/operationally:

- the exact finite-window object that determines temporal `f,2f` covariance;
- a window design that gives exact white-noise orthogonality;
- a robust correlation target tied directly to retained science Fisher;
- a Gaussian lower bound on independent blocks needed to certify that correlation;
- a same-state dual-tone transfer likelihood;
- a transfer-amplitude precision target and injection-Fisher budget.

Still open experimentally:

- actual same-state `S_y(nu)`, temporal covariance and block independence;
- physical injection SNR and actuator linearity in a candidate apparatus;
- propagation of transfer uncertainty into all seven RQIR calibration blocks;
- source preparation/reset/visibility/coherence and duty;
- an absolute Toy009/Toy014 NG-030 winner.

## 9. Next admissible gate

Build the **joint science + injected-transfer likelihood** with transfer amplitude/phase and `rho` as profiled nuisance parameters rather than independent post-hoc error bars. Derive the Schur-complement `R_beta|transfer,rho` and solve the calibration/science time split that minimizes total wall clock for a fixed retained-Fisher target.

This will show whether the new detector bottleneck is primarily cross-covariance estimation, transfer calibration, or raw science exposure. Only if the residual dominant cost is source-specific should Toy015 be opened.

## 10. Reproducibility

Code:

`analysis/same_state_f2f_calibration_protocol_iteration101.py`

The script verifies exact integer-cycle white-noise orthogonality, a colored finite-block counterexample, the 90% `rho` bound, the 312-block Gaussian certification lower bound, and the `N*SNR_inj^2` transfer-calibration requirements.
