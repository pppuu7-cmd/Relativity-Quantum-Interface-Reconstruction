# RQIR Iteration 091 — Tunable Dual-Mode f,2f Apparatus Design Envelope

**Date:** 2026-08-30  
**Status:** engineering/design-envelope closure built on Iterations 087–090; not an apparatus forecast and not a new-physics claim.

## 1. Purpose

Iteration 090 established that no audited published platform yet supplies the complete RQIR apparatus likelihood in one common normalization. The next admissible step is therefore not to splice best-in-class numbers from unrelated experiments, but to derive the exact performance surface that a tunable simultaneous `f,2f` detector must satisfy.

This iteration combines:

- robust correlated two-band science Fisher (087);
- seven-layer physical calibration throughput (088);
- joint source/calibration/control wall-clock closure (089);
- APP-002 prohibition on fabricating a fixed apparatus from incompatible literature data (090).

## 2. One common detector/calibration scale

Let `R0` be one physical Fisher-throughput scale supplied by a declared detector family. It may arise from an input-referred force PSD, transfer function, acceptance and live-time model. Do not interpret `R0` as a universal apparatus constant; it is a convenient common normalization for a parameterized design family.

Write the conservative raw science band rates as

`r2^- = a2 R0`,

`r4^- = a4 R0`,

with `a2,a4>0`, and let `rho_+` be the worst allowed effective cross-correlation from Iteration 087.

Then

`R_beta^- = s R0`,

where

`boxed{s = 4 a2 a4 / (a2+a4+2 rho_+ sqrt(a2 a4))}`.

Thus all science transfer/PSD imbalance and conservative cross-PSD information is compressed into the dimensionless coefficient `s` after the physical coordinate and uncertainty model are fixed.

For the seven same-time calibration layers write

`R_cal,j^- = k_j R0`,

where each `k_j>0` is obtained from the physical `2x2` matrix Fisher block using the Iteration-088 robust minimum-eigenvalue construction.

This is the required common normalization: science and calibration are not assigned unrelated arbitrary seconds conversions.

## 3. Detector + calibration coefficient

For target significance `Z` and calibration requirement `gamma`, define

`boxed{A = Z^2/s + gamma sum_j 1/k_j}`.

Then the conservative pre-duty time for science plus seven calibration layers is exactly

`T_det+cal = A/R0`.

This converts the old abstract Fisher quantities into one physical detector-throughput requirement while retaining the seven-layer audit trail through the individual `k_j`.

## 4. Add source preparation and control duty

Let

- `C_src` be the independent source-metrology Fisher requirement (for the standard late-front `Z=5`, 90% multiplicative-retention benchmark, `C_src=225`);
- `R_src^-` be the robust source-metrology rate, using the Iteration-089 max-design/min-uncertainty discipline;
- `d^+` be the conservative upper control/reference duty;
- `m=1/(1-d^+)`.

Then

`boxed{T_total^upper = m [ A/R0 + C_src/R_src^- ]}`.

This is a one-scale specialization of RESOURCE-042, not a replacement for it.

## 5. RQIR-RESOURCE-043 — exact f,2f feasibility surface

For a desired wall-clock cap `T_cap`, the source channel alone imposes the strict feasibility condition

`boxed{R_src^- > m C_src/T_cap}`.

If this condition fails, no finite improvement in detector PSD, calibration transduction, bandwidth or repetition rate can satisfy the time cap.

When it holds, the minimum common detector/calibration scale is

`boxed{R0_min = m A / [T_cap - m C_src/R_src^-]}`.

This is the requested design envelope.

Properties:

1. `R0_min` diverges as `R_src^-` approaches the source-only floor from above;
2. as `R_src^- -> infinity`, `R0_min -> m A/T_cap`;
3. improving a single science band changes `s` through the full correlated two-band law rather than through a scalar ASD;
4. improving one calibration layer matters harmonically through `sum 1/k_j`, so a single slow layer can dominate;
5. duty inflates both source and detector/calibration requirements consistently.

## 6. RQIR-NG-041 — detector improvements cannot rescue a source-throughput violation

The inequality

`R_src^- > m C_src/T_cap`

is a strict no-rescue boundary for this architecture class.

If preparation/reset/visibility/coherence make `R_src^-` equal to or below that floor, taking `R0 -> infinity` still gives

`T_total^upper >= T_cap`.

