# RQIR Operational Master Table

**Version:** 2.0  
**Date:** 2026-08-29

The repository is authoritative. `OPEN` means the required comparison is not yet demonstrated at RQIR precision. RQIR must remain separate from RTK/DSIR and no toy/resource result is an empirical new-physics claim.

## Programme channels

| Channel | Main observable | Main obstacle | Current strategy | Status |
|---|---|---|---|---|
| Q1 clocks | conditional phase/visibility | ordinary relativity + differential timing drift | profiled likelihood + TDEV/PSD controls | OPEN |
| Q2 superposed sources | potential/force/phase spectra | static-density blindness; tomography at complete history | finite NP3 + detector transfer | HIGH |
| Q3 source/backreaction | mean, noise, ordered/retarded response | source-amplitude degeneracy; calibration/control nuisance | joint source+calibration+detector Fisher + source metrology | HIGHEST |
| Q4 gravity-mediated QI | entanglement/non-Gaussianity | non-unique interpretation | common likelihood across interface classes | HIGH |
| Q5 geometry fluctuations | noise/response spectra | matter/intrinsic/technical degeneracy | joint covariance/response inference | HIGH |
| Q6 causal/process | relational timing/process observables | control-system confounds | nuisance-closed scaling tests | OPEN |
| Q7 low-energy QG EFT | long-range/nonanalytic corrections | tiny signals/local-UV degeneracy | cross-process fingerprints | OPEN |

## Current exact source/calibration baseline

Toy009 source radii:

`(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Iteration-011 practical calibration:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact rank `24/25`;
- positive source states;
- selected exact equality residual `<1e-15`;
- raw-row normalized `s_min~1.99954e-3`;
- condition `~2313`.

Toy009/Toy010 exact null/ordered-response results remain retained after all later resource corrections.

Primary statistical object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab = ||(I-P_J)s_tilde||^2`.

Exact rank/null geometry is not equivalent to statistical identifiability.

## Mandatory numerical/coordinate corrections

### RQIR-NUM-001 — hard constraints

Trace+energy must be eliminated analytically. The old huge-penalty + threshold-pseudoinverse implementation inflated weak-direction Fisher and the large Iteration-013/014 allocation gains were withdrawn.

### RQIR-NUM-002 — Fisher-coordinate Jacobian

Iteration 020 QFI is for the physical single-branch amplitude `a` in

`rho(a)=I/5+a Delta0`, `a=EPS=0.08`.

Later detector Fisher uses fractional hidden amplitude `alpha` with

`a=EPS alpha`.

Therefore

`F_Q^(alpha)=EPS^2 F_Q^(a)`.

Current values:

- `F_Q^(a)~=13.27068619` per ideal accepted single-branch copy;
- `F_Q^(alpha)~=0.0849323916`.

For normalized detector Fisher `S_D=1`, 90% isolated-amplitude retention needs `C_alpha=9`, corresponding to about `105.97` accepted single-branch copies or `52.98` independent plus/minus pair equivalents at the QFI bound.

For historical `S_D=25`, `C_alpha=225` requires about `2649.17` single-branch copies or `1324.58` pair equivalents.

The old `~17 copies for C_a=225` physical mapping is withdrawn for the current fractional-amplitude Fisher. The QFI formula itself remains correct.

Coordinate-correct preparation rate:

`R_P^(alpha)=p_P eta_P EPS^2 F_Q^(a)/t_P`

per single-branch cycle.

## Centered noise-kernel correction

RQIR physically targets centered symmetrized noise. For a symmetric state pair about `rho0=I/5`, the correct finite-noise covariance-difference derivative row is

`C_AB = sym(A,B) - <A>0 B - <B>0 A`

up to a trace-irrelevant identity term.

**RQIR-CAL-013 — centered-noise linearization:** raw second-moment rows are equivalent only under exact mean conditioning or if raw moments are explicitly the measured statistic.

Exact Toy009/Toy010 null geometry is unchanged:

