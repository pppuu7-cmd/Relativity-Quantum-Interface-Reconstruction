# RQIR Candidate Gravity — Iteration 255

## Same-parent field-space Christoffel first variation

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Frozen parent

Continue the C5 Vilkovisky route with the already frozen conventions: `D=4`, `Lambda=0`, DeWitt choice `a=-1/2`, standard linear covariant-metric split (`gamma1=1`, `gamma2=...=gamma6=0`) for this local field-space block, and the Iteration-252 factorization

`U1 = Nhat^-1 W [R.(D R).E] Nhat^-1`.

No observable, parent dynamics, ansatz or parameter convention is changed.

## Which connection is required

The primary Vilkovisky-gravity authority (Giacchini, de Paula Netto, Shapiro, PRD 102, 106006; arXiv:2006.04217) separates the physical-space affine connection as `Tscript = Gamma + T`, and explicitly defines the derivative occurring in `U1,U2`, `D_i R^j_alpha`, with the **Christoffel connection `Gamma` of the configuration-space metric**, not with the nonlocal gauge-orbit part `T`. This removes the connection ambiguity left at Iteration 254.

For the frozen simple split, their Eq. (43) gives

`c1=-1, c2=1/4, c3=1/4, c4=-1/8`.

Write

`P^{mn,ab}(g)=1/2 (g^{ma}g^{nb}+g^{mb}g^{na})`

and let `S_{rs}^{mn,ab}(X)` denote the algebraically symmetrized first tensor structure

`S(X)=1/4[delta^{ma}_{rs} X^{nb}+delta^{na}_{rs} X^{mb}+delta^{mb}_{rs} X^{na}+delta^{nb}_{rs} X^{ma}]`.

Then, stripping the common `kappa`,

`Gamma/kappa = -S(g^-1) + 1/4[delta^{mn}_{rs} g^{ab}+delta^{ab}_{rs} g^{mn}] + 1/4 P^{mn,ab}(g) g_rs - 1/8 g^{mn}g^{ab}g_rs`.

The algebraic symmetrizations hidden in the compact published notation are made explicit here; this is essential for implementation on the 10-dimensional space of symmetric metric components.

## First background variation

For `delta g_rs = h_rs`, define

`H^{mn}=g^{ma}g^{nb}h_ab`, so `delta g^{mn}=-H^{mn}`,

and

`delta P^{mn,ab} = -1/2[H^{ma}g^{nb}+g^{ma}H^{nb}+H^{mb}g^{na}+g^{mb}H^{na}]`.

The required same-parent vertex is therefore

`delta Gamma/kappa =`

`+ S(H)`

`- 1/4[delta^{mn}_{rs} H^{ab}+delta^{ab}_{rs} H^{mn}]`

`+ 1/4[(delta P^{mn,ab}) g_rs + P^{mn,ab} h_rs]`

`+ 1/8[H^{mn}g^{ab}g_rs + g^{mn}H^{ab}g_rs - g^{mn}g^{ab}h_rs]`.

This object is point-local in the background metric. It introduces no new momentum denominator and no new loop corner; any momentum dependence in the full `K1 E2` block comes from the already frozen diffeomorphism generators, `E^(2)`, resolvents and weight/source factors.

## Independent pointwise validation

A reproducible certificate constructs the full 10x10 configuration-space metric directly from the published DeWitt line element

`ds^2 = int sqrt(|g|) 1/2[P + a g^-1 g^-1] delta g delta g`, `a=-1/2`,

computes its Christoffel symbol by numerical differentiation, and compares it against the explicit compact-tensor formula above. It then differentiates the independently reconstructed 10x10 Christoffel along a Lorentzian TT direction

`eta=diag(-1,1,1,1)`, `h=diag(0,1,-1,0)`.

Results:

- maximum base-Christoffel mismatch: `1.81e-10`;
- maximum first-variation mismatch: `5.82e-8`;
- input-pair symmetry residual of analytic `delta Gamma`: `0.0`.

The finite-difference error is many orders below the O(1) component scale and is stable under step variation used in the certificate.

Freeze

`PASS_SCOPED_FIELDSPACE_CHRISTOFFEL_FIRST_VARIATION_AND_TT_VALIDATION`.

## Scientific scope

This closes the genuinely new geometric vertex identified by Iteration 254. It does **not** yet close the full `K1 E2` contribution, because the two `delta(Nhat^-1)` placements, `delta W`, the explicit `delta R` pieces and the `E^(2)` contraction still have to be assembled in one condensed-index convention.

It is not a full cubic Ward PASS: by Iteration 253 the only admissible cubic Ward target remains

`K0 E3 + K1 E2 + K2 E1`.

Retain

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and

`BLOCKED_NOT_ZERO`.

This is an operational/derivational BLOCKED, not a consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

## Reproducibility

- `candidate_gravity/code/iteration255_vd_fieldspace_christoffel_variation.py`
- `candidate_gravity/results/iteration255_vd_fieldspace_christoffel_variation.json`

## Readiness

MODEL_READINESS: 24%

Change from Iteration 254: **0 percentage points**. A real numerator-library element is now frozen and independently validated, but comparator foundation remains `24/25` and unique residual discovery remains `0/20`; no new readiness-rubric block has closed.

## Exact next gate

Assemble the complete `E^(2) K^(1)` contribution to `Tr U1` in the same condensed-index convention: combine the two already frozen `delta(Nhat^-1)` placements, `delta W`, both explicit `delta R` terms, and the new `delta Gamma` term. Before tensor integration, run local/index-orientation/TT checks. In parallel construct the minimal `K0 E3` and `K2 E1` siblings needed for the first legitimate cubic Ward test of `K0E3+K1E2+K2E1`. Heavy integration, Fisher/resources and `ANSATZ-003` remain forbidden.