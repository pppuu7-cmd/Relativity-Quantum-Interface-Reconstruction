# RQIR Candidate Gravity — Iteration 273

## Translation-closed null-soft physical B3 certificate

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Iteration 272 established that the Iteration-270 fixed-p nonzero kernel was evaluated off the momentum-conservation surface. This iteration reruns the exact same-parent routed `A=R(DR)E`, `Q0/Q1/Q2` and 15-term null-soft `B3=[Q A Q]_3` construction at

`k_s+k_a+k_b=0`.

Frozen kinematics:

- `k_s=(1,0,0,1)` with `k_s^2=0`;
- `k_a=(0.25,0.6,0.3,0.15)`;
- `k_b=(-1.25,-0.6,-0.3,-1.15)`;
- a fresh TT polarization is constructed for the new `k_b`.

## Result

The exact soft check remains satisfied:

`||A1[s]||_F = 1.0006e-9`.

The cubic A-layer permutation residual is

`8.64e-11`.

All 15 null-soft surviving partitions are included. At the frozen loop momentum `p0=(0.7,-0.4,0.5,0.9)`,

`||B3||_F = 1.3106212325`,

`max|B3| = 0.5424761616`.

The endpoint-reversal transpose residual is

`2.39e-7`.

Finite-difference step scans give `||B3||_F` from `1.3106189340` to `1.3106438385`, corresponding to a relative spread `1.90e-5`. The nonzero signal exceeds the conservative numerical envelope by orders of magnitude.

Freeze:

`PASS_SCOPED_TRANSLATION_CLOSED_NULLSOFT_B3_EXPLICIT_NONZERO`.

## Scientific meaning

The stronger statement is now certified: the same-parent C5 cubic Vilkovisky parent numerator remains explicitly nonzero **on the physical momentum-conservation surface**, not merely as an open off-closure kernel.

This removes

`BLOCKED_PHYSICAL_B3_NONZERO_UNTIL_K_SUM_ZERO_RERUN`.

It does not yet produce the linked `T_cut` comparator. A one-point value at `p0` is not a loop-integrand reconstruction, and tensor/master reduction still requires the closed `p`-dependent numerator and its actual denominator families.

## Readiness

`MODEL_READINESS: 24%`.

No rubric category closes yet: comparator foundation remains `24/25`, robust unique residual `0/20`. `ANSATZ-003`, Fisher and resource stages remain forbidden.

## Next gate

Re-run the Iteration-271 primitive inverse census under the exact `K=0` relation, identify routed denominator coincidences caused by momentum closure, and determine whether the earlier raised bubble/triangle topology bound is restored before constructing `B3(p)`.
