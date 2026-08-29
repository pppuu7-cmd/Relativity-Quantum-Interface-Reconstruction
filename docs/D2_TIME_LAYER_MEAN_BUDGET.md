# RQIR Iteration 042 — D2 Time-Layer Mean Calibration Budget

**Date:** 2026-08-29  
**Scope:** centered D2 mean calibration at the balanced Toy009/Iteration-011 geometry.  
**Status:** backaction-safe scheduling/resource baseline; no apparatus forecast and no new-physics claim.

## 1. Motivation

Iteration 041 showed that the 14 force-mean observables cannot be treated as one disturbance-free multitime measurement. The only commuting pairs are the two probes evaluated at the same phase setting.

A conservative strong-measurement baseline is therefore:

- seven independent source-preparation/time layers;
- at each layer, measure the two same-time probe-force means jointly if the hardware supports parallel dual-probe readout;
- do not reuse one quantum source copy across different phase settings unless an explicit weak/backaction model is supplied.

This gives a physical scheduling interpretation of the current centered `gamma_mean`.

## 2. Per-layer repetition law

Let `xi_mu^2` be the single accepted cycle Fisher information for one row-normalized force-mean coordinate.

The current centered D2 mean target is

`gamma_mean ~= 1.830265e6`.

Each time layer therefore needs

`N_layer = gamma_mean / xi_mu^2`

accepted cycles.

With simultaneous same-time two-probe readout, the full seven-layer campaign needs

`N_acc,total = 7 gamma_mean / xi_mu^2`.

If the two probes must instead be measured in separate campaigns, the count doubles to

`14 gamma_mean / xi_mu^2`.

### RQIR-CAL-015 — same-time dual-probe pairing

> The current force operators permit a clean two-probe parallelization at each phase because `G0(t_j)` and `G1(t_j)` commute. This is the maximal disturbance-free grouping of the 14 mean rows in Toy009: different phase layers remain incompatible without an explicit weak/backaction model.

This is an architecture statement for the present model, not a general gravity theorem.

## 3. Coherence-aware wall time

For dimensionless phase `tau_j` and source gap frequency `f_gap`, the minimum evolution/coherence time of layer `j` is

`t_j = tau_j / (2 pi f_gap)`.

The seven current phases are

`(0, 3.09855988, 3.45849306, 2.93830159, 4.13016958, 4.84480925, 4.99085067)`.

At `100 Hz`:

- sum of the seven evolution times: `0.0373396341 s`;
- largest single-layer coherence time: `0.00794318794 s`.

For parallel two-probe readout, acceptance `p` and per-layer dead/readout time `d`, the lower-bound mean campaign time is

`T_mean = gamma_mean/(xi_mu^2 p) * sum_j (t_j+d)`.

For sequential probes, multiply by two.

### RQIR-RESOURCE-017 — phase-layer coherence accounting

> When phase settings use independent preparations, each layer pays only its own required evolution/coherence time. A seven-layer calibration budget must therefore use `sum_j t_j`, not seven times the largest coherence time. Conversely, one must not count multiple noncommuting phase settings as one disturbance-free source copy.

This separates two common resource-accounting errors in opposite directions.

## 4. Numerical lower bounds at 100 Hz

### Ideal acceptance `p=1`, zero dead/readout time

For `xi_mu=1`:

- parallel dual-probe campaign: `18.9837 h`;
- sequential two-probe campaign: `37.9675 h`.

The Iteration-040 best-four covariance graph floor under the same zero-overhead convention is

`2.60416 h`.

Therefore mean calibration is no slower than the covariance floor only if

- parallel dual-probe: `xi_mu >= 2.69996`;
- sequential probes: `xi_mu >= 3.81832`.

## 5. Transparent `p=0.5`, `1 ms` dead/readout benchmark

Using the same acceptance/dead-time benchmark retained in earlier resource work:

best-four covariance floor:

`T_cov,min ~= 5.86402 h`.

Parallel dual-probe mean campaign:

| `xi_mu` | accepted time-layer cycles | wall time |
|---:|---:|---:|
| 1 | `1.28119e7` | `45.0852 h` |
| 2 | `3.20296e6` | `11.2713 h` |
| 3 | `1.42354e6` | `5.00946 h` |
| 5 | `5.12474e5` | `1.80341 h` |
| 10 | `1.28119e5` | `0.450852 h` |

The crossover where the mean layer becomes no slower than the covariance floor is

`xi_mu ~= 2.77280`

for parallel dual-probe readout, or

`xi_mu ~= 3.92134`

for sequential probes.

Thus the joint-trajectory idea from Iteration 040 does **not** require a fantastically large mean sensitivity in principle: a per-accepted-cycle standardized row sensitivity of order `2.8` would make the centered mean layer comparable to the already-required best-four covariance campaign in this transparent benchmark.

## 6. What `xi_mu` means physically

`xi_mu` is not detector SNR for `beta`. It is the standardized sensitivity of one physical calibration cycle to a row-normalized source mean coordinate:

`xi_mu = |d mu / d u| / sigma_output`

in the local Gaussian single-cycle representation.

For a stationary white-force template one can ultimately obtain it from the detector-level expression

`I_u = 4 int |d h(f)/d u|^2 / S_F(f) df`,

but the current phase-layer schedule by itself does not specify the readout integration window or SI transduction Jacobian. Therefore `xi_mu~2.8` is a **target for the next apparatus model**, not a claim that current hardware achieves it.

## 7. Resource interpretation

The result narrows the physical design problem:

- covariance-only completion is expensive because of graph congestion;
- mean calibration, if done as seven independent strong-measurement layers, is also substantial but its target standardized sensitivity is moderate;
- same-time two-probe parallelization can halve the mean campaign cost without violating operator compatibility;
- the remaining opportunity is to design one physical detector record that reaches roughly `xi_mu>=2.8` per accepted layer while also producing the required covariance information **without excessive backaction**.

The latter condition cannot be checked in the present scheduling model.

## 8. Reproducibility

Code:

`analysis/d2_time_layer_mean_budget_iteration042.py`

The script computes per-layer repetition counts, coherence-aware wall time, parallel/sequential probe bounds and the mean-vs-best4 covariance crossover.

## 9. Next gate

Construct a minimal continuous weak-measurement / detector-output model with an explicit information-backaction parameter. It must answer:

1. can the same D2 coupling achieve per-layer mean sensitivity `xi_mu~2.8` or better at the 100-Hz benchmark;
2. can it simultaneously approach the best-four covariance Fisher ceiling;
3. how much does the required measurement strength perturb the hidden-state ordered-response signal and the nuisance geometry;
4. does profiling detector backaction reopen the `beta`/source degeneracy?
