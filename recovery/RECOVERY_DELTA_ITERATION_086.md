# RQIR Recovery Delta — Iteration 086

**Date:** 2026-08-30  
**Authority:** read after `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, and Iterations 081–085.

## What changed

Iteration 086 audits the correlated two-band law from Iteration 085 and corrects an over-strong interpretation of the weak-band asymptote.

Base law retained:

`R_beta = 4 r2 r4/(r2+r4+2 rho_eff sqrt(r2 r4))`, `|rho_eff|<1`.

The limit

`r_partner -> infinity => R_beta -> 4 r_weak`

is correct for every finite `|rho_eff|<1`.

However it is **not** a global ceiling when `rho_eff<0`.

## New retained result — RQIR-CORR-001

Fix `r_weak=b` and vary the partner rate.

- For `rho_eff>=0`, `R_beta` grows monotonically and has supremum `4b`.
- For `rho_eff<0`, the finite optimum is

`r_partner/b = 1/rho_eff^2`,

with

`R_beta,max = 4b/(1-rho_eff^2)`.

Explicit counterexample to the old global reading:

`rho=-0.5`, `b=1`, `r_partner=4` gives `R_beta=16/3>4`.

Therefore the correlated-band blanket requirement `r_n>R_*/4` is withdrawn for negative correlation.

Correct optimized weak-band floor:

- `b >= R_*/4` for `rho>=0`;
- `b >= (1-rho^2)R_*/4` for `rho<0`.

At fixed total raw rate `r2+r4`, balance `r2=r4` remains optimal for all ordinary `|rho|<1`.

## Guardrail

The enhancement `4/(1-rho^2)` becomes large near `rho=-1`, but that is the singular covariance boundary. Any apparatus claim exploiting strong anti-correlation must propagate cross-PSD uncertainty, covariance conditioning/eigenvalue floor, and campaign stability; use a reduced likelihood at true rank deficiency.

## Reproduce

- `analysis/correlated_partner_optimum_iteration086.py`
- `docs/PAPER_III_CORRELATED_PARTNER_OPTIMUM_ITERATION086.md`
- `research_log/2026-08-30_iteration_086_correlated_partner_optimum.md`

## Next admissible gate

Use the corrected full `(r2,r4,rho_eff)` geometry with uncertainty intervals. Derive a conservative lower bound on `R_beta` from a declared two-band spectral matrix uncertainty set before inserting an external/apparatus PSD into the Paper-III wall-clock certificate.
