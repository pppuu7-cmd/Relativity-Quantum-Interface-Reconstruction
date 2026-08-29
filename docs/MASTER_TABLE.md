# RQIR Operational Master Table

**Version:** 2.8  
**Date:** 2026-08-30  
**Authority:** repository source of truth. RQIR remains separate from RTK/DSIR. No toy, Fisher, resource or detector-model result is an empirical new-physics claim.

## Programme objective

RQIR reconstructs the operational gravity–quantum interface from distinguishable observables rather than assuming a preferred quantum-gravity theory.

Primary inference object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Exact rank/nullspace is not statistical identifiability. Every physical comparison must include source preparation, calibration, detector, controls, backaction and wall-clock rates in one consistent parameter coordinate.

## Mature Toy009/Toy010 baseline

Toy009 radii:

`(1.00000,1.60090005,1.77911036,2.60900799,5.90723562)`.

Balanced Iteration-011 geometry:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact rank `24/25`;
- positive hidden states;
- selected equality residual `<1e-15`.

Toy009/Toy010 exact mean/noise equality and ordered-response split remain retained.

## Mandatory corrections

- **RQIR-NUM-001:** trace+energy constraints must be eliminated analytically; huge penalty + threshold pseudoinverse can truncate real weak nuisance directions.
- **RQIR-NUM-002:** downstream hidden amplitude is fractional `alpha`, with `a=0.08 alpha`; transform Fisher by `F_alpha=0.08^2 F_a`.
- **RQIR-CAL-013:** finite-noise covariance uses centered noise derivatives, not raw second moments unless raw moments are explicitly measured.

Toy009 centered D2 baseline:

- `gamma_mean=1.830264703e6`;
- `gamma_cov=5.901272925e5`.

Toy009 full source QFI:

`F_Q^alpha=0.0849323916` per ideal accepted single-branch copy.

## Retained no-go / structural gates

- **NG-005:** an exact gravitational null cannot self-calibrate hidden source amplitude.
- **NG-006:** low-rank timing/geometry/additive nuisances can remain detector-degenerate at arbitrarily high science exposure.
- **NG-007:** a stability floor above the target cannot be repaired by faster white averaging.
- **NG-008:** SI additive tolerances require a physical transduction Jacobian.
- **NG-010:** replacing a calibration observable can rotate rather than remove a detector-relevant null.
- **NG-011:** force determines potential only relationally without an independent reference/integration constant.
- **NG-012:** information on one old hidden amplitude does not guarantee profiled beta identifiability if another detector-aligned null survives.
- **NG-013:** PSD+bandwidth do not determine source-covariance Fisher without covariance/spectral transfer derivatives.
- **NG-014:** current covariance observables are phase-referenced nonstationary two-time objects, not stationary scalar PSD coordinates.
- **NG-015:** detector-output covariance is not automatically the source symmetrized correlator for noncommuting observables.
- **NG-016/017/018:** finite Gaussian covariance readout has positivity/shared-matrix/shared-endpoint Fisher ceilings.
- **NG-019:** current 14 force means are not one disturbance-free multitime observable bundle; only same-time dual-probe pairs commute.
- **NG-020:** direct non-QND diffusive monitoring trades information for source dephasing.
- **NG-021:** reciprocal linear probe mediation obeys `S_u S_BA,src >= hbar^2/(4 eta)`; gain/susceptibility cannot remove the quantum-limited input-referred product.
- **NG-022:** full nuisance profiling tightens the same-copy backaction limit beyond raw signal attenuation.
- **NG-023:** QND with respect to isolated source `H` is not equivalent to ordered-response nondemolition.
- **NG-024:** under exact trace+mean-energy matching, weak energy metrology is quartically suppressed in measurement strength.
- **NG-025:** an algebraically optimized source need not be spatially local; locality cannot be imposed reliably by post-hoc truncation.
- **NG-026:** full hard rank can coexist with poor finite-noise `F_beta|theta`; rank completion is not resource closure.

## Control benchmark retained

At `100 Hz` after centered-noise correction:

- D1 timing target `~11.0511 us`;
- D2 timing target `~9.19001 us`;
- D2 normalized additive targets `sigma(b_mean)~7.39168e-5`, `sigma(b_cov)~1.30175e-4`.

Toy009 coherence floor from largest stored phase:

`T_coh,min~7.94319 ms` at 100 Hz.

## Toy009 complementary D2 branch — historical mature resource reference

At `y_ref=-4`, centered likelihood, `lambda=1`:

| added force-cov rows | `F_beta|theta` | `C_alpha*` |
|---|---:|---:|
| 0 | `~0.833432` | `4.55511` |
| best4 `(0,1,3,7)` | `~0.899477` | `0.05006144` |
| best5 `(0,1,3,6,7)` | `~0.903527` | `0` |
| all8 | `~0.905293` | `0` |

