# RQIR Iteration 106 — Robust Detector-Side Ratio Certificate

**Date:** 2026-08-30  
**Status:** Paper-III common-normalization / robust architecture gate. No hardware forecast and no new-physics claim.

## 1. Purpose

Iteration 105 reduced the final-significance Toy009/Toy014 decision, where separability is valid, to the measurable ratios

`u=R_D,14/R_D,09`,

`v=R_A,14/R_A,09`,

`z=R_A,09/R_D,09`,

`delta=(1-d_14)/(1-d_09)`.

The highest-value missing quantity was `u`: the ratio of the already optimized detector/transfer/seven-calibration profiled Fisher rates in one common apparatus normalization.

A scalar science SNR ratio or calibration-cost ratio is not sufficient because `R_D` is the optimum of a full nuisance-profiled Fisher campaign. This iteration derives a rigorous matrix certificate for `u` without inventing an absolute ASD.

## 2. Profiled Fisher as a variational functional

For a positive-semidefinite Fisher matrix in the common parameter vector `(beta,theta)`,

`J=[[a,b^T],[b,N]]`,

the retained beta information is

`Phi(J)=a-b^T N^-1 b`.

Equivalently, on an identifiable branch,

`Phi(J)=min_q (1,-q)^T J (1,-q)`.

This representation immediately gives two properties already compatible with Iteration 103:

1. **Loewner monotonicity:** if `J_2 >= J_1`, then `Phi(J_2)>=Phi(J_1)`;
2. **positive homogeneity:** `Phi(cJ)=c Phi(J)` for `c>=0`.

These are the ingredients needed to compare two source architectures before a complete absolute apparatus normalization is available.

## 3. RQIR-RESOURCE-062 — Loewner sandwich certificate for `u`

Let the common detector-side campaign set contain science, same-state transfer calibration, the seven physical calibration layers, and any detector/control campaigns that enter the same Fisher schedule. Let

`J_09,k(xi)` and `J_14,k(xi)`

be the corresponding Fisher-rate matrices at apparatus state / uncertainty coordinate `xi`.

Suppose there exist constants `alpha,beta>0` such that, **uniformly for every campaign and every admissible apparatus state**, 

`alpha J_09,k(xi) <= J_14,k(xi) <= beta J_09,k(xi)`

in Loewner order.

If both architectures use the same feasible campaign-fraction set, then after the full Iteration-103/104 schedule optimization,

`boxed{alpha <= u=R_D,14/R_D,09 <= beta}`.

The same statement holds for the robust max-min detector rate when the sandwich is uniform over the same uncertainty set.

This is valuable because it converts the missing detector-side comparison into a finite set of **matrix measurements/bounds** rather than requiring an already-complete absolute wall-clock forecast.

## 4. How to obtain `alpha,beta` from measured Fisher matrices

When `J_09,k` is positive definite, the tight per-campaign bounds are the generalized eigenvalues of the pair `(J_14,k,J_09,k)`:

`alpha_k=lambda_min(J_09,k^-1/2 J_14,k J_09,k^-1/2)`,

`beta_k=lambda_max(J_09,k^-1/2 J_14,k J_09,k^-1/2)`.

A uniform certificate may use

`alpha=min_{k,xi} alpha_k`,

`beta=max_{k,xi} beta_k`.

For singular Fisher matrices the support must be audited explicitly. A finite upper sandwich `J_14<=beta J_09` requires that Toy014 not contain information in a direction that is exactly null for Toy009. Conversely, loss of a Toy009-supported direction can drive the useful lower bound to zero.

Thus nullspace/support information is part of the physical certificate, consistent with the exact-null versus statistical-identifiability distinction of the mature RQIR framework.

## 5. RQIR-NG-061 — scalar subsystem ratios do not certify `u`

A list such as

- science-only `S_eff` ratio;
- seven separate scalar SNR ratios;
- `gamma` or total calibration-cost ratio;
- transfer-amplitude error ratio;

is not, by itself, a certificate for `R_D,14/R_D,09`.

The reason is nuisance orientation: two Fisher matrices with the same trace or standalone scalar information can project very differently after `beta`-nuisance profiling. The campaign optimum can also use different mixtures of science and calibration settings.

A valid detector-ratio certificate therefore requires either

1. the full common-coordinate matrix schedule and direct robust optimization, or
2. a matrix Loewner/generalized-eigenvalue sandwich such as RESOURCE-062.

If the feasible schedule sets differ because one architecture has extra mandatory recertification/minimum-duty constraints, RESOURCE-062 cannot simply be applied with a common simplex. Those scheduling constraints must be included explicitly or justified by set inclusion.

## 6. Direct engineering threshold for the missing detector ratio

Iteration 105 gives

