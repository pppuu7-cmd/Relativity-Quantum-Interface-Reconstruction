# RQIR Iteration 062 — Toy012 Profiled Two-Band Metric Audit

**Date:** 2026-08-30  
**Status:** mandatory numerical/design correction; no hardware or new-physics claim.

## 1. Why the science-rate calculation had to stop

Toy012 Iteration 055 reported the balanced local candidate as retaining

`~0.21617`

of Toy009 D2 detector information and therefore suggested a same-noise science-time penalty of only `~4.63x`.

That number is correct for the **Euclidean squared norm of the four real harmonic detector components** used by the normalized nuisance-geometry code:

`|G2|^2 + |G4|^2`.

It is **not** the physical D2 Fisher metric already adopted in Iteration 019 when a relative spectral-tilt nuisance is profiled.

For equal equivalent-force ASD in the two bands, Iteration 019 uses

`S_eff = 4 |G2|^2 |G4|^2 / (|G2|^2 + |G4|^2)`.

This metric requires both harmonics to carry information.

## 2. Balanced Toy012 has collapsed the n=4 science band

For the balanced Toy012 source,

`G2 ~= 0.00893149 + 0.00678180 i`,

while

`G4 ~= -1.1683e-6 + 1.2169e-6 i`.

The amplitude ratio is only

`|G4|/|G2| ~= 1.5043e-4`.

Thus the earlier Euclidean norm is dominated almost entirely by the n=2 band.

The physical equal-ASD spectral-profiled source factor is

`S_eff,Toy012 / S_eff,Toy009 ~= 1.96963e-8`.

So the corresponding same-apparatus science-time ratio would be

`~5.077e7`,

not `4.63`.

Equivalently, to balance the two band Fisher contributions purely by detector noise would require approximately

`ASD_4 / ASD_2 ~= 1.50e-4`,

or an n=4 equivalent-force ASD roughly **6600 times lower** than n=2. No such detector asymmetry has been established.

## 3. The high-response Toy012 point has the same qualitative problem

The retained aggressive local candidate had Euclidean D2 norm ratio

`~0.30469`.

But its physical equal-ASD profiled ratio is only

`~1.214e-4`,

corresponding to a science-time penalty of about

`8.24e3`.

It would require roughly a factor `100` ASD advantage in the n=4 band to equalize the two band contributions.

So neither current Toy012 Pareto point is acceptable as a physical two-band D2 source design.

## 4. D1 is affected too

The same mismatch appears in the D1 four-switch metric. After re-optimizing the switch parameter separately for each source:

- balanced Toy012 physical two-band D1 ratio is only `~5.81e-8` of Toy009;
- high-response point is only `~2.94e-6`.

Again, the local redesign concentrated detector norm into one harmonic instead of preserving the two-band fingerprint.

## 5. RQIR-NUM-003 — detector norm is not a profiled Fisher metric

> A Euclidean norm of detector response components may be used as a local normalization only when it matches the declared detector covariance and nuisance model. It cannot be interpreted as physical detector Fisher after profiling a spectral-shape nuisance. Source design must optimize the same profiled metric that will be used for wall-clock conversion.

The earlier inference

`Toy012 D2 science penalty ~= 4.63x`

is therefore **withdrawn**.

This is a metric/normalization correction, not a failure of the exact local-source construction.

## 6. What remains valid from Toy012

The following Toy012 results remain valid:

- exact nearest-neighbour source Hamiltonian;
- exact spectrum `(1,2,3,4,6)`;
- rank `24/25` NP3 calibration geometry;
- positive hidden states;
- exact selected mean/noise equality and nonzero ordered response;
- the normalized calibration/nullspace calculations as abstract Fisher-geometry diagnostics;
- source QFI and energy/Ramsey source-metrology calculations for the declared hidden direction;
- Iterations 059–061 as auxiliary-resource studies **conditional on the normalized detector metric**.

What is no longer justified is combining those auxiliary numbers with `0.21617` as though it were the physical D2 science rate.

## 7. RQIR-DESIGN-005 — physical detector likelihood belongs inside source co-design

The locality redesign must now optimize at least

`(locality, calibration conditioning, profiled D1/D2 detector Fisher, source metrology)`

rather than

`(locality, calibration conditioning, detector-vector norm)`.

This is stronger than DESIGN-003: the detector objective itself must already contain the physical band noise and detector nuisance profiling relevant to the intended experiment.

## 8. Scientific consequence

The encouraging Toy012 result — that exact locality can coexist with near-Toy009 **calibration** efficiency — survives.

But the present Toy012 candidate is not the right physical-source baseline because it achieves that calibration efficiency by rotating the ordered-response signal almost entirely into one harmonic. The next search must enforce a two-band information floor or optimize the full profiled D2 rate directly.

This also explains why Toy011 response-oriented points, which were selected using the two-band `S_eff` proxy, retained much healthier physical D2 balance despite worse calibration cost.

## 9. Reproducibility

Code:

`analysis/toy012_profiled_two_band_metric_audit_iteration062.py`

Regression checks compare

- Euclidean norm-power ratios;
- physical equal-ASD D2 `S_eff`;
- source-optimized D1 four-switch Fisher;
- required band-ASD imbalance.

## 10. Next gate — Toy013

Do **not** proceed to a nominal SI wall-clock using Toy012's `0.21617` number.

Instead construct a new locality-constrained source search whose objective contains the physical profiled two-band detector metric. A natural first version should require both `n=2` and `n=4` band powers to remain finite and score candidates using

`S_eff,D2`

plus centered calibration cost.

Then re-run the physical source-metrology and complementary-calibration pipeline only on the resulting Pareto candidates.
