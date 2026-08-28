# RQIR Operational Master Table

**Version:** 0.1  
**Date:** 2026-08-29

This table is intentionally conservative. `OPEN` means the comparison has not yet been demonstrated at the precision needed for RQIR; it does not mean the literature is absent.

| Channel | Operational observable | Controlled baseline | Main competing explanations/classes | Current key degeneracy | Candidate discriminant | Status |
|---|---|---|---|---|---|---|
| Q1 Quantum clocks | relative/conditional clock phase, visibility, clock-clock correlations | relativistic QM/QFT on prescribed spacetime | semiclassical backreaction, quantum geometry, quantum reference-frame effects | ordinary relativistic phase vs genuinely nonclassical spacetime contribution | multi-clock correlations and state-dependent scaling beyond prescribed-background prediction | OPEN |
| Q2 Superposed sources | probe phase/force statistics conditional on source preparation | weak-field GR + quantum matter preparation | mean-field semiclassical, stochastic source, branch-conditioned/hybrid, quantum mediator | different source rules can agree at leading Newtonian order | nonlinear response + branch correlations + noise spectrum | OPEN |
| Q3 Backreaction/source rule | response to changes in quantum state, conditioning, measurement protocol | semiclassical Einstein equation in controlled regime | stochastic gravity, local classical-QFT coupling, collapse/hybrid, quantized metric | expectation-value and more general rules can approximate each other for narrow states | deliberately nonclassical source states + correlated probe observables | OPEN |
| Q4 Gravity-mediated quantum information | entanglement witness, phase pattern, correlation scaling | chosen low-energy interaction model | perturbative QG, classical gravity + full QFT matter, hybrid models | entanglement itself is not uniquely diagnostic | mass/time/distance/order scaling; multiple observables rather than binary entanglement | HIGH PRIORITY |
| Q5 Geometry fluctuations | force/phase/clock noise; cross-correlations | detector noise + matter stress-energy fluctuation prediction | stochastic induced metric fluctuations, intrinsic quantum geometry, environmental noise | induced and intrinsic fluctuations may share spectra over limited bandwidth | cross-channel correlations with independently measured matter fluctuations | OPEN |
| Q6 Causal/process structure | process correlations, causal-order witnesses, relational timing | classical causal spacetime + quantum systems | quantum reference frames, indefinite causal structures, emergent geometry | nonclassical process signatures can originate in control systems rather than gravity | gravity-dependent scaling plus controls eliminating nongravitational mediator | OPEN |
| Q7 Low-energy QG EFT | scattering/phase/potential corrections in EFT-valid regime | classical GR + Standard Model/QFT | perturbatively quantized gravity EFT, unknown higher-curvature coefficients, classical systematics | universal nonanalytic corrections can be tiny; local terms absorb UV dependence | identify nonanalytic/long-range pieces and cross-check multiple processes | OPEN |

## Priority ranking v0.1

### P1 — Q4: Entanglement is not enough

**Established boundary:** Aziz & Howl (Nature 2025) show that when matter is treated in full QFT, a local theory with a classical gravitational field can generate quantum communication and entanglement via matter processes. Therefore RQIR must not use “entanglement observed” as a one-bit proof that gravity itself is quantized.

**RQIR task:** derive a discriminator vector rather than a binary witness:

\[
D_{Q4}=\left(
\phi(m,t,d),
E(m,t,d),
C^{(n)},
\Gamma_{\rm decoh},
\text{range/order scaling}
\right).
\]

We seek parameter domains where competing classes predict parametrically different dependence, not merely different fitted coefficients.

### P2 — Q3/Q5: Mean response versus fluctuations

Semiclassical gravity uses \(\langle T_{\mu\nu}\rangle\), while stochastic gravity explicitly introduces stress-energy fluctuations through the noise kernel. This supplies an existing controlled hierarchy in which RQIR can test how much information survives beyond the mean.

**RQIR task:** build cross-observable ratios that cancel poorly known source normalization while retaining sensitivity to fluctuation transfer.

### P3 — Q1: Proper time as an operational bridge

Quantum clocks provide observables that are intrinsically quantum but depend on relativistic proper time. They are valuable because they probe the interface without requiring Planckian energy.

**RQIR task:** isolate predictions that differ only when spacetime/source degrees of freedom themselves cannot be treated as a prescribed classical background.

### P4 — Q7: EFT anchor

Low-energy quantum GR as EFT supplies controlled statements that any proposed UV theory must reproduce in its domain of validity.

**RQIR task:** catalog which effects are universal/nonanalytic, which are Wilson-coefficient dependent, and which are experimentally inaccessible at present.

## Cross-channel matrix

| Pair | Why it matters | First proposed null test |
|---|---|---|
| Q1 ↔ Q2 | source superposition changes clock/probe phase | compare source-conditioned clock phase with classical mixture having same mean stress-energy |
| Q2 ↔ Q3 | directly tests source rule | construct states sharing the same \(\langle T\rangle\) but differing in higher moments |
| Q3 ↔ Q5 | mean-field versus fluctuation response | compare measured response variance with independently reconstructed stress-energy noise |
| Q3 ↔ Q4 | source rule constrains mediator/information flow | fit one source-rule model simultaneously to force/phase and entanglement data |
| Q4 ↔ Q5 | entanglement generation may imply characteristic noise/decoherence | search for class-specific relation between entanglement rate and force/metric noise |
| Q1 ↔ Q6 | clocks operationalize causal/reference-frame structure | conditional timing experiment with gravitationally controlled branch variable |
| Q7 ↔ all | EFT sets low-energy consistency boundary | reject phenomenological interface laws that contradict controlled EFT limits |

## First null-state construction to investigate

A particularly useful strategy is to compare two source preparations \(\rho_A\) and \(\rho_B\) engineered so that

\[
\langle \hat T_{\mu\nu}(x)\rangle_A
\approx
\langle \hat T_{\mu\nu}(x)\rangle_B,
\]

while

\[
C_A^{(2)}(x,y)\neq C_B^{(2)}(x,y)
\]

and/or higher cumulants differ.

A pure expectation-value semiclassical response predicts no leading distinction tied solely to the differing higher moments, whereas fluctuation-sensitive or genuinely quantum interface maps may. The practical existence of sufficiently controlled realizations and the exact observable consequences remain `OPEN` and must be derived rather than assumed.

## Evidence coding

For every table entry added later, record:

- citation / DOI / arXiv;
- exact theoretical assumptions;
- energy/length/time domain;
- leading scaling law;
- observable and detector model;
- uncertainty or bound;
- known alternative explanations;
- RQIR consistency gates passed/failed.

## Seed references

1. J. F. Donoghue, *Quantum General Relativity and Effective Field Theory*, arXiv:2211.09902.
2. B. L. Hu & E. Verdaguer, *Stochastic Gravity: Theory and Applications*, Living Rev. Relativity / arXiv:0802.0658.
3. A. R. H. Smith & M. Ahmadi, *Quantum clocks observe classical and quantum time dilation*, Nature Communications 11, 5360 (2020).
4. J. Aziz & R. Howl, *Classical theories of gravity produce entanglement*, Nature 646, 813–817 (2025), DOI: 10.1038/s41586-025-09595-7.

## Next iteration

The next iteration should convert Q2/Q3/Q4 into explicit toy models with a common source state and common measured probe, so differences are attributable to the interface law rather than inconsistent experimental definitions.