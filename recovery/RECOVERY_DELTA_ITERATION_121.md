# RQIR Recovery Delta — Iteration 121

**Date:** 2026-08-31  
**Parent front:** Iteration 120.

## Physical rate-level detector bracket

For final detector Fisher target `F_*`, science rate `R_s` and independent common-gain reference rate `R_c`,

`T_DT=F_*[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

Seven mean layers:

`T_m=gamma_m sum_j 1/R_m,j`.

Four covariance matching blocks:

`T_C,match=gamma_c sum_b 1/R_C,b`.

Eight separate covariance rows:

`T_C,sep=gamma_c sum_k 1/r_C,k`.

### RESOURCE-091

`T_D^L=max(T_DT,T_m,T_C,match)`

`T_D^M=T_DT+T_m+T_C,match`

`T_D^U=T_DT+T_m+T_C,sep`.

### RESOURCE-092

At fixed target `R_D=F_*/T_D`, so for `T_i in [L_i,U_i]`,

`u=R_D14/R_D09=T_D09/T_D14`

obeys

`u in [L_09/U_14,U_09/L_14]`.

### RESOURCE-093

A common multiplicative scaling of all detector-side Fisher rates rescales all times inversely but leaves the `u` interval unchanged.

### NG-079

If `1` lies in the certified `u` interval, detector-side architecture selection remains unresolved. Final selection must also include source ratio `v`, baseline ratio `z` and duty `delta`.

The stored regression interval `~[0.0902,0.5650]` uses deliberately artificial rates and is not an apparatus forecast.

## Readiness after Iteration 121

- Paper III scientific-content readiness: **94%**.
- Paper III submission readiness: **75%**.
- Repository readiness to begin Candidate Gravity: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Files

- `analysis/detector_rate_bracket_iteration121.py`
- `docs/PAPER_III_DETECTOR_RATE_BRACKET_ITERATION121.md`
- `research_log/2026-08-31_iteration_121_detector_rate_bracket.md`

## Next gate

Tighten physical rate intervals from defensible same-apparatus data for common-gain transfer, covariance throughput/backaction, geometry and additive references. If unavailable, keep the certificate parametric and move effort toward Paper-III manuscript/literature synthesis rather than inventing rates.