- raw rank `24/25`;
- centered rank `24/25`;
- exact-null overlap `1.0` numerically.

Preferred normalized 90%-retention centered row weights (hard trace+energy basis):

- D1 `gamma_mean~1.26572e6`, `gamma_cov~0.621783e6`, allocation gain `~1.09308`;
- D2 `gamma_mean~1.83026e6`, `gamma_cov~0.590127e6`, allocation gain `~1.18719`.

Old Iteration-015 weights remain historical **raw-second-moment protocol** numbers, not the preferred centered-noise baseline.

## Retained structural gates

- **RQIR-NG-001:** static diagonal density can be phase blind.
- **RQIR-NG-002:** minimal ordered-response split has an energy confound.
- **RQIR-NG-003:** generic complete density history becomes tomography.
- **RQIR-NG-004:** one additional independent exact row kills a one-dimensional exact null.
- **RQIR-NG-005:** an exact gravitational null cannot self-calibrate the hidden source amplitude; independent source metrology is required.
- **RQIR-NG-006:** uncontrolled low-rank timing/geometry/additive systematics can remain detector-degenerate; exposure alone cannot cure them.
- **RQIR-NG-007:** a stability floor above the required prior cannot be fixed by faster white-noise averaging.
- **RQIR-NG-008:** SI additive tolerances require a physical transduction Jacobian.
- **RQIR-NG-010:** replacing a calibration observable may rotate rather than remove an exact detector-relevant null.
- **RQIR-NG-011:** detector-native force determines potential only relationally without an independent reference.
- **RQIR-NG-012:** information on one old hidden amplitude is insufficient for profiled beta identifiability if another detector-aligned null survives.
- **RQIR-NG-013:** force PSD + bandwidth do not determine source-covariance Fisher without `dS/du` / cross-spectral derivatives.
- **RQIR-NG-014:** current Toy009 covariance rows are nonstationary phase-referenced two-time observables; stationary scalar PSD rates cannot be assigned without a stationary/cyclostationary reduction.
- **RQIR-NG-015:** for noncommuting source observables, detector-output covariance is not automatically the source symmetrized operator correlator; measurement transfer/order/backaction must be explicit.

## Current centered first-order control requirements — Iteration 036

RQIR-NG-006 survives the centered correction: with no control priors, D1/D2 `F_beta|theta` remains numerical zero even at `100x` calibration exposure.

Centered-likelihood conservative control bundle:

### D1

- `sigma(delta tau)~6.94360e-3`;
- `sigma_t~11.0511 us` at 100 Hz;
- `sigma(b_mean)~8.88857e-5`;
- `sigma(b_cov)~1.26818e-4`;
- restored `F_beta|theta~0.899915`.

### D2

- `sigma(delta tau)~5.77425e-3`;
- `sigma_t~9.19001 us` at 100 Hz;
- `sigma(b_mean)~7.39168e-5`;
- `sigma(b_cov)~1.30175e-4`;
- restored `F_beta|theta~0.899893`.

Old `9.47 us` / `8.01 us` values are raw-second-moment historical benchmarks.

Transparent timing-drift benchmark (`sigma_event=10 us`, `sigma_ref=target/3`, acceptance `0.5`, current coherence floor, `1 ms` dead time):

- reference blocks: D1 `~0.131812 s`, D2 `~0.190604 s`;
- `D=100 us^2/h`: D1 `~2.17114 h`, D2 `~1.50145 h`;
- `D=1000 us^2/h`: D1 `~13.03 min`, D2 `~9.01 min`;
- equal-diffusion cadence ratio D2/D1 `~0.69155`.

## Detector/resource stack

D1 detector rate remains phase/interference based with contrast, lock-in/control window, acceptance, coherence and dead time. Coherence time is a hard per-shot lower bound and is not campaign wall-clock duration.

D2 detector rate remains force-domain/live-time based:

`R_D2 = eta_duty * 4 r2 r4/(r2+r4)`, `r_n=|Delta F_n|^2/S_F,n`.

