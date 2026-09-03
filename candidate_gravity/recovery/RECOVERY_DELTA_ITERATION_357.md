# Recovery Delta — Candidate Gravity Iteration 357

Date: 2026-09-03

## Scope

Freeze the fail-closed cut-method split for the 42 physical U2 families already distinguished by Iterations 355-356. This gate does not integrate a discontinuity.

## Raw Actions authority

- authoritative run: `33789235049`
- job: `100761488578`
- artifact: `9906649986` (`iteration357-result`)
- artifact digest: `sha256:3be8fe0a2b1762a9965adab669a422157db77226dc33e52c4e1287d9d0d4a2e8`
- scientific JSON SHA-256: `71d775d456527a0ebad19f08aae36872e3602884cd1a85b5f8379911daff0918`
- workflow head: `38826d8383880ef7a1adc3b79dd7315529366438`

The raw artifact contains exactly one Iteration-357 object and `scientific_authority_pass=true`.

## Result

Authority:

`PASS_U2_SIMPLE_VS_REPEATED_POLE_CUT_CONTRACT__12_SIMPLE_FAMILIES_NEXT__30_REPEATED_FAMILIES_DISTRIBUTIONAL_BLOCKED`.

Census:
- total physical families: `42`;
- ordinary-simple-cut families: `12`;
- typed ordinary-simple timelike pair channels: `36`;
- repeated-pole families: `30`;
- typed repeated-pole timelike pair channels: `114`.

The 12 simple-distinct-pole families may proceed to ordinary two-particle cut diagnostics. The 30 repeated-pole families are **operationally/methodologically BLOCKED for ordinary simple Cutkosky substitution**, not zero and not a consistency FAIL. They require an explicit derivative/distributional (or analytically equivalent) repeated-pole reduction before any discontinuity value can be certified.

This result does not claim a nonzero U2 discontinuity, comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate.

## Exact next gate

For only the 12 ordinary-simple families, evaluate numerator-on-shell regularity and the separation/nonvanishing of every uncut denominator on each of the 36 typed timelike pair channels. Assign each channel `REGULAR`, `ZERO`, or `BLOCKED` before performing normalized integration. Keep all 30 repeated-pole families separate and BLOCKED pending a dedicated repeated-pole derivation.

MODEL_READINESS: 24%

Change from Iteration 356: `0 pp`. The cut-method contract closes a real hard prerequisite but no complete readiness-rubric bucket and no robust comparator-subtracted residual are closed.
