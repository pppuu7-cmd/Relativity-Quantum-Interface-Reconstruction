# RQIR Candidate Gravity — Recovery Delta Iteration 529

Date: 2026-09-07

## Authority advanced
Iteration 529 establishes the exact combinatorial support requirement for the frozen Iteration-424 quarter-step central4 reevaluation and records the Iteration-528 first-run operational failure without converting it into a scientific FAIL.

Frozen quarter step: `h=1.25e-6`. Axis nodes: `{-2.5e-6,-1.25e-6,+1.25e-6,+2.5e-6}`. Full Cartesian support: 16 coordinates. Exact overlap with the already-certified HALF support is only the four corners with both coordinates in `{±2.5e-6}`. Therefore exactly 12 new quarter coordinates are required. The first deterministic u-major/v-major new coordinate is `(-2.5e-6,-1.25e-6)`, matching the staged rank1 target.

Classification: `PASS_ITER424_QUARTER_SUPPORT_MANIFEST_EXACT__NON_PROMOTING`.

## Iteration-528 operational event
First run `34094343153`, job `101654453787`, failed before sampling because the stage bound to stale prerequisite-key names. Iteration-527 authority actually uses top-level `iteration=527` and `observed.scientific_authority_pass=true`. Repository state repaired only this schema binding and retriggered exactly one run `34094463024`, which was `in_progress` at the time of this recovery delta. No dynamics, mass nodes, precision levels, z/phi/radial support or thresholds were changed.

The first run therefore has classification `operational BLOCKED`, not Candidate-Gravity consistency FAIL. It produced no physical quarter-step result.

## Exact next gate
Raw-consume repaired quarter-rank1 run `34094463024` after completion. Only raw-valid PASS permits quarter source rank2. Full frozen Iteration-424 physical reevaluation remains blocked until all 12 new quarter coordinates are raw-closed and the quarter assembly exists; none of the five physical fallback clauses may be zero-filled or replaced by a local support metric.

Physical/operator authority: Iteration 411.
Physical blocker authority: Iteration 421, unresolved set `[2]`.
Latest local mass-support authority: Iteration 523, `32/32 = 100%` for BASE/HALF support.
Latest assembled numerical authority: Iteration 527.
Latest structural/support authority: Iteration 529.
Latest authoritative research iteration: Iteration 529.

Comparator quotient remains operationally BLOCKED upstream of concrete `Source/Ward/contact+K2`. Robust comparator-subtracted residual is absent. ANSATZ-003 remains uncreated. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Readiness change: 0 percentage points. Exact support necessity and failure classification are now fixed, but no additional stable model-readiness rubric sector is complete.
