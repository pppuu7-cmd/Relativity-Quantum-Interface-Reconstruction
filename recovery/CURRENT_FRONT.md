# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 097**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast Paper-III resource front. Read this pointer plus the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Publication-track status

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–097 translate abstract Fisher requirements into physical science/calibration/source/control rates, robust correlated two-band likelihoods, seven-layer matrix calibration rates, interval-safe wall-clock architecture comparison, physical Toy009/Toy014 crossover, primitive value-of-information, and now characterization-time optimization.

RQIR remains separate from RTK/DSIR. No toy, Fisher, resource, detector, or characterization result is an empirical new-physics claim.

## Mature inference backbone

Primary detector quantity:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Mandatory retained gates:

- **NG-005:** exact gravitational-null calibration cannot self-calibrate hidden source amplitude;
- **NG-006/007:** low-rank control degeneracies and low-frequency stability floors can survive arbitrarily high science exposure;
- **NG-023:** H-QND source metrology is not automatically ordered-response nondemolition;
- **NG-025/026:** locality belongs inside co-design; exact rank completion is not finite-noise/resource closure;
- exact hard constraints, centered covariance derivatives, spectral-tilt profiling and full matrix PSD/cross-PSD Fisher are mandatory.

## Physical wall-clock backbone

Use

`T_sci = Z^2/R_beta`,

`T_cal = gamma sum_j 1/R_cal,j`,

`T_src = C_src/R_src`,

with duty multiplier

`m = 1/(1-d)`.

For the common `Z=5`, 90% multiplicative source-retention benchmark, `C_src=225`.

**NG-030:** robust branch dominance requires conservative nonoverlap, `T_i^upper < T_k^lower`.

Iteration 089 gives

`T_total^upper = [Z^2/R_beta^- + gamma sum_j 1/R_cal,j^- + C_src/R_src^-]/(1-d^+)`,

with the corresponding lower bound from upper rates and lower duty.

## Correlated simultaneous two-band science — Iterations 084–087

