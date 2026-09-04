# Candidate Gravity Authoritative Iteration ID Registry

Purpose: prevent recovery/provenance ambiguity when workflows are launched concurrently with research-log updates.

## Rule

An authoritative iteration number is allocated by the first committed `RESEARCH_LOG_ITERATION_N.md` / recovery record pair for that scientific iteration. A later workflow that embeds the same integer but represents a different scientific object is a **workflow-local duplicate identifier**. Its raw payload may be consumed only under a new unique authoritative iteration; it must never overwrite the earlier research/recovery meaning.

This is a provenance/operational rule. Identifier collision is not a physics FAIL.

## Reconciled collisions

- **432 authoritative:** raw consumption of Iteration-426 phi-resolution diagnostic. Later workflow-local `432` = parent primitive recursive-closure payload (run `33894344918`), consumed under authoritative Iteration 434.
- **434 authoritative:** parent-precision authority reconciliation (`Q0/y_down` plus recursive closure). Later concurrent workflow-local `434` = Q1/N1 conditioning audit (run `33899370539`), consumed under authoritative Iteration 435.

## Explicit current allocations

- **435:** raw-consumed frozen `Q1/N1` conditioning diagnostic; non-promoting.
- **436:** exact Iteration-270 `geometry -> nhat -> y_down -> norb -> N1` 80/120-digit precision closure at frozen `h=3e-5`; raw-consumed PASS.
- **437:** exact Iteration-270 `Q1=-Q0(p+k)@N1@Q0(p)` 80/120-digit precision closure with shifted-Q0 certification; raw-consumed PASS.
- **438:** exact Iteration-270 `A_finite` 80/120-digit arithmetic-core closure over the 26 signed nodes entering the seven frozen `Acoef/Asub` subsets; prospectively allocated before result consumption.

These meanings are reserved and may not be reused by concurrent workflows or research records.

## Forward guard

No future workflow or research record may reuse an already allocated authoritative integer for a different object. When concurrent work makes the next integer uncertain, use a descriptive workflow stage name without claiming a new authoritative iteration until raw consumption assigns the unique number.
