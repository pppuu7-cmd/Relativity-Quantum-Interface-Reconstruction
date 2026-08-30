# RQIR Iteration 104 — Robust Campaign Simplex and Final-Significance Source Closure

**Date:** 2026-08-30  
**Status:** Paper-III robust scheduling / source-preparation consistency correction. Exact local-Gaussian results plus synthetic robustness regressions; not an apparatus forecast and not a new-physics claim.

## 1. Purpose

Iteration 103 showed that science, complex-transfer injection and all physical calibration campaigns belong in one concave profiled-Fisher scheduling problem. Two tasks remained immediately useful:

1. robustify that campaign simplex against apparatus uncertainty rather than optimizing only a nominal Fisher matrix;
2. audit the long-used `C_src=225` / 90%-retention convention against a **final** significance target after source-amplitude profiling.

The second audit exposes an important distinction between a raw detector benchmark and a final profiled significance certificate.

## 2. RQIR-NUM-006 — raw `5 sigma` retention is not final `5 sigma`

For the local multiplicative source-amplitude degeneracy, write

- raw detector Fisher for `beta`: `A`;
- independent source-amplitude Fisher: `C`.

After profiling the source amplitude,

`boxed{F_final = A C/(A+C)}`.

The mature benchmark used

`A=25`, `C=225`.

It indeed retains 90% of the raw detector information because

`F_final/A = 225/(25+225)=0.9`.

But numerically

`F_final=22.5`,

so

`sqrt(F_final)=4.74341649`,

not final `5 sigma`.

Therefore:

> **RQIR-NUM-006:** `C_src=225` is a valid **90%-retention of a raw 5-sigma detector benchmark**, but it must not be described as a final 5-sigma certificate after source-amplitude profiling.

No earlier NG-005 conclusion is changed. The correction is only about target bookkeeping.

## 3. Fixed-retention formula for a final target

If the desired final Fisher is

`F_*=Z_final^2`

and one chooses a retained fraction `r=F_final/A`, then exact consistency requires

`boxed{A = F_*/r}`

and

`boxed{C = F_*/(1-r)}`.

For final `Z=5` and `r=0.90`:

- required raw detector Fisher `A=27.7777777778`;
- required independent source Fisher `C=250`;
- final profiled Fisher is exactly `25`.

Thus the older `225` remains useful as a regression convention, while a final-target campaign must use the corrected pair or, preferably, optimize science and source metrology jointly.

## 4. Source metrology belongs in the campaign optimizer

Let `R_s` be the raw detector science Fisher rate along the local `(beta,alpha)` collinear direction, and let `R_a` be the independent source-amplitude Fisher rate.

With science time `T_s` and source-metrology time `T_a`,

`A=R_s T_s`, `C=R_a T_a`,

and

`F_final = A C/(A+C)`.

Equivalently,

`1/F_final = 1/(R_s T_s) + 1/(R_a T_a)`.

This is mathematically the same harmonic structure found for transfer calibration in Iteration 102, but here it closes NG-005 at the source-preparation level.

## 5. RQIR-RESOURCE-060 — jointly optimal source-retention fraction

For a required final Fisher `F_*`, minimizing

`T_s+T_a`

rather than fixing `r` in advance gives

`boxed{T_s/T_a = sqrt(R_a/R_s)}`

and

`boxed{T_min = F_* [1/sqrt(R_s)+1/sqrt(R_a)]^2}`.

The retained detector fraction at that optimum is

`boxed{r_* = sqrt(R_a)/(sqrt(R_s)+sqrt(R_a))}`.

A useful identity is that `r_*` equals the optimal science-time fraction of the two-campaign budget.

Therefore a fixed 90% source-retention target is wall-clock optimal only if

`r_*=0.9`,

which requires

`boxed{R_a/R_s = 81}`.

### RQIR-NG-059 — fixed 90% retention is not a universal optimum

If the physical source-metrology rate is not exactly 81 times the raw detector science rate in the normalized local two-parameter problem, pre-imposing 90% retention over-calibrates or under-calibrates relative to the minimum-time final-significance solution.

The `C_src=225` convention should therefore remain as a transparent benchmark/regression slice, not as a universal optimal resource rule.

## 6. Robust campaign simplex

Now let apparatus uncertainty be represented by a declared convex set `U`. For each uncertainty state `u` and campaign `k`, let the Fisher-rate matrix be `J_k(u)`.

For fixed campaign fractions `x` on the simplex, the retained rate in state `u` is

`F_u(x)=profile[sum_k x_k J_k(u)]`.

Define the guaranteed rate

`R_rob(x)=min_{u in U} F_u(x)`.

