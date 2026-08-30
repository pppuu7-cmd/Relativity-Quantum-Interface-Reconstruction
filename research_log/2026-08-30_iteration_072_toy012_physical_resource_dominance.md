# RQIR Research Log — Iteration 072

**Date:** 2026-08-30

## Question

What does the Iteration-071 general Fisher-rate wall-clock closure imply for Toy012 after the mandatory Iteration-062/063 physical two-band correction?

## Result

Do not instantiate Toy012 with the old Euclidean-normalized `gamma` / `0.21617` science numbers. In the physical spectral-tilt-profiled D2 metric, balanced Toy012 is worse than Toy009 on every retained independent resource axis under shared transfer/scheduling kernels:

- science time factor `q_s = 5.0770994e7`;
- physical calibration time factor conservatively `q_c > 4.4e4`;
- zero-reset Ramsey source-metrology time factor `q_p = 1.18233035`.

Therefore for all nonnegative baseline ratios `x=T_cal,009/T_sci,009` and `y=T_src,009/T_sci,009`,

`q_s + q_c x + q_p y > 1+x+y`.

New retained rule **RQIR-RESOURCE-034 — componentwise resource-dominance pruning**: within a declared positive wall-clock factorization, a candidate slower on every component cannot be rescued by reallocating those components. A rescue must come from an explicit source-specific transfer/PSD/scheduling change, consistent with NG-029.

Minimum balanced-Toy012 rescue gains just for parity are approximately

- science Fisher-rate gain `>5.08e7`;
- calibration-rate gain `>4.4e4`;
- source-metrology rate gain `>1.1823`.

The high-response Toy012 point is not componentwise dominated because its Ramsey rate is `~1.150503x` Toy009, but its science/calibration penalties are enormous. Using conservative `q_c=490`, it can beat Toy009 only if

`y > 62961.68 + 3738.10 x`.

Thus balanced Toy012 is removed from the physical D2 Pareto front in the shared-kernel reference class. It remains a valid exact-locality existence construction. High-response Toy012 remains only an extreme source-metrology-favouring direction.

## Next

Audit the physical local-source Pareto set across Toy011-response, Toy011-conditioning, Toy012-high and Toy013 using science, spectral-tilt-profiled calibration, and Ramsey source-metrology time factors. Determine which candidates are dominated before apparatus selection and derive the local-only lower envelope in `(x,y)`.
