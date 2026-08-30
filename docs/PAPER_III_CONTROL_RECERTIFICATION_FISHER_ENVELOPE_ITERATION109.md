# RQIR Iteration 109 — Control Recertification Fisher Envelope

**Date:** 2026-08-30  
**Status:** Paper-III control/reference resource gate; no apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 108 corrected the pure-dead timing-overhead convention. The next open control problem is broader: timing, geometry, additive and gain references must be promoted from toy tolerances into physical RESOURCE-064 scheduling constraints without inventing SI rates.

The useful intermediate step is to derive the minimum Fisher-rate requirement for a generic recertified nuisance coordinate under Brownian drift.

## 2. Scalar recertification model

Let a physical control coordinate `x` have:

- allowed total standard deviation `sigma_*`;
- irreducible floor `sigma_f`;
- Brownian drift convention `Var_drift(t)=D t/2`, matching the retained repository cadence convention;
- reference Fisher rate `R_ref`;
- reference integration time `t_ref`.

The reference contributes

`sigma_ref^2 = 1/(R_ref t_ref)`.

Define the usable variance budget

`S = sigma_*^2 - sigma_f^2 > 0`.

If a live interval `tau` is allowed between references, the admissibility condition is

`sigma_ref^2 + D tau/2 <= S`.

Hence

`tau = 2(S-sigma_ref^2)/D`.

For a pure-dead reference block the overhead/live ratio is

`r = t_ref/tau`.

## 3. RQIR-RESOURCE-067 — optimal reference/drift variance split

Substituting `t_ref=1/(R_ref sigma_ref^2)` gives

`r = D/[2 R_ref sigma_ref^2 (S-sigma_ref^2)]`.

The denominator is maximized at

`boxed{sigma_ref^2 = S/2}`.

Therefore the minimum-overhead schedule is

`boxed{t_ref^* = 2/(R_ref S)}`,

`boxed{tau_live^* = S/D}`,

and

`boxed{r_min = 2D/(R_ref S^2)}`.

The optimal design allocates exactly half of the available variance budget to reference-estimation uncertainty and half to drift accumulation.

This is a wall-clock result, not an arbitrary one-third rule.

## 4. RQIR-RESOURCE-068 — minimum reference Fisher rate

For a declared maximum overhead/live ratio `r_max`, the required physical reference Fisher rate is

`boxed{R_ref >= 2D/[r_max (sigma_*^2-sigma_f^2)^2]}`.

Thus recertification becomes expensive quartically in a tight zero-floor tolerance:

`R_ref ~ sigma_*^-4`.

An irreducible floor makes the requirement diverge as `sigma_f -> sigma_*`.

### RQIR-NG-065 — a tolerance alone is not a control-time budget

A nuisance tolerance `sigma_*` cannot be converted into campaign time without both a physical drift law/floor and a reference Fisher rate. Conversely, a fast reference detector does not rescue a stability floor at or above the required tolerance.

## 5. Physical Toy009/Toy014 timing comparison

Timing is currently the cleanest source-specific control coordinate because both retained tolerances are already in the same physical unit:

- Toy009 D2: `sigma_t ~= 9.19001083 us` (Iteration 036);
- Toy014: `sigma_t ~= 3.97715 us` (Iteration 075).

For equal timing diffusion `D`, equal desired pure-dead overhead and equal Fisher normalization, RESOURCE-068 gives

`R_ref,14/R_ref,09 = (sigma_09/sigma_14)^4`.

Numerically,

`boxed{R_ref,14/R_ref,09 ~= 28.5086209}`.

This is stronger than the static prior-precision ratio `(sigma_09/sigma_14)^2 ~= 5.33935`: a tighter tolerance both demands a more precise reference and shortens the allowed drift interval.

This does **not** say Toy014 physically costs 28.5x more timing time. It says that under the same scalar Brownian-drift/reference model, maintaining the same optimized overhead fraction requires about 28.5x larger timing-reference Fisher rate.

Iteration 108 remains the correct benchmark when the reference block duration is instead fixed explicitly.

## 6. Additive controls: conditional ratios only

Retained normalized 10%-bundle tolerances are approximately

Toy009 D2:

- additive mean `7.39167814e-5`;
- additive covariance `1.30174869e-4`.

Toy014:

- additive mean `4.19676208e-5`;
- additive covariance `6.06486956e-5`.

If — and only if — these values were expressed in the same physical control coordinate with the same drift and Fisher normalization, the corresponding RESOURCE-068 rate ratios would be

