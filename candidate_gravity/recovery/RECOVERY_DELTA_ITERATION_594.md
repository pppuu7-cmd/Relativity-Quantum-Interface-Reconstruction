# Recovery Delta — Iteration 594

Date: 2026-09-08

## Authoritative change
Iteration 594 closes the explicit **full routed cubic source assembly** prerequisite downstream of Iter593.

Using the exact Iter368/Iter588 three-mode fixture, Iter589 same-action normalization, Iter590 inverse-kernel identity and Iter593 split-invariance rule, the complete MSSC-001 cubic source response was assembled as one object:

`d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G)`.

Thus the routed object contains simultaneously:
1. K3 contact;
2. all six K1/K2 placements, with both orientations;
3. all six ordered K1^3 chains.

No family was removed before assembly and no Source/Born subtraction was performed.

## Reproducible authority
- code: `analysis/source_full_cubic_routed_assembly_iteration594.py`;
- result: `candidate_gravity/results/iteration594_full_cubic_routed_assembly.json`.

Classification:
`PASS_FULL_SAME_ACTION_ROUTED_CUBIC_SOURCE_ASSEMBLY_AND_PERMUTATION_SYMMETRY__NON_WARD_NON_RESIDUAL`.

## Numerical result
Exact fixture momentum closure: `0.0`.

Frozen probe `p0=[0.43,-0.27,0.39,0.21]`:
- `-G K3 G = +0.01812399093080123`;
- six K1/K2 sum = `-0.005276095685186276`;
- six K1^3 sum before required minus sign = `+0.0012068925861444435`;
- full `d_abc G = +0.01164100265947051`;
- K3 last-step change `5.395683899678261e-08`;
- full six-label-permutation spread `6.734631775862088e-10`.

Frozen probe `p0=[0.61,0.19,-0.31,0.47]`:
- `-G K3 G = -0.0017882359820402566`;
- six K1/K2 sum = `+0.20405717388220662`;
- six K1^3 sum before required minus sign = `+0.12178043612382511`;
- full `d_abc G = +0.08048850177634126`;
- K3 last-step change `3.615857613326057e-08`;
- permutation spread `1.0009177930925262e-09`.

Inherited tolerances were not weakened: Iter368 closure `1e-14` and Iter590 K3 numerical envelope `2e-7` remain binding. Both probes pass comfortably.

## Binding interpretation
Iteration 594 is **not** a nonlinear Ward PASS and is not a Candidate-Gravity consistency PASS/FAIL. It removes the assembly ambiguity: the next Ward test now has a concrete complete 13-term same-action routed input, rather than an incomplete six-term K1/K2 subset.

Do not map this object to Iter582 yet. Do not perform Source/Born subtraction. Do not call this a comparator residual, exact comparator identity, near-degeneracy, model-level non-identifiability or novelty certificate.

The fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remains **operational BLOCKED** until the full source-level Ward contraction and the full-observable source-to-Iter582 map are closed.

`ANSATZ-003` remains forbidden. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Readiness change from Iter593: **0 percentage points**. A substantive hard prerequisite is closed, but no complete readiness-rubric sector is newly closed and no robust comparator-subtracted residual exists.

## Exact next gate
From the same MSSC-001 parent dynamics, derive and prospectively freeze the full cubic pure-gauge/Ward contraction target for the exact Iter594 routed 13-term object. Its inverse-propagator structure must reduce consistently to the authoritative Iter587 one-graviton Ward RHS. Then evaluate that full nonlinear Ward identity with K3 and K1^3 retained.

Only after source-level Ward closure may a full-observable source-to-Iter582/native-linked map be applied and the fixed comparator quotient become eligible.
