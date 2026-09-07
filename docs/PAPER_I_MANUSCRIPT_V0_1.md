# Relativity–Quantum Interface Reconstruction I

## Operational Hierarchy, Ordered Stress-Energy Information, and Finite Nullspace Discriminants

**Manuscript:** v0.1  
**Started:** 2026-09-08  
**Scientific scope:** CLOSED at RQIR Iteration 078  
**Editorial status:** active draft; not submission-ready  
**Novelty/priority wording:** provisional pending dedicated literature audit  
**Authors:** TBD

---

## Abstract — v0.1

The interface between relativistic gravitation and quantum matter is commonly discussed by comparing candidate microscopic theories or by proposing individual signatures of gravitational quantumness. Here we formulate a complementary operational reconstruction problem: which components of quantum source information are, in principle, distinguishable after passage through a gravity–matter interface and a declared calibration map? We separate the one-point stress-energy source `J=<T>` from the centered symmetrized noise kernel `N`, the antisymmetric/commutator sector `D`, and the associated retarded response `chi^R`, treating these as projections of a common closed-time-path source object rather than as interchangeable second-order data. We then study finite calibration maps on physically admissible source-state perturbations. A finite-dimensional theorem shows that if the calibration map has a physical null direction on which an ordered-response functional is nonzero, then two positive source states can agree on all declared calibration observables while differing in that response. Constructive RQIR toy models realize this separation and show that the hidden direction can be rotated by calibration geometry. The result is an information-structure statement, not evidence that gravity is quantized: semiclassical, stochastic, classical, hybrid and full-QFT matter alternatives must still be tested at the level of the complete observable map. The framework therefore separates operational distinguishability from ontological interpretation and provides the source-side foundation for the statistical-identifiability analysis developed in Paper II.

---

## 1. Introduction — working draft

Reconciling gravity with quantum theory is usually approached from one of two directions. One begins with a candidate fundamental framework and asks for its low-energy or experimentally accessible predictions. The other starts from a proposed laboratory signature—an interferometric phase, an entanglement witness, a decoherence channel, a clock observable, a fluctuation spectrum—and asks whether the signal would establish that gravity itself possesses quantum degrees of freedom.

Both strategies are scientifically useful, but they create a recurrent inverse-problem ambiguity. A measured signal is generated not only by a microscopic gravity model but by a chain containing state preparation, matter dynamics, gravitational response, calibration, detector transfer, noise, nuisance parameters and data reduction. Distinct microscopic descriptions can therefore be operationally degenerate, while apparently similar source statistics can contain different ordered quantum information. Conversely, a nonclassical-looking observable need not uniquely identify quantum gravitational degrees of freedom.

Relativity–Quantum Interface Reconstruction (RQIR) addresses this ambiguity by reversing the usual order of construction. Rather than choosing a preferred quantum-gravity theory at the outset, we first ask what information a gravity–quantum interface would have to transmit for different operational claims to become distinguishable. The object of inference is therefore an equivalence class of interface maps compatible with the measured probability law,

`P_data(o|s) -> [I]`,

not an assumed microscopic theory label.

Paper I develops the source-side and finite-discriminant layer of this programme. Its central question is deliberately narrower than “is gravity quantum?”:

> **What source information can remain operationally distinct after a declared finite calibration map?**

The answer requires preserving operator ordering. At second order, the expectation value of the stress tensor, its symmetrized fluctuations, and its commutator/retarded-response sector are not generally equivalent data. A calibration protocol can match a finite set of means and noise observables while leaving a physical direction that changes an ordered-response functional. We formalize this statement as a finite-dimensional nullspace theorem and exhibit constructive positive-state examples.

This conclusion must be interpreted conservatively. It does not assert that gravity couples to the commutator or retarded stress-energy response in nature. It does not make a nonzero matter commutator a signature of quantum geometry. It does not establish that an entanglement signal is uniquely gravitationally quantum. Those are model-comparison questions that require additional interface dynamics and comparator analysis. The purpose of Paper I is instead to establish the operational information hierarchy that later papers subject to nuisance profiling, resource closure and model comparison.

