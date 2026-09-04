# Candidate Gravity Current Front

**Updated:** 2026-09-04  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Latest validated Candidate Gravity physical/operator authority:** **Iteration 411**  
**Latest validated structural authority:** **Iteration 410**  
**Latest validated physical-blocking result:** **Iteration 421 — raw-valid `BLOCKED_CONVERGENCE` for index 2**  
**Latest validated numerical/conditioning diagnostics:** **Iterations 419, 422, 426(raw-consumed as 432), 428**  
**Latest exact non-promoting derivative-coordinate contract:** **Iteration 427**  
**Latest raw-valid implementation manifest:** **Iteration 429**  
**Latest prospective implementation contract:** **Iteration 430**  
**Latest source/dependency precision-boundary authority:** **Iteration 431**  
**Latest raw diagnostic consumption:** **Iteration 432**  
**Prospective authorized physical fallback:** **Iteration 424**, constrained by Iterations 425/427/428/429/430/431/432

Repository commits, raw schema-validated Actions artifacts, recovery material and this file are source of truth. Workflow colour alone is never scientific authority.

## Closed operator coordinates retained

### Timelike `Tr U2`

Iteration 406 complete coordinate before `+i/2` weight:
- `q^2=-1 -> +0.0005345424186332474`;
- `q^2=-0.34 -> -0.000734101259784574`;
- `q^2=-0.14 -> -0.001572666890130343`.

### Timelike `Tr U1^2`

Frozen census: 57 physical channels = 6 simple-simple + 36 simple-double + 15 double-double, exactly 19 per `q^2`.

Retained closures:
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

Strong passes include direct original-integrand `2.0658997659274425e-09 < 2e-06`, polynomial heldout `7.852876335312509e-16`, affine-denominator `2.220446049250313e-16`, radial Richardson `5.29849601693666e-15`, design condition `362.20107548262695 < 1000`, and synthetic oracle `1.6653345369377348e-16`.

This remains a narrow convergence/representation block, not a Candidate-Gravity consistency FAIL. No coordinate is promoted and no zero fill is allowed.

## Numerical / representation authority retained for index 2

- **Iteration 419:** summation-level binary64 effects alone are insufficient.
- **Iteration 422:** affine moments `J_0..J_4` are stable against 80-digit reference; max discrepancy `1.8927180676033106e-14`, Vandermonde condition `32.67245147666588`.
- **Iteration 425:** full fixed-mass `F(u,v)=1/2 beta(u,v) sum_k c_k(u,v) J_k(cc(u,v),aa(u,v))`; denominator-only auxiliary-mass differentiation is algebraically incomplete and forbidden.
- **Iteration 427:** exact non-measure chain oracle `D_s = H/s^2 + H_alphaalpha/(8 s^2) - H_rhorho/(8 s)`; at `s=1`, `D_s = H + (H_alphaalpha-H_rhorho)/8`. Non-promoting.
- **Iteration 428:** whole-path symmetric-cross conditioning is severe; outer-only high precision is insufficient.
- **Iteration 429:** raw-valid full-F precision manifest requires arbitrary-precision provenance or downstream-safe quantitative error bounds along `407 -> 379 -> 374 -> 370 -> 368`.
- **Iteration 430:** nominal deepest-first order frozen as `368/370 -> 379/374 -> 407 -> Iteration 424 -> Iteration 427`.

## Iteration 431 — corrected stage-1 precision boundary

Classification: `PASS_CHANNEL2_STAGE1_PARENT_PRECISION_BOUNDARY_CLOSURE__NON_PROMOTING`.

Source audit proves nominal `368/370` is not self-contained. Iteration 368 executes the pre-certificate prefix of `iteration270_vd_physical_b3_nonzero.py` and binds `ETA`, `Q0`, `Q1`, `Asub`, `y_down`; Iteration 370 then executes the setup/block-definition prefix of Iteration 368.

The true deepest precision closure therefore starts at

`270[Q0,Q1,Asub,y_down plus recursive numerical dependencies] -> 368/370`.

Iteration 270 contains genuine lower-precision numerical work (`np.linalg.inv/det/norm`, floating/complex arrays, and finite differences `N1`, `N2`, `Acoef/Asub`). A high-precision wrapper only around 368/370 would leave a hidden binary64 core and is not a valid stage-1 certificate unless each retained parent primitive gets a quantitative bound sufficient for all final gates.

Iteration 431 is source/provenance authority only; no physical `D_s` promotion occurs.

## Iteration 432 — raw consumption of Iteration 426