Natural Gaussian cross-covariance graph floors:

- best4 `N>1.180254e6`;
- best5 `N>2.135100e6`;
- all8 `N>3.540762e6`.

**RESOURCE-015:** covariance graph congestion can make extra jointly acquired rows increase total cost.

## Measurement/backaction resource front — Iterations 041–046

- 14 force means form seven commuting same-time dual-probe layers; 84/91 cross-time pairs do not commute.
- **CAL-015:** same-time dual probes are the maximal disturbance-free grouping in Toy009.
- **RESOURCE-016:** one trajectory may receive shared mean/covariance/control Fisher credit only if one physical likelihood supplies all scores/cross-Fisher/backaction.
- **RESOURCE-017:** independent phase layers pay `sum_j t_j`, not `7*t_max` and not one reused noncommuting copy.
- Reciprocal quantum-limited same-copy monitoring cannot carry the old optimistic full mean target while retaining 90% profiled beta information.
- At Toy009 `lambda=1`, even perfect source-amplitude metrology requires `xi_shared<=~0.7001`; only ~31.6% of mean Fisher can be safely shared in the optimistic proxy.
- **RESOURCE-020:** shared mean Fisher, source metrology and calibration exposure form a three-way backaction frontier.

## Explicit Toy009 source metrology — Iterations 047–052

Projective energy-population metrology:

`F_E^alpha(+)=0.0093918844`.

It carries ~11.1% of full Toy009 QFI but is assigned to independent/sacrificial copies because projective energy dephasing destroys most ordered response on the same science copy.

Finite Gaussian pointer:

- weak Fisher starts at `O(r^4)` because trace and mean energy are exactly matched;
- zero-reset Toy009 rate coefficient `R/(p eta kappa_E)=0.0082700957` at `r~0.86775`.

QND Ramsey ancilla:

- per-copy optimum `phi~2.41867`;
- Fisher/sec zero-reset optimum `phi~1.09231`;
- `R/(p Omega_E)=0.0025234392`.

**RESOURCE-024:** Fisher-per-copy and Fisher-per-time optima differ.

## Canonical Iteration 056 — reset/visibility surface

Canonical numbering note: Iteration 055 is Toy012; Ramsey reset/visibility was reindexed to **Iteration 056**.

Independent Ramsey rate:

`R_alpha(phi)=p_E F_alpha(phi,V)/(t_reset+phi/Omega_E)`.

**RESOURCE-026:** source reset/preparation overhead is a first-class Fisher resource; per-copy Fisher alone cannot select a branch.

For the historical Toy009 complementary branch, source-metrology rate thresholds remain

- branch0↔best4 `2.1340355e-4 s^-1`;
- best4↔best5 `2.9312162e-6 s^-1`.

Do not reuse these numbers for Toy012 without re-profiling its branch geometry.

## Locality branch — Toy011 / Iterations 053–054

Toy009 locality audit in its literal radius basis:

- `64.46%` of off-diagonal coupling power lies beyond nearest neighbours;
- naive truncation changes `H` by relative Frobenius `~0.369` and shifts the spectrum.

**DESIGN-002:** locality belongs inside source/calibration/detector co-design.

Toy011 proved existence of an exactly nearest-neighbour five-site source with rank `24/25`, positive hidden states and nonzero ordered response.

Iteration 054 showed the first Toy011 points were not resource competitive:

- response point: D2 raw signal `0.1707` Toy009, D2 normalized calibration cost `34.6x`;
- conditioning point: D2 raw `0.0842`, calibration cost `10.1x`.

However full source QFI remained close to Toy009 and `C_alpha(lambda)` nuisance shape stayed similar: locality did **not** create a new catastrophic beta/source degeneracy.

**RESOURCE-025:** locality is a multi-resource tradeoff among absolute detector signal, calibration burden and source-metrology rate.

## Toy012 — leading locality-constrained candidate, Iteration 055

Resource-aware nearest-neighbour co-design found a much better balanced local source.

Geometry:

- `q0=(0.18244654,0.68436894,0.16559135,0.67932486,0.09720934)`;
- `y1=-2.94878657`;
- phases `(0,1.03886746,2.98596300,4.87581918,4.15089956,1.62391517,5.27522069)`.

Exact properties:

- strictly nearest-neighbour site Hamiltonian with exact spectrum `(1,2,3,4,6)`;
- rank `24/25`;
- `s_min=1.43255e-3`, condition `~3264`;
- positive hidden pair and residual `<6e-17`.

Relative to Toy009:

