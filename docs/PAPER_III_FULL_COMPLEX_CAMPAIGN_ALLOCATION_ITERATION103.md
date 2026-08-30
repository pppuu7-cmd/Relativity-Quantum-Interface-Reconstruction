# RQIR Iteration 103 — Full Complex `f,2f` Profile and Multi-Campaign Time Allocation

**Date:** 2026-08-30  
**Status:** Paper-III full-complex detector/calibration closure; exact local-Gaussian resource theorem plus deterministic regression examples. Not a hardware forecast and not a new-physics claim.

## 1. Purpose

Iteration 102 placed multiplicative transfer uncertainty inside the science Fisher and solved the balanced scalar science/transfer time split. The remaining detector-level task was to remove that scalar simplification and treat the actual four-real-component temporal two-band data vector

`y = (Re z_f, Im z_f, Re z_2f, Im z_2f)`

with complex transfer amplitude/phase nuisance, spectral tilt and multiple calibration campaigns.

The central result of this iteration is that the complete time-allocation problem has a clean convex structure. This is more useful than choosing an arbitrary science/calibration split or optimizing the transfer campaign separately from the seven calibration layers.

## 2. Full campaign Fisher representation

Let the parameter vector be

`p = (beta, theta)`

where `theta` contains every locally retained nuisance coordinate: complex transfer gains/phases, spectral tilt, source/calibration nuisance coordinates and any other detector nuisance admitted by the declared likelihood.

Let campaign `k` supply a positive-semidefinite Fisher **rate** matrix `J_k` per unit wall time. The campaigns may include

- the science acquisition `J_sci`;
- the same-state dual-tone complex-transfer injection `J_tr`;
- the seven physical calibration campaigns `J_cal,1 ... J_cal,7`;
- later source/control campaigns if they are written in the same joint parameterization.

For non-negative campaign times `t_k`, the total Fisher is

`J(t) = sum_k t_k J_k`

and partition it as

`J = [[a,b^T],[b,N]]`.

The detector-level profiled science information is

`F_beta(t) = a - b^T N^-1 b`

on an identifiable branch with nonsingular nuisance block `N`. Exact hard constraints should be eliminated before forming this matrix; singular branches require the established exact-null/pseudoinverse discipline rather than threshold deletion.

## 3. RQIR-RESOURCE-057 — campaign-simplex theorem

Because `a`, `b` and `N` are affine in campaign time and the matrix-fractional function `b^T N^-1 b` is convex, the profiled information

`F_beta(t)`

is a concave, positively homogeneous function of the non-negative campaign times.

Therefore the minimum-wall-clock problem

`min sum_k t_k`

subject to

`F_beta(t) >= F_* = Z^2`

is a convex optimization problem.

Equivalently, write campaign fractions `x_k>=0`, `sum x_k=1`. Define the best achievable profiled Fisher rate

`R_* = max_x F_beta(sum_k x_k J_k)`.

Then the exact minimum pre-duty wall time is

`boxed{T_min = Z^2/R_*}`

and the optimal campaign times are

`t_k^* = T_min x_k^*`.

This converts science + transfer + seven-layer calibration scheduling into one Fisher-rate optimization rather than a sequence of independent heuristic budgets.

## 4. Exact marginal value of one campaign

Define

`q = N^-1 b`

and the efficient-profile direction

`w = (1,-q)`.

For an infinitesimal increase of campaign `k`,

`boxed{partial F_beta / partial t_k = w^T J_k w}`.

This quantity is non-negative for `J_k>=0` and has the units of retained profiled Fisher per additional wall-clock second.

### RQIR-RESOURCE-058 — profile-Fisher equal-marginal rule

At an interior optimum over campaign fractions, every active campaign satisfies

`boxed{w^T J_k w = R_*}`.

Inactive campaigns satisfy

`w^T J_k w <= R_*`.

