# RQIR Candidate Gravity Recovery Delta — Iteration 367

Date: 2026-09-04

MODEL_READINESS: 24%

## Starting authority

Validated scientific authority entering this closure was Iteration 366. Fresh Actions state also showed that Iteration 364 run `33801351823` had ended `completed/cancelled` during the scientific step, with no sentinel/schema audit and no artifact. Therefore Iteration 364 has **no scientific PASS/FAIL authority** and its 48 cut-through-double-pole channels remain unresolved. The cancelled heavy run must not be blindly duplicated.

## Scope

Re-audit the historical Iteration-310 singleton-soft pruning premise for `Tr U1^2` on the current matched timelike common-background fixture. This gate tests only whether the first-order singleton `U1` block that was historically killed on the null-soft fixture remains zero after the physical timelike rebase. It does not perform the full 42-placement contraction and does not perform a cut integral.

## Validated authority

- workflow: `rqir-iteration367-tru1sq-timelike-singleton-pruning-reaudit`
- run: `33806321673`
- head commit: `19e7080aff61beac11a7bf6c9fa5366024724600`
- artifact: `9913046693`, `iteration367-result`
- artifact digest: `sha256:4361ce81fb2be3863b030a4eab5a686c69aceeab0160b229d307353031393e50`
- raw scientific JSON SHA-256: `e71b895495d3e00187372430427895e56423ea1be576991cb99e5fdd6f35f87d`
- exactly one top-level JSON object; sentinel `367`; `scientific_authority_pass=true`.

Freeze:

`PASS_TRU1SQ_TIMELIKE_REBASE_INVALIDATES_OLD_SINGLETON_SOFT_PRUNING__FULL_PREPRUNING_PHYSICAL_ROUTING_REQUIRED`

## Scientific result

The historical null-soft negative control reproduces the intended vanishing scale:

- null-soft singleton `s`: `||U1^(1)[s]||_F = 4.172141756553574e-16`.

On the current timelike common-background fixture the same singleton sector is decisively nonzero:

- `q_s^2=-1`: `||U1^(1)[s]||_F = 0.5850412233520722`;
- `q_a^2=-0.14`: `||U1^(1)[a]||_F = 0.2519141158697874`;
- `q_b^2=-0.34`: `||U1^(1)[b]||_F = 1.2355711687033575`.

For the crucial timelike `s` singleton, the margin over the frozen nonzero threshold `1e-6` is `585041.2233520722`. The three-step derivative scan has relative spread `9.488417057724452e-16`; independent two-point versus five-point derivative agreement has relative error `7.760065778909101e-10`, well below the frozen `2e-4` tolerances. Momentum closure is exact at stored precision and maximum q2 fixture error is `5.551115123125783e-17`.

## Interpretation

The physical timelike rebase **invalidates** the Iteration-310 singleton-soft pruning premise. Therefore the historical reduction

`42 raw ordered placements -> 16 survivors -> 8 cyclic classes`

is not physically transferable to the current timelike fixture. The old eight classes are retained only as historical null-soft authority and may not be used for the physical `Tr U1^2` computation.

This is a scoped negative pruning/quotient result, not a Candidate Gravity consistency FAIL, not an exact comparator identity, not regime-specific non-identifiability, not near-degeneracy and not a novelty certificate.

## Exact next gate

Rebuild physical `Tr U1^2` from the full **42 pre-pruning ordered placements** on the current timelike fixture. For every placement, evaluate the same-parent `U1=N_L V2 N_R Y` first- and second-background blocks with exact cumulative incoming momentum. Only after executable route-by-route contraction authority is established may cyclic trace equivalence be applied; reversal quotient is forbidden unless separately proved. No cut integration before this routing/contraction gate passes.

In parallel, the unresolved 48 cut-through-double-pole `Tr U2` channels require a targeted reduced/isolated-channel replacement for cancelled Iteration 364, not a blind duplicate.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 366: `0 pp`. A false historical pruning shortcut has been removed and the physical `Tr U1^2` starting set is now correctly fixed, but no complete readiness-rubric bucket and no robust comparator-subtracted residual have closed. `ANSATZ-003` remains uncreated and Fisher/resources remain forbidden.

Authoritative iteration: 367.
