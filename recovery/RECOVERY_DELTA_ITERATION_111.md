# RQIR Recovery Delta — Iteration 111

**Date:** 2026-08-30  
**Parent front:** Iteration 110.  
**Scientific parent:** Iteration 109.

## New Paper-III result

For pure-dead scalar control references,

`S_ij=sigma_*ij^2-sigma_f,ij^2`,

`h_ij=2D_ij/(R_ref,ij S_ij^2)`,

`H_i=sum_j h_ij`.

### RESOURCE-069

For non-overlapping pure-dead control blocks,

`eta_i=1/(1+H_i)`,

`u_wall=u_live(1+H_09)/(1+H_14)`.

This is the multi-control extension of the Iteration-108 timing-only correction.

### RESOURCE-070

For final detector threshold `u_req`, one unresolved Toy014 control `j` has decision headroom

`K_14,j=(u_live/u_req)(1+H_09)-1-H_14,-j`.

If `K<=0`, improving that one reference cannot rescue Toy014. If `K>0`, its required Fisher rate is

`R_ref,14,j > 2D_14,j/[K_14,j (sigma_*14,j^2-sigma_f,14,j^2)^2]`.

At fixed rate/drift/headroom,

`sigma_f^2 <= sigma_*^2-sqrt[2D/(R_ref K)]`.

### NG-067

A larger reference Fisher rate cannot repair an irreducible stability floor that leaves insufficient usable variance budget.

### RESOURCE-071

For independent interval boxes,

`u_wall,L=uL(1+H09L)/(1+H14U)`,

`u_wall,U=uU(1+H09U)/(1+H14L)`.

- robust Toy014 detector-side sufficiency: `u_wall,L>u_req`;
- full-box impossibility: `u_wall,U<=u_req`;
- otherwise unresolved / characterization valuable.

Correlated uncertainty remains subject to NG-030 and requires the actual joint set.

### DESIGN-015

Characterize boundary-crossing controls first; after physical likelihood closure, rank them by RESOURCE-064 schedule shadow price.

## Scope guard

The aggregate `H=sum h_j` is exact only for genuinely pure-dead, non-overlapping references. Fisher-carrying/jointly estimated controls belong in the full RESOURCE-064 matrix schedule.

No missing geometry/additive/gain SI rate was invented.

## Files

- `analysis/control_threshold_surface_iteration111.py`
- `docs/PAPER_III_CONTROL_THRESHOLD_SURFACE_ITERATION111.md`
- `research_log/2026-08-30_iteration_111_control_threshold_surface.md`

## Next gate

Close one same-apparatus physical control channel and insert it into RESOURCE-071. Leading candidate: complex gain/phase, because injected-transfer Fisher already exists from Iterations 101–103 while temporal gain/phase drift/stability remains missing. Do not open Toy015 yet.
