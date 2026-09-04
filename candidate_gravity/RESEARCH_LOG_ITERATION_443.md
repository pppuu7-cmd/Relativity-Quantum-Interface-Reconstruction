# Candidate Gravity Research Log — Iteration 443

**Date:** 2026-09-04  
**Scope:** next outward precision boundary after Iteration 442  
**Classification:** `PASS_ITER443_LAYER368_370_PRECISION_BOUNDARY_AUDIT__NON_PROMOTING`

## Starting authority

Repository source of truth was read before this iteration: `CURRENT_QG_FRONT.md`, recovery/log through Iteration 442, recent commits, and recent Actions. Physical/operator authority remains Iteration 411; Iteration 421 remains the latest raw-valid physical blocker for double-double index 2. No active duplicate heavy Action was found.

Iteration 442 closed arithmetic precision plus a fixed-h independent representation/truncation oracle for the Iteration-270 `Acoef/Asub` parent. The next authorized outward layer was therefore Iterations 368/370.

## Source-level result

Direct audit of the frozen Iteration-368 implementation shows that the 368/370 layer contains numerical objects not covered by the already closed Iteration-270 `Q0/Q1/Acoef/Asub` certificate.

The first uncovered object is the Y-site derivative

\[
y_1=\frac{y_{\downarrow}(+h)-y_{\downarrow}(-h)}{2h},\qquad h=4\times10^{-5}.
\]

This derivative is constructed separately inside the Iteration-368 layer. It is therefore not certified merely because the parent `y_down`, `Q0/Q1`, and `Acoef/Asub` ingredients have scoped precision certificates.

After site construction, the same layer performs NumPy complex matrix products and trace contractions. These post-parent contractions are another retained-binary64 boundary unless either ported to arbitrary precision or quantitatively bounded tightly enough for the downstream frozen gates.

Iteration 370 inherits the Iteration-368 physical-numerator machinery, so its earlier numerator-transport result does not independently close this precision boundary.

Therefore the correct scoped conclusion is:

\[
\boxed{\text{Iteration-270 closure is necessary but not sufficient for 368/370 precision closure.}}
\]

This is a methodological precision-boundary PASS, not a physical-coordinate promotion, not a consistency FAIL, not a comparator identity, not non-identifiability, not near-degeneracy, and not a novelty certificate.

## Prospectively frozen next subgate

Before looking at any future result, the next test is frozen as follows.

For every distinct frozen Y-site input pair exercised by the representative/transport probe set of Iterations 368/370, evaluate the same `y_down` dynamics at 80 and 120 decimal digits using exactly the original

\[
h=4\times10^{-5}.
\]

Compare the original central derivative with the independent same-h fourth-order oracle

\[
y_1^{(4)}=\frac{y(-2h)-8y(-h)+8y(+h)-y(+2h)}{12h}.
\]

Fail-closed acceptance:
- `max |y1_80-y1_120| <= 1e-30`;
- `max scaled(y1_central_120,y1_fourth_120) <= 2e-5`;
- all outputs finite;
- all distinct frozen Y-site pairs covered.

Forbidden: smaller/adapted `h`, threshold weakening, altered routing, altered numerator, or wrapping outer arbitrary precision around binary64 Y-site values.

Only after this Y-site subgate passes may the post-parent matrix-product/trace contraction layer itself be certified. Only then may the precision chain advance to `379/374 -> 407 -> 424`.

## Scientific status

Physical unresolved set remains exactly `[2]`. Iteration 412 exact15 remains blocked. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No literature update is required for this numerical-provenance subgate because no comparator, novelty, or consistency claim changed.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Readiness change from Iteration 442: **0 percentage points**. Iteration 443 removes a false precision-closure shortcut and freezes the next numerical subgate, but it closes no additional model-readiness rubric component and promotes no physical coordinate.

## Exact next gate

Execute the frozen 80/120-digit Y-site `y1` test at the unchanged `h=4e-5` with the independent same-h fourth-order oracle over all distinct frozen 368/370 Y-site input pairs. If and only if that passes, certify the post-parent matrix products/trace contractions before advancing to `379/374`.
