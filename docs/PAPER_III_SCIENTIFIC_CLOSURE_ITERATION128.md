# RQIR Iteration 128 — Paper III Scientific Closure Certificate

**Date:** 2026-08-31  
**Decision:** **Paper III scientific scope CLOSED.**  
**Scientific-content readiness:** **100%** for the stated Paper-III resource/design/certificate scope.  
**Important boundary:** this is **not** an apparatus-specific numerical forecast and **not** a new-physics claim.

## 1. Frozen Paper-III scientific claim

Paper III develops an end-to-end resource-certificate framework specialized to the RQIR interface-discrimination problem. It connects

`interface discriminant -> exact source/calibration constraints -> detector nuisance profile -> source metrology -> transfer/cross-PSD calibration -> calibration span/backaction/no-double-counting -> physical Fisher rates -> robust wall clock -> final architecture certificate`.

The paper is scientifically complete when every arrow in this chain is explicit, reproducible and bounded by a stated limitation. A measured Toy009/Toy014 runtime is a conditional application of the framework, not a prerequisite for the framework's scientific claim.

## 2. Closure criteria

### C1 — detector-level identifiability

Closed. Use exact hard-constraint reduction and

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Paper II supplies the statistical certificate; Paper III uses it as the inference backbone.

### C2 — source-amplitude degeneracy and independent metrology

Closed. NG-005 is propagated into physical source-preparation Fisher, accepted copies, reset/visibility/coherence and wall-clock rate. Final-significance bookkeeping is corrected by NUM-006/NUM-008.

For a fixed retained fraction `r` and final target `F_*=Z_final^2`,

`A_raw=F_*/r`, `C_src=F_*/(1-r)`.

The historical `225` is retained only as a raw-5-sigma / 90%-retention regression.

### C3 — physical Fisher-rate bridge

Closed. Abstract `gamma` and source-preparation Fisher are converted to detector/source Fisher rates, shots, SNR, coherence/evolution time, acceptance, reset/readout and wall clock. The old post-Toy010 resource-conversion task must not be restarted.

### C4 — same-state temporal two-band likelihood

Closed at the design/certificate level. Finite-window `f,2f` covariance, colored-noise leakage, PSD/cross-PSD requirements and same-state dual-tone transfer calibration are explicit. A scalar ASD at two center frequencies is not credited as a full likelihood.

### C5 — full complex transfer nuisance

Closed. Gain and phase are treated inside the detector Fisher. The common-gain science-coupled quotient and full-complex Schur reduction are explicit; differential gain is identified with the spectral-tilt direction in the retained two-band model.

### C6 — control recertification

Closed algebraically. Scalar and matrix reference/drift/floor recertification envelopes are derived, including the likelihood-derived science-coupled transfer budget.

Physical drift matrices remain apparatus inputs, not missing theory.

### C7 — joint campaign scheduling / no double counting

Closed. One physical record receives one wall-clock charge. Joint Fisher blocks are credited once, and separate campaigns are combined by the campaign simplex / quota optimization rather than by summing duplicated scalar SNR costs.

### C8 — calibration score-span feasibility

Closed. Repeating an unchanged setting cannot create missing Fisher directions. For the retained Toy009/Toy014 construction after hard constraints, the source-nuisance dimension is 22; seven mean dual-probe layers provide rank 14 and centered covariance contributes the missing rank 8.

### C9 — covariance/backaction guard

Closed as a scope condition. The detector-output covariance endpoint graph and four-matching optimum are explicit, while NG-019/RESOURCE-016 prevent those output-sharing gains from being promoted to disturbance-free quantum-source sharing without a declared measurement/backaction likelihood.

An apparatus may close that likelihood later; Paper III does not assume it.

### C10 — detector-side architecture interval

Closed parametrically. Science, transfer, mean-calibration and covariance-calibration rates propagate into a robust interval for

`u=R_D14/R_D09`.

No central-value apparatus winner is required.

### C11 — final-significance architecture certificate

Closed. With

`u=R_D14/R_D09`,

`v=R_A14/R_A09`,

`z=R_A09/R_D09`,

`delta=(1-d14)/(1-d09)`,

use

