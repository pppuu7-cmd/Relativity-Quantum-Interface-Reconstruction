# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity physical/operator authority:** **Iteration 411**  
**Latest validated structural authority:** **Iteration 410**  
**Latest validated physical-blocking result:** **Iteration 421 — raw-valid `BLOCKED_CONVERGENCE` for index 2**  
**Latest validated numerical/conditioning diagnostics:** **Iterations 419, 422, 428**  
**Latest exact non-promoting derivative-coordinate contract:** **Iteration 427**  
**Latest raw-valid implementation manifest:** **Iteration 429**  
**Latest prospective implementation contract:** **Iteration 430**  
**Latest source/dependency precision-boundary authority:** **Iteration 431**  
**Prospective authorized physical fallback:** **Iteration 424**, constrained by Iterations 425/427/428/429/430/431

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Workflow colour alone is never scientific authority.

## Closed operator coordinates retained

### Timelike `Tr U2`

Iteration 405 raw-validates exact 48/48 repeated-cut assembly. Iteration 406 gives the complete timelike coordinate before the `+i/2` effective-action weight:

- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

### Timelike `Tr U1^2`

Frozen census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`.

Closed components retained:
- Iteration 374 simple-simple 6/6;
- Iteration 393 simple-double 36/36;
- Iteration 399 double-double index 5 / class 8 / `q^2=-0.14` = `+0.000119747535002548`;
- Iteration 409 index 4 / class 5 / `q^2=-1` = `+0.003562716046166582`;
- Iteration 411 index 11 / class 16 / `q^2=-0.34` = `+0.013050543643260309`.

**Exact unresolved double-double physical set: `[2]`.**

## Index 2 physical authority

Target: double-double index 2 / class 3 / `q^2=-1`.

Iteration 421 is the latest raw-valid physical attempt: run `33871920373`, job `101019660127`, artifact `9942128452`, digest `sha256:d75c5063b81e02872fe1255421c62e0679de22ae13fce7e2013358eba73152ff`, scientific JSON SHA-256 `c297cb15b707ef59b9d940c159a1fcb7e9f3a1e64135ccebc077b48a869f5e20`.

Classification: `BLOCKED_CONVERGENCE`; diagnostic estimate only `D_s Tr(U1^2)[2] ~= +0.0035843041850530683` is **not authority**.

Frozen failures:
- `max_stability_scaled = 2.2720400683804223e-05 > 2e-05`;
- `max_required_fit_residual_scaled = 2.585665489102237e-05 > 2e-05`.

Strongly passing checks:
- direct original-integrand cross-check `2.0658997659274425e-09 < 2e-06`;
- polynomial heldout `7.852876335312509e-16 < 2e-06`;
- affine-denominator `2.220446049250313e-16 < 2e-11`;
- radial Richardson `5.29849601693666e-15 < 5e-4`;
- design condition number `362.20107548262695 < 1000`;
- synthetic oracle `1.6653345369377348e-16 < 1e-12`.

This is a narrow convergence/representation block, not a Candidate-Gravity consistency FAIL. No coordinate is promoted and no zero fill is allowed.

## Numerical / representation authority retained for index 2

- **Iteration 419:** summation-level binary64 effects are far below the frozen materiality threshold and are insufficient by themselves.
- **Iteration 422:** affine moments `J_0..J_4` are stable versus 80-digit reference; max discrepancy `1.8927180676033106e-14`, Vandermonde condition `32.67245147666588`.
- **Iteration 425:** full fixed-mass function is `F(u,v)=1/2 beta(u,v) sum_k c_k(u,v) J_k(cc(u,v),aa(u,v))`; denominator-only mass differentiation is algebraically incomplete and forbidden.
- **Iteration 427:** exact non-measure chain reduction `D_s = H/s^2 + H_alphaalpha/(8 s^2) - H_rhorho/(8 s)`; at target `s=1`, `D_s = H + (H_alphaalpha-H_rhorho)/8`. Non-promoting independent oracle only.
- **Iteration 428:** whole-path symmetric-cross conditioning is severe; at the smallest frozen node the signed four-corner numerator must remain accurate to about `5e-16` absolute to preserve the `2e-5` quotient tolerance. Outer-only high precision is insufficient.
- **Iteration 429:** raw-valid full-F precision-closure manifest binds the shallow implementation chain `407 -> 379 -> 374 -> 370 -> 368`; every retained lower-precision sublayer requires a quantitative downstream-safe bound or arbitrary-precision provenance.
- **Iteration 430:** deepest-first implementation order frozen as nominal `368/370 -> 379/374 -> 407 -> Iteration 424 -> Iteration 427`.

## Iteration 431 — stage-1 parent precision-boundary closure

Classification: `PASS_CHANNEL2_STAGE1_PARENT_PRECISION_BOUNDARY_CLOSURE__NON_PROMOTING`.

Source audit corrects the nominal Iteration-430 stage boundary without changing any physics. `iteration368_tru1sq_timelike_full_prepruning_routing.py` executes the pre-certificate prefix of `iteration270_vd_physical_b3_nonzero.py` and binds the numerical parent primitives `ETA`, `Q0`, `Q1`, `Asub`, and `y_down`. Iteration 370 then executes the setup/block-definition prefix of Iteration 368.

The actual deepest precision closure therefore begins at

`270[Q0,Q1,Asub,y_down plus recursive numerical dependencies] -> 368/370`,

not at the 368 file boundary alone.

Iteration 270 contains genuine lower-precision numerical work: NumPy floating/complex arrays, `np.linalg.inv`, `np.linalg.det`, `np.linalg.norm`, and finite-difference constructions `N1`, `N2`, `Acoef/Asub`. Therefore a nominal arbitrary-precision wrapper around only 368/370 would leave a hidden binary64 core and cannot be certified as complete stage-1 high precision under Iterations 429/430 unless every retained parent primitive gets a quantitative error bound sufficient for all final gates.

Iteration 431 is source/provenance authority only. It computes no `D_s`, does not promote index 2, does not weaken thresholds, and does not unlock exact15.

## Active Actions

At the last checked state retained from the preceding front, Iteration 426 phi-mean 16-vs-32 diagnostic run `33886485823` was still `in_progress` and independent/non-promoting. It must be raw-consumed fail-closed when complete and must not be duplicated. Its outcome cannot by itself promote index 2.

## Authorized fallback — Iteration 424

Because Iteration 421 is raw-valid `BLOCKED_CONVERGENCE`, Iteration 424 remains authorized.

Frozen acceptance remains simultaneous:
- physical mass-step discrepancy `<=2e-5`;
- direct original-integrand cross-check `<=2e-6`;
- full tensor-degree-(1,1) fit residual `<=2e-5`;
- identical fixed-node evaluation at 80 and 120 decimal digits with `|D_s(80)-D_s(120)|<=2e-6`;
- finite outputs.

Guardrails: same parent dynamics, routing, numerator, sign, normalization and mass nodes; no smaller `h`; no angular-grid escalation; no threshold weakening; no zero fill; full `F` precision provenance required under Iterations 425/428/429/430/431.

## Frozen Iteration 412 exact15 assembly

Iteration 412 requires exactly 15 unique double-double indices, five scientifically valid `CONVERGED` records per `q^2` bucket, finite coordinates, no duplicates, no missing indices and no zero fill. It remains BLOCKED until index 2 obtains raw-valid physical authority.

## Exact next gates

1. Raw-consume Iteration 426 fail-closed when its artifact appears; it is diagnostic-only and cannot promote index 2 by itself.
2. Port or quantitatively certify the relevant **Iteration-270 parent primitive closure** `Q0/Q1/Asub/y_down` and recursively used numerical operations at 80/120-digit provenance.
3. Only after that inner closure passes, certify nominal Iteration 368/370 traced-numerator transport under the same precision provenance.
4. Continue outward through 379/374 and then 407 only after each inner layer has arbitrary-precision provenance or a quantitative retained-binary64 bound sufficient for the final gates.
5. Evaluate the exact Iteration-424 frozen mass nodes independently at 80 and 120 digits and compare against Iteration 427.
6. Promote index 2 only if all frozen physical, tensor-fit, direct-integrand, cross-precision and finite-output conditions pass under raw workflow authority.
7. If index 2 closes, immediately execute frozen Iteration 412 exact15 assembly, then complete `Tr U1^2` and assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2 using Iteration 406 `Tr U2`.
8. Comparator quotient / matched-observable completion remains downstream. No Candidate residual before comparator closure.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change at Iteration 431: **0 percentage points**. Iteration 431 closes a hidden implementation/provenance boundary but does not close index 2, exact15, a comparator-subtracted residual, or any additional stable-rubric block.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
