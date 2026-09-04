# Recovery Delta — Candidate Gravity Iteration 443

**Date:** 2026-09-04  
**Authority type:** methodological / numerical-provenance, non-promoting  
**Classification:** `PASS_ITER443_LAYER368_370_PRECISION_BOUNDARY_AUDIT__NON_PROMOTING`

## Previous authoritative state

- physical/operator authority: Iteration 411;
- structural authority: Iteration 410;
- latest raw-valid physical blocker: Iteration 421, double-double index 2 / class 3 / `q^2=-1`;
- latest parent numerical authority: Iteration 442 consuming Iteration 441 PASS;
- exact unresolved physical set: `[2]`;
- `MODEL_READINESS: 24%`.

Iteration 442 closed the frozen Iteration-270 `Acoef/Asub` arithmetic and fixed-h representation/truncation sublayer. The next authorized outward dependency layer was Iterations 368/370.

## New result

Source audit of the frozen Iteration-368/370 path proves that Iteration-270 parent closure is not sufficient to certify this next layer.

The first uncovered numerical object is the separately formed Iteration-368 Y-site derivative

\[
y_1=\frac{y_{\downarrow}(+h)-y_{\downarrow}(-h)}{2h},\qquad h=4\times10^{-5}.
\]

The layer subsequently uses complex NumPy matrix products and trace contractions, which are a second retained-binary64 boundary. Iteration 370 inherits the Iteration-368 numerator machinery, so its earlier transport test does not supply an independent precision certificate for those operations.

Frozen interpretation:

\[
\boxed{270\text{ parent closure}\;\not\Rightarrow\;368/370\text{ continuous precision closure}.}
\]

No dynamics, numerator, routing, mass nodes, finite-difference step, sign, normalization, or downstream threshold changed.

## Prospectively frozen next gate

Before any Y-site result is observed:

1. use exactly `h=4e-5`;
2. use the same frozen `y_down` dynamics and all distinct Y-site input pairs from the 368/370 representative/transport probe set;
3. evaluate at 80 and 120 decimal digits;
4. retain the original central derivative;
5. compare to the independent same-h fourth-order oracle
   `y1_4=[y(-2h)-8y(-h)+8y(+h)-y(+2h)]/(12h)`;
6. require `max |y1_80-y1_120| <= 1e-30`;
7. require central-vs-fourth-order scaled discrepancy `<=2e-5`;
8. require all outputs finite and full frozen-pair coverage.

Smaller/adapted `h`, weakened thresholds, altered routing/numerator, or outer-only arbitrary precision around binary64 Y-site values are forbidden.

After Y-site PASS, certify post-parent matrix multiplication/trace arithmetic. Only then proceed to `379/374 -> 407 -> 424`.

## Scientific classification

This is not a new physical `D_s`, not a consistency FAIL, not an exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate. It is a source/provenance closure that prevents a false continuous-precision claim.

Exact unresolved physical set remains `[2]`. Iteration 412 exact15 stays blocked. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Change from previous estimate: **0 percentage points**. The iteration eliminates a numerical-provenance ambiguity but closes no additional stable model-readiness rubric component and promotes no physical coordinate.

## Recovery point

Authoritative research continuation is now Iteration 443. Reproduce the audit with `candidate_gravity/code/iteration443_layer368_370_precision_boundary_audit.py`; frozen audit result is `candidate_gravity/results/iteration443_layer368_370_precision_boundary_audit.json`.

**Exact next gate:** run the frozen 80/120-digit Y-site `y1` precision + same-h fourth-order oracle test over all distinct frozen 368/370 Y-site pairs, then certify post-parent contractions/trace if it passes.
