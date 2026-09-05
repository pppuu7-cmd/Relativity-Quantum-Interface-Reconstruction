# Candidate Gravity Authoritative Iteration ID Registry

Purpose: prevent recovery/provenance ambiguity when workflows are launched concurrently with research-log updates.

## Rule
An authoritative iteration number is allocated by the first committed research/recovery record pair for that scientific iteration. A later workflow embedding the same integer for a different object is a workflow-local duplicate identifier and may only be consumed under a new unique authoritative iteration. Identifier collision is operational/provenance, not physics FAIL.

## Reconciled collisions
- 432 authoritative: raw consumption of Iteration-426 phi-resolution diagnostic. Later workflow-local 432 parent recursive-closure payload was consumed under 434.
- 434 authoritative: parent-precision authority reconciliation. Later workflow-local 434 Q1/N1 audit was consumed under 435.
- workflow-local 431 run `33918967955` is a duplicate identifier; authoritative 431 was already reserved and may not be overwritten.

## Explicit current allocations
- 435: raw-consumed Q1/N1 conditioning diagnostic; non-promoting.
- 436: exact Iteration-270 geometry→N1 MP80/120 closure; PASS.
- 437: exact Q1 shifted-Q0 MP80/120 closure; PASS.
- 438: exact A_finite MP80/120 arithmetic-core closure; PASS.
- 439: Acoef binary64 cancellation-conditioning diagnostic; non-promoting PASS.
- 440: Acoef/Asub MP80/120 signed-assembly closure; PASS.
- 441: prospectively frozen same-h Acoef/Asub representation/truncation oracle.
- 442: raw consumption of 441 PASS; parent arithmetic + same-h representation closure.
- 443: outward source audit freezing Y-site y1 MP80/120 + same-h fourth-order gate.
- 444: post-parent contraction graph audit freezing continuous seven-matmul + trace MP gate.
- 445: raw Y-site y1 precision/oracle PASS.
- 446: raw continuous post-parent contraction PASS.
- 447: downstream source-boundary audit locating remaining Iteration-407 spectral/sample precision layer.
- 448: prospective representative-slab coverage/promotion barrier.
- 449: raw selected-slab MP PASS plus full frozen 2560-row occurrence denominator.
- 450: raw remaining-z same-coordinate PASS, completing five training-z at `(+5e-6,+5e-6)`.
- 451: prospective bounded gate at `(-1e-5,-1e-5)` plus artifact provenance guard.
- 452: frozen mass-support multiplicity audit: 32 source occurrences, 28 distinct coordinates, four exact BASE/HALF overlaps.
- 453: raw PASS at `(-1e-5,-1e-5)`.
- 454: exact `u<->v` shortcut rejection; no transposition deduplication allowed.
- 455: deterministic 32-occurrence/28-coordinate source-order manifest with exact multiplicities.
- 456: raw PASS at `(-1e-5,-5e-6)`; occurrence-weighted certified coverage `4/32=12.5%`.
- 457: exact BASE/HALF overlap-weight audit; shared precision certificate allowed for identical coordinates but derivative occurrences retain level-specific weights differing by factor 16.
- 458: exact central4×central4 mixed-derivative precision-budget audit. Establishes operator L1 norms `9e10` (BASE) and `3.6e11` (HALF), rejects any shortcut from local MP sample PASS directly to derivative-level MP closure, and prospectively freezes independent assembled BASE/MP80↔120 and HALF/MP80↔120 scaled discrepancy gates `<=2e-6` after all 28 distinct coordinates are locally certified. Non-promoting.
- 459: raw PASS at Iteration-455 distinct rank 2 `(-1e-5,+5e-6)` from run `33946347229`, artifact `9964610341`; occurrence-weighted certified coverage `5/32=15.625%`; non-promoting.
- 460: prospective post-support assembly cancellation/provenance contract. Requires reporting `D=sum w_i F_i`, `S_abs=sum |w_i F_i|`, `kappa_cancel`, and the weighted cross-precision bound `B_80_120=sum |w_i||F_i^80-F_i^120|` independently for BASE/HALF, while retaining the frozen assembled scaled MP80↔120 threshold `<=2e-6`. Triangle-bound violation is implementation/provenance BLOCKED; large cancellation is diagnostic only. Non-promoting.
- 461: raw PASS at Iteration-455 distinct rank 3 `(-1e-5,+1e-5)` from run `33951807833`, job `101267895504`, artifact `9966351908`; occurrence-weighted certified coverage `6/32=18.75%`; non-promoting.
- 462: exact central4×central4 tensor-moment invariants. Verifies 1D moments `m0=0,m1=1,m2=m3=m4=0,m5=-4`, tensor exactness on all `u^a v^b` with `0<=a,b<=4`, and freezes post-support operator sanity probes. Implementation/provenance closure only; non-promoting.
- 463: raw PASS at Iteration-455 distinct rank 4 `(-5e-6,-1e-5)` from canonical run `33957232727`, job `101282656909`, artifact `9968019110`; occurrence-weighted certified coverage `7/32=21.875%`; non-promoting. Concurrent race-duplicate rank-4 run is not separate authority.
- 464: exact central4 leading truncation-structure audit. Extends moments through `m9`, derives `D_h f=f'-h^4 f^(5)/30-h^6 f^(7)/252+O(h^8)` and the tensor mixed-derivative analogue; freezes BASE/HALF asymptotic scaling signatures `16` for isolated `h^4` and `64` for isolated `h^6`. `(16 D_half-D_base)/15` is diagnostic-only and cannot replace `ds=-d_base` or any frozen threshold. Non-promoting.

These meanings are reserved and may not be reused by concurrent workflows or research records.

## Forward guard
No future workflow or research record may reuse an already allocated authoritative integer for a different object. When concurrent work makes the next integer uncertain, use a descriptive workflow stage name without claiming a new authoritative iteration until raw consumption assigns the unique number.