For raw band Fisher rates `r2,r4` and ordinary covariance correlation `rho`,

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`, `|rho|<1`.

Retain:

- **RESOURCE-039:** `rho=0` gives twice the harmonic mean;
- **NG-036:** marginal ASD/PSD values do not determine simultaneous `R_beta`; cross-PSD/full spectral matrix is required;
- **CORR-001:** for `rho<0`, the partner optimum is `r_partner/r_weak=1/rho^2`;
- **RESOURCE-040:** exact box lower science rate uses `rho_hi` and the four rate corners;
- **NG-037:** anti-correlation is not robust credit unless its uncertainty upper bound remains sufficiently negative.

## Seven-layer physical calibration — Iteration 088

For each dual-probe calibration block

`F_j=[[a_j,c_j],[c_j,b_j]]`,

use

`R_cal,j=lambda_min(F_j)`.

For PSD-safe independent entry uncertainty, concavity of `lambda_min` places the exact lower envelope at one of the eight box vertices.

`H_cal^- = 7/sum_j(1/R_cal,j^-)`,

`T_cal^upper = gamma sum_j(1/R_cal,j^-)`.

Shot mapping:

`N_acc,j >= gamma/i_j^-`,

`N_try,j = gamma/(p_j^- i_j^-)`,

`R_cal,j^- = p_j^- i_j^- / t_cyc,j^+`.

**NG-038:** uncertainty boxes crossing the PSD boundary do not certify positive robust calibration throughput.

## Source-metrology robustness — Iteration 089

**NG-039:** for fixed predeclared source-metrology design, guaranteed throughput is `max_design min_uncertainty R`, not `min_uncertainty max_design R`, unless adaptive retuning and its cost are explicitly modeled.

## External apparatus audit — Iteration 090

Published multimode levitated platforms show useful simultaneous readout/control capability but do not yet supply one common RQIR-normalized apparatus containing the required `f,2f` science bands, seven calibration blocks, source metrology and campaign duty.

- **APP-002:** published multimode capability is not yet a complete RQIR apparatus envelope.
- **NG-040:** do not concatenate best-in-class subsystem numbers from separate experiments as one likelihood.

## Tunable simultaneous f,2f envelope — Iteration 091

With common physical detector/calibration throughput `R0`, write

`r2^-=a2 R0`, `r4^-=a4 R0`,

`s=4a2a4/(a2+a4+2 rho_+ sqrt(a2a4))`,

`R_beta^-=s R0`,

`R_cal,j^-=k_j R0`,

`A=Z^2/s + gamma sum_j 1/k_j`.

Then

`T_total^upper=m[A/R0+C_src/R_src^-]`.

**RESOURCE-043:** for a target `T_cap`, first require `R_src^- > m C_src/T_cap`, then

`R0_min=m A/[T_cap-m C_src/R_src^-]`.

**NG-041:** below the source-only floor no detector/calibration improvement can rescue the requested wall clock.

## Physical Toy009/Toy014 crossover — Iterations 092–093

For architecture `i`,

`T_i=m_i[A_i/R0+C_src/R_src,i]`.

Nominal difference:

`T_14-T_09 = Delta_D/R0 + Delta_S`,

with

`Delta_D=m_14 A_14-m_09 A_09`,

`Delta_S=C_src(m_14/R_src,14-m_09/R_src,09)`.

**RESOURCE-044:** a positive finite nominal crossing is `R0_cross=-Delta_D/Delta_S`.

**NG-042:** if Toy014 is worse in detector/calibration and has no duty-adjusted source advantage, it cannot win at any finite positive `R0`.

**PREP-005:** in the common Ramsey model and declared reset/visibility box, the optimized Toy014/Toy009 source-rate ratio remains above `1.39`; this is a finite design-box result, not a theorem.

Under independent source-specific uncertainty intervals,

`T_i^upper=m_i^+[A_i^+/R0+C_src/R_src,i^-]`,

`T_i^lower=m_i^-[A_i^-/R0+C_src/R_src,i^+]`.

**RESOURCE-045:** each robust crossing remains an exact `D/R0+S` boundary.

**NG-043:** forward and reverse robust boundaries can leave an unresolved throughput band in which neither architecture is an NG-030 winner.

**NG-044:** shared-kernel Pareto ratios `(q_s,q_c,q_p)` are not sufficient statistics for robust physical dominance.

## Characterization value-of-information — Iterations 094–095

For an active robust boundary `B=-D/S`,

**RESOURCE-046:** `dB=-(1/S)dD+(D/S^2)dS`.

For interval half-width contraction `eta`, define

`Lambda_x=(1/W)dW/deta_x`.

- **DESIGN-006:** prioritize characterization by reduction of the robust decision band, not raw percentage uncertainty.
- **NG-045:** largest fractional uncertainty need not be highest decision value.
- **NG-046:** local leverage must be recomputed after substantial contractions and replaced by joint uncertainty treatment when correlated.

Iteration 095 propagates this to measurable primitives.

Science:

`A_sci=Z^2[1/(4a2)+1/(4a4)+rho/(2 sqrt(a2a4))]`.

- **RESOURCE-047:** compose exact `(a2,a4,rho)` gradients with RESOURCE-046.

Calibration block `F_j=[[u,w],[w,v]]`:

`k_j=lambda_min(F_j)`, `A_cal=gamma sum_j 1/k_j`.

- **DESIGN-007:** under equal fractional improvement, the slowest calibration layer has the largest calibration-time leverage.

Source metrology on a smooth branch:

`R_src=p_E Omega_E q(V,Omega_E t_reset)`

with primitive derivatives in acceptance, coupling, reset and visibility.

- **NG-047:** for `rho<0`, improving one raw science band is not globally monotone useful; the local sign flips at `a2/a4=1/rho^2`.
- **NG-048:** local primitive derivatives fail at repeated calibration eigenvalues, PSD contact, robust-corner switches or Ramsey active-set changes; use finite contractions/subgradients/robust optimization.

## Iteration 096 — characterization value per physical second

A sensitivity derivative is not yet a measurement schedule.  Let `h_x` be the current uncertainty scale of primitive `x` and `R_char,x` its independent characterization Fisher rate.

**RESOURCE-048:** in the Fisher-limited smooth model,

`Xi_x = -(1/W)dW/dt = 0.5 Lambda_x R_char,x h_x^2`.

This is the local fractional unresolved-band shrink rate per characterization second.

**NG-049:** the largest `Lambda_x` need not be the best measurement per second.  Physical priority depends on `R_char,x h_x^2` and any shared duty/cost.

For an irreducible floor `h_f`,

**RESOURCE-049:** contracting `h0 -> h1` costs

`T_char=[1/(h1^2-h_f^2)-1/(h0^2-h_f^2)]/R_char`,

provided `h1>h_f`; targets at/below the floor are impossible.  With zero floor, halving an uncertainty costs `3/(R_char h0^2)`.

The old Iteration-094 leverage ranking is recovered only when normalized characterization speeds `R_char h^2` are equal.  In its synthetic regression box, Toy014 aggregate `A` overtakes Toy014 `R_src` as the better measurement per second when its normalized characterization speed is more than `2.866505...x` larger.  This number is regression-only.

Files:

- `analysis/characterization_time_voi_iteration096.py`
- `docs/PAPER_III_CHARACTERIZATION_TIME_VOI_ITERATION096.md`
- `research_log/2026-08-30_iteration_096_characterization_time_voi.md`
- `recovery/RECOVERY_DELTA_ITERATION_096.md`

## Iteration 097 — finite characterization-time allocation

On a fixed smooth branch, approximate the uncertainty-dependent decision width by

`W ~= W_const + sum_i c_i/sqrt(I_i0+R_i t_i)`

with `sum_i t_i=T_char`.

Each term is convex, so the KKT solution is globally optimal in the declared local model.

**RESOURCE-050 — characterization water-filling:**

`boxed{t_i(lambda)=max(0,[(c_i R_i/(2 lambda))^(2/3)-I_i0]/R_i}`,

with `lambda` chosen so `sum_i t_i=T_char`.

Every active channel finishes with equal marginal decision-band shrink rate

`c_i R_i/[2(I_i0+R_i t_i)^(3/2)] = lambda`.

The initial marginal reduces exactly to Iteration 096:

`(1/W)M_i0 = 0.5 Lambda_i R_i h_i^2`.

**NG-050:** equal characterization time or equal fractional contraction is generally suboptimal.  Channels enter the active set as higher-value measurements accumulate Fisher and their marginal value falls.

For systematic floors use RESOURCE-049 piecewise/numerically.  For correlated posterior updates use a joint Fisher/covariance model.  NG-048 remains active at nonsmooth branch/eigenvalue/corner changes.

Files:

- `analysis/characterization_waterfill_iteration097.py`
- `docs/PAPER_III_CHARACTERIZATION_WATERFILL_ITERATION097.md`
- `research_log/2026-08-30_iteration_097_characterization_waterfill.md`
- `recovery/RECOVERY_DELTA_ITERATION_097.md`

## Immediate next gate — Paper III only

Construct the first declared primitive Toy009/Toy014 characterization table.  For every active science/calibration/source/control primitive supply:

`central value, uncertainty interval/covariance, physical characterization Fisher rate, irreducible floor, correlations, and characterization duty/cost`.

Use repository-backed source coefficients and externally measured/sourced apparatus quantities where one common normalization exists; otherwise keep the apparatus layer explicitly parameterized rather than inventing a hardware forecast.

Then apply RESOURCE-050 together with RESOURCE-045/NG-030 to determine a robust architecture or the remaining unresolved band.  Do not start Toy015 unless this physical schedule identifies a genuinely source-dependent bottleneck that a new local source could plausibly improve.

## Discipline

Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
