# Candidate Gravity Reference Ansatz — Iteration 133

**Date:** 2026-08-31  
**Model:** `ANSATZ-PQG-EFT-001` v0.1  
**Status:** retained reference/control; not promotable to `QGxxx`.

## Goal

Exercise the Candidate Gravity gate process on a real coherent dynamics before attempting a novel construction. Use standard low-energy perturbative quantum GR EFT with a minimally coupled scalar as a control model.

## Core model

`S = int sqrt(-g) [2R/kappa^2 - 1/2 g^mn d_m phi d_n phi - 1/2 m^2 phi^2] + S_GF + S_ghost + S_EFT`,

with `g=eta+kappa h`, `kappa=sqrt(32 pi G)`.

The first-order coupling is the universal stress-tensor coupling

`S_int^(1)=-(kappa/2) int h_mn T^mn`.

Thus the RQIR source hierarchy is derived from one dynamics:

- `J=<T>`;
- centered symmetrized `N=1/2 <{delta T,delta T}>`;
- retarded `chi^R=-i theta <[T,T]>`;
- higher connected functions from the same CTP/SK generating functional.

## Gate results

### QG-001 — PASS

A perturbative matter x graviton state space is specified about asymptotically Minkowski boundary data, with gauge/BRST unphysical sectors distinguished from physical states. Coordinate components of `h_mn` are not automatically RQIR observables.

### QG-002 — PASS

One covariant action fixes matter, gravity and their interaction. RQIR-facing kernels may not be independently tuned.

### QG-007 — FAIL

This ansatz is deliberately identical at theory-class level to baseline comparator C5: low-energy perturbative quantum gravity EFT.

Therefore no independent model label `beta` distinguishes the ansatz from C5. In the class-indicator representation,

`beta_class = I_ansatz - I_C5 = 1 - 1 = 0`.

No Paper-I finite discriminator, Paper-II positive profiled Fisher or Paper-III resource certificate can be generated for a nonexistent C5-distinguishing parameter direction.

**CG-NG-003 — exact reference-comparator degeneracy:** a standard perturbative quantum-GR EFT reference cannot satisfy QG-007 as a novel Candidate Gravity against comparator C5. Detector optimization cannot repair theory-class identity.

This negative result is permanent for this model version. Changing the dynamics enough to evade C5 creates a new ansatz/version.

## Why this is useful

The first use of the frozen Candidate Gravity process has rejected a tempting but invalid promotion route: merely quantizing the linearized metric or using a graviton mediator does not by itself define a new RQIR Candidate Gravity.

The branch remains valuable as:

1. a standard quantum-gravity reference;
2. a source-hierarchy normalization/control;
3. a future comparator for genuinely distinct candidates;
4. a test bed for QG-003/QG-005/QG-006 consistency derivations.

## Literature anchors

- Donoghue, Phys. Rev. D 50, 3874 (1994), arXiv:gr-qc/9405057: GR as low-energy quantum EFT.
- Donoghue, arXiv:1209.3511: EFT treatment of quantum gravity.
- Hu & Verdaguer, arXiv:0802.0658: CTP/noise-kernel/stochastic-gravity relation used to define comparator boundaries.

## Reproducibility

Run:

`python analysis/candidate_gravity_reference_ansatz_iteration133.py`

Expected structural result:

- QG-001 PASS;
- QG-002 PASS;
- QG-007 FAIL / `REFERENCE_DEGENERACY_C5`;
- promotion disabled.

## Next gate

Use this reference branch to perform the controlled Newtonian/classical-GR limit audit (QG-003). This validates conventions and normalizations but cannot undo CG-NG-003.