A recent result by Aziz and Howl showing that local classical-gravity theories with full-QFT matter can generate entanglement reinforces the need for this discipline: an apparently quantum-information-bearing observable need not by itself identify a quantized gravitational mediator. The appropriate target is therefore a multi-layer operational discriminator with explicit comparator and degeneracy control.

### 1.1 Contributions of this paper

Within its frozen scientific scope, Paper I establishes the following:

1. a source-side ordered hierarchy separating `J`, `N`, `D`, `chi^R` and higher CTP information;
2. an explicit rule that matching means and symmetrized noise does not algebraically imply matching the ordered/response sector without an additional physical identity;
3. a finite nullspace theorem guaranteeing positive source-state pairs with identical declared finite calibration data but distinct response when a suitable physical null direction exists;
4. constructive finite-dimensional RQIR realizations of this theorem;
5. a calibration-steering result showing that the hidden discriminant direction depends on calibration geometry;
6. a strict boundary between source-side operational distinguishability and any claim about the ontology of gravity;
7. a bridge to Paper II, where exact separation is replaced by nuisance-profiled statistical identifiability.

### 1.2 Non-claims

Paper I does **not** claim:

- empirical evidence for new physics;
- empirical evidence that gravity is quantized;
- that gravity necessarily transmits `D` or `chi^R`;
- that stochastic gravity is equivalent to a quantum theory of geometry;
- that entanglement alone is a sufficient witness of quantum gravity;
- relativistic completeness of the finite toy models;
- detector-level statistical identifiability after uncertain source preparation and nuisance profiling;
- apparatus-specific feasibility or wall-clock closure.

These exclusions are part of the result rather than disclaimers appended after the fact.

---

## 2. Operational reconstruction of the gravity–quantum interface

Let `O={O_A}` denote operational observables. The index `A` is understood to include the source preparation, smearing or coarse graining, detector transfer, experimental setting and any renormalization prescription required for the observable to be meaningful.

For an explicit baseline `B` in domain `D`, define

`Delta_A^(B)(D) = O_A^obs(D) - O_A^(B)(D)`.

RQIR does not combine residuals defined relative to different baselines without an explicit map. Possible controlled baselines include classical GR, QFT on a prescribed curved background, semiclassical gravity and low-energy gravitational EFT.

Abstractly, the interface is represented as

`I : (rho_matter, G, C, lambda) -> P(o|s)`,

where `G` denotes gravitational/interface degrees of freedom or effective variables, `C` denotes constraints and consistency structure, and `lambda` denotes model and nuisance parameters. Operational reconstruction asks which equivalence class `[I]` remains compatible with data after all declared nuisance and comparator freedoms are included.

Paper I isolates an earlier step: before assigning a microscopic interface, determine which source-side information coordinates are distinct and which can be eliminated by calibration.

---

## 3. Ordered stress-energy information hierarchy

Define the centered source operator

`delta T_A(x) = T_A(x) - <T_A(x)>`.

### 3.1 One-point source

`J_A(x) = <T_A(x)>`.

A mean-field semiclassical equation uses this object as its source, schematically

`G_mn + Lambda g_mn + H_mn^EFT = 8 pi G <T_mn>_ren`.

This equation is an important baseline, but the one-point function does not exhaust the quantum source information.

### 3.2 Greater and lesser correlators

`G^>_AB(x,y) = <delta T_A(x) delta T_B(y)>`,

`G^<_AB(x,y) = <delta T_B(y) delta T_A(x)>`.

### 3.3 Symmetrized/noise sector

`N_AB(x,y) = (1/2)<{delta T_A(x),delta T_B(y)}>`

so that

`N = (G^> + G^<)/2`.

The noise kernel is central to stochastic gravity. In the influence-functional/Einstein–Langevin formulation, stress-energy fluctuations induce stochastic metric fluctuations while the full open-system construction also carries response/dissipation information. This already demonstrates that a second-order gravity–quantum interface cannot in general be represented by one undifferentiated covariance object.

### 3.4 Antisymmetric/commutator sector

`D_AB(x,y) = (1/2i)<[delta T_A(x),delta T_B(y)]>`

with

