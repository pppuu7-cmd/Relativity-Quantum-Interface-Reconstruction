# RQIR Iteration 093 — Robust Toy009/Toy014 Physical Crossover Under Source-Specific Uncertainty

**Date:** 2026-08-30  
**Status:** Paper-III robustness/resource gate; parameterized apparatus result, not a hardware forecast and not a new-physics claim.

## 1. Purpose

Iteration 089 gave exact robust wall-clock intervals for a single architecture. Iteration 092 gave the exact Toy009/Toy014 physical crossover for fixed source-specific coefficients. The next admissible step is to combine those two results analytically: solve the Toy009/Toy014 crossover itself when detector+calibration coefficients, source-metrology rates and duty are uncertain.

This is the required bridge from nominal RESOURCE-044 to the NG-030 robust architecture decision.

For architecture `i`, retain

`T_i = m_i [A_i/R0 + C_src/R_src,i]`,

`m_i = 1/(1-d_i)`,

with independent declared intervals

`A_i in [A_i^-,A_i^+]`,

`R_src,i in [R_src,i^-,R_src,i^+]`,

`d_i in [d_i^-,d_i^+]`.

The physical throughput `R0>0` is treated as a declared common apparatus axis. If the two sources require genuinely different absolute detector throughput scales, the more general Iteration-089 rate form must be used instead.

## 2. Exact architecture time envelopes

Because total time increases with `A`, increases with duty loss `d`, and decreases with `R_src`, the exact Cartesian-box extrema are

`T_i^upper(R0) = m_i^+ [A_i^+/R0 + C_src/R_src,i^-]`,

`T_i^lower(R0) = m_i^- [A_i^-/R0 + C_src/R_src,i^+]`,

where

`m_i^- = 1/(1-d_i^-)`,

`m_i^+ = 1/(1-d_i^+)`.

This is the Iteration-089 monotonicity result specialized to the compressed physical `A_i` representation of Iterations 091–092.

## 3. RQIR-RESOURCE-045 — exact robust crossover law

To certify Toy014 faster than Toy009 under NG-030, require

`T_14^upper(R0) < T_09^lower(R0)`.

Define the worst-case detector/calibration difference

`D_14|09 = m_14^+ A_14^+ - m_09^- A_09^-`,

and worst-case source difference

`S_14|09 = C_src [m_14^+/R_src,14^- - m_09^-/R_src,09^+]`.

Then

`boxed{T_14^upper - T_09^lower = D_14|09/R0 + S_14|09}`.

Therefore the robust dominance region is obtained without Monte Carlo.

When `D_14|09>0` and `S_14|09<0`, the usual Toy014 rescue regime survives uncertainty, but only above

`boxed{R0 > R0_cross,14|09^rob = -D_14|09/S_14|09}`.

The reverse certificate is separate. Define

`D_09|14 = m_09^+ A_09^+ - m_14^- A_14^-`,

`S_09|14 = C_src [m_09^+/R_src,09^- - m_14^-/R_src,14^+]`.

Toy009 is robustly faster wherever

`D_09|14/R0 + S_09|14 < 0`.

The two boundaries need not coincide.

## 4. Full sign classification

For a generic robust difference

`g(R0)=D/R0+S`,

the exact positive-throughput winning region `g<0` is:

1. `D<=0, S<=0`, with at least one strict: all `R0>0`;
2. `D>=0, S>=0`: no positive `R0`;
3. `D>0, S<0`: `R0>-D/S`;
4. `D<0, S>0`: `0<R0<-D/S`.

Case 4 is physically important: if an architecture has a detector/calibration advantage but a source-metrology disadvantage, increasing detector throughput can eventually remove the very resource axis on which it was winning.

Thus "better detector" does not imply a fixed architecture ranking; it changes the relative weight of source and detector/calibration costs.

## 5. RQIR-NG-043 — robust dominance can have an unresolved throughput band

The robust Toy014 boundary and robust Toy009 boundary are constructed from different worst/best endpoints. Consequently there can exist

