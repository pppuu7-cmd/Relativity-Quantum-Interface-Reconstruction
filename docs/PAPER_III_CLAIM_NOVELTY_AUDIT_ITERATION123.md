# RQIR Iteration 123 — Paper-III Claim / Novelty Boundary Audit

**Date:** 2026-08-31  
**Status:** manuscript-facing literature/claim discipline. No new-physics claim.

## 1. Purpose

Paper III is close enough to scientific closure that the main risk is no longer only a missing equation. A publication can also fail by claiming novelty for ingredients that are already standard or by conflating an RQIR-specific synthesis with prior gravity proposals.

This iteration classifies the central Paper-III ingredients into:

1. standard statistical/experimental-design machinery;
2. prior gravity-test/resource literature;
3. external experimental precedent;
4. RQIR candidate novelty that may be claimed only after final priority search.

## 2. Standard ingredients — cite, do not claim as RQIR inventions

### Profiled Fisher / Schur complement

Partitioning a Fisher matrix into parameters of interest and nuisance parameters and maximizing the nuisance-profiled Schur complement is standard optimal-design methodology. For example, Fisher-optimal MRI design explicitly uses the Schur complement to optimize a parameter of interest while accounting for nuisance parameters.

Therefore RQIR must **not** claim invention of

`F_beta|theta = F_bb-F_btheta F_thetatheta^-1 F_thetab`.

The RQIR contribution, if novel, lies in what physical gravity-interface scores enter this matrix and how the resulting profile is connected to calibration/source/control resources.

### Fisher-optimal experiment allocation

Optimal experimental design based on Fisher information, selection of measurement times/settings, and allocation of experiments to achieve a target precision at minimum cost are established fields. Modern work explicitly optimizes observation schedules under correlated noise and model-calibration uncertainty.

Therefore RESOURCE-057/083 should be described as **RQIR specializations/derivations of optimal-design structure**, not as the first use of Fisher allocation or convex experiment design.

## 3. Prior gravity-test/resource literature — distinguish the RQIR target

### Gravity-mediated entanglement

Bose et al. (PRL 119, 240401, 2017) and Marletto & Vedral (PRL 119, 240402, 2017) established the gravity-mediated entanglement witness route.

Subsequent QGEM studies already estimate measurement counts, decoherence thresholds and optimized witness schedules. Tilly et al. (PRA 104, 052416, 2021), for example, reports order `10^3` measurements in a favorable no-decoherence configuration and much larger counts when decoherence becomes important.

Thus Paper III must not claim to be the first gravity-quantum proposal to translate a quantum-gravity discriminator into shots or decoherence requirements.

RQIR differs by targeting **model-class reconstruction and detector-level nuisance identifiability**, rather than assuming entanglement itself is the discriminator.

### Classical/hybrid gravity alternatives

Classical-channel gravity and later classical-quantum/postquantum frameworks already predict experimentally relevant decoherence, stochasticity or diffusion. Oppenheim et al. (Nature Communications 14, 7910, 2023) derives a generic decoherence-versus-diffusion trade-off for consistent classical-quantum dynamics and proposes experimental figures of merit.

Hence RQIR must not imply that classical/stochastic alternatives were previously devoid of operational predictions.

RQIR's intended role is to place such alternatives, semiclassical models, stochastic models, hybrid models and quantum-gravity candidates into a common observable/likelihood reconstruction pipeline whenever their predictions can be mapped into it.

## 4. External experimental precedent — cite as feasibility, not theory novelty

The Iteration-122 apparatus audit identifies prior experimental demonstrations of

- calibrated transfer-function force-sensitivity spectra;
- multimode PSD/cross-spectrum measurements;
- feedback gain/phase control and cross-talk suppression;
- exact simultaneous fundamental/second-harmonic mechanical operation.

These establish feasibility of ingredients. They are not RQIR discoveries.

## 5. RQIR candidate-novelty layer

The following claims survive the first novelty-boundary audit as **candidate RQIR contributions**, but priority must still be checked before final manuscript wording.

### NOVELTY-CANDIDATE-001 — ordered interface reconstruction as the primary inverse problem

RQIR begins from

`P_data(o|s) -> [operational gravity-interface class]`

rather than selecting a gravity model first. The ordered hierarchy involving mean source, noise/symmetric correlations and ordered/retarded response is treated as the object to reconstruct.

The claim is not that stress-energy means, noise kernels or response functions are individually new. The candidate novelty is their use as an ordered **model-agnostic reconstruction hierarchy with explicit finite discriminants and no-go boundaries**.

### NOVELTY-CANDIDATE-002 — finite nullspace source design linked to detector identifiability

The Toy001–014 program constructs source pairs/settings designed to be exactly degenerate under lower interface levels while separated by higher ordered information, then propagates these nullspace discriminants through nuisance-profiled detector Fisher geometry.

