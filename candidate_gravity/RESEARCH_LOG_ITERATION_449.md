# Candidate Gravity Research Log — Iteration 449

**Date:** 2026-09-05  
**Authority type:** raw consumption + frozen support enumeration; non-promoting  
**Classification:** `PASS_RAW_CONSUMED_SELECTED_PHI_SAMPLE_SLAB__FULL_SUPPORT_DENOMINATOR_ENUMERATED__NON_PROMOTING`

## Source-of-truth entry

Physical/operator authority remains Iteration 411. Structural authority remains Iteration 410. Raw-valid physical blocker remains Iteration 421 for double-double index 2 / class 3 / `q^2=-1`; exact unresolved physical set remains `[2]`.

Run `33928248369` completed successfully and is raw-consumed here under the prospective Iteration-448 interpretation. Raw provenance: job `101201330811`, artifact `9958661360`, artifact digest `sha256:16d70f63275c451c15cb13243240612dcdc2fc09f598fe08194b1b91c2ecd3c8`, head `8257cda2607fde9ec73245719b00671a17b43aeb`, raw scientific JSON SHA-256 `d7a148b1f55364145612e3c032aaa13a24634b87bad965a9f40a4d1db2b478bb`. Raw authority audit passed.

## Raw numerical result

The frozen selected slab was one mass corner `u=v=+5e-6`, z=`{-0.86,0,+0.86}`, all 16 phi nodes, radial Richardson h=`{2e-3,1e-3,5e-4}` with both signs, and direct parent recomputation at 80 and 120 decimal digits.

Observed:

- all 48 output rows finite;
- `scaled_mp80_vs_mp120_max = 1.87674211442491552330414104428e-80 <= 1e-30`;
- `max_radial_richardson_scaled_error = 2.57040398242795503891540021587e-15`, far below the inherited radial tolerance;
- 576 direct parent MP evaluations completed.

Therefore the raw stage is a genuine selected-slab precision PASS, but remains non-promoting exactly as Iteration 448 prospectively required.

## New coverage result

The retained raw-consumed Iteration-407 spectral support fixes:

- 32 frozen mass nodes;
- training z support `{-0.86,-0.43,0,+0.43,+0.86}`;
- 16 phi nodes.

Hence the complete sample-generation provenance denominator is now explicitly enumerated as

`32 x 5 x 16 = 2560` output `(mass-node,z,phi)` rows.

Each row requires 3 radial h values x 2 signs x 2 precision levels = 12 direct parent MP evaluations, so exhaustive support requires `30720` direct parent MP evaluations.

The raw-valid selected slab therefore covers exactly `48/2560 = 1.875%` of the frozen output-row support. This percentage is allowed only because the complete denominator is now explicit. It is a numerical-provenance coverage fraction, not model readiness, not physical closure and not a scientific residual claim.

At the already-tested mass corner, the only missing z values are `{-0.43,+0.43}`, i.e. 32 additional output rows and 384 direct parent MP evaluations. That is the next permitted stage under unchanged conventions.

No literature update was needed: this iteration makes only internal numerical-provenance claims.

## Scientific classification

This is not a Candidate-Gravity consistency FAIL, not an exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate. It does not promote physical index 2. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Readiness change: **0 percentage points**. A genuine numerical subgate passed and the full coverage denominator is now explicit, but no new stable model-readiness rubric component has closed.

## Exact next gate

Execute the remaining z=`{-0.43,+0.43}` at the same mass corner `u=v=+5e-6`, with the same 16 phi nodes, radial h values, direct 80/120-digit parent recomputation and unchanged thresholds. PASS closes full-z support only for that single mass node; it still cannot promote index 2. BLOCKED must localize the first failing z/phi/radial sample without changing conventions.
