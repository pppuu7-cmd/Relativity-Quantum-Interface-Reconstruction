# RQIR Iteration 073 — Physical Local-Source Pareto / Lower-Envelope Audit

**Date:** 2026-08-30  
**Status:** architecture-selection geometry using retained physical resource ratios; not an apparatus forecast and not a new-physics claim.

## 1. Motivation

Iteration 072 removed balanced Toy012 from the physical D2 Pareto front in the shared-kernel reference class. The next question is different:

**If exact nearest-neighbour locality is mandatory, which of the remaining local source designs should be used as the physical baseline?**

A single raw-response or calibration number cannot answer this. The relevant retained axes are

1. physical spectral-tilt-profiled D2 science time;
2. physical spectral-tilt-profiled calibration time;
3. independent Ramsey source-metrology time.

For each source define factors relative to Toy009:

`q_s`, `q_c`, `q_p`.

Use the projected weighted wall-clock plane

`L_i(x,y)=q_s,i + q_c,i x + q_p,i y`,

where `x,y>=0` are reference weights for calibration and source-metrology cost relative to science. In a locality-only comparison they are simply resource weights; Toy009 need not itself be an admissible source.

## 2. Retained physical local-source vectors

Using the physical two-band source information from the local-source searches, the Iteration-063 spectral-tilt-profiled calibration scan, and the declared zero-reset Ramsey source-metrology class:

| source | `q_s` science time | `q_c` calibration | `q_p` Ramsey source time |
|---|---:|---:|---:|
| Toy011 response | `~6.418` | `~21.7` | `~3.759` |
| Toy011 conditioning | `~12.250` | `~8.83` | `~2.384` |
| Toy012 high-response | `~8237.33` | `~5.2e2` | `~0.8692` |
| Toy013 trial 29100 | `23.6496` | `0.123301` | `330.907` |

The Toy011/Toy012 calibration factors are finite-scan central values from Iteration 063, so the final digits of crossover coordinates are not promoted to physical constants.

## 3. Unrestricted vs locality-constrained architecture

If Toy009 is allowed, both Toy011 points are componentwise dominated by Toy009:

- larger science time;
- larger physical calibration burden;
- slower Ramsey source metrology.

Toy012-high is not componentwise dominated because its Ramsey source-metrology rate is about 15% faster than Toy009. Toy013 is not dominated because its physical calibration burden is only about 0.1233 of Toy009.

Thus the unrestricted physical Pareto set contains Toy009 plus conditional specialization branches Toy012-high and Toy013.

However, this is not the right comparison if the source Hamiltonian is required to be exactly nearest-neighbour local. Toy009 is then excluded by the Iteration-053 locality audit.

## 4. All four retained local branches are supported lower-envelope points

Using the central physical-resource vectors, every remaining local source wins the weighted objective in some nonnegative `(x,y)` region.

Robust witness points:

- `(x,y)=(0,0)` → **Toy011 response** wins: science time dominates the objective;
- `(0.7,0)` → **Toy011 conditioning** wins: moderate calibration pressure rewards its better nuisance geometry;
- `(2,0)` → **Toy013** wins: calibration dominates strongly enough to justify its weaker science signal;
- `(0,6000)` → **Toy012 high-response** wins: an extreme source-metrology-dominated regime rewards its Ramsey advantage.

Therefore no one of these four local designs can be removed by ordinary weighted-sum Pareto pruning using the current three axes.

### RQIR-DESIGN-008 — locality-constrained Pareto plurality

> After physical detector profiling, a locality-constrained source family can contain several genuinely supported resource-specialized architectures. Promoting a single local source as “the baseline” is unjustified until the experiment supplies the relative science/calibration/source-metrology rate weights.

This is the physically corrected version of the earlier “locality creates a tradeoff” lesson: the tradeoff persists even after the Euclidean detector-metric error is removed.

## 5. Central reference crossover geometry

With the Iteration-063 central calibration values, along `y=0` the lower envelope changes approximately as

`Toy011-response -> Toy011-conditioning -> Toy013`

at

- `x ~0.453`;
- `x ~1.309`.

Along `x=0` it changes approximately as

`Toy011-response -> Toy011-conditioning -> Toy012-high`

at

- `y ~4.24`;
- `y ~5.43e3`.

These coordinates are **reference geometry**, not apparatus predictions. The exact boundaries move when source-specific transfer functions, cross spectra, reset/visibility, control costs or a different source-metrology protocol are inserted, as required by NG-029.

## 6. Scientific interpretation

The local-source program now has three distinct specialization directions:

- **Toy011 response:** minimize science exposure among current local retained points;
- **Toy011 conditioning:** compromise between science, calibration and source metrology;
- **Toy013:** minimize physical spectral-tilt-profiled calibration burden;
- **Toy012 high:** minimize the current Ramsey source-metrology time, but only at enormous science/calibration cost.

This suggests that the next source search should not optimize one scalar resource. It should attempt to **collapse the Pareto spread** by co-designing a source that preserves the healthy Toy011 two-band science signal while approaching Toy013 calibration efficiency and retaining a non-pathological energy/Ramsey metrology channel.

## 7. Next gate — Toy014 multi-resource co-design

Construct a new exact nearest-neighbour search with a physical multi-objective/minimax score. The cheap stage should require

- exact NP3/locality/state gates;
- noncollapsed `n=2` and `n=4` bands;
- physical `S_eff,D2` floor;
- source-metrology accessibility floor (energy population or Ramsey proxy).

The expensive stage should include Iteration-063 spectral-tilt-profiled calibration Fisher.

A useful first target is not “beat Toy009 everywhere,” which may be too strong, but find a local candidate that Pareto-dominates at least one of Toy011-response / Toy011-conditioning while keeping

- science factor `q_s` of order `<=10`;
- calibration factor substantially below the current Toy011 values;
- Ramsey source-time factor of order unity rather than hundreds.

No winner should be recorded until the deterministic search is executed.

## 8. Reproducibility

Code:

`analysis/local_source_physical_pareto_iteration073.py`

It verifies unrestricted componentwise dominance statements, local-only lower-envelope witness points, and the central axis crossover geometry.
