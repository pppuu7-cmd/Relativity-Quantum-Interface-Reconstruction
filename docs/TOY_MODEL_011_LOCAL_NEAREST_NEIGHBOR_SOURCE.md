# RQIR Toy Model 011 — Local Nearest-Neighbor Source Embedding

**Date:** 2026-08-29  
**Iteration:** 052  
**Status:** finite-dimensional locality-constrained source construction; not a hardware implementation and not a new-physics claim.

## 1. Why this gate is necessary

Toy009 was optimized in an abstract five-level source space and then given a Newtonian radius operator. That was sufficient for the operational/nullspace programme, but it did not prove that the accepted source can be realized by a spatially local Hamiltonian.

A source intended to represent a physical multiwell/multimode massive system should not silently require arbitrary long-range tunnelling between distant radius sites.

Toy011 therefore imposes spatial locality directly on the source Hamiltonian.

## 2. Locality audit of Toy009

Use the Toy009 radii

`(1.00000, 1.60090, 1.77911, 2.60901, 5.90724)`

as eigenvalues of a radius/site operator `R`.

Transform the fixed energy Hamiltonian

`H=diag(1,2,3,4,6)`

into the sorted radius basis of Toy009.

The resulting site-basis Hamiltonian is dense. Quantitatively,

`boxed: 64.46%`

of its off-diagonal Frobenius power lies outside nearest-neighbor couplings.

Simply zeroing the non-nearest-neighbor matrix elements changes the Hamiltonian by

`||Delta H||_F / ||H||_F ~= 0.36893`

and shifts the spectrum from

`(1,2,3,4,6)`

to approximately

`(1.335, 2.817, 3.430, 3.984, 4.434)`.

### RQIR-NG-025 — post-hoc source-locality obstruction

> A detector-aware finite-dimensional source that is valid algebraically need not correspond to a local spatial Hamiltonian when its probe/radius operator is interpreted physically. Locality must be imposed during source optimization rather than obtained by truncating long-range couplings afterward.

This does not invalidate Toy009 as an operational counterexample. It limits its interpretation as a literal local massive-source design.

## 3. Exact-spectrum local chain construction

Toy011 keeps the same five radii and exact spectrum `E=(1,2,3,4,6)` but replaces the dense radius-basis Hamiltonian by a Jacobi chain.

Start from a positive cyclic spectral-weight vector `q0` and Lanczos-tridiagonalize `diag(E)`.

This produces an orthogonal basis `Q(q0)` such that

`H_site = Q^T diag(E) Q`

is exactly nearest-neighbor/tridiagonal while retaining the exact eigenvalues `E`.

The physical site/radius operator is diagonal by construction:

`R_site=diag(r_1,...,r_5)`.

The Newtonian calibration probe is then

`B(y)=Q diag(1/|r_i-y|) Q^T`

in the energy basis.

Thus every scanned source satisfies simultaneously:

- exact five-level spectrum;
- diagonal spatial/radius operator;
- exact nearest-neighbor Hamiltonian in the radius basis;
- the same finite NP3 calibration observable family.

## 4. Joint local-source/calibration scan

A deterministic `12000`-trial scan with seed

`20260902`

varies jointly:

- the positive Lanczos spectral-weight vector `q0`;
- second probe position `y1`;
- six nonzero calibration phases.

The source and calibration geometry are therefore co-designed **inside the local-source manifold**, in the spirit of RQIR-DESIGN-001.

Two Pareto-relevant points are retained rather than declaring a single global optimum.

## 5. Local response-oriented point

Trial `6304`:

`q0 ~= (0.331914, 0.631771, 0.260908, 0.317702, 0.567178)`.

Calibration geometry:

`y1 ~= -5.8641521`,

phases

`(0, 3.27041685, 3.75296867, 0.63489295, 2.05420608, 5.27344622, 4.02285984)`.

Exact calibration properties:

- rank `24/25`;
- `s_min ~= 9.92249e-4`;
- condition number `~4701.83`;
- positive hidden-pair states;
- selected equality residual `<2e-16`.

