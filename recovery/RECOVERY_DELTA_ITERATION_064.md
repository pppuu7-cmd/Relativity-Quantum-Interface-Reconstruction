# RQIR Recovery Delta — Iteration 064

**Date:** 2026-08-30

Authoritative predecessor: Iteration 063.

## What changed

Toy012 is not to be used as the physical D2 baseline after RQIR-CAL-019. The active local-source task is Toy013, with the detector spectral-tilt nuisance included inside source/calibration co-design.

New code: `analysis/toy013_physical_d2_codesign_iteration064.py`.

New rule **RQIR-DESIGN-005**: preserve both physical D2 harmonics during source optimization. The cheap objective uses `S_eff=4 p2 p4/(p2+p4)`, rejects severe band imbalance, and only then rewards conditioning. The expensive audit profiles spectral tilt together with source nuisances and re-optimizes centered mean/covariance calibration cost.

## Exact promotion gates

A Toy013 candidate may enter the master baseline only after executed checks confirm:

1. exact nearest-neighbour site Hamiltonian;
2. positive hidden states;
3. calibration-null residual < `1e-12`;
4. normalized tilt-profiled beta Fisher = 1 within numerical tolerance;
5. finite centered calibration allocation with spectral tilt included;
6. explicit comparison against Toy009 and both retained Toy011 points.

## Current status

Search code is committed but no numerical winner is claimed yet. This is intentional: unevaluated search output must not enter the recovery chain as a retained scientific result.

After execution, the winner (if any) should be propagated into independent source-metrology rate, fresh-copy/reset budget, D2 timing/additive systematics, and a common SI wall-clock comparison. NG-005, NG-006, NG-023, NG-026 and all relativistic/degeneracy gates remain active.