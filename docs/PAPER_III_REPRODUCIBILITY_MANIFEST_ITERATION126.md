# RQIR Iteration 126 — Paper III Reproducibility Manifest

**Date:** 2026-08-31  
**Status:** manuscript reproducibility/package gate. No apparatus forecast and no new-physics claim.

## 1. Purpose

Paper III contains a long development history, but a reader/reviewer should not have to rerun every exploratory iteration. This iteration freezes a **minimum manuscript-bearing regression set** that reproduces the central numerical identities, no-go checks and architecture/resource reductions.

The manifest explicitly separates:

- deterministic offline regressions;
- external-literature/evidence audits;
- editorial/claim-structure checks.

An external evidence table is not treated as an offline reproduction of an experiment.

## 2. Environment convention

Canonical commands are run from repository root with Python 3 and NumPy. Some historical exploratory scripts may require their sibling modules in `analysis/`; the manuscript manifest below uses the repository file layout as committed.

No script in the minimum manifest may require secret data or unpublished apparatus measurements.

## 3. Minimum deterministic command set

| Manuscript object | Command | Expected invariant / check |
|---|---|---|
| final-significance source correction | `python analysis/robust_campaign_source_target_iteration104.py` | `(25,225) -> F=22.5`; final-5σ fixed-90% pair `(27.7778,250)`; robust source/science optimum |
| final Toy009/Toy014 architecture algebra | `python analysis/final_significance_architecture_crossover_iteration105.py` | exact `(u,v,z,delta)` crossover identities |
| same-state temporal `f,2f` calibration | `python analysis/same_state_f2f_calibration_protocol_iteration101.py` | white integer-cycle orthogonality; colored-noise counterexample; `rho_hi=1/9`; `N_rho>=312`; transfer injection budget |
| full complex campaign allocation | `python analysis/full_complex_campaign_allocation_iteration103.py` | free-gain zero-Fisher gate; phase-metric coupling; concavity/homogeneity; equal-marginal KKT regression |
| common-gain reference rate | `python analysis/full_complex_common_gain_rate_iteration115.py` | direct vs staged Schur profiling equivalence; phase-free Iteration-114 recovery |
| joint reference/no-double-counting | `python analysis/joint_reference_quota_iteration116.py` | generalized-eigenvalue quota; joint `max` vs separated `sum` regression |
| reference span/rank | `python analysis/reference_span_rank_iteration117.py` | repeating one setting does not enlarge score span; range/null feasibility |
| Toy009/Toy014 calibration span | `python analysis/toy009_toy014_calibration_span_iteration118.py` | source nuisance dimension 22; mean rank 14; covariance complement rank 8; full rank 22 |
| full covariance partition | `python analysis/full_covariance_endpoint_partition_iteration119.py` | full endpoint graph congestion and exact four-matching optimum in the declared cross-covariance class |
| calibration-cover bracket | `python analysis/calibration_cover_bracket_iteration120.py` | conservative/intermediate/optimistic calibration resource branches remain ordered |
| detector-rate bracket | `python analysis/detector_rate_bracket_iteration121.py` | rate-box propagation into an interval for `u=R_D14/R_D09`; common-rate-scale invariance |
| final notation | `python analysis/paper3_notation_dependency_audit_iteration125.py` | historical `225` semantics and canonical final-significance identities |

## 4. External-evidence command

`python analysis/external_apparatus_evidence_matrix_iteration122.py`

This reproduces only the **classification/evidence matrix encoded from the cited literature**. It does not reproduce the cited experiments and does not create a same-apparatus RQIR dataset.

External source verification remains a literature task and must be refreshed at manuscript submission if materially newer evidence appears.

## 5. Editorial/claim guards

Run:

- `python analysis/paper3_claim_evidence_matrix_iteration123.py`;
- `python analysis/paper3_manuscript_skeleton_iteration124.py`;
- `python analysis/paper3_reproducibility_manifest_iteration126.py`.

These verify that:

- standard Fisher/OED ingredients are not claimed as RQIR inventions;
- parametric/regression sections are not promoted to measured apparatus predictions;
- the minimum manuscript authority files exist;
- deterministic, external-evidence and editorial classes remain distinct.

