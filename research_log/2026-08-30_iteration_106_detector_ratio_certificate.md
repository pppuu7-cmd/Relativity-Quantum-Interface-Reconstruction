# RQIR Research Log — Iteration 106

**Date:** 2026-08-30

## Goal

Continue from authoritative Iteration 105 and attack the highest-value missing quantity

`u=R_D,14/R_D,09`

without inventing an absolute apparatus ASD. Preserve the full profiled Fisher geometry and the Iteration-103/104 campaign scheduler.

## Source-of-truth audit

Re-read:

- `docs/RECOVERY_GUIDE.md`;
- `docs/MASTER_TABLE.md`;
- `recovery/CURRENT_FRONT.md` (Iteration 105);
- latest research log (Iteration 105);
- Toy009 detector-aware source document;
- Toy010 calibration-geometry co-optimization;
- `STATISTICAL_IDENTIFIABILITY.md`;
- `STATISTICAL_IDENTIFIABILITY_002_NOISY_PREPARATION_CALIBRATION.md`.

The audit confirms that scalar response or conditioning ratios are not enough: the missing architecture comparison must preserve nuisance orientation in the common physical Fisher coordinate.

## New result — RESOURCE-062

For campaign Fisher-rate matrices in common `(beta,theta)` coordinates, define

`Phi(J)=F_beta|theta`.

Using

`Phi(J)=min_q (1,-q)^T J (1,-q)`, 

`Phi` is Loewner-monotone and positively homogeneous.

Therefore, if uniformly over campaigns and apparatus uncertainty

`alpha J_09,k <= J_14,k <= beta J_09,k`,

and both architectures share the same feasible schedule set, then the optimized detector-side rates satisfy

`alpha <= R_D,14/R_D,09 <= beta`.

For positive-definite reference matrices the tight per-campaign constants are generalized eigenvalue extrema of `J09^-1/2 J14 J09^-1/2`.

## New guardrail — NG-061

Standalone science SNR ratios, gamma ratios, calibration-cost ratios or transfer-error ratios do not certify `u`. The matrix score orientation and feasible schedule matter. Singular-support mismatch or architecture-specific recertification constraints must be audited explicitly.

## New detector threshold / no-rescue result

From Iteration 105,

`G=Q14/Q09=delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

For fixed `(v,z,delta)`, Toy014 requires

`u > [sqrt(delta)(1+z^-1/2)-(v z)^-1/2]^-2`

when the denominator bracket is positive.

If

`delta v (1+sqrt(z))^2 <= 1`,

then even `u -> infinity` cannot make Toy014 faster. Registered as **NG-062**.

Using the retained finite Ramsey-box source-rate ratio `v=1.39` only as a regression slice and equal duty, required detector ratios are:

- z=.01 -> u>0.1577067791;
- z=.03 -> u>0.2839954413;
- z=.10 -> u>0.4564952030;
- z=1 -> u>0.7537676652.

These are engineering threshold surfaces, not apparatus predictions.

## Robust box closure — RESOURCE-063

For independent positive intervals in `(u,v,z,delta)`, monotonicity gives exact lower/upper final-rate-ratio endpoints. `u,v,delta` take their corresponding lower/upper endpoints; the active `z` endpoint is selected by the sign of `v-u`.

Thus:

- lower `G>1` certifies Toy014 under NG-030;
- upper `G<1` certifies Toy009;
- otherwise the branch remains unresolved.

Correlated apparatus uncertainties require the actual joint set rather than independent-box assembly.

## Numerical regression

Synthetic two-campaign positive-definite matrices give generalized-eigenvalue bounds

`alpha=0.55`, `beta=1.40`.

Direct campaign-simplex optimization gives

`u=0.6172845158`,

inside the certified interval.

The code also reproduces the Iteration-105 crossover exactly and verifies RESOURCE-063 against Cartesian corners.

## Files

- `analysis/detector_ratio_certificate_iteration106.py`
- `docs/PAPER_III_DETECTOR_RATIO_CERTIFICATE_ITERATION106.md`
- `recovery/RECOVERY_DELTA_ITERATION_106.md`

## Next gate

Include mandatory timing/geometry/additive/gain recertification as **schedule constraints**, because Toy009 and Toy014 can have different control cadence/duty. Derive how minimum campaign fractions and periodic recertification modify the detector-side optimized rate and the RESOURCE-062 ratio bound. Then combine the resulting robust `u` interval with robust `v,z,delta` under RESOURCE-063/NG-030.

Do not start Toy015 unless the remaining active marginal cost is demonstrably source-dependent.
