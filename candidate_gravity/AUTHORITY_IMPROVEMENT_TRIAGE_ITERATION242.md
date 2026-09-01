# Candidate Gravity — Comparator Authority-Improvement Triage, Iteration 242

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Starting point

Iteration 241 froze

`NO_EXECUTABLE_RESIDUAL_TARGET_UNDER_CURRENT_COMPARATOR_AUTHORITY`.

The next scientifically permitted task is therefore not another proxy observable. It is to improve the missing comparator authority that prevents the linked pure-gravity residual quotient from being executed.

## Frozen selection criteria

Each authority-improvement route is judged by:

1. **internal derivability** — can the missing object be derived from already defined parent dynamics/formalism rather than fitted/interpolated from absent data?;
2. **new-model-choice risk** — would completing the route require choosing a new physical projector, boundary condition, interaction or ansatz not fixed by the comparator parent?;
3. **observable identity** — does the route lead to the frozen pure-gravity `h^3/h^2` linked causal object rather than another proxy?;
4. **reproducibility** — can the derivation be encoded symbolically/numerically in the repository with explicit conventions?;
5. **external-authority dependence** — does closure require unpublished/new external data?

## Route A — C5 standard quantum-gravity authority

### Existing authority

- Barvinsky–Gusev–Zhytnikov–Vilkovisky covariant perturbation theory computes the generic one-loop effective action to third order in background curvatures and supplies nonlocal form factors/spectral representations: arXiv:0911.1168.
- Barvinsky's causal/Euclidean-Schwinger-Keldysh framework supplies a route from Euclidean nonlocal effective action to causal expectation-value equations under the stated assumptions: arXiv:1408.6112.
- Giacchini–de Paula Netto–Shapiro compute the one-loop Vilkovisky unique effective action for quantum Einstein gravity and explicitly demonstrate gauge/parametrization independence of the divergent part: arXiv:2006.04217.

### Missing piece

The published pure-Einstein Vilkovisky calculation is organized for the divergent part and uses an equations-of-motion insertion expansion sufficient for that UV objective. The frozen RQIR comparator requires the **finite nonlocal curvature-cubic sector**, so all Vilkovisky connection/gauge-orbit insertion terms capable of contributing through cubic curvature order must be retained and mapped into the generic CPT3 form factors before causal/source projection.

### Classification

- internal derivability: **HIGH but computationally heavy**;
- new-model-choice risk: **LOW** if the exact Vilkovisky definition/configuration-space metric/gauge convention is retained;
- observable identity: **HIGH** — native metric effective action can in principle generate both `K2[h,h]` and `Gamma3[h,h,h]` in one convention;
- reproducibility: **HIGH** in principle;
- external-authority dependence: **MODERATE** — formulas exist, but the finite pure-gravity specialization is not available as a ready package.

**Priority rank: 1.**

## Route B — C3 postquantum-classical gravity authority

### Existing authority

The final 2026 PRX paper `Covariant Path Integrals for Quantum Fields Backreacting on Classical Space-Time` fixes a covariant classical-quantum path-integral parent and a metric-dependent generalized Wheeler-DeWitt kernel. The May-2026 `Stochastic modes in postquantum classical gravity` paper demonstrates consistency between Onsager-Machlup, MSR and stochastic formulations after linearization around Minkowski.

### Missing piece

Iteration 229 constructs an explicit `O(h)` doubly-transverse homogeneous nonlinear conserved family that preserves the background linear authority. Conservation/Bianchi conditions therefore do not by themselves uniquely select the nonlinear ordered-response completion. No audited same-parent nonlinear projector/Green-function/boundary prescription was found that excludes this family rather than choosing one representative.

### Classification

- internal derivability: **MEDIUM/LOW** under current authority;
- new-model-choice risk: **HIGH** — choosing a projector or setting the homogeneous family to zero would define an extra comparator model;
- observable identity: **HIGH** if uniquely completed;
- reproducibility: **MEDIUM**;
- external-authority dependence: **HIGH** for a non-arbitrary completion principle.

**Priority rank: 2, but frozen pending new same-parent completion authority.**

## Route C — asymptotic-safety authority

### Existing authority

Recent Lorentzian AS work supplies:

- self-consistent graviton spectral functions (arXiv:2507.22169);
- scalar two-to-two scattering with reconstructed scalar-graviton vertex (arXiv:2603.10168);
- Lorentzian graviton spectral functions plus the effective action to quadratic order in curvature (arXiv:2606.19321).

### Missing piece

The frozen RQIR quotient requires one-convention, same-parent, real-time/retarded **three-graviton** nonlinear response with controlled hard-channel discontinuity and normalization linked to physical `K2`. Existing two-point spectra, curvature-quadratic action and scalar-graviton scattering data do not uniquely reconstruct that object without interpolation/new dynamics input.

### Classification

- internal derivability: **LOW** from currently published data;
- new-model-choice risk: **HIGH** if off-symmetric real-time three-graviton information is interpolated/guessed;
- observable identity: **HIGH** only after missing object exists;
- reproducibility: **LOW/MEDIUM** now;
- external-authority dependence: **VERY HIGH**.

**Priority rank: 3.**

## Decision

Freeze the authority-improvement order:

1. **C5 full Vilkovisky finite-CPT3 specialization**;
2. C3 only if a genuinely same-parent nonlinear conserved completion principle appears or is derivable without new choice;
3. AS waits for adequate real-time three-graviton authority unless a direct first-principles FRG derivation becomes available.

New label:

`AUTHORITY_IMPROVEMENT_PRIORITY_C5_FULL_VD_FINITE_CPT3`

This is not a Candidate Gravity ansatz and not a claim that C5 will produce a particular residual. It is the least assumption-adding route to make the frozen comparator quotient executable.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

No comparator block has yet been completed by the triage itself.

## Next exact gate — Iteration 243

Construct the **complete one-loop Vilkovisky insertion bookkeeping through finite cubic curvature order** before any heavy tensor calculation.

Required deliverables:

1. freeze the unique-action one-loop operator convention and field-space parameter choice already retained by Iterations 231–233;
2. expand the trace-log/insertion structure far enough to enumerate every term that can contribute at `O(R^3)` to the finite effective action, not merely to UV divergence;
3. include ghost sector and all connection/gauge-orbit insertion combinations required by curvature counting;
4. map each trace topology onto generic CPT orders (`V1`, `V2`, `V3` / curvature powers) and identify which published form-factor master integrals can be reused;
5. prove which terms can be dropped by curvature/EOM counting rather than by UV-only arguments;
6. only after this bookkeeping passes decide whether a heavy symbolic GitHub Action is justified.
