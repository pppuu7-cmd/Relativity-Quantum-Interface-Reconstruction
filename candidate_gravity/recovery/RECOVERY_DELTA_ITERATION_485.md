# Recovery Delta — Iteration 485

**Date:** 2026-09-06  
**MODEL_READINESS:** 24%  
**Readiness change:** 0 percentage points  
**Physical promotion:** none

## New exact authority
For frozen central4 mixed-derivative weights `w_ij=c_i c_j/h^2`, every exact BASE/HALF shared coordinate `(±5e-6,±5e-6)` obeys

`w_HALF = w_BASE / 16`

with identical sign. Derivation: BASE sees these as inner `±h_B` nodes with `|c|=2/3`; HALF has `h_H=h_B/2` and sees them as outer `±2h_H` nodes with `|c|=1/12`. Thus coefficient-product ratio is `1/64`, inverse-step-squared ratio is `4`, and net HALF/BASE ratio is exactly `1/16`.

Classification: `PASS_SHARED_BASE_HALF_CERTIFICATE_WEIGHT_RATIO_EXACT__NON_PROMOTING`.

This strengthens Iteration 457: exact coordinate overlap permits sharing the local MP precision certificate for `F(u,v)`, but never the derivative contribution weight. Future independent BASE/HALF assembly must multiply the shared sampled value by its own level-specific frozen weight. Any violation is implementation/provenance `BLOCKED`, not Candidate-Gravity consistency FAIL.

Reproducible code: `candidate_gravity/code/iteration485_shared_overlap_weight_audit.py`. Result: `candidate_gravity/results/iteration485_shared_overlap_weight_audit.json`.

## Active numerical gate retained
At the start and during this iteration canonical rank13 run `34003038811` was still `in_progress`; no duplicate heavy run was launched. Certified occurrence coverage therefore remains `17/32 = 53.125%` pending raw consumption.

## Authority retained
- physical/operator authority: Iteration 411;
- structural authority: Iteration 410;
- blocker authority: Iteration 421, unresolved set `[2]`;
- latest completed numerical mass-support authority: Iteration 484;
- latest authoritative research iteration: Iteration 485;
- no `ANSATZ-003`;
- Fisher/resources forbidden.

## Exact next gate
Raw-consume rank13 `34003038811` fail-closed. Only on raw scientific PASS advance to frozen rank14 `(u,v)=(+1e-5,+5e-6)`, multiplicity 1, and coverage `18/32=56.25%`. If BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen conventions.

MODEL_READINESS: 24%
