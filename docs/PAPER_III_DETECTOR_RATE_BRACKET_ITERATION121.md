# RQIR Iteration 121 — Physical Detector-Rate Bracket and Robust `u` Interval

**Date:** 2026-08-31  
**Status:** Paper-III detector-side rate certificate. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 120 bracketed mean/covariance calibration in a normalized accepted-cycle coordinate. The next step is to remove the equal-cycle simplification and write the bracket directly in **physical Fisher-rate variables** so that unequal duration, acceptance, transfer and detector sensitivity can be inserted without changing the algebra.

The target is a reusable interval for

`u = R_D,14/R_D,09`,

the detector-side Toy014/Toy009 rate ratio used by the final architecture certificate.

## 2. Science plus common-gain transfer

For final detector Fisher target `F_*`, science rate `R_s` and independent common-gain reference rate `R_c`, Iterations 114–115 give the optimized science/transfer time

`boxed{T_DT = F_* [1/sqrt(R_s)+1/sqrt(R_c)]^2}`.

This term already contains the optimal science/common-gain time split. Do not add a second common-gain calibration time to it.

## 3. Seven physical mean-layer rates

Let the seven same-time dual-probe mean campaigns have weakest-direction Fisher rates

`R_m,j>0`, `j=1,...,7`.

With the current architecture-specific target `gamma_m`, their separate-campaign time is

`boxed{T_m = gamma_m sum_j 1/R_m,j}`.

Each `R_m,j` must come from the full two-output matrix likelihood, not from two independently quoted marginal SNR values.

## 4. Covariance campaign libraries

### Four-matching library

Let the four Iteration-119 matching blocks have physical weakest-direction Fisher rates

`R_C,b>0`, `b=1,...,4`.

If they are physically realizable but scheduled separately from the mean campaign,

`boxed{T_C,match = gamma_c sum_b 1/R_C,b}`.

### Eight-separate-row library

Let the eight individually scheduled covariance rows have rates `r_C,k>0`. Then

`boxed{T_C,sep = gamma_c sum_k 1/r_C,k}`.

These two expressions replace the normalized `4 gamma_c` and `8 gamma_c` counts of Iteration 120 once real cycle duration, acceptance and per-record Fisher are known.

## 5. RQIR-RESOURCE-091 — physical detector-time bracket

Without a joint transfer/mean/covariance likelihood, three useful detector-side branches are

### Absolute perfect-sharing lower bound

`boxed{T_D^L = max(T_DT,T_m,T_C,match)}`.

This is only a mathematical lower bound: it assumes one physical wall-clock stream could satisfy all three information burdens simultaneously.

### Matching covariance, no cross-family sharing

`boxed{T_D^M = T_DT+T_m+T_C,match}`.

### Conservative separate covariance

`boxed{T_D^U = T_DT+T_m+T_C,sep}`.

Thus

`T_D^L <= T_D^M <= T_D^U`

for the declared campaign libraries.

A physical joint block can tighten this interval only through its full Fisher-rate matrix and RESOURCE-083. No overlap credit is granted from shared timestamps or shared hardware alone.

## 6. RQIR-RESOURCE-092 — robust detector-ratio interval

At fixed final detector Fisher target,

`R_D = F_*/T_D`.

Therefore

`u = R_D,14/R_D,09 = T_D,09/T_D,14`.

If architecture `i` has certified detector-time interval

`T_i in [L_i,U_i]`,

then

`boxed{u in [L_09/U_14, U_09/L_14]}`.

This is the first direct non-double-counted interval map from the current science/transfer/mean/covariance campaign libraries to the final detector-side architecture variable `u`.

### NG-079 — no detector architecture claim from overlapping `u`

- if `u_L>1`, Toy014 has a robust detector-side rate advantage under the declared intervals;
- if `u_U<1`, Toy014 has a robust detector-side rate disadvantage;
- if `1 in [u_L,u_U]`, the detector-side choice remains unresolved and NG-030 applies.

This decision is still **detector-side only**. Final architecture selection must also include source-metrology ratio `v`, baseline ratio `z` and duty `delta` through RESOURCE-061/063.

## 7. Homogeneity

If every detector-side Fisher rate for both architectures is multiplied by one common positive factor `k`, then every time bound scales as

`T -> T/k`,

while the `u` interval is unchanged.

### RQIR-RESOURCE-093 — common-rate scale invariance

> Architecture selection depends on relative rate geometry and resource composition, not on an overall common detector-speed scale.

This is useful when an apparatus model determines reliable relative transfer/calibration matrices before the absolute PSD normalization is finalized.

## 8. Dimensionless regression only

The stored script uses deliberately artificial positive rates solely to test the certificate:

- `R_s,09=1`;
- `R_s,14=0.28301465746` (the old same-kernel science ratio used as a regression);
- `R_c,09=R_c,14=1`;
- all mean-layer rates `=9`;
- all covariance matching/separate rates `=1`;
- `F_*=25`.

This gives an illustrative detector interval approximately

`u in [0.0902,0.5650]`.

Because every calibration/transfer rate in this regression was chosen artificially, this is **not** evidence that Toy009 beats Toy014 on a real apparatus. The only purpose is to verify the interval algebra and NG-079 logic.

## 9. Relation to RESOURCE-083

RESOURCE-091 is a bracket built from campaign families whose mutual overlap is unknown.

When a physical same-state likelihood supplies a joint Fisher matrix spanning, for example, common transfer gain plus a covariance matching block, replace the corresponding separate terms by one RESOURCE-083 campaign matrix. The detector interval must then tighten monotonically relative to the current conservative library if the new joint block genuinely adds simultaneous information.

## 10. What this iteration closes

Closed:

- physical-rate replacement of the normalized Iteration-120 calibration bracket;
- inclusion of optimized common-gain transfer time without double counting;
- exact conversion of detector-time intervals into the architecture variable `u`;
- common-rate scale invariance;
- explicit detector-side NG-030 decision rule.

Still open:

- physical same-apparatus `R_s`, `R_c`, seven `R_m,j`, and four/eight covariance rates for Toy009/Toy014;
- transfer/source-calibration overlap matrix, if any;
- geometry/additive SI reference rates and physical drift;
- final total architecture decision including `(v,z,delta)`.

## 11. Readiness snapshot after Iteration 121

Project-management estimates, not statistical quantities.

- **Repository readiness for writing Paper III — scientific content:** **94%**.
- **Paper III submission-ready state:** **75%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **84%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

Paper III increases because the calibration-sharing uncertainty can now be propagated all the way to the final detector architecture coordinate `u` using physical rate inputs. Candidate-Gravity readiness remains unchanged because no candidate dynamics or QG consistency gate was closed.

## 12. Next admissible gate

The remaining high-value Paper-III task is no longer another abstract scheduler theorem. It is to **tighten the physical rate intervals** using repository-backed or externally defensible same-apparatus information:

1. common-gain `R_c` from the full-complex same-state reference;
2. covariance matching-block rates/backaction feasibility;
3. geometry and additive SI reference rates;
4. then evaluate the robust `u` interval and combine it with `(v,z,delta)`.

If no defensible apparatus data exist, keep the result parametric and shift effort to manuscript synthesis/literature audit rather than inventing numbers.

## 13. Reproducibility

Run

`python analysis/detector_rate_bracket_iteration121.py`.

The script verifies the detector-time ordering, `u` interval construction, common-rate homogeneity and the NG-079 decision guard on a dimensionless regression.
