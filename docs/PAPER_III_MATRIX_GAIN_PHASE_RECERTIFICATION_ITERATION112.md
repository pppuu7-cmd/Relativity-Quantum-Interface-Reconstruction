# RQIR Iteration 112 — Matrix Complex-Gain/Phase Recertification Envelope

**Date:** 2026-08-31  
**Status:** Paper-III control/resource gate. Exact multivariate pure-dead recertification reduction; no apparatus winner and no new-physics claim.

## 1. Purpose

Iteration 111 reduced several independent scalar pure-dead controls to aggregate loads

`H_i=sum_j h_ij`.

The leading unresolved control is complex transfer gain/phase. Iterations 101–103 already define a same-state dual-tone transfer Fisher matrix, but a complex gain is naturally multivariate: amplitude and phase errors can be correlated, their drift can be correlated, and one reference block can estimate several transfer coordinates at once.

Therefore treating gain amplitude and phase as two independent scalar `h_j` terms is not generally exact.

This iteration derives the coordinate-invariant matrix recertification problem that replaces that scalar approximation.

## 2. Physical matrix objects

Let `x` be a real vector of local transfer-control coordinates, for example

`x=(delta ln|chi_2|, delta phi_2, delta ln|chi_4|, delta phi_4)`

or any equivalent nonsingular local coordinate system.

Declare:

- `Sigma_*` — maximum admissible control-error covariance matrix;
- `Sigma_f` — irreducible covariance floor;
- `S = Sigma_* - Sigma_f`, required positive definite on the controlled support;
- `F_ref` — reference Fisher-rate matrix per unit reference time;
- `Q` — covariance-diffusion matrix under the Iteration-109 convention `Cov_drift=tau Q/2`.

A reference block of duration `t_ref` has the efficient-estimator covariance floor

`Cov_ref=(t_ref F_ref)^-1`.

At the end of a live interval `tau`, the pure-dead recertification condition is

`boxed{(t_ref F_ref)^-1 + tau Q/2 <= S}`

in Loewner order.

The matrix statement is the direct gain/phase analogue of the scalar Iteration-109 condition.

## 3. Whitened exact reduction

Whiten by the usable covariance budget `S` and define

`A = S^-1/2 F_ref^-1 S^-1/2`,

`B = S^-1/2 Q S^-1/2`.

Then the constraint becomes

`A/t_ref + tau B/2 <= I`.

For a fixed live cadence `tau`, define

`C(tau)=I-tau B/2`.

Admissibility requires

`0 < tau < 2/lambda_max(B)`

when `B` has nonzero drift support.

For fixed `tau`, the minimum reference time is exactly

`boxed{t_ref,min(tau)=lambda_max[C(tau)^-1/2 A C(tau)^-1/2]}`.

Therefore the minimum pure-dead overhead/live ratio is

`boxed{r_mat^*=min_tau t_ref,min(tau)/tau}`

with the minimization over the admissible interval above.

### RQIR-RESOURCE-072 — matrix recertification envelope

A correlated multivariate control whose reference is pure dead time is reduced to a **one-dimensional cadence optimization**, regardless of the number of controlled gain/phase coordinates. The full Fisher/drift/tolerance orientation is retained inside the generalized eigenvalue.

No scalarization or arbitrary choice of amplitude/phase basis is required.

## 4. Scalar recovery

For one coordinate,

`F_ref=R_ref`, `Q=D`, `S=sigma_*^2-sigma_f^2`.

Then

`A=1/(R_ref S)`, `B=D/S`.

The exact optimum is

`tau*=S/D`,

`t_ref*=2/(R_ref S)`,

`r_mat^*=2D/(R_ref S^2)`.

Thus RESOURCE-072 reproduces RESOURCE-067 exactly.

The deterministic regression uses `R_ref=3.7`, `D=2.3`, `S=0.8` and obtains

- numerical `r*=1.94256759`;
- analytic `r*=1.94256757`;
- numerical `tau*=0.34786`;
- analytic `tau*=0.347826`.

The small mismatch is only dense-grid resolution.

## 5. Coordinate invariance

For a nonsingular reparameterization `y=M x`,

`S_y=M S_x M^T`,

`Q_y=M Q_x M^T`,

`F_y=M^-T F_x M^-1`.

The physical constraint and `r_mat^*` are invariant.

The stored 2D regression changes to a nonorthogonal coordinate basis and reproduces `r_mat^*` to relative `~1.4e-15` in the numerical audit.

### RQIR-NG-068 — scalar gain/phase loads are basis dependent in the correlated case

If `F_ref`, `Q`, or the admissible covariance budget has correlated/off-diagonal structure, assigning independent amplitude and phase overheads and summing them can change under reparameterization and can miscount a shared reference block.

Use RESOURCE-072 unless the declared physical likelihood genuinely factorizes into independent reference blocks and independent stability processes.

