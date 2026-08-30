# RQIR Research Log — Iteration 096

**Date:** 2026-08-30  
**Track:** Paper III physical resources / robust apparatus characterization.

Started from authoritative Iteration 095.  No GitHub Actions runs were active and no closed computation was duplicated.

## New retained results

- **RQIR-RESOURCE-048:** for an uncertainty coordinate with Iteration-094 local leverage `Lambda`, current scale `h`, and independent characterization Fisher rate `R_char`, the local fractional unresolved-band shrink rate is

  `Xi = 0.5 Lambda R_char h^2`.

  Architecture-characterization priority therefore depends on decision leverage **and** physical characterization throughput.

- **RQIR-NG-049:** the largest raw decision leverage is not automatically the best measurement per characterization second.  A lower-leverage coordinate wins if its normalized characterization speed `R_char h^2` is sufficiently larger.

- **RQIR-RESOURCE-049:** with uncertainty floor `h_f`,

  `T_char = [1/(h1^2-h_f^2)-1/(h0^2-h_f^2)]/R_char`.

  Targets at or below the floor are impossible.  With zero floor, halving an uncertainty costs `3/(R_char h0^2)`.

## Regression

Using the synthetic Iteration-094 box only as an algebraic test, equal `R_char h^2` reproduces the old ranking.  Toy014 aggregate `A` overtakes Toy014 `R_src` in per-second characterization value once its normalized characterization speed is `>2.866505...` times larger, proving the ranking can reverse without changing the architecture likelihood.

## Interpretation

Iteration 095 supplied primitive derivatives but not the physical rate at which each primitive uncertainty can be reduced.  The actual highest-value characterization measurement is therefore underdetermined until `(h, R_char, floor, duty/cost)` or a joint characterization Fisher model is supplied.

This is the characterization analogue of the earlier transition from abstract `C_a,gamma` to physical Fisher rates.

## Next

Derive the finite-time optimal allocation across multiple characterization channels with diminishing Fisher returns, then apply it to a declared Toy009/Toy014 primitive uncertainty envelope.  Keep NG-048 active at nonsmooth branch/eigenvalue/corner changes.  Do not start Toy015 yet.
