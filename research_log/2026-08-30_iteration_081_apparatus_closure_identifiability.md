# RQIR Research Log — Iteration 081

**Date:** 2026-08-30

## Goal

Determine whether the existing repository physical benchmarks are sufficient to instantiate absolute Toy009/Toy014 wall-clock rates without introducing any new arbitrary ASD/source-coupling assumptions.

## Result

They are not sufficient for an absolute apparatus forecast, and the missing information is now explicit.

New **RQIR-NG-032**: normalized Fisher geometry does not determine absolute wall clock. A common detector PSD normalization `S -> lambda S` sends detector and calibration Fisher rates to `R/lambda`; the dimensionless calibration ratio `x` is unchanged while absolute detector/calibration time scales as `lambda`. More generally, multiplying all Fisher rates by a common factor leaves `(x,y,d)` unchanged but rescales total seconds inversely.

Independent source metrology has its own scale freedom: the mature Ramsey coefficient fixes `R_src/(p Omega_E)` only in the zero-reset special limit. General `R_src` still needs physical acceptance, visibility, coupling and reset/readout time.

New **RQIR-APP-001** records the minimum apparatus closure vector: science transfer and full PSD/cross-PSD, seven physical calibration Jacobians and matrix PSD/rates, source-metrology coupling/reset/visibility/acceptance/coherence, and low-frequency control/reference stability/duty with uncertainties.

The old `sigma_phi=1e-3 rad`, `1e-21 N/sqrtHz`, and unit-transduction examples are retained only as explicitly labeled scaling benchmarks; they may not be promoted to measured apparatus performance.

## Decision

Paper III remains open but its unresolved front is now apparatus instantiation rather than missing Fisher/resource algebra. Next build a declared reference apparatus model from externally sourced/measured platform parameters or retain a parameterized design envelope. Do not force absolute hours from illustrative numbers.

## Reproduce

`python analysis/apparatus_closure_identifiability_iteration081.py`

## Document

`docs/PAPER_III_APPARATUS_CLOSURE_IDENTIFIABILITY_ITERATION081.md`
