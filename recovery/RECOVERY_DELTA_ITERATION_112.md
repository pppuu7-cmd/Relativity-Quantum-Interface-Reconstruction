# RQIR Recovery Delta — Iteration 112

**Date:** 2026-08-31  
**Parent front:** Iteration 111.

## New Paper-III control result

Complex gain/phase recertification is now treated as a matrix problem rather than as independent scalar amplitude/phase loads.

For

`S=Sigma_*-Sigma_f > 0`,

reference Fisher-rate matrix `F_ref`, drift covariance rate `Q`, reference duration `t_ref`, live cadence `tau`, require

`(t_ref F_ref)^-1 + tau Q/2 <= S`.

Whiten:

`A=S^-1/2 F_ref^-1 S^-1/2`,

`B=S^-1/2 Q S^-1/2`.

For fixed `tau`,

`t_ref,min=lambda_max[(I-tau B/2)^-1/2 A (I-tau B/2)^-1/2]`.

### RESOURCE-072

`r_mat*=min_tau t_ref,min(tau)/tau`, with `0<tau<2/lambda_max(B)`.

The scalar Iteration-109 formula is recovered exactly.

### NG-068

Correlated/shared complex gain/phase controls cannot generally be reduced to basis-dependent independent scalar overheads. The full Fisher/drift/tolerance orientation matters.

Deterministic same-spectrum orientation regression:

- aligned strong-reference/fast-drift case `r*~=51.005`;
- swapped case `r*~=200.000`;
- orientation penalty `~3.92x`.

These are dimensionless regression values, not apparatus forecasts.

### DESIGN-016

Optimize reference Fisher along generalized fast-drift/tight-budget modes, not marginal amplitude/phase SNR.

### RESOURCE-073

Insert a joint pure-dead gain/phase block into Iteration-111 control headroom through `r_mat*`.

For uniform reference-Fisher scaling `F_ref -> kappa F_ref`,

`r_mat*(kappa)=r_mat*(1)/kappa`,

so the architecture-boundary scale is

`kappa_req=r_mat*/K_gain-phase`.

## Reproducibility

- `analysis/matrix_gain_phase_recertification_iteration112.py`
- `docs/PAPER_III_MATRIX_GAIN_PHASE_RECERTIFICATION_ITERATION112.md`
- `research_log/2026-08-31_iteration_112_matrix_gain_phase_recertification.md`

Regression checks cover scalar recovery, coordinate invariance and orientation dependence.

## Active front

Paper I: scientifically closed at Iteration 078.

Paper II: scientifically closed at Iteration 079.

Paper III: active. The algebraic recertification treatment of complex gain/phase is now closed at the matrix level, but physical same-apparatus `Q`, `Sigma_f` and likelihood-derived `Sigma_*` intervals remain open.

Candidate Gravity remains inactive future work.

## Next gate

Derive the admissible complex-transfer covariance budget `Sigma_*` from detector-level profiled-Fisher loss geometry (Iterations 102–103), then combine it with RESOURCE-072. Do not invent drift rates. If physical drift remains unavailable, report a symbolic `Q` threshold surface and continue with the strongest apparatus-independent certificate.
