# RQIR Iteration 068 — Physical Fisher-Rate Closure for Preparation and Mean Calibration

**Date:** 2026-08-30  
**Status:** resource/notation correction and physical-rate bridge; no apparatus forecast and no new-physics claim.

## 1. Why this iteration was needed

Iteration 067 converted the spectral-tilt-profiled D2 science metric into independent detector-cycle Fisher. The next source-of-truth gate was to put source-preparation Fisher `C_a` and row-normalized calibration strength `gamma` into the same repetition/PSD/wall-clock language.

A notation issue had to be fixed first. Two different quantities had historically been called `alpha`:

1. the fractional hidden-source preparation amplitude, with the current physical coordinate `a = 0.08 alpha`;
2. the pump impulse area in Protocol 002B, `alpha = (m_s/hbar) int A(t) dt`.

They are not the same physical parameter.

### RQIR-NUM-004 — separate preparation amplitude from drive amplitude

From this iteration onward use

- `alpha_h` for the fractional hidden-source preparation amplitude (`a=0.08 alpha_h`);
- `epsilon_drv` for the pump/drive impulse area entering the ordered-response detector signal.

At nominal `alpha_h=1`, the D2 detector leverage is therefore

`q_drv = 2 |epsilon_drv| Gamma_G / sigma_phi`,

not a factor built from the source-preparation coordinate.

The local response is schematically

`mu_D ~ beta alpha_h epsilon_drv s`.

Thus the `beta`/`alpha_h` derivative collinearity of RQIR-NG-005 remains exactly intact, while `epsilon_drv` belongs to the declared detector/control protocol. This notation correction does not alter the already computed Toy013/Toy009 science-time ratio because that ratio cancels the common detector leverage.

## 2. Science Fisher rate in one detector-cycle coordinate

Retain the Iteration-067 physical, spectral-tilt-profiled D2 source factor `S_eff`. For one statistically independent accepted science cycle,

`I_beta,cycle = q_drv^2 S_eff`.

For attempt duration `tau_s`, acceptance `p_s`, and no inter-cycle correlations,

`R_beta = p_s I_beta,cycle / tau_s`.

For a benchmark displacement `Delta beta=1` and target significance `Z`,

`T_sci = Z^2 / R_beta`.

Colored/correlated cycles require the full time-series likelihood; this formula is the white independent-cycle limit retained under RQIR-NG-027.

For the established physical two-band metric,

- `S_eff,009 = 5.779507196013e-4`;
- `S_eff,013/S_eff,009 = 0.04228407350`.

Therefore the same-apparatus science-time penalty remains

`T_sci,013/T_sci,009 = 23.64956630775`.

This exact regression survives RQIR-NUM-004.

## 3. Convert C_a into accepted source copies

Statistical Identifiability 002 gives, for the isolated `beta`/hidden-amplitude degeneracy,

`F_beta|alpha_h = S C_prep/(S+C_prep)`.

To retain fraction `r` of raw detector Fisher `S`,

`C_prep = [r/(1-r)] S`.

For a `Delta beta=1`, `Z=5` science target, raw detector information is `S=Z^2=25`. Therefore 90% retention requires

`C_prep = 9*25 = 225`.

This is a physical-coordinate Fisher target, not the old normalized `C_a=9` shorthand. The old value `9` was the ratio `C_a/S` when `S` was normalized to unity.

If one accepted independent source-metrology copy supplies `I_alpha,copy`, then

`N_prep,accepted = C_prep/I_alpha,copy`.

For Toy009:

- projective energy-population metrology gives `I_alpha,copy = 0.0093918844`, so
  `N_prep,accepted = 23956.85364`;
- the full ideal source QFI ceiling is `0.0849323916`, so even an optimal measurement cannot beat
  `N_prep,accepted = 2649.165951` for the same 90%-retention, 5-sigma target.

At `p_prep=0.5`, the corresponding preparation attempts are about

- `47913.71` for energy-population metrology;
- `5298.33` even at the ideal QFI ceiling.

These are lower bounds before reset/readout time, imperfect visibility, extra state nuisances, and apparatus systematics. They directly quantify why RQIR-NG-005 is experimentally consequential rather than merely algebraic.

For fresh-copy duration `tau_prep` and acceptance `p_prep`, the simple wall-clock form is

`R_alpha = p_prep I_alpha,copy/tau_prep`,

`T_src = C_prep/R_alpha`.

For Ramsey/pointer protocols, `tau_prep` must include the protocol-specific interaction plus reset/preparation/readout overhead already identified in Iterations 056–058.

## 4. Convert gamma into detector PSD and wall clock

Let `u_j` be one row-normalized calibration coordinate and let the physical detector record for one attempt have template `h_j(t;u_j)`. For a stationary Gaussian readout with one-sided output PSD `S_out,j(f)`, the single-cycle Fisher is

`I_mu,j = 4 int_0^infty |d htilde_j(f)/d u_j|^2 / S_out,j(f) df`.

