# RQIR Candidate Gravity — Iteration 271

## Open routed `B3` integrand-closure audit before master reduction

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Starting authority

Iteration 270 certified an explicitly nonzero routed null-soft cubic operator kernel

`<p+K|B3[s,a,b]|p>`

at the frozen generic point `p=(0.7,-0.4,0.5,0.9)`, with `||B3||_F=2.2209140981`, and authorized a scoped tensor/master-integral reduction. Iterations 245 and 250 separately froze a bubble/triangle topology bound for the **closed composite Vilkovisky trace families**.

Before reducing the Iteration-270 object, this iteration audits whether those two statements can be composed directly.

## Exact inverse-recursion census

The 15 surviving null-soft terms of

`B3=[Q A Q]_3`

were expanded only through the already frozen inverse recursion

`Q1[x] = -Q0 N1[x] Q0`,

`Q2[x,y] = Q0 N1[x] Q0 N1[y] Q0 + (x<->y) - Q0 N2[x,y] Q0`,

with the exact routed momentum convention of Iterations 267-270.

This produces **23 primitive resolvent branches**:

- 1 `A3 Q0 Q0` branch with 2 `Q0` factors;
- 6 `Q1 A2 Q0`/transpose branches with 3 `Q0` factors;
- 4 `Q2_contact A1 Q0` branches with 3 `Q0` factors;
- 8 ordered `Q2_sequential A1 Q0` branches with 4 `Q0` factors;
- 4 `Q1 A1 Q1` branches with 4 `Q0` factors.

Hence the exact open-kernel denominator-rank histogram is

`#Q0=2 : 1`,

`#Q0=3 : 10`,

`#Q0=4 : 12`.

Freeze:

`PASS_EXACT_OPEN_B3_RESOLVENT_RANK_CENSUS`.

## Routed-shift result

For generic distinct leg labels, every primitive branch has the same number of **distinct** routed `Q0` shifts as `Q0` factors. For example, sequential `Q2[x,y]` contains

`Q0(p+k_x+k_y) N1[x] Q0(p+k_y) N1[y] Q0(p)`

(or the opposite ordering), and after multiplication by the remaining `A1/Q0` block a four-resolvent open branch is possible.

At the frozen Iteration-270 momenta,

`K = k_s+k_a+k_b = (1.1,0.8,0.85,0.8)`,

so

`K != 0`,

and in the `(-,+,+,+)` convention

`K^2 = 0.7925`.

Thus the certified object is genuinely an **open** kernel mapping `p -> p+K`; it is not by itself a closed one-loop trace integrand.

## Why the Iteration-245/250 bound cannot be applied yet

The old topology result is retained without modification:

- closed composite Vilkovisky traces at cubic curvature order require no scalar loop polygon beyond bubble/triangle;
- their raised master families include `I22`, `I222`, `I212` and descendants.

But that theorem was established **after trace closure**. The Iteration-270 certificate instead fixes one open Fourier kernel at one loop-momentum point. The present census shows that before closure the exact recursion can expose four distinct routed inverse factors.

Therefore identifying those four open factors with a closed box master, or alternatively collapsing them by hand into a raised triangle, would both be unjustified. The missing information is the kinematic closure: the linked insertion carrying `-K` (or an equivalent momentum-conservation prescription) that converts the open operator kernel into the actual `T_cut` loop integrand. Only after that closure is explicit can one determine which endpoint factors are identified and re-apply the Iteration-245/250 bubble/triangle theorem.

This is a **scope/order correction**, not a contradiction of Iterations 245/250 and not a scientific consistency FAIL.

## Second hard constraint: fixed-p nonzero is not an integrand reconstruction

Iteration 270 establishes `B3(p0) != 0` at a generic `p0` and checks finite-difference stability. That is enough for the algebraic nonzero gate.

It is not enough for tensor integration. A master-integral reduction requires the numerator as a function of loop momentum `p` (analytically or via an exact interpolation/reconstruction scheme with a certified degree/rational denominator basis). A single value `B3(p0)` does not determine the tensor numerator coefficients.

Therefore the requested master reduction is operationally blocked until both are supplied:

1. **kinematic closure** of the open `+K` kernel into the linked `T_cut` object;
2. **p-dependent integrand reconstruction** of the same-parent numerator/denominator structure.

Freeze operational status:

`BLOCKED_MASTER_REDUCTION_UNTIL_KINEMATIC_CLOSURE_AND_P_DEPENDENT_INTEGRAND`.

Guardrails:

`DO_NOT_FORCE_OPEN_B3_BRANCHES_INTO_CLOSED_BUBBLE_TRIANGLE_MASTERS_BEFORE_CLOSURE`;

`ITER245_250_TOPOLOGY_BOUND_APPLIES_TO_CLOSED_COMPOSITE_TRACE_FAMILIES_NOT_TO_AN_UNCLOSED_FIXED_P_KERNEL`;

`NONZERO_AT_ONE_P_IS_NOT_A_LOOP_INTEGRAND_RECONSTRUCTION`.

## What remains true

The Iteration-270 nonzero certificate remains fully valid:

`PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED`.

No `BLOCKED_NOT_ZERO` is reinstated. The new blocker begins strictly **after** algebraic nonzero and before loop reduction.

This result is not:

- a consistency FAIL;
- an exact comparator identity;
- regime-specific non-identifiability;
- a near-degeneracy;
- a novelty certificate;
- a Candidate Gravity residual.

No `ANSATZ-003`, Fisher, resource estimate, or blind heavy-C5 run is authorized.

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 270: **0 percentage points**. The iteration prevents an invalid master-reduction step and precisely relocates the blocker, but it does not close comparator foundation beyond `24/25` and does not create a unique residual (`0/20`).

## Exact next gate — Iteration 272

Construct the **closure-aware, p-dependent linked `T_cut` integrand** for the already-certified null-soft `B3` sector:

1. introduce the explicit closing insertion/momentum `-K` required by the linked observable, without yet performing final source tensor projection;
2. expose `B3(p)` rather than only `B3(p0)`, keeping exact routed `Q0/Q1/Q2` denominators;
3. re-run the primitive denominator census after closure and verify explicitly that the resulting scalar families obey the frozen Iteration-245/250 bubble/triangle bound;
4. certify a finite numerator tensor basis/degree (or a rational interpolation basis) sufficient for reproducible reconstruction;
5. only then launch scoped tensor/master-integral reduction and nonanalytic hard-channel extraction.

Final source/Ward/contact projection, Lorentzian discontinuity, comparator quotient, Fisher/resources, and `ANSATZ-003` remain downstream.
