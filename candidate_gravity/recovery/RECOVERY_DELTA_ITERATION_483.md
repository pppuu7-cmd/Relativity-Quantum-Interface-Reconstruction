# Recovery Delta — Iteration 483

**Date:** 2026-09-06  
**MODEL_READINESS:** 24%  
**Readiness change:** 0 percentage points  
**Physical promotion:** none

## New exact authority
The frozen central4×central4 stencil sensitivity was mapped onto the frozen Iteration-455 manifest. Exact total absolute stencil weight per assembly is `9/4`.

At the current raw-certified ranks `0..11`:
- BASE certified absolute weight is `17/8`, i.e. `17/18 = 94.444444...%` of BASE stencil-L1 sensitivity;
- the remaining BASE ranks `12..15` carry only `1/8 = 1/18` of BASE absolute stencil weight;
- rank 12 contributes `1/144`; if it passes, BASE sensitivity-weight coverage becomes `307/324 = 94.753086...%`;
- HALF has only the four certified shared-corner entries (manifest ranks `5,6,9,10`), total absolute weight `1/36`, i.e. only `1/81 = 1.2345679...%` of HALF stencil-L1 sensitivity;
- HALF-exclusive ranks `19,20,23,24` alone carry `16/9 = 64/81` of HALF absolute stencil weight and remain untested.

Therefore occurrence-weighted support coverage (`16/32 = 50.000%`) is not a proxy for derivative-sensitivity coverage. BASE is already heavily covered in sensitivity weight while HALF remains largely untested in its dominant-weight nodes.

Classification: `PASS_OCCURRENCE_COVERAGE_DISTINCT_FROM_ASSEMBLY_SENSITIVITY_COVERAGE__NON_PROMOTING`.

This is diagnostic/provenance authority only. It does not promote physical index 2, does not change source order, and does not relax the requirement to certify all 28 distinct support coordinates before independent BASE/HALF MP80/120 assembly.

## Active gate
Canonical rank-12 run `33997856739`, job `101391409387`, remains `in_progress`. No duplicate run was launched.

## Authority retained
- physical/operator authority: Iteration 411;
- blocker authority: Iteration 421, unresolved set `[2]`;
- latest completed numerical mass-support authority: Iteration 480;
- latest authoritative research iteration: Iteration 483;
- no `ANSATZ-003`;
- Fisher/resources forbidden.

## Exact next gate
Raw-consume rank-12 run `33997856739` fail-closed. Only on raw scientific PASS advance to frozen rank 13 `(u,v)=(+1e-5,-5e-6)`, multiplicity 1. If BLOCKED, localize the first failing `z/phi/radial` sample without changing thresholds, dynamics, routing, support order, or precision conventions.

MODEL_READINESS: 24%

The percentage remains unchanged because no additional stable readiness-rubric component has closed.