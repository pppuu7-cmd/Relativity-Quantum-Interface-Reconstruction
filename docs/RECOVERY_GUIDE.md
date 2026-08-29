# RQIR Recovery Guide

**Last updated:** 2026-08-29  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v2.6

This is the continuity backbone. The repository, not chat history, is authoritative. Do not mix RQIR with RTK or DSIR. No toy/resource/detector result is an empirical new-physics claim.

## 1. Objective and discipline

RQIR reconstructs the operational interface between relativity/gravity and quantum physics without assuming in advance whether gravity is classical, stochastic, quantized, hybrid, emergent or UV-completed in any preferred way.

Central inverse problem:

`P_data(o|s) -> [interface class]`.

Mandatory rules:

- observable first;
- explicit baseline/domain;
- preserve operator ordering;
- source response is not detector observability;
- exact rank/null is not statistical identifiability;
- use exact hard constraints;
- compare Fisher/QFI/rates only in one physical parameter coordinate;
- use centered noise, not raw second moments, unless raw moments are explicitly measured;
- distinguish stationary PSD from phase-referenced/cyclostationary likelihoods;
- include source preparation, calibration, detector, controls, backaction and wall clock in one chain;
- preserve negative/correction results;
- no new-physics interpretation before consistency and competitor-degeneracy gates close.

## 2. Ordered source hierarchy

At second order use

`K_T^(2)=(<T>,N,D or chi^R)`

with centered symmetrized noise `N`, commutator/ordered response `D`, and retarded susceptibility `chi^R`. Parent object: Schwinger–Keldysh / CTP generating functional.

Highest-priority working channel remains Q3 source/backreaction, with Q2/Q5/Q4 cross-checks.

## 3. Exact Toy009/Toy010 baseline

Current Toy009 source radii:

`(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Balanced Iteration-011 calibration geometry:

- second probe `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact rank `24/25`;
- positive hidden-pair states;
- selected equality residual `<1e-15`.

Toy009/Toy010 exact mean/noise equality and ordered-response split remain retained.

Toy009 design rule: optimize the whole chain

`source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> F_beta|theta`.

Toy010 design rule: finite calibration geometry actively steers the hidden null direction.

## 4. Statistical identifiability

Primary inference quantity:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

RQIR-NG-005: if the calibration leaves hidden direction `n` exact-null and detector signal is locally `mu_D=beta*a*s`, gravitational null calibration cannot self-calibrate `a`; without independent source metrology, local `F_beta|a=0`.

Independent source metrology is required unless complementary calibration removes the detector-relevant null.

## 5. Mandatory corrections

### RQIR-NUM-001 — exact constraints

Trace+energy must be eliminated analytically by a reduced/nullspace basis. The old `1e12` Fisher penalty + threshold pseudoinverse truncated weak physical nuisance directions and inflated Fisher. Large Iteration-013/014 allocation gains are withdrawn.

### RQIR-NUM-002 — Fisher-coordinate Jacobian

Iteration 020 QFI is for physical amplitude `a` in

`rho(a)=I/5+a Delta0`, nominal `a=0.08`.

Current detector Fisher uses fractional amplitude `alpha` with

`a=0.08 alpha`.

Therefore

`F_Q^(alpha)=0.08^2 F_Q^(a)`.

Current values:

- `F_Q^(a)=13.27068619`;
- `F_Q^(alpha)=0.0849323916` per ideal accepted single-branch copy.

The old downstream `~17 copies for C_a=225` mapping is withdrawn.

### RQIR-CAL-013 — centered noise

For a symmetric state pair about `rho0=I/5`, use

`C_AB=sym(A,B)-<A>0 B-<B>0 A`

on the trace-zero tangent.

Exact Toy009/Toy010 nullspace is unchanged.

Preferred centered 90%-retention row weights:

- D1 `gamma_mean~1.266e6`, `gamma_cov~0.622e6`;
- D2 `gamma_mean=1.830264703e6`, `gamma_cov=5.901272925e5`.

## 6. Controls, timing and coherence

RQIR-NG-006 survives centered correction: without independent timing/geometry/additive priors, D1/D2 profiled Fisher remains numerical zero even at `100x` calibration exposure.

At 100 Hz:

- D1 timing target `~11.0511 us`;
- D2 timing target `~9.19001 us`;
- D2 normalized additive targets `sigma(b_mean)~7.39168e-5`, `sigma(b_cov)~1.30175e-4`.

Largest stored phase gives

`T_coh,min=4.99085067/(2 pi f_gap)`;

at 100 Hz: `~7.94319 ms`.

RQIR-NG-007: a low-frequency stability floor above the target prior cannot be repaired by faster white averaging.

## 7. Current centered D2 Fisher front

At finite reference `y_ref=-4`, `lambda=1`:

- 0 added force-cov rows: `F_beta~0.833432`, `C_alpha*=4.55511`;
- best4 `(0,1,3,7)`: `F_beta~0.899477`, `C_alpha*=0.05006144`;
- best5 `(0,1,3,6,7)`: `F_beta~0.903527`, `C_alpha*=0`;
- all8: `F_beta~0.905293`, `C_alpha*=0`.

