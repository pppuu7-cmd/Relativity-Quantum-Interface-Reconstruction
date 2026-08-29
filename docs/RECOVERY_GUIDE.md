# RQIR Recovery Guide

**Last updated:** 2026-08-30  
**Project:** Relativity–Quantum Interface Reconstruction (RQIR)  
**Current operational framework:** v2.8

This is the continuity backbone. The repository, not chat history, is authoritative. Do not mix RQIR with RTK or DSIR. No toy/resource/detector result is an empirical new-physics claim.

## 1. Objective and discipline

RQIR reconstructs the operational gravity–quantum interface without assuming in advance whether gravity is classical, stochastic, quantized, hybrid, emergent or described by a preferred UV theory.

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
- include spatial locality as a source-design constraint when a toy source is interpreted physically;
- preserve negative/correction results;
- no new-physics interpretation before classical/stochastic/full-QFT/hybrid degeneracy and relativistic consistency gates close.

## 2. Ordered source hierarchy

At second order use

`K_T^(2)=(<T>,N,D or chi^R)`

with centered symmetrized noise `N`, commutator/ordered response `D`, and retarded susceptibility `chi^R`. Parent source object: Schwinger–Keldysh / CTP generating functional.

Highest-priority working channel remains Q3 source/backreaction, with Q2/Q5/Q4 cross-checks.

## 3. Mature Toy009/Toy010 exact baseline

Toy009 radii:

`(1.00000,1.60090005,1.77911036,2.60900799,5.90723562)`.

Balanced Iteration-011 geometry:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact rank `24/25`;
- positive hidden pair;
- selected equality residual `<1e-15`.

Toy009/Toy010 exact mean/noise equality and ordered-response split remain retained after all later statistical/resource/locality corrections.

Core design lesson:

`source -> calibration/Fisher geometry -> gravity transfer -> detector/noise -> F_beta|theta`.

Finite calibration geometry actively steers the hidden direction.

## 4. Statistical identifiability

Primary inference quantity:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

RQIR-NG-005: if calibration leaves hidden direction `n` exact-null and detector signal is locally `mu_D=beta*a*s`, gravitational null calibration cannot self-calibrate the hidden source amplitude. Independent source metrology or genuinely complementary calibration is required.

## 5. Mandatory corrections

### RQIR-NUM-001 — exact constraints

Trace+energy must be eliminated analytically through a reduced/nullspace basis. Old huge-penalty + threshold-pseudoinverse calculations inflated Fisher by deleting weak physical nuisance directions.

### RQIR-NUM-002 — source-amplitude coordinate

Current detector Fisher uses fractional amplitude `alpha` with

`a=0.08 alpha`.

Therefore

`F_Q^(alpha)=0.08^2 F_Q^(a)`.

Toy009 full QFI:

`F_Q^alpha=0.0849323916` per ideal accepted single-branch source copy.

### RQIR-CAL-013 — centered noise

For symmetric perturbations about `rho0=I/5`, finite-noise covariance derivative is

`C_AB=sym(A,B)-<A>0 B-<B>0 A`

on the trace-zero tangent.

Toy009 centered D2 weights:

- `gamma_mean=1.830264703e6`;
- `gamma_cov=5.901272925e5`.

## 6. Controls and coherence

RQIR-NG-006 survives centered correction: without independent timing/geometry/additive priors, D1/D2 profiled Fisher remains near zero even with very large exposure.

At 100 Hz Toy009 benchmark:

- D1 timing target `~11.0511 us`;
- D2 timing target `~9.19001 us`;
- D2 `sigma(b_mean)~7.39168e-5`;
- D2 `sigma(b_cov)~1.30175e-4`.

RQIR-NG-007: a low-frequency stability floor above target cannot be repaired by faster white-noise averaging.

Toy009 current coherence floor from the largest phase is `~7.94319 ms` at 100 Hz.

## 7. Toy009 complementary D2 reference branch

At `y_ref=-4`, centered likelihood and `lambda=1`:

- no added force cov: `F_beta~0.833432`, `C_alpha*=4.55511`;
- best4 `(0,1,3,7)`: `F_beta~0.899477`, `C_alpha*=0.05006144`;
- best5 `(0,1,3,6,7)`: `F_beta~0.903527`, `C_alpha*=0`;
- all8: `F_beta~0.905293`, `C_alpha*=0`.