- mean: `~9.62310`;
- covariance: `~21.22378`.

They are **not yet physical architecture ratios**, because the rows are source-normalized and their SI/output transduction has not been closed. They are retained only as conditional regression slices.

### RQIR-NG-066 — normalized additive tolerances are not cross-source SI controls

Do not compare Toy009 and Toy014 additive-reference costs directly from normalized row tolerances. First supply the physical output/force transduction Jacobian, offset process covariance/drift spectrum and same-apparatus reference likelihood.

## 7. Control-cut status matrix

| control cut | Toy009/Toy014 tolerance | common physical coordinate? | drift/floor model? | reference Fisher rate? | RESOURCE-064 ready? |
|---|---|---|---|---|---|
| timing | yes | **yes, seconds** | transparent Brownian benchmark only | benchmark block models exist | **parameterized / partial** |
| geometry | yes in toy coordinate | **no** | no common SI drift spectrum | no | **open** |
| additive mean | yes normalized | **no** | no physical offset drift spectrum | no | **open** |
| additive covariance | yes normalized | **no** | no physical covariance-offset drift spectrum | no | **open** |
| complex gain/phase | transfer Fisher formalism exists | partial through Iterations 101–103 | same-state drift/cadence not yet certified | injected calibration Fisher formalism exists | **partial** |

## 8. Minimum same-apparatus measurement objects for open cuts

### Geometry

Need a physical coordinate `g_phys`, source-specific Jacobian

`J_geom = partial(theta_toy)/partial g_phys`,

plus the reference estimator covariance/Fisher rate and low-frequency drift PSD/Allan model for `g_phys`.

### Additive mean/covariance

Need the row-to-physical-output transduction, a zero/input-off reference likelihood that estimates the additive mean/covariance coordinates, their cross-covariance, and their drift/stability spectra.

### Gain/phase

Iterations 101–103 already specify same-state injected-transfer Fisher. The missing control object is the time evolution of that transfer between injections: gain/phase drift covariance or a measured stability process sufficient to set recertification constraints.

These objects, not merely tighter toy priors, are what promote the cuts into RESOURCE-064.

## 9. Architecture-decision shadow price

Let a binding minimum reference quota `b_ij` reduce the optimized detector rate as

`lambda_ij = - partial R_D,i / partial b_ij >= 0`.

From RESOURCE-061, define the detector-ratio elasticity

`E_u = partial ln(Q14/Q09)/partial ln u`

with

`E_u = u^-1/2/[u^-1/2 + (v z)^-1/2]`.

Then a tighter Toy014 quota changes the architecture log-rate ratio locally by

`boxed{partial ln G/partial b_14,j = -E_u lambda_14,j/R_D,14}`,

while a tighter Toy009 quota gives

`boxed{partial ln G/partial b_09,j = +E_u lambda_09,j/R_D,09}`.

### RQIR-DESIGN-014 — rank controls by architecture-decision shadow price

Once physical reference likelihoods exist, characterize the control with the largest product of schedule shadow price and architecture elasticity, not simply the tightest tolerance or largest drift.

Without `lambda_j` from the same-apparatus Fisher schedule, an absolute ranking of geometry/additive/gain controls is not justified.

## 10. Consequence

Timing alone is now sufficiently parameterized to show that its source-specific tolerance is substantially tighter for Toy014, yet the retained fixed-block Brownian benchmarks of Iteration 108 still produce sub-percent timing-only rate corrections over the `D=100–1000 us^2/h` range.

Therefore the current evidence does **not** identify timing recertification as the dominant Toy014 penalty.

The highest-value missing information is the physical geometry/additive/gain reference Fisher and stability model. Those quantities determine the actual RESOURCE-064 shadow prices and therefore the robust detector ratio `u`.

## 11. Reproducibility

Run

`python analysis/control_recertification_fisher_envelope_iteration109.py`.

The script verifies RESOURCE-067/068, the physical timing rate-ratio result, the conditional additive ratios and the divergence near a stability floor.

## 12. Next admissible gate

Do not start Toy015.

Construct a **parameterized control-threshold surface** for `u` in terms of measurable reference Fisher rates and drift strengths for timing, geometry, additive mean/covariance and complex gain/phase. Use RESOURCE-067/068 to convert each `(R_ref,D,sigma_floor)` into a schedule quota, insert those quotas into RESOURCE-064, and derive break-even conditions for NG-030.

Where common-apparatus Fisher matrices are still absent, keep the shadow prices symbolic or interval-bounded rather than assigning fabricated SI rates.