`G^> - G^< = 2 i D`.

### 3.5 Retarded response

With a fixed sign convention,

`chi^R_AB(x,y) = (i/hbar) theta(x0-y0) <[T_A(x),T_B(y)]>`.

Thus the retarded response is causally constructed from the commutator sector, up to the declared convention.

### 3.6 Ordering-preservation rule

The crucial algebraic point is simple:

> Matching `J` and `N` does not imply matching `D` or `chi^R` unless an additional physical identity, commutativity condition, spacelike-separation statement, equilibrium relation or controlled limiting argument supplies that implication.

This is the source of the finite discriminant studied below.

---

## 4. Closed-time-path parent object

A compact parent object for ordered source information is the Schwinger–Keldysh/closed-time-path generating functional

`Z_T[J_+,J_-] = Tr(U[J_+] rho_T U[J_-]^dagger)`,

with

`W_T = - i hbar ln Z_T`.

Functional derivatives generate branch-ordered correlators, including Wightman, time-ordered, retarded and higher nested-response structures. RQIR therefore treats the appropriately smeared/renormalized equivalence class `[Z_T]` as a source-side information object and asks which of its projections can survive an interface and detector map.

This notation does **not** assume an operator-valued metric. The same source hierarchy can be inserted into classical, stochastic, hybrid or quantum gravitational/interface models, which is precisely why source-side distinction must be kept separate from gravitational ontology.

---

## 5. Finite calibration as a quotient of source information

Let `V` be the real tangent space of Hermitian source-state perturbations after exact hard linear preparation constraints have been eliminated. Let

`A : V -> R^m`

be a finite calibration map. Its rows can represent matched means and other declared linear expectation constraints. When means are also fixed, selected symmetrized second moments can represent equality of the corresponding centered covariance entries.

Let

`c : V -> R`

be a linear ordered-response functional.

The operational question becomes geometrical: does the calibration map remove every physical direction on which `c` changes?

If `ker A` is nontrivial, calibration alone leaves an equivalence class. If `c` vanishes on that entire nullspace, the response is fixed by the declared calibration. If instead there exists a physical `n in ker A` with `c(n) != 0`, the response remains distinct despite calibration equality.

This observation leads to the main finite-dimensional theorem.

---

## 6. RQIR-THM-001 — finite nullspace response-discriminant existence

### Theorem

Let `V` be the real tangent space of Hermitian source-state perturbations after all exact hard linear constraints in the declared preparation domain have been eliminated. Let

`A : V -> R^m`

be a finite linear calibration map with one-dimensional nullspace

`ker A = span{n}`,

and let

`c : V -> R`

be a linear response functional. Suppose:

1. `c(n) != 0`;
2. the nominal density operator `rho0` lies in the interior of the physical state set on the retained finite-dimensional Hilbert space;
3. `n` is represented by a Hermitian traceless perturbation compatible with the exact preparation constraints already imposed.

Then there exists `epsilon > 0` such that

`rho_+ = rho0 + epsilon n`,

`rho_- = rho0 - epsilon n`

are both physical states, satisfy identical declared calibration data,

`A(rho_+ - rho0) = A(rho_- - rho0) = 0`,

and have different response,

`c(rho_+ - rho_-) = 2 epsilon c(n) != 0`.

### Proof

Because `rho0` is strictly positive, choose

`0 < epsilon < lambda_min(rho0)/||n||_op`.

Weyl's eigenvalue bound then guarantees that `rho0 +/- epsilon n` remain positive. Trace and any other exact linear preparation constraints are preserved because `n` lies in the reduced tangent space. Since `A n = 0`, every declared finite calibration row agrees for the pair. Since `c(n) != 0`, their response differs by `2 epsilon c(n)`. QED.

### Interpretation

The theorem does not say that nature realizes `c` gravitationally. It establishes a conditional operational fact: **finite calibration equality need not identify the ordered-response coordinate even within the physical state set.**

The one-dimensional-nullspace form is the cleanest closed Paper-I statement. Higher-dimensional generalizations are immediate by replacing the condition with the existence of at least one physical null vector not annihilated by `c`, but the manuscript should avoid unnecessary theorem inflation unless it improves exposition.

