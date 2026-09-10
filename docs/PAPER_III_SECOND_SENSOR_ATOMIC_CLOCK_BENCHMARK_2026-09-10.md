# Paper III — second-sensor transfer benchmark: atomic clock

**Date:** 2026-09-10  
**Purpose:** QST submission hardening / cross-architecture transfer test  
**Status:** controlled benchmark extension outside frozen RQIR Core v1.0  
**Claim boundary:** reduced design-principle regression; **not** an apparatus-specific clock performance forecast.

## Why this benchmark exists

Paper III states a nuisance-profiled resource/design criterion in the form

\[
I_\beta(e;\Lambda)=\min_a\left[\sum_k e_k\|s_k-J_k a\|^2+a^\top\Lambda a\right].
\]

The atom-gravimeter chain demonstrates the criterion in detail for one sensing architecture.  This benchmark asks a narrower but editorially important question: **does the same criterion, with the same RQIR nuisance-profiling implementation and no change to the scientific decision rule, produce the expected design logic for a physically different quantum sensor?**

The answer is **yes** for the reduced atomic-clock example below.

## Frozen-core reuse

The new adapter `analysis/paper3_profiled_resource_law.py` does not implement a second nuisance minimizer.  It converts `(e,s,J,Lambda)` into the corresponding Fisher block matrix and delegates profiling to the pre-existing

`analysis/protocol002_profiled_fisher.py::profiled_beta_information`.

The sensor-specific benchmark is

`analysis/paper3_atomic_clock_second_sensor_benchmark.py`.

The checked-in machine-readable result is

`results/paper3_atomic_clock_second_sensor.json`.

Thus the architecture changes, while the nuisance-profiled decision machinery does not.

## Reduced clock architecture

We use four interleaved Ramsey/clock interrogation-control settings at normalized cycle times

\[
t=(-3/2,-1/2,+1/2,+3/2).
\]

The shared nuisance vector contains a local-oscillator frequency offset and linear drift, giving

\[
J_k=(1,t_k).
\]

This is intentionally a reduced benchmark.  Optical clocks are frequency sensors whose operation and systematic evaluation depend on interrogation/control sequences, local oscillators, references and repeated/interleaved comparisons.  Interleaved clock operation is routinely used to compare configurations or evaluate systematic shifts; the benchmark abstracts that design geometry rather than modelling a particular clock's instability or uncertainty budget.

Representative background references:

- A. D. Ludlow et al., *Optical atomic clocks*, Rev. Mod. Phys. **87**, 637 (2015), doi:10.1103/RevModPhys.87.637.
- T. Lindvall et al., *Measurement of the Differential Static Scalar Polarizability of the 88Sr+ Clock Transition*, Phys. Rev. Lett. **135**, 043402 (2025), doi:10.1103/52by-28mr; this work explicitly uses a single-clock interleaved scheme with switched operating conditions.

## Four transfer facts

### 1. Nuisance-induced failure

For an unmodulated clock response

\[
s=(1,1,1,1),\qquad \Lambda=0,
\]

the science direction is exactly collinear with the free LO-offset nuisance.  The common Paper-III resource law returns

\[
I_\beta=0.
\]

More exposure to the same setting cannot repair a missing score direction.

### 2. Recovery by response diversity

Use the signed control-reversal pattern

\[
s=(1,-1,-1,1)
\]

with uniform allocation

\[
e=(1/4,1/4,1/4,1/4).
\]

The weighted science score is orthogonal to both nuisance columns,

\[
J^\top\operatorname{diag}(e)s=0,
\]

and the same resource law gives

\[
I_\beta=1.
\]

The value is normalized; the result of interest is the restoration of full normalized information after nuisance profiling.

### 3. Recovery by finite calibration

Return to the unmodulated response and supply independent LO-offset calibration only,

\[
\Lambda=\operatorname{diag}(\lambda,0).
\]

The common profiler gives

\[
I_\beta=\frac{\lambda}{1+\lambda}.
\]

The regression records

- `lambda = 1` -> `I_beta = 0.5`;
- `lambda = 9` -> `I_beta = 0.9`.

Thus a nuisance-induced failure can be repaired by an explicit calibration resource rather than hidden by assuming the nuisance known.

### 4. Allocation matters

For the same response-diverse pattern, replacing uniform exposure by

\[
e=(0.4,0.3,0.2,0.1)
\]

reduces the profiled information from `1.0` to `0.84`.  Therefore the criterion is not merely a rank test: resource allocation and nuisance geometry jointly determine the retained information.

## Reviewer-facing interpretation

This benchmark supplies the four ingredients needed for a minimal second sensing example:

| Requirement | Atomic-clock benchmark |
|---|---|
| Different quantum sensor | interleaved Ramsey/atomic-clock frequency sensing |
| Different nuisance model | shared LO frequency offset + linear drift |
| Explicit nuisance failure | unmodulated response gives `I_beta = 0` |
| Design/calibration recovery | control reversal gives `1.0`; finite calibration gives `0.5` or `0.9` |
| Allocation dependence | asymmetric allocation gives `0.84` |
| Same RQIR profiler | existing `profiled_beta_information` reused unchanged |

The legitimate manuscript conclusion is therefore **cross-architecture transfer of the design criterion**, not a claim that a specific clock apparatus has achieved the benchmark values.

## Manuscript-ready insertion

A compact second example can be described as follows:

> To test whether the criterion is specific to atom gravimetry, we applied the same nuisance-profiled resource law to a reduced interleaved atomic-clock frequency-sensing architecture.  With shared local-oscillator offset and linear drift as nuisance directions, an unmodulated science response is non-identifiable (`I_beta=0`).  A four-setting signed control sequence that is orthogonal to both nuisance scores restores the full normalized information (`I_beta=1`), while finite independent offset calibration yields the expected continuous recovery (`I_beta=lambda/(1+lambda)`).  An asymmetric resource allocation reduces the retained information to `0.84`.  No change to the RQIR profiling rule is made between the gravimeter and clock examples; only the sensor response and nuisance Jacobian change.

This paragraph should be adapted to the manuscript's final notation and equation numbering rather than pasted blindly.

## Reproduction

Run:

```bash
python analysis/paper3_profiled_resource_law.py
python analysis/paper3_atomic_clock_second_sensor_benchmark.py --check-result
```

Expected gates:

- independent sensor architecture: PASS;
- same profiled resource law: PASS;
- nuisance-induced failure: PASS;
- response-diversity recovery: PASS;
- calibration recovery: PASS;
- allocation sensitivity: PASS;
- frozen core decision rules modified: **false**.

## QST scope effect

This extension directly strengthens the QST-facing claim that Paper III is a reusable quantum-sensing experimental-design criterion rather than a construction tied only to Raman atom gravimetry.  It supports the existing QST hardening gates for concrete architecture, reviewer-style reproducibility and scope alignment.  It does **not**, by itself, promote the entire QST submission package to 100%, because figures/tables, final prose/formatting and the other submission-gate items remain separately controlled.