Because the Schur-complement profile is concave in the Fisher matrix and the Fisher matrix is affine in both campaign fractions and an affine apparatus uncertainty coordinate, `F_u(x)` is concave on each fixed branch.

The robust design is

`boxed{R_rob^* = max_{x in simplex} min_{u in U} F_u(x)}`.

### RQIR-RESOURCE-059 — robust campaign-simplex theorem

The worst-case campaign-rate function is concave in `x`, so the max-min campaign allocation remains a convex optimization problem.

If the declared uncertainty set is a polytope and every `J_k(u)` depends affinely on `u` while the same identifiable branch remains valid, the minimum over `u` is attained at an extreme point. Thus a finite vertex audit is an exact robust certificate for that declared polytope.

This does **not** authorize reducing non-affine PSD uncertainty, active-set changes, singularity crossings or non-Gaussian model uncertainty to arbitrary box vertices; those remain under NG-048-style finite robust treatment.

## 7. Robust equal-marginal certificate

At a robust optimum, several worst-case vertices may be simultaneously active. For each active vertex `v`, define its efficient direction `w_v` from Iteration 103.

There exist non-negative active-vertex weights `lambda_v`, summing to one, such that every active campaign satisfies

`boxed{sum_v lambda_v w_v^T J_{k,v} w_v = R_rob^*}`.

Inactive campaigns have no larger weighted marginal value.

This is the robust generalization of RESOURCE-058. One should not optimize a campaign against one central apparatus state and then merely evaluate another state afterward.

## 8. Deterministic robust regression

A transparent two-campaign/two-vertex model is used only to verify the theorem.

Vertex A:

`(R_s,R_a)=(1,9)`.

Vertex B:

`(R_s,R_a)=(9,1)`.

The robust optimum is exactly at equal campaign fractions

`x_s=x_a=0.5`,

with both vertices giving

`R_rob^*=0.45`.

The marginal profile-Fisher rates are

- vertex A: `(0.81,0.09)`;
- vertex B: `(0.09,0.81)`.

With equal active-vertex weights `1/2,1/2`, the weighted marginals are

`(0.45,0.45)`,

exactly equal to the robust rate as required by the KKT certificate.

For the affine segment connecting the two vertices, a dense deterministic scan verifies that the worst retained Fisher lies at one of the endpoints; the interior is better, reproducing the concave-uncertainty vertex result.

These numbers are regression-only and have no apparatus interpretation.

## 9. Consequence for the existing Paper-III wall-clock backbone

The late-front additive convention

`T_sci=Z^2/R_beta`,

`T_src=C_src/R_src`

with fixed `C_src=225` remains useful when one explicitly wants the historical raw-5-sigma / 90%-retention benchmark.

For a **final significance target**, the preferred procedure is now:

1. include source-amplitude metrology as a physical Fisher campaign in the same `(beta,theta)` parameterization;
2. include transfer calibration and seven detector/source calibration layers likewise;
3. maximize robust profiled Fisher per total pre-duty second using RESOURCE-059;
4. scale by `Z_final^2/R_rob^*`;
5. then apply mandatory duty/recertification constraints.

This removes an arbitrary fixed-retention choice from the final experiment-design problem while preserving the old convention as a regression slice.

## 10. What remains open

- physical common-normalization `J_k(u)` matrices for Toy009 and Toy014;
- robust temporal PSD/cross-PSD and transfer-rate uncertainty from one apparatus;
- source-metrology physical rate intervals `(p_E,Omega_E,t_reset,V)` in that same experimental architecture;
- mandatory control/reference recertification and non-overlap scheduling constraints;
- absolute NG-030 Toy009/Toy014 winner;
- classical/stochastic/full-QFT and relativistic/gauge/EFT/renormalization gates.

No new physics is claimed.

## 11. Next admissible gate

Build a **unified final-significance campaign certificate** for Toy009/Toy014 in which source metrology is no longer a fixed `C_src` add-on but a campaign Fisher matrix, while retaining the old 90%-raw benchmark as a regression check.

Then add control/reference duty as explicit scheduling constraints. If physical apparatus matrices remain unavailable, derive threshold surfaces in their measured rate ratios rather than fabricating an absolute winner.

Only after the robust marginal-cost certificate shows a genuinely source-dependent residual bottleneck should Toy015 be opened.

## 12. Reproducibility

Code:

`analysis/robust_campaign_source_target_iteration104.py`

The script verifies the `22.5 -> 4.7434 sigma` bookkeeping correction, the final-5-sigma `(A,C)=(27.7778,250)` fixed-retention pair, the jointly optimal source-retention formula, the special `R_a/R_s=81` condition for 90% optimal retention, the exact robust two-vertex optimum and its weighted marginal KKT certificate.
