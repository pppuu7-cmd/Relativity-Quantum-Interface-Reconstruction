# RQIR Candidate Gravity — Iteration 367

Date: 2026-09-04

MODEL_READINESS: 24%

## Starting authority

Repository scientific authority at the start of this closure was Iteration 366. Fresh Actions state superseded one stale operational line in `CURRENT_QG_FRONT`: Iteration 364 run `33801351823` had ended `completed/cancelled` during its scientific step and produced no artifact, so it has no scientific PASS/FAIL authority.

## Scientific question

Does the historical Iteration-310 singleton-soft pruning premise remain valid after rebasing `Tr U1^2` onto the current matched timelike common-background fixture?

The gate uses the same-parent finite-geometry `V2` construction, two independent derivative stencils and a step scan. The old null-soft fixture is retained as a negative control. No full 42-placement contraction and no cut integration are performed here.

## Validated result

Workflow run `33806321673` completed successfully. Artifact `9913046693` (`iteration367-result`) has digest `sha256:4361ce81fb2be3863b030a4eab5a686c69aceeab0160b229d307353031393e50`. Authority audit reports exactly one top-level JSON object, sentinel `367`, `scientific_authority_pass=true`, with raw scientific JSON SHA-256 `e71b895495d3e00187372430427895e56423ea1be576991cb99e5fdd6f35f87d`.

Historical null-soft control:

`||U1^(1)[s]||_F = 4.172141756553574e-16`.

Current timelike fixture:

- `q_s^2=-1`: `||U1^(1)[s]||_F = 0.5850412233520722`;
- `q_a^2=-0.14`: `||U1^(1)[a]||_F = 0.2519141158697874`;
- `q_b^2=-0.34`: `||U1^(1)[b]||_F = 1.2355711687033575`.

For the decisive timelike `s` singleton, the nonzero margin over the frozen `1e-6` threshold is `585041.2233520722`. Step-scan relative spread is `9.488417057724452e-16`; two-point versus five-point derivative relative error is `7.760065778909101e-10`, both far inside frozen tolerances. Maximum q2 fixture error is `5.551115123125783e-17`.

## Classification

`PASS_TRU1SQ_TIMELIKE_REBASE_INVALIDATES_OLD_SINGLETON_SOFT_PRUNING__FULL_PREPRUNING_PHYSICAL_ROUTING_REQUIRED`

This is a scoped negative result for transferability of the historical pruning shortcut. It is not Candidate Gravity consistency FAIL, not exact comparator identity, not regime-specific non-identifiability, not near-degeneracy and not a novelty certificate.

## Consequence

The historical physical-looking reduction `42 -> 16 -> 8 cyclic classes` is invalid on the current timelike fixture. Physical `Tr U1^2` must restart from all 42 pre-pruning ordered placements. Cyclic trace quotient may be applied only after route-by-route physical contraction authority is established; reversal quotient remains forbidden unless separately proved.

Iteration 364's operational timeout is kept distinct from this scientific result. Its 48 cut-through-double-pole `Tr U2` channels remain unresolved and must be attacked by a targeted reduced/isolated strategy rather than a blind rerun.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 366: `0 pp`. The iteration removes an invalid physical shortcut and correctly fixes the `Tr U1^2` starting space, but no complete stable readiness bucket and no robust comparator-subtracted residual have closed.

## Exact next gate

Construct executable physical routing/contraction authority for all 42 pre-pruning `Tr U1^2` ordered placements on the same timelike fixture, using `U1=N_L V2 N_R Y` with exact cumulative incoming momenta. Only then quotient by proven cyclic trace identities and classify numerator/denominator families before any cut integration.
