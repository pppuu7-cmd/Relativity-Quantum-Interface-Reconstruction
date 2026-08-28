# RQIR Operational Master Table

**Version:** 0.4  
**Date:** 2026-08-29

This table is intentionally conservative. `OPEN` means the comparison has not yet been demonstrated at the precision needed for RQIR.

| Channel | Operational observable | Controlled baseline | Main competing explanations/classes | Current key degeneracy/no-go | Candidate discriminant | Status |
|---|---|---|---|---|---|---|
| Q1 Quantum clocks | relative/conditional clock phase, visibility, clock-clock correlations | relativistic QM/QFT on prescribed spacetime | semiclassical backreaction, quantum geometry, quantum reference-frame effects | ordinary relativistic phase vs genuinely nonclassical spacetime contribution | multi-clock correlations with source tomography and state-dependent scaling | OPEN |
| Q2 Superposed sources | probe phase/force/potential statistics conditional on source preparation | weak-field GR + quantum matter preparation | mean-field semiclassical, stochastic source, branch-conditioned/hybrid, quantum mediator | static density-diagonal coupling is phase-blind; one potential can hide local density differences; complete density history can become full state tomography | finite multiprobe calibration with explicit observation rank/nullspace | HIGH PRIORITY |
| Q3 Backreaction/source rule | mean, noise, retarded response under source state/drive changes | semiclassical Einstein equation / Einstein–Langevin | stochastic gravity, local classical-QFT coupling, collapse/hybrid, quantized metric | equal chosen mean+noise do not determine response, but over-complete source calibration removes all distinct-state freedom | optimize calibrated constraint span while retaining response projection | HIGHEST PRIORITY |
| Q4 Gravity-mediated quantum information | entanglement, visibility, non-Gaussianity, phase/correlation scaling | common low-energy interaction model | perturbative QG, classical gravity + full QFT matter, hybrid models | entanglement alone is not unique to quantized gravity | perturbative order + mass/time/distance scaling + force/noise/response cross-check | HIGH PRIORITY |
| Q5 Geometry fluctuations | force/phase/clock noise and response spectra | detector noise + matter stress-energy fluctuation prediction | stochastic induced metric fluctuations, intrinsic quantum geometry, environmental noise | noise alone is not diagnostic; matter-induced response exists | jointly calibrate source `N` and `chi^R`, then infer gravity transfer ratios | HIGH PRIORITY |
| Q6 Causal/process structure | process correlations, causal-order witnesses, relational timing | classical causal spacetime + quantum systems | quantum reference frames, indefinite causal structures, emergent geometry | nonclassical process signatures can originate in controls rather than gravity | gravity-dependent scaling plus nongravitational-control closure | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections in EFT-valid regime | classical GR + Standard Model/QFT | perturbatively quantized gravity EFT, higher-curvature Wilson coefficients, classical systematics | universal nonanalytic pieces tiny; local terms absorb UV dependence | cross-process nonanalytic/long-range fingerprint | OPEN |

## Current source-side mathematical object

At second order RQIR preserves operator ordering:

\[
\boxed{\mathcal K_T^{(2)}=(\langle T\rangle,N,D\text{ or }\chi^R).}
\]

\[
N_{AB}=\frac12\langle\{\delta T_A,\delta T_B\}\rangle,
\qquad
D_{AB}=\frac1{2i}\langle[\delta T_A,\delta T_B]\rangle,
\]

\[
\chi^R_{AB}=\frac{i}{\hbar}\theta(x^0-y^0)\langle[T_A,T_B]\rangle.
\]

Parent source object: Schwinger–Keldysh/CTP generating functional `Z_T[J_+,J_-]`.

---

## Null-pair grades

- **NP0:** equal global scalar only;
- **NP1:** equal chosen gravitational readout mean;
- **NP2:** equal chosen readout mean + symmetrized noise;
- **NP3:** equal finite independent multiprobe/multipole mean/noise set;
- **NP4:** equal complete relevant smeared stress-energy mean/noise over declared domain;
- **NP5:** NP4 plus full source/apparatus stress-energy, conservation, gauge/relational and relativistic controls.

Toy 005 reaches NP2.

---

## New central quantity — observability rank

For the finite set of source calibration operators/settings

\[
\mathcal M=\{M_\alpha\},
\]

define

\[
\mathcal S_M=\operatorname{span}_{\mathbb R}\{M_\alpha\},
\qquad
\boxed{r_{obs}=\dim\mathcal S_M.}
\]

The mean-level invisible state-direction space is

\[
\mathcal N_{obs}=\mathcal S_M^\perp,
\qquad
\boxed{\dim\mathcal N_{obs}=d^2-r_{obs}.}
\]

After adding symmetrized-noise equality operators, a response witness exists only if a candidate commutator/retarded operator has nonzero projection into the remaining nullspace.

This converts RQIR null-test design into an inverse-tomography / experimental-design problem.

---

## Result chain

### RQIR-NG-001 — static density phase blindness (`NEG/DRV`)

For nonoverlapping orthogonal mass configurations and density-diagonal static coupling/readout, relative source phase is invisible when diagonal mass statistics match.

### RQIR-NG-002 — minimal qubit energy obstruction (`NEG/DRV`)

Equal density mean/noise with different response is possible in a qubit, but the same state direction changes mean generator energy.

### Toy 004 — balanced algebraic ordered-kernel witness (`NUM/DRV`)

