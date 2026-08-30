# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 077**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast resource front. For current work, read this pointer and the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Active architecture status

- **Toy009:** mature global/statistical reference; literal radius-basis Hamiltonian remains dense/nonlocal.
- **Toy014:** leading balanced exact-nearest-neighbour local D2 candidate after physical multi-resource co-design.
- **Toy013:** retained calibration-specialized local comparison branch; non-dominated only in sufficiently calibration-heavy regimes.
- **Toy011/Toy012:** retained as locality/history and negative-design evidence; no longer leading physical resource branches after the two-band/spectral-tilt corrections and Toy014 search.

## Mandatory mature gates

- **NG-005:** gravitational exact-null cannot self-calibrate hidden source amplitude; independent source metrology is mandatory.
- **NG-006/007:** low-rank controls and stability floors can kill profiled Fisher even at high exposure.
- **NG-023:** H-QND source metrology is not automatically ordered-response nondemolition; strong source metrology belongs on independent/sacrificial copies unless a full same-copy likelihood proves otherwise.
- **NG-025/026:** locality belongs inside co-design; exact rank completion is not finite-noise resource closure.
- Detector comparisons use spectral-tilt-profiled `F_beta|theta`, centered noise derivatives, exact hard constraints, and full same-time 2x2 matrix PSD/cross-PSD Fisher blocks.

## Physical Fisher-rate closure — Iterations 067–071

Use

`T_sci = Z^2/R_beta`,

`T_cal = gamma_mean sum_j 1/R_cal,j`,

`T_src = C_prep/R_src`.

At retained multiplicative source-amplitude fraction `r`,

`C_prep=[r/(1-r)] Z^2`.

For current `Z=5`, `r=.90`, `C_prep=225`.

## Toy014 — Iterations 074–076

Toy014 retained physical same-kernel resource vector relative to Toy009:

`(q_s,q_c,q_p)=(3.53338589945,3.48482822888,0.67054046)`.

It is slower in science/calibration than Toy009 but faster in Ramsey source metrology; it componentwise dominates the previously retained physical Toy011/Toy012 local branches on the audited axes.

Toy014 controls remain source-specific. Its 100-Hz timing target is `~3.97715 us`; unconstrained low-rank timing/geometry/additive controls still collapse final profiled Fisher (NG-006 survives).

Under the declared Brownian timing-reference benchmark, recertification duty carries a fourth-power tolerance penalty but stays below 1% for the illustrative `D=100–1000 us^2/h` cases. This is not an apparatus prediction.

## Iteration 077 — apparatus-rate certificate

Primitive per-architecture inputs:

1. nuisance-profiled detector science Fisher rate `R_beta`;
2. seven same-time dual-probe matrix calibration rates `R_cal,j`;
3. independent source-metrology rate `R_src` including preparation/reset/readout/acceptance/visibility;
4. timing/reference duty `d`.

Compress them to

`x = gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`,

`y = C_prep R_beta/(Z^2 R_src)`,

`m = 1/(1-d)`.

Then

`T_total = m (Z^2/R_beta) (1+x+y)`.

**RQIR-RESOURCE-036:** after the physical likelihood/profile are fixed, the sufficient architecture-selection certificate is `(R_beta,x,y,d)` per branch. Keep all seven `R_cal,j` as audit inputs even though they compress to `x` in total wall clock.

General pairwise dominance:

`q_s(i/k) (m_i/m_k) (1+x_i+y_i) < 1+x_k+y_k`,

where `q_s(i/k)=R_beta,k/R_beta,i`.

This no longer assumes common ASD/transduction/bandwidth/acceptance/reset.

Regression to the old shared-kernel projections is exact:

- Toy014 vs Toy009: `y > 7.6895205385 + 7.5421347000 x` before duty correction;
- Toy013 vs Toy014: `x > 5.9842386660 + 98.2399220663 y`.

**RQIR-NG-030:** a nominal branch crossing is not retained when rate/duty uncertainty intervals overlap. Require conservative `T_i^upper < T_k^lower` for robust architecture dominance.

Files:

- `analysis/apparatus_certificate_iteration077.py`
- `docs/APPARATUS_RATE_CERTIFICATE_ITERATION077.md`
- `research_log/2026-08-30_iteration_077_apparatus_rate_certificate.md`
- `recovery/RECOVERY_DELTA_ITERATION_077.md`

## Immediate next gate

Instantiate the certificate from a repository-backed detector/source-metrology model for at least Toy009 and Toy014: physical profiled `R_beta`, seven full matrix `R_cal,j`, `R_src`, and control duty. Do not invent an absolute ASD merely to force a wall-clock number.

Only begin Toy015 if this measured/declared rate map shows that a source-dependent bottleneck dominates total wall clock; if detector/control characterization dominates similarly across branches, improve the apparatus model instead.

## Discipline

RQIR remains separate from RTK/DSIR. No toy, Fisher, resource or detector-model result is an empirical new-physics detection or a complete theory of quantum gravity. Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