Iteration 426 run `33886485823` completed successfully. Artifact `9943246167`, digest `sha256:efd42550e9e5be80436585f1d4090d7ad29cb8adeed573f40dbadc3fc6fe6a66`; raw scientific JSON SHA-256 `a19104c54351227139135ba7a78e9766b22f505cc35abc5eefec1add65b29a00`; raw audit `scientific_authority_pass=true`, scope `DIAGNOSTIC_ONLY`.

Classification consumed as `PASS_CHANNEL2_ITERATION426_RAW_AUTHORITY_CONSUMPTION__PHI_MEAN_RESOLUTION_STABLE_DIAGNOSTIC_ONLY`.

Frozen diagnostic facts:
- max symmetric-cross `nphi=16` vs `nphi=32` scaled delta = `1.231653667943533e-05 < 2e-05`;
- max fixed-mass corner delta = `6.006480035569695e-16`;
- parent-vs-reimplementation reproduction = `8.673617379884035e-19 < 1e-13`;
- polynomial heldout = `4.547143911404206e-16`;
- radial Richardson = `4.599294035900758e-15`;
- min analytic uncut denominator = `0.11857147221810008`.

Therefore phi-node resolution is **not material enough by itself** to explain the Iteration-421 blocker at the unchanged `2e-5` physical tolerance. Diagnostic priority remains traced-numerator/radial/full-chain precision with the corrected Iteration-431 parent boundary. This result is diagnostic-only and cannot promote index 2.

## Active Actions

Iteration 426 is complete and consumed. No duplicate run is authorized. No currently known Action changes physical authority beyond Iteration 421.

## Authorized fallback — Iteration 424

Because Iteration 421 is raw-valid `BLOCKED_CONVERGENCE`, Iteration 424 remains authorized.

Frozen simultaneous acceptance:
- physical mass-step discrepancy `<=2e-5`;
- direct original-integrand cross-check `<=2e-6`;
- tensor-degree-(1,1) fit residual `<=2e-5`;
- identical fixed-node evaluation at 80 and 120 decimal digits with `|D_s(80)-D_s(120)|<=2e-6`;
- finite outputs.

Guardrails: same parent dynamics, routing, numerator, sign, normalization and mass nodes; no smaller `h`; no angular-grid escalation; no threshold weakening; no zero fill; full `F` precision provenance under Iterations 425/428/429/430/431/432.

## Frozen Iteration 412 exact15 assembly

Exactly 15 unique double-double indices are required, five scientifically valid `CONVERGED` records per `q^2` bucket, finite coordinates, no duplicates/missing indices/zero fill. It remains BLOCKED until index 2 gets raw-valid physical authority.

## Exact next gates

1. Port or quantitatively certify the relevant **Iteration-270 parent primitive closure** `Q0/Q1/Asub/y_down` and recursive numerical operations with 80/120-digit provenance.
2. Only after that inner closure passes, certify nominal Iteration 368/370 traced-numerator transport under the same precision provenance.
3. Continue outward through 379/374 and then 407 only after each inner layer has arbitrary-precision provenance or a quantitative retained-binary64 bound sufficient for final gates.
4. Evaluate exact Iteration-424 frozen mass nodes independently at 80 and 120 digits and compare with Iteration 427.
5. Promote index 2 only if all frozen physical, tensor-fit, direct-integrand, cross-precision and finite-output conditions pass under raw workflow authority.
6. If index 2 closes, execute frozen Iteration 412 exact15 assembly, complete `Tr U1^2`, then assemble `D_s Gamma_{e=2}=+(i/2)D_s TrU2-(i/4)D_s TrU1^2` q2-by-q2 using Iteration 406 `Tr U2`.
7. Comparator quotient / matched-observable completion remains downstream. No Candidate residual before comparator closure.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change at Iteration 432: **0 percentage points**. Iterations 431/432 close a hidden precision-boundary ambiguity and eliminate phi-node resolution as a material standalone explanation, but do not close index 2, exact15, comparator-subtracted residual, or any new stable-rubric block.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Negative/scoped results are preserved. Operational failure/cancellation is not scientific FAIL. Denominator equivalence is not numerator equivalence. Denominator-only auxiliary-mass differentiation is forbidden. Repeated poles are never ordinary simple cuts. Distinct `q^2` variables are never summed. Same `i0` is mandatory. No effective-action weight before operator-coordinate closure. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No blind heavy full-C5. Source/Born subtraction only in a matched observable after pole/cut-origin classification.
