# RQIR Operational Master Table

**Version:** 2.2  
**Date:** 2026-08-29

The repository is authoritative. `OPEN` means the required comparison is not yet demonstrated at RQIR precision. RQIR remains separate from RTK/DSIR. No toy/resource result is an empirical new-physics claim.

## Programme channels

| Channel | Main observable | Main obstacle | Current strategy | Status |
|---|---|---|---|---|
| Q1 clocks | conditional phase/visibility | ordinary relativity + differential timing drift | profiled likelihood + TDEV/phase controls | OPEN |
| Q2 superposed sources | potential/force/phase spectra | static-density blindness; tomography at complete history | finite NP3 + detector transfer | HIGH |
| Q3 source/backreaction | mean, noise, ordered/retarded response | source-amplitude degeneracy; calibration/control nuisance | joint source+calibration+detector Fisher + source metrology | HIGHEST |
| Q4 gravity-mediated QI | entanglement/non-Gaussianity | non-unique interpretation | common likelihood across interface classes | HIGH |
| Q5 geometry fluctuations | noise/response spectra | matter/intrinsic/technical degeneracy | joint covariance/response inference | HIGH |
| Q6 causal/process | relational timing/process observables | control-system confounds | nuisance-closed scaling tests | OPEN |
| Q7 low-energy QG EFT | long-range/nonanalytic corrections | tiny signals/local-UV degeneracy | cross-process fingerprints | OPEN |

## Current exact baseline

Toy009 source radii:

`(1.00000,1.60090,1.77911,2.60901,5.90724)`.

Balanced Iteration-011 geometry:

- `y1=-3.7766873837`;
- phases `(0,3.09855988,3.45849306,2.93830159,4.13016958,4.84480925,4.99085067)`;
- exact rank `24/25`;
- positive source states;
- selected equality residual `<1e-15`.

Toy009/Toy010 exact null/ordered-response results remain retained after later statistical/resource corrections.

