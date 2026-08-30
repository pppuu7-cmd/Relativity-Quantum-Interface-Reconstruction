# RQIR Research Log — Iteration 079

**Date:** 2026-08-30

## Goal

Freeze one source-agnostic regression certificate for the Paper-II likelihood layer so future D1/D2 apparatus changes cannot silently alter nuisance geometry or revive thresholded-pseudoinverse errors.

## Result

Added **RQIR-STAT-001** with seven deterministic checks:

1. Schur complement equals the orthogonal projection residual in the no-prior whitened likelihood.
2. Profiled Fisher is invariant under invertible nuisance reparameterization when Jacobian and prior transform consistently.
3. Adding positive-semidefinite independent nuisance information cannot reduce `F_beta|theta`.
4. NG-005 reproduces `F=C_a/(1+C_a)` and gives zero for `C_a=0`.
5. An exactly detector-aligned unconstrained control nuisance remains degenerate at arbitrarily increased exposure, reproducing the structural content of NG-006.
6. Two-band relative spectral-tilt profiling gives exactly `4 g2^2 g4^2/(g2^2+g4^2)`.
7. A weak but exactly science-aligned nuisance with norm `1e-8` gives true `F~0`; deleting its `1e-16` Fisher entry with a `1e-12` threshold falsely gives `F=1`, a minimal NUM-001 counterexample.

The local execution passed all assertions.

## Decision

Paper II is scientifically closed for the scope fixed in the article architecture. Physical conversion of Fisher requirements into shots/PSD/SNR/coherence/wall clock is Paper III.

## Reproduce

`python analysis/paper12_reference_regression_iteration079.py`

## Document

`docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md`