Natural Gaussian covariance graph floors:

- best4 `>1.180254e6` accepted trajectories;
- best5 `>2.135100e6`;
- all8 `>3.540762e6`.

Retain:

- NG-010 null rotation;
- NG-011 finite-reference/integration-constant obstruction;
- NG-012 old-amplitude information is not full profiled identifiability;
- RESOURCE-015 covariance graph congestion.

## 8. Covariance measurement gates

Current two-time covariance observables are nonstationary and may involve noncommuting source operators.

- **NG-014:** stationary PSD rates are not directly valid without a stationarity/cyclostationarity derivation.
- **NG-015:** detector-output covariance is not automatically source symmetrized covariance; ordering/transfer/backaction must be explicit.
- **NG-016/017:** finite-dimensional affine Gaussian covariance measurements have positivity-limited per-shot/matrix Fisher budgets.
- **NG-018:** actual shared endpoint graph can tighten per-row Fisher further.
- **RESOURCE-013:** shared covariance shots require full matrix Fisher, not summed independent row times.
- **CAL-014:** covariance signal directions should be Fisher-orthogonal to dominant detector-noise nuisances where physically possible.

## 9. Mean compatibility and backaction — Iterations 041–046

The 14 force-mean operators have 91 pairs:

- 7 commuting same-time dual-probe pairs;
- 84 noncommuting cross-time pairs.

They are not QND with respect to the source Hamiltonian.

- **NG-019:** multitime force calibration cannot be credited as one disturbance-free source trajectory.
- **CAL-015:** same-time dual probes are the maximal disturbance-free grouping in current toys.
- **RESOURCE-016:** shared trajectory Fisher credit is valid only from one declared physical likelihood containing all scores/cross-Fisher/backaction.
- **RESOURCE-017:** independent phase layers pay their own evolution/coherence times.

Reciprocal linear detector:

`S_u S_BA,src >= hbar^2/(4 eta)`.

- **NG-021:** gain/probe susceptibility cannot beat this input-referred reciprocal product.
- **NG-022:** full nuisance profiling tightens the safe shared-information limit beyond raw signal attenuation.

Toy009 at lambda=1 allows at most about `xi_shared~0.7001` in the optimistic proxy for 90% final profiled Fisher; this is only ~31.6% of current mean Fisher across best4 trajectories.

**RESOURCE-020:** shared mean Fisher, independent source metrology and calibration exposure form a three-way backaction frontier.

## 10. Independent QND source metrology — Toy009

Because Toy009 `H` is nondegenerate, exact H-QND Hermitian observables are energy diagonal.

Projective energy-population metrology:

`F_E^alpha(+)=0.0093918844`.

This is ~11.1% of full Toy009 QFI. However same-copy projective energy dephasing leaves only ~0.2985 of D2 response norm.

- **PREP-002:** simple energy populations already carry finite hidden-amplitude information.
- **NG-023:** QND with respect to `H` is not ordered-response nondemolition; strong energy metrology belongs on independent/sacrificial copies.

Finite Gaussian pointer:

- weak Fisher `~O(r^4)` due exact trace+mean-energy matching (**NG-024**);
- Toy009 zero-reset Fisher-rate coefficient `R/(p eta kappa_E)=0.0082700957`.

Ramsey ancilla:

- per-copy optimum differs from Fisher/sec optimum;
- Toy009 zero-reset rate optimum `phi~1.09231`;
- `R/(p Omega_E)=0.0025234392`.

**RESOURCE-024:** maximize Fisher per wall time, not per accepted copy.

## 11. Locality audit and Toy011 — Iterations 053–054

Literal Toy009 radius-basis Hamiltonian is dense:

- ~64.46% of off-diagonal coupling power lies beyond nearest neighbours;
- naive nearest-neighbour truncation changes H by relative Frobenius ~0.369 and shifts spectrum.

**NG-025:** spatial locality cannot be imposed reliably after optimizing an abstract source.

Toy011 uses exact-spectrum Jacobi/Lanczos nearest-neighbour chains and proves a positive existence result:

