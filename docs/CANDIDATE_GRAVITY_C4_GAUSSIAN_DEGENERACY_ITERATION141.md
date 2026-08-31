# Candidate Gravity Iteration 141 — exact Gaussian C4/KK continuum degeneracy

**Date:** 2026-08-31  
**Model:** `ANSATZ-RQIR-KL-002` v0.1  
**Decision:** QG-007 FAIL for promotion as a novel gravity model at the frozen linear-Gaussian level; retain as reference/control

## Question

Does a positive Källén–Lehmann spin-2 continuum with linear conserved-stress coupling define an operationally new gravitational model, or is it exactly reproducible by ordinary quantum mediator continua allowed by comparator C4/KK-like alternatives?

## Direct-integral construction

The candidate two-point function is

`D = D_GR + beta int_1^infty ds rho_hat(s) D_s`,

where `D_s` is the standard positive massive spin-2 propagator with `m_s^2=M_*^2 s`.

Introduce independent positive-norm Gaussian massive spin-2 fields `H_s` and define the RQIR-facing field schematically as

`h = h_GR + sqrt(beta) direct_integral ds sqrt(rho_hat(s)) H_s`.

Because the fields are independent and Gaussian,

`<h h> = <h_GR h_GR> + beta int ds rho_hat(s) <H_s H_s>`.

This is exactly the `KL-002` two-point function.

Thus the Källén–Lehmann representation is not merely similar to a continuum of ordinary mediators; at the Gaussian two-point level it **is** such a direct-integral representation.

## CTP / RQIR consequence

For a linear conserved-stress coupling, a Gaussian environment is completely characterized by its retarded kernel and Hadamard/noise kernel.

If the direct-integral mediator construction has the same

- `D_R`;
- `D_H` / vacuum Gaussian covariance;
- tensor coupling to the same conserved source,

then its CTP influence functional is identical to that of `KL-002`.

Consequently all linear-Gaussian RQIR observables and likelihoods built from these kernels are exactly identical.

No detector optimization, Fisher profiling or physical-resource increase can distinguish two models with the same complete Gaussian influence functional.

## Numerical positive-tower certificate

For the frozen spectral shape set `s=1+t`, so

`rho_hat(s) ds = exp(-t) dt`.

Gauss–Laguerre quadrature then represents the continuum as a finite tower with strictly positive weights and masses

`m_i^2/M_*^2=1+t_i`.

The repository audit shows rapid convergence of the positive discrete tower to the exact continuum. For example at `x=q^2/M_*^2=1`:

- 4 mediators: absolute error `2.18e-4`;
- 8 mediators: `2.63e-6`;
- 16 mediators: `4.24e-9`;
- 32 mediators: `4.11e-13`.

The numerical convergence is illustrative; the exact degeneracy follows from the direct-integral identity.

## Funnel decision

**QG-007 = FAIL — `EXACT_GAUSSIAN_C4_KK_DEGENERACY`.**

`ANSATZ-RQIR-KL-002` remains a consistent and useful spectral-control model but is not promotable as the new Candidate Gravity in its frozen linear-Gaussian form.

Retained negative result **CG-NG-006**:

> A positive Källén–Lehmann spin-2 continuum with only linear conserved-stress coupling is exactly equivalent, at Gaussian RQIR level, to an ordinary positive-norm continuum/tower of quantum spin-2 mediators. Two-point response/noise optimization cannot establish gravity-specific novelty.

## Why the vDVZ and threshold relations do not save novelty

The `4/3` NR tensor factor, `3/4` traceless/NR relation and the threshold spectral shape are all reproduced by the same mediator continuum used in the direct-integral construction. They improve falsifiability of the spectral model but do not distinguish it from C4/KK-like quantum mediator physics.

## Required structure for the next ansatz

The next Candidate Gravity cannot be only a new propagator/covariance.

It must introduce at least one **derived non-Gaussian or nonlinear gravitational relation** that follows from one dynamics and cannot be freely reproduced by an ordinary mediator continuum. Candidate directions include, subject to independent prior-art audits:

1. nonlinear stress-energy self-coupling fixed by diffeomorphism/Ward bootstrap;
2. connected three- and higher-point gravitational correlators tied to the same two-point spectral kernel rather than independently parameterized;
3. a constraint-algebra or relational-observable identity linking nonlinear response to the linear spectrum;
4. universal gravitational self-coupling that survives comparison with hidden/KK/nonlocal mediator models;
5. an RQIR observable involving those higher connected/ordered structures after exact calibration quotient.

This requirement follows from the funnel; it is not an aesthetic preference.

## Reproducibility

- `analysis/candidate_gravity_gaussian_c4_equivalence_iteration141.py`
- `results/candidate_gravity_gaussian_c4_equivalence_iteration141.json`

## Article value

`KL-002` provides a second distinct negative-model lesson:

- `CTP-001` failed **consistency** at QG-004;
- `KL-002` survives scoped consistency but fails **novelty/identity** at QG-007.

This cleanly demonstrates why the RQIR funnel separates physical consistency from model-specific evidence.
