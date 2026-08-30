# RQIR Recovery Delta — Iteration 109

**Date:** 2026-08-30  
**Parent front:** Iteration 108.

## What changed

Control recertification now has a physical Fisher-rate envelope rather than only source-specific toy tolerances.

For a scalar control coordinate with usable variance budget

`S=sigma_*^2-sigma_floor^2`,

Brownian drift `Var=D t/2`, and reference Fisher rate `R_ref`, the optimal pure-dead recertification split is

`RESOURCE-067:`

`sigma_ref^2=S/2`, `t_ref^*=2/(R_ref S)`, `tau_live^*=S/D`,

`r_min=2D/(R_ref S^2)`.

For a target overhead/live ratio `r_max`,

`RESOURCE-068:`

`R_ref >= 2D/[r_max S^2]`.

New guards:

- **NG-065:** tolerance alone does not determine reference time; physical drift/floor and Fisher rate are required.
- **NG-066:** normalized additive tolerances are not cross-source SI controls without a common transduction and stability/reference likelihood.

Physical timing comparison:

- Toy009 D2 `sigma_t~=9.19001083 us`;
- Toy014 `sigma_t~=3.97715 us`;
- equal-`D`, equal-overhead, equal-reference-normalization requirement:
  `R_ref,14/R_ref,09~=28.5086209`.

This does not contradict Iteration 108: fixed-block timing-only rate corrections remain sub-percent over its transparent `D=100–1000 us^2/h` benchmark.

Control-cut status:

- timing: parameterized/partial;
- geometry: open physical transduction/drift/reference Fisher;
- additive mean/covariance: open physical transduction/drift/reference Fisher;
- gain/phase: same-state injected Fisher formalism exists, stability/recertification process open.

`DESIGN-014:` after physical Fisher schedules exist, rank control measurements by architecture-decision shadow price. For binding quota `b_ij`, `lambda_ij=-dR_D,i/db_ij`, and detector elasticity `E_u`,

`d ln G/db_14,j=-E_u lambda_14,j/R_D,14`,

`d ln G/db_09,j=+E_u lambda_09,j/R_D,09`.

## Files

- `analysis/control_recertification_fisher_envelope_iteration109.py`
- `docs/PAPER_III_CONTROL_RECERTIFICATION_FISHER_ENVELOPE_ITERATION109.md`
- `research_log/2026-08-30_iteration_109_control_recertification_fisher_envelope.md`

## Next admissible gate

Build a parameterized control-threshold surface for constrained `u` using measurable `(R_ref,D,sigma_floor)` and RESOURCE-067/068 quotas. Keep missing geometry/additive/gain SI rates symbolic or interval-bounded; do not fabricate an apparatus winner. Then combine with robust `(v,z,delta)` via RESOURCE-063/NG-030.