No global D1/D2 ranking is allowed without one common apparatus/rate model.

## D2 branch status after centered correction

| Branch | Observable family | Hard rank | Current centered result | Status |
|---|---|---:|---|---|
| NP3-null | potential means + centered potential covariance | `22/23` on hard source tangent | hidden amplitude remains calibration-null | retained |
| Historical hybrid replacement | force means + old potential/raw covariance | `22/23` | Iteration-026/028 mixed protocol | retained only as labeled historical branch |
| Fully force-native centered | force means + centered force covariance | `22/23` | `F_beta(C_alpha=0,lambda=1)~0.019515`; `C_alpha90~7.78026` | current force-native baseline |
| Finite-reference relational centered | relational means + centered relational covariance | `22/23` | finite reference rotates but does not remove detector-relevant null | retained |
| Complementary centered | relational + force means with complementary centered covariance | `23/23` | at `y_ref=-4`, `F_beta(C_alpha=0,lambda=1)~0.905293` | highest D2 design priority, rate gate open |

At `y_ref=-4`, centered force-covariance row selection:

- 0 added: `F_beta~0.833432`, `C_alpha*=4.55511`;
- best 4 `(0,1,3,7)`: `F_beta~0.899477`, `C_alpha*=0.0500614`;
- best 5 `(0,1,3,6,7)`: `F_beta~0.903527`, `C_alpha*=0`.

Equal-row local preparation-substitution thresholds:

- first four: `q_cov/R_P^(alpha) > ~5.24e5`;
- fifth after first four: `> ~1.18e7`.

## Nonstationary covariance measurement rate — Iteration 035

Current hidden states have

`||[rho_+,H]||_F=||[rho_-,H]||_F~0.240672`.

A common time shift changes the probe-0 centered force covariance substantially, so the current rows are not stationary PSD coordinates.

The high-value rows `(0,1,3,7)` also involve noncommuting source-operator pairs.

Preferred apparatus-neutral rate for one real Gaussian phase-referenced detector-output sample:

`I_ij^(shot) = (d_i mu)^T Sigma^-1(d_j mu) + 1/2 Tr[Sigma^-1 Sigma_,i Sigma^-1 Sigma_,j]`,

`q_ij = p_C eta_C I_ij^(shot)/t_C`.

**RQIR-RESOURCE-012:** use the Fisher rate of the actual phase-referenced/cyclostationary detector-output likelihood. Stationary PSD Fisher is a special case only after its assumptions are demonstrated.

Coordinate-correct equal-row break-even becomes:

- first four: `I_cov^(shot)*(pC etaC/pP etaP)*(tP/tC) > ~4.4502e4`;
- fifth: `> ~1.0012e6`.

## Publication architecture (fixed for future drafting)

See `docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`.

Planned logical series:

1. RQIR I — operational hierarchy / ordered source information / finite discriminants;
2. RQIR II — statistical identifiability / nuisance geometry / source calibration;
3. RQIR III — physical resources / experimental architecture;
4. later candidate-gravity paper only after a concrete model passes the reconstruction gates.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy; G13 detector covariance/nuisance/measurability.

## Priority ranking v2.0

1. Build a phase-referenced repeated-shot or cyclostationary D2 detector-output likelihood for high-value centered covariance rows `(0,1,3,7)`.
2. Derive row-specific covariance transduction and detector-output `Sigma_,i`, including imprecision, backaction and cross-noise; obtain physical `q_i`.
3. Test the `~4.45e4` first-four resource product against coordinate-correct source metrology `R_P^(alpha)` and centered timing/additive priors.
4. Optimize full D2 wall-clock cost over `(y_ref,lambda,C_alpha,covariance subset)` on the corrected centered likelihood.
5. Revalidate second-order timing/gain bias only if it becomes competitive with the covariance-rate gate.
6. Build a common D1/D2 resource budget at one source mass, gap, coherence, separation and campaign duration.
7. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.
8. Close conservation, gauge, renormalization and full-stress-energy gates after detector/inference geometry stabilizes.
