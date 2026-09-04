# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity physical/operator authority:** **Iteration 411**  
**Latest validated structural authority:** **Iteration 410**  
**Latest validated numerical-method diagnosis:** **Iteration 415**  
**Latest prospective methodological authority:** **Iteration 420**

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Green/red workflow colour alone is never scientific authority.

## Authoritative state

### Determinant `e=0,c<=3`

- Iteration 383 closes the ordinary-two-simple-particle determinant absorptive vector: `q^2=-1 -> -0.002357789063884683 i`, `q^2=-0.34 -> +0.001462759351572654 i`, `q^2=-0.14 -> +0.0012389565044298413 i`.
- Iteration 387 preserves the evanescent/R2 warning: the hard-branch discontinuity is valid but the full finite local/rational DR remainder remains BLOCKED. This is not a Candidate residual.

### Timelike `Tr U2` — COMPLETE OPERATOR COORDINATE

- Iteration 366 repeated-family simple-simple sector is closed 18/18.
- Iteration 392 freezes the exact 48-channel topology mask; empty-uncut `+Infinity` is allowed only on indices `[4,13,22,27,28,29,30,33,36,39,42,45]`.
- Iteration 405 raw-validates exact 48/48 repeated-cut assembly: run `33832181526`, artifact `9922054102`, digest `sha256:1dd9bbc6c863954059263171c5a160510ce3605bb416a46498c3453b48343729`, result SHA-256 `f766c6641fb9a89838784ae7572fa1f8459dd0260fd71007f8de93e727840cab`.
- Iteration 406 complete timelike coordinate, still before `+i/2`: `q^2=-1 -> +0.0005345424186332474`, `q^2=-0.34 -> -0.000734101259784574`, `q^2=-0.14 -> -0.001572666890130343`.
- Iterations 416/417 do **not** reopen this authority: both independent null-soft-current re-audits suffered post-science raw-output parsing/audit failures (`JSONDecodeError: Extra data`). They are operational/audit failures, not scientific FAILs and not new authority.

### Timelike `Tr U1^2`

