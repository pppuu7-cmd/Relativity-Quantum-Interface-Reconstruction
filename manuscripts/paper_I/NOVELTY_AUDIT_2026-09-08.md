# RQIR Paper I — targeted novelty audit

Date: 2026-09-08
Status: targeted prior-art audit; not a substitute for a final database/expert literature review

## Narrow novelty target

The manuscript should not claim novelty for any isolated ingredient below. The candidate contribution is the conjunction:

1. a **declared finite calibration map** acting on physically admissible source-state perturbations;
2. a **physical calibration null direction** retained inside the positive-state set;
3. an explicit **positivity-preserving pair** of calibration-equivalent states;
4. a **separate ordered/retarded-response functional** evaluated on that calibration nullspace;
5. a constructive detector-facing witness of the same hidden direction; and
6. **calibration steering**, in which perturbing the calibration geometry rotates the unresolved direction and changes the surviving response coordinate.

The theorem itself is an elementary finite-dimensional existence result. The intended novelty is its operational packaging and use at the gravity–quantum source interface, not a claim of new linear algebra.

## Search classes checked

### A. Informationally incomplete quantum tomography

Relevant close prior art:

- D'Ariano, Paris & Sacchi (2003), general quantum tomography.
- Teo, Řeháček & Hradil (2013), informationally incomplete tomography.
- Gonçalves et al. (2013), state estimation with incomplete data.
- Lyyra, Kuusela & Heinosaari (2019), conclusive membership information from incomplete tomography.

Overlap: finite measurements need not uniquely determine a global state; incomplete data can define equivalence/feasible sets or still answer restricted questions.

Difference from Paper I: these works do not, in the checked formulations, define a gravity–quantum source calibration quotient and then evaluate a separate ordered stress-energy response discriminant on a physical null direction.

### B. Positivity-constrained reconstruction

Relevant close prior art:

- Kalev, Kosut & Deutsch (2015), positivity can turn compressed-sensing measurement records into a stronger form of informational completeness.

Overlap: positivity can radically change the feasible set of states compatible with a measurement map.

Difference from Paper I: RQIR uses interior positivity in the opposite logical direction: given an allowed null perturbation, it constructs a sufficiently small positive pair that remains inside one declared calibration-equivalence class. It is not a compressed-sensing recovery theorem and does not claim positivity generically preserves ambiguity.

### C. Kernels and invertibility of retarded response functions

Relevant close prior art:

- Giesbertz (2015), invertibility/kernel conditions for retarded response functions for Laplace-transformable perturbations.
- Giesbertz (2016), extension to mixed states/ensembles.

Overlap: explicit analysis of kernels associated with retarded linear response.

Critical distinction: the kernel in these works is a kernel of the **dynamical response map** from perturbing potentials to observables. In RQIR-THM-001, `ker A` is the kernel of a **finite calibration map on source-state perturbations**. The response functional `c` is then evaluated on `ker A`; it is not itself the map whose kernel defines the equivalence class.

### D. Calibration/nuisance quotient geometry

Relevant close prior art:

- Wani & Al-Kuwari (2026), *Quantum speed limit under calibration uncertainty*, which profiles nuisance directions in a quantum Fisher metric and formulates a quotient-state-space speed limit.

Overlap: calibration/nuisance ambiguity is handled geometrically by quotienting operationally redundant directions.

Difference from Paper I: Wani–Al-Kuwari quotient parameter-estimation/nuisance directions in an information metric. Paper I starts from an experimentally declared finite source calibration map, identifies its physical nullspace, and asks whether an ordered-response coordinate survives that source-level quotient. The Wani–Al-Kuwari framework is closer to RQIR Paper II's nuisance-profiled information geometry than to RQIR-THM-001.

### E. Quantum-clock gravity probes

Relevant anchors:

- Roura (2020), gravitational redshift in quantum-clock interferometry.
- Wakakuwa (2026), post-Newtonian classical/quantum gravity via quantum-clock interferometry.

These close a literature-coverage gap in the introduction but do not materially overlap the theorem.

## Searches that did not reveal an exact match

Targeted searches combined terms corresponding to:

- calibration nullspace + density matrix / positive states;
- calibration-equivalent quantum states + response;
- finite calibration map + quantum;
- ordered/retarded response + tomography/nullspace;
- same finite measurement record + different susceptibility/response;
- physical null direction + quantum state;
- quotient calibration uncertainty + quantum response.

The searches found the neighboring classes above but did not reveal a publication containing the full Paper-I conjunction.

## Current novelty judgment

**Status: AMBER-GREEN.**

The targeted audit supports a defensible narrow novelty statement, but it is not sufficient to assert exhaustive priority. The manuscript should say that its contribution is the **combined calibration-aware construction**, not that nullspaces, positivity, retarded-response kernels, quantum tomography or quotient geometry are individually new.

Recommended language:

> The contribution is conjunctive rather than elemental: we combine a finite source calibration quotient on physically admissible states with a positivity-preserving response-distinct pair, evaluate an ordered-response discriminant on the unresolved direction, and treat calibration geometry as a controllable steering variable.

Avoid language such as "first ever use of a nullspace", "new positivity theorem", "new retarded-response kernel theorem", or "first quotient treatment of calibration uncertainty".

## Remaining closure before submission

1. Run a final scholarly-database sweep using the same conjunction across Crossref/OpenAlex/INSPIRE/Google Scholar-equivalent indexing where available.
2. Search citation neighborhoods of the closest works, especially Kalev et al. 2015, Giesbertz 2015/2016 and Wani–Al-Kuwari 2026.
3. If an earlier close conjunction is found, narrow the RQIR novelty claim to the gravity–quantum operational application and constructive calibration-steering certificate rather than overclaim priority.
4. Keep the claims/non-claims boundary synchronized with `CLAIMS_EVIDENCE_MATRIX.md`.