Primary inference object:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab = ||(I-P_J)s_tilde||^2`.

Exact rank is not statistical identifiability.

## Mandatory corrections retained

### RQIR-NUM-001 — exact hard constraints

Trace+energy must be eliminated analytically. The old huge-penalty + threshold-pseudoinverse implementation inflated weak-direction Fisher; the large Iteration-013/014 gains are withdrawn.

### RQIR-NUM-002 — Fisher-coordinate Jacobian

Iteration 020 QFI is for physical amplitude `a` in `rho(a)=I/5+a Delta0`, while current detector Fisher uses fractional amplitude `alpha` with `a=EPS alpha`, `EPS=0.08`.

Therefore

`F_Q^(alpha)=EPS^2 F_Q^(a)`.

Current values:

- `F_Q^(a)~=13.27068619`;
- `F_Q^(alpha)~=0.0849323916` per ideal accepted single-branch source-metrology copy.

At normalized detector Fisher `S_D=1`, isolated 90% amplitude retention requires `C_alpha=9`, about `105.97` single-branch copies or `52.98` independent plus/minus pair equivalents at the QFI bound.

The old `~17 copies for C_a=225` mapping is withdrawn for the downstream fractional-amplitude coordinate.

Coordinate-correct preparation rate:

`R_P^(alpha)=p_P eta_P F_Q^(alpha)/t_P`.

### RQIR-CAL-013 — centered-noise linearization

The physical RQIR noise object is centered. For a symmetric pair about `rho0=I/5`, use

`C_AB = sym(A,B) - <A>0 B - <B>0 A`

on the trace-zero tangent. Raw second moments are equivalent only under exact mean conditioning or when raw moments are explicitly the measured statistic.

Exact Toy009/Toy010 null geometry is unchanged. Preferred centered 90%-retention normalized weights are approximately:

- D1 `gamma_mean=1.266e6`, `gamma_cov=0.622e6`;
- D2 `gamma_mean=1.830e6`, `gamma_cov=0.590127e6`.

## Retained structural gates

- **NG-001:** static diagonal density can be phase blind.
- **NG-002:** minimal ordered-response split has an energy confound.
- **NG-003:** generic complete density history becomes tomography.
- **NG-004:** one additional independent exact row kills a one-dimensional exact null.
- **NG-005:** an exact gravitational null cannot self-calibrate the hidden source amplitude.
- **NG-006:** uncontrolled low-rank timing/geometry/additive systematics can remain detector-degenerate; exposure alone cannot cure them.
- **NG-007:** a stability floor above the required prior cannot be fixed by faster white-noise averaging.
- **NG-008:** SI additive tolerances require physical transduction Jacobians.
- **NG-010:** replacing a calibration observable can rotate rather than remove a detector-relevant null.
- **NG-011:** detector-native force determines potential only relationally without a reference.
- **NG-012:** information on one old hidden amplitude is insufficient if another detector-aligned null remains.
- **NG-013:** force PSD + bandwidth do not determine source-covariance Fisher without spectral/covariance derivatives.
- **NG-014:** current Toy009 covariance rows are nonstationary phase-referenced two-time observables; stationary PSD rates are not directly valid.
- **NG-015:** detector-output covariance is not automatically the source symmetrized correlator for noncommuting source observables.
- **NG-016:** an `m`-dimensional full-range affine covariance-only Gaussian readout has `I_alpha^shot < m/2` for one covariance amplitude.
- **NG-017:** for `q` simultaneously varied full-range affine covariance coordinates, `Tr K < m/2` and `lambda_min(K)<m/(2q)`.
- **NG-018:** the actual six-endpoint cross-covariance graph of rows `(0,1,3,7)` further limits per-row Fisher to `<1/2` because of shared endpoints.

## Current centered control requirements

RQIR-NG-006 survives the centered correction. Preferred first-order benchmark at 100 Hz:

### D1

- `sigma(delta tau)~6.94360e-3`;
- `sigma_t~11.0511 us`;
- `sigma(b_mean)~8.88857e-5`;
- `sigma(b_cov)~1.26818e-4`;
- restored `F_beta|theta~0.899915`.

### D2

- `sigma(delta tau)~5.77425e-3`;
- `sigma_t~9.19001 us`;
- `sigma(b_mean)~7.39168e-5`;
- `sigma(b_cov)~1.30175e-4`;
- restored `F_beta|theta~0.899893`.

Current coherence floor from the latest stored phase:

`T_coh,min=4.99085067/(2 pi f_gap)`.

At 100 Hz: `~7.94319 ms`.

## D2 branch status

| Branch | Observable family | Hard rank | Current centered result | Status |
|---|---|---:|---|---|
| NP3-null | potential means + centered potential covariance | `22/23` | hidden amplitude remains null | retained |
| Historical hybrid | force means + old potential/raw covariance | `22/23` | Iteration-026 mixed protocol | historical only |
| Fully force-native centered | force means + centered force covariance | `22/23` | `F_beta(C_alpha=0,lambda=1)~0.019515`; `C_alpha90~7.78026` | retained |
| Finite-reference relational centered | relational means + centered relational covariance | `22/23` | finite reference rotates but does not remove detector-relevant null | retained |
| Complementary centered | relational + force means + complementary centered covariance | `23/23` | at `y_ref=-4`, all-cov `F_beta~0.905293` | highest D2 design branch; physical joint-readout gate open |

At `y_ref=-4`, `lambda=1`:

- 0 added force-cov rows: `F_beta~0.833432`, `C_alpha*=4.55511`;
- best4 `(0,1,3,7)`: `F_beta~0.899477`, `C_alpha*=0.0500614`;
- best5 `(0,1,3,6,7)`: `F_beta~0.903527`, `C_alpha*=0`;
- all8: `F_beta~0.905293`, `C_alpha*=0`.

## Phase-referenced covariance measurement layer — Iterations 035–040

Preferred one-shot Gaussian likelihood:

`I_ij^shot=(d_i mu)^T Sigma^-1(d_j mu)+1/2 Tr[Sigma^-1 Sigma_,i Sigma^-1 Sigma_,j]`,

`q_ij=p_C eta_C I_ij^shot/t_C`.

**RQIR-RESOURCE-012:** stationary PSD Fisher is only a special case; current rows require an explicit phase-referenced/cyclostationary detector-output likelihood.

**RQIR-RESOURCE-013:** shared covariance shots must be costed with the full matrix Fisher rather than `sum gamma_i/q_i` when one trajectory contributes to multiple rows.

**RQIR-CAL-014:** covariance source directions should be Fisher-orthogonal to dominant imprecision/backaction/cross-noise nuisance derivatives. A nuisance aligned with one covariance derivative removes that direction after profiling.

### Iteration 038 — generic shared-output bound

For four covariance coordinates and a disjoint `m=8` near-saturating Gaussian output:

- ideal weakest-direction per-shot Fisher `<1`;
- accepted cycles at centered `lambda=1`: `>5.90127e5`;
- best4 saves `Delta C_alpha~4.5050486`, only `~53.04` source-copy equivalents;
- equal-efficiency wall-clock break-even: `t_P/t_C>~1.11255e4`;
- at 100 Hz coherence floor: source-metrology cycle must exceed `~88.37 s` before overhead (`~99.50 s` with `1 ms` detector overhead).

**RQIR-RESOURCE-014:** shared-shot speedup is dimension-limited; reuse of one shot across four directions can approach a factor four over separate bivariate campaigns, not an arbitrary gain.

### Iteration 039 — actual endpoint-sharing graph

Rows `(0,1,3,7)` use only six unique phase/probe endpoints and form two degree-two stars. For a natural cross-covariance-only encoding:

- full-hypercube positivity requires edge amplitude `<1/sqrt(2)`;
- per-row Fisher `<1/2`;
- accepted shared trajectories `>1.180254e6`;
- equal-efficiency `t_P/t_C>~2.22510e4`;
- at 100 Hz: `t_P>~176.74 s` before overhead, `~198.99 s` with `1 ms` overhead.

### Iteration 040 — covariance graph congestion

For a uniform cross-covariance edge encoding, per-edge Fisher ceiling is controlled by endpoint-graph spectral radius:

`K_edge < 1/rho(A_G)^2`.

- best4: `rho^2=2`, `N>1.180254e6`;
- best5: `rho^2=3.61803399`, `N>2.135100e6`;
- all8: `rho^2=6`, `N>3.540762e6`.

**RQIR-RESOURCE-015 — covariance graph congestion:** adding a jointly acquired covariance row can reduce the admissible per-shot Fisher of the entire edge set by increasing graph spectral radius.

The fifth row removes only residual `C_alpha=0.0500614`, equivalent to `~0.58943` source-copy equivalents, while increasing the covariance cycle lower bound by `~9.54846e5` trajectories. Therefore best5 beats best4 + minimal source metrology only if

`(p_C eta_C/p_P eta_P)*(t_P/t_C)>~1.61996e6`.

At 100 Hz and equal efficiency this requires source-metrology cycles longer than `~3.57 h` before overhead (`~4.02 h` with `1 ms`).

For the fixed 90% target, all8 is resource-dominated by best5 in the covariance-only cross-covariance graph architecture because both need `C_alpha=0` but all8 has the larger graph congestion cost.

## Current resource conclusion

The original idea that extra covariance rows might cheaply replace source metrology is now sharply constrained. Covariance complementarity remains geometrically powerful, but under the natural phase-referenced Gaussian cross-covariance implementation:

- the high-value four-row core is preferable to completing the covariance bundle;
- a tiny independent source prior is usually much cheaper than the fifth covariance row unless source verification is extremely slow;
- the complementary branch can become competitive only if the **same coherent trajectory** also earns substantial force-mean/control Fisher or if a different measurement class beats the present covariance-only graph bounds.

## Publication architecture

See `docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`.

1. RQIR I — operational hierarchy / ordered source information / finite discriminants.
2. RQIR II — statistical identifiability / nuisance geometry / source calibration.
3. RQIR III — physical resources / experiment architecture.
4. Later Candidate Gravity paper only after a concrete model passes reconstruction gates.

## Mandatory open consistency gates

G1 gauge/relational; G2 conservation/Bianchi with apparatus; G3/G3b positivity/unitarity/spectral response; G4a causal retarded support; G8 controlled Newtonian limit; G9 EFT power counting; G10/G10a stress-energy smearing/renormalization; G12/G12a classical/stochastic/full-QFT degeneracy; G13 detector covariance/nuisance/measurability.

## Priority ranking v2.2

1. Build a **joint mean + covariance phase-referenced D2 trajectory likelihood** on the actual shared endpoints, so the same accepted cycle earns force-mean and covariance Fisher.
2. Include timing/additive controls and explicit imprecision/backaction/cross-noise covariance derivatives in that same Fisher; enforce RQIR-CAL-014 nuisance orthogonality where physically possible.
3. Compare `best4 + minimal C_alpha` against `best5` and the fully force-native branch using one shared-cycle wall-clock model, not row-time sums.
4. Derive the physical mean transduction/SNR required for the joint trajectory to overcome the covariance-only graph bounds.
5. Revalidate second-order timing/gain bias only if it becomes competitive with the joint-readout gate.
6. Build a common D1/D2 budget at one source mass, gap, coherence, separation and campaign duration.
7. Propagate semiclassical, stochastic, classical-gravity+full-QFT and perturbative-QG alternatives through one likelihood.
8. After detector/inference geometry stabilizes, embed a more physical oscillator/atomic/full stress-energy source and close conservation, gauge and renormalization gates.
