# RQIR Candidate Gravity — Iteration 273

## Translation-closed denominator-topology certificate

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Iteration 272 established the mandatory translation-closure condition for the physical closed three-point trace,

`k_s+k_a+k_b=0`,

and corrected the status of the Iteration-270 `K != 0` result to an off-conservation-surface parent-kernel nonidentity certificate rather than a physical closed three-point nonzero certificate.

This iteration asks an independent exact question before any master reduction: once the already frozen 15 null-soft `B3=[Q A Q]_3` terms are expanded through the exact inverse recursion and the global `K=0` condition is imposed, how many distinct routed `Q0` denominators survive in each primitive branch?

The exact routed recursion is

`Q1[x](p) = -Q0(p+k_x) N1[x](p) Q0(p)`,

and `Q2[x,y]` has the three primitive branches with Q0 shift sets

`{p+k_x+k_y, p+k_y, p}`,

`{p+k_x+k_y, p+k_x, p}`,

and

`{p+k_x+k_y, p}`.

Expanding the 15 surviving polarized Leibniz partitions again gives exactly 23 primitive branches, in agreement with Iteration 271. Before closure their Q0-factor census is 1 branch with two Q0 factors, 10 with three, and 12 with four.

After imposing `k_b=-(k_s+k_a)`, duplicate routed endpoints collapse exactly. The joint census becomes

- 1 branch: 2 Q0 factors but only 1 distinct denominator;
- 10 branches: 3 Q0 factors but only 2 distinct denominators;
- 12 branches: 4 Q0 factors but only 3 distinct denominators.

Therefore

`max distinct closed denominators = 3`,

and there are exactly zero four-distinct-denominator closed branches.

Freeze:

`PASS_EXACT_TRANSLATION_CLOSED_B3_DENOMINATOR_TOPOLOGY_REDUCTION`.

This directly reconciles the open-kernel Iteration-271 census with the frozen Iterations-245/250 theorem: on the translation-closed object the primitive denominator families fall back inside raised bubble/triangle topology. The 12 four-Q0 branches are raised-triangle descendants (three distinct denominators with one repeated factor), the 10 three-Q0 branches are raised-bubble descendants, and the remaining branch is a single-denominator-squared descendant.

This is not a proof that the translation-closed physical `B3` is nonzero, not a source/Ward-completed `T_cut`, and not a final C5 comparator coordinate. The already-added executable `iteration273_closed_kinematics_physical_b3.py` remains the next numerical authority step; if that K=0 rerun is stably nonzero, the following task is p-dependent numerator reconstruction inside the now-certified raised bubble/triangle families.

No `ANSATZ-003` is created. Fisher/resources and blind heavy full-C5 runs remain forbidden.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 272: 0 percentage points. A topology blocker is removed, but comparator foundation remains 24/25 and robust unique residual remains 0/20 because translation-closed physical B3 nonzero and comparator subtraction are not yet certified.
