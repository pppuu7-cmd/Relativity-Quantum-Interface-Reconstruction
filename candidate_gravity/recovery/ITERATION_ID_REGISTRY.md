# Candidate Gravity Authoritative Iteration ID Registry

Purpose: prevent recovery/provenance ambiguity when workflows are launched concurrently with research-log updates.

## Rule

An authoritative iteration number is allocated by the first committed research/recovery record pair for that scientific iteration. A later workflow that embeds the same integer but represents a different scientific object is a **workflow-local duplicate identifier**. Its raw payload may be consumed only under a new unique authoritative iteration; it must never overwrite the earlier research/recovery meaning.

This is a provenance/operational rule. Identifier collision is not a physics FAIL.

## Reconciled collisions

- **432 authoritative:** raw consumption of Iteration-426 phi-resolution diagnostic. Later workflow-local `432` = parent primitive recursive-closure payload (run `33894344918`), consumed under authoritative Iteration 434.
- **434 authoritative:** parent-precision authority reconciliation (`Q0/y_down` plus recursive closure). Later concurrent workflow-local `434` = Q1/N1 conditioning audit (run `33899370539`), consumed under authoritative Iteration 435.

## Explicit current allocations

- **435:** raw-consumed frozen `Q1/N1` conditioning diagnostic; non-promoting.
- **436:** exact Iteration-270 `geometry -> nhat -> y_down -> norb -> N1` 80/120-digit precision closure at frozen `h=3e-5`; raw-consumed PASS.
- **437:** exact Iteration-270 `Q1=-Q0(p+k)@N1@Q0(p)` 80/120-digit precision closure with shifted-Q0 certification; raw-consumed PASS.
- **438:** exact Iteration-270 `A_finite` 80/120-digit arithmetic-core closure over the 26 signed nodes entering the seven frozen `Acoef/Asub` subsets; raw-consumed PASS.
- **439:** exact Iteration-270 `Acoef` signed-sum binary64 cancellation-conditioning diagnostic at unchanged `h1/h2/h3`; raw-consumed non-promoting PASS.
- **440:** exact Iteration-270 `Acoef/Asub` 80/120-digit signed-assembly arithmetic closure at unchanged `h1/h2/h3`; raw-consumed PASS.
- **441:** exact Iteration-270 `Acoef/Asub` fixed-h representation/truncation oracle comparing the frozen central stencil against a same-spacing tensor-product fourth-order derivative rule; prospectively allocated before result consumption.
- **442:** authoritative raw consumption of Iteration-441 PASS, closing the scoped Iteration-270 `Acoef/Asub` arithmetic + fixed-h representation/truncation parent layer; non-promoting.
- **443:** source/provenance audit of outward Iterations 368/370 identifying the independently formed Y-site `y1` at frozen `h=4e-5` and post-parent matrix-product/trace arithmetic as still-unclosed precision boundaries; prospectively freezes the Y-site 80/120 + same-h fourth-order subgate; non-promoting.
- **444:** source/provenance audit freezing the exact Iteration-368 post-parent contraction arithmetic graph (7 matrix multiplications + 1 trace per routed amplitude) and the continuous 80/120-digit contraction certificate to be run only after Y-site PASS; non-promoting.
- **445:** raw consumption of the frozen Iteration-443 Y-site `y1` 80/120-digit + same-h fourth-order oracle; PASS, non-promoting.
- **446:** raw consumption of the Iteration-444 continuous post-parent seven-matmul + trace 80/120-digit certificate; PASS, non-promoting.
- **447:** raw consumption of the downstream source/provenance boundary audit after Iteration 446; locates still-uncertified Iteration-407 spectral/sample binary64 arithmetic; source-boundary PASS only, not numerical closure and non-promoting.
- **448:** prospective staged-coverage/promotion barrier for the post-447 class-3 phi/sample MP slab; freezes selected-slab PASS/BLOCKED interpretation and forbids treating 48-row one-mass-corner coverage as full-`F(u,v)` closure; non-promoting.
- **449:** raw consumption of run `33928248369` as a selected-slab 80/120-digit precision PASS plus explicit enumeration of the complete frozen Iteration-407 sample-support denominator (`32 mass nodes x 5 z x 16 phi = 2560 output rows`); non-promoting. The post-449 same-corner remaining-z workflow is intentionally unnumbered until raw consumption.
- **450:** raw consumption of run `33932061794`, job `101212520875`, artifact `9959560285` as PASS for z=`{-0.43,+0.43}` at `u=v=+5e-6`; combined with Iteration 449 this closes all five frozen training-z values at that one mass coordinate only. Numerical precision authority, non-promoting; physical unresolved set remains `[2]`.
- **451:** prospective bounded numerical gate at the first untested retained Iteration-407 source-order base-stencil coordinate `u=v=-1e-5`, run `33935454815`; active/in-progress at allocation time. Includes an operational provenance-reconciliation guard for the Iteration-450 artifact-digest convention; non-promoting.
- **452:** frozen Iteration-407 mass-support multiplicity audit. Establishes 32 source occurrences but 28 distinct `(u,v)` coordinates, with four BASE/HALF overlaps; retains the 32-occurrence denominator while adding a deduplication/provenance view and prospectively fixing `(-1e-5,-5e-6)` as the next source-order coordinate only if the active Iteration-451 run passes. Non-promoting.
- **453:** raw consumption of run `33935454815`, job `101222379474`, artifact `9961449686` as PASS at `u=v=-1e-5` across all five training-z, NPHI16 and full unchanged radial Richardson. Numerical precision authority only; non-promoting. Prospectively fixes `u=-1e-5, v=-5e-6` as the only next mass coordinate.
- **454:** frozen Iteration-407 `u<->v` mass-swap source/algebra audit. Establishes that although the Kallen/rho/beta sector is swap-symmetric, `alpha(v,u)-alpha(u,v)=(u-v)/s` shifts the routed momentum by `((u-v)/s)q`; no frozen numerator/uncut-denominator invariance exists under that shift. Therefore no additional transposition-based mass-support deduplication is authorized beyond the exact BASE/HALF coordinate overlaps of Iteration 452. Non-promoting shortcut no-go, not a physics FAIL.
- **455:** frozen deterministic Iteration-407 mass-support source-order manifest. Enumerates the 32 BASE/HALF source occurrences into 28 distinct coordinates with exact occurrence multiplicities and source labels, binds current certified/active states, and fixes `(-1e-5,+5e-6)` as the unique next coordinate if active run `33940931120` PASSes. Provenance/queue closure only; non-promoting.
- **456:** raw consumption of run `33940931120`, job `101238084215`, artifact `9963059047` as PASS at `u=-1e-5, v=-5e-6` across all five training-z, NPHI16 and unchanged full radial Richardson with direct MP80/120 parent recomputation. Numerical precision authority only; occurrence-weighted certified coverage becomes `4/32 = 12.5%`; non-promoting. Prospectively authorizes only `u=-1e-5, v=+5e-6` next.
- **457:** exact frozen central4×central4 BASE/HALF overlap-weight audit. Establishes that the four identical overlap coordinates may share one `F(u,v)` precision certificate, but BASE and HALF mixed-derivative source occurrences have same-sign coefficients differing by exact factor `16`, so the 32 derivative occurrences may not be collapsed to 28 weighted occurrences. Algebra/provenance closure only; non-promoting.

A later workflow-local job labelled `431` (`rqir-iteration431-channel2-cut-kinematic-h1-sensitivity`, run `33918967955`) is a duplicate identifier because authoritative 431 is already reserved. It may only be consumed under a future unique authoritative iteration and may not overwrite prior records.

These meanings are reserved and may not be reused by concurrent workflows or research records.

## Forward guard

No future workflow or research record may reuse an already allocated authoritative integer for a different object. When concurrent work makes the next integer uncertain, use a descriptive workflow stage name without claiming a new authoritative iteration until raw consumption assigns the unique number.
