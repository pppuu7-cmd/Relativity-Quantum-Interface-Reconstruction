# RQIR Papers I–V — strict repository-readiness audit

**Date:** 2026-09-09  
**Purpose:** estimate how ready the current repository is to support each paper scientifically. This is **not** a probability of journal acceptance and is deliberately stricter than old frozen-scope percentages where later work exposed additional apparatus or comparator requirements.

## Canonical five-paper architecture

1. **Paper I** — operational hierarchy / ordered source information / finite discriminants.
2. **Paper II** — statistical identifiability / nuisance geometry.
3. **Paper III** — physical resource budgets / experiment architecture.
4. **Paper IV** — existing gravity and quantum-gravity frameworks through the common RQIR comparator funnel, ending in one of `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, `NEW_REQUIRED`.
5. **Paper V** — a genuinely new RQIR-derived Candidate Gravity model **only if** Paper IV returns `NEW_REQUIRED`.

A `BLOCKED` comparator is not evidence for `NEW_REQUIRED`.

## Readiness definition used here

The headline percentage means **scientific/material readiness of the repository for the strengthened paper**, not portal/submission administration. It combines:

- frozen definitions and claims;
- derivations / numerical or algebraic audits;
- reproducibility and provenance;
- closure of the paper's decisive scientific gate;
- enough article-facing synthesis to support a defensible manuscript.

For Paper III, the old Iteration-128 statement `100% scientific / 97% submission` remains valid only for the **frozen abstract resource/design/certificate scope**. The current audit adopts the stronger apparatus-specific standard introduced on 2026-09-09, so it does not reuse that 100% headline.

For Paper V, readiness cannot be treated as an ordinary countdown before Paper IV authorizes it. We therefore report `0% article-authorized` and separately report the live Candidate-Gravity groundwork score.

## Current headline table

| Paper | Current strict repository readiness | Status | Decisive reason |
|---|---:|---|---|
| I | **100% scientific material** | CLOSED for frozen scope | RQIR-THM-001/source-calibration layer is scientifically closed; remaining work is editorial/submission hardening rather than missing scientific content. |
| II | **100% scientific material** | CLOSED | detector-facing likelihood, nuisance profiling, whitening, rank-deficient tests and independent submission audit are closed; submission package is essentially complete. |
| III | **74% strengthened apparatus-specific readiness** | ACTIVE | the physical colored-noise Fisher layer is now propagated through the nonlinear detector observable `P=(1+C cos Phi)/2`, using source-grounded detection noise and an effective contrast anchor. Science estimability survives simultaneous phase, contrast and readout-gain drift profiling; finite reference uncertainty produces the expected calibration floor. Certified injected-reference metrology and a final end-to-end campaign certificate remain open. |
| IV | **55%** | ACTIVE / prerequisite-blocked at decisive residual gate | comparator funnel and many framework audits exist, but the common physical observable/source-completion bridge and robust comparator-subtracted residual are still missing, so none of the four terminal Paper-IV decisions is yet authorized. |
| V | **0% article-authorized**; **24% conditional Candidate-Gravity groundwork** | CONDITIONAL / NOT AUTHORIZED | Paper IV has not returned `NEW_REQUIRED`; live Candidate-Gravity rubric is 24/100, consisting almost entirely of comparator foundation (24/25), with robust residual, parent dynamics, consistency, identifiability and resources still 0. |

## Paper I

Repository scientific scope remains closed at Iteration 078. The CQG-targeted manuscript exists and the scientific material is sufficient for the paper. The remaining gaps are publication figures/tables, final provenance binding for Toy009/Toy010, journal-specific bibliography/priority normalization, independent clean reproduction, and final package assembly. These reduce **submission readiness**, not the scientific-material score used in the headline table.

## Paper II

Paper II is the most publication-mature branch. The repository states the scientific scope is closed and the PRR package includes manuscript, vector figures, deterministic data regeneration, 10,000 randomized property tests, rank-deficient nuisance tests, correlated-covariance whitening, cover letters, manifest and checklist. Remaining actions are predominantly author/portal administration.

## Paper III — strengthened standard

The 2026-09-09 apparatus audits now close the structural identifiability layer, most of the physical same-apparatus noise/resource layer, and the principal detector-facing nuisance layer:

- common multiplicative science-scale degeneracy is explicit;
- after additive-nuisance and correlated-covariance profiling, a known modulated acceleration reference can make the RQIR science amplitude estimable even when internal `k/T` calibration retains a null direction;
- recoil provides a distinct `(2,1)` scale direction relative to acceleration `(1,2)`;
- recoil alone does **not** close absolute science-amplitude identifiability when the science scale remains free;
- unknown reference amplitude without prior remains non-identifiable for all shot counts;
- with a reference prior, the resource law exposes an irreducible calibration floor rather than falsely treating it as ordinary statistics;
- the same-apparatus audit is tied to the published SYRTE 87Rb Raman gravimeter: `2T=100 ms`, `4 Hz` cycle, about `10 us` Raman pulse, and measured `11 mrad/shot`;
- the derived `k_eff T^2` scale reproduces the published `1.4e-8 g at 1 s` short-term sensitivity to rounding accuracy;
- the Cheinet sensitivity-function result supplies a concrete low-frequency acceleration transfer, and the `2T/Tc=0.4` duty/dead-time cost is explicit;
- a coarse log-log digitization of the published passive-platform Fig.-8 acceleration ASD, without amplitude fitting, propagates to `6.35e-8 g at 1 s`, within about 2.3% of the paper's independently quoted `6.5e-8 g at 1 s` inferred vibration limit;
- applying the paper's factor-3 vibration rejection and its independent `4 mrad/shot` non-vibration budget yields `2.18e-8 g at 1 s`, within about 8.8% of the quoted typical corrected `2e-8 g at 1 s`;
- this physical PSD is converted into sampled Toeplitz covariance by integrating the continuous phase PSD at actual shot separations, so the off-diagonal covariance is no longer an arbitrary AR(1) family;
- science estimability survives a smooth 2-Hz crosstalk stress boosted up to five times the nominal trace, although the uncertainty degrades as expected;
- the actual detector observable is now modeled as `P=(1+C cos Phi)/2` near mid-fringe rather than treating reconstructed phase as the primitive data product;
- the source reports `sigma_P ~ 3e-4` at high atom number and `sigma_phi=2 sigma_P/C`; combining this with the stated near-`1 mrad/shot` detector sensitivity gives an approximate effective working contrast `C~0.6` used as a source-derived anchor;
- the physical phase covariance is propagated through the shot-dependent nonlinear fringe slope into a non-Toeplitz probability covariance, with independent probability detection noise added explicitly;
- the detector-facing likelihood profiles common scale, phase offset plus linear/quadratic phase drift, absolute contrast plus linear/quadratic contrast drift, centered readout gain plus gain drift, readout offset and optional unknown reference amplitude simultaneously;
- finite calibrated reference makes `theta` estimable even though apparatus-only contrast/readout null modes remain; those null directions are explicitly theta-orthogonal rather than being hidden by priors;
- at `theta=1 ng`, the detector-facing forecast is approximately `5.73 ng` at 60 s and `1.83 ng` at 600 s under the physical covariance;
- a combined detector stress with 20% lower contrast, contrast drift, readout-gain drift and phase drifts in the source-described mid-fringe regime leaves `theta` estimable;
- the detector-facing calibration scan reproduces `sigma_theta^2 ~= sigma_stat^2 + (theta f_ref)^2` to numerical precision, making the statistical-to-reference-calibration crossover explicit;
- the negative controls remain intact: static science with free phase offset fails, modulation without reference fails, and an unknown uncalibrated reference fails.

The remaining high-value authorities are now tightly localized: a certified finite absolute uncertainty for a realizable injected acceleration reference, inclusion of the actual reference/modulation protocol in the duty-cycle ledger, raw shot-level population/contrast evolution and campaign cross-spectral data if obtainable, and one final joint end-to-end campaign certificate. The current probability model is detector-facing and source-grounded but does not pretend that the proposed reference amplitude has already been experimentally calibrated on this apparatus.

Therefore the strengthened Paper-III readiness is now **74%**.

## Paper IV

The repository contains substantial article-ready comparator material and a negative-results matrix spanning semiclassical, stochastic/postquantum, Gaussian/Källén–Lehmann, perturbative GR EFT, nonlocal/form-factor and asymptotic-safety directions. Later Candidate-Gravity work extends the audit chain through Iteration 675.

However the live front is prerequisite-blocked. Exact missing authorities are:

- **M1:** a concrete same-parent conserved detector/asymptotic observable geometry;
- **M2:** matched Source/Born/contact completion in that same observable;
- **M3:** a concrete nonzero robust comparator-subtracted residual;
- **M4:** actual `Tr U1` only if a future C5 route requires it.

Because `M1–M3` are upstream of the terminal comparator decision, Paper IV cannot yet honestly choose `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED`. The large quantity of negative/audit material therefore does not justify a near-complete score. **55%** is retained as a conservative scientific-material estimate.

## Paper V

Paper V is not merely unfinished; under the accepted architecture it is **not yet authorized to exist as a new-model paper**. The correct headline is therefore `0% article-authorized`, not 24%.

The separate **24% Candidate-Gravity groundwork** remains valuable. The live model rubric is:

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

If Paper IV eventually returns `NEW_REQUIRED`, this 24% groundwork becomes the starting asset for Paper V rather than its publication-readiness percentage.

## Program-level interpretation

Do **not** average the five percentages into a single publication score: Paper V is conditional and Paper III is currently being judged against a deliberately stronger apparatus-specific standard than the historical frozen scope.

Current working RQIR programme/model readiness is now approximately **72%**. The Candidate-Gravity/new-model branch remains **24%**. Paper IV remains the main programme-level bottleneck despite the Paper-III advance.

## Next high-value research action

For Paper III, the next authority is an end-to-end campaign certificate: freeze an experimentally realizable reference-injection protocol, attach a source-grounded absolute transfer uncertainty, account for its modulation/reference shots in the duty-cycle resource ledger, and combine that with the physical PSD plus detector-facing probability likelihood in one final certificate with explicit failure domains. Raw population/contrast and cross-spectral data should replace the coarse source digitization if obtainable, but their absence should remain labelled rather than silently estimated. For Paper IV, computation remains prerequisite-blocked until new authority supplies M1/M2 or an independent admissible comparator branch.