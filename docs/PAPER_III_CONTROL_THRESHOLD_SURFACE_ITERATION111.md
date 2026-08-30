# RQIR Iteration 111 — Parameterized Control-Threshold Surface

**Date:** 2026-08-30  
**Status:** Paper-III architecture/resource gate. No apparatus winner and no new-physics claim.

## 1. Purpose

Iteration 109 derived the optimized scalar recertification overhead

`r_j = 2 D_j / [R_ref,j (sigma_*j^2-sigma_f,j^2)^2]`

for one pure-dead reference coordinate. The next open problem is to combine several such controls into a detector-side architecture threshold without inventing missing SI Fisher rates for geometry, additive offsets or gain/phase stability.

This iteration derives that threshold surface exactly for non-overlapping pure-dead control references and states when the scalar reduction is invalid.

## 2. Aggregate pure-dead control load

For architecture `i in {09,14}` and pure-dead control coordinates `j`, define

`S_ij = sigma_*ij^2 - sigma_f,ij^2 > 0`,

`h_ij = 2 D_ij / (R_ref,ij S_ij^2)`.

If the reference blocks are non-overlapping and contribute no science/nuisance Fisher beyond maintaining the control coordinate, their overheads add per unit live time:

`boxed{H_i = sum_j h_ij}`.

The exact live fraction is then

`eta_i = 1/(1+H_i)`.

Therefore, if `u_live=R_D,14^live/R_D,09^live`, the detector-rate ratio after recertification is

`boxed{u_wall = u_live (1+H_09)/(1+H_14)}`.

### RQIR-RESOURCE-069 — aggregate pure-dead control surface

For scalar pure-dead references obeying RESOURCE-067, all timing/geometry/additive/gain recertification costs enter the detector ratio through the two aggregate loads `H_09,H_14`.

This generalizes RESOURCE-066 from timing alone to a set of certified pure-dead controls.

## 3. Architecture break-even surface

Let `u_req` be the detector-side threshold obtained from the final-significance architecture relation (RESOURCE-061/NG-062) for the currently certified `(v,z,delta)` slice.

Toy014 satisfies the detector-side requirement iff

`u_wall > u_req`,

or equivalently

`boxed{H_14 < (u_live/u_req)(1+H_09)-1}`.

This is the total Toy014 control-overhead budget compatible with the decision.

If the right-hand side is non-positive, no reduction of a positive Toy014 pure-dead control load can rescue the current `u_live` at the declared Toy009 load and `u_req`.

## 4. Per-control Fisher-rate threshold

Separate one Toy014 control `j` from all other Toy014 controls:

`H_14 = H_14,-j + h_14,j`.

Define its architecture-decision headroom

`boxed{K_14,j = (u_live/u_req)(1+H_09)-1-H_14,-j}`.

If `K_14,j <= 0`, that control cannot be made compatible with the decision by increasing its own reference Fisher rate alone.

If `K_14,j > 0`, then RESOURCE-067 gives the exact threshold

`boxed{R_ref,14,j > 2 D_14,j / [K_14,j (sigma_*14,j^2-sigma_f,14,j^2)^2]}`.

### RQIR-RESOURCE-070 — decision-relevant reference Fisher threshold

A missing physical reference channel becomes architecture-decision relevant only through the combination of its drift, usable variance budget and remaining global headroom `K`, not through its toy tolerance alone.

This provides the requested symbolic threshold for geometry, additive mean/covariance and gain/phase until their same-apparatus SI likelihoods are measured.

## 5. Stability-floor threshold

At fixed `R_ref,D,K`, the same inequality can be inverted for the admissible irreducible floor.

Because

`S >= sqrt[2D/(R_ref K)]`,

we require

`boxed{sigma_f^2 <= sigma_*^2 - sqrt[2D/(R_ref K)]}`.

If the right-hand side is negative, even a zero stability floor cannot meet the architecture threshold at that `R_ref` and `D`.

### RQIR-NG-067 — reference-rate rescue has a hard floor boundary

Increasing reference integration/Fisher cannot compensate for an irreducible stability floor that leaves too little usable variance budget. Architecture feasibility should therefore be reported jointly in `(R_ref,D,sigma_f)`, not as a single nominal cadence.

