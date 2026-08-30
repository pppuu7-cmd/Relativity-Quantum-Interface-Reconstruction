# RQIR Research Log — Iteration 125

**Date:** 2026-08-31

## Question

Can Paper III freeze one internally consistent manuscript notation and dependency chain without rewriting historical calculations or confusing the old raw-5-sigma `C_src=225` benchmark with a final-5-sigma target?

## Result

Yes.

Canonical final-significance notation is now:

`F_*=Z_final^2`,

`F_final=A_raw C_src/(A_raw+C_src)`.

At fixed retention `r`,

`A_raw=F_*/r`, `C_src=F_*/(1-r)`.

Thus final `Z=5`, `r=.9` requires

`A_raw=27.7777777778`, `C_src=250`.

The old `(25,225)` pair remains a valid raw-5-sigma / 90%-retention regression and gives `Z_final=4.74341649`.

Registered **NUM-008**: Paper III must not call `225` a final-5-sigma certificate.

The manuscript rate symbols and architecture variables `(u,v,z,delta)` are frozen, and differential transfer gain is renamed locally to `d_g` in prose to avoid collision with duty `d`.

Registered **CAL-025**: historical iteration aliases are preserved as provenance; do not renumber old commits. Manuscript authority follows the named late-front dependency map.

The existing regression script `analysis/paper3_notation_dependency_audit_iteration125.py` reproduces the final-significance bookkeeping and architecture-variable identities.

## Readiness snapshot

- Paper III scientific-content readiness: **97%**.
- Paper III submission readiness: **89%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **86%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Next gate

Create the minimum manuscript reproducibility manifest with command, expected invariant, dependency and claim-class metadata for every manuscript-bearing numerical result. Then run the final literature/priority audit before scientific closure.
