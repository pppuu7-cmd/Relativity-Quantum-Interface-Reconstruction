# RQIR Recovery Delta — Iteration 080

**Date:** 2026-08-30

Paper III advanced from architecture selection to an inverse apparatus-specification envelope.

New **RQIR-RESOURCE-037**: for seven independently acquired calibration layers define `H_cal=7/sum_j(1/R_cal,j)`, giving

`T_total = m [Z^2/R_beta + 7 gamma_mean/H_cal + C_prep/R_src]`.

New **RQIR-NG-031**: individual subsystem floors are necessary but not jointly sufficient. If science, calibration and source rates are each placed exactly at their individual `T_cap` floor, total payload time is `3*T_cap`.

With positive allocation fractions summing to one, sufficient targets are

`R_beta >= m Z^2/(f_sci T_cap)`,
`H_cal >= m 7 gamma_mean/(f_cal T_cap)`,
`R_src >= m C_prep/(f_src T_cap)`.

This is a rate requirement, not an apparatus forecast and not raw event Hz.

Code: `analysis/apparatus_specification_envelope_iteration080.py`.
Document: `docs/PAPER_III_APPARATUS_SPECIFICATION_ENVELOPE_ITERATION080.md`.

Immediate next gate: instantiate actual/source-specific `R_beta`, seven matrix `R_cal,j`, `R_src`, control duty and uncertainty intervals for Toy009/Toy014 from one repository-backed physical apparatus model; do not invent absolute ASD.