At the target phase the selected mean and centered noise agree exactly while the ordered response changes sign:

`<B>_+ = <B>_- ~= 0.54785973`,

`N_+ = N_- ~= -0.00156204`,

`D_+ ~= +0.00404741`,

`D_- ~= -0.00404741`.

The local-chain two-band harmonics are nonzero:

D1/potential-like:

`H2 ~= -0.00551652 - 0.00091806 i`,

`H4 ~= +0.00226998 - 0.00269397 i`.

D2/gradient-like:

`G2 ~= -0.00788744 - 0.00161094 i`,

`G4 ~= +0.00378474 - 0.00449166 i`.

Relative to the current practical Toy009/Iteration-011 two-band source proxy, this point retains approximately

- `12.2%` of D1 `S_eff`;
- `15.6%` of D2 `S_eff`.

Thus locality is obtained without destroying the discriminator, but with a substantial detector-information penalty.

## 6. Local conditioning-oriented point

The composite conditioning/information score selects trial `3811`:

`q0 ~= (0.151268, 0.598236, 0.201050, 0.409645, 0.641095)`.

Calibration geometry:

`y1 ~= -2.77703786`,

phases

`(0, 3.58229696, 2.69261425, 3.36881763, 1.53334798, 4.76982170, 1.05761912)`.

It gives

- `s_min ~= 1.84219e-3`;
- condition number `~2540.42`.

This is close to the practical Toy009 conditioning (`s_min~1.99954e-3`, condition `~2313`) while remaining exactly nearest-neighbor in the radius basis.

The price is a weaker two-band response:

- D1 `S_eff ~5.42%` of current Toy009;
- D2 `S_eff ~8.16%` of current Toy009.

Again, exact mean/noise equality, positive states and opposite ordered response survive.

## 7. Scientific result

Toy011 establishes a new positive existence statement:

`boxed: finite NP3 mean/noise equality + nonzero ordered-response split is compatible with an exactly local nearest-neighbor five-site source Hamiltonian.`

Therefore the ordered-response discriminator found by RQIR is **not intrinsically dependent on the dense/nonlocal Toy009 Hamiltonian**.

However, the present local-source scan also finds a clear cost: the best sampled locality-constrained sources retain only a fraction of Toy009's detector information at comparable calibration conditioning.

### RQIR-DESIGN-002 — locality belongs inside the source/inference co-design

> Source locality is an active design constraint that competes with detector information and calibration conditioning. A physically meaningful optimization must therefore include `(locality, calibration geometry, detector Fisher)` simultaneously rather than localizing an already optimized abstract source afterward.

## 8. What is and is not closed

Closed at finite-dimensional toy level:

- exact nearest-neighbor spatial source exists;
- exact spectrum retained;
- exact finite NP3 null retained;
- hidden states positive;
- ordered-response discriminator nonzero;
- practical conditioning can remain within order unity of Toy009.

Still open:

- recover more of the lost D1/D2 detector information inside the local manifold;
- include centered finite-noise/profile Fisher rather than only exact null and two-band source proxy;
- attach physical masses, trap/multiwell couplings and preparation times;
- embed apparatus stress-energy and conservation;
- extend beyond one-particle five-site mechanics.

## 9. Reproducibility

Code:

`analysis/toy011_local_nearest_neighbor_source.py`

The script reconstructs the Toy009 locality audit, builds exact-spectrum Jacobi chains, performs the deterministic joint source/calibration scan and verifies both retained Pareto points.

## 10. Next gate

The next useful calculation is to pass Toy011 through the same hard-constrained statistical-identifiability machinery used after Toy010:

1. build centered calibration rows for the local response-oriented and conditioning-oriented points;
2. recompute D1/D2 `F_beta|theta` and the hidden-amplitude/source-metrology requirement;
3. determine whether the apparent ~6–16% two-band information retention translates into a tolerable wall-clock penalty or whether a broader local-source search is required.

Only after that should Toy011 be promoted as the new physical-source baseline.
