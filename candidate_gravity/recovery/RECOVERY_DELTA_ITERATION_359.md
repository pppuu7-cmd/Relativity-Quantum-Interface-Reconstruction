# Recovery Delta — Candidate Gravity Iteration 359

Date: 2026-09-03

## Scope

Close an independent method prerequisite for the 30 repeated-pole physical U2 families frozen by Iterations 356-357. This iteration does **not** compute a discontinuity and does not reclassify any repeated-pole family as zero.

Iteration 358, launched immediately before this branch, ended operationally before scientific authority because its helper called the inherited norm-only `mdot(x)` as a bilinear `mdot(x,y)`. That failure is preserved as `OPERATIONAL_FAIL_ITERATION358_MD0T_ARITY__NO_PHYSICS_GATE_EVALUATED`. A new-version replacement is Iteration 360; no Iteration-358 threshold or physics result was modified post hoc.

## Raw Actions authority

- authoritative run: `33794603500`
- job: `100779139597`
- artifact: `9908669271` (`iteration359-result`)
- artifact digest: `sha256:2ee439e1dae46d77cbe3aed83110942f47f6a5374d5f27dc4d0998c9f61bfa78`
- scientific JSON SHA-256: `1d7482b0000699e0611adc172edf021e33491c23843fe025fce6246ebd25db76`
- workflow head: `b800924a75f4dfe2cac053b582837a6fbf304f61`

The raw artifact contains one Iteration-359 result with `scientific_gate_pass=true`; the sentinel/schema audit also passed.

## Result

Authority:

`PASS_U2_REPEATED_POLE_MULTIPLICITY_AND_DERIVATIVE_DISTRIBUTIONAL_REDUCTION_CONTRACT`.

Exact census for the 30 repeated-pole U2 families:

- repeated-pole families: `30`;
- maximum pole multiplicity: `2`;
- multiplicity pattern `(2,1)`: `12` families;
- multiplicity pattern `(2,1,1)`: `18` families;
- repeated momentum groups requiring a derivative: `30`;
- required derivative order for every repeated group: exactly `1`;
- typed timelike distinct-group channels that actually cut through a repeated pole and therefore require repeated-pole reduction: `48`.

Thus no cubic U2 family in the present matched timelike fixture contains a pole of order three or higher. Every repeated denominator is a **double pole**. The allowed algebraic bridge is therefore uniformly first order:

\[
\frac{1}{(D+i0)^2}
= -\left.\frac{\partial}{\partial \mu^2}\frac{1}{D+\mu^2+i0}\right|_{\mu^2=0}.
\]

The auxiliary derivative must be applied while preserving the same `+i0` prescription and before the repeated-pole cut is interpreted. The overall repository discontinuity sign and `2\pi i` normalization are intentionally not redefined here; they remain inherited from the frozen simple-cut normalization when physical integration is performed.

This is a method-contract PASS. It is not a nonzero U2 discontinuity certificate, not a consistency PASS/FAIL of Candidate Gravity, not comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate.

## Exact next gate

For the repeated-pole branch, introduce one auxiliary mass-squared parameter for the unique double-pole momentum group of each family, derive the channel-resolved massive-simple cut representation, differentiate once with respect to that auxiliary parameter, then take `mu2 -> 0`. Validate the resulting distributional expression against an independent smooth test-function oracle before any physical repeated-pole integration.

In parallel, Iteration 360 is the new-version replacement for the operationally failed ordinary-simple on-shell Iteration 358. It preserves the Iteration-358 physics scope and thresholds.

MODEL_READINESS: 24%

Change from Iteration 357: `0 pp`. The repeated-pole method blocker is narrowed to an explicit first-derivative construction, but no complete readiness-rubric bucket and no robust comparator-subtracted residual are closed.
