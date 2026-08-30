# RQIR Iteration 080 — Paper III Apparatus Specification Envelope

**Date:** 2026-08-30  
**Status:** physical rate-space closure step; not an apparatus forecast and not a new-physics claim.

## 1. Question

Iteration 077 identified the minimal measured apparatus certificate `(R_beta,x,y,d)`, but the next Paper-III need is the inverse question:

> Given a declared wall-clock cap, what minimum measured Fisher rates would an apparatus have to achieve, without inventing an absolute ASD?

This iteration answers that question in rate space.

## 2. Starting point

For one architecture,

`T_total = m [ Z^2/R_beta + gamma_mean sum_j 1/R_cal,j + C_prep/R_src ]`,

where

`m=1/(1-d)`,

`R_beta` is the nuisance-profiled science Fisher rate, the seven `R_cal,j` are the independently acquired same-time dual-probe matrix calibration Fisher rates, and `R_src` is independent source-metrology Fisher rate including preparation/reset/readout/acceptance/visibility.

At the retained `Z=5`, source-amplitude information-retention target `r=0.90`,

`C_prep=225`.

## 3. RQIR-RESOURCE-037 — harmonic calibration-rate compression

Define the harmonic mean of the seven calibration Fisher rates,

`H_cal = 7 / sum_j (1/R_cal,j)`.

Then the exact wall clock becomes

`boxed{T_total = m [ Z^2/R_beta + 7 gamma_mean/H_cal + C_prep/R_src ]}`.

The harmonic mean, not the arithmetic mean, is the correct one-number calibration throughput because slow independent layers dominate total calibration time.

This compression is exact only for the current scheduling model in which the seven layers pay independent acquisition time. Shared likelihoods must instead be treated with their full matrix Fisher as required by RESOURCE-016.

## 4. Necessary componentwise floors

For a target cap `T_cap`, each positive component must individually satisfy

`R_beta >= m Z^2/T_cap`,

`H_cal >= m 7 gamma_mean/T_cap`,

`R_src >= m C_prep/T_cap`.

These are useful impossibility tests. If any one fails, the architecture cannot meet the cap even if the other two resources were free.

## 5. RQIR-NG-031 — individual floors are not jointly sufficient

Meeting all three componentwise floors simultaneously is **not** enough. If all three are exactly at their individual floors, each consumes the whole allowed wall clock and

`T_total = 3 T_cap`.

Thus an apparatus specification must allocate the total time budget, rather than quote three unrelated subsystem minima.

## 6. Sufficient allocated specification

Choose positive budget fractions

`f_sci + f_cal + f_src = 1`.

A sufficient rate specification is

`boxed{R_beta >= m Z^2/(f_sci T_cap)}`,

`boxed{H_cal >= m 7 gamma_mean/(f_cal T_cap)}`,

`boxed{R_src >= m C_prep/(f_src T_cap)}`.

At equality the three payload terms exactly sum to the target cap. The fractions are experiment-design choices, not physical constants.

This turns Paper III's conclusion into a measurable engineering target: report rates, not an arbitrary guessed ASD.

## 7. Transparent equal-third examples

The following table uses `d=0` and `f_sci=f_cal=f_src=1/3`. These are **requirements under an allocation**, not predictions of a real apparatus.

### Common science/source requirements

| cap | `R_beta` minimum [Fisher/s] | `R_src` minimum [Fisher/s] |
|---:|---:|---:|
| 1 day | `8.68056e-4` | `7.81250e-3` |
| 7 days | `1.24008e-4` | `1.11607e-3` |
| 30 days | `2.89352e-5` | `2.60417e-4` |

### Harmonic-mean calibration requirement

Using retained centered D2 `gamma_mean` values:

- Toy009: `gamma_mean=1.830264703e6`;
- Toy014: `gamma_mean=5.6776851e6`.

| cap | `H_cal` Toy009 [Fisher/s] | `H_cal` Toy014 [Fisher/s] |
|---:|---:|---:|
| 1 day | `444.8560` | `1379.9929` |
| 7 days | `63.55086` | `197.14184` |
| 30 days | `14.82853` | `45.99976` |

These numbers are in the declared normalized calibration-parameter coordinate. They are **not** raw shot rates, detector Hz, or equivalent-force ASD.

The Toy014 calibration requirement is higher because its retained `gamma_mean` is larger. Whether Toy014 still wins overall depends on its physical science and source-metrology rates and control duty, exactly as in Iteration 077.

## 8. Control/coherence feasibility must be checked before rate closure

The rate envelope is necessary only after basic scheduling feasibility is satisfied.

At the retained 100-Hz benchmark:

- Toy009 evolution/coherence floor is about `7.94319 ms` and D2 timing target about `9.19001 us`;
- Toy014 evolution/coherence floor is about `6.81327 ms` and timing target about `3.97715 us`.

A declared apparatus must show that its acquisition windows, recertification cadence and stability floor are compatible with those source-specific requirements. Existing NG-007 remains active: a stability floor above target cannot be repaired by increasing white-noise averaging.

## 9. What is now closed and what remains open for Paper III

Closed:

- conversion of the abstract calibration burden into a measured-rate envelope;
- exact compression of seven independent calibration-layer rates into `H_cal` for wall-clock accounting;
- necessary versus sufficient wall-clock specifications;
- a direct route from a desired experiment duration to minimum measurable Fisher-rate targets.

Still open:

1. instantiate `R_beta`, all seven `R_cal,j`, `R_src`, and `d` from one repository-backed detector/source-metrology apparatus model for Toy009 and Toy014;
2. attach real transfer functions and PSD/cross-PSD or experimentally declared sensitivity curves rather than guessed ASD values;
3. propagate rate uncertainties and require NG-030 robust dominance;
4. decide whether the actual bottleneck is detector, calibration, source preparation or controls.

Therefore Paper III advances materially but is not scientifically closed.

## 10. Reproducibility

Run

`python analysis/apparatus_specification_envelope_iteration080.py`.

The script verifies the harmonic-mean identity, the exact allocated-cap closure, the NG-031 `3*T_cap` counterexample, and the 1/7/30-day rate tables.