## 6. Orientation matters even when spectra are identical

A deterministic 2D regression uses `S=I` and the same eigenvalue spectra

`eig(F_ref)={1,100}`,

`eig(Q)={1,100}`

in two cases.

Only the relative orientation is changed.

When the strongest reference-Fisher direction is aligned with the fastest drift direction,

`r_mat^* ~= 51.005`.

When the Fisher eigenvectors are swapped relative to the drift eigenvectors,

`r_mat^* ~= 200.000`.

The orientation penalty is therefore about

`boxed{3.92x}`

in this dimensionless regression despite identical marginal Fisher and drift spectra.

This is not an apparatus number. It is a counterexample showing that lists of per-coordinate precisions/rates do not determine multivariate recertification cost.

### RQIR-DESIGN-016 — co-design reference Fisher with drift eigenmodes

For complex transfer control, engineering effort should be directed toward the generalized modes that are simultaneously fast-drifting, tightly budgeted and weakly observed by the reference likelihood. Marginal amplitude/phase SNR alone is not the correct design objective.

## 7. Architecture-decision headroom

Iteration 111 defines a remaining Toy014 pure-dead control headroom `K` after the other control loads are accounted for.

For a joint gain/phase block, replace the scalar term `h_gain+h_phase` by `r_mat^*`.

The detector-side control condition is

`boxed{r_mat^* < K_gain-phase}`.

If the entire same-state transfer Fisher-rate matrix can be increased by a common scale `kappa`,

`F_ref -> kappa F_ref`,

then `A -> A/kappa` and therefore exactly

`r_mat^*(kappa)=r_mat^*(1)/kappa`.

Hence

`boxed{kappa_req = r_mat^*(1)/K_gain-phase}`

is the required common Fisher-rate speedup at the architecture boundary.

### RQIR-RESOURCE-073 — matrix reference-rate headroom gate

A joint complex-gain recertification channel can be inserted directly into RESOURCE-069/071 through `r_mat^*`; a uniform improvement of its transfer-reference Fisher matrix has an exact inverse-linear effect on the pure-dead load.

Anisotropic improvements require re-evaluating RESOURCE-072 rather than scaling one scalar SNR.

## 8. Relation to Iterations 101–103

Iteration 101 already defines the same-state complex dual-tone calibration likelihood

`F_cal = J_chi^T Sigma_z^-1 J_chi`

per block.

Its physical Fisher-rate matrix can therefore become the `F_ref` input to RESOURCE-072 once a candidate apparatus supplies:

- actual same-state block duration and acceptance;
- measured full transfer-score covariance;
- time-series drift/diffusion matrix `Q` for the complex transfer coordinates;
- irreducible stability floor `Sigma_f`;
- a declared admissible covariance budget `Sigma_*` derived from the profiled science likelihood.

No new transduction convention is needed beyond the complex transfer coordinates already used in Iterations 101–103.

What remains missing is the **measured or defensibly specified time-domain stability process**, not the algebraic Fisher bridge.

## 9. Scope guard

RESOURCE-072/073 applies when the recertification block is genuinely pure dead time relative to the science likelihood.

If transfer references are injected simultaneously with science, if the same block carries science Fisher, or if transfer drift is estimated continuously from the science record, use the full RESOURCE-064 campaign Fisher scheduler instead of adding `r_mat^*` as a dead-time load.

Likewise, singular control directions require explicit support reduction before inversion; do not hide them with a pseudoinverse threshold.

## 10. What this iteration closes

Closed:

- exact multivariate pure-dead recertification formula;
- scalar Iteration-109 recovery;
- coordinate invariance;
- an explicit orientation counterexample;
- direct architecture-headroom insertion for joint gain/phase control;
- exact scaling with a common reference-Fisher-rate improvement.

Still open:

- physical same-apparatus `Q`, `Sigma_f` and `Sigma_*` intervals for Toy009/Toy014;
- whether gain/phase recertification is pure dead time or should be embedded in the joint campaign scheduler;
- geometry and additive SI stability/reference likelihoods;
- robust numerical `u` interval and final Toy009/Toy014 apparatus decision.

## 11. Next admissible gate

Use the science likelihood itself to derive the admissible **complex-transfer covariance budget `Sigma_*`** rather than assigning independent 5.13% amplitude and arbitrary phase tolerances. This can be done locally from the profiled-Fisher loss Hessian / generalized gain nuisance block of Iterations 102–103.

That step would connect the gain/phase control target to detector-level `F_beta|theta` in a basis-invariant way. If a physical drift matrix remains unavailable afterwards, report the resulting `Q` threshold surface symbolically rather than fabricate apparatus stability.

## 12. Reproducibility

Run

`python analysis/matrix_gain_phase_recertification_iteration112.py`.

The script asserts scalar recovery, coordinate invariance and the orientation-sensitive 2D regression and prints `PASS` when all checks succeed.
