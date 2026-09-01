# Candidate Gravity — Iteration 220: pure-helicity source amplitude

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Iteration 219 used real factorized vector polarizations. Those are valid KLT gauge-algebra controls, but they are not by themselves pure Einstein helicity states. Iteration 220 keeps the old result and adds the physical-state projection.

For each null momentum choose two real transverse basis vectors `e1,e2` and define complex helicity vectors `(e1 + i e2)/sqrt(2)` and `(e1 - i e2)/sqrt(2)`. Matched helicities in the two KLT copies give pure spin-2 external states.

Frozen audit on the same scalar Compton kinematics (`m=0.7`, `sqrt(s)=2`, five angles, all four helicity pairs):

- momentum conservation error: `0`;
- mass-shell error: `3.33e-16`;
- helicity-vector transversality error: `1.41e-17`;
- helicity-vector null self-contraction: `5.55e-17`;
- independent-copy gravitational Ward residual: `2.96e-16`;
- graviton-exchange asymmetry: `1.78e-15`;
- nonzero stripped amplitude range: `0.01899 ... 11.68558`.

Classification: `PASS`. The `MSSC-001` nonlinear source tree block is validated for pure Einstein external gravitons.

Retain:

- `SRC-CORR-001 — REAL_FACTORIZED_KLT_POLARIZATIONS_ARE_GAUGE_ALGEBRA_CONTROLS_NOT_BY_THEMSELVES_PURE_HELICITY_EINSTEIN_STATES`;
- `SRC-NG-005 — MATCHED_COMPLEX_KLT_HELICITIES_GIVE_A_PURE_EINSTEIN_TWO_SCALAR_TWO_GRAVITON_BLOCK_WITH_MACHINE_PRECISION_WARD_TESTS`;
- `C5-CUT-019 — PURE_EINSTEIN_DYNAMICAL_SCALAR_SOURCE_TREE_BLOCK_IS_READY_FOR_PHYSICAL_UNITARITY_CUT_CONSTRUCTION`.

`MODEL_READINESS: 23%` — unchanged. The next gate is a connected scalar-source one-loop discontinuity built from physical intermediate states.