The novelty claim should concern the integrated finite-design methodology, not linear algebra nullspaces themselves.

### NOVELTY-CANDIDATE-003 — source-calibration + detector-profile + wall-clock chain

RQIR explicitly refuses to equate exact theoretical separation with experimental identifiability. Independent source-preparation metrology, detector calibration, cross-PSD, transfer gain/phase, control recertification, acceptance/reset/coherence and wall time are connected to the same final profiled discriminator.

The candidate novelty is the **end-to-end gravity-interface resource certificate**, not any one metrology formula.

### NOVELTY-CANDIDATE-004 — architecture certificate `(u,v,z,delta)` under final significance

The Toy009/Toy014 comparison is compressed only after the likelihood/profile is fixed, into detector-rate, source-rate and duty variables, with robust interval guards. This supplies an architecture-selection criterion that explicitly prevents a source design from winning merely because one omitted resource is hidden.

Again, ratio algebra is not itself a novelty; the candidate contribution is its role inside the RQIR reconstruction pipeline.

### NOVELTY-CANDIDATE-005 — likelihood-derived transfer recertification

Iterations 112–121 derive transfer calibration tolerances from loss of the profiled science Fisher itself, reduce two-band gain uncertainty through the common-gain/tilt quotient, prevent reference-time double counting, and propagate calibration-span/backaction uncertainty to a robust detector-rate interval.

The candidate novelty is this likelihood-to-control-recertification chain for a gravity-interface discriminator.

## 6. RQIR-NG-081 — novelty must be claimed at the integration level

> Generic Fisher information, Schur complements, convex/optimal experiment allocation, gravity-mediated entanglement resource estimates, cross-spectral force sensing and classical-gravity decoherence predictions all have substantial prior literature. Paper III must not claim novelty for these ingredients in isolation.

The strongest defensible RQIR novelty claim is presently the **specific integrated reconstruction/resource architecture** connecting finite interface discriminants to source calibration, detector nuisance profiling, transfer/control certification and robust wall-clock requirements.

## 7. Claim-evidence ladder for the manuscript

Every major Paper-III statement should be tagged internally as one of:

- **THEOREM/DERIVATION:** exact algebra proved in the repository;
- **DETERMINISTIC REGRESSION:** numerical result for a declared toy model with fixed seed/coordinates;
- **EXPERIMENTAL PRECEDENT:** capability demonstrated externally, not an RQIR apparatus forecast;
- **PARAMETRIC SPECIFICATION:** exact formula awaiting physical apparatus inputs;
- **OPEN GATE:** unresolved consistency, measurement or hardware requirement;
- **CANDIDATE NOVELTY:** potentially original integration/result, requiring final priority search.

### RQIR-CAL-024 — no claim-class mixing

A deterministic toy regression must not be worded as an experimental forecast; experimental precedent must not be worded as validation of the RQIR signal; and a parametric certificate must not be given an invented numerical apparatus value.

## 8. Implication for Candidate Gravity

The novelty audit also sharpens the future Candidate-Gravity branch. A concrete candidate cannot claim novelty merely by reproducing a standard weak-field coupling such as `h_mn T^mn`, by using a Lindblad channel, or by predicting decoherence.

Its novelty would have to reside in a concrete consistent dynamics and/or a genuinely new derived relation that survives QG-001…QG-010 and is distinguishable from semiclassical, stochastic, classical-channel/postquantum and ordinary perturbative-QG alternatives.

This makes the RQIR repository slightly more ready to **evaluate** a future candidate, without advancing the candidate model itself.

## 9. Readiness snapshot after Iteration 123

Project-management estimates, not statistical quantities.

- **Repository readiness for writing Paper III — scientific content:** **95%**.
- **Paper III submission-ready state:** **81%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **85%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

Scientific content stays at 95% because this iteration does not close the remaining apparatus-rate gaps. Submission readiness rises because the novelty/claim boundary and several required prior-literature anchors are now explicit. Candidate-Gravity start readiness rises slightly because the comparator/novelty boundary for a future model is clearer; the actual model remains unconstructed.

## 10. Next admissible gate

Build a manuscript-ready Paper-III skeleton from the now-mature results:

1. one central claim per section;
2. exact supporting equations/results;
3. corresponding regression figure/table target;
4. literature comparator/citation target;
5. explicit limitation/open gate.

This can expose any final missing scientific link before prose drafting. In parallel, update the Candidate-Gravity entry checklist with the clarified comparator classes, but do not activate a model claim yet.

## 11. Reproducibility

Run

`python analysis/paper3_claim_evidence_matrix_iteration123.py`.

The script enforces that generic Fisher/OED/prior-gravity/experimental-precedent ingredients are not tagged as RQIR novelty and restricts candidate novelty to the integrated repository-specific constructions pending final priority review.
