# Iteration 604 — Prospective Finite-Lattice Boundary/Convergence Contract

Date frozen: 2026-09-08

Scope: **contract-only / non-residual** prerequisite for a future production rerun of the Iter596/602 full source-level nonlinear Ward gate. Iter602 remains a preserved historical FAIL; Iter603 remains diagnostic-only.

## Continuum authority kept unchanged
The production identity remains the Iter596/601 convention
`Delta G - R G - G L = 0`,
with all five mandatory Ward classes, exact Iter588 fixture, complete 13-family same-action cubic source object, symmetric route `p=-q_g/2`, `p'=+q_g/2`, and Iter601 endpoint matrices. No source family, normalization, momentum split, polarization, q2 grouping or comparator rule changes.

## Why a new lattice contract is required
Raw-consumed Iter603 shows strong radius sensitivity only in the three nonconvergent Iter602 `s/xi0..2` rows. At the same time the `s`-sector kernel condition estimates are of order `1e18`; therefore choosing one apparently favorable enlarged radius after inspecting the Ward residual would be scientifically invalid.

## Prospectively frozen adaptive rule for the next production gate
1. Use nested lattice radii `R = 4, 5, 6` as the primary convergence sequence. `R=3` is retained only as historical Iter602/603 provenance and is not used to certify convergence.
2. Keep the existing FD sequence exactly `(2e-2, 1e-2, 5e-3)`.
3. Keep the existing absolute Ward threshold exactly `2e-6` and existing last-FD-step convergence threshold exactly `2e-5`.
4. For each of the 12 frozen Ward rows, production authority requires at `R=5` and `R=6` simultaneously:
   - last absolute Ward residual `<= 2e-6`;
   - last FD-step difference `<= 2e-5`.
5. Radius stability is a separate mandatory condition: for each row, `|W_R6 - W_R5| <= 2e-6` for the final (`h=5e-3`) complex Ward value.
6. The 12 Iter587 one-leg anchors must remain `<=2e-11` at both `R=5` and `R=6`.
7. The Iter594 complete 13-family assembly cross-check remains `<=2e-5` and all 13 source families remain present.
8. No condition-number threshold is used to discard a row or alter the inverse. Condition estimates are recorded diagnostically only; failures of the frozen Ward/radius/anchor conditions cannot be waived because of conditioning.
9. Fail closed: if any mandatory row/anchor/assembly condition fails, classification is `BLOCKED_CONVERGENCE` or `FAIL_WARD` according to whether radius/FD convergence fails or a converged row exceeds the unchanged Ward threshold. No zero-fill, source deletion or threshold relaxation.
10. A result from this adaptive rerun cannot erase Iter602. It becomes a new prospective authority only after independent raw artifact consumption.

## Classification logic
For each row:
- if either `R=5` or `R=6` fails the FD last-step threshold, or `|W_R6-W_R5|>2e-6`: `BLOCKED_CONVERGENCE`;
- else if both radii are converged but either final residual exceeds `2e-6`: `FAIL_WARD`;
- else: row PASS.

Full gate PASS requires all 12 rows PASS plus the anchor and 13-family prerequisites. Otherwise the negative/BLOCKED result is preserved exactly.

## Forbidden downstream steps until full raw-valid Ward closure
No Source/Born subtraction; no source-to-Iter582 mapping; no comparator quotient; no `ANSATZ-003`; no Fisher/resources.

MODEL_READINESS: 24%
