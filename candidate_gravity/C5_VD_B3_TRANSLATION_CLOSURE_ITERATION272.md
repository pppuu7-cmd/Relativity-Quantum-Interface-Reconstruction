# RQIR Candidate Gravity — Iteration 272

## Translation/trace closure gate for the routed cubic B3 kernel

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Input state

Iteration 270 established an explicitly nonzero routed cubic parent kernel `B3=[U1 W]_3` at one generic loop momentum. Iteration 271 then correctly observed that this object is an open kernel

`<p+K|B3|p>`

with

`K=k_s+k_a+k_b != 0`, so its primitive inverse-recursion branches cannot yet be identified with a closed loop master family.

## Exact closure statement

For a translationally invariant Fourier-space trace, the global spacetime integral produces

`(2 pi)^4 delta^4(k_s+k_a+k_b)`.

Equivalently, a closed three-point trace requires

`K=k_s+k_a+k_b=0`.

The Iteration-270 frozen momenta give

`K=(1.1,0.8,0.85,0.8)`,

with Minkowski square

`K^2=0.7925`.

Therefore the Iteration-270 nonzero result is a valid certificate that the same-parent cubic kernel is **not identically zero off the momentum-conservation surface**, but it is not yet a certificate that the physical translation-closed three-point numerator is nonzero.

Freeze:

`PASS_EXACT_TRANSLATION_TRACE_CLOSURE_GATE`.

Operational state:

`BLOCKED_PHYSICAL_B3_NONZERO_UNTIL_K_SUM_ZERO_RERUN`.

This supersedes any wording that calls the K-nonzero fixed-p object itself a final physical three-point comparator. It does **not** invalidate its non-identically-zero parent-kernel information.

## Closed rerun kinematics

Keep the exact Iteration-270 null-soft leg and hard `a` leg:

`k_s=(1,0,0,1)`,

`k_a=(0.25,0.6,0.3,0.15)`.

Choose

`k_b=-(k_s+k_a)=(-1.25,-0.6,-0.3,-1.15)`.

Then

`k_s+k_a+k_b=0`,

with `k_s^2=0`, `k_a^2=0.41`, `k_b^2=0.21` in the frozen `(-,+,+,+)` convention. Use an independently constructed TT polarization for `b`; do not recycle the old Iteration-270 `E_b` after changing its momentum.

## Why master reduction is still premature

Iteration 271 found 23 primitive inverse-recursion branches in the open B3 decomposition, with up to four distinct routed `Q0` factors. The earlier Iteration-245/250 bubble/triangle bound refers to closed composite traces; it cannot be imposed on the open K-nonzero kernel before closure.

After the K=0 rerun, rederive the denominator family from the actually closed p-dependent object. Only then decide whether cancellations reduce it to the earlier raised bubble/triangle families or whether additional intermediate denominators cancel only after summation.

## Executable next certificate

`candidate_gravity/code/iteration273_closed_kinematics_physical_b3.py`

reuses the exact Iteration-270 same-parent implementation, imposes `K=0`, rebuilds the `b` TT polarization, evaluates all 15 null-soft surviving partitions, checks endpoint transpose/permutation structure and scans finite-difference steps. It deliberately does not assume a nonzero answer.

If the closed B3 remains nonzero above its numerical envelope, the next gate is p-dependent numerator reconstruction and denominator-family derivation. If it becomes unresolved/near-zero, increase numerical authority before any loop reduction.

## Readiness

`MODEL_READINESS: 24%`.

No rubric block closes yet. Candidate residual: none. `ANSATZ-003`: not created. Fisher/resources: forbidden. Blind heavy C5 run: not authorized.
