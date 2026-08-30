# RQIR Recovery Delta — Iteration 113

**Date:** 2026-08-31  
**Parent front:** Iteration 112.

## New result

The admissible complex-transfer uncertainty is now derived directly from detector-level profiled Fisher geometry.

After profiling all non-transfer nuisances, write

`J_bar=[[F0,b^T],[b,G]]`.

With independent transfer-reference Fisher `C`,

`F_beta(C)=F0-b^T(G+C)^-1 b`.

### RESOURCE-074 — exact transfer-retention LMI

For retained fraction `q`,

`F_beta(C)>=qF0`

iff

`G+C >= b b^T/[(1-q)F0]`.

### NG-069 — no unique full covariance budget

For `C=Sigma^-1`, the exact admissible object is the set

`{Sigma>0: G+Sigma^-1 >= b b^T/[(1-q)F0]}`.

A unique full SPD `Sigma_*` is generally not determined by scalar-beta retention and can over-calibrate science-insensitive transfer directions.

### RESOURCE-075 — science-coupled transfer mode

Define

`B=b^T G^-1 b`, `ell0=B/F0`, `q_free=1-ell0`.

If `q>q_free`,

`kappa*=ell0/(1-q)-1`,

`a=b/sqrt(B)`,

`C*=kappa* a a^T`.

Then exactly

`F_beta(C*)=qF0`.

Equivalent covariance certificate:

`a^T Sigma a <= 1/kappa*`.

### RESOURCE-076 — likelihood-derived transfer recertification

For reference Fisher-rate matrix `F_ref`, drift covariance rate `Q`, floor `Sigma_f`,

`R_eta=1/[a^T F_ref^-1 a]`,

`D_eta=a^T Q a`,

`sigma_f,eta^2=a^T Sigma_f a`,

`S_eta=1/kappa*-sigma_f,eta^2`.

If `S_eta>0`,

`t_ref*=2/(R_eta S_eta)`,

`tau*=S_eta/D_eta`,

`r_eta*=2D_eta/(R_eta S_eta^2)`.

If `S_eta<=0`, the stability floor alone violates the target.

### NG-070

The Iteration-101 deterministic `5.13%` hard amplitude-retention bound and a Gaussian nuisance-prior covariance are different uncertainty semantics and must not be interchanged.

Scalar NG-005/NUM-006 regression is recovered exactly: raw `F0=25`, q=0.9 -> `C=225`, `F=22.5`; final `F=25` at the same retention requires raw `F0=27.7777778`, `C=250`.

## Files

- `analysis/transfer_likelihood_covariance_budget_iteration113.py`
- `docs/PAPER_III_LIKELIHOOD_TRANSFER_BUDGET_ITERATION113.md`
- `research_log/2026-08-31_iteration_113_likelihood_transfer_budget.md`

## Next gate

Compute source-specific conditional transfer objects `(F0,b,G)` for Toy009 and Toy014 under one common detector likelihood, derive `a_09,a_14,kappa_09,kappa_14`, and compare them with the same-state reference Fisher geometry. Do not invent physical drift/floor data; retain normalized or symbolic certificates where required.
