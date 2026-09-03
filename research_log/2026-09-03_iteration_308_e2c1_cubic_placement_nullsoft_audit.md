# RQIR Candidate Gravity — Iteration 308

Date: 2026-09-03

MODEL_READINESS: 24%

## Starting authority

Repository authority at launch was ahead of the stale `CURRENT_QG_FRONT`: Iteration 307 had already frozen the complete eight-family `e=1,c=2` weight-completed `Tr U1` normalized cut at the frozen timelike row,

`D_s TrU1[e=1,c=2] = -0.5157080054161807`,

with fitted combined cut `1/epsilon` residue `1.2896746939995822e-09`. Iteration 308 code/workflow commits were present but had not yet been promoted into recovery/front authority.

The Iteration-308 Action `33703692659` completed successfully and, unlike the rejected original Iteration-296 artifact, passed the fail-closed authority validator: exactly one top-level JSON object, sentinel `308`, scientific JSON SHA-256 `7623aa20ab729d2fe13a3da8f8d464431d32fc431b042c94a712a169f125db5b`.

## Scientific question

Before evaluating the remaining connection `e=2,c<=1` sector, enumerate the complete cubic-background-order placement classes of

`+(i/2) Tr U2 -(i/4) Tr U1^2`

using only the already-authoritative operator order

`U1 = N_L V2 N_R Y`,

`U2 = N_L V1_L H V1_R N_R Y`,

and prune only those rows that vanish by the exact singleton null-soft rule `E^(1)[h_s]=0`.

## Exact result

For `Tr U2`, cubic background order requires one additional insertion on one of the six ordered sites. Full distinct-leg enumeration gives 30 ordered primitive placements. Exactly 18 are killed because a linear `V1` receives the singleton soft leg. Twelve survive. The survivor census is uniform: two survivors for each extra site `N_L`, `V1_L`, `H`, `V1_R`, `N_R`, `Y`.

For `Tr U1^2`, one `U1` block is first background order and one is second background order. The ordered enumeration contains 42 primitive placements. Exactly 26 are killed by a singleton soft leg on a linear `V2`. Sixteen ordered placements survive. Cyclic trace equivalence identifies these into exactly eight cyclic classes. The surviving second-order extra-site census is four each for `V2`, `N_L`, `N_R`, `Y`.

The pruning is deliberately narrow: mixed quadratic soft-hard vertices such as `V1^(2)[h_s,h]` and `V2^(2)[h_s,h]` are retained and are not zero-filled.

## Classification

`PASS_E2C1_CUBIC_BACKGROUND_PLACEMENT_AND_NULLSOFT_PRUNING_AUDIT__EXACT_V1_H_KERNEL_IMPLEMENTATION_REMAINS`

This is an exact combinatorial/operator-placement certificate, not a Candidate Gravity consistency PASS, not an exact comparator identity, not a near-degeneracy result, and not a novelty certificate.

## What remains blocked

The 12 surviving `U2` rows cannot yet be evaluated without deriving the exact same-parent `V1-H-V1` index kernel in the frozen pure-Einstein convention, including `H0` and the required first-background variations (`H1`, `V1_2`, plus already-existing `N1/Y1` infrastructure). No blind heavy contraction is authorized.

The 8 cyclic `Tr U1^2` classes can reuse the existing authoritative U1 primitive machinery after their placement/routing contract is frozen.

## Readiness

MODEL_READINESS: 24%

Change from previous assessment: 0 pp. Comparator foundation remains 24/25 and robust unique residual remains 0/20. Iteration 308 closes an exact e2c1 placement/pruning prerequisite but does not yet close any stable readiness-rubric block.

## Exact next gate

Derive and freeze the primary Vilkovisky `U2` index formula into an executable same-parent `V1-H-V1` kernel. Explicitly map index spaces, transposes, `H0`, and first-background `H1/V1_2` terms for the 12 surviving placements before evaluating numerators. In parallel, map the 8 cyclic `Tr U1^2` classes onto the already-frozen U1 primitive kernels. Only after these exact operator contracts pass trace/transpose/routing checks may scoped numerator reconstruction begin.
