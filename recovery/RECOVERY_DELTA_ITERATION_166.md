# RQIR Candidate Gravity — Recovery Delta Iteration 166

**Date:** 2026-08-31  
**Authoritative predecessor:** Iteration 165  
**MODEL_READINESS:** 24% (unchanged)

## What changed

Iteration 165 closed the 12-row spacelike ordered-TT sector by showing that a target-independent local C5 cubic subset through the already frozen dimension-12 cutoff has rank 12/12. Iteration 166 therefore changes **observable type**, not merely the number of spacelike rows.

A new target-independent timelike causal pre-protocol is frozen:

`A_odd(s)=[Im chi_R(+omega)-Im chi_R(-omega)]/(2*pi)`, `s=omega^2>0`.

Eight benchmark values are

`s_i=0.004*i`, `i=1..8`.

All are below the frozen dRGT TT pole `m^2=0.04`.

## New exact/scoped result

For any real local Hermitian tree EFT contribution evaluated away from isolated poles,

`A_odd^local-tree=0`.

Thus the finite local-polynomial interpolation mechanism that saturated Iterations 163–165 cannot saturate this absorptive block, no matter how many local tree Wilson coefficients are added.

Retain:

`C5-NG-004 — LOCAL_HERMITIAN_TREE_EFT_CANNOT_SATURATE_OFF_POLE_ABSORPTIVE_BLOCK`.

## C5 positive control

A leading massless-loop logarithm with

`K_R=s[1+ell*s*log(-s-i0)]`

gives

`d chi_R/d ell=-log(-s-i0)`

and normalized

`A_odd=1`.

The eight-row leading-log rank is 1. A stress-test basis `x^n A_odd`, `n=0..3`, has rank 4 with condition number about 165.

This demonstrates nonanalytic observable capacity; it is not a four-parameter C5 loop claim.

## New Lorentzian asymptotic-safety comparator

Created:

`candidate_gravity/comparators/AS-LOR-SPEC-002.md`.

Primary authority: Pawlowski, Reichert, Wessely, arXiv:2507.22169 (2025), supported by Fehre et al., arXiv:2111.13232.

Published IR structure:

`G_hh^ph=z_spec^-1[1/p^2-A_h log(p^2)+...]`,

`A_h=61/(60*pi)=0.32361505095352056`,

`z_spec~=1.486`.

The leading AS IR absorptive shape is constant and therefore collinear with the C5 massless-loop logarithmic direction after gain profiling:

`rank([C5_log,AS_IR])=1`,

normalized residual `1.715e-16`.

Retain:

`AS-NG-004 — LORENTZIAN_AS_LEADING_IR_LOG_IS_COLLINEAR_WITH_C5_MASSLESS_LOOP_SHAPE`.

## New funnel rules

`NG-FUNNEL-024 — ABSORPTIVE_NONANALYTICITY_ESCAPES_LOCAL_TREE_INTERPOLATION_BUT_NOT_QUANTUM_COMPARATOR_SUBTRACTION`.

`NG-FUNNEL-025 — BARE_TT_SPECTRAL_COEFFICIENT_IS_NOT_YET_A_SOURCE_COMPLETED_RQIR_OBSERVABLE`.

The second rule is mandatory because the published AS coefficient belongs to a particular TT fluctuation-field/gauge/normalisation convention. It may not be substituted directly for the final conserved-source/detector response.

## Comparator state in the new block

- C5 local tree: supported zero absorptive off pole.
- C5 massless log: supported nonzero leading shape; exact source-completed amplitude still blocked.
- C4 dRGT tree: supported zero on chosen below-pole rows; loops/matter/helicity completion blocked and never zero-filled.
- C3 tree EH boundary: supported zero off pole; diffusion/MSR ordered corrections blocked.
- entire-form-factor nonlocal tree: no form-factor branch cut scoped; full CTP/loop completion blocked.
- AS Lorentzian: continuum and leading IR log supported; source-completed finite-frequency RQIR map blocked.

## Candidate state

No unique Candidate Gravity residual.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

Readiness remains 24% because the new sector improves/narrows comparator coverage but does not yet close the common source-completed absorptive quotient.

## Iteration 166 authorities

- `analysis/timelike_absorptive_protocol_iteration166.py`;
- `results/timelike_absorptive_protocol_iteration166.json`;
- `candidate_gravity/TIMELIKE_ABSORPTIVE_PROTOCOL_ITERATION166.md`;
- `candidate_gravity/comparators/AS-LOR-SPEC-002.md`;
- this recovery delta.

## Exact next gate — Iteration 167

1. Build a conserved-source/source-completed timelike transfer rather than a bare TT propagator coefficient.
2. Derive the leading C5 massless-loop nonanalytic column in that same convention, with source/vertex pieces required for gauge invariance.
3. Map `AS-LOR-SPEC-002` into the same normalized source response.
4. Search only for a **sub-leading frequency dependence after the universal constant-log direction is projected out**.
5. Do not create ANSATZ-003 unless a residual survives all supported comparator directions and blocked sectors are either instantiated or shown irrelevant by a theorem-level argument.
