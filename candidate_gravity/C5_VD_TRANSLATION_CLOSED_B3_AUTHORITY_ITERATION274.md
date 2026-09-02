# RQIR Candidate Gravity — Iteration 274

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Purpose

Consolidate the two now-available translation-closed C5 certificates into one authoritative gate: (i) the exact denominator-topology reduction on `k_s+k_a+k_b=0`, and (ii) the committed numerical K=0 same-parent `B3=[Q A Q]_3` rerun.

## Exact closed-topology certificate

Expanding the 15 frozen null-soft B3 partitions through the exact routed Q1/Q2 inverse recursion gives 23 primitive branches. After imposing `k_b=-(k_s+k_a)`, the exact joint census is

- 1 branch with 2 Q0 factors but 1 distinct denominator;
- 10 branches with 3 Q0 factors but 2 distinct denominators;
- 12 branches with 4 Q0 factors but 3 distinct denominators.

Hence `max distinct closed denominators = 3`; no four-distinct-denominator branch survives. Freeze remains

`PASS_EXACT_TRANSLATION_CLOSED_B3_DENOMINATOR_TOPOLOGY_REDUCTION`.

This re-enters the frozen Iterations-245/250 raised bubble/triangle topology bound exactly; no box master is authorized from the open K!=0 census.

## Translation-closed physical B3 nonzero certificate

The committed K=0 rerun uses

`k_s=(1,0,0,1)`,
`k_a=(0.25,0.6,0.3,0.15)`,
`k_b=(-1.25,-0.6,-0.3,-1.15)`,

so the total shift vanishes exactly. It reports

`||B3||_F = 1.3106212324933462`,
`max|B3| = 0.5424761616499705`,

with endpoint-transpose residual `2.3948450944555333e-7`, step-scan absolute spread `2.4904473885145606e-5`, and relative spread `1.900170981140208e-5`.

The Frobenius norm exceeds the conservative numerical envelope by about `5.26e4`, while the maximum component exceeds it by about `2.18e4`. Therefore the K=0 numerator is not near-zero on this frozen family.

Freeze:

`PASS_SCOPED_TRANSLATION_CLOSED_NULLSOFT_B3_EXPLICIT_NONZERO`.

This supersedes `BLOCKED_PHYSICAL_B3_NONZERO_UNTIL_K_SUM_ZERO_RERUN`.

## Scope discipline

The result is a translation-closed physical parent-numerator certificate. It is still not the linked/source-completed `T_cut`, not a Lorentzian discontinuity, not a comparator-subtracted C5 residual, and not a novelty certificate.

The correct umbrella blocker is now

`BLOCKED_P_DEPENDENT_TRANSLATION_CLOSED_B3_RECONSTRUCTION_TENSOR_REDUCTION_SOURCE_COMPLETION_AND_LORENTZIAN_HARD_CHANNEL`.

Master reduction is now conditionally authorized only after a reproducible `B3(p)` numerator/basis reconstruction. Fisher/resources and `ANSATZ-003` remain forbidden.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 273: 0 percentage points. Two important C5 sub-gates are now closed, but the stable rubric does not award a new point until the physical comparator coordinate itself is produced. Comparator foundation remains 24/25; robust unique residual remains 0/20.