`local nearest-neighbour H + exact NP3 rank 24/25 + positive hidden states + nonzero ordered response`.

First Toy011 points were resource-poor:

- response point: D2 raw signal `0.1707` Toy009, D2 calibration cost `34.6x`;
- conditioning point: D2 raw `0.0842`, cost `10.1x`.

But full QFI stayed close to Toy009 and `C_alpha(lambda)` nuisance structure remained similar.

**RESOURCE-025:** source locality creates a multi-resource tradeoff, not an automatic identifiability failure.

## 12. Toy012 — resource-aware local co-design / canonical Iteration 055

Canonical numbering: **Iteration 055 = Toy012**. Ramsey reset/visibility was reindexed to Iteration 056.

Balanced Toy012 geometry:

- `q0=(0.182446543760,0.684368939221,0.165591352865,0.679324856717,0.097209344214)`;
- `y1=-2.94878656991`;
- phases `(0,1.038867458294,2.985962997881,4.875819177097,4.150899563476,1.623915172581,5.275220686287)`.

Properties:

- exact nearest-neighbour site Hamiltonian, spectrum `(1,2,3,4,6)`;
- rank `24/25`;
- `s_min=1.43254596e-3`, condition `~3264.22`;
- positive states, equality residual `<6e-17`.

Relative to Toy009:

- D1 raw detector Fisher `0.17042`;
- D2 raw detector Fisher `0.21617`;
- D1 centered calibration cost `1.515x`;
- D2 centered calibration cost `1.058x`;
- `F_Q^alpha=0.0992807` (`1.169x`);
- energy-population Fisher `0.00629727` (`0.671x`);
- Ramsey zero-reset Fisher-rate coefficient `0.00213429` (`0.846x`).

**DESIGN-003:** large Toy011 calibration penalties were objective-dependent. Exact nearest-neighbour dynamics can coexist with near-Toy009 nuisance-calibration efficiency. The main remaining local penalty is absolute detector signal.

Toy012 is the leading locality-constrained source; Toy009 remains the mature global baseline until detector/systematic rebuilding is complete.

## 13. Iteration 056 — reset/visibility source-metrology surface

For independent Ramsey metrology:

`R_alpha(phi)=p_E F_alpha(phi,V)/(t_reset+phi/Omega_E)`.

**RESOURCE-026:** fresh-source reset/preparation overhead is a first-class Fisher resource and shifts both the optimal phase and branch winner.

Historical Toy009 branch rate thresholds:

- branch0↔best4 `2.1340355e-4 s^-1`;
- best4↔best5 `2.9312162e-6 s^-1`.

These numbers belong to Toy009 and must not be imported into Toy012 without its own branch profiling.

## 14. Toy012 complementary D2 — Iteration 057

Balanced Toy012 centered D2 NP3 weights:

- `gamma_mean=1.2086865e6`;
- `gamma_cov=1.8994980e6`.

At common `y_ref=-4`, relational means + direct force means + centered relational covariance already have hard rank `23/23` with smallest hard singular value `~1.7141e-3`.

Yet

`F_beta|theta(C_alpha=0,lambda=1)=0.194405`.

**NG-026:** hard rank completion is not finite-noise/resource closure.

Minimum source prior needed for 90% at lambda=1:

- k0 force-cov: `C_alpha=13.669415`;
- k1 `(1)`: `13.135585`;
- k2 `(1,3)`: `12.309076`;
- k3 `(1,3,5)`: `12.152511`;
- k4 `(1,3,4,5)`: `12.097052`;
- k5 `(0,1,3,4,5)`: `12.009588`;
- all8: `11.891638`.

Toy009's dramatic best4 covariance closure does not transfer.

**DESIGN-004:** complementary covariance geometry is source-specific and must be co-designed with the source Hamiltonian/hidden direction.

At y_ref=-4, best4 `(1,3,4,5)`:

- graph `rho^2=2`;
- natural covariance lower bound `N>3.798996e6`;
- saves only `Delta C_alpha~1.57236`;
- at 100 Hz, p=.5, 1 ms overhead, lower-bound time `~19.83 h`;
- source-metrology break-even `R_alpha~2.20253e-5 s^-1`.

