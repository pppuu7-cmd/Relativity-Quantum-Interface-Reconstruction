# Recovery Delta — RQIR Iteration 175

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Previous front

Iteration 174 established that a fixed covariant nonlocal tree action has nontrivial cubic operator structure, including a Fréchet variation of its nonlocal form factor, but its full closed-unitary/diffeomorphism tree amplitude is annihilated by the current coarse relation coordinates.

## New authoritative decomposition

Replace scalar `WardLock=0` by the soft tensor relation

`Gamma3_soft = W[K2] + Rlin_soft : B3 + higher-soft-order`.

- `W[K2]` is fixed by the same quadratic inverse kernel and source convention through the 1PI diffeomorphism Ward/covariantization relation. Treat it as exact shared/consistency structure.
- `Rlin:B3` is a separately gauge-invariant transverse/nonminimal three-point structure not fixed by the two-point kernel alone.

## Reproducible tensor certificate

For null `k=(1,0,0,1)` and pure-gauge `eps=k⊗xi+xi⊗k`:

- max linearized-Riemann component `5.55e-17`;
- norm `1.36e-16`.

For normalized TT plus polarization:

- max component `0.35355339059327373`;
- norm `2` to floating-point precision.

Under `k -> a k`, TT Riemann norm ratios are `0.25`, `4`, `9.000000000000002` for `a=0.5,2,3`, with maximum `k^2` scaling error `1.78e-15`.

Therefore the independent `Rlin:B3` structure is pure-gauge null, physically nonzero, and enters at sub-subleading `O(k^2)` soft order.

## New finite residual coordinates

For each of the six frozen amputated kinematic rows define

`B_T(i)=P_T[Gamma_arr(i)-W_i[K2]]`.

The Ward-determined longitudinal part is projected as hard shared structure. This leaves six transverse row coordinates **before** comparator subtraction.

The six-dimensional transverse space is not a Candidate Gravity residual by itself.

## Retained results

- `SOFT-NG-001 — WARD_DETERMINED_SOFT_CUBIC_PART_IS_SHARED_STRUCTURE_FIXED_BY_THE_TWO_POINT_KERNEL`;
- `SOFT-NG-002 — LINEARIZED_RIEMANN_THREE_POINT_FORM_FACTOR_IS_GAUGE_INVARIANT_AND_ENTERS_AT_SUBSUBLEADING_K2_ORDER`;
- `NG-FUNNEL-035 — REPLACE_SCALAR_WARDLOCK_WITH_WARD_SUBTRACTED_TRANSVERSE_CUBIC_COORDINATES`.

## Comparator boundary

- C3 ordered `B_T`: BLOCKED until nonlinear conserved diffusion plus explicit MSR-to-metric-CTP map exists;
- C4 `B_T`: requires fixed parent projection;
- C5 `B_T`: requires local EFT operator projection and is the immediate next target;
- fixed nonlocal `QG-NL-EXP-001` `B_T`: fixed in principle by the parent action but not yet numerically projected;
- AS `B_T`: BLOCKED real-time/source-completed three-point completion.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

No robust unique residual or parent dynamics exists.

## Exact restart instruction

Resume at **Iteration 176 — finite C5 transverse soft comparator basis**.

Required order:

1. freeze a target-independent local diffeomorphism-invariant C5 EFT operator subset capable of modifying sub-subleading soft structure at the declared truncation order;
2. project its source-completed cubic vertices into the six `B_T` coordinates;
3. compute rank, SVD tolerance and authority map without target optimization;
4. only after C5 is finite add fixed C4 and nonlocal transverse columns;
5. preserve C3 ordered and AS real-time transverse entries as BLOCKED unless explicitly derived;
6. no `ANSATZ-003`, Fisher or resources until a nonzero residual survives the full transverse comparator quotient.