A five-level source satisfies equal mean energy + equal chosen-source mean history + equal symmetrized kernel but different commutator response.

### PE-1 / Toy 005 — exact Newtonian single-channel embedding (`DRV/NUM`)

Any positive finite-dimensional `B` can be represented as a one-particle Newtonian potential observable at one fixed probe:

\[
B=\sum_a b_a n_a,
\qquad
r_a=L/b_a,
\qquad
\Phi_p=-\frac{Gm}{L}B.
\]

A real five-level source gives

\[
(\langle H\rangle,\langle\Phi_p\rangle,N_{\Phi_p})\not\Rightarrow D_{\Phi_p}.
\]

This is NP2, not a full stress-energy null pair.

### RQIR-NG-003 / Toy 006 — complete density-history tomography obstruction (`DRV/NEG`)

For a finite one-particle source, if:

1. positive Bohr gaps are nondegenerate;
2. every energy pair is visible in at least one local mode;
3. `W_ai=|V_ia|^2` has full rank,

then

\[
\operatorname{span}_{\mathbb R}\{P_a(t):a,t\}=\operatorname{Herm}(d),
\]

hence

\[
\langle n_a(t)\rangle_+=\langle n_a(t)\rangle_-\;\forall a,t
\Rightarrow\rho_+=\rho_-.
\]

Thus an exact distinct-state full-density-history null pair with different response is impossible in this generic regime.

Interpretation: complete infinite-resolution calibration is not the right experimental target because it may already perform full quantum-state tomography.

---

## Priority ranking v0.4

### P1 — Toy 007: finite multiprobe optimal nullspace design

Choose a realistic finite set of Newtonian probe locations/times and construct all calibrated mean and symmetrized auto/cross-noise equality operators.

Compute their rank/nullspace and maximize the surviving response projection while minimizing ordinary source ambiguity.

Target mathematical structure:

\[
A\,\delta\rho=0,
\]

with response operator vector `c`. If `P_N` projects onto the nullspace of `A`, define the normalized surviving response fraction

\[
\boxed{
\eta_R=\frac{\|P_N c\|}{\|c\|}.
}
\]

A useful design needs `eta_R>0` while `dim ker(A)` is small enough that nuisance alternatives are controlled.

For multiple candidate response operators collected into a matrix `C`, use singular values of the nullspace-projected response family to identify the strongest surviving direction.

### P2 — source-to-detector transfer law

Derive explicitly

\[
(\langle T\rangle,N_T,\chi_T^R)
\longrightarrow
(\langle O_p\rangle,N_p,\chi_p^R),
\]

including detector susceptibility and environmental covariance.

### P3 — Q4 multi-observable scaling comparison

Compare perturbative-QG and classical-gravity+full-QFT mechanisms using the same operational observables and perturbative-order bookkeeping.

### P4 — Q7 EFT anchor

Reject phenomenological interface laws that contradict controlled low-energy quantum-GR EFT.

---

## Cross-channel matrix v0.4

| Pair | Why it matters | Current strategy |
|---|---|---|
| Q1 ↔ Q2 | source preparation changes clock phase | source-calibration rank must be explicit before attributing residual to coherence/gravity |
| Q2 ↔ Q3 | directly tests source rule | Toy 005 NP2 + Toy 006 tomography no-go -> finite-rank Toy 007 |
| Q3 ↔ Q5 | mean/noise/response transfer | infer detector response only after source `N` and `chi^R` calibration |
| Q3 ↔ Q4 | source rule constrains information flow | one interface model must fit potential/force, response and quantum-information observables |
| Q4 ↔ Q5 | information mechanisms predict accompanying fluctuation/response structure | search class-specific ratios and perturbative scaling |
| Q1 ↔ Q6 | clocks operationalize causal/reference-frame structure | relational timing with gravity-dependent controls |
| Q7 ↔ all | EFT provides low-energy boundary | reject inconsistent interface maps |

---

## Seed references

1. J. F. Donoghue, *Quantum General Relativity and Effective Field Theory*, arXiv:2211.09902.
2. B. L. Hu & E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Rev. Relativity 11, 3 (2008), arXiv:0802.0658.
3. N. G. Phillips & B. L. Hu, *Noise Kernel in Stochastic Gravity and Stress Energy Bi-Tensor of Quantum Fields in Curved Spacetimes*, Phys. Rev. D 63, 104001 (2001).
4. R. Howl et al., *Non-Gaussianity as a Signature of a Quantum Theory of Gravity*, PRX Quantum 2, 010325 (2021).
5. A. Czerwinski, *Quantum state tomography with informationally complete POVMs generated in the time domain*, arXiv:2010.13777.
6. A. R. H. Smith & M. Ahmadi, *Quantum clocks observe classical and quantum time dilation*, Nature Communications 11, 5360 (2020).
7. J. Aziz & R. Howl, *Classical theories of gravity produce entanglement*, Nature 646, 813–817 (2025).
8. J. Yant & M. Blencowe, *Operational quantum field theoretic model for gravitationally induced entanglement*, Phys. Rev. D 114, 026006 (2026).

## Exact next iteration

1. Implement `Toy 007` finite multiprobe geometry/rank optimizer.
2. Include mean plus symmetrized auto/cross-noise constraints.
3. Compute `eta_R`, nullspace dimension and conditioning versus probe geometry/timing.
4. Add a concrete detector susceptibility and derive signal scaling.
5. Only then estimate experimental feasibility.
