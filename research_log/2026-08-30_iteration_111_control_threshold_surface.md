# RQIR Research Log — Iteration 111

**Date:** 2026-08-30

## Goal

Advance the Paper-III front after Iteration 109/110 without reopening the already-completed Toy010 physical-resource conversion. Construct the requested parameterized control-threshold surface for the constrained detector ratio `u=R_D,14/R_D,09` while leaving missing same-apparatus SI rates symbolic.

## Result

For each pure-dead scalar control reference,

`h_ij = 2 D_ij/[R_ref,ij (sigma_*ij^2-sigma_f,ij^2)^2]`.

For non-overlapping pure-dead control blocks,

`H_i=sum_j h_ij`,

`eta_i=1/(1+H_i)`,

and therefore

`u_wall=u_live(1+H_09)/(1+H_14)`.

This is RESOURCE-069 and generalizes the Iteration-108 timing-only wall-clock correction.

For detector-side architecture threshold `u_req`, Toy014 requires

`H_14 < (u_live/u_req)(1+H_09)-1`.

For one unresolved Toy014 control `j`, define

`K_14,j=(u_live/u_req)(1+H_09)-1-H_14,-j`.

If `K<=0`, increasing that reference channel alone cannot rescue the architecture. If `K>0`, the minimum physical Fisher rate is

`R_ref,14,j > 2D_14,j/[K (sigma_*14,j^2-sigma_f,14,j^2)^2]`.

This is RESOURCE-070.

At fixed `R_ref,D,K`, the admissible stability floor satisfies

`sigma_f^2 <= sigma_*^2-sqrt[2D/(R_ref K)]`.

Registered NG-067: reference-rate improvement cannot rescue a floor that leaves insufficient usable variance budget.

## Robust interval result

For independent boxes

`u_live in [uL,uU]`, `H09 in [H09L,H09U]`, `H14 in [H14L,H14U]`,

the exact monotone detector-ratio box is

`u_wall,L=uL(1+H09L)/(1+H14U)`,

`u_wall,U=uU(1+H09U)/(1+H14L)`.

Toy014 is robustly sufficient if the lower bound exceeds `u_req`; impossible over the full box if the upper bound is at/below `u_req`; otherwise further characterization is decision-relevant. Correlated physical uncertainty still requires the actual joint set under NG-030.

Registered RESOURCE-071 and DESIGN-015: characterize controls whose physical uncertainty intervals cross the architecture boundary before spending effort on channels that are safely far from it; then use RESOURCE-064 shadow prices to rank surviving channels.

## Scope

The scalar aggregate is exact only for genuinely pure-dead, non-overlapping reference blocks. Fisher-carrying or jointly estimated correlated references remain RESOURCE-064 matrix-schedule problems.

No geometry/additive/gain SI rate was fabricated. Timing remains the only common physical control regression anchor and remains sub-percent in the stored `D_tau=100–1000 us^2/h` fixed-block slice.

## Reproducibility

- `analysis/control_threshold_surface_iteration111.py`
- `docs/PAPER_III_CONTROL_THRESHOLD_SURFACE_ITERATION111.md`

## Next gate

Close one open same-apparatus physical control channel. Complex gain/phase is the highest-leverage candidate because injected-transfer Fisher already exists from Iterations 101–103; the missing object is its temporal drift/stability process. Insert the resulting interval into RESOURCE-071 and recompute the robust detector-ratio decision before opening Toy015.