Therefore current leading Toy012 architecture does **not** inherit Toy009's force-covariance bundle by default.

## 15. Toy012 pointer vs Ramsey reset surface — Iteration 058

Use the Iteration-057 source-metrology target

`R_alpha*=2.2025279e-5 s^-1`.

### Gaussian pointer

- `F_E^alpha=0.00629727076` projective ceiling;
- zero-reset optimum `r~1.44273`;
- `R/(p Gamma_E)=0.00425193299`;
- at `p=.5`, zero-reset `Gamma_E~0.01036 s^-1`.

### Ramsey

- zero-reset optimum `phi~1.57508`;
- `R/(p Omega_E)=0.00213429284`;
- per-copy max `F_R,max=0.00349867283`;
- at `p=.5`, zero-reset `Omega_E~0.02064 s^-1`.

Do not equate `Gamma_E` and `Omega_E`; they are protocol-specific coupling normalizations.

### RQIR-RESOURCE-027 — hard reset ceiling

For any independent fresh-copy source metrology,

`R_alpha <= p_E F_max/t_reset`.

At p=.5 and current Toy012 target:

- pointer reset ceiling `~142.96 s`;
- Ramsey reset ceiling `~79.42 s`.

Beyond these limits no coupling strength can make that protocol beat Toy012 best4 in the current source-amplitude-only comparison.

**PREP-004:** fresh-copy throughput is an architecture variable.

## 16. Current architecture / baseline decisions

### Mature statistical baseline

Keep **Toy009** as the reference for established D1/D2 detector/systematic machinery.

### Leading locality-constrained physical source

Use **Toy012 balanced**.

### Current Toy012 D2 source-amplitude route

Prefer

`Toy012 + relational/direct-force means + independent source metrology`

when reset/visibility/coupling achieve `R_alpha >~2.20e-5 s^-1` in the current y_ref=-4 transparent comparison.

Additional force covariance is a fallback for slow source preparation or future covariance-specific co-design, not the default local architecture.

## 17. Publication architecture

`docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`:

1. RQIR I — operational hierarchy / ordered source information / finite discriminants;
2. RQIR II — statistical identifiability / nuisance geometry / source calibration;
3. RQIR III — physical resources / experiment architecture;
4. later Candidate Gravity paper after a concrete model passes RQIR I–III gates.

## 18. Mandatory open consistency gates

G1 gauge/relational observables; G2 source+apparatus conservation/Bianchi; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a semiclassical/stochastic/classical-gravity+full-QFT/quantum degeneracy; G13 detector covariance/nuisance/measurability.

## 19. Current priority — v2.8

P1. Build a **total Toy012 D2 wall-clock budget** combining absolute science signal, independent seven-layer/direct-force mean calibration, source metrology, timing/additive controls, acceptance/coherence/dead/reset time.

P2. Attach a physical force transduction/PSD to Toy012 mean calibration so its `gamma_mean` becomes actual shot count/time.

P3. Compare total Toy012 and Toy009 under one common mass/gap/separation/detector-noise budget; never compare normalized Fisher alone.

P4. Recompute Toy012 timing/additive systematics if they become competitive in total cost.

P5. Re-open force-covariance source co-design only if independent source metrology is not viable after full wall-clock accounting.

P6. Build one common D1/D2 apparatus budget.

P7. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.

P8. After detector/inference geometry stabilizes, close gauge, conservation, renormalization and full stress-energy gates.

## 20. Continuation protocol

At every substantive iteration:

1. read `RECOVERY_GUIDE.md`, `MASTER_TABLE.md`, latest research log and relevant Toy/Fisher documents;
2. repository is source of truth;
3. check recent commits before assigning an iteration number because parallel research may advance the repo;
4. do not duplicate closed/active calculations without reason;
5. derive before adding numerical complexity;
6. preserve hard constraints, parameter-coordinate consistency, centered noise and operator ordering;
7. separate normalized nuisance geometry from absolute detector signal/rate;
8. save reproducible code, main document, research log and recovery delta;
9. update master/recovery after a material front change;
10. do not claim new physics before consistency/competitor/experimental gates close.