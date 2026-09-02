# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 271**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–267 fixed physical multilinear polarization, null-soft 19-to-15 reduction, project-before-expand `A=K E`, physical `Gamma2`, nonzero Einstein `E2/E3`, exact `K0/K1/K2` 2/4/7 primitive library, the 28-primitive null-soft `A3` target, the exact 15-to-8 `B3` transpose-class reduction, and condensed-index/Fourier endpoint routing. Iteration 268 instantiated exact routed inverse recursion. Iteration 269 corrected the orbit-density orientation

`Y^up = g^-1/sqrt(|g|)`, `Y_down = sqrt(|g|) g`, `N_orb = Y_down Nhat`,

restoring second-order routed endpoint transpose for physical `N2/Q2`.

Iteration 270 then constructed the same-parent routed `A=R(DR)E` coefficients and the complete physical null-soft `B3=[Q A Q]_3` numerator. It froze

`PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED`,

with

`||B3[s,a,b](p0)||_F = 2.2209140981`, `max|B3| = 1.3471946832`,

at the frozen generic loop momentum `p0=(0.7,-0.4,0.5,0.9)`. Direct 15-term assembly and eight transpose-class reconstruction agree to `2.78e-16`; the endpoint-reversal envelope is `~3e-7`. The old `BLOCKED_NOT_ZERO` state remains superseded for this scoped numerator.

## Iteration 271 — closure-before-master-reduction hard gate

Before applying the raised bubble/triangle master map, the 15 surviving null-soft `B3` terms were expanded through the already frozen exact inverse recursion

`Q1[x] = -Q0 N1[x] Q0`,

`Q2[x,y] = Q0 N1[x] Q0 N1[y] Q0 + (x<->y) - Q0 N2[x,y] Q0`.

This yields exactly **23 primitive open-kernel branches**:

- 1 branch with 2 `Q0` factors;
- 10 branches with 3 `Q0` factors;
- 12 branches with 4 `Q0` factors.

At generic distinct leg labels, every branch has equally many distinct routed `Q0` momentum shifts as `Q0` factors. Four-distinct-resolvent open branches occur in the sequential `Q2 N1N1` and `Q1 A1 Q1` sectors.

Freeze:

`PASS_EXACT_OPEN_B3_RESOLVENT_RANK_CENSUS`.

For the frozen Iteration-270 external momenta,

`K=k_s+k_a+k_b=(1.1,0.8,0.85,0.8)`,

`K^2=0.7925` in the `(-,+,+,+)` convention, hence `K != 0`. Therefore the certified object is an open Fourier kernel

`<p+K|B3|p>`,

not by itself a closed loop trace.

Iterations 245/250 remain frozen and correct: the **closed composite Vilkovisky trace families** at the relevant order need no scalar polygon beyond raised bubbles/triangles (`I22`, `I222`, `I212` and descendants). Iteration 271 does not weaken that theorem. It establishes a scope/order constraint: the closed topology theorem cannot be imposed on an unclosed fixed-`p` kernel before the linked insertion carrying `-K` (or equivalent momentum-conservation closure) is specified.

A second hard constraint is independent: the Iteration-270 one-point value `B3(p0) != 0` proves algebraic nonzero but is not a tensor-integral numerator reconstruction. Tensor/master reduction requires `B3(p)` or a certified exact/rational interpolation basis over loop momentum with explicit routed denominators.

Freeze operational status:

`BLOCKED_MASTER_REDUCTION_UNTIL_KINEMATIC_CLOSURE_AND_P_DEPENDENT_INTEGRAND`.

Guardrails:

- `DO_NOT_FORCE_OPEN_B3_BRANCHES_INTO_CLOSED_BUBBLE_TRIANGLE_MASTERS_BEFORE_CLOSURE`;
- `ITER245_250_TOPOLOGY_BOUND_APPLIES_TO_CLOSED_COMPOSITE_TRACE_FAMILIES_NOT_TO_AN_UNCLOSED_FIXED_P_KERNEL`;
- `NONZERO_AT_ONE_P_IS_NOT_A_LOOP_INTEGRAND_RECONSTRUCTION`.

This is an operational BLOCKED / hard-ordering correction, not a consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

## Blocker update

The scoped numerator remains explicitly nonzero. The current C5 umbrella blocker is now

`BLOCKED_4D_EINSTEIN_VD_CLOSED_P_DEPENDENT_INTEGRAND_TENSOR_REDUCTION_SOURCE_PROJECTION_AND_LORENTZIAN_HARD_CHANNEL`.

The next authorized computation is **not** blind loop reduction of the fixed-`p` certificate. It is construction of the closure-aware p-dependent linked `T_cut` integrand, followed by a re-certified closed denominator family and only then scoped tensor/master reduction.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 270: **0 percentage points**. The iteration closes a logical ordering ambiguity and prevents an invalid master-map application, but does not yet produce the physical C5 comparator coordinate. Comparator foundation remains `24/25`; robust unique residual remains `0/20`.

## Retained program guardrails

- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction; the present nonzero C5 numerator alone is insufficient.
- `e+c<=3` remains the frozen finite-`R^3` truncation rule.
- Iteration 269 density correction supersedes only the old second-order density/N2/Q2 numerical representative, not earlier topology/polarization/K/E results.
- Endpoint transpose always means full condensed-index endpoint reversal / real `-K` sector, never raw same-routing matrix transpose.

## Retained comparator state

### C3
`BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` — not zero and not consistency FAIL.

### C4
Standalone positive two-point spectral/cut information remains mediator-degenerate.

### C5
`BLOCKED_4D_EINSTEIN_VD_CLOSED_P_DEPENDENT_INTEGRAND_TENSOR_REDUCTION_SOURCE_PROJECTION_AND_LORENTZIAN_HARD_CHANNEL`.

The scoped physical numerator is explicitly nonzero; the immediate missing object is a closure-aware p-dependent linked integrand.

### Other routes
Asymptotic-safety, nonlocal and proxy routes retain their frozen blockers; no proxy replaces the frozen comparator identity.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full C5 run: NOT AUTHORIZED.  
Direct master reduction of one-point `B3(p0)`: NOT AUTHORIZED.  
Closure-aware p-dependent integrand construction: AUTHORIZED.

## Iteration 271 authority files

- `candidate_gravity/C5_VD_OPEN_B3_INTEGRAND_CLOSURE_AUDIT_ITERATION271.md`
- `candidate_gravity/code/iteration271_open_b3_resolvent_rank_census.py`
- `candidate_gravity/results/iteration271_open_b3_resolvent_rank_census.json`
- `research_log/2026-09-02_iteration_271_open_b3_integrand_closure_audit.md`
- `recovery/RECOVERY_DELTA_ITERATION_271.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION271.md`

## Exact next gate — Iteration 272

Construct the **closure-aware, p-dependent linked `T_cut` integrand** for the already-certified null-soft `B3` sector:

1. introduce the explicit closing insertion/momentum `-K` required by the linked observable, without yet performing final source tensor projection;
2. expose `B3(p)` rather than only `B3(p0)`, keeping exact routed `Q0/Q1/Q2` denominators;
3. re-run the primitive denominator census after closure and verify explicitly that the resulting scalar families obey the frozen Iteration-245/250 raised bubble/triangle bound;
4. certify a finite numerator tensor degree/basis or rational interpolation basis sufficient for reproducible reconstruction;
5. only then perform scoped tensor/master-integral reduction and regular/log/nonanalytic hard-channel extraction.

Final source/Ward/contact projection, Lorentzian discontinuity, comparator quotient, Fisher/resources, and `ANSATZ-003` remain downstream.
