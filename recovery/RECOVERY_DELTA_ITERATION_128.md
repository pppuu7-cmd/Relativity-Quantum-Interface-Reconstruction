# RQIR Recovery Delta — Iteration 128

**Date:** 2026-08-31  
**Parent front:** Iteration 127.  
**New decision:** **Paper III scientific scope CLOSED.**

## Scientific closure

Paper III is now 100% scientifically ready for its frozen resource/design/certificate scope.

The complete chain is explicit and repository-backed:

`interface discriminant -> exact constraints/source calibration -> detector nuisance profile -> source metrology -> transfer/cross-PSD calibration -> calibration span/backaction/no-double-counting -> physical Fisher rates -> robust wall clock -> final architecture certificate`.

### NG-084

Scientific closure is not apparatus closure. No same-apparatus numerical runtime or experimentally established Toy009/Toy014 winner is claimed.

### P3-CLOSE-001

Freeze Paper-III scientific scope. Do not open Toy015 or add scientific scope merely to continue iteration count unless an internal contradiction, failed regression or materially relevant new literature result requires reopening.

## Conditional apparatus extension — not a closure blocker

Still useful if a numerical experiment-specific verdict is desired:

- same-apparatus `f,2f` science transduction and PSD/cross-PSD;
- full complex transfer-reference Fisher-rate matrix;
- seven physical calibration Fisher-rate matrices and uncertainty correlations;
- geometry/additive reference Fisher and drift/floor models;
- an explicit measurement/backaction likelihood if covariance sharing is credited;
- measured source-metrology rate and duty;
- a robust `u=R_D14/R_D09` interval narrow enough for NG-030.

These are conditional inputs to the completed framework, not hidden assumptions.

## Files

- `analysis/paper3_scientific_closure_iteration128.py`
- `docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md`
- `research_log/2026-08-31_iteration_128_paper3_scientific_closure.md`
- this recovery delta.

## Readiness snapshot

- **Paper III scientific-content readiness: 100%.**
- **Paper III submission readiness: 97%.**
- **Repository readiness to begin a concrete Candidate-Gravity model: 90%.**
- **Concrete Candidate-Gravity model itself: ~10%.**

## Next action

For Paper III: manuscript production, figures/tables, bibliography refresh, independent clean rerun and journal formatting. Do not restart resource-theory research unless closure is invalidated.

For future Candidate Gravity: begin only as a separate branch using `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md` and QG-001…QG-010.
