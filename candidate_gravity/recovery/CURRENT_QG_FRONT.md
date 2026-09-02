# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 273**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–269 fixed the polarized same-parent construction, null-soft bookkeeping, field-space/orbit density conventions, exact routed inverse recursion and endpoint-transpose rules. Iteration 270 constructed the full routed null-soft cubic parent kernel `B3=[Q A Q]_3` and found it explicitly nonzero at generic `K!=0`; that result remains valid only as an off-conservation-surface parent-kernel nonidentity certificate after the translation-closure correction below.

Iteration 271 expanded the 15 surviving null-soft terms through exact Q1/Q2 recursion and found 23 primitive open-kernel branches: 1 with 2 Q0 factors, 10 with 3, and 12 with 4. For generic unclosed `K!=0`, the four-Q0 sectors can carry four distinct routed momenta.

Iteration 272 imposed the exact translation-invariance gate for a physical closed three-point trace:

`k_s+k_a+k_b=0`.

Freeze:

`PASS_EXACT_TRANSLATION_TRACE_CLOSURE_GATE`.

Correct status of the Iteration-270 nonzero result:

`VALID_OFF_CONSERVATION_SURFACE_PARENT_KERNEL_NONIDENTICAL_ZERO_CERTIFICATE; NOT_YET_PHYSICAL_THREE_POINT_NONZERO`.

## Iteration 273 — exact translation-closed denominator topology

The same 15 null-soft B3 partitions were expanded through the frozen exact routed Q1/Q2 recursion, and `k_b=-(k_s+k_a)` was imposed only after all Q0 momentum arguments were constructed.

The primitive branch count remains exactly 23, but duplicate routed endpoints collapse. The exact joint census is:

- 1 branch: `2 Q0 / 1 distinct denominator`;
- 10 branches: `3 Q0 / 2 distinct denominators`;
- 12 branches: `4 Q0 / 3 distinct denominators`.

Therefore

`max distinct closed denominators = 3`,

and there are exactly zero four-distinct-denominator closed branches.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_B3_DENOMINATOR_TOPOLOGY_REDUCTION`.

This reconciles Iteration 271 with the frozen Iterations 245/250 theorem: after physical translation closure, the B3 primitive families fall entirely within raised bubble/triangle descendants. The 12 four-Q0 branches are raised triangles with one repeated denominator; the 10 three-Q0 branches are raised bubbles; the remaining branch is single-denominator-squared.

This topology PASS does not prove that the translation-closed physical B3 is nonzero and is not a final linked `T_cut` comparator coordinate.

## Current C5 blocker

`BLOCKED_TRANSLATION_CLOSED_PHYSICAL_B3_NONZERO_AND_P_DEPENDENT_NUMERATOR_AUTHORITY`.

The existing executable

`candidate_gravity/code/iteration273_closed_kinematics_physical_b3.py`

implements the K=0 physical rerun using the Iteration-270 same-parent dynamics. Its committed numerical result is still missing. Master reduction remains forbidden until that closed numerator is stably classified and, if nonzero, promoted to a reproducible p-dependent numerator/integrand basis.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 272: **0 percentage points**. The translation-closed topology sub-blocker is now exactly closed, but no readiness rubric block closes because the physical K=0 numerator and final comparator coordinate remain uncertified.

## Retained program guardrails

- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- `e+c<=3` remains the frozen finite-R^3 truncation rule.
- Endpoint transpose means full condensed-index endpoint reversal, never raw same-routing matrix transpose.
- Do not reintroduce box masters from the unclosed K!=0 census: translation closure removes all four-distinct-denominator branches exactly.
- Do not claim the translation-closed B3 is nonzero until the K=0 rerun has a committed numerical certificate.
- Do not master-reduce a one-point numerator value.

## Retained comparator state

### C3
`BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` — not zero and not consistency FAIL.

### C4
Standalone positive two-point spectral/cut information remains mediator-degenerate.

### C5
Raised bubble/triangle topology after translation closure: exact PASS.  
Translation-closed physical B3 nonzero: OPEN / operational BLOCKED.  
p-dependent numerator, source/Ward/contact completion and Lorentzian hard-channel comparator: downstream BLOCKED.

### Other routes
Asymptotic-safety, nonlocal and proxy routes retain their frozen blockers; no proxy replaces the frozen comparator identity.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full C5 run: NOT AUTHORIZED.  
Master reduction before closed-numerator authority: NOT AUTHORIZED.

## Iteration 273 authority files

- `candidate_gravity/C5_VD_TRANSLATION_CLOSED_DENOMINATOR_TOPOLOGY_ITERATION273.md`
- `candidate_gravity/code/iteration273_translation_closed_denominator_census.py`
- `candidate_gravity/results/iteration273_translation_closed_denominator_census.json`
- `research_log/2026-09-02_iteration_273_translation_closed_denominator_topology.md`
- `recovery/RECOVERY_DELTA_ITERATION_273.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION273.md`

## Exact next gate — Iteration 274

Execute/refine the translation-closed physical B3 rerun on the K=0 family and commit a numerical certificate with finite-difference, permutation and endpoint-transpose envelopes. If the K=0 B3 is stably nonzero, reconstruct/sample the full p-dependent B3 numerator and certify a finite polynomial/rational basis, then perform scoped tensor/master reduction only within the now-certified raised bubble/triangle families. If the closed B3 is near-zero or numerically unresolved, improve derivative/precision authority before any master reduction.

Final source/Ward/contact projection, Lorentzian discontinuity, comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream.