The equality follows from the KKT conditions plus positive homogeneity (Euler's theorem). Hence the correct analogue of water-filling is not equal time, equal raw Fisher, or equal fractional calibration precision. The optimum equalizes **marginal profiled science information per second** among the campaigns that are actually worth running.

This is the full-matrix generalization of Iteration-102 RESOURCE-056 and Iteration-097 characterization water-filling.

## 5. Full complex transfer nuisance

For each temporal band, let the fiducial complex science signal define two real vectors:

- amplitude derivative `a_n`;
- phase derivative `p_n = J a_n`, where `J` is the 90-degree quadrature rotation in that band's two-real-dimensional plane.

The full local science mean Jacobian may therefore contain

`H = [s_beta, a_f, p_f, a_2f, p_2f, t_tilt, ...]`.

For a Gaussian mean likelihood with four-real precision matrix `W`,

`J_sci = H^T W H`.

The deterministic regression verifies the mature NG-056 result in this complete four-real representation: if the two independent complex transfer gains are unconstrained, their amplitude columns span the common-amplitude science direction and the profiled `beta` Fisher is zero up to numerical precision.

Adding a positive same-state injected-transfer Fisher block restores positive information.

## 6. RQIR-NG-058 — phase calibration is not automatically irrelevant

It is tempting to drop transfer phase uncertainty because, in Euclidean quadratures,

`a_n^T p_n = 0`.

That is only valid when the science Fisher metric preserves this orthogonality.

The correct condition is

`boxed{s_beta^T W p_n = 0}`

(and the corresponding conditions after all other nuisance projections).

For block-isotropic independent quadrature noise this can hold. Under anisotropic quadrature precision, cross-quadrature covariance, cross-band covariance, filtering or whitening uncertainty, it need not.

The full-complex regression uses a positive-definite non-isotropic `W` and obtains nonzero phase couplings (`~0.104` and `~-0.0312`) although Euclidean amplitude/phase products vanish exactly.

> **RQIR-NG-058:** do not omit transfer-phase calibration merely because the unweighted complex signal is amplitude/phase orthogonal. Phase is removable only after Fisher-metric orthogonality has been demonstrated in the declared same-state likelihood.

## 7. Eight-calibration symmetric regression

To verify the multi-campaign theorem transparently, use a synthetic model with `m=8` nuisance gains. One science campaign measures `beta+g_i` in all eight channels, while each of eight independent calibration campaigns measures one gain at Fisher rate `c`.

With total-time fractions `x_s` for science and equal `x_c` for each calibration,

`x_s + m x_c = 1`.

The exact optimum is

`boxed{x_s = sqrt(c/m)/(1+sqrt(c/m))}`

`boxed{x_c = 1/[m(1+sqrt(c/m))]}`

and

`boxed{R_* = c/[1+sqrt(c/m)]^2}`.

For the deterministic regression `m=8`, `c=8`:

- science fraction `x_s=0.5`;
- each of eight calibration fractions `x_c=0.0625`;
- optimized profiled Fisher rate `R_*=2`;
- for `Z=5`, minimum total time in the arbitrary regression units is `12.5`.

Every one of the nine active campaigns has exactly the same marginal profiled rate `2`, verifying RESOURCE-058.

These numbers are algebraic regression only; they are not RQIR apparatus times.

## 8. Relation to the seven physical calibration layers

The theorem does not require each RQIR calibration layer to be a scalar nuisance or an independent `2x2` block. Each physical layer contributes its actual Fisher-rate matrix `J_cal,j` in the common nuisance coordinates. Therefore the already mature Iteration-088 blocks

`F_j=[[a_j,c_j],[c_j,b_j]]`

can be inserted after mapping their physical transduction into the joint source/detector nuisance basis.

If a layer has zero marginal value `w^T J_cal,j w` on the active branch, the optimizer allocates it zero *for the declared science target*. This must not be confused with deleting a hard consistency/calibration requirement: any externally mandated constraint must remain as an explicit feasibility constraint.

## 9. Consequence for Paper III

The remaining detector/calibration problem is no longer algebraically ambiguous. Given one common-normalization apparatus that supplies

- the four-real science Fisher-rate matrix;
- full complex transfer-injection Fisher rate;
- measured temporal covariance/cross-PSD model;
- seven physical calibration Fisher-rate matrices;

then the minimum `T_sci+T_transfer+T_7cal` is a single convex optimization with an exact marginal certificate.

The missing information is still apparatus data, not another arbitrary resource parameter.

## 10. What remains open

Still open:

- source-specific physical `J_k` matrices for Toy009/Toy014 from one apparatus;
- covariance uncertainty/robust corners in the same optimization rather than a fixed `W`;
- source preparation/metrology and campaign control duty added to the campaign simplex;
- simultaneous-reference/backaction constraints if calibration is performed during science;
- absolute NG-030 Toy009/Toy014 winner;
- classical/stochastic/full-QFT and relativistic/gauge/EFT/renormalization gates.

No new physics is claimed.

## 11. Next admissible gate

Extend RESOURCE-057/058 from fixed covariance to the **robust apparatus envelope**:

1. take the worst admissible temporal PSD/cross-PSD covariance matrix and transfer/calibration-rate intervals;
2. solve the max-min campaign-fraction problem rather than optimizing only at nominal central values;
3. add the already physical source-metrology rate `R_src` and control/reference duty;
4. evaluate Toy009 and Toy014 with the same robust scheduling rule and apply NG-030.

Only if the resulting dominant marginal cost is source-dependent should Toy015 be opened.

## 12. Reproducibility

Code:

`analysis/full_complex_campaign_allocation_iteration103.py`

The script verifies the full-complex free-gain zero-Fisher gate, restoration by transfer calibration, nonzero phase coupling in a non-isotropic Fisher metric, the exact derivative identity, positive homogeneity, concavity, the symmetric multi-calibration optimum and the equal-marginal KKT certificate.
