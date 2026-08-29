# RQIR Operational Master Table

**Version:** 1.8  
**Date:** 2026-08-29

The repository is authoritative. `OPEN` means the required comparison is not yet demonstrated at RQIR precision.

| Channel | Main observable | Main obstacle | Current strategy | Status |
|---|---|---|---|---|
| Q1 clocks | conditional phase/visibility | ordinary relativity + differential timing drift | profiled likelihood + TDEV/PSD controls | OPEN |
| Q2 superposed sources | potential/force/phase spectra | static-density blindness; tomography at complete history | finite NP3 + detector transfer | HIGH |
| Q3 source/backreaction | mean, noise, ordered/retarded response | source-amplitude degeneracy; calibration/control nuisance | joint source+calibration+detector Fisher + source metrology | HIGHEST |
| Q4 gravity-mediated QI | entanglement/non-Gaussianity | non-unique interpretation | common likelihood across interface classes | HIGH |
| Q5 geometry fluctuations | noise/response spectra | matter/intrinsic/technical degeneracy | joint covariance/response inference | HIGH |
| Q6 causal/process | relational timing/process observables | control-system confounds | nuisance-closed scaling tests | OPEN |
| Q7 low-energy QG EFT | long-range/nonanalytic corrections | tiny signals/local-UV degeneracy | cross-process fingerprints | OPEN |

## Current baseline

Toy009 source radii: `(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Iteration-011 practical calibration:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- rank `24/25`;
- `eta_R~0.573426`;
- `s_min~1.99954e-3`;
- condition `~2313`.

Primary inference coordinate:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab = ||(I-P_J)s_tilde||^2`.

Exact null rank is not equivalent to statistical identifiability.

## Mandatory correction retained

**RQIR-NUM-001:** trace+energy constraints must be removed analytically through a hard-constrained basis. The earlier huge-penalty+pseudoinverse method inflated Fisher.

Corrected 90%-retention row weights:

- D1 `gamma_mean~1.722e6`, `gamma_cov~0.938e6`;
- D2 `gamma_mean~2.414e6`, `gamma_cov~0.929e6`.

Large Iteration-013/014 allocation gains are withdrawn; corrected gains are only about `x1.07` D1 and `x1.14` D2.

## Retained structural gates

- **RQIR-NG-005:** an exact gravitational null cannot self-calibrate the hidden-source amplitude; without independent source metrology, local `F_beta|a=0`.
- **RQIR-NG-006:** uncontrolled timing/geometry/additive systematics can remain detector-degenerate; exposure alone cannot cure them.
- **RQIR-NG-007:** a stability floor above the required prior cannot be fixed by faster white-noise averaging.
- **RQIR-NG-008:** SI additive tolerances require a physical transduction Jacobian.
- **RQIR-NG-010:** replacing a calibration observable may rotate rather than remove an exact detector-relevant null.
- **RQIR-NG-011:** detector-native force determines potential only relationally without an independent reference.
- **RQIR-NG-012:** information on one old hidden amplitude is not sufficient for profiled beta identifiability if another detector-aligned null survives.

## Physical resource stack

- D1 uses a phase/interference Fisher-rate model with contrast, control window, acceptance, coherence and dead time.
- D2 uses a force-PSD/live-time model `R_D2=eta_duty*4 r2 r4/(r2+r4)`.
- Source preparation has `F_Q(a~0.08)~13.2707` per ideal accepted copy and rate `R_P=p_P eta_P F_Q/t_P`.
- Differential timing priors are about `9.47 us` D1 and `8.01 us` D2 at 100 Hz.
- Long-run timing is controlled by measured differential TDEV/PSD and recertification duty, not single-event jitter alone.
- Finite-reference potential transduction obeys `q_pot=2||Delta B||^2/(L^2 S_F)` and has a reference-distance cost/geometry tradeoff.

## D2 branch table after Iteration 032

| Branch | Observable family | Hard rank | Current result | Status |
|---|---|---:|---|---|
| NP3-null | original potential means + original covariance | `22/23` | hidden amplitude remains calibration-null | retained |
| Hybrid replacement | force means + old potential covariance | `22/23` | old Iteration-026/028 branch; null remains | retained, relabeled hybrid |
| Fully force-native | force means + force covariance | `22/23` | `F_beta(C_a=0,lambda=1)~0.019445`; `C_a*~8.29464` | current native-force baseline |
| Finite-reference relational | potential differences + relational covariance | `22/23` | old amplitude becomes partly visible but a new detector-aligned null remains | retained |
| Complementary relational+force | relational potential + force, with complementary covariance | `23/23` | nearly 90% at current scale; physical covariance cost still open | highest D2 design priority |

### Iteration 032

**RQIR-CAL-011 — observable-family consistency:** detector-native means and covariance/noise calibration must be derived from the same declared physical observable family, unless the branch is explicitly hybrid.

Fully force-native result:

- exact null overlap with old hidden direction `~0.95003346`;
- detector alignment `~0.99003961`;
- `F_beta(C_a=0,lambda=1)~0.0194450`;
- `C_a*~8.29464` for 90% at `lambda=1`;
- with strong source metrology, 90% threshold `lambda~0.1537665`.

Complementary branch at `y_ref=-4` with relational + force means and both covariance families:

- rank `23/23`;
- `F_beta(C_a=0,lambda=1)~0.8994327`;
- `C_a*~0.06708` for 90% at `lambda=1`;
- calibration-only 90% at `lambda~1.00632`.

The best four added force-covariance rows are `(0,1,3,7)`, yielding `F_beta~0.894857`, `C_a*~0.58896`, and calibration-only 90% at `lambda~1.05755`.

**RQIR-CAL-012 — covariance complementarity:** a targeted covariance subset can remove most of the remaining detector-relevant nuisance penalty. Covariance-row choice is an active design/resource variable.

The old Iteration-028 phase diagram is therefore valid for its declared mixed protocols but is not yet the final fully physical D2 resource map.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 Newtonian-limit control; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy; G13 detector covariance/nuisance/measurability.

No current toy/resource result is an empirical new-physics claim.

## Priority ranking v1.8

1. Derive physical Fisher rates for **force covariance** and **finite-reference relational covariance** from one common D2 PSD/bandwidth/duty model.
2. Optimize D2 wall-clock cost over `(y_ref,lambda,C_a,covariance subset)` and compare fully force-native vs complementary branches.
3. Add measured differential timing/reference recertification duty to the same `F_beta|theta/T_wall` objective.
4. Build a common D1/D2 resource budget at one source mass, gap, coherence, separation and campaign duration.
5. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.
6. Close conservation, gauge, renormalization and full-stress-energy gates after detector/inference geometry stabilizes.
