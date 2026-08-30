# RQIR Research Log — Iteration 080

**Date:** 2026-08-30

## Goal

Advance Paper III beyond the Iteration-077 architecture certificate without inventing an absolute detector ASD: invert the wall-clock equation into measurable apparatus-rate requirements for a declared duration cap.

## Result

Defined the harmonic mean of seven independently acquired calibration Fisher rates,

`H_cal = 7 / sum_j (1/R_cal,j)`,

which gives the exact current scheduling form

`T_total = m [Z^2/R_beta + 7 gamma_mean/H_cal + C_prep/R_src]`.

New **RQIR-RESOURCE-037**: `H_cal` is the correct single calibration-throughput number for current independent-layer wall-clock accounting.

For target `T_cap`, componentwise necessary floors are

- `R_beta >= m Z^2/T_cap`;
- `H_cal >= m 7 gamma_mean/T_cap`;
- `R_src >= m C_prep/T_cap`.

New **RQIR-NG-031**: satisfying all three individual floors is not jointly sufficient; at equality it costs `3*T_cap`.

With allocated positive fractions `f_sci+f_cal+f_src=1`, a sufficient specification is

- `R_beta >= m Z^2/(f_sci T_cap)`;
- `H_cal >= m 7 gamma_mean/(f_cal T_cap)`;
- `R_src >= m C_prep/(f_src T_cap)`.

The local reproducibility script verifies the harmonic-mean identity, exact cap closure, the `3*T_cap` trap and 1/7/30-day requirement tables for Toy009/Toy014.

## Decision

Paper III is materially advanced but remains open. The next gate is still a repository-backed physical apparatus model supplying `R_beta`, all seven matrix `R_cal,j`, `R_src`, duty and uncertainties for at least Toy009 and Toy014. The new envelope tells exactly what such a model must beat for any chosen duration target.

## Reproduce

`python analysis/apparatus_specification_envelope_iteration080.py`

## Document

`docs/PAPER_III_APPARATUS_SPECIFICATION_ENVELOPE_ITERATION080.md`
