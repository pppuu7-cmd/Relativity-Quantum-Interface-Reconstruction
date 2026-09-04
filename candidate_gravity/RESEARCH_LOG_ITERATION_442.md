# RQIR Candidate Gravity — Research Log Iteration 442

## Scope
Raw-consume Iteration 441 fail-closed and decide whether the frozen Iteration-270 `Acoef/Asub` finite-amplitude representation/truncation gate is closed. Repository state and raw Actions artifact are authoritative; workflow colour alone is not.

## Raw provenance
- Iteration 441 workflow run: `33904593636` (`completed/success`)
- head SHA: `ebd52b26936d7f6d15a9541d0cbdcfe5cb0f66b0`
- artifact: `9949120808`
- artifact digest: `sha256:49e17960074953f502fec7672a6e7c67b471dca4882a8426120dea49d2b55e44`
- raw scientific JSON SHA-256: `141aa237b79d3acf8ba428c08dbcfe5ca0d81051abff260c3255e7789d37ffae`
- raw authority audit: `scientific_authority_pass=true`

## Frozen gate and result
The independent oracle used the same parent spacings as Iteration 270 — `h1=1e-4`, `h2=5e-4`, `h3=1e-3` — and only added `±2h` evaluations for the tensor-product fourth-order first-derivative rule. No smaller amplitude spacing was introduced.

Frozen acceptance:
- max 80↔120 high-order scaled discrepancy `<=1e-30`;
- max central-vs-high-order 120-digit scaled discrepancy `<=2e-5`;
- finite outputs;
- exactly 124 high-order node evaluations and seven nonempty subsets.

Observed:
- max 80↔120 high-order discrepancy = `3.39660363388259398057433228844e-75`;
- max central-vs-high-order discrepancy = `4.47609790628742112552755346023e-6`;
- worst subset = `(s,a,b)`;
- all values finite;
- node count = 124; subset count = 7.

Hence

`PASS_RAW_CONSUMED_ITER441_ASUB_FIXED_H_FOURTH_ORDER_ORACLE__NON_PROMOTING`.

The representation discrepancy is about 4.47 times below the prospectively frozen `2e-5` ceiling. Together with Iteration 440, this closes both arithmetic precision and finite-amplitude stencil representation/truncation for the frozen Iteration-270 `Acoef/Asub` parent layer.

## Strict interpretation
This is a scoped parent numerical-method PASS. It is not a physical `D_s` coordinate, not a Candidate-Gravity consistency PASS, not an exact comparator identity, not non-identifiability, not near-degeneracy, and not a novelty certificate. Iteration 421 remains the latest physical index-2 authority and remains `BLOCKED_CONVERGENCE`.

No thresholds, parent dynamics, mass steps, routing, numerator, signs, or normalizations were changed.

## Next gate
Proceed outward in the already frozen deepest-first chain: certify the Iteration `368/370` dependency layer under continuous 80/120-digit provenance or quantitative retained-binary64 bounds strong enough to preserve the downstream Iteration-424 gates. Do not jump directly to the physical fallback while a binary64 provenance gap remains.

## Readiness
Stable rubric remains:
- comparator foundation `24/25`
- unique residual discovery `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change from prior estimate: `0 percentage points`. A parent numerical representation ambiguity closed, but no additional stable model-readiness rubric component closed and no new physical coordinate was promoted.
