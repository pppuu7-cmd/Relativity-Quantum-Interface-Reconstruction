# RQIR Iteration 127 — Final Literature / Priority Audit for Paper III

**Date:** 2026-08-31  
**Status:** final manuscript-facing priority audit. This is a finite literature search, not a proof of priority and not a new-physics claim.

## 1. Question

Before scientific closure, does the current literature contain the same end-to-end object claimed by Paper III, or do the closest works cover only constituent methods / alternative gravity-test architectures?

The audited RQIR chain is:

`interface discriminator -> exact constraints/source calibration -> nuisance-profiled detector likelihood -> PSD/cross-PSD + transfer calibration -> calibration span/backaction/no-double-counting -> physical Fisher rates -> robust wall-clock -> final architecture certificate`.

## 2. Nuisance-aware Fisher / optimal experimental design is established prior art

Schur-complement and Fisher-information methods are standard tools in parameter estimation and optimal experimental design. Examples include:

- A. Bürger et al., *A Schur Complement Method for Optimum Experimental Design in the Presence of Process Noise*, IFAC-PapersOnLine 50 (2017), DOI `10.1016/j.ifacol.2017.08.1853`.
- N. N. Lam, P. D. Docherty, R. Murray, *Practical identifiability of parametrised models: A review of benefits and limitations of various approaches*, Mathematics and Computers in Simulation 199 (2022), DOI `10.1016/j.matcom.2022.03.020`.
- modern model-calibration/OED literature explicitly uses Fisher information to design experiments under uncertainty.

Therefore Paper III must not claim novelty for the Schur complement, Fisher profiling, convex campaign allocation or OED as mathematical techniques by themselves.

## 3. Quantum-gravity laboratory-test design is also established prior art

The literature contains mature resource/feasibility discussions for gravity-mediated entanglement and related schemes. Relevant comparators include:

- Marletto & Vedral, *Quantum-information methods for quantum gravity laboratory-based tests*, arXiv:2410.07262 (2024), a review of information-theoretic laboratory tests including gravitational entanglement.
- Schut et al., *Relaxation of experimental parameters in a quantum-gravity-induced entanglement of masses protocol using electromagnetic screening*, Phys. Rev. Research 5, 043170 (2023), DOI `10.1103/PhysRevResearch.5.043170`.
- Krisnanda et al., *Observable quantum entanglement due to gravity*, npj Quantum Information 6, 12 (2020), DOI `10.1038/s41534-020-0243-y`, which estimates experimental parameters for gravitationally induced entanglement.

The 2025 Nature paper by Aziz & Howl, *Classical theories of gravity produce entanglement*, DOI `10.1038/s41586-025-09595-7`, further demonstrates why a simple statement “observed entanglement implies quantized gravity” is not a sufficient universal discriminator once broader matter/gravity model classes are admitted.

This strengthens RQIR's requirement for explicit alternative-model degeneracy audits rather than supplying novelty by itself.

## 4. Classical / stochastic / postquantum gravity already has experimentally targeted observables

Important comparators include:

- Oppenheim et al., *Gravitationally induced decoherence vs space-time diffusion: testing the quantum nature of gravity*, Nature Communications 14, 7910 (2023), DOI `10.1038/s41467-023-43348-2`, deriving a decoherence/diffusion tradeoff for classical-quantum dynamics.
- Kryhin & Sudhir, *Distinguishable Consequence of Classical Gravity on Quantum Matter*, Phys. Rev. Lett. 134, 061501 (2025), DOI `10.1103/PhysRevLett.134.061501`, proposing experimentally relevant cross-correlation / phase-response observables that distinguish a consistent classical-gravity hypothesis from quantum gravity and naive decoherence.
- Stefanov et al., *Testing classicality of gravity by gravitation decoherence*, Phys. Rev. D 111, 065026 (2025), DOI `10.1103/PhysRevD.111.065026`.
- Oppenheim & Sajjad, *Stochastic modes in postquantum classical gravity*, arXiv:2605.05375 (2026), deriving stochastic metric modes and PSDs in a postquantum classical-gravity framework.

Hence Paper III cannot claim that resource-aware experimental discrimination of classical/stochastic gravity is unique to RQIR in broad terms.

## 5. Measurement-disturbance and interferometric nonclassicality tests are active alternatives

Comparators include:

