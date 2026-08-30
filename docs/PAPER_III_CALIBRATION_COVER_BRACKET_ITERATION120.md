# RQIR Iteration 120 — Strong-vs-Shared Calibration Cover Bracket

**Date:** 2026-08-31  
**Status:** Paper-III calibration scheduling/resource bracket. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iterations 118–119 established two facts:

1. the current Toy009/Toy014 source-calibration requirement is genuinely full rank 22, with 14 mean directions plus an indispensable 8D centered-covariance complement;
2. in the optimistic affine Gaussian detector-output model, the eight covariance rows are best partitioned into four endpoint-disjoint matching blocks, with normalized accepted-trajectory burden `>4 gamma_cov` rather than `>6 gamma_cov` for one giant graph or `>8 gamma_cov` for eight separate rows.

The remaining question is how much total calibration cost can change depending on whether mean and covariance information must be scheduled separately or can share a physical output record.

This iteration gives a transparent bracket without inventing detector ASD, SI transduction or cycle durations.

## 2. Normalized accepted-cycle coordinate

Let

`xi_mean^2`

be the weakest-direction Fisher per accepted same-time dual-probe mean layer in the normalized current basis.

Then the seven nonredundant mean layers require

`M = 7 gamma_mean/xi_mean^2`

accepted layer-cycles.

For covariance, Iteration 119 gives two useful normalized burdens:

- optimistic four-matching detector-output cover:
  `C4 = 4 gamma_cov`;
- fully separate eight-row cover:
  `C8 = 8 gamma_cov`.

These are information-count coordinates only. Physical wall time still requires each campaign's acceptance and cycle duration.

## 3. Three exact accounting branches

### Absolute shared-output lower bound

If one physical set of records could simultaneously satisfy both the mean and four-matching covariance quotas with no loss or extra nuisance penalty, its accepted-cycle count could not be smaller than

`boxed{N_lower = max(M,C4)}`.

This is an optimistic lower bound, not a realizability claim.

### Matching covariance, but no mean/covariance sharing

If the four matching covariance blocks are physically realizable but cannot share records with the mean campaign,

`boxed{N_match = M+C4}`.

### Conservative separate-row branch

If covariance rows cannot share detector-output records and mean/covariance are separate,

`boxed{N_strong = M+C8}`.

Therefore, in the equal-cycle normalized coordinate,

`N_lower <= N_physical <= N_strong`

for any implementation lying between those declared branches. A real apparatus can move outside this simple cycle-count bracket if cycle durations, acceptance or per-block Fisher differ between families; then RESOURCE-083 must be used in physical rate units.

### RQIR-RESOURCE-090 — calibration-cover bracket

> The current calibration resource can be bounded without double counting by separating (i) the irreducible information burdens from (ii) the physical sharing assumption. The lower branch uses the maximum of simultaneous quotas; the conservative branch sums non-overlapping campaign costs.

## 4. Mean-versus-covariance bottleneck crossover

The optimistic matching covariance branch dominates the mean count when

`4 gamma_cov > 7 gamma_mean/xi_mean^2`.

Hence the crossover is

`boxed{xi_cross = sqrt[7 gamma_mean/(4 gamma_cov)]}`.

Using the stored calibration normalizations:

- Toy009:
  `xi_cross ~= 2.32971677`;
- Toy014:
  `xi_cross ~= 1.91172817`.

Thus for the transparent historical regression `xi_mean=3`, covariance is already the larger normalized information burden in both architectures.

## 5. Transparent xi_mean=3 regression

This is only a normalized cycle-count comparison, chosen because `xi=3` is the long-standing regression value in the physical calibration scripts.

### Toy009

- mean `M ~= 1.4235392e6`;
- four-matching covariance `C4 ~= 2.3605092e6`;
- separate covariance `C8 ~= 4.7210183e6`;
- optimistic shared lower bound:
  `N_lower ~= 2.3605092e6`;
- matching but separate from mean:
  `N_match ~= 3.7840484e6`;