Retain:

- NG-010 observable replacement can rotate, not remove, a detector-relevant null;
- NG-011 force gives potential only relationally without reference;
- NG-012 information on one old amplitude is not enough if another detector-aligned null survives.

## 8. Covariance measurement gates

Current Toy009 hidden states are nonstationary; high-value covariance pairs involve noncommuting source operators.

- **NG-014:** current covariance rows are phase-referenced two-time observables, not stationary scalar PSD coordinates.
- **NG-015:** detector-output covariance is not automatically the source symmetrized operator covariance; transfer/order/backaction must be explicit.

Preferred one-shot Gaussian output Fisher:

`I_ij=(d_i mu)^T Sigma^-1(d_j mu)+1/2 Tr[Sigma^-1 Sigma_,i Sigma^-1 Sigma_,j]`.

Physical rate:

`q_ij=p_C eta_C I_ij/t_C`.

- **NG-016:** one affine covariance coordinate in `m` Gaussian outputs has `I_shot<m/2` over the full allowed amplitude range.
- **NG-017:** several covariance coordinates share a finite matrix-Fisher budget.
- **RESOURCE-013:** shared shots require full matrix Fisher, not summed row times.
- **CAL-014:** covariance source directions should be Fisher-orthogonal to dominant detector-noise nuisance directions.

## 9. Covariance graph congestion

Natural best4 cross-covariance encoding uses six unique endpoints and gives per-row Fisher `<1/2`.

Trajectory lower bounds:

- best4 `N>1.180254e6`;
- best5 `N>2.135100e6`;
- all8 `N>3.540762e6`.

**RQIR-RESOURCE-015:** adding a covariance row can increase endpoint-graph spectral radius and reduce per-shot information of the whole shared set.

## 10. Mean compatibility and conservative scheduling

The 14 current D2 force-mean operators have 91 pairs:

- 7 commuting same-time two-probe pairs;
- 84 noncommuting cross-time pairs.

Also `G0,G1` are not QND with respect to source `H`.

**NG-019:** seven phase settings cannot be credited as one disturbance-free source measurement.

**CAL-015:** same-time dual probes can be paired; this is the maximal disturbance-free grouping of the 14 current mean rows.

**RESOURCE-016:** one physical cycle counts simultaneously toward mean/covariance/control only if one declared likelihood supplies all score vectors, correlations and backaction.

**RESOURCE-017:** independent phase layers pay `sum_j t_j`, not `7*t_max`, and do not reuse one noncommuting source copy.

Transparent `100 Hz`, `p=.5`, `dead=1 ms` parallel dual-probe mean campaign:

- xi=1 -> `45.09 h`;
- xi=2 -> `11.27 h`;
- xi=3 -> `5.01 h`;
- xi=5 -> `1.80 h`.

Mean equals best4 covariance floor near `xi_mu=2.7728`.

## 11. Information/backaction chain — Iterations 043–046

Direct diffusive reference:

`xi_mu^2=4 eta kappa T`, `zeta=xi_mu^2/(4 eta)`.

At ideal efficiency:

- xi=1.245286 -> response norm `~0.856964`;
- xi=2.772804 -> response norm `~0.493450`.

**NG-020:** resource-competitive direct non-QND monitoring is not perturbatively free.

**RESOURCE-018:** detector efficiency is a coherence/backaction resource, not only a time penalty.

### Reciprocal linear probe — NG-021

For

`x_p=chi_p(g u+F_BA)`, `y=x_p+x_imp`,

and detector noise satisfying

`S_xx S_FF-S_xF^2 >= hbar^2/(4 eta)`,

source-referred noise obeys

`S_u S_BA,src >= hbar^2/(4 eta)`.

Coupling and probe susceptibility cancel. Correlated/variational readout can saturate but not beat the reciprocal product.

To retain 90% raw detector signal Fisher at eta=1, require

`xi_shared<=0.723982`, `I_shared<=0.5241495`.

### Full profiled backaction — NG-022 / RESOURCE-020

Transforming the complete detector/nuisance Jacobian through the same dephasing proxy tightens the current `lambda=1` strong-preparation limit to

`xi_shared<=0.700101`, `I_shared<=0.490142`.

Across best4 trajectories this can cover at most `~31.61%` of centered `gamma_mean` even with perfect source-amplitude metrology.

At fixed lambda=1, required `C_alpha90` rises rapidly and diverges near xi~.7001. Keeping baseline `C_alpha=0.05006144` instead requires calibration scale growing from ~1.02 at xi=.1 to ~3.11 at .6, ~8.19 at .68 and ~14.78 at .70.

**RESOURCE-020:** shared mean Fisher, source metrology and calibration exposure form a three-way backaction compensation frontier.

The older optimistic shared target xi=1.245 and crossover xi=2.773 are absolutely incompatible with a 90% target in this reciprocal-linear/dephasing proxy because detector-only beta Fisher is already below .9.

