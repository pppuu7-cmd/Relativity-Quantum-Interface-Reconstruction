# RQIR Research Log — Candidate Gravity Iterations 136–140

**Date:** 2026-08-31  
**Purpose:** preserve the complete decision chain from first RQIR-driven candidate rejection through existing-model funnel audit and second-candidate C5 degeneracy result.

## Iteration 136 — reject first RQIR-driven ansatz

Frozen model: `ANSATZ-RQIR-CTP-001` v0.1.

For `0<y=p^2/M_*^2<1`,

`F(y)=-y exp(1-y)E1(1-y)`

is continuous, strictly decreasing, `F(0)=0`, and `F->-infinity` as `y->1-`.

Therefore every `beta>0` forces exactly one root of

`1+beta F(y)=0`.

Since `F'(y)<0`, the additional pole has opposite residue sign in the frozen spin-2 convention.

Decision: **QG-004 FAIL / REJECT v0.1**.

Retained result: `CG-NG-004`.

## Iteration 137 — existing-model funnel audit

Audited first-wave comparator classes:

- semiclassical mean gravity;
- stochastic gravity;
- classical-channel/measurement-feedback gravity;
- postquantum classical gravity;
- perturbative quantum GR EFT;
- ghost-free nonlocal/form-factor gravity;
- asymptotic safety.

Key classification principle:

`consistency failure != novelty failure != operational blocking`.

Prepared article-ready section:

`docs/CANDIDATE_GRAVITY_ARTICLE_FUNNEL_SECTION_ITERATION137.md`.

## Iteration 138 — second RQIR-driven ansatz

Created `ANSATZ-RQIR-KL-002` v0.1.

Architecture:

- unchanged massless GR spectral delta;
- smooth nonnegative gapped continuum;
- retarded transfer defined directly by positive spectral measure;
- no isolated added continuum pole at Gaussian level.

Scoped positivity/static checks PASS.

## Iteration 139 — tensor restoration

Restored conserved-source tensor exchange:

massless:

`T.T'-(1/2)TT'`,

massive continuum:

`T.T'-(1/3)TT'`.

Consequences:

- NR continuum/GR tensor ratio `4/3`;
- static potential `Phi=-GM/r[1+(4/3)beta W]`;
- traceless-probe response relative to NR-calibrated continuum `3/4`.

This is a known vDVZ-type tensor signature and is retained as a cross-channel RQIR relation.

No nonlinear Vainshtein mechanism is assumed.

## Iteration 140 — C5 infrared degeneracy

For the candidate continuum below threshold,

`C(x)=int ds rho(s)/(s+x)`

has a convergent analytic expansion for `|x|<1`:

`C(x)=sum (-x)^n A_(n+1)`.

Therefore at any fixed finite derivative order the beta contribution is exactly representable by local gravitational EFT Wilson coefficients.

Decision:

- do not reject `KL-002`;
- reject the **deep-IR finite-order regime as a discovery regime**;
- QG-007 becomes PARTIAL_NEGATIVE;
- QG-008 is BLOCKED_REGIME until threshold/cross-channel observables are built.

Retained result: `CG-NG-005`.

## Existing literature role

The comparison audit uses standard/current literature showing:

- stochastic gravity derives noise/dissipation via CTP/influence-functional methods;
- classical-channel gravity links Newtonian interaction to decoherence and cannot generate entanglement in the standard measurement-feedback construction;
- current postquantum classical-gravity models produce stochastic metric modes and observable spectra;
- specific nonlocal/form-factor gravity models can avoid extra poles and admit positive spectral representations;
- asymptotic-safety phenomenology and Lorentzian spectral work are active and must be instantiated concretely before RQIR testing;
- standard gravitational EFT contains mandatory nonanalytic low-energy quantum corrections from massless propagation.

## Scientific interpretation after Iteration 140

The project now has three qualitatively distinct model outcomes:

1. `ANSATZ-PQG-EFT-001`: viable reference, fails novelty by exact C5 identity;
2. `ANSATZ-RQIR-CTP-001`: fails consistency analytically and is rejected;
3. `ANSATZ-RQIR-KL-002`: passes early consistency screens but fails C5 distinctness in the deep-IR finite-order regime.

This staged structure is publication-useful even before a final model survives the full funnel.

## Frozen next work

Iteration 141 must define a C5-excess spectral direction and attack it with the strongest continuum comparators before any detector optimization.
