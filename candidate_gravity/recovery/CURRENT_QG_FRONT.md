# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 290**

## Current scientific state

Iterations 278–286 established translation-closed timelike C5 support, canonical raised bubble/triangle sectors and complete actual-oracle numerator reconstructions. Iteration 287 reduced both hard raised bubbles to nonzero coefficient-level DR results. Iteration 288 reduced all three complete raised-triangle numerators, and Iteration 289 corrected the naive finite extrapolation by a Laurent audit.

The current scoped same-parent triangle block has a robust common-cut pole

`A_B3 = -0.061289813814603585`,

with scalar-calibration pole residues below `6.1e-8`. Therefore the finite diagnostic triangle/bubble sums are not yet physical C5 coefficients.

Freeze retained from Iteration 289:

`PASS_DETECTED_ROBUST_UNCANCELLED_TRIANGLE_COMMON_CUT_IR_POLE__FINITE_COEFFICIENT_BLOCKED`.

## Iteration 290 — B3/source IR interface authority map

The existing MSSC-001 source sector already has a physical connected-cut IR factorization

`R_in = R_out = -8 M_Born`

from Iteration 222. It cannot be subtracted directly from `A_B3`.

Reason: the two residues belong to different objects/conventions. The current `B3` pole is a scoped off-shell/1PI Vilkovisky same-parent contribution before source/Ward/contact completion, whereas the `-8 M_Born` relation is an on-shell connected scalar+graviton source-cut result in the stripped Iteration-219/221 normalization.

The same MSSC-001 parent action fixes the off-shell Ward identity

`k_mu V^{mu nu} = (p'^2-m^2)p^nu - (p^2-m^2)p'^nu`.

Thus the longitudinal off-shell completion is tied to inverse scalar propagators and nonlinear contact terms; these EOM contributions vanish on shell and cannot be inferred from the on-shell Born-factorizing residue alone. This preserves the Iteration-217 non-identifiability boundary.

Freeze:

`PASS_SOURCE_IR_INTERFACE_AUTHORITY_MAP__B3_POLE_ORIGIN_STILL_BLOCKED`.

The pole must be separated into:

- A: Ward/EOM/source-convention pole — cancel/remove in linked/source completion;
- B: physical universal gravitational IR factor — need not vanish; subtract only in the matched physical connected observable using the frozen Born/inclusive prescription;
- C: finite transverse hard remainder — only this is eligible for comparator-coordinate promotion.

Current data do not identify whether `A_B3` is A, B, or a mixture.

## Current C5 blocker

`BLOCKED_POLE_LEVEL_LINKED_K2_SOURCE_WARD_CONTACT_COMPLETION_IN_SAME_CONVENTION`.

The frozen linked target remains

`T_cut = D Gamma3_ret,soft - W[D K2]`.

No additional finite master extraction is authoritative until the `1/epsilon` coefficient of the linked `W[D K2]` plus MSSC-001 source/contact completion is derived in the same convention as `B3`.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 289: **0 percentage points**. The source/IR interface is now authority-clean, but no new readiness-rubric block is closed.

## Retained guardrails

- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not reintroduce box masters from unclosed routing.
- Apply loop shifts/reflections to primitive numerators before sector summation.
- Do not use the superseded denominator-only 9/50 bases.
- Do not use Iteration-288 ordinary polynomial epsilon extrapolations as finite triangle coefficients.
- Do not promote diagnostic finite Laurent terms before pole classification/completion.
- Do not subtract `-8 M_Born` from the current `B3` residue without an explicit observable/normalization map.
- Do not require a physical Born-factorizing gravitational IR pole to vanish merely because the partial 1PI block must be completed.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 290 authority files

- `candidate_gravity/results/iteration290_b3_source_ir_interface_audit.json`
- `candidate_gravity/C5_B3_SOURCE_IR_INTERFACE_ITERATION290.md`
- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_290.md`
- `research_log/2026-09-03_iteration_290_b3_source_ir_interface.md`

## Exact next gate — Iteration 291

1. Construct the pole-level linked quantity `T_cut = D Gamma3_ret,soft - W[D K2]` in one parameter and normalization convention.
2. Derive the `1/epsilon` coefficient of the same-parent `W[D K2]` term and every MSSC-001 source/contact term fixed by the parent action.
3. Test the Ward/EOM pole sum against `A_B3 = -0.061289813814603585` before computing finite terms.
4. If a residual pole survives, determine whether it factorizes onto the matched physical Born amplitude; only then apply the already frozen source hard-remainder prescription.
5. Only a finite transverse remainder after A/B separation may enter the C5 comparator quotient.
6. `ANSATZ-003`, Fisher/resources and blind heavy full-C5 remain forbidden.