---

## 7. Constructive realization: Toy009 and Toy010

The mature RQIR finite examples are not used as empirical models. Their role is constructive: they verify that the theorem's nontrivial ingredients can coexist in an explicit positive-state realization rather than only in abstract linear algebra.

The retained numerical structure includes:

- calibration rank `24/25`;
- a one-dimensional hidden direction;
- positive physical state pairs;
- calibration-equality residuals at approximately machine precision;
- equality of the selected mean/noise coordinates;
- nonzero, opposite ordered response along the hidden direction;
- a detector-aware response coordinate that survives the declared finite calibration map.

The finite models therefore instantiate the theorem while preserving the central interpretation boundary: the construction demonstrates source-information separability, not a measured gravity signal and not a proof of quantum geometry.

### 7.1 Why the finite construction matters

The value of the construction is not the particular Hilbert-space dimension or numerical coefficients. It closes three logical loopholes:

1. the null direction can be compatible with positivity;
2. matching the declared finite calibration rows need not force the response to match;
3. the distinction can survive a declared detector-facing projection rather than disappearing immediately under readout.

---

## 8. Calibration geometry as an active design variable

Toy010 shows that calibration is not merely a passive verification stage. Changing the finite calibration geometry rotates the hidden null direction.

For a smooth calibration map with normalized null vector `n`, a perturbative relation of the form

`n' = - A^+ A' n`

gives the first-order steering of the hidden direction, with bound

`||n'|| <= ||A'|| / s_min(A)`

in the stated finite setting.

The implication is operationally important. A source Hamiltonian can remain fixed while experimental calibration choices change which source-state direction is left unresolved and therefore which response functional can remain distinguishable. Source preparation, calibration and detector geometry must consequently be co-designed.

This motivates the later RQIR distinction between exact nulls, soft nulls and nuisance-profiled score directions developed in Paper II.

---

## 9. Operational sensitivity hierarchy

The source-information analysis suggests a hierarchy of interface sensitivity:

- `L1 mean-sensitive`: only `J=<T>` is operationally relevant;
- `L2 noise-sensitive`: `N` contributes independent information;
- `L3 order/response-sensitive`: `D` or `chi^R` contributes independently;
- `L4 higher-order-sensitive`: genuinely higher CTP cumulants or nested responses are required;
- `L5 quantum-information-sensitive`: entanglement/process observables supply additional independent constraints.

These levels classify **transmitted operational information**, not whether gravity is fundamentally classical or quantum.

A stochastic classical interface can occupy a higher information level than a mean-only semiclassical model. Conversely, a quantized gravitational description need not generate an experimentally unique direction once the complete comparator and nuisance set is included. This distinction is essential for avoiding ontological over-interpretation of an operational classification.

---

## 10. Degeneracy discipline and relation to existing approaches

### 10.1 Semiclassical gravity

Mean-source semiclassical gravity provides the natural `L1` reference. Agreement with `<T_mn>` alone cannot establish sensitivity to higher ordered information.

### 10.2 Stochastic gravity

Stochastic gravity demonstrates why “mean versus noise” is already too coarse a dichotomy. The Einstein–Langevin/influence-functional framework includes stress-energy fluctuations and associated response/dissipation structure. It is therefore a strong comparator whenever a proposed discriminator is based only on excess fluctuations.

### 10.3 Entanglement witnesses

Gravity-mediated entanglement proposals are important operational probes, but entanglement should not be identified with a quantized gravitational mediator without a complete comparator statement. The 2025 result of Aziz and Howl provides an especially direct warning: with full-QFT matter, local classical-gravity theories can generate entanglement through quantum matter propagation. The discriminating content can then reside in scaling, multi-observable structure or a more complete operational fingerprint rather than in the binary presence of entanglement.

### 10.4 Low-energy quantum-gravity EFT

Perturbative quantum GR/EFT provides controlled low-energy quantum-gravitational predictions without requiring a UV completion. In RQIR it is therefore a necessary quantum comparator, not an automatic target theory. Paper I does not attempt to distinguish a new theory from that reference; it establishes the source-information coordinates that a later model comparison must map into observable predictions.

