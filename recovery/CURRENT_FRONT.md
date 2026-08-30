# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 086**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast resource front. Read this pointer plus the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Publication-track status

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III:** ACTIVE. Iterations 080–086 develop the apparatus-rate closure, physical two-band likelihood and its correlation/robustness corrections.

RQIR remains separate from RTK/DSIR. No toy, Fisher, resource or detector result is an empirical new-physics claim.

## Mature backbone

Primary detector inference quantity:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Mandatory retained gates include:

- **NG-005:** an exact gravitational null cannot self-calibrate hidden source amplitude;
- **NG-006/007:** low-rank control degeneracies and low-frequency stability floors can survive arbitrarily high science exposure;
- **NG-023:** H-QND source metrology is not automatically ordered-response nondemolition;
- **NG-025/026:** locality belongs inside co-design; exact rank completion is not finite-noise/resource closure;
- exact hard constraints, centered covariance derivatives and full matrix PSD/cross-PSD Fisher must be used.

## Physical wall-clock backbone

Use

`T_sci = Z^2/R_beta`,

`T_cal = gamma_mean sum_j 1/R_cal,j`,

`T_src = C_prep/R_src`,

with

`C_prep=[r/(1-r)] Z^2`.

For the common `Z=5`, `r=.90` benchmark, `C_prep=225`.

Iteration 077 compresses a physically normalized apparatus to

`x = gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`,

`y = C_prep R_beta/(Z^2 R_src)`,

`m = 1/(1-d)`,

`T_total = m (Z^2/R_beta)(1+x+y)`.

**NG-030:** robust branch dominance requires conservative nonoverlap, `T_i^upper < T_k^lower`.

Iteration 080 defines the seven-layer harmonic calibration throughput

`H_cal = 7/sum_j(1/R_cal,j)`

and

`T_total = m[Z^2/R_beta + 7 gamma_mean/H_cal + C_prep/R_src]`.

**NG-031:** individual science/calibration/source rate floors are not jointly sufficient without explicit time allocation.

## Iteration 081 — absolute-rate identifiability

**NG-032:** normalized Fisher/resource geometry does not determine absolute seconds. Absolute detector/calibration/source rate normalization must come from measured, externally sourced or explicitly declared apparatus data.

**APP-001:** apparatus closure requires science transfer plus full PSD/cross-PSD, seven physical calibration Jacobians/rates, source-metrology acceptance/coupling/visibility/reset/coherence, control-reference stability/duty and uncertainty intervals.

## Iteration 082 — single-resonance frequency incompatibility

A quoted narrowband on-resonance ASD cannot be applied to both RQIR science harmonics separated by a factor two without measured transfer/PSD at both frequencies.

**NG-033:** one narrowband ASD is not a two-band apparatus normalization.

## Iteration 083 — sequential retuning

For retuned settings with raw science informations `P2,P4` and independent gain/relock Fisher `C2,C4`,

`F_beta = P2 C2/(P2+C2) + P4 C4/(P4+C4)`.

**NG-034:** independent unconstrained gains make sequential-retuning science unidentifiable even at arbitrarily large science exposure.

## Iteration 084 — simultaneous independent dual-band rate

For independent simultaneous band rates `r2,r4`,

`R_beta = 4 r2 r4/(r2+r4)`.

**RESOURCE-038:** simultaneous two-band throughput is twice the ordinary harmonic mean.

**NG-035 is retained only in this independent-band (`rho=0`) scope:** for fixed weak band, `R_beta -> 4 r_weak` as the partner rate diverges, and the independent-band target requires each band above `R_*/4`.

## Iteration 085 — correlated dual-band matrix Fisher

For matched-filter raw rates `r2,r4` and effective cross-channel correlation `rho_eff` in an ordinary positive-definite two-channel covariance,

`R_beta = 4 r2 r4/(r2+r4+2 rho_eff sqrt(r2 r4))`, `|rho_eff|<1`.

**RESOURCE-039:** Iteration 084 is exactly the `rho_eff=0` slice.

For balanced rates `r2=r4=r`,

`R_beta=2r/(1+rho_eff)`.

**NG-036:** marginal ASD/PSD values alone do not determine simultaneous two-band `R_beta`; require the cross-PSD/full spectral matrix or a demonstrated negligible cross term.

The Iteration-085 statement `r_partner -> infinity => R_beta -> 4 r_weak` remains correct. Its stronger interpretation as a global ceiling for every correlation is superseded by Iteration 086.

## Iteration 086 — correlated partner optimum correction

Fix `r_weak=b` and define `t=sqrt(r_partner/b)`.

Then

`R_beta/b = 4 t^2/(t^2+1+2 rho t)`

and

`d(R_beta/b)/dt = 8 t(1+rho t)/(t^2+1+2 rho t)^2`.

### RQIR-CORR-001

- For `rho>=0`, partner strength is monotone useful and `sup R_beta=4b`, reached asymptotically.
- For `rho<0`, the global maximum occurs at the finite ratio

`r_partner/b = 1/rho^2`,

with

`R_beta,max = 4b/(1-rho^2)`.

Explicit counterexample to the old global ceiling:

`rho=-0.5`, `b=1`, `r_partner=4` gives

`R_beta=16/3=5.3333333333 > 4b`.

Therefore the optimized weak-band feasibility floor is

- `b >= R_*/4` for `rho>=0`;
- `b >= (1-rho^2) R_*/4` for `rho<0`, provided the anti-correlation is physically measured, stable and the covariance remains well-conditioned.

At fixed total raw Fisher `r2+r4`, balanced rates remain optimal for every ordinary `|rho|<1`.

Near `rho=-1` the formal enhancement is singular/fragile; cross-PSD uncertainty, covariance eigenvalue floor and campaign stability must be propagated before any apparatus claim.

Numerical regression: 1000 random negative-correlation cases agree with the analytic finite optimum to maximum relative discrepancy `~3.33e-15`.

Files:

- `analysis/correlated_partner_optimum_iteration086.py`
- `docs/PAPER_III_CORRELATED_PARTNER_OPTIMUM_ITERATION086.md`
- `research_log/2026-08-30_iteration_086_correlated_partner_optimum.md`
- `recovery/RECOVERY_DELTA_ITERATION_086.md`

## Immediate next gate — Paper III only

Before importing an external/apparatus spectral matrix into the wall-clock certificate, derive an **uncertainty-safe lower bound** on `R_beta` over declared intervals/uncertainty sets for `(r2,r4,rho_eff)` or directly for the full spectral matrix. This is required especially when using negative correlation, where the nominal optimum can be nonmonotone and near-singular enhancement is fragile.

Then obtain/source one simultaneous two-band transfer plus spectral matrix, propagate the same apparatus model through all seven same-time calibration layers to derive `R_cal,j`, add independent `R_src`, control duty and uncertainty intervals, and apply NG-030 to Toy009 versus Toy014.

Do not start Toy015 unless that full rate map shows a genuinely source-dependent bottleneck.

## Discipline

Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