- conservative:
  `N_strong ~= 6.1445576e6`.

### Toy014

- mean `M ~= 4.4159773e6`;
- four-matching covariance `C4 ~= 1.08746944e7`;
- separate covariance `C8 ~= 2.17493888e7`;
- optimistic shared lower bound:
  `N_lower ~= 1.08746944e7`;
- matching but separate from mean:
  `N_match ~= 1.52906717e7`;
- conservative:
  `N_strong ~= 2.61653661e7`.

The corresponding Toy014/Toy009 normalized calibration-burden ratios are

- lower shared branch: `~4.60693`;
- four-matchings separate from mean: `~4.04082`;
- conservative separate-row branch: `~4.25830`.

These are **not** the final physical calibration-time ratio because the two architectures have different phase schedules, transfer functions, acceptance, backaction and potentially different per-layer Fisher rates.

## 6. Relation to the earlier q_c result

Iteration 074 found the optimized abstract physical-calibration cost ratio

`q_c ~= 3.48483`

for Toy014/Toy009 in the established spectral-tilt-profiled row-normalized optimization.

The current branch ratios do not replace that result. They answer a different question: how much the physical scheduling of the already-required mean/covariance information can move when covariance rows are shared or separated.

The stored gamma ratios are

`gamma_mean,14/gamma_mean,09 ~= 3.10211`,

`gamma_cov,14/gamma_cov,09 ~= 4.60693`.

Therefore any apparatus whose calibration wall time becomes covariance-dominated will generally penalize Toy014 more strongly than one whose wall time is mean-dominated. This identifies the covariance channel as a high-value target for physical characterization.

### RQIR-DESIGN-019 — characterize covariance throughput before reopening source search

> Because Toy014's covariance calibration normalization is relatively more expensive than its mean normalization, the next apparatus characterization should prioritize the physical covariance-complement throughput and sharing/backaction model. A new Toy015 search is premature until that bottleneck is known.

## 7. Backaction-safe interpretation

The absolute lower branch `max(M,C4)` assumes perfect mean/covariance record sharing. Iteration 041 explicitly forbids granting that credit without a measurement model because cross-time source observables are noncommuting and non-QND.

Therefore the current scientifically safe use is:

- `N_lower`: optimistic detector-output lower bound;
- `N_match`: intermediate branch if covariance matchings are realizable but do not share mean records;
- `N_strong`: conservative no-sharing branch.

Physical Paper-III wall-clock closure should replace these normalized counts with full rate matrices and RESOURCE-083 as soon as a measurement model is declared.

## 8. Readiness snapshot after Iteration 120

Project-management estimates, not statistical quantities.

- **Repository readiness for writing Paper III — scientific content:** **93%**.
- **Paper III submission-ready state:** **74%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **84%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

Paper III increases because the unresolved sharing ambiguity is now represented by an explicit lower/intermediate/conservative resource bracket, and the covariance channel is identified as the next dominant characterization target. Candidate-Gravity readiness remains unchanged because no candidate dynamics or QG consistency gate was closed.

## 9. Next admissible gate

Convert the normalized calibration-cover bracket into a **rate-matrix bracket** that retains unequal layer durations, acceptance and correlations:

1. assign symbolic `R_mean,j` to the seven same-time layers;
2. assign symbolic Fisher-rate matrices to the four covariance matching blocks;
3. include common-gain transfer `K_x` from Iteration 115 as either a separate block or a declared joint block;
4. solve RESOURCE-083 for both conservative and optimistic campaign libraries;
5. derive a symbolic interval for the detector-side ratio `u=R_D14/R_D09` before inserting any apparatus-specific ASD.

Geometry/additive SI rates remain separate symbolic controls.

## 10. Reproducibility

Run

`python analysis/calibration_cover_bracket_iteration120.py`.

The script verifies the two bottleneck crossovers, all `xi_mean=3` normalized burden values and the Toy014/Toy009 branch ratios.
