# RQIR Recovery Delta — Iteration 096

**Date:** 2026-08-30  
**Parent front:** Iteration 095.

## What changed

The robust Toy009/Toy014 value-of-information programme now includes the physical rate/cost of characterization itself.

Retain:

`Xi_x = 0.5 Lambda_x R_char,x h_x^2`

for a locally smooth, independent Fisher-limited characterization coordinate. `Lambda_x` is the Iteration-094 fractional unresolved-band leverage, `h_x` the present uncertainty scale, and `R_char,x` the characterization Fisher rate.

### New labels

- **RQIR-RESOURCE-048:** decision value per characterization second.
- **RQIR-NG-049:** raw decision leverage does not determine measurement priority without characterization throughput/cost.
- **RQIR-RESOURCE-049:** finite uncertainty-contraction time with an irreducible floor:

  `T_char=[1/(h1^2-hf^2)-1/(h0^2-hf^2)]/R_char`.

Do not claim an 'actual highest-value measurement' from Iteration-095 derivatives alone.  A primitive characterization envelope must supply `(h,R_char,h_floor,duty/cost)` or a joint Fisher/covariance update.

NG-048 remains active at calibration eigenvalue crossings, PSD boundaries, robust-corner switches and Ramsey active-set changes.

## Files

- `analysis/characterization_time_voi_iteration096.py`
- `docs/PAPER_III_CHARACTERIZATION_TIME_VOI_ITERATION096.md`
- `research_log/2026-08-30_iteration_096_characterization_time_voi.md`

## Next admissible gate

Optimize finite characterization-time allocation across multiple channels (diminishing Fisher returns), then apply it to a declared Toy009/Toy014 primitive uncertainty envelope.  Do not start Toy015 unless the physical rate-space budget shows a source-dependent bottleneck.
