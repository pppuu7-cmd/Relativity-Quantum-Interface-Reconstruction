# RQIR Research Log — Iteration 013

**Date:** 2026-08-29  
**Topic:** heterogeneous physical calibration Fisher allocation  
**Labels:** `DRV`, `NUM`, `NEG`, `OPEN`

## Starting point

Iteration 012 established that scalar `gamma` is not a physical shot count. The current source/calibration baseline is the Iteration-011 balanced Toy009 geometry. The next gate was to replace equal row weights by a physical repeated-setting Fisher sum.

## Model

The 24 NP3 calibration rows decompose into:

- trace normalization: 1;
- source mean energy: 1;
- gravitational potential means: 14;
- symmetrized covariance/noise settings: 8.

Trace and energy are treated as independent high-information constraints. The gravitational calibration Fisher is parameterized by two accumulated information strengths:

`F_C = F_trace+energy + gamma_m M_m + gamma_c M_c`.

The standardized shot-equivalent objective is

`14 gamma_m/q_m + 8 gamma_c/q_c`,

where `q_m,q_c` are per-shot Fisher informations.

Both D1 and D2 use the same source and NP3 operator set, and the detector-only beta Fisher is normalized to one. Target retained profiled information: 90%.

## Result A — D1

For equal per-shot mean/covariance information (`q_c/q_m=1`):

- uniform row weight threshold `~1.54e6`;
- uniform standardized cost `~3.38e7`;
- optimized `gamma_m~1.82e5`;
- optimized `gamma_c~3.49e5`;
- optimized cost `~5.35e6`;
- cost reduction `~6.3x`.

## Result B — D2

At `q_c/q_m=1`:

- uniform row weight threshold `~2.14e6`;
- uniform standardized cost `~4.72e7`;
- optimized `gamma_m~1.7e5`;
- optimized `gamma_c~1.0e6`;
- optimized cost `~1.03e7`;
- cost reduction `~4.6x`.

D2 allocates substantially more information to covariance calibration than D1.

## Result C — per-shot covariance efficiency

Representative allocation scan:

- D1 `q_c/q_m=0.1`: cost `~2.71e7`, gain vs uniform `~5.3x`;
- D1 `q_c/q_m=10`: cost `~2.04e6`, gain `~11.2x`;
- D2 `q_c/q_m=0.1`: cost `~7.97e7`, gain `~2.5x`;
- D2 `q_c/q_m=10`: cost `~3.14e6`, gain `~10.1x`.

The optimum therefore depends strongly on both detector branch and measurement-class efficiency.

## New retained rule

**RQIR-CAL-005 — heterogeneous calibration allocation principle.** At fixed likelihood and calibration operator set, resource-optimal calibration allocates information according to downstream nuisance-projection leverage and per-shot information cost. Equal precision on all calibration observables is generally not resource-optimal.

Scope: finite-dimensional numerical design result, not universal theorem.

## Negative result

No detector-independent optimal calibration schedule exists even for the same Toy009 source and same NP3 operator set. D1 and D2 demand materially different mean/covariance allocations.

## Files

- `analysis/heterogeneous_calibration_allocation_iteration013.py`
- `docs/HETEROGENEOUS_CALIBRATION_FISHER_ALLOCATION.md`

## Next gate

Add correlated/common-mode calibration drift and slow source/detector gain/position nuisances. Test whether the multi-fold allocation gains survive correlated covariance. Only after this should standardized `q_m,q_c` be converted to branch-specific seconds using D1 phase-shot noise/control loss and D2 PSD/transfer laws.