This is the physical replacement for the abstract `xi_mu^2` used in earlier scheduling work.

With accepted-attempt probability `p_j` and attempt duration `tau_j`, the Fisher rate is

`R_mu,j = p_j I_mu,j/tau_j`.

For independently scheduled calibration layers all requiring the same row-normalized target `gamma`, a conservative campaign time is

`T_cal = gamma sum_j 1/R_mu,j`.

This reproduces the old homogeneous formula because if `I_mu,j=xi_mu^2`, `p_j=p`, then

`T_cal = gamma/(p xi_mu^2) sum_j tau_j`.

For Toy009, `gamma_mean=1.830264703e6`. Seven same-time dual-probe layers at `xi_mu=3` require

`7 gamma_mean/9 = 1,423,539.213` accepted layer-cycles,

exactly reproducing Iteration 042 before wall-clock overhead is applied.

### Multichannel caution

Two same-time commuting probe rows may share one physical cycle only when the detector supplies a declared joint likelihood. In that case the relevant information is the full `2x2` Fisher block (including cross-Fisher), not the sum of two independently quoted row SNRs. Cross-time noncommuting rows remain separate unless an explicit weak-measurement/backaction likelihood justifies sharing.

## 5. Apparatus-consistent x = T_cal/T_sci

The Iteration-066 dominance variable can now be written without the abstract `xi_mu`:

`x = T_cal/T_sci`

`  = [gamma R_beta/Z^2] sum_j 1/R_mu,j`.

This is **RQIR-RESOURCE-030 — Fisher-rate closure of gamma**:

> A row-normalized calibration strength becomes a physical resource only after every required calibration layer is assigned a detector-template Fisher rate in the same acquisition coordinate as the science likelihood. The dimensionless `gamma` alone does not determine shots or hours.

For multiple independent calibration families (for example relational and direct-force means), add their `gamma_f sum_j 1/R_mu,fj` contributions. For a shared multichannel record, replace this scalar sum by the appropriate full Fisher matrix and profile the common nuisance parameters once.

## 6. Detector SNR interpretation

For one scalar Gaussian mean measurement with parameter derivative equal to its signal template, the standardized single-cycle calibration SNR obeys

`rho_mu,j^2 = I_mu,j`.

Therefore

`N_j = gamma/rho_mu,j^2`

accepted cycles for one independent row-normalized layer.

This gives an immediate design interpretation of detector sensitivity while avoiding the error identified by RQIR-NG-027: `rho_mu` must be a **single declared cycle** SNR. An uncertainty already averaged over many cycles cannot be inserted as though it were single-shot noise.

## 7. Coherence and preparation accounting

The Fisher-rate bridge does not make coherence free.

- Science cycles must preserve the ordered source dynamics for their declared response window.
- Toy009 retains the stored 100-Hz source coherence floor `~7.94319 ms` for its largest phase layer.
- Independent strong source metrology belongs on sacrificial/fresh copies under RQIR-NG-023 unless a same-copy nondemolition likelihood is explicitly proven.
- Cross-time calibration layers pay their own preparation/evolution times under RESOURCE-017.
- Reset/dead/readout time belongs in `tau_j` or `tau_prep`, not outside the Fisher-rate denominator.

## 8. What is and is not closed

Closed in this iteration:

- the collision between hidden-amplitude and drive-amplitude notation;
- the conversion of the isolated `C_a/S` requirement into an absolute Fisher target and accepted-copy count for a stated science significance;
- the general physical PSD/rate expression that converts `gamma` into detector cycles and wall-clock time;
- exact regression of the Iteration-067 Toy013/Toy009 D2 science penalty.

Still open:

- an actual apparatus `S_out(f)` and transduction Jacobian for the relational/direct-force mean channels;
- full multichannel calibration covariance and detector correlations;
- timing/additive/control nuisance profiling on the same record;
- source-reset/visibility values for a chosen preparation implementation;
- D1 and D2 common-apparatus comparison;
- all relativistic, conservation, renormalization and full-QFT/classical/stochastic degeneracy gates.

No new physics is claimed.

## 9. Reproducibility

Code:

`analysis/physical_fisher_rate_closure_iteration068.py`

It verifies the Toy013/Toy009 science penalty, the 90%-retention `C_prep=225` benchmark, Toy009 energy-population/QFI copy bounds, and the Iteration-042 seven-layer `xi_mu=3` regression.

## 10. Next scientifically admissible gate

Build one explicit two-channel D2 calibration detector likelihood with a declared transduction Jacobian and one-sided equivalent-force/output PSD. Compute the `2x2` per-layer Fisher blocks for the simultaneous same-time probe pair, propagate them through all seven layers, and evaluate

`x = T_cal/T_sci`

using the same science-cycle acquisition model. Then combine it with

`y = T_src/T_sci`

from a chosen source-metrology protocol and test the Iteration-066 architecture dominance boundary without normalized-Fisher placeholders.
