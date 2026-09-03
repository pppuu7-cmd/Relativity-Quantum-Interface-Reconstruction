# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 308**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority.

## Current scientific state

### Iterations 291–295 — direct timelike weight-completed TrU1 numerator authority

Iteration 295 reconstructs all eight non-scaleless direct-timelike `[Tr U1]_{sab}` numerator families at frozen `s=0.016`: 36 primitive branches, 8 families, primitive/direct residual `6.485922909860165e-13`, maximum held-out relative error `4.842076903979733e-09`, no oracle imaginary contamination.

Freeze: `PASS_DIRECT_TIMELIKE_S0016_WEIGHT_COMPLETED_TRU1_ALL_FAMILY_NUMERATOR_RECONSTRUCTION`.

### Iterations 296/298/300–302 — corrected bubble-cut authority

The original Iteration-296 green artifact was rejected because it lacked sentinel 296. The repaired fail-closed run `33700626052` / job `100478933598` / artifact `9873542469` freezes the four bubble-family normalized cuts. Iteration 301 proves the relevant HV-like evanescent bubble layers are cut-null; Iteration 302 promotes the four bubble normalized-cut subsector. Full finite amplitude remains unpromoted.

### Iterations 303–304 — triangle evanescent cut protection

Iteration 303 counts 274 hidden HV-like polynomial coefficients beyond the 4D triangle oracle. Iteration 304 proves the corresponding hidden `mu^(2r)` layers are cut-null in the normalized common timelike discontinuity under the frozen HV-like barred-external-state convention, assuming regular same-parent D-dimensional coefficients near `D=4`.

Freeze: `PASS_HV_TRIANGLE_EVANESCENT_CUT_PROTECTION_ALL_274_HIDDEN_POLYNOMIAL_COEFFICIENTS_CUT_NULL_WITHIN_SCOPE`.

This protects the CUT only; the hidden coefficients are not zero-filled and the full finite amplitude is not promoted.

### Iteration 307 — complete e=1,c=2 TrU1 cut authority

Iteration 307 combines only schema-valid immutable Iterations 302 and 305 artifacts and freezes the complete eight-family weight-completed `Tr U1` normalized cut at the frozen timelike row:

- bubble subsector: `-0.010850153804447154`
- triangle subsector: `-0.5048578516117335`
- complete `D_s TrU1[e=1,c=2] = -0.5157080054161807`
- combined fitted cut `1/epsilon` residue: `1.2896746939995822e-09`.

Validated provenance: run `33703335692`, job `100487121536`, artifact `9874302096`, scientific JSON SHA-256 `3bc271990d63b90da42b339139b8ca68b8c9830242292adcb18696cc111ef22e`.

Freeze: `PASS_COMPLETE_WEIGHT_COMPLETED_TRU1_E1C2_EIGHT_FAMILY_NORMALIZED_CUT_AT_FROZEN_TIMELIKE_ROW`.

This is `Tr U1` only. The effective-action `-i/2` factor is not folded into the stored coordinate. It is not the complete C5 Gamma3 or a Candidate Gravity residual.

### Iteration 308 — e=2,c<=1 cubic placement/null-soft authority

Frozen operator order:

- `U1 = N_L V2 N_R Y`
- `U2 = N_L V1_L H V1_R N_R Y`
- EOM-degree-2 connection contribution: `+(i/2) Tr U2 -(i/4) Tr U1^2`.

At cubic background order on `(s,a,b)`:

`Tr U2`: 30 raw ordered placements; 18 exact singleton-soft kills; 12 surviving ordered placements, exactly 2 for each extra site `N_L`, `V1_L`, `H`, `V1_R`, `N_R`, `Y`.

`Tr U1^2`: 42 raw ordered placements; 26 singleton-soft kills; 16 surviving ordered placements; exactly 8 cyclic trace classes; 4 survivors for each second-order extra site `V2`, `N_L`, `N_R`, `Y`.

Only singleton null-soft linear EOM insertions are zero. Mixed soft-hard quadratic `V1^(2)`/`V2^(2)` vertices are retained.

