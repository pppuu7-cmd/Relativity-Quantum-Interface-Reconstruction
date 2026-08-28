# RQIR Operational Master Table

**Version:** 0.3  
**Date:** 2026-08-29

This table is intentionally conservative. `OPEN` means the comparison has not yet been demonstrated at the precision needed for RQIR.

| Channel | Operational observable | Controlled baseline | Main competing explanations/classes | Current key degeneracy | Candidate discriminant | Status |
|---|---|---|---|---|---|---|
| Q1 Quantum clocks | relative/conditional clock phase, visibility, clock-clock correlations | relativistic QM/QFT on prescribed spacetime | semiclassical backreaction, quantum geometry, quantum reference-frame effects | ordinary relativistic phase vs genuinely nonclassical spacetime contribution | multi-clock correlations and state-dependent scaling beyond prescribed-background prediction | OPEN |
| Q2 Superposed sources | probe phase/force/potential statistics conditional on source preparation | weak-field GR + quantum matter preparation | mean-field semiclassical, stochastic source, branch-conditioned/hybrid, quantum mediator | static density-diagonal coupling is phase-blind; a single weighted potential can hide local density differences | independent multiprobe/multipole tomography + unequal-time response | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, noise, retarded response under changes in source state/drive | semiclassical Einstein equation / Einstein–Langevin | stochastic gravity, local classical-QFT coupling, collapse/hybrid, quantized metric | even equal mean potential and equal symmetrized potential noise do not determine retarded response in Toy 005 | reconstruct `<T>`, `N`, `chi^R` across enough independent source kernels to close density degeneracies | HIGH PRIORITY |
| Q4 Gravity-mediated quantum information | entanglement, visibility, non-Gaussianity, phase/correlation scaling | common low-energy interaction model | perturbative QG, classical gravity + full QFT matter, hybrid models | entanglement alone is not unique to quantized gravity | perturbative order + mass/time/distance scaling + force/noise/response cross-check | HIGH PRIORITY |
| Q5 Geometry fluctuations | force/phase/clock noise and response spectra | detector noise + matter stress-energy fluctuation prediction | stochastic induced metric fluctuations, intrinsic quantum geometry, environmental noise | noise alone is not diagnostic; matter-induced response also exists | joint source `N`–`chi^R` calibration and gravity-channel transfer ratios | HIGH PRIORITY |
| Q6 Causal/process structure | process correlations, causal-order witnesses, relational timing | classical causal spacetime + quantum systems | quantum reference frames, indefinite causal structures, emergent geometry | nonclassical process signatures can originate in controls rather than gravity | gravity-dependent scaling plus nongravitational-control closure | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections in EFT-valid regime | classical GR + Standard Model/QFT | perturbatively quantized gravity EFT, higher-curvature Wilson coefficients, classical systematics | universal nonanalytic pieces are tiny; local terms absorb UV dependence | cross-process nonanalytic/long-range fingerprint | OPEN |

## Current source-side mathematical object

RQIR preserves operator ordering. At second order,

\[
\boxed{
\mathcal K_T^{(2)}
=\left(
\langle T\rangle,
N,
D\;\text{or}\;\chi^R
\right),
}
\]

with

\[
N_{AB}(x,y)=\frac12\langle\{\delta T_A(x),\delta T_B(y)\}\rangle,
\]

\[
D_{AB}(x,y)=\frac{1}{2i}\langle[\delta T_A(x),\delta T_B(y)]\rangle,
\]

\[
\chi^R_{AB}(x,y)=\frac{i}{\hbar}\theta(x^0-y^0)
\langle[T_A(x),T_B(y)]\rangle.
\]

The parent source object is the Schwinger–Keldysh/CTP generating functional `Z_T[J_+,J_-]`.

---

## Null-pair strength grading v0.3

To avoid calling a weak calibration a “full null pair”, RQIR now grades constructions:

- **NP0:** equal global scalar only;
- **NP1:** equal chosen gravitational readout mean;
- **NP2:** equal chosen readout mean + symmetrized noise;
- **NP3:** equal finite independent multiprobe/multipole mean/noise set;
- **NP4:** equal complete relevant smeared stress-energy mean/noise in a declared spacetime domain;
- **NP5:** NP4 plus complete source/apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Toy 005 reaches **NP2**.

---

## Priority ranking v0.3

### P1 — Q2/Q3: raise Toy 005 from NP2 toward NP4

Toy 005 supplies the first exact Newtonian mass-density-channel embedding of the ordered-response split.

For one fixed probe point,

\[
\boxed{
\langle\Phi_p(t)\rangle_+
=\langle\Phi_p(t)\rangle_-\quad\forall t,
}
\]

\[
\boxed{
N_{\Phi,+}(t,0)=N_{\Phi,-}(t,0)\quad\forall t,
}
\]

but

\[
\boxed{D_{\Phi,+}(t,0)\neq D_{\Phi,-}(t,0).}
\]

The source is a one-particle five-mode mass distribution with a real coupled-mode Hamiltonian.

However the local occupations differ, so another independent probe can generally distinguish the preparations at mean-field level.

**Next task:** impose equality of several independent Newtonian kernels and ultimately the relevant local/smeared density history and cross-noise matrix.

### P2 — Q3/Q5: derive the common transfer law

Need an explicit probe equation of the schematic form