## 6. Dependency order

The recommended reviewer reproduction order is:

1. Iteration 125 notation/final-significance bookkeeping;
2. Iterations 101, 103, 115 for detector/transfer likelihood;
3. Iterations 116–119 for joint calibration/no-double-counting/span/backaction-safe bounds;
4. Iterations 120–121 for the detector resource interval;
5. Iterations 104–105 for final detector+source architecture closure;
6. Iterations 122–124 for external evidence, novelty and manuscript claim boundaries.

This order follows logical dependency rather than historical iteration number.

## 7. Figure/table provenance package

Paper III can be built from seven figure/table families:

1. **Pipeline schematic** — conceptual, derived from Iteration 124; no measured data.
2. **NG-005 source-metrology curve/table** — deterministic formulas/regressions from Iterations 047–058, 098, 104.
3. **Two-band transfer/cross-PSD panel** — deterministic/parameterized results from 084–087 and 101–115.
4. **Calibration span/endpoint graph** — deterministic results from 117–120.
5. **Detector-rate interval `u`** — parameterized/interval result from 121; no apparatus point unless closure data are supplied.
6. **Final `(u,v,z,delta)` phase diagram** — analytic/parameterized result from 105/106; robust winner only under NG-030 interval separation.
7. **External apparatus evidence matrix** — literature-derived table from 122; explicitly component feasibility only.

### RQIR-REP-001 — figure provenance rule

Every manuscript figure/table must be tagged internally as one of:

`DERIVATION`, `DETERMINISTIC_REGRESSION`, `PARAMETRIC_SPECIFICATION`, `EXTERNAL_EVIDENCE`, or `MEASURED_APPARATUS`.

Paper III currently contains no `MEASURED_APPARATUS` RQIR closure dataset. A parameterized interval may not be styled or captioned as measured hardware performance.

## 8. Minimum numerical anchors

The manuscript/repository should preserve at least the following anchors because they detect common bookkeeping/regression failures:

- `F_final(25,225)=22.5`, `Z=4.74341649`;
- final `Z=5`, fixed `r=.9`: `A_raw=27.7777778`, `C_src=250`;
- same-state 90% balanced correlation bound `rho_hi=1/9`;
- ideal Gaussian correlation certificate `N_rho>=312` at `z=1.96`;
- transfer injection `N*SNR_inj^2>=1458.80` under the Iteration-101 hard-bound convention;
- Toy009/Toy014 source nuisance rank `22`, mean rank `14`, covariance complement `8`;
- full eight-row covariance cross-output optimum uses four matching blocks in the declared graph model.

These anchors are not apparatus forecasts.

## 9. Reproducibility scope boundary

The repository is reproducible for the **scientific claims it actually makes**: algebraic theorems, deterministic toy regressions, parameterized resource certificates and literature evidence classification.

It cannot reproduce a numerical same-apparatus Toy009/Toy014 runtime because no such compatible measured closure vector has been inserted. That absence is an explicit limitation, not an omitted input hidden by normalization.

### RQIR-NG-083 — reproducible parametric closure is not reproducible apparatus data

A fully reproducible parameterized experiment-design calculation must not be advertised as reproducing an experimental measurement that was never supplied.

## 10. Readiness snapshot — Iteration 126

Project-management estimates, not statistical confidence measures:

- **Paper III scientific-content readiness:** **98%**.
- **Paper III submission readiness:** **93%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **86%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

## 11. Next gate

Perform the final current literature/priority audit across the closest comparator classes:

- nuisance-profiled Fisher / optimal experimental design;
- gravity-mediated entanglement / QGEM resource estimates;
- classical-channel, stochastic and postquantum/classical-gravity experimental criteria;
- multimode/cross-spectral/transfer-calibrated force sensing;
- system-identification/calibration design.

The goal is not to prove priority from a finite search, but to determine whether any paper already contains the same end-to-end RQIR-specific resource-certificate chain and to narrow the manuscript novelty wording accordingly.