## 6. Robust interval certificate

Suppose the still-uncertain physical apparatus only certifies independent intervals

`u_live in [u_L,u_U]`,

`H_09 in [H_09,L,H_09,U]`,

`H_14 in [H_14,L,H_14,U]`.

Since `u_wall` is monotone increasing in `u_live,H_09` and decreasing in `H_14`, the exact interval is

`boxed{u_wall,L = u_L (1+H_09,L)/(1+H_14,U)}`,

`boxed{u_wall,U = u_U (1+H_09,U)/(1+H_14,L)}`.

Therefore:

- Toy014 is **robustly detector-side sufficient** if `u_wall,L > u_req`;
- Toy014 is **detector-side impossible over the whole box** if `u_wall,U <= u_req`;
- otherwise the apparatus decision remains unresolved and further characterization has positive value.

### RQIR-RESOURCE-071 — monotone control-box certificate

For independent interval uncertainty in pure-dead control loads, the robust detector-side decision requires only the two opposite corners above. Correlated physical uncertainty still requires the actual joint set under NG-030.

## 7. Relation to shadow prices

Iteration 109 defined schedule shadow price for a binding physical quota. The threshold surface adds a complementary screening rule.

A control is high-value to characterize when:

1. its uncertainty materially spans the boundary `h_j=K_j`; and
2. its RESOURCE-064 shadow price is large once the actual Fisher-carrying schedule is constructed.

Thus a sensible measurement priority is not the smallest `sigma_*`, nor the largest raw drift, but the control whose certified interval most strongly changes the sign of the architecture margin and/or carries the largest schedule shadow price.

### RQIR-DESIGN-015 — characterize boundary-crossing controls first

Before investing in a full same-apparatus calibration campaign, use RESOURCE-070/071 to identify which missing control channel can actually change the Toy009/Toy014 architecture decision. Then rank those surviving channels by RESOURCE-064 shadow price.

## 8. Timing implication

Timing is already in a common physical coordinate and remains a regression anchor. Iterations 108–109 showed Toy014 has a substantially tighter timing tolerance, but the stored `D_tau=100–1000 us^2/h` fixed-block benchmark changes the timing-only detector ratio by less than one percent.

Therefore timing remains unlikely to be the dominant architecture discriminator in that benchmark slice. The threshold surface makes this statement sharper: unless the timing term itself approaches the available `K_14,timing`, further timing characterization has low decision value relative to an unresolved geometry/additive/gain term whose interval crosses the boundary.

No numerical geometry/additive/gain winner is assigned because their common SI `R_ref,D,sigma_f` objects are still absent.

## 9. Scope guard

The aggregate formula is valid only when each reference block is genuinely pure dead time relative to the science likelihood and the blocks can be scheduled without overlap/double counting.

If a reference campaign also carries nuisance/science Fisher, or several controls are estimated jointly with correlated scores, use the full RESOURCE-064 campaign Fisher matrix. In that case `H_i=sum h_ij` is at most a conservative bookkeeping envelope, not the exact optimum.

This preserves NG-063 and NG-064.

## 10. Reproducibility

Run

`python analysis/control_threshold_surface_iteration111.py`.

The script verifies:

- exact additive composition of pure-dead overhead/live ratios;
- the detector-ratio wall-clock transformation;
- the per-control headroom/Fisher threshold;
- the stability-floor inversion;
- robust lower/upper interval classification.

## 11. Next admissible gate

Do not start Toy015 yet.

The next highest-value Paper-III step is to connect at least one currently open physical control channel to a same-apparatus measurable object:

- complex gain/phase is the leading candidate because injected-transfer Fisher already exists from Iterations 101–103; only its time-domain drift/stability process is missing;
- geometry and additive channels remain acceptable alternatives if a common SI transduction and reference likelihood can be derived without apparatus invention.

Once one such channel is closed, insert its physical `(R_ref,D,sigma_f)` interval into RESOURCE-071, recompute the robust `u` box, and evaluate whether the architecture margin is still controlled by detector resources or by source-metrology `(v,z)` uncertainty.
