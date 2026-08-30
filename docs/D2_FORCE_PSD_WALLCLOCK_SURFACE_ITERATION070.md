# RQIR Iteration 070 — D2 Force-PSD Wall-Clock Surface

**Date:** 2026-08-30  
**Status:** retained physical-resource bridge; not an apparatus forecast and not a new-physics claim.

## 1. Front and purpose

Iteration 069 established that the two same-time D2 probe channels must be treated with a full `2x2` Fisher/PSD matrix. The remaining problem was to connect that matrix likelihood to the wall-clock ratio

`x = T_cal/T_sci`

without inventing an undocumented laboratory detector.

This iteration therefore uses a deliberately transparent *reference likelihood* rather than a claimed experimental specification: a rectangular equivalent-force template, one-sided white equivalent-force PSD, equal science/calibration cycle scheduling, and symmetric two-channel cross correlation. The final answer is kept as a surface in a physical force-scale ratio, so absolute ASD cancels where it legitimately can.

## 2. Declared force-PSD likelihood

For a scalar force template of amplitude `F` lasting time `T`, with one-sided white equivalent-force PSD

`S_F = A_F^2`, 

the frequency-domain matched-filter Fisher is

`I_F = 4 int_0^inf |F T sinc(pi f T)|^2/S_F df`

and therefore exactly

`I_F = 2 F^2 T/S_F`.

For a same-time two-probe layer with symmetric normalized noise covariance

`C = [[1,rho],[rho,1]]`,

the detector-relevant worst eigenmode has

`I_cal,min = 2 F_cal^2 T / [S_F (1+|rho|)]`.

This reproduces the correlation penalty of Iteration 069, now in SI force/PSD language.

## 3. Science Fisher in the same coordinate

Write the Toy009 spectral-tilt-profiled D2 source factor as

`S_eff^009 = 5.7795071960e-4`.

Let `F_sci` be the physical equivalent-force amplitude multiplying the normalized D2 science direction, and `F_cal` the corresponding force amplitude for one row-normalized calibration coordinate. Define

`r_F = F_sci/F_cal`.

Under the declared equal-schedule/equal-PSD reference likelihood, common acceptance, PSD, template duration and cycle-time factors cancel between science and calibration rates.

Using seven independent same-time calibration layers and Toy009

`gamma_mean = 1.830264703e6`,

the wall-clock ratio becomes

`x = [7 gamma_mean S_eff^009/Z^2] (1+|rho|) r_F^2`.

At `Z=5`,

`boxed{x = 296.184784604 (1+|rho|) r_F^2}`.

This is **RQIR-RESOURCE-032**: once science and calibration are expressed in one equivalent-force PSD coordinate, the relevant calibration/science wall-clock ratio is controlled by a physically meaningful transduction ratio `r_F`, not by the old abstract `xi_mu`.

## 4. Toy013-vs-Toy009 dominance surface

Iteration 066 gave the apparatus-independent total-time boundary

`x > 25.8350584 + 376.305592 y`,

where

`y = T_src^009/T_sci^009`.

Combining it with the force-PSD bridge yields

`296.184784604 (1+|rho|) r_F^2 > 25.8350584 + 376.305592 y`.

Equivalently,

`r_F > sqrt[(25.8350584+376.305592 y)/(296.184784604(1+|rho|))]`.

This is the first explicit transduction/source-metrology phase boundary for the mature Toy009 vs calibration-efficient Toy013 comparison.

### Equal force scales: `r_F=1`

For `rho=0`,

`x = 296.184784604`,

and Toy013 can beat Toy009 only if

`y < 0.718431328`.

For `rho=0.5`,

`x = 444.277176906`,

with

`y < 1.111974224`.

For `rho=0.9`,

`x = 562.751090748`,

with

`y < 1.426808540`.

The increase of the Toy013-favouring region with `|rho|` is not a benefit of correlated noise. Correlation makes Toy009 mean calibration more expensive; because Toy013 had a much lower profiled calibration cost in Iteration 065, this shifts the *relative* architecture comparison toward Toy013.

### Critical transduction ratio

At `rho=0`:

- if `y=0`, `r_F,crit ~= 0.29534`;
- if `y=0.1`, `r_F,crit ~= 0.46298`;
- if `y=1`, `r_F,crit ~= 1.16510`.

Thus, even under this intentionally favourable common-PSD benchmark, Toy013 is not automatically preferred. Its lower calibration burden compensates its science penalty only when the physical science-force scale is sufficiently large relative to a row-normalized calibration-force scale *and* independent source metrology is sufficiently fast.

## 5. Negative result / guardrail

### RQIR-NG-028 — absolute ASD cancellation is conditional

An equivalent-force ASD can cancel from `T_cal/T_sci` only when science and calibration actually share the same transduction/output-noise model, acceptance and acquisition template up to the declared scale factors. If their transfer functions, bandwidths, PSDs, duty factors or estimators differ, replacing them by a single `A_F` gives a false resource cancellation.

Therefore the surface above is a controlled reference likelihood, not a statement that a real D2 apparatus has `x=296...`.

## 6. Consistency with prior gates

- NG-005 remains active: the gravitational exact-null does not identify the hidden preparation amplitude.
- NG-006 remains active: timing/geometry/additive nuisance degeneracies are not cured by this resource bridge.
- NG-023 remains active: source H-QND metrology is not automatically ordered-response nondemolition.
- NG-026 remains active: hard rank is not finite-noise closure.
- NG-027 remains active: an already-demodulated phase sigma is not automatically a single-shot detector likelihood.
- No relativistic, full-QFT, stochastic/classical-gravity degeneracy or experimental consistency gate is claimed closed.

## 7. Reproducibility

Run:

`python analysis/d2_force_psd_wallclock_surface_iteration070.py`

The script prints the exact `x` prefactor, equal-force-scale `y` boundaries and critical `r_F` values, with regression assertions.

## 8. Next admissible gate

The next useful step is to remove the equal-schedule/equal-PSD simplification without selecting a speculative laboratory number. Introduce separate science and calibration transfer functions and PSD integrals,

`K_sci = 4 int |H_sci(f)|^2/S_sci(f) df`,

`K_cal,j = 4 int J_j^dag S_j^-1 J_j df`,

plus acceptance/dead/reset/coherence factors. Then propagate these into one total wall-clock budget together with the already explicit source-metrology Fisher rates. This will show which cancellations are structural and which were artifacts of the reference likelihood.