`R0_cross,09|14^rob < R0 < R0_cross,14|09^rob`

where neither

`T_14^upper < T_09^lower`

nor

`T_09^upper < T_14^lower`

holds.

In this interval the nominal RESOURCE-044 ranking may have a definite sign, but NG-030 forbids a robust architecture claim.

This is not a numerical nuisance. It is the direct decision-theoretic consequence of source-specific apparatus uncertainty.

### Design consequence

The width of this unresolved band is itself a useful apparatus-characterization target. Reducing uncertainty in the coordinates that move the two robust boundaries most strongly can be more valuable than increasing the nominal Fisher rate.

## 6. RQIR-NG-044 — Pareto ratios are not a robust physical certificate

The retained Toy014 summary factors

`q_s=3.53338589945`,

`q_c=3.48482822888`,

`q_p=0.67054046`

remain useful shared-kernel regression summaries, and Iteration 092 preserves the historical boundary derived from them.

However these three ratios alone do not determine

`A_i^-, A_i^+, R_src,i^-, R_src,i^+, d_i^-, d_i^+`.

In particular they do not encode source-specific transfer-function uncertainty, two-band cross-PSD uncertainty, all seven matrix calibration-rate intervals, or duty uncertainty. Therefore they are **not sufficient statistics for NG-030 robust dominance**.

A robust Toy009/Toy014 decision requires the physical interval certificate, not only the normalized `(q_s,q_c,q_p)` vector.

This sharpens, rather than replaces, APP-001/NG-032 and NG-040: absolute and joint apparatus characterization cannot be manufactured from normalized source ratios or stitched subsystem benchmarks.

## 7. Transparent regression example

Use a deliberately synthetic, dimensionless test box only to verify the algebra:

Toy009:

- `A in [1.0,1.1]`;
- `R_src in [1.0,1.1]`;
- `d in [0.02,0.04]`.

Toy014:

- `A in [3.3,3.8]`;
- `R_src in [1.4,1.6]`;
- `d in [0.03,0.06]`.

With `C_src=225`, the exact certificates give

`Toy009 robustly faster for R0 < 0.025237237237237236`,

`Toy014 robustly faster for R0 > 0.08006274509803925`.

Hence the interval

`[0.025237237237237236, 0.08006274509803925]`

is unresolved by NG-030 even though a nominal central-value crossover could be reported inside it.

These values are regression-only and are not a detector specification.

## 8. Numerical verification

`analysis/robust_physical_crossover_iteration093.py` verifies:

- the exact endpoint time envelopes against all eight Cartesian corners per architecture;
- the analytic robust crossing values above;
- 10,000 fixed-seed random interior draws lying inside the analytic time intervals;
- explicit low-`R0`, unresolved-band and high-`R0` architecture decisions.

## 9. What is now closed and what remains open

Closed algebraically:

- `C_src`/NG-005 to physical source-metrology time;
- `gamma` to seven-layer physical calibration repetitions/rates/time;
- correlated two-band science rate and uncertainty lower envelope;
- joint robust total-time interval;
- fixed-parameter physical Toy009/Toy014 crossover;
- now the **interval-robust physical crossover itself**.

Still open experimentally:

- source-specific `A_009` and `A_014` intervals from one declared apparatus;
- robust Ramsey/pointer `R_src` intervals in that same apparatus;
- duty/control intervals and their correlations;
- joint uncertainty if the independent-box extrema are not simultaneously admissible.

## 10. Next gate

Do not begin Toy015 yet.

The highest-value next step is an **information-value / uncertainty-budget gate**: differentiate the two robust crossover boundaries with respect to `A_i`, `R_src,i` and `d_i`, identify which measured apparatus coordinate most efficiently shrinks the NG-043 unresolved band, and convert that into a prioritized characterization specification.

If a repository-backed or externally sourced common apparatus later supplies the full source-specific intervals, insert them directly into RESOURCE-045 and test NG-030 without changing the algebra.
