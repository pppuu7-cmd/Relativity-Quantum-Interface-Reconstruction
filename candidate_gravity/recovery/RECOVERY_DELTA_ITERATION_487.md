# Recovery Delta — Iteration 487

**Date:** 2026-09-06  
**MODEL_READINESS:** 24%  
**Readiness change:** 0 percentage points  
**Physical promotion:** none

## Exact two-level central4 truncation authority
For frozen central4 coefficients `c=[1/12,-2/3,2/3,-1/12]` on `[-2,-1,+1,+2]`, exact moments through k=11 are `[0,1,0,0,0,-4,0,-20,0,-84,0,-340]`. Thus the one-dimensional derivative expansion begins with coefficients `-1/30` at `h^4`, `-1/252` at `h^6`, and `-1/4320` at `h^8`.

For mixed `D_h=L_h^x L_h^y`, exact BASE-minus-HALF (`h` versus `h/2`) through `h^8` is:

`D_h-D_{h/2} = -(h^4/32)(f_51+f_15) -(h^6/256)(f_71+f_17) + h^8[-17/73728(f_91+f_19)+17/15360 f_55] + O(h^10)`.

Classification: `PASS_CENTRAL4_TWO_LEVEL_TRUNCATION_MISMATCH_EXACT__NON_PROMOTING`.

This proves the two-level mismatch is generically a mixture of higher-derivative structures; two levels do not identify a unique truncation order and do not authorize Richardson promotion. Frozen `ds=-d_base`, assembled MP80↔MP120 threshold `2e-6`, and BASE↔HALF threshold `2e-5` are unchanged. Any implementation violating the exact estimator identity is provenance `BLOCKED`, not physics FAIL.

## Active heavy gate
Rank14 `(u,v)=(+1e-5,+5e-6)`, multiplicity 1, canonical run `34008118612`, job `101418951867`, remains `in_progress` at this iteration. No duplicate run launched. Current certified support remains `18/32 = 56.25%`.

## Retained authority
Physical/operator 411; structural 410; blocker 421 with unresolved set `[2]`; latest completed mass-support authority 486. `ANSATZ-003` absent; Fisher/resources forbidden.

## Exact next gate
Raw-consume rank14 fail-closed. Only on raw PASS advance to the next explicit UNTESTED Iteration455 manifest coordinate; on BLOCKED localize the first failing `z/phi/radial` sample without threshold changes.

MODEL_READINESS: 24%