- Frozen census: Iteration 372 has 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`.
- Iteration 374 closes 6/6 simple-simple: `[-1:+6.253219881951187e-05, -0.34:+3.5044107116946374e-05, -0.14:+2.9297648005638963e-05]`.
- Iteration 393 closes all 36 simple-double: `[-1:-0.002329411286740447, -0.34:-0.0005948791870822445, -0.14:-7.368142632096214e-05]`.
- Iteration 399 closes double-double index 5 / class 8 / `q^2=-0.14`: `D_s TrU1^2=+0.000119747535002548`, scaled error `1.8393013149631406e-7`.
- Iteration 403 proves exact central4×central4 auxiliary-mass stencil commutation with the sphere mean as a finite linear combination.
- Iteration 409 raw-closes index 4 / class 5 / `q^2=-1`: run `33835806522`, artifact `9924759934`, authoritative `D_s TrU1^2=+0.003562716046166582`, mass-step error `1.694511628814576e-05 < 2e-05`, direct original-integrand cross-check `2.0657185788308663e-09 < 2e-06`.
- Iteration 410 raw-validates structural oracles for blockers 2 and 11.
- Iteration 411 raw-closes index 11 / class 16 / `q^2=-0.34`: run `33851983789`, artifact `9931076355`, authoritative `D_s TrU1^2=+0.013050543643260309`, mass-step error `5.421327239850046e-06 < 2e-05`, direct cross-check `1.1526331104849685e-12 < 2e-06`.
- Iteration 411 index 2 / class 3 / `q^2=-1` remains `BLOCKED_CONVERGENCE`: artifact `9930938547`, mass-step discrepancy `5.0042074065288766e-05 > 2e-05`; diagnostic value is not authority.
- **Exact unresolved double-double physical set: `[2]`.** No blind angular-grid escalation is authorized.

## Iteration 413 raw negative result

Run `33861440653`, job `100986560018`, artifact `9934109783`, artifact digest `sha256:a7166a6a9c52cee4b7f66550027e8cd0adf04627f43774c22a5fc2c215913887`, raw result SHA-256 `9195de1f24c65bc85458a9bf5bd0f6173ca8b07011cb46f4ad81e5d3e087eef8`.

- Target: double-double index 2 / class 3 / `q^2=-1`.
- Frozen analytic/spectral structure and original-integrand cross-check remain valid.
- At `h=2.5e-6` vs `h/2=1.25e-6`, scaled mass-step discrepancy is `2.769196909034482e-04 > 2e-05`.
- Diagnostic coarse `D_s TrU1^2=+0.003621190924267374` is **not authority** and is not inserted in any sum.
- Iteration 413 is therefore a genuine negative numerical result: `BLOCKED_CONVERGENCE`, not an operational failure.

## Iterations 414–415 numerical-method authority

- Iteration 414 prospectively predicted `O(h^4)` behavior and expected the next discrepancy near `3.127629629080548e-06`.
- Raw Iteration 413 falsifies that model: discrepancy grows from `5.0042074065288766e-05` to `2.769196909034482e-04`.
- Iteration 415 diagnostic, commit `e5c43052b3ea869ea96aee21ee8f298ffd8ec18d`, records ratio `5.533737154423608`, observed order `-2.4682571634198707`, expected `O(h^4)` ratio `0.0625`, and `ROUND_OFF_OR_CANCELLATION_SUSPECTED` with diagnostic-only authority.
- Further blind `h` refinement is forbidden. The allowed path is derivative-representation / cancellation-roundoff analysis without threshold weakening or angular-grid escalation.

## Iteration 418 operational classification

- Run `33866891471`, job `101003680709`, artifact `9934301219` ended before scientific calculation.
- The cause was a source-drift sentinel defect: the marker `start=time.perf_counter()` occurs twice textually in the frozen Iteration-407 parent, while the wrapper required exactly one occurrence.
- Classification: `OPERATIONAL_EXECUTION_DEFECT`, not scientific FAIL. No physical convention or diagnostic result was tested. Artifact 9934301219 is not authority.

## Active computation — Iteration 419

**Run `33867065291`, job `101004215030` is `in_progress`** on the repaired channel-2 cancellation audit.

- repair code: `candidate_gravity/code/iteration419_tru1sq_channel2_mass_derivative_cancellation_audit_repair.py`;
- repair commit: `173e237beceb8616fcd290be4b8bd6c91870d961`;
- workflow/head commit: `e9566efd88cfa68d336e4a5527a6a3ce010260b0`;
- recovery: `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_419.md`.

Iteration 419 changes only the operational marker selection to the final executable occurrence. The scientific diagnostic is otherwise unchanged from Iteration 418: no new smaller mass step; only existing `h={5e-6,2.5e-6,1.25e-6}`; frozen Iteration-407 analytic sphere representation; central4×central4 mixed derivative; unchanged physical threshold `2e-5`; no angular-grid escalation; no zero fill. It measures 16-term cancellation conditioning, compensated-versus-naive summation and binary64 amplification. It is diagnostic-only and cannot promote index 2.

No useful heavy physical run is duplicated.

## Iteration 420 prospective interpretation contract

Iteration 420 is a methodological-only PASS frozen before Iteration-419 raw consumption. It uses the raw Iteration-413 discrepancy `2.769196909034482e-04` and prospectively defines a materially explanatory binary64 scale at 25% of that value:

`6.922992272586205e-05`.

- If either Iteration-419 `max_binary64_roundoff_bound_scaled` or `max_naive_vs_compensated_scaled_delta` is at least this threshold, binary64 cancellation is classified as materially capable of explaining the instability; the next gate is an algebraically identical higher-precision evaluation at the same frozen mass nodes and central4×central4 derivative.
- If both metrics are below this threshold, binary64 summation alone is insufficient; the next gate is a high-precision conditioning audit inside the fixed-mass `analytic_sphere_G` evaluation itself (kinematics, polynomial reconstruction, affine-denominator recurrence, radial extrapolation), again with no smaller `h`.
- Neither branch can promote index 2. Physical authority still requires a later raw-valid `CONVERGED` algebraically equivalent high-precision representation with unchanged `2e-5` and the existing structural/direct-original-integrand checks.

Code: `candidate_gravity/code/iteration420_channel2_cancellation_interpretation_contract.py`. Recovery: `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_420.md`.

## Iteration 412 exact15 assembly contract

Iteration 412 remains frozen and fail-closed. It requires exactly 15 unique double-double indices, five scientifically valid `CONVERGED` records per `q^2` bucket, finite coordinates, no duplicates, no missing indices and no zero fill. It remains BLOCKED until index 2 obtains raw-valid physical authority.

## Exact next gates

1. Raw-consume Iteration 419 artifact fail-closed and apply the already-frozen Iteration-420 decision rule; do not reinterpret the cancellation metrics post-hoc.
2. Construct the branch-appropriate algebraically equivalent high-precision auxiliary-mass representation for index 2 at the same frozen mass nodes, with prospectively frozen precision/stability checks and the existing original-integrand structural cross-check. Diagnostics alone cannot promote a physical coordinate.
3. Only if index 2 becomes raw-valid `CONVERGED`, run frozen Iteration 412 exact15 assembly, then complete `Tr U1^2`.
4. Only after complete `Tr U1^2`, assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2 using Iteration 406 `Tr U2`.
5. Source/Ward/contact completion + matched K2 and the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain downstream. No Candidate residual before comparator quotient closure.

Repeated-cut signs remain frozen: `D_s(simple)=-sphere_mean`; simple-double `D_s=+sphere_mean[d_mu G]`; double-double `D_s=-sphere_mean[d_mu1 d_mu2 G]`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

No readiness point is added by Iterations 413–420. Index 2 remains physically unresolved, exact15 `Tr U1^2` is blocked, and no robust comparator-subtracted residual exists.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results remain preserved. Operational failure/cancellation is not scientific FAIL. Empty uncut topology may use `+Infinity` only on the exact Iteration-392 mask. Denominator equivalence is not numerator equivalence. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