- D1 raw detector Fisher proxy `0.17042`;
- D2 raw detector Fisher proxy `0.21617`;
- D1 centered calibration cost `1.515x`;
- D2 centered calibration cost `1.058x`;
- `F_Q^alpha=0.0992807` (`1.169x`);
- energy-population Fisher `0.00629727` (`0.671x`);
- Ramsey Fisher/sec coefficient `0.00213429` (`0.846x`).

**DESIGN-003:** the large first Toy011 locality penalty was objective-dependent; near-Toy009 calibration efficiency is compatible with exact nearest-neighbour dynamics. The leading remaining Toy012 penalty is absolute detector signal.

Toy012 is the **leading locality-constrained source**, but Toy009 remains the mature global resource baseline until all detector/systematics machinery is rebuilt.

## Toy012 complementary D2 — Iteration 057

At common `y_ref=-4`, Toy012 uses

- `gamma_mean=1.2086865e6`;
- `gamma_cov=1.8994980e6`.

Relational means + force means + centered relational covariance already have hard rank `23/23`, but

`F_beta|theta(C_alpha=0,lambda=1)=0.194405`.

Source-prior requirements at lambda=1:

| force-cov rows | best subset by `C_alpha` | `C_alpha*` |
|---:|---|---:|
| 0 | `()` | `13.669415` |
| 1 | `(1)` | `13.135585` |
| 2 | `(1,3)` | `12.309076` |
| 3 | `(1,3,5)` | `12.152511` |
| 4 | `(1,3,4,5)` | `12.097052` |
| 5 | `(0,1,3,4,5)` | `12.009588` |
| all8 | all | `11.891638` |

Toy009's strong covariance completion does **not** transfer.

**DESIGN-004:** complementary covariance geometry is source-specific and must be co-designed with the source.

Best4 Toy012 saves only `Delta C_alpha~1.57236` but has natural graph floor `N>3.798996e6`; at 100 Hz, p=.5, 1 ms overhead this is `~19.83 h`. Independent source-metrology break-even is only

`R_alpha~2.20253e-5 s^-1`.

## Toy012 pointer/Ramsey reset surface — Iteration 058

For the Iteration-057 rate target:

### Gaussian pointer

- projective `F_E^alpha=0.00629727`;
- zero-reset rate optimum `r~1.44273`;
- `R/(p Gamma_E)=0.00425193`;
- at p=.5, zero-reset threshold `Gamma_E~0.01036 s^-1`.

### Ramsey ancilla

- zero-reset rate optimum `phi~1.57508`;
- `R/(p Omega_E)=0.00213429`;
- per-copy maximum `F_R,max~0.00349867`;
- at p=.5, zero-reset threshold `Omega_E~0.02064 s^-1`.

**RESOURCE-027:** finite Fisher per accepted source copy creates a coupling-independent reset ceiling:

`R_alpha <= p_E F_max/t_reset`.

At p=.5 and the current Toy012 branch0/best4 target:

- pointer reset ceiling `~142.96 s`;
- Ramsey reset ceiling `~79.42 s`.

**PREP-004:** fresh-source throughput is an architecture variable. Do not rank source-metrology protocols from per-copy Fisher alone.

## Current architecture decision

For Toy012, do **not** inherit Toy009 best4 covariance by default. Current leading local architecture is

`local Toy012 + relational/direct-force mean calibration + independent source metrology`

provided fresh-source metrology exceeds the Iteration-057 rate target after reset/visibility.

Added force covariance remains an active fallback only for slow source preparation or if future complementary co-design substantially improves its nuisance overlap.

## Publication architecture

See `docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`:

1. RQIR I — operational hierarchy / ordered source information / finite discriminants;
2. RQIR II — statistical identifiability / nuisance geometry / source calibration;
3. RQIR III — physical resources / experiment architecture;
4. later Candidate Gravity paper only after a concrete model passes RQIR I–III gates.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a semiclassical/stochastic/classical-gravity+full-QFT/quantum degeneracy; G13 detector covariance/nuisance/measurability.

## Priority ranking v2.8

1. Build a **total Toy012 D2 wall-clock budget**: absolute science signal, independent seven-layer/direct-force mean calibration, source metrology, timing/additive references, acceptance/coherence/dead/reset time.
2. Attach physical force transduction / detector PSD to Toy012 mean calibration so `gamma_mean` becomes actual shot count/time.
3. Compare total Toy012 local branch against mature Toy009 on one common mass/gap/separation/detector-noise budget; do not compare normalized Fisher alone.
4. Rebuild centered timing/additive systematics explicitly on Toy012 if they become comparable to mean/science cost.
5. Only re-open force-covariance source co-design if total wall-clock shows independent source metrology is not viable.
6. Build one common D1/D2 physical apparatus budget.
7. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.
8. After detector/inference geometry stabilizes, close gauge, conservation, renormalization and full stress-energy gates.