- *Testing Whether Gravity Acts as a Quantum Entity When Measured*, Phys. Rev. Lett. 133, 180201 (2024), DOI `10.1103/PhysRevLett.133.180201`, which targets irreducible measurement disturbance without requiring gravity-mediated entanglement.
- Liu et al., *Testing the quantum nature of gravity through interferometry*, Phys. Rev. D 113, 022002 (2026), proposing a Michelson-type protocol for testing whether gravity can consistently remain classical.

These establish that RQIR is one member of a broader class of model-discrimination strategies; novelty must be formulated at the level of the reconstruction/resource architecture, not the general aim of testing gravity's quantum character.

## 6. Detector transfer / force calibration / multimode sensing is established instrumentation prior art

Force-sensing literature already calibrates transfer functions and converts displacement spectra into force sensitivity. For example, the levitated-nanomechanical calibration work *Force detection sensitivity spectrum calibration of levitated nanomechanical sensor using harmonic Coulomb force* explicitly measures transfer functions and calibrated force-sensitivity spectra.

Recent levitated optomechanics also demonstrates concurrent multimode and fundamental/second-harmonic control, including the 2026 Nature Communications work *Thermomechanically squeezed multi-mode phonon lasers with levitated optomechanics* (Nature Communications 17, 8852, 2026; DOI associated with article `s41467-026-75601-9`).

These are component precedents. Iteration 122 remains authoritative that the searched public literature did not provide one compatible same-state dataset containing the full RQIR closure vector.

## 7. Finite-search result

Across the comparator classes checked in Iterations 123 and 127, no inspected source was found that explicitly combines all of the following in one gravity-interface reconstruction workflow:

1. model-agnostic ordered source-information discriminant;
2. exact finite calibration/nullspace construction;
3. detector-level nuisance-profiled Fisher identifiability;
4. independent source-amplitude metrology forced by an exact multiplicative degeneracy;
5. same-state two-band transfer and cross-PSD treatment;
6. calibration score-span / backaction / no-double-counting resource gates;
7. conversion to shots, coherence/reset/duty and physical Fisher rates;
8. robust final wall-clock architecture certificate with unresolved-apparatus intervals explicitly preserved.

### RQIR-PRIORITY-001 — finite-search candidate novelty statement

The defendable candidate contribution of Paper III is the **RQIR-specific end-to-end integration and closure discipline**, not any constituent Fisher/OED, force-sensing, QGEM, decoherence/diffusion or system-identification technique.

This is a finite-search conclusion, not a proof that no related paper exists. The literature search must be refreshed before submission.

## 8. Wording allowed in the manuscript

Safe wording:

> “We develop an end-to-end resource-certificate formulation specialized to the RQIR interface-discrimination problem, integrating source-amplitude metrology, detector nuisance profiling, same-state transfer/cross-spectral calibration, calibration-span/backaction constraints, and robust wall-clock architecture comparison.”

Avoid:

- “first use of Fisher information to test quantum gravity”;
- “first resource analysis of a quantum-gravity experiment”;
- “entanglement uniquely proves quantized gravity”;
- “first use of transfer-function calibration / cross spectra / OED”;
- “a numerical apparatus prediction” without a compatible closure dataset.

## 9. Novelty risk register

| Risk | Status after audit |
|---|---|
| Schur/Fisher/OED claimed as new | CLOSED — explicitly prior art |
| gravity-test resource accounting claimed as new generically | CLOSED — prior QGEM/other resource literature exists |
| classical/stochastic comparator omitted | CLOSED at literature-boundary level; must still be included in model-specific future likelihoods |
| transfer/cross-spectrum instrumentation claimed as new | CLOSED — component prior art acknowledged |
| exact end-to-end RQIR chain already found elsewhere | **not found in inspected finite search**, but priority not proven |
| apparatus-specific runtime claimed | FORBIDDEN until closure vector supplied |

## 10. Readiness snapshot — Iteration 127

Project-management estimates, not statistical confidence measures:

- **Paper III scientific-content readiness:** **99%**.
- **Paper III submission readiness:** **96%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **87%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

The final 1% is a formal scientific-closure audit: verify the frozen scope against Iterations 079/104/115/121/124–127, enumerate explicit limitations, and certify that no remaining open item is required for the stated Paper-III claim.

## 11. Next gate

Issue **Paper III Scientific Closure** only if all of the following are true:

- canonical notation is frozen;
- minimum regressions are manifest and reproducible in the repository layout;
- novelty wording is bounded by prior art;
- apparatus-specific numerical closure is explicitly outside the scientific-scope requirement;
- all remaining open controls/data are presented as conditional extension inputs rather than hidden assumptions;
- no claim of new gravity physics is made.