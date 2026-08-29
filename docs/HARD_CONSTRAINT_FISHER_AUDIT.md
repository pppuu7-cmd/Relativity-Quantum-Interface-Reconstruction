# RQIR Iteration 015 — Hard-Constraint Fisher Audit

**Date:** 2026-08-29  
**Status:** numerical correction / resource-layer audit.  
**Scope:** Toy009 + Iteration-011 calibration geometry. The exact NP3 construction, Toy009 source, RQIR-NG-005, and scalar-gamma thresholds are not revoked.

## 1. Why this audit was necessary

Iterations 013-014 treated trace and mean-energy constraints as effectively exact by adding a Fisher penalty of order `1e12`, then profiling with `np.linalg.pinv(..., rcond=1e-12)`.

That is safe only if the numerical rank selected by the pseudoinverse is unchanged across the heterogeneous calibration scan. It was not.

When `gamma_mean` and `gamma_cov` become very unequal, the combined Fisher matrix spans many orders of magnitude. The pseudoinverse threshold then discards genuine weak nuisance directions. Those discarded directions can overlap the detector nuisance tangent, so the computed profiled `F_beta` is artificially high.

This is a numerical/inference bug, not new physics.

## 2. Exact fix

Let `Q` span the 24 source-state nuisance directions orthogonal to the exact NP3 null direction and let

`C = A_fixed Q`

contain the trace and energy rows.

Instead of a huge soft penalty, compute an orthonormal basis `Z` for the exact nullspace

`C Z = 0`.

For the current model, `rank(C)=2`, so `Z` has dimension `24 x 22`.

All subsequent Fisher calculations are then performed directly in the 22-dimensional hard-constrained nuisance space:

`u = Z w`.

No large penalty and no rank-sensitive pseudoinverse are required.

## 3. Direct falsification of the old heterogeneous optima

The Iteration-013 q=1 points were:

- D1: `gamma_mean=1.82e5`, `gamma_cov=3.49e5`;
- D2: `gamma_mean=1.70e5`, `gamma_cov=1.00e6`.

Evaluated with exact trace+energy elimination, they retain only approximately

- **D1:** `F_beta ~= 0.5724`;
- **D2:** `F_beta ~= 0.4811`.

They therefore do **not** satisfy the declared 90% target.

The previously reported cost reductions of about `6.3x` (D1) and `4.6x` (D2) are revoked.

## 4. Corrected heterogeneous allocation

The uniform 90% thresholds remain approximately unchanged:

- D1 `gamma_uniform ~= 1.537e6`;
- D2 `gamma_uniform ~= 2.145e6`.

These values were robust because the uniform path did not trigger the same heterogeneous numerical rank pathology.

With exact hard constraints and equal standardized per-shot class efficiency (`q_cov/q_mean=1`), the corrected resource optima are approximately:

### D1

- `gamma_mean ~= 1.72e6`;
- `gamma_cov ~= 0.94e6`;
- standardized cost `~=3.16e7`;
- uniform/optimal cost gain only `~=1.07`.

### D2

- `gamma_mean ~= 2.41e6`;
- `gamma_cov ~= 0.93e6`;
- standardized cost `~=4.12e7`;
- uniform/optimal cost gain only `~=1.14`.

Thus heterogeneous allocation remains mildly useful, but the dramatic prior gain was numerical rather than physical.

## 5. Correction to Iteration 014 correlation result

The compound-symmetry stress test was recomputed in the hard-constrained basis.

At fixed 90% retention, optimized cost ratios relative to the corrected uncorrelated optimum are approximately:

| rho | D1 | D2 |
|---:|---:|---:|
| 0.01 | 0.990 | 0.991 |
| 0.05 | 0.951 | 0.954 |
| 0.10 | 0.901 | 0.909 |

Therefore the old claim that D2 cost rises by about `2.13x` at `rho=0.10` is revoked for this compound-symmetry model.

In the corrected calculation, positive class-common correlation actually lowers the required standardized cost modestly because the inverse covariance enhances contrast-like row combinations that are useful for both current detector branches.

The broader qualitative statement **RQIR-CAL-006 survives**: correlation cannot be summarized by a scalar degradation factor; orientation of covariance eigendirections matters. But the earlier detector-specific numerical example was wrong.

## 6. Corrected conservative drift scales

The first-order derivative norms from Iteration 014 are independent of the pseudoinverse bug and remain valid:

- probe-position drift norm `||v_y|| ~= 2.91e-4`;
- common phase/time drift norm `||v_tau|| ~= 2.56e-2`.

Using the corrected q=1 allocations and the same conservative requirement that deterministic drift residual be below 10% of the statistical calibration sigma gives approximately:

- D1 `|delta tau| <~5.96e-3`;
- D2 `|delta tau| <~5.03e-3`.

At `f_gap=100 Hz`, this corresponds to roughly

- D1: `9.5 us`;
- D2: `8.0 us`.

These replace the old `26 us` and `15 us` illustrative bounds.

## 7. New methodological rule

### RQIR-NUM-001 — eliminate declared exact constraints analytically before Fisher profiling

If a nuisance constraint is intended to be exact, enforce it by basis reduction / nullspace elimination rather than by an arbitrarily large Fisher penalty when subsequent inference uses thresholded pseudoinverses.

Large penalties plus pseudoinverse cutoffs can silently change effective nuisance rank and create false information gains.

For soft physical priors, retain finite Fisher weights and report sensitivity to those priors explicitly.

## 8. What survives unchanged

This correction does **not** affect:

- the exact rank-24/25 NP3 construction;
- positivity of the Toy009/Toy010 states;
- equal selected mean/noise constraints;
- nonzero opposite ordered response;
- Toy009 source geometry;
- Iteration-011 calibration geometry;
- RQIR-NG-005 null-amplitude self-calibration obstruction;
- the need for independent source-preparation metrology;
- the distinction between coherence time and total integration time;
- the scalar uniform-gamma diagnostic thresholds to the quoted precision.

## 9. Next gate

Rebuild the planned explicit low-rank drift/additive-offset Fisher model **in the hard-constrained basis**. Only after that should finite priors on timing, geometry, offsets, and gain-state couplings be translated into physical clock/control requirements.

Reproducibility code: `analysis/hard_constraint_fisher_audit_iteration015.py`.
