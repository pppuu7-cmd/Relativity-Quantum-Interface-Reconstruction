# RQIR Research Log — Iteration 108

**Date:** 2026-08-30

## Goal

Continue from Iteration 107 and use the already repository-backed Toy009/Toy014 timing-control benchmarks to build the first source-specific recertification correction without inventing geometry/additive/gain drift models.

## Source audit

Re-read:

- `docs/TIMING_RECERTIFICATION_WALLCLOCK_ITERATION076.md`;
- `docs/TOY014_PHYSICAL_SYSTEMATICS_ITERATION075.md`;
- `docs/CENTERED_SYSTEMATICS_REVALIDATION.md`;
- `analysis/timing_recertification_wallclock_iteration076.py`.

The source-specific centered timing tolerances are:

- Toy009 D2 `sigma_t ~= 9.19001 us`;
- Toy014 `sigma_t ~= 3.97715 us`.

Iteration 076 correctly found about a 24.91x larger Toy014 timing-reference overhead under identical transparent jitter/drift assumptions.

## NUM-007 — resource convention correction

Iteration 076 used

`r=T_ref/T_cad`

where `T_cad` is the allowed live interval, then called `r` a duty fraction and used `1/(1-r)` as payload multiplier.

Under the explicit Iteration-107 live/reference convention:

`m_wall=1+r`,

`d_wall=r/(1+r)`,

`eta_live=1/(1+r)`.

The old expression is only first-order accurate for small r.

## Corrected numerical regressions

At `D_tau=100 us^2/h`:

- Toy014 exact wall-reference fraction `8.7751553e-4`;
- Toy009 `3.5261872e-5`.

At `D_tau=1000 us^2/h`:

- Toy014 `8.7063953e-3`;
- Toy009 `3.5250685e-4`.

The corrected historical projected Toy014/Toy009 boundaries are:

- D=100: `y > 7.71179277314 + 7.56402916784 x`;
- D=1000: `y > 7.91566900880 + 7.76444739107 x`.

The qualitative conclusion of Iteration 076 is unchanged at small/moderate overhead.

## Corrected high-overhead interpretation

For Toy014 in the declared Brownian/reference benchmark:

- exact 10% total-wall reference fraction occurs at `D_tau ~= 1.26509e4 us^2/h`;
- the old `D_tau ~= 1.13858e5 us^2/h` point corresponds to `r=1`, hence exactly 50% total-wall reference time, not 100%;
- 100% total-wall duty is approached only asymptotically as r diverges.

## RESOURCE-066

For pure-dead timing references:

`u_wall=u_live (1+r09)/(1+r14)`.

Therefore a detector threshold `u_req` requires

`u_live > u_req (1+r14)/(1+r09)`.

If reference blocks carry nuisance Fisher, use Iteration-107 RESOURCE-064 instead of this scalar correction.

## Remaining control cuts

Timing can now be parameterized source-specifically without new apparatus assumptions. Geometry/additive/gain tolerances exist in toy coordinates, but their common physical transduction, drift spectra and reference Fisher-rate models are still not supplied. Do not fabricate them.

## Files

- `analysis/timing_overhead_convention_iteration108.py`
- `docs/PAPER_III_TIMING_OVERHEAD_CONVENTION_ITERATION108.md`
- `recovery/RECOVERY_DELTA_ITERATION_108.md`

## Next gate

Build a Toy009/Toy014 control-cut status matrix: timing as parameterized/partially closed; geometry, additive and gain as open physical cuts. For each open cut derive the minimum same-apparatus reference measurement/Fisher object needed to promote it into the constrained scheduler. Toy015 remains closed.
