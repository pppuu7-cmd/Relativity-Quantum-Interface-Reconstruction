# Paper III — second-sensor transfer benchmark: dual-transition atomic clock

**Date:** 2026-09-10  
**Purpose:** QST submission hardening / cross-architecture transfer test  
**Status:** controlled benchmark extension outside frozen RQIR Core v1.0  
**Claim boundary:** reduced design-principle regression; **not** an apparatus-specific clock performance or new-physics forecast.

## Why this benchmark exists

Paper III states the nuisance-profiled resource/design criterion

\[
I_\beta(e;\Lambda)=\min_a\left[\sum_k e_k\|s_k-J_k a\|^2+a^\top\Lambda a\right].
\]

The Raman atom-gravimeter chain tests that criterion in detail for one sensing architecture. This benchmark asks the narrower editorial question needed for a general quantum-sensing claim: **does the same frozen profiling rule produce the expected experimental-design logic for an independent frequency-sensing architecture when only `(s,J,Lambda,e)` are changed?**

The answer is yes for the reduced dual-transition atomic-clock example below.

## Frozen-core reuse

`analysis/paper3_profiled_resource_law.py` maps `(e,s,J,Lambda)` into the Fisher block matrix and delegates nuisance profiling to the pre-existing

`analysis/protocol002_profiled_fisher.py::profiled_beta_information`.

The sensor-specific benchmark is

`analysis/paper3_atomic_clock_second_sensor_benchmark.py`,

and its checked-in machine-readable result is

`results/paper3_atomic_clock_second_sensor.json`.

No second minimizer, sensor-specific profiling rule, or modified decision threshold is introduced.

## Reduced clock architecture

Consider two clock transitions/references, A and B, each interrogated at four normalized cycle times

\[
t=(-3/2,-1/2,+1/2,+3/2).
\]

Their illustrative normalized science sensitivities are

\[
q_A=+1,\qquad q_B=-0.6.
\]

These numerical values are **not atomic constants and are not attributed to a particular species**. They are normalized benchmark coefficients chosen only to make the required physical design fact explicit: two clock responses can have different sensitivity to the science parameter. Any nonzero contrast `q_A-q_B` produces the same qualitative result.

Both channels share a reference/local-oscillator offset and linear drift,

\[
J_k=(1,t_k),\qquad \Lambda=0
\]

unless an independent calibration resource is supplied. This is intentionally a reduced frequency-sensing geometry rather than an uncertainty budget for a named clock.

For background on atomic-clock interrogation, local-oscillator noise, comparisons and systematic evaluation, see A. D. Ludlow et al., *Optical atomic clocks*, Rev. Mod. Phys. **87**, 637 (2015), doi:10.1103/RevModPhys.87.637.

## Four transfer facts

### 1. Single-transition nuisance failure

Allocate all unit resource to A, uniformly across its four times. Its science response is constant over those settings,

\[
s_A=q_A(1,1,1,1),
\]

and is therefore collinear with the free common-offset nuisance. The common Paper-III law returns

\[
I_\beta(f_A=1)=0.
\]

The same happens with B alone,

\[
I_\beta(f_A=0)=0.
\]

Thus simply adding exposure to one response channel cannot repair a missing score direction.

### 2. Recovery by genuinely different clock responses

Let a fraction `f_A` of the resource interrogate A and `1-f_A` interrogate B, with balanced time sampling inside each transition. Because `q_A != q_B`, the science vector is no longer globally proportional to the shared offset nuisance when both transitions are used.

For this reduced geometry the zero-prior profile information is

\[
I_\beta(f_A)=f_A(1-f_A)(q_A-q_B)^2.
\]

With `q_A-q_B=1.6`,

\[
I_\beta(f_A)=2.56 f_A(1-f_A).
\]

The recovery is therefore caused by **cross-transition response diversity**, not by a hand-chosen sign pattern in a single response channel.

### 3. Allocation is optimized, not assumed

The benchmark scans 101 allocations from `f_A=0` to `1`. It recovers

\[
f_A^*=f_B^*=0.5,
\]

with

\[
I_\beta^*=0.64.
\]

An asymmetric allocation `f_A=0.75` retains only

\[
I_\beta=0.48,
\]

while either endpoint returns zero. This makes the second example a genuine resource-allocation problem rather than only a rank demonstration.

### 4. Independent calibration also repairs the failure

Return to the otherwise degenerate A-only design and supply independent common-offset precision

\[
\Lambda=\operatorname{diag}(\lambda,0).
\]

The same profiler gives

- `lambda=1` -> `I_beta=0.5`;
- `lambda=9` -> `I_beta=0.9`.

Hence the same Eq. (1) exposes two distinct remedies: spend resource on response diversity, or supply explicit calibration information about the nuisance.

## Reviewer-facing transfer matrix

| Requirement | Dual-transition clock benchmark |
|---|---|
| Independent quantum sensor class | Ramsey/atomic-clock frequency sensing rather than inertial Raman phase sensing |
| Different `s_k` | transition sensitivities `q_A=+1`, `q_B=-0.6` |
| Different `J_k` | shared frequency-reference offset + drift |
| Explicit nuisance failure | A-only and B-only both give `I_beta=0` |
| Response-diversity recovery | mixed A/B interrogation gives positive information |
| Resource optimization | 101-point scan finds `f_A=f_B=0.5`, `I_beta=0.64` |
| Calibration recovery | A-only rises to `0.5` and `0.9` for finite offset precision |
| Same numerical machinery | frozen `profiled_beta_information` reused unchanged |

This supports **cross-architecture transfer of the design criterion**. It does not establish the performance of a specific clock, nor does it rely on the illustrative sensitivity values being realized by a particular species.

## Manuscript-ready insertion

> To test whether Eq. (1) is specific to atom gravimetry, we applied the unchanged nuisance-profiled resource law to a reduced dual-transition atomic-clock frequency-sensing architecture. Two clock responses with distinct normalized science sensitivities share a common reference-frequency offset and linear drift. Either response used alone is locally non-identifiable after profiling (`I_beta=0`), whereas mixed interrogation creates a differential score direction that survives the common nuisances. A 101-point resource scan finds an interior optimum at equal allocation, giving `I_beta=0.64` in normalized units, compared with `0.48` at a 75:25 allocation and zero at either single-transition endpoint. Independent offset calibration provides a second recovery route. Thus the gravimeter and clock examples use different physical responses and nuisance Jacobians but the same Eq. (1) implementation and profiling rule.

The paragraph should be adapted to the manuscript's final notation and equation numbering. The normalized `q_A,q_B` values should remain identified as illustrative coefficients, not species-specific constants.

## Reproduction

```bash
python analysis/paper3_profiled_resource_law.py
python analysis/paper3_atomic_clock_second_sensor_benchmark.py --check-result
```

Expected gates:

- independent sensor architecture: PASS;
- explicit transition-response diversity: PASS;
- same profiled resource law: PASS;
- nuisance-induced failure: PASS;
- response-diversity recovery: PASS;
- allocation optimum scanned: PASS;
- calibration recovery: PASS;
- frozen core decision rules modified: **false**.

## QST scope effect

Compared with the original sign-reversal toy construction, the dual-transition version makes the scope argument materially harder to dismiss as gravimeter-specific algebra: the second example is explicitly a frequency sensor, has its own response coefficients and reference/drift nuisances, exhibits a nuisance-induced endpoint failure, and recovers information through a computed allocation optimum while importing the same frozen profiler. This directly supports framing Paper III as a reusable quantum-sensing experimental-design criterion.
