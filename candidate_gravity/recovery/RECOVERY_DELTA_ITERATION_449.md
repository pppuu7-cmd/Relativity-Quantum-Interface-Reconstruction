# Recovery Delta — Candidate Gravity Iteration 449

**Date:** 2026-09-05  
**Authority type:** raw consumption + exhaustive frozen-support denominator enumeration; non-promoting  
**Classification:** `PASS_RAW_CONSUMED_SELECTED_PHI_SAMPLE_SLAB__FULL_SUPPORT_DENOMINATOR_ENUMERATED__NON_PROMOTING`

## Authority

Physical/operator authority remains Iteration 411; structural authority remains Iteration 410; physical blocker remains raw-valid Iteration 421 for double-double index 2 / class 3 / `q^2=-1`. Exact unresolved physical set remains `[2]`.

Iteration 449 raw-consumes run `33928248369` under the prospective Iteration-448 promotion barrier. Raw authority audit passed. Provenance: job `101201330811`, artifact `9958661360`, digest `sha256:16d70f63275c451c15cb13243240612dcdc2fc09f598fe08194b1b91c2ecd3c8`, raw JSON SHA-256 `d7a148b1f55364145612e3c032aaa13a24634b87bad965a9f40a4d1db2b478bb`.

## Raw PASS

Selected slab: `u=v=+5e-6`, z=`{-0.86,0,+0.86}`, 16 phi nodes, radial h=`{2e-3,1e-3,5e-4}` both signs, direct 80/120-digit parent recomputation.

Observed:

- 48/48 rows finite;
- max scaled 80/120 discrepancy `1.87674211442491552330414104428e-80 <= 1e-30`;
- max radial Richardson scaled error `2.57040398242795503891540021587e-15`;
- 576 direct parent MP evaluations.

This is `REPRESENTATIVE_SLAB_PRECISION_PASS__NON_PROMOTING` only.

## Exhaustive frozen support denominator

Raw-consumed Iteration-407 spectral support fixes 32 mass nodes, five training z values `{-0.86,-0.43,0,+0.43,+0.86}`, and 16 phi nodes. Therefore the sample-generation provenance denominator is exactly `32*5*16 = 2560` output rows. At 3 radial h x 2 signs x 2 precision levels, exhaustive support entails `30720` direct parent MP evaluations.

The passed slab covers `48/2560 = 1.875%` of this numerical-provenance support. This is not MODEL_READINESS and not physical closure.

The immediate allowed next stage is only z=`{-0.43,+0.43}` at the same mass point: 32 output rows / 384 direct parent MP evaluations under unchanged conventions.

`ANSATZ-003` remains uncreated. Iteration 412 exact15 remains BLOCKED. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Change: **0 percentage points** — selected-slab precision genuinely passed and the coverage denominator is now explicit, but no stable model-readiness rubric component closed.

## Next gate

Run the same-corner remaining-z MP stage. PASS closes all five frozen z values only at `u=v=+5e-6`; BLOCKED localizes the first failure. No threshold, node, routing, dynamics, numerator, precision-selection or mass-point change is allowed.