`G=Q_14/Q_09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

Solving `G>1` for `u` gives a directly measurable threshold. Define

`H = sqrt(delta)(1+z^-1/2) - (v z)^-1/2`.

If `H>0`, Toy014 can win only if

`boxed{u > u_req(v,z,delta)=H^-2}`.

If `H<=0`, no finite detector-side improvement can rescue Toy014.

Equivalently, the `u -> infinity` limit is

`G_infinity=delta v (1+sqrt(z))^2`.

### RQIR-NG-062 — detector no-rescue condition

If

`boxed{delta v (1+sqrt(z))^2 <= 1}`,

then Toy014 cannot beat Toy009 for any finite positive detector-side ratio `u` within the separable final-significance model.

This is distinct from NG-060: NG-060 says the Ramsey advantage alone is insufficient; NG-062 identifies the region in which **even arbitrarily favorable detector-side throughput cannot compensate the source/duty geometry**.

## 7. Regression threshold surface — not an apparatus forecast

Iteration 092 found that, in the common Ramsey model over the declared reset/visibility audit box, the Toy014/Toy009 optimized source-rate ratio stayed above approximately

`v=1.39`.

Use this value only as a retained design-box regression, not as a universal hardware lower bound.

For equal duty, RESOURCE-062 gives the following detector-ratio thresholds:

| `z=R_A,09/R_D,09` | required `u` for Toy014 |
|---:|---:|
| `0.01` | `0.1577067791` |
| `0.03` | `0.2839954413` |
| `0.10` | `0.4564952030` |
| `1.00` | `0.7537676652` |

Thus the required detector competitiveness depends strongly on whether the Toy009 baseline is source-limited or detector/calibration-limited.

Using instead the mature zero-reset Ramsey ratio

`v=1.49133431799`

and the Iteration-105 crossover value

`z=0.04239396157`

returns exactly

`u_req=0.283014657458`,

recovering the old science-only regression slice as a consistency check.

If the illustrative duty factors `d_09=.02`, `d_14=.08` are imposed and `v=1.39`, the required thresholds rise to approximately

- `u_req=0.2111831` at `z=.01`;
- `0.3603510` at `z=.03`;
- `0.5481772` at `z=.10`;
- `0.8422677` at `z=1`.

Again these are threshold surfaces, not measured apparatus predictions.

## 8. RQIR-RESOURCE-063 — exact independent-box architecture certificate

Suppose a common-normalization audit yields independent positive intervals

`u in [u-,u+]`, `v in [v-,v+]`, `z in [z-,z+]`, `delta in [delta-,delta+]`.

`G` is monotone increasing in `u`, `v`, and `delta`. Its dependence on `z` has the Iteration-105 sign determined by `v-u`.

Therefore the exact lower bound is obtained at

`u=u-`, `v=v-`, `delta=delta-`,

and

- `z=z+` if `v->u-`;
- `z=z-` if `v-<u-`.

The exact upper bound is obtained at

`u=u+`, `v=v+`, `delta=delta+`,

and

- `z=z-` if `v+>u+`;
- `z=z+` if `v+<u+`.

Consequently:

- if `G_lower>1`, Toy014 is an NG-030 robust winner;
- if `G_upper<1`, Toy009 is an NG-030 robust winner;
- otherwise the architecture decision remains unresolved.

For correlated physical uncertainties replace this Cartesian-box rule by the actual joint uncertainty set; do not manufacture independent endpoints.

## 9. Numerical regression

`analysis/detector_ratio_certificate_iteration106.py` constructs two synthetic positive-definite campaign matrices for each architecture.

The exact per-campaign generalized-eigenvalue envelope is

`alpha=0.55`, `beta=1.40`.

Direct simplex optimization gives

`R_D,14/R_D,09 ~= 0.617284516`,

which lies inside the certified interval as required.

A separate four-coordinate box regression verifies RESOURCE-063 against all Cartesian corners. The script also reproduces the Iteration-105 crossover and an explicit NG-062 no-rescue case.

All matrices and interval examples in the script are synthetic algebraic regressions only.

## 10. Scientific consequence

The missing detector-side quantity `u` is no longer conceptually an opaque scalar that must be guessed from an ASD. It can be bounded directly from measured or simulated **common-coordinate Fisher matrices** campaign by campaign.

This narrows Paper III's remaining apparatus task:

1. obtain same-state temporal `f,2f` science/transfer Fisher matrices for Toy009 and Toy014;
2. obtain the seven physical calibration Fisher-rate matrices in the same coordinate system;
3. include mandatory control/recertification schedule constraints;
4. compute either direct robust `R_D` or the RESOURCE-062 matrix envelope;
5. combine it with robust `v,z,delta` using RESOURCE-063 and NG-030.

Toy015 remains premature until this exercise shows that the residual active marginal cost is genuinely source-dependent.

## 11. Reproducibility

Run

`python analysis/detector_ratio_certificate_iteration106.py`.