---

## 11. Structural-identifiability bridge from later RQIR work

A later Candidate-Gravity audit exposed a useful general caution that can strengthen Paper I without reopening its scientific scope.

Exact on-shell information need not uniquely determine the off-shell/source-completed response object required by an operational interface map. Algebraically, one may have

`Gamma_B = Gamma_A + K2(p) H`

with

`K2(p)=0`

on shell, so the physical on-shell amplitudes can agree, while off shell

`D Gamma_B - D Gamma_A = K2(p) D H`

is generically nonzero.

For Paper I this should remain a short bridge rather than a new comparator section. Its role is conceptual: just as finite calibration can quotient source-state directions, a reduced on-shell description can quotient response-map information. Operational reconstruction must therefore specify the source-completed observable map actually entering the experiment.

Paper II develops the complementary statistical statement: once the physical signal map is fixed, nuisance profiling can still eliminate or suppress its identifiable component.

---

## 12. From exact separation to statistical identifiability

The Paper-I theorem is exact and finite-dimensional. It answers whether a declared calibration map leaves a response-sensitive physical direction. It does **not** answer whether a finite noisy experiment can estimate the amplitude of that direction once source, apparatus and detector uncertainties are included.

That obstruction is the endpoint of Paper I and the entry point of Paper II.

Schematically, Paper I establishes

`A n = 0`, `c(n) != 0`,

whereas Paper II asks whether the corresponding detector score survives projection against nuisance scores,

`F_beta|theta = F_bb - F_btheta F_thetatheta^{-1} F_thetab`

or equivalently in whitened geometry

`F_beta|theta = ||(I-P_J) s_tilde||^2`.

Thus exact operational distinction is necessary but not sufficient for inferability.

---

## 13. Discussion

The main conceptual contribution of Paper I is to replace a binary question—“classical or quantum gravity?”—with a hierarchy of operational information questions that can be answered before choosing a microscopic theory.

Three lessons follow.

First, source information is ordered. Means, symmetrized fluctuations and response/commutator data are distinct coordinates unless a physical relation collapses them. Any analysis that represents all second-order information by one covariance object risks erasing the very distinction one hopes to test.

Second, calibration defines a quotient. Experimental equality is always equality relative to a declared map. A finite calibration can leave physical hidden directions, and those directions can carry nonzero response. Therefore the correct comparison is not “two states have the same coarse statistics” but “two physical preparations lie in the same declared calibration equivalence class while differing in a specified operational functional.”

Third, an operationally nonclassical source coordinate is not an ontological conclusion about gravity. Classical stochastic interfaces, full-QFT matter effects, hybrid constructions and standard perturbative quantum gravity can overlap in observable space. RQIR therefore treats degeneracy analysis as part of the definition of a valid discriminator.

The practical consequence is a staged research programme. Paper I identifies source-side information directions. Paper II determines whether those directions remain statistically identifiable under nuisance profiling. Paper III converts surviving directions into physical resource and experiment-architecture requirements. Paper IV then subjects existing gravity and quantum-gravity frameworks to the common funnel. Only if that comparison leaves a robust comparator-subtracted residual does a new Candidate Gravity construction become justified in Paper V.

---

## 14. Conclusion — working draft

We formulated the first layer of Relativity–Quantum Interface Reconstruction as an operational source-information problem. The stress-energy expectation value, symmetrized noise, commutator/ordered sector and retarded response are retained as distinct projections of an ordered CTP hierarchy. We proved that a finite calibration map with a physical response-sensitive null direction admits positive source-state pairs that agree on all declared calibration rows while differing in response, and we identified constructive finite examples realizing this separation. Calibration geometry can rotate the hidden direction, making source preparation and calibration part of discriminator design rather than external bookkeeping.

The result is deliberately weaker—and therefore more reusable—than a claim of quantum gravity. It establishes an operational information distinction that any classical, semiclassical, stochastic, hybrid or quantum interface model may be asked to transmit. Whether that distinction is statistically inferable, physically measurable, or unique to a microscopic gravity theory is deferred to the subsequent RQIR stages.

---

# Figure and table plan

