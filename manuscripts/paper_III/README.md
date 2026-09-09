# RQIR Paper III — working manuscript

**Title:** *Relativity–Quantum Interface Reconstruction III: Resource Conversion, Optimal Allocation, and Feasibility after Nuisance Profiling*

**Status:** v0.1 theorem/resource scaffold, 9 September 2026.

## Scope

Paper III begins exactly where Paper II stops: a target direction has survived the calibration quotient and nuisance profiling, but no physical resource claim has yet been made. This paper introduces the conversion from profiled local information to explicit resource allocation and minimum-budget problems.

Core result:

\[
\mathcal I_\beta(\mathbf e;\Lambda)
=
\min_{\mathbf a}
\left[
\sum_k e_k\|\mathbf s_k-J_k\mathbf a\|^2+\mathbf a^T\Lambda\mathbf a
\right].
\]

For fixed per-unit score models this map is monotone and concave in resource allocation; for data-only scaling (\(\Lambda=0\)) it is positively homogeneous. This yields convex inner allocation and minimum-budget problems.

## Five-paper RQIR architecture

1. **Paper I — calibration/source distinguishability.** Exact calibration quotient, ordered source information, and physical directions that survive finite calibration.
2. **Paper II — statistical identifiability.** Detector-facing likelihoods, nuisance geometry, covariance, Fisher/profile identifiability, and self-calibration.
3. **Paper III — resource closure.** Convert surviving profiled information into shots, wall time, spectral-density information rates, coherence/geometry/control budgets, and optimal allocation.
4. **Paper IV — known-model comparator funnel.** Pass established classical, semiclassical, stochastic, hybrid, postquantum, and quantum-gravity/interface models through the common RQIR funnel; identify which gates they pass, fail, or leave degenerate.
5. **Paper V — constructive KG model.** Build and present the KG model only after the first four layers have fixed the operational requirements, statistical gates, resource constraints, and empirical failure modes of known models.

Paper III therefore does **not** perform the known-model benchmark and does **not** introduce the KG model. Its endpoint is a resource-closed experimental/interface design language that Paper IV can use as a common comparator standard.

## Initial certificate

Run:

```bash
cd manuscripts/paper_III/data
python ../scripts/rqir_resource_certificate.py
```

The script writes `rqir_resource_certificate.json`. The initial RQIR-RES-001 suite checks:

1. positive homogeneity without fixed prior;
2. monotonicity with added resource;
3. concavity of nuisance-profiled information;
4. exact-alignment obstruction under arbitrary resource scaling;
5. analytic two-band optimal allocation;
6. minimum-budget inversion;
7. envelope/marginal-information derivative;
8. separation of fixed prior information from scalable exposure;
9. atom-interferometer wall-time binding with a free phase-offset nuisance.

Seed: `20260909`. Randomized tests: 5000 problems per stochastic property.

## Next work before submission

- deepen the initial atom-interferometer binding into a full apparatus nuisance/covariance case;
- add independent implementation audit, not only the certificate script;
- add resource-allocation and budget-reach figures;
- audit literature and claims against apparatus-specific metrology references;
- freeze a submission commit and update data-availability text;
- prepare PRR cover letter/checklist only after the physical-binding layer is credible.

The downstream handoff is now fixed: **Paper III → Paper IV known-model funnel → Paper V KG model**.