`Q14/Q09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

NG-030 requires interval-safe separation for any robust winner.

### C12 — external experimental boundary

Closed for the manuscript scope. The literature audit establishes component feasibility for transfer-calibrated force sensing, cross-spectral/multimode sensing and exact `f:2f` platform operation, while explicitly finding no complete public same-apparatus RQIR closure vector in the inspected sources.

NG-080 forbids splicing incompatible experiments into one forecast.

### C13 — novelty / prior-art boundary

Closed at the finite-search manuscript level. Schur complements, Fisher/OED, force-transfer calibration, gravity-test resource estimates, QGEM, classical/stochastic gravity observables and related methods are prior art.

PRIORITY-001 limits the candidate Paper-III contribution to the RQIR-specific end-to-end integration and closure discipline. This is not a proof of global priority; refresh the search before submission.

### C14 — canonical notation/dependency chain

Closed at Iteration 125. Final-significance notation, rate symbols, architecture variables and supersession rules are frozen. Historical provenance is preserved without silently overriding late corrections.

### C15 — reproducibility package

Closed at Iteration 126. Manuscript-bearing deterministic regressions, external-evidence audits and editorial checks have a minimum command/evidence manifest. Figures/tables must retain provenance labels.

## 3. Non-blocking conditional extensions

The following remain scientifically useful but are **not prerequisites for the frozen Paper-III claim**:

1. measured same-apparatus two-band science transduction and PSD/cross-PSD;
2. measured full complex transfer-reference Fisher-rate matrix;
3. measured seven calibration-layer Fisher-rate matrices and correlated uncertainty;
4. physical geometry/additive reference Fisher and drift/floor models;
5. explicit weak/continuous-measurement backaction likelihood that permits covariance-sharing credit;
6. measured independent source-metrology rate and duty in the same apparatus accounting;
7. a numerical `u` interval narrow enough for NG-030 to choose Toy009 or Toy014.

These define an **apparatus-specific numerical extension**, not a hidden assumption of Paper III.

### RQIR-NG-084 — scientific closure is not apparatus closure

The statement “Paper III scientific scope is closed” must never be paraphrased as “the experiment is already numerically forecast” or “Toy009/Toy014 has an experimentally established winner.”

### RQIR-P3-CLOSE-001 — scope freeze

Absent an internal contradiction, failed regression or materially relevant new literature result, do not expand Paper III by launching new toy-source searches merely to increase its scope. New source design (including Toy015) belongs to a later research branch unless a manuscript review exposes a source-dependent gap required by the frozen claim.

## 4. What 100% means

`100% scientific-content readiness` means:

- all scientific links required by the stated Paper-III claim are present in repository authority files;
- core numerical identities have deterministic regression code;
- negative/no-go results are preserved;
- open apparatus data are explicit conditional inputs rather than normalized placeholders;
- novelty wording is bounded by prior art;
- the paper can now be drafted without inventing a physical measurement.

It does **not** mean the manuscript text, figures, bibliography and journal formatting are finished. Those are submission-readiness tasks.

## 5. Readiness snapshot — Iteration 128

Project-management estimates, not statistical confidence measures:

- **Paper III scientific-content readiness: 100%.**
- **Paper III submission readiness: 97%.**
- **Repository readiness to begin a concrete Candidate-Gravity model: 90%.**
- **Concrete Candidate-Gravity model itself: ~10%.**

The KG-start increase reflects completion of the reconstruction/identifiability/resource test pipeline. It does not imply that QG-001…QG-010 have been passed by a concrete model.

## 6. Next work after closure

For Paper III, the next tasks are manuscript production rather than expansion of scientific scope:

- generate/canonicalize figures and tables from the reproducibility manifest;
- write the prose from the Iteration-124 skeleton;
- refresh references immediately before submission;
- perform one independent clean rerun / reviewer-style audit;
- choose journal-specific formatting.

In parallel, a separate Candidate-Gravity branch may now be started from `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`, while Paper III remains frozen unless a real contradiction is found.

## 7. Reproducibility

Run

`python analysis/paper3_scientific_closure_iteration128.py`.

The checker verifies the presence of the canonical closure authorities and explicitly keeps the apparatus-specific numerical extension outside the completed scientific criteria.