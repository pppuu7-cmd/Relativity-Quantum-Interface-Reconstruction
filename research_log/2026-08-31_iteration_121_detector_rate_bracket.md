# RQIR Research Log — Iteration 121

**Date:** 2026-08-31

## Question

Can the current science/transfer/mean/covariance uncertainty be propagated directly into the final detector-side architecture variable `u=R_D14/R_D09` using physical Fisher-rate inputs?

## Result

For final detector Fisher target `F_*`, science rate `R_s` and common-gain reference rate `R_c`,

`T_DT=F_*[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

Seven mean layers:

`T_m=gamma_m sum_j 1/R_m,j`.

Four covariance matching blocks:

`T_C,match=gamma_c sum_b 1/R_C,b`.

Eight separate covariance rows:

`T_C,sep=gamma_c sum_k 1/r_C,k`.

Detector-time branches:

`T_D^L=max(T_DT,T_m,T_C,match)`

`T_D^M=T_DT+T_m+T_C,match`

`T_D^U=T_DT+T_m+T_C,sep`.

At fixed target,

`u=T_D,09/T_D,14`, so for intervals `T_i in [L_i,U_i]`,

`u in [L_09/U_14,U_09/L_14]`.

A common multiplicative scaling of every detector-side Fisher rate rescales all detector times but leaves the `u` interval invariant.

Labels:

- **RESOURCE-091:** physical detector-time bracket.
- **RESOURCE-092:** exact detector-time interval -> robust `u` map.
- **RESOURCE-093:** common-rate scale invariance.
- **NG-079:** detector choice unresolved whenever `1` lies in the certified `u` interval.

The stored artificial regression gives `u~[0.0902,0.5650]` only to verify algebra; it is explicitly not an apparatus forecast.

## Readiness snapshot

Project-management estimates, not statistical quantities:

- Paper III scientific-content readiness: **94%**.
- Paper III submission readiness: **75%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Next gate

Tighten physical rate intervals using defensible same-apparatus information for common-gain transfer, covariance throughput/backaction, geometry and additive references. If such data cannot be justified, preserve the parametric interval and prioritize Paper-III manuscript/literature synthesis rather than fabricating rates.
