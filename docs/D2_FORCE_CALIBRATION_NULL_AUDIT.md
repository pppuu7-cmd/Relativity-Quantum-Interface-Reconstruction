# RQIR Iteration 025 — D2 Force-Calibration Null Audit

**Date:** 2026-08-29  
**Scope:** detector/calibration consistency gate. No new-physics claim.

## 1. Question

Iteration 022 wrote a physical D2 mean-calibration Fisher rate in terms of an equivalent-force template. Iteration 024 then made explicit that SI conversion requires a branch-specific readout Jacobian.

This raises a structural question that must be answered before assigning D2 wall-clock time:

> If the existing Toy009 NP3 potential-mean calibration is physically implemented by a D2 force/gradient readout, does the exact hidden source direction remain in the calibration nullspace?

For the current geometry, the answer is **no**.

## 2. Existing NP3 null

The authoritative Toy009/Iteration-011 calibration matrix has 24 row-normalized constraints in a 25-dimensional Hermitian source space and rank 24. Let `n` denote its exact null direction:

`A n = 0`.

This exact null underlies the hidden-amplitude discussion and RQIR-NG-005.

## 3. Direct force/gradient rows

The potential probe operator at dimensionless probe coordinate `y` is

`B(y) = V diag[1/(scale/lambda_i-y)] V^T`

for the current geometry, where all denominators are positive at `y=0` and `y=Y1`.

A direct Newtonian force readout is proportional to the spatial derivative,

`G(y) = dB/dy = V diag[1/(scale/lambda_i-y)^2] V^T`.

I constructed the same 14 time-sampled mean rows used by the NP3 potential calibration, but with `B(y)` replaced by `G(y)`, and row-normalized them independently.

## 4. Numerical result

The projections of the 14 normalized force rows on the exact Toy009 hidden direction are not zero.

For the current source and Iteration-011 geometry:

- maximum `|g_i . n| ~ 1.43036e-2`;
- RMS projection `~6.13671e-3`.

When all 14 force rows are appended to the original 24-row NP3 calibration matrix:

- original rank: `24/25`;
- augmented rank: `25/25`;
- augmented smallest singular value: `~3.0014e-3`.

Thus the exact one-dimensional calibration null is removed.

## 5. RQIR-NG-009 — calibration-observable mismatch

> A detector-native observable may not be substituted for an NP3 calibration observable while keeping the same nullspace assumptions. For current Toy009, direct force-gradient mean rows see the hidden direction and therefore destroy the exact NP3 null.

This is not a failure of D2. It is a bookkeeping/experimental-design constraint: the physical calibration operator is part of the protocol definition.

## 6. Consequence for RQIR-NG-005

RQIR-NG-005 remains valid **conditional on the declared gravitational null calibration** `A n=0`.

If D2 calibration adds force-gradient rows that satisfy `G n != 0`, then the amplitude `a` of the hidden source direction acquires gravitational calibration information. The Fisher problem must be rebuilt with the augmented calibration matrix. One may no longer reuse the old `F_beta|a=0` obstruction unchanged.

The exact-null design and the physical calibration implementation must therefore be co-designed.

## 7. Consequence for Iteration 022 D2 rate formula

The native force-template Fisher formula

`I_i = 4 int |dh_i/du_i|^2 / S_F df`

is mathematically correct for a D2 force readout. However, the resulting information belongs to the *actual force-calibration Jacobian*. It cannot automatically be assigned to the existing NP3 potential-row Fisher matrix.

There are two scientifically valid paths:

1. preserve the Toy009 exact null by physically realizing the declared potential/covariance calibration observables with a beta-blind transducer; or
2. accept detector-native force calibration, rebuild the augmented calibration matrix/nullspace, and re-run source optimization, RQIR-NG-005, D1/D2 profiled Fisher, and resource budgets.

The second path may improve identifiability, but it is a **different protocol**.

## 8. Physical scaling distinction

For D1 potential-phase calibration, a raw potential coordinate has the direct weak-field transduction

`d phi / d B = Gamma_G = G m_s m_p T_D / (hbar L0)`

(up to the declared control/filter response), so the Iteration-024 row-norm map can be converted directly once `Gamma_G` is specified.

For D2 force readout,

`F = -(G m_s m_p/L0^2) dB/dy`,

which probes a derivative operator rather than `B` itself. That is precisely why the nullspace can change.

## 9. Scientific status

This iteration closes an internal detector/calibration consistency gate and prevents an invalid SI-time assignment for D2. It does not establish experimental feasibility and does not close any relativistic/QFT/interface-class degeneracy gate.

## 10. Next gate

The highest-value continuation is to build and compare two explicit calibration protocols:

- **D2-null-preserving:** retain the exact NP3 potential/noise rows and provide an independent physical transducer for them;
- **D2-native-force:** augment/replace rows by force-gradient observables, then recompute the exact/soft nullspace and detector-level `F_{beta|theta}` from scratch.

Only after that comparison should D2 force-PSD calibration time be inserted into the full wall-clock optimizer.
