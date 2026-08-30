# RQIR Iteration 089 — Joint Robust Total-Time Certificate

**Date:** 2026-08-30  
**Status:** Paper-III robustness/resource gate; not an apparatus forecast and not a new-physics claim.

## 1. Purpose

Iterations 087 and 088 separately closed conservative science-rate and seven-layer calibration-rate bounds. The remaining algebraic step before apparatus insertion is to combine those with bounded independent source metrology and control/reference duty into one exact wall-clock interval suitable for RQIR-NG-030.

This iteration also fixes an optimization-under-uncertainty issue in the source-metrology layer.

## 2. Total wall-clock model

For one architecture use

`T_total = [Z^2/R_beta + gamma sum_j 1/R_cal,j + C_src/R_src] / (1-d)`

with seven positive calibration rates and `0<=d<1`.

For the common retained preparation target, `C_src=C_prep=[r/(1-r)]Z^2`; at `Z=5`, `r=.90`, `C_prep=225`.

Assume independent interval bounds

`R_beta in [R_beta^-,R_beta^+]`,

`R_cal,j in [R_cal,j^-,R_cal,j^+]`,

`R_src in [R_src^-,R_src^+]`,

`d in [d^-,d^+]`.

The wall time is strictly decreasing in every positive Fisher rate and strictly increasing in duty loss `d`.

Therefore the exact Cartesian-box extrema are

`boxed{T_total^upper = [Z^2/R_beta^- + gamma sum_j 1/R_cal,j^- + C_src/R_src^-]/(1-d^+)}`

and

`boxed{T_total^lower = [Z^2/R_beta^+ + gamma sum_j 1/R_cal,j^+ + C_src/R_src^+]/(1-d^-)}`.

No multidimensional Monte Carlo is needed for this independent bounded-uncertainty model.

## 3. RQIR-RESOURCE-042 — exact joint interval certificate

The pair

`[T_total^lower,T_total^upper]`

is the exact robust wall-clock interval for the current Cartesian product of rate/duty intervals.

It composes directly with:

- Iteration-087 `R_beta^-` from the correlated two-band spectral matrix;
- Iteration-088 `R_cal,j^-` from the seven PSD-safe matrix-Fisher uncertainty sets;
- a physically derived independent `R_src^-`;
- an upper campaign control/reference duty `d^+`.

For correlated apparatus uncertainties shared across science, calibration, source metrology or duty, this independent-box interval remains conservative only if the separate extrema are jointly admissible. Otherwise a joint uncertainty model must be optimized directly.

## 4. NG-030 becomes a one-number margin

For architectures `i` and `k`, define

`M_{i<k}=T_k^lower-T_i^upper`.

Then

- `M_{i<k}>0`: architecture `i` is robustly faster;
- `M_{i<k}<=0`: robust dominance of `i` is not certified.

The reverse margin is evaluated separately. If neither is positive, the architecture intervals overlap and NG-030 requires the decision to remain unresolved.

A transparent synthetic regression gives

- architecture A: `[45.8754208754,70.2319587629] s`;
- architecture B: `[50.5281059792,68.9506673882] s`.

The intervals overlap; neither branch is robustly dominant despite different central tendencies. These numbers are regression-only.

## 5. Source metrology under uncertain apparatus parameters

The independent Ramsey resource layer has the physical structure

`R_src(phi,u)=p_E F_alpha(phi,V)/(t_reset + phi/Omega_E)`

where `u` denotes uncertain apparatus quantities such as acceptance, visibility, coupling rate and reset overhead.

A subtle but important distinction arises when the protocol setting `phi` must be chosen before the true apparatus parameters are known precisely.

The correct guaranteed rate is

`boxed{R_src^- = max_phi min_{u in U} R_src(phi,u)}`.

By the elementary minimax inequality,

`max_phi min_u R <= min_u max_phi R`.

The right-hand side corresponds to re-optimizing `phi` separately for every uncertainty realization and then taking the worst result. It can therefore be optimistic when the experiment cannot retune freely after the unknown state of the apparatus is revealed.

## 6. RQIR-NG-039 — post-hoc optimized source rate is not automatically robust

A source-metrology lower rate used in NG-030 must respect the actual order of experimental decisions and uncertainty realization.

If the Ramsey/pointer setting is frozen in advance, use

`max_design min_uncertainty R`.

Using

`min_uncertainty max_design R`

without an explicit adaptive calibration/retuning protocol can overstate source-metrology throughput and understate `T_src^upper`.

A deterministic positive-rate counterexample uses

`R(q,u)=exp[-(q-u)^2]`, `u in {-1,+1}`.

Then

`max_q min_u R = exp(-1)=0.36787944117`,

whereas

`min_u max_q R = 1`.

The factor `e` gap is entirely due to the optimization order. This is a generic decision-theory correction, not new physics.

If adaptive retuning is physically available, its calibration time, state-estimation uncertainty and duty must be included before using the post-hoc envelope.

## 7. Relation to C_a and gamma

The resource chain is now explicit:

### Source preparation / NG-005

A required independent preparation information `C_a` or `C_prep` becomes

`T_src=C_a/R_src`.

For per-copy Fisher `I_src`, acceptance `p`, interaction/read/reset cycle time `t_cyc`,

`R_src=p I_src/t_cyc`,

subject to visibility/coherence and robust protocol optimization.

### Seven-layer calibration

A required nuisance-calibration strength `gamma` becomes

`T_cal=gamma sum_j 1/R_cal,j`,

where every `R_cal,j` is a full two-probe matrix-Fisher rate, not a marginal SNR proxy.

Thus the old abstract Fisher coordinates are now connected to physical repetition count, acceptance/shot noise, coherence-constrained cycle duration, state reset/preparation, detector transfer/noise and total wall time.

## 8. What remains open for Toy009/Toy014

The **rate algebra is now sufficient** to perform a robust branch comparison as soon as one declared apparatus supplies uncertainty intervals for:

1. two-band science transfer and full PSD/cross-PSD -> `R_beta^-/R_beta^+`;
2. seven same-time calibration matrix Fisher blocks -> `R_cal,j^-/R_cal,j^+`;
3. independent source-metrology apparatus -> robust `R_src^-/R_src^+` with correct max/min order;
4. campaign control/reference duty -> `[d^-,d^+]`.

Do not substitute old illustrative ASD, phase-noise or unit-transduction numbers as measurements.

## 9. Next admissible gate

The next high-value scientific step is no longer another normalized Fisher derivation. It is to construct one **declared physical reference apparatus envelope** from externally sourced or explicitly design-level D1/D2 parameters and feed it through the Iteration-089 certificate.

If externally published data cannot supply all needed cross-PSD/calibration/source-metrology quantities, record the missing coordinates explicitly and retain the result as a feasibility envelope rather than a forecast.

## 10. Reproducibility

Run

`python analysis/joint_robust_total_time_iteration089.py`.

The script verifies the monotone endpoint formula against direct corner enumeration, implements the NG-030 dominance margin and checks the max-min/min-max source-metrology counterexample.
