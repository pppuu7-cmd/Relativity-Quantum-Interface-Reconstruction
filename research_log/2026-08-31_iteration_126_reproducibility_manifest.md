# RQIR Research Log — Iteration 126

**Date:** 2026-08-31

## Question

Can Paper III be reduced to a reviewer-scale reproducibility package rather than requiring the entire exploratory history to be rerun?

## Result

Yes. A minimum manifest now maps each manuscript-bearing numerical claim to one canonical script, expected invariant and claim class.

The manifest explicitly separates deterministic regressions from external-literature evidence and editorial audits. This prevents an evidence table from masquerading as an experimental reproduction.

Registered **REP-001**: every manuscript figure/table must be internally classed as `DERIVATION`, `DETERMINISTIC_REGRESSION`, `PARAMETRIC_SPECIFICATION`, `EXTERNAL_EVIDENCE`, or `MEASURED_APPARATUS`.

Registered **NG-083**: reproducible parameterized closure is not reproduction of apparatus data that were never supplied.

The minimum numerical anchors include the NUM-006/008 final-significance correction, the Iteration-101 temporal-correlation/transfer targets, the exact `22=14+8` calibration span, and the four-matching covariance-output partition.

## Readiness snapshot

- Paper III scientific-content readiness: **98%**.
- Paper III submission readiness: **93%**.
- Repository readiness to begin a concrete Candidate-Gravity model: **86%**.
- Concrete Candidate-Gravity model itself: **~10%**.

## Next gate

One final current literature/priority audit, followed by Paper-III scientific-closure certification if no missing scientific dependency appears.