\[
(\langle T\rangle,N_T,\chi_T^R)
\longrightarrow
(\langle O_p\rangle,N_p,\chi_p^R),
\]

for one controlled weak-field detector, so source-side ordered structure is not confused with detector susceptibility.

### P3 — Q4: multi-observable discrimination

Aziz & Howl (Nature 2025) invalidate a one-bit “entanglement means quantum gravity” inference in sufficiently general full-QFT matter treatments.

A current 2026 operational QFT calculation of gravitationally induced entanglement also reinforces the value of field-theoretic source/probe observables rather than purely first-quantized labels.

RQIR should compare full fingerprints:

\[
D_{Q4}=(\phi,E,N,\chi^R,\text{non-Gaussianity},C^{(n)},\Gamma_{\rm decoh},\text{scaling/order}).
\]

### P4 — Q7: EFT anchor

Any phenomenological interface law must reproduce controlled low-energy quantum-GR EFT where applicable.

---

## Current closed/positive results

### RQIR-NG-001 — static density phase blindness (`NEG/DRV`)

For nonoverlapping orthogonal mass configurations and density-diagonal static coupling/readout, relative branch phase is invisible when diagonal mass statistics match.

See `TOY_MODEL_002_PHASE_BLINDNESS_NO_GO.md`.

### RQIR-NG-002 — minimal qubit energy obstruction (`NEG/DRV`)

A qubit can have equal density mean/noise and opposite response, but the same component changes mean generator energy, preventing a clean gravity null interpretation.

See `TOY_MODEL_003_SAME_NOISE_DIFFERENT_RESPONSE.md`.

### Toy 004 — balanced algebraic witness (`NUM/DRV`)

Equal mean energy + equal full chosen-source mean history + equal reference-time symmetrized kernel do not fix the commutator sector in a five-level model.

See `TOY_MODEL_004_BALANCED_FIVE_LEVEL_ORDERED_KERNEL.md`.

### PE-1 / Toy 005 — exact single-channel Newtonian embedding (`DRV/NUM`)

Any positive finite-dimensional `B` can be represented as a one-particle Newtonian potential observable at one fixed probe:

\[
B=\sum_a b_a n_a,
\qquad
r_a=L/b_a,
\qquad
\Phi_p=-\frac{Gm}{L}B.
\]

A real five-level witness then gives

\[
(\langle H\rangle,\langle\Phi_p\rangle,N_{\Phi_p})
\not\Rightarrow D_{\Phi_p}.
\]

See `TOY_MODEL_005_NEWTONIAN_DENSITY_EMBEDDING.md` and `analysis/search_real_newtonian_embedding.py`.

---

## Cross-channel matrix v0.3

| Pair | Why it matters | Current strategy |
|---|---|---|
| Q1 ↔ Q2 | source preparation changes clock/probe phase | require matched classical source tomography before assigning coherence-specific clock residual |
| Q2 ↔ Q3 | directly tests source rule | NP2 Toy 005 -> NP3/NP4 multiprobe density matching |
| Q3 ↔ Q5 | separates source noise from source response and gravity transfer | calibrate `N_T` and `chi_T^R`, then infer transfer into probe noise/lag |
| Q3 ↔ Q4 | source rule constrains information flow | force one interface model to fit potential/force, response and entanglement/non-Gaussianity |
| Q4 ↔ Q5 | information-generation mechanisms imply accompanying fluctuation/response structure | search class-specific ratios/scalings |
| Q1 ↔ Q6 | clocks operationalize causal/reference-frame structure | relational timing with gravity-dependent controls |
| Q7 ↔ all | EFT provides low-energy consistency boundary | reject interface laws violating controlled EFT predictions |

---

## Evidence coding

For every future entry record citation/DOI/arXiv, assumptions, regime, leading scaling, detector observable, uncertainty/bound, alternative explanations and RQIR gates.

## Seed references

1. J. F. Donoghue, *Quantum General Relativity and Effective Field Theory*, arXiv:2211.09902.
2. B. L. Hu & E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Rev. Relativity 11, 3 (2008), arXiv:0802.0658.
3. N. G. Phillips & B. L. Hu, *Noise Kernel in Stochastic Gravity and Stress Energy Bi-Tensor of Quantum Fields in Curved Spacetimes*, Phys. Rev. D 63, 104001 (2001), arXiv:gr-qc/0010019.
4. R. Howl et al., *Non-Gaussianity as a Signature of a Quantum Theory of Gravity*, PRX Quantum 2, 010325 (2021).
5. A. R. H. Smith & M. Ahmadi, *Quantum clocks observe classical and quantum time dilation*, Nature Communications 11, 5360 (2020).
6. J. Aziz & R. Howl, *Classical theories of gravity produce entanglement*, Nature 646, 813–817 (2025), DOI: 10.1038/s41586-025-09595-7.
7. J. Yant & M. Blencowe, *Operational quantum field theoretic model for gravitationally induced entanglement*, Phys. Rev. D 114, 026006 (2026).

## Exact next iteration

1. `Toy Model 006`: impose independent multiprobe/local-density matching and matched symmetrized cross-noise.
2. Determine whether a response split survives; if not, formulate/prove the resulting no-go under explicit assumptions.
3. Derive the first source-to-probe linear-response transfer equation for `J,N,chi^R`.
4. Begin a quantitative Q4 scaling/order comparison of classical-gravity+QFT versus perturbative QG.
