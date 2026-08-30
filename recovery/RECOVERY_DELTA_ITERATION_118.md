# RQIR Recovery Delta — Iteration 118

**Date:** 2026-08-31  
**Parent front:** Iteration 117.

## Exact calibration-span result

After trace, mean-energy and hidden-signal hard constraints, the current source-nuisance basis has dimension `22`.

For both Toy009 and Toy014:

`A_m=pm Zu` has shape `14x22` and rank `14`;

`A_c=pc Zu` has shape `8x22` and rank `8`;

`rank([A_m;A_c])=22`.

The seven same-time mean layer pairs each contribute exactly two new directions. After the full mean span is present, the eight centered-covariance rows each contribute exactly one new direction.

### RESOURCE-087

Current mean+covariance calibration spans the full 22D hard-constrained source-nuisance space.

### NG-075

No one of the seven current mean layer pairs is exactly redundant in this basis.

### NG-076

Mean-only calibration cannot replace centered covariance by more repetition/SNR; covariance supplies the missing 8D complement.

### RESOURCE-088

Starting from the 14D mean span, replacing all eight covariance-complement directions with four-real reference settings requires at least two distinct settings even dimensionally, and only if their score orientations cover the complement. One unchanged four-real transfer setting is insufficient.

Conditioning:

- Toy009 full span `s_min=0.00212667906656`, condition `~409.926`;
- Toy014 full span `s_min=0.00150105788788`, condition `~650.582`.

## Readiness after Iteration 118

- Paper III scientific-content readiness: **91%**.
- Paper III submission readiness: **72%**.
- Repository readiness to begin Candidate Gravity: **84%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Files

- `analysis/toy009_toy014_calibration_span_iteration118.py`
- `docs/PAPER_III_TOY009_TOY014_CALIBRATION_SPAN_ITERATION118.md`
- `research_log/2026-08-31_iteration_118_toy009_toy014_calibration_span.md`

## Next gate

Audit the physical sharing graph of the eight covariance rows and seven mean layers using the stored endpoint/backaction results. Determine the minimum physically distinct acquisition/setting cover compatible with the exact 22D span, then solve RESOURCE-083 without double counting.
