# RQIR research log — Iteration 269

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Follow-up to the newly committed routed `N/Q` layer (Iteration 268). A direct endpoint-reversal test showed `N1/Q1` transpose residuals near `1e-10` but `N2/Q2` residuals of order `1e-2` to `1e-1`. The mismatch was localized below `A/B3` and traced to the explicit density representative used when converting the minimal ghost matrix to the orbit metric.

Primary-authority audit of Giacchini–de Paula Netto–Shapiro (2020), Eqs. (5), (14), (48), (53), fixes

`Y^up = g^-1/sqrt(|g|)`,

`Y_down = sqrt(|g|) g`,

up to the frozen common sign. Thus `N_orb=Y_down Nhat`.

For TT `g=eta+t eps`, the correct second-order single-mode coefficient is

`V2=-(tr(H^2)/4) eta`,

not the `+` sign inherited from Iteration 258. First order remains unchanged because `delta sqrt(|g|)=0` for TT.

With the corrected factor, routed physical `N2/Q2` endpoint-transpose residuals fall to the finite-difference envelope (`<=4.49e-8` for Q2 at h2=2e-4), while exact routed inverse identities remain at machine precision (`<=4.45e-16`). The superseded density factor leaves N2 transpose residuals `0.03165`, `0.21036`, `0.62805` under the same tests.

Freeze `PASS_PRIMARY_AUTHORITY_ORBIT_DENSITY_CORRECTION_AND_ROUTED_N2_Q2_TRANSPOSE_RESTORATION`.

Supersede only the density representative in Iteration 252 and second-order `Norb2/Q2` numerical values in Iterations 258/259/268. Retain their first-order results, exact factorization, inverse-recursion algebra and Fourier-routing logic.

No Candidate Gravity residual. Heavy integration, Fisher/resources and `ANSATZ-003` remain forbidden. Next gate: recompute routed physical `A1/A2/A3`, then all 8 independent `B3` representatives and endpoint-reversed partners using corrected Q2.
