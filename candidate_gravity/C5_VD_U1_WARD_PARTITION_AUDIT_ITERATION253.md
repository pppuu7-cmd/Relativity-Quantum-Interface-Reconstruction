# RQIR Candidate Gravity — Iteration 253

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Purpose

Iteration 252 left one missing first-order kernel block in `E^(2)K^(1)`, namely `delta[R.(D R)] E^(2)`, and proposed a condensed-index/Ward test immediately after assembling that block. Before doing a long component differentiation, this iteration audits what the exact gauge Ward identity actually constrains at cubic background order.

## Exact identity

Gauge invariance of the classical parent action gives

`E_j R^j_delta = 0`.

Using the same torsion-free field-space covariant derivative `D_i` as in the Vilkovisky construction,

`D_i(E_j R^j_delta) = (D_i E_j) R^j_delta + E_j (D_i R^j_delta) = 0`.

Multiplying by `R^i_gamma` yields the exact same-parent identity

`A_{gamma delta}[E] := R^i_gamma (D_i R^j_delta) E_j`

`= - R^i_gamma R^j_delta (D_i E_j)`.

Because `D_i E_j = D_i D_j S` is the covariant Hessian of a scalar action, it is symmetric in `i,j`; therefore the **complete** `A_{gamma delta}[E]` is symmetric in the gauge indices `gamma,delta`.

Primary authority for the ingredients is Giacchini–de Paula Netto–Shapiro, *Vilkovisky unique effective action in quantum gravity*, Phys. Rev. D 102, 106006 (2020): gauge invariance `E_i R^i_alpha=0`, the torsion-free field-space connection, and the nonlocal kernel `R (D R) E` entering the Vilkovisky connection.

## Critical cubic-order partition result

Let the background amplitude be `t` and write

`K(t) := R.(D R) = K0 + t K1 + t^2 K2 + ...`,

`E(t) = t E1 + t^2 E2 + t^3 E3 + ...`.

Then the coefficient at total cubic order is exactly

`[K E]_{t^3} = K0 E3 + K1 E2 + K2 E1`.

The reproducible symbolic certificate in

`candidate_gravity/code/iteration253_vd_u1_ward_partition_audit.py`

returns `partition_match = true`.

This changes the interpretation of the planned Ward gate. The exact Ward/symmetry identity constrains the **sum**

`K0 E3 + K1 E2 + K2 E1`,

not automatically the middle partition `K1 E2` by itself. Therefore a failure of `K1 E2` alone to be symmetric in condensed ghost indices would not be a scientific FAIL; it could be cancelled by the same-parent `K0 E3` and `K2 E1` pieces required at the same total order.

## Scientific classification

Freeze

`PASS_SCOPED_CUBIC_WARD_PARTITION_AUDIT`.

Also freeze the guardrail

`NO_STANDALONE_CUBIC_WARD_FAIL_FROM_E2K1_PARTITION`.

This is not a comparator identity, not a Candidate Gravity residual, not a consistency FAIL, not near-degeneracy, and not regime-specific non-identifiability. It is an upstream algebraic correction preventing a false rejection of the C5 construction.

The umbrella status remains

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`,

`BLOCKED_NOT_ZERO`.

## Consequence for the next calculation

The `delta[R.(D R)] E^(2)` block is still required and should still be derived in the frozen `D=4`, `Lambda=0`, `a=-1/2` convention. However, after assembling the four `E^(2)K^(1)` terms (two `delta Nhat^-1` placements, `delta Y^up`, and `delta[R.(D R)]`), only **internal algebraic/index-orientation checks** are legitimate at that stage.

A final cubic Ward/symmetry PASS/FAIL must wait until the same-parent `E^(3)K^(0)` and `E^(1)K^(2)` partitions are also assembled.

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 252: **0 percentage points**. A potentially invalid gate was corrected and the exact Ward target was sharpened, but no comparator coordinate or robust residual was closed.

## Exact next gate — Iteration 254

Derive the explicit `delta[R^i_gamma (D_i R^j_delta)] E^(2)_j` contribution in the same convention and combine it with the two frozen ghost-resolvent placements plus `delta Y^up`. Require local/index-orientation and TT checks only. In parallel, prepare the minimum `K0 E3` and `K2 E1` bookkeeping needed so the eventual cubic Ward certificate is applied to the complete same-parent sum. No heavy integral, Fisher/resources, or `ANSATZ-003` before this upstream block closes.