This is distinct from NG-005. NG-005 says independent source information is structurally required; NG-041 says that even after such a channel exists, insufficient physical source throughput can make a declared wall-clock target impossible regardless of detector sensitivity.

## 7. Shot/repetition interpretation

If the common detector scale is realized by attempts with

- per-attempt reference information `i0`;
- acceptance `p`;
- cycle time `t_cyc` including the required coherent evolution plus read/reset overhead,

then

`R0 = p i0/t_cyc`.

Therefore the envelope can be rewritten as

`p i0/t_cyc >= R0_min`.

This directly connects the design surface to shot noise, accepted repetitions, coherence-time floor and dead/reset time. A proposed point that requires `t_cyc` below the source coherent evolution span is inadmissible by RESOURCE-002.

Likewise, each calibration layer has accepted information per attempt `k_j i0` only if that scaling follows from the same declared physical likelihood. Otherwise its rate must be supplied independently and the more general Iteration-089 certificate used.

## 8. Transparent numerical slice — not a forecast

Use only as an algebraic scale check:

- `Z=5`;
- `C_src=225`;
- `T_cap=7 days`;
- `d^+=0.05`;
- equal raw science coefficients `a2=a4=1`;
- `rho_+=0`, hence `s=2`;
- seven normalized calibration coefficients `k_j=1`.

The strict source-rate floor is

`boxed{R_src^- > 3.91604010025e-4 s^-1}`.

At exactly the floor, `R0_min` diverges.

At `R_src^-=10` times the floor, source metrology consumes 10% of the allowed campaign after duty inflation. Using the repository gamma values only as a normalized design slice:

Toy009 `gamma_mean=1.830264703e6` gives

`A_009 = 1.2811865421e7`,

`R0_min ~= 24.7761870 s^-1`.

Toy014 `gamma_mean=5.6776851e6` gives

`A_014 = 3.9743808200e7`,

`R0_min ~= 76.8584428 s^-1`.

These `R0` numbers are not hardware requirements because `k_j=1` and the band coefficients were deliberately normalized. Their only role is to verify the scaling and expose why the calibration burden cannot be omitted.

## 9. Architecture comparison and Toy014 regression

For two architectures under the same common `R0` and duty,

`T_i - T_k = m[(A_i-A_k)/R0 + C_i/R_src,i - C_k/R_src,k]`.

Therefore a branch that is worse on detector+calibration coefficient `A` can win only if it has a sufficiently large source-metrology time advantage.

The old shared-kernel Toy014/Toy009 projected model is recovered exactly:

`3.53338589945 + 3.48482822888 x + 0.67054046 y < 1+x+y`,

or

`boxed{y > 7.6895205385 + 7.5421347000 x}`.

Iteration 091 does not promote this projected boundary to an apparatus forecast. It is retained as a regression slice. A physical Toy009/Toy014 comparison must construct source-specific `a2,a4,rho,k_j,R_src,d` with uncertainties and then apply NG-030.

## 10. Scientific consequence

The late Paper-III problem has now been reduced from “find an apparatus ASD” to a finite set of measurable dimensionless performance coefficients plus two absolute rate scales:

- science coefficients `(a2,a4,rho)`;
- seven calibration coefficients `k_j`;
- absolute detector/calibration throughput `R0`;
- robust independent source rate `R_src`;
- duty `d`.

Given these, the wall-clock cap and robust branch comparison are algebraic.

The missing physics is therefore not another Fisher identity. It is construction or measurement of a self-consistent apparatus map that supplies these coefficients in one physical normalization.

## 11. Next admissible gate

Use the envelope to solve the **Toy009/Toy014 source-throughput crossover in physical rate coordinates** rather than the old abstract `(x,y)` plane:

1. include the known Toy014 Ramsey rate advantage and reset/visibility dependence;
2. retain source-specific science/calibration coefficients rather than assuming common kernels;
3. derive robust crossover surfaces in `(R0,R_src,d)`;
4. identify whether the winning region is source-metrology dominated enough to justify a new Toy015 search.

Do not start Toy015 unless that rate-space analysis shows a source-dependent bottleneck that source redesign can actually improve.

## 12. Reproducibility

Run

`python analysis/tunable_f2f_apparatus_envelope_iteration091.py`.

The script checks the science coefficient identities, source floor/divergence, exact cap saturation for the analytic `R0_min`, the Toy014/Toy009 shared-kernel regression, and 1000 deterministic random envelope points.
