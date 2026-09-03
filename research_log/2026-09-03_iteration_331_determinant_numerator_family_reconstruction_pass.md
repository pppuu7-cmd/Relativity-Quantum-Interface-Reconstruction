# RQIR Candidate Gravity — Iteration 331

Date: 2026-09-03

## Result

`PASS_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION_V2_CLOSED_TARGET_EXCLUDED_FROM_NONZERO_PROPER_SUBINDEX_CHECK`

Validated Action run `33742866100`, job `100608562495`, artifact `9888424625`, digest `sha256:ab86eeeb40dcf4d1e0f9d6529e7560147c1ca83a0da9cb33da1247ad02027f28`.

Iteration 331 is a new gate version after the preserved Iteration-330 scoped gate-design FAIL. It changes only the logically incorrect auxiliary condition: the full closed target `(1,1,1)` is excluded from the requirement that proper nonzero subindices carry nonzero external denominator differences. Parent dynamics, physical H/N construction, cubic logdet weights `1,-1/2,+1/3`, signed-affine loop maps, three held-out loop momenta and the `5e-10` threshold are unchanged.

All `13` physical cubic sequences are assembled with the common-parent combination

`weight * (1/2 Tr_H - Tr_N)`.

The canonical denominator census is exactly:

- `1` singleton;
- `3` bubble families under translations;
- `1` triangle integration family under the previously proved signed-affine quotient.

Crucially, denominator equivalence is not used as numerator equivalence. Each ordered route retains its own numerator transported through its explicit `p = sigma k + C` map. Held-out validation gives maximum denominator-map scaled error `1.1102230246251565e-16` and maximum numerator/integrand reconstruction scaled error `1.3877787807814457e-17`, both far below `5e-10`.

Scoped origin classification is now allowed:

- singleton: scaleless in dimensional regularization after loop translation, hence no nonlocal timelike cut origin;
- three bubble families: cut-capable topology only, nonzero discontinuity not yet certified;
- signed-affine triangle family: cut-capable topology only, nonzero discontinuity not yet certified.

This is not an integrated determinant cut, comparator-subtracted residual, novelty certificate, or consistency result. Iteration-297 evanescent/scheme authority remains binding for any claim about the full finite DR remainder. Source/Born subtraction remains forbidden until actual family discontinuities are reduced.

MODEL_READINESS: 24%

Change from Iteration 330: `0 pp`. A determinant hard prerequisite closes, but no full readiness-rubric bucket and no robust comparator-subtracted residual close.

## Exact next gate

Perform scoped DR/timelike discontinuity reduction for the three canonical bubble families and the signed-affine triangle family using the transported physical numerators. Certify zero/nonzero discontinuity family by family before any Source/Born subtraction. Do not claim a full finite DR remainder without resolving the frozen Iteration-297 evanescent/scheme authority blocker.
