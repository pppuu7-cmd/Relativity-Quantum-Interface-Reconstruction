# RQIR Recovery Delta — Iteration 125

**Date:** 2026-08-31  
**Parent front:** Iteration 124.

## Canonical Paper-III notation

Freeze

`F_*=Z_final^2`,

`F_final=A_raw C_src/(A_raw+C_src)`.

At fixed retained fraction `r`:

`A_raw=F_*/r`,

`C_src=F_*/(1-r)`.

For final `Z_final=5`, `r=.9`:

`A_raw=27.7777777778`, `C_src=250`, `F_final=25`.

### NUM-008

Historical `A_raw=25`, `C_src=225` remains a raw-5-sigma / 90%-retention regression only. It gives `F_final=22.5`, `Z_final=4.74341649`; do not present it as final 5 sigma.

Canonical architecture variables remain

`u=R_D14/R_D09`, `v=R_A14/R_A09`, `z=R_A09/R_D09`, `delta=(1-d14)/(1-d09)`.

Use `d_g` for differential transfer gain in manuscript prose to avoid collision with duty `d`.

### CAL-025

Do not renumber historical iteration aliases. Preserve provenance and use the named late-front authority/dependency map for manuscript claims.

## Files

- `analysis/paper3_notation_dependency_audit_iteration125.py`
- `docs/PAPER_III_NOTATION_DEPENDENCY_AUDIT_ITERATION125.md`
- `research_log/2026-08-31_iteration_125_notation_dependency_audit.md`
- this recovery delta.

## Readiness snapshot

- Paper III scientific-content readiness: **97%**.
- Paper III submission readiness: **89%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **86%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Next gate

Build the Paper-III reproducibility manifest with one canonical command/expected invariant per manuscript-bearing result, then perform the final literature/priority audit. Apparatus-specific numerical closure remains conditional and is not required for Paper-III scientific closure.
