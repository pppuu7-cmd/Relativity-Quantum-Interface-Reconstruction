# RQIR post497 — auto-research reconciliation and level-decomposed support preflight

Date: 2026-09-06
MODEL_READINESS: 24%

## Auto-research reconciliation
The hourly RQIR automation advanced the repository from the earlier post483 state through authoritative Iteration 497. The latest completed numerical mass-support authority is Iteration 496 rank17, raw-consumed PASS. Iteration 497 adds an exact odd-odd parity projection/provenance identity and is non-promoting.

Current frozen coverage before rank18 completion is 22/32 source occurrences = 68.75% = 1760/2560 row occurrences. The distinct certified prefix is ranks 0..17, i.e. 18/28 distinct coordinates.

The sole active heavy gate is manifest rank18 `(u,v)=(-2.5e-6,-5e-6)`, HALF local index 4, canonical run `34029482604`, job `101476261793`. No duplicate heavy run is authorized.

## New level-decomposed assembly preflight
A new exact static preflight reconstructs the frozen Iteration-455 level mapping:

BASE rank matrix (u-major/v-major):
`[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]`.

HALF rank matrix (u-major/v-major):
`[[5,16,17,6],[18,19,20,21],[22,23,24,25],[9,26,27,10]]`.

The only exact BASE/HALF shared-coordinate ranks are `[5,6,9,10]`; union is exactly ranks `0..27` with 28 distinct coordinates.

At the Iteration-497 snapshot:
- BASE local support is already `16/16 = 100%` certified.
- HALF local support is `6/16 = 37.5%` certified.
- Aggregate occurrence-weighted support is `22/32 = 68.75%`.
- Distinct-coordinate support is `18/28 = 64.28571428571429%`.
- HALF missing local ranks are `[18,19,20,21,22,23,24,25,26,27]`; rank18 is exactly the first missing HALF position and the sole active gate.

Classification: `PASS_LEVEL_DECOMPOSED_SUPPORT_AND_ASSEMBLY_MAPPING_PREFLIGHT__NON_PROMOTING`.

This decomposition is useful because the aggregate 68.75% figure hides the fact that BASE local support is already complete. However, no early numerical BASE assembly is authorized: the frozen contract still defers independent BASE/HALF assembly until all 28 distinct support coordinates are locally certified. No zero-fill, support reorder, u<->v inference, or threshold change is allowed.

Reproducible code: `candidate_gravity/code/post497_level_decomposed_support_preflight.py`.
Result: `candidate_gravity/results/post497_level_decomposed_support_preflight.json`.

If rank18 raw-consumes PASS, the purely local support counts become HALF `7/16 = 43.75%`, distinct `19/28 = 67.85714285714286%`, and occurrence-weighted `23/32 = 71.875%`; only rank19 then becomes authorized.

## New HALF parity-orbit no-skip audit
Combining the Iteration-497 odd-odd projection with the exact HALF rank matrix gives four disjoint parity orbits. Their exact coefficients before the common `1/h^2` factor are:
- `(|x|,|y|)=(1,1)`: `4/9`, ranks `[24,20,23,19]`;
- `(1,2)`: `-1/18`, ranks `[25,21,22,18]`;
- `(2,1)`: `-1/18`, ranks `[27,17,26,16]`;
- `(2,2)`: `1/144`, ranks `[10,6,9,5]`.

All four coefficients are exactly nonzero. At the current snapshot only the outer-outer `(2,2)` orbit is complete; the `(2,1)` orbit has only ranks 16 and 17 certified; the other two are incomplete. Every remaining rank 18..27 belongs to one of these incomplete nonzero-coefficient orbits.

Classification: `PASS_PARITY_PROJECTION_REDUCES_FORM_NOT_REQUIRED_SUPPORT__NON_PROMOTING`.

Exact consequence: Iteration-497 parity projection is an assembly/checksum reduction, not a license to skip HALF nodes. Without an additional independently frozen field-symmetry identity, all remaining ranks 18..27 remain necessary. Frozen manifest order therefore remains controlling.

Reproducible code: `candidate_gravity/code/post497_half_parity_orbit_support_audit.py`.
Result: `candidate_gravity/results/post497_half_parity_orbit_support_audit.json`.

## Retained physical status
Physical/operator authority remains Iteration 411. Iteration 421 remains raw-valid `BLOCKED_CONVERGENCE` at unresolved double-double index 2/class3/q^2=-1. No physical Ds authority exists. Robust comparator-subtracted residual remains absent; ANSATZ-003 is uncreated; Fisher/resources remain forbidden.

## Readiness
MODEL_READINESS: 24%
Readiness change: 0 percentage points. The new preflights close assembly/provenance bookkeeping subgates but no stable readiness-rubric component.