## 12. QND energy-basis source metrology — Iteration 047

Toy009 `H` is nondegenerate, so exact Hermitian QND observables are energy-diagonal. After trace+energy removal the hard QND sector is three-dimensional.

At `y_ref=-4`, relational hard rank is `22/23`; adding a complete three-row diagonal QND basis gives `23/23`.

**CAL-016:** the current relational null is locally visible to the QND diagonal sector.

Simple projective energy-population metrology gives

- `F_E^alpha(+)=0.0093918844`;
- `F_E^alpha(-)=0.0095791291`;
- pair `=0.0189710135`.

A plus-branch energy measurement extracts about `11.1%` of full Toy009 QFI per copy.

**PREP-002:** the ideal Delta0 eigenbasis is not the only useful source-metrology channel.

Current best4 residual `C_alpha=0.05006144` needs only about `5.33` accepted plus copies or `2.64` pair equivalents at ideal energy-population Fisher.

However, full projective energy dephasing on the same science copy leaves only `~0.29848` of D2 response norm.

**NG-023:** QND relative to `H` is not equivalent to ordered-response nondemolition. Use strong energy/population metrology on independent/sacrificial copies.

## 13. Explicit energy-metrology phase diagram — Iteration 048

Use

`F_E^alpha=0.0093918844`

per accepted plus-branch copy.

Source-amplitude closure costs:

- branch0 (no added force-cov): `C_alpha=4.55511` -> `~485.00` energy copies;
- best4: `N4=1.180254e6` covariance trajectories + `~5.33` energy copies;
- best5: `N5=2.135100e6`, no source prior.

Define

`x_E=(p_C eta_C)/(p_E eta_E) * t_E/t_C`.

**RESOURCE-021 — explicit source-metrology branch phase diagram**

- `x_E<2460.53`: branch0 + energy metrology wins;
- `2460.53<x_E<1.79136e5`: best4 + tiny energy metrology wins;
- `x_E>1.79136e5`: best5 wins.

At equal efficiency, 100 Hz and 1 ms covariance readout overhead:

- branch0/best4 boundary: `t_E~22.0 s`;
- best4/best5 boundary: `t_E~26.7 min`.

Therefore the next key experimental input is the actual energy/population metrology rate. If one accepted source-metrology cycle is faster than ~22 s in this benchmark, even best4 covariance is not wall-clock optimal for source-amplitude closure.

## 14. Current working D2 architecture

Do not freeze the experiment to best4 covariance yet.

Keep two active leading branches:

1. **branch0 + independent energy-basis source metrology** if source energy/population readout is relatively fast;
2. **best4 + tiny energy metrology** if source readout is intermediate.

Best5 is only favored when source metrology is very slow.

Strong same-copy mean monitoring remains disfavored in the generic reciprocal linear class. Independent/sacrificial seven-layer mean calibration remains the conservative baseline.

## 15. Publication architecture

Fixed in `docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`:

1. RQIR I — operational hierarchy / ordered source information / finite discriminants;
2. RQIR II — statistical identifiability / nuisance geometry / source calibration;
3. RQIR III — physical resources / experiment architecture;
4. later Candidate Gravity paper only after a concrete model passes the reconstruction gates.

## 16. Mandatory open consistency gates

G1 gauge/relational observables; G2 source+apparatus conservation/Bianchi; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a semiclassical/stochastic/classical-gravity+full-QFT/quantum degeneracy; G13 detector covariance/nuisance/measurability.

## 17. Current priority — v2.6

P1. Build a minimally physical **energy/population source-metrology protocol** and estimate `t_E,p_E,eta_E`; determine which side of the ~22-s branch0/best4 boundary the intended source lies on.

P2. Keep independent/sacrificial seven-layer force-mean calibration as the backaction-safe baseline and attach physical force transduction/SNR.

P3. Recompute total wall clock for branch0 vs best4 including common mean calibration, timing/additive controls, science integration and source reset/preparation.

P4. Pursue shared strong science monitoring only if a concrete QND/backaction-evading, nonreciprocal, coherent-noise-cancellation or ancilla architecture explicitly changes an assumption of NG-021/022.

P5. Build one common D1/D2 apparatus budget at fixed source mass, gap, coherence and separation.

P6. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood before interpretation as new physics.

P7. After detector/inference geometry stabilizes, close gauge, conservation, renormalization and full stress-energy gates.

## 18. Continuation protocol

At every substantive iteration:

1. read `RECOVERY_GUIDE.md`, `MASTER_TABLE.md`, latest research log, Toy009/Toy010 and Statistical Identifiability docs;
2. repo is source of truth;
3. do not duplicate closed/active calculations without reason;
4. derive before adding numerical complexity;
5. preserve exact hard constraints and coordinate consistency;
6. distinguish raw/centered, stationary/phase-referenced and same-copy/independent-copy resources;
7. propagate measurement backaction through detector/nuisance geometry before crediting shared Fisher;
8. save reproducible code, main document, research log and recovery delta;
9. do not claim new physics before consistency/degeneracy/experimental gates close.
