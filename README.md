# Relativity–Quantum Interface Reconstruction (RQIR)

**Status:** research programme, v0.1 bootstrap  
**Started:** 2026-08-29  
**Repository:** model-independent reconstruction of the interface between general relativity and quantum physics.

## Objective

RQIR does **not** begin by choosing a preferred theory of quantum gravity. Its objective is to reconstruct, from consistency requirements and observables, what structure the interface between quantum matter and spacetime must possess.

The core question is operational:

> Which measurable properties distinguish a classical, semiclassical, stochastic, quantum, or emergent gravitational interface?

The programme deliberately separates three layers:

1. **Established baseline physics** — GR, QFT in curved spacetime, low-energy effective field theory (EFT), quantum information and precision metrology.
2. **Model-independent residuals and null tests** — quantities that can reveal departures from the baseline without assuming a UV completion.
3. **Candidate realizations** — semiclassical gravity, stochastic gravity, perturbatively quantized gravity/EFT, collapse/hybrid models, emergent spacetime, string/LQG/etc. These are tested against the same observable channels rather than used as starting axioms.

## Null baseline

A first reference layer is semiclassical gravity,

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}+\text{EFT counterterms}
=8\pi G\,\langle \hat T_{\mu\nu}\rangle_{\rm ren}.
\]

This is a **benchmark**, not an assumption that nature is semiclassical.

For any operational observable \(O_A\), define a residual

\[
\Delta_A \equiv O_A^{\rm obs}-O_A^{\rm baseline}.
\]

The baseline attached to each observable must be stated explicitly; it may be GR+QFT in curved spacetime, a low-energy EFT calculation, or another controlled limit. RQIR will never combine residuals with different baselines without an explicit map.

## Information hierarchy

The expectation value \(\langle T_{\mu\nu}\rangle\) is not the full quantum interface. We therefore track an observable hierarchy:

\[
\mathcal H_{RQ}=\{\text{means},\text{fluctuations},\text{correlations},\text{coherence},\text{entanglement},\text{causal structure},\text{higher cumulants}\}.
\]

At second order, stress-energy fluctuations motivate the noise kernel

\[
N_{\mu\nu\rho\sigma}(x,y)
\sim \frac12\left\langle\{\delta \hat T_{\mu\nu}(x),\delta \hat T_{\rho\sigma}(y)\}\right\rangle,
\]

which provides a natural bridge from semiclassical to stochastic descriptions.

## Initial observable channels

- **Q1 — Quantum clocks / proper time:** superpositions of trajectories, internal clocks, relativistic phases.
- **Q2 — Superposed sources:** gravitational response to spatial or internal-state superpositions of massive systems.
- **Q3 — Backreaction / source rule:** whether geometry responds to an expectation value, stochastic source, conditional state, operator-valued field, or another structure.
- **Q4 — Gravity-mediated quantum information:** entanglement, channel capacity, phase correlations, and discriminants beyond a single entanglement witness.
- **Q5 — Geometry fluctuations:** metric/curvature noise and correlations beyond matter-induced uncertainty.
- **Q6 — Causal/process structure:** whether causal order and reference frames remain classical.
- **Q7 — Low-energy quantum gravity EFT:** universal or controlled quantum corrections that do not require knowledge of the UV completion.

The channel list is provisional and may be split or extended when the operational atlas is built.

## Non-negotiable research rules

1. **No theory by popularity.** Candidate frameworks are hypotheses, not priors disguised as facts.
2. **Observable first.** Every claimed distinction must map to an operational observable or a consistency condition.
3. **Baseline discipline.** Every residual has a declared null model and approximation regime.
4. **Degeneracy tracking.** A signal is not called a quantum-gravity signature if a classical/stochastic/hybrid model can reproduce it in the same regime.
5. **Dimensional and limit checks.** Newtonian, classical, flat-spacetime, \(\hbar\to0\), \(G\to0\), weak-field and low-energy limits are explicit gates where applicable.
6. **Gauge/diffeomorphism discipline.** Coordinate-dependent quantities are not treated as observables without relational or gauge-invariant completion.
7. **No Planck-scale exceptionalism.** Low-energy interface tests are investigated before assuming direct access to Planckian physics.
8. **Negative results are results.** No-go regions, degeneracies and failed discriminants are logged permanently.
9. **Reproducibility.** Derivations, code, assumptions, datasets and iteration chronology belong in the repository.
10. **Epistemic labels.** Each result is tagged as definition, established result, derived result, numerical evidence, conjecture, open question, or excluded branch.

## First project milestone: RQIR-0 — Operational Interface Atlas

RQIR-0 will construct a matrix

| Observable | Controlled GR/QFT baseline | Semiclassical | Stochastic | Quantized low-energy gravity | Hybrid/emergent | Existing constraint | Degeneracy | Best discriminant |
|---|---|---|---|---|---|---|---|---|

The aim is to identify **minimal combinations of observables** that distinguish classes of interfaces.

A useful fingerprint notation is

\[
\mathbf F_M=(\Delta_{\rm clock},\Delta_{\rm phase},\Delta_{\rm ent},\Delta_{\rm decoh},\Delta_{\rm noise},\Delta_{\rm causal},\Delta_{\rm scatter},\ldots)_M.
\]

Two models are operationally degenerate in a domain \(D\) when their predicted fingerprints agree within experimental/theoretical resolution throughout \(D\).

## Immediate workstream

1. Formalize observable spaces and baseline maps.
2. Build the Q1–Q7 evidence/degeneracy matrix.
3. Derive a hierarchy of residuals and covariance objects.
4. Define consistency gates before fitting any candidate theory.
5. Identify the first high-value discriminants that are feasible far below the Planck scale.
6. Build reproducible symbolic/numerical notebooks only after the analytic definitions are frozen.

## Seed references

- J. F. Donoghue, *Quantum General Relativity and Effective Field Theory* (2022), arXiv:2211.09902 — https://arxiv.org/abs/2211.09902
- B. L. Hu & E. Verdaguer, *Stochastic Gravity: Theory and Applications* (2008), arXiv:0802.0658 — https://arxiv.org/abs/0802.0658
- A. R. H. Smith & M. Ahmadi, *Quantum clocks observe classical and quantum time dilation*, Nature Communications 11, 5360 (2020) — https://www.nature.com/articles/s41467-020-18264-4
- J. Aziz & R. Howl, *Classical theories of gravity produce entanglement*, Nature 646, 813–817 (2025) — https://www.nature.com/articles/s41586-025-09595-7

## Repository map

- `docs/FOUNDATIONS.md` — mathematical and epistemic foundations.
- `docs/MASTER_TABLE.md` — live observable/channel matrix.
- `docs/RECOVERY_GUIDE.md` — sufficient context to resume the project from a new chat/session.
- `research_log/` — chronological iteration record.

---

RQIR is a reconstruction programme. A successful outcome need not be a single microscopic theory: it may instead be a sharply constrained equivalence class plus experimentally decisive discriminants.