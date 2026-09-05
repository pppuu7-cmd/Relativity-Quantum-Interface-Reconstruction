# RQIR Candidate Gravity — post-482 parallel audits

Date: 2026-09-06

## Scope

Repository-first continuation while the sole permitted heavy numerical gate, frozen manifest rank 12 `(u,v)=(+1e-5,-1e-5)`, is active as run `33997856739`, job `101391409387`. No duplicate heavy run was launched. No threshold, support order, ansatz, dynamics, Fisher or resource gate was changed.

## Rank-11 authority rechecked

Iteration 480 remains the latest completed numerical mass-support authority for raw-consumed rank 11 `(u,v)=(+5e-6,+1e-5)`: `80/80` finite, max scaled MP80↔MP120 `2.94779472003420316940302965078e-80 <= 1e-30`, max radial Richardson scaled error `2.56155487488387492604714966234e-15 <= 5e-4`. Certified occurrence-weighted support is therefore `16/32 = 50.000%` pending rank-12 raw consumption.

## Frozen manifest tail

The Iteration-455 manifest was re-read rather than inferred by symmetry. Rank 12 is exactly `(u,v)=(+1e-5,-1e-5)`, multiplicity 1. Ranks 12–15 finish the BASE tail; ranks 16–27 are HALF-exclusive. All 16 coordinates after rank 11 have multiplicity 1, so each future local PASS changes occurrence-weighted coverage by exactly `1/32 = 3.125 percentage points`.

## Protocol-invariance audit

Source stages and workflows for rank 11 and rank 12 were compared. The numerical protocol is invariant in the scientifically relevant fields: Python 3.12; `numpy==2.1.3`, `mpmath==1.3.0`, `scipy==1.14.1`; the same parent sampler and mass-binding source; BASE_H `5e-6`; five frozen z nodes; NPHI16; radial steps `[0.002,0.001,0.0005]`; MP80/MP120; 80 required samples; all-finite requirement; MP discrepancy threshold `1e-30`; unchanged radial threshold and raw-authority schema. Only the prerequisite binding, manifest coordinate/rank and run-specific names change.

Classification: `PASS_RANK11_TO_RANK12_FROZEN_PROTOCOL_INVARIANCE__NON_PROMOTING`.

Result commit: `df1118619ba2f30f87cb2364a7cfe85fdb84ac34`.

## Index-2 blocker scale separation

Iteration 421 remains the physical blocker: stability `2.2720400683804223e-05` and required fit residual `2.585665489102237e-05` exceed the frozen `2e-05` limits by about 13.602% and 29.283%, respectively.

Those blocked scales are far above already-passed local numerical diagnostics: stability is about `4.288e9` times the Iteration-421 radial Richardson error and about `1.100e4` times the direct original-integrand crosscheck error; fit residual is about `4.880e9` and `1.252e4` times those errors, respectively. Relative to rank-11 radial error the separation is about `8.870e9` and `1.009e10`.

Therefore the evidence does not support treating increased decimal precision alone as a sufficient remedy. The unresolved mechanism is more plausibly derivative/mass-step reconstruction or representation consistency. This strengthens the rationale for completing the frozen mass-support set and then performing the prospectively retained independent BASE/HALF assembled derivative closure.

Classification: `PASS_BLOCKER_LOCALIZED_ABOVE_ARITHMETIC_AND_RADIAL_ERROR_SCALES__NON_PROMOTING`.

Result commit: `02790da414403de8f32b69e31b70e6a2fbe9941b`.

## Current active gate

Canonical rank-12 run `33997856739`, job `101391409387` is still the sole heavy authority candidate. Raw-consume fail-closed after completion. If PASS, coverage becomes `17/32 = 53.125%` and the next permitted heavy coordinate is frozen rank 13 `(u,v)=(+1e-5,-5e-6)`, multiplicity 1. If BLOCKED, localize the first failing `z/phi/radial` sample without changing thresholds or substituting a neighboring coordinate.

**MODEL_READINESS: 24% (unchanged).**

The new audits improve mechanism localization and protocol integrity but do not close any additional stable readiness-rubric component and do not promote physical `D_s`.
