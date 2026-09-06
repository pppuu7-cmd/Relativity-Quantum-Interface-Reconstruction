# Recovery Delta — Iteration 514

**MODEL_READINESS: 24%**  
**Infrastructure: 100%**

## New exact assembly/error authority
Frozen central4 support geometry from Iteration 508 gives exact row L1 norms in units of `1/h^2`: `BASE=9/4`, `HALF=9`, union-aggregated `BASE-HALF=397/36`.

For arbitrary coordinate perturbations with only `|e_i| <= epsilon`, the deterministic induced bounds are:

- `|delta BASE| <= (9/4) epsilon / h^2`,
- `|delta HALF| <= 9 epsilon / h^2`,
- `|delta(BASE-HALF)| <= (397/36) epsilon / h^2`.

Ignoring shared-node aggregation would give the looser coefficient `45/4`; exact four-node cancellation reduces it by `2/9`, with union/separate ratio `397/405` and relative reduction `8/405`.

Classification: `PASS_BASE_HALF_DETERMINISTIC_LINF_ERROR_OPERATOR_BOUND_EXACT__NON_PROMOTING`.

Reproducible audit: `candidate_gravity/code/iteration514_base_half_deterministic_error_operator_bound.py`. Result: `candidate_gravity/results/iteration514_base_half_deterministic_error_operator_bound.json`.

This is distribution-free absolute numerical-error provenance only. It does not convert local scaled MP discrepancies into assembled scaled discrepancies absent a common absolute normalization, does not create or weaken a threshold, and does not promote physical/model authority.

## Retained numerical front
Latest completed mass-support authority remains Iteration 513: raw-valid rank23 `(u,v)=(+2.5e-6,-2.5e-6)` with certified occurrence-weighted support `28/32 = 87.5% = 2240/2560`.

Canonical rank24 `(u,v)=(+2.5e-6,+2.5e-6)`, HALF local index 10, multiplicity 1, run `34063351852`, job `101567716622`, remains `in_progress`. No duplicate run was launched.

## Retained blockers/nonclaims
Physical/operator authority: Iteration 411. Raw-valid physical blocker: Iteration 421 `BLOCKED_CONVERGENCE`, unresolved set `[2]`. Comparator quotient remains operationally BLOCKED because its concrete upstream target is not assembled. No consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or novelty certificate is inferred from that BLOCKED state. Robust comparator-subtracted residual remains absent; `ANSATZ-003` remains uncreated; Fisher/resources remain forbidden.

Readiness change: **0 percentage points**. The new result closes an exact numerical assembly/error subgate only.

## Exact next gate
Fail-closed raw-consume rank24 run `34063351852` after completion. Only raw-valid PASS permits frozen rank25 `(+2.5e-6,+5e-6)`, HALF local index 11, multiplicity 1. BLOCKED freezes suffix progression and requires first-failing `z/phi/radial` localization under unchanged frozen dynamics, support order, thresholds, MP levels, radial hs, and angular grid.
