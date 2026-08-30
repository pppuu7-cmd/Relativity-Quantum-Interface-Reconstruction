# RQIR Recovery Delta — Iteration 072

**Date:** 2026-08-30

## Current front

Iteration 071 gave the general physical Fisher-rate wall-clock closure. Iteration 072 applies the mandatory Iteration-062/063 physical detector correction to Toy012 before any nominal apparatus-time estimate.

## New retained result

**RQIR-RESOURCE-034 — componentwise resource-dominance pruning.**

For a declared positive resource factorization, if a candidate has time ratios `q_s>1`, `q_c>1`, `q_p>1` relative to a baseline for science, calibration, and independent source metrology, then for all `x,y>=0`

`q_s + q_c x + q_p y > 1+x+y`.

It cannot become optimal by reallocating those three resources. It requires an explicit source-specific transfer/PSD/schedule gain that reverses at least one factor (NG-029).

## Balanced Toy012

Using the physical two-band D2 results:

- `S_eff,012/S_eff,009 = 1.9696285538e-8`;
- science time factor `q_s = 5.0770994e7`;
- Iteration-063 conservative physical calibration factor `q_c > 4.4e4`;
- Ramsey rate coefficients `0.002134292844` vs Toy009 `0.0025234392`, hence source-metrology time factor `q_p = 1.18233035`.

Balanced Toy012 is therefore componentwise dominated by Toy009 in the projected physical resource space under shared transfer/scheduling kernels.

Minimum source-specific rescue gains for parity are approximately:

- science Fisher rate `>5.08e7`;
- calibration rate `>4.4e4`;
- source-metrology rate `>1.1823`.

The exact locality/null/positivity/ordered-response existence result is retained; only physical D2 competitiveness is demoted.

## High-response Toy012

- science time factor `q_s = 8237.3298`;
- conservative physical calibration factor `q_c >490`;
- Ramsey source-time factor `q_p ~=0.869185`.

Because source metrology is modestly better, strict componentwise dominance does not apply. With optimistic `q_c=490`, Toy012-high beats Toy009 only if

`y > 62961.68 + 3738.10 x`,

where `x=T_cal,009/T_sci,009`, `y=T_src,009/T_sci,009`.

## Reproduce

`python analysis/toy012_physical_resource_dominance_iteration072.py`

Primary note:

`docs/TOY012_PHYSICAL_RESOURCE_DOMINANCE_ITERATION072.md`

## Next admissible gate

Construct a physical local-source Pareto audit for Toy011-response, Toy011-conditioning, Toy012-high and Toy013 on common axes:

1. spectral-tilt-profiled science time;
2. spectral-tilt-profiled calibration time;
3. Ramsey source-metrology time.

Identify dominated local candidates and derive the lower-envelope regions in `(x,y)` without choosing speculative apparatus parameters.
