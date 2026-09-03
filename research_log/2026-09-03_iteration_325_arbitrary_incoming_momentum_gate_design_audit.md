# RQIR Candidate Gravity — Iteration 325

Date: 2026-09-03

## Purpose

Test the frozen physical ghost `N1/N2/N3` and graviton `H1/H2/H3` insertions at the actual incoming loop momentum `p+Q_before_insertion` required by the Iteration-324 shifted-propagator routing engine.

## Result

The first workflow attempt lost diagnostics after the scientific process returned nonzero. Only the workflow observability contract was repaired: the scientific code, mixed-finite-difference step and frozen thresholds were not changed. Diagnostic run `33732034116` then produced a schema-valid artifact (`9884220998`) with scientific JSON SHA-256 `7fbcac2f284f4036bfde903be789662601282afad7f5b182ee5be68fae892185` and scientific exit code 2.

All 18 actually requested shifted physical H/N insertions passed the direct exact-geometry comparison by large margins. Max scaled errors were:

- ghost order 1: `2.4427370126645087e-09`
- ghost order 2: `4.154289856561633e-09`
- graviton order 1: `7.896245324268136e-10`
- graviton order 2: `3.99741803894238e-09`

The gate nevertheless failed because its request inventory contained only ordered pair/triple partitions of target `(1,1,1)`. Therefore no single insertion could be the full cubic multiindex `(1,1,1)`. The exact Iteration-312 cubic logdet topology also contains the singleton `Tr(G0 K3)` term, so Iteration 325 did not actually test the required `H3/N3` singleton.

## Classification

`FAIL_SCOPED_GATE_DESIGN_INCOMPLETE_CUBIC_TOPOLOGY__TESTED_SHIFTED_HN_INSERTIONS_PASS`

This is a gate-design/completeness failure. It is **not** a Candidate Gravity consistency FAIL, not an exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty result. It does not invalidate the tested H/N kernels.

The failed gate is preserved as a negative methodological result. It is not edited post-hoc. A new version, Iteration 326, must add the missing singleton topology without changing parent dynamics, finite-difference step or thresholds.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 324: `0 pp`. The iteration exposed and quarantined a completeness defect in the validation gate but did not close any full readiness bucket or produce a robust comparator-subtracted residual.