## Figure 1 — RQIR information flow

Conceptual diagram:

`source state -> ordered source hierarchy [J,N,D,chiR,...] -> interface I_G -> calibration/detector map -> P(o|s)`

Show explicitly that different microscopic theories may map to the same operational equivalence class.

## Figure 2 — Ordered second-order decomposition

Visual decomposition of `G^>` and `G^<` into `N` and `D`, with the causal projection from `D` to `chi^R`.

## Figure 3 — Finite calibration nullspace geometry

Geometric illustration of a calibration hyperplane with hidden physical null direction `n`, two positive states `rho_+/-`, and response functional `c` transverse to the calibrated quotient.

## Figure 4 — Calibration steering

Show how changing calibration geometry rotates `n` and changes `c(n)` while the source model is held fixed.

## Table 1 — Operational sensitivity levels

Columns: level, source information, example observable class, what it does **not** imply.

## Table 2 — Claims versus non-claims

A compact reviewer-facing boundary table preventing over-interpretation.

---

# Literature anchors verified for manuscript v0.1

These are starting anchors, not a completed novelty/priority audit.

1. B. L. Hu and E. Verdaguer, **Stochastic Gravity: Theory and Applications**, Living Reviews in Relativity / arXiv:0802.0658.  
   https://arxiv.org/abs/0802.0658

2. A. R. H. Smith and M. Ahmadi, **Quantum clocks observe classical and quantum time dilation**, Nature Communications 11, 5360 (2020).  
   https://doi.org/10.1038/s41467-020-18264-4

3. J. F. Donoghue, **Quantum General Relativity and Effective Field Theory** (2022), arXiv:2211.09902.  
   https://arxiv.org/abs/2211.09902

4. J. Aziz and R. Howl, **Classical theories of gravity produce entanglement**, Nature 646, 813–817 (2025).  
   https://doi.org/10.1038/s41586-025-09595-7

---

# Mandatory literature/priority audit before novelty wording is frozen

Search and classify at minimum:

- stochastic-gravity noise/response and influence-functional literature;
- operational reconstructions of gravity–quantum interfaces;
- gravity-mediated entanglement witness/no-go/counterexample literature;
- quantum clocks and proper-time superposition literature;
- source-state distinguishability under restricted observables/calibration;
- Schwinger–Keldysh/CTP stress-tensor response formulations;
- quantum metrology/nullspace or nuisance-quotient results that may overlap mathematically with RQIR-THM-001;
- low-energy quantum-gravity EFT operational observables;
- 2024–2026 literature that could alter any novelty or exclusivity wording.

No claim of “first”, “unique”, “model-independent proof”, or “smoking gun” is authorized before this audit.

---

# Reproducibility material to bind into the manuscript

Before submission, link every numerical statement to a canonical repository source and regenerate final figures/tables from frozen scripts. At minimum:

- `docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md`;
- `docs/FOUNDATIONS.md`;
- canonical Toy009/Toy010 source and result files;
- the calibration/null-direction steering derivation;
- independent clean rerun of the finite rank/positivity/equality/response checks;
- a machine-readable manifest for every figure and numerical table used in Paper I.

---

# Manuscript completion checklist

- [x] scientific scope frozen;
- [x] central theorem frozen;
- [x] claims/non-claims boundary frozen;
- [x] v0.1 abstract drafted;
- [x] v0.1 introduction drafted;
- [x] core mathematical narrative drafted;
- [x] Discussion/Conclusion drafted;
- [x] figure/table plan created;
- [ ] comprehensive 2024–2026 literature and priority audit;
- [ ] citation-complete bibliography;
- [ ] canonical Toy009/Toy010 figure regeneration;
- [ ] independent clean numerical reproduction;
- [ ] journal target selection and length adaptation;
- [ ] LaTeX manuscript conversion;
- [ ] reviewer-style internal audit;
- [ ] final language polish.

## Current manuscript-planning estimate

**Scientific content readiness:** 100% for the frozen Paper-I scope.  
**Manuscript/submission preparation:** approximately **35%** after this v0.1 scaffold. This is an editorial planning estimate, not a probability of acceptance.
