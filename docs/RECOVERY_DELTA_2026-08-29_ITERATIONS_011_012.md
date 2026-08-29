# RQIR Recovery Delta — Iterations 011–012

**Date:** 2026-08-29  
**Applies after:** operational framework v0.9 / Toy 009

This delta exists so a continuation session can recover the newest frontier even if `RECOVERY_GUIDE.md` has not yet been compacted again.

## New accepted result: Toy 010

Files:

- `docs/TOY_MODEL_010_CALIBRATION_GEOMETRY_COOPTIMIZATION.md`
- `analysis/toy010_calibration_geometry_optimization.py`
- `research_log/2026-08-29_iteration_011_toy010_calibration_geometry.md`

Toy 009 source is held fixed. Only second calibration-probe position and five non-target calibration times change.

Accepted calibration:

- `y1 = -3.764531439702698`;
- times `(0, 2.99076642, 3.583928899215236, 2.86845279, 4.17773776, 4.88882082, 4.99774842)`.

Checks/results:

- exact rank `24/25`;
- equality residual `<2e-16`;
- positive null-pair density matrices;
- target mean/noise equality preserved;
- target response `D+ ~ +0.01328591`, `D- ~ -0.01328591`;
- `eta_R ~ 0.600174`;
- `s_min ~ 2.21101e-3`;
- condition `~2084.2`;
- D1 two-band information `~1.67881 x Toy009`, `~2.05123 x Toy007`;
- D2 `~1.58406 x Toy009`, `~2.22336 x Toy007`;
- null direction rotates about `37.7 deg` relative to inherited Toy 009 calibration.

Analytic result **RQIR-CAL-002**:

For smooth rank-`p-1` calibration `A(q)` and normalized null vector `n(q)`,

`n' = -A^+ A' n`,

so

`||n'|| <= ||A'|| / s_min(A)`.

Interpretation: calibration geometry actively steers the surviving null direction; poor conditioning amplifies fragility.

D1 four-switch Toy 010 window:

- optimum `a ~ 2.24169`;
- `|W2| ~ 0.49864`, `|W4| ~ 0.31000`;
- Fisher `~1.819 x` old Toy007 eight-switch bounded window;
- same illustrative physical benchmark becomes `m_s m_p ~6.01e-29 kg^2`, equal-mass `~7.75e-15 kg`.

## New identifiability gate: RQIR-NG-005 / CAL-003

Files:

- `docs/STATISTICAL_IDENTIFIABILITY_002_NOISY_PREPARATION_CALIBRATION.md`
- `analysis/toy010_noisy_calibration_fisher.py`
- `research_log/2026-08-29_iteration_012_noisy_preparation_calibration.md`

Let `a` be the actual prepared-source amplitude along exact gravitational null direction `n`, and `beta` the interface-response amplitude.

Detector signal is locally proportional to `beta a s`, while gravitational calibration obeys `A n=0`.

Therefore without independent source-preparation information,

`F_beta|a = 0`

for any precision of the gravitational calibration on orthogonal directions.

Named **RQIR-NG-005 — null-amplitude self-calibration obstruction**.

Independent nongravitational preparation Fisher `C_a` gives, with all other nuisances perfectly known and detector information normalized to one,

`F_beta = C_a/(1+C_a)`.

To retain 90% detector information requires `C_a/S=9`, i.e. preparation-amplitude SNR about `3 x` detector response SNR.

With all 24 orthogonal state nuisance directions included, Toy 010 row-normalized calibration has `s_min~2.211e-3`, crude scale `1/s_min^2~2.05e5`.

For effectively perfect source-amplitude calibration, numerical full-Fisher thresholds are roughly:

- 50% retention: `gamma~1.2e5`;
- 80%: `~5e5`;
- 90%: `~1.2e6`;
- 95%: `~2.5e6`.

`gamma` is abstract row-normalized information strength, not yet a physical SNR.

Named **RQIR-CAL-003 — dual source characterization**:

1. gravitational/null calibration constrains ordinary mean/noise nuisance directions;
2. nongravitational preparation calibration constrains amplitude/quantum coordinates intentionally hidden from the gravitational null set.

Both are required for local interface identifiability.

## Exact next target

Translate `gamma` and `C_a` into physical measurement budgets:

1. covariance/shot-noise model for mean-potential calibration rows;
2. covariance/sample-complexity model for symmetrized-noise rows;
3. concrete nongravitational source-preparation measurement;
4. repetition/integration-time budget relative to source coherence time;
5. recompute full D1 `F_beta|theta` with the physical covariance matrix rather than row-normalized isotropic `gamma`.