Validated provenance: run `33703692659`, job `100488195810`, head `2bfd7ac2cdab22aeca3f443aa329d012ab7ecb3b`, artifact `9874425140`, digest `sha256:bfbdb7e04859109b79f337132a29d94624fa226d089dbee9f95410a8c0dc53e3`, scientific JSON SHA-256 `7623aa20ab729d2fe13a3da8f8d464431d32fc431b042c94a712a169f125db5b`, exactly one JSON object, sentinel 308, validator PASS.

Freeze: `PASS_E2C1_CUBIC_BACKGROUND_PLACEMENT_AND_NULLSOFT_PRUNING_AUDIT__EXACT_V1_H_KERNEL_IMPLEMENTATION_REMAINS`.

This is an exact placement/pruning certificate only, not numerical `Tr U2`/`Tr U1^2` authority.

## Frozen timelike kinematics

At `s=0.016`:

- `k_s^2=0`
- `k_s.k_a=-0.1`
- `k_a^2=-0.016`
- `k_b=-(k_s+k_a)`
- `k_b^2=-0.216`.

Linked physical target: `T_cut = D_s Gamma3_ret,soft - W[D_s K2]`.

## Active C5 sectors

Iteration 246 proves generic connection `e=3,c=0` null-soft trilinear sector vanishes; do not reopen it.

- connection `e=1,c<=2`: complete `Tr U1` normalized cut frozen by Iteration 307
- connection `e=2,c<=1`: placement/pruning frozen by Iteration 308; exact `V1-H-V1` executable kernel and numerical `Tr U2`/`Tr U1^2` remain open
- determinant `e=0,c<=3`: open.

## Current blockers / downstream

1. Derive and freeze the exact same-parent primary U2 index formula as an executable `V1-H-V1` kernel in the frozen pure-Einstein convention.
2. Explicitly map index spaces/transposes, flat graviton Green operator `H0`, and first-background `H1/V1_2` terms required by the 12 surviving U2 placements; reuse frozen `N1/Y1` infrastructure.
3. Map the 8 cyclic `Tr U1^2` classes onto authoritative U1 primitive kernels and freeze trace/routing equivalences without extra symmetry quotients.
4. Only after exact operator/trace/routing checks perform scoped numerator reconstruction and cut reduction for `e=2,c<=1`.
5. Then close determinant `e=0,c<=3`.
6. Source/Ward/contact completion and matched `K2` bridge remain required before source/Born subtraction.
7. Only then perform fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
8. Full finite-amplitude scheme authority remains separately blocked unless a same-parent D-dimensional numerator continuation or explicit scheme-conversion/counterterm map is frozen.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change from previous assessment: `0 pp`. Iterations 307–308 materially advance C5 cut authority and exact placement bookkeeping, but no stable rubric block has yet closed beyond the existing 24/25 comparator foundation.

## Retained guardrails

- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not promote weighted-kernel `tr(B3)` or Iteration-289 proxy coefficients/poles to actual `Tr U1` authority.
- Do not subtract `-8 M_Born` from a 1PI/comparator intermediate without an explicit matched source-observable map.
- Hidden evanescent coefficients are not zero; Iterations 301/304 are cut-protection statements only.
- Do not accept a green Action without expected sentinel/schema validation and raw artifact audit.
- Do not accept a failed Action as scientific FAIL unless a schema-valid diagnostic artifact preserves the violated frozen threshold and raw metrics.
- No unproven left/right or reversal quotient may be applied to the 12 surviving U2 placements.
- Mixed soft-hard EOM vertices are not zero-filled.
- Blind heavy full-C5 remains unauthorized.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Exact next gate

Derive/freeze the exact primary Vilkovisky U2 index formula into an executable same-parent `V1-H-V1` kernel, including index spaces/transposes, `H0`, and the first-background `H1/V1_2` terms required by the 12 surviving U2 placements. Reuse authoritative U1 primitives for the 8 cyclic `Tr U1^2` classes. Only after exact trace/transpose/routing checks may scoped numerator reconstruction begin.
