# RQIR Iteration 086 — Correlated Partner-Band Optimum and Correction to the Weak-Band Ceiling

**Date:** 2026-08-30  
**Status:** Paper-III detector-rate correction/refinement; not an apparatus forecast and not a new-physics claim.

## 1. Purpose

Iteration 085 derived the exact correlated two-band profiled rate

`R_beta = 4 r2 r4/(r2+r4+2 rho sqrt(r2 r4))`,

for positive raw band rates and an ordinary positive-definite two-channel covariance with `|rho|<1`.

Iteration 085 correctly noted the asymptotic limit

`r_partner -> infinity => R_beta -> 4 r_weak`.

However, the subsequent statement that this asymptote is a **global weak-band ceiling for every finite correlation** was too strong. For negative matched-filter correlation, `R_beta` is not monotone in the partner-band rate. A finite partner rate can exceed the asymptotic value `4 r_weak`.

This iteration corrects that overclaim explicitly rather than silently editing the historical result.

## 2. Fixed weak band

Let

`r4 = r_weak = b`,

and define

`t = sqrt(r2/b) > 0`.

Then

`R_beta/b = 4 t^2/(t^2+1+2 rho t)`.

Differentiate with respect to `t`:

`d(R_beta/b)/dt = 8 t (1 + rho t)/(t^2+1+2 rho t)^2`.

The denominator is positive for the ordinary `|rho|<1` positive-definite likelihood.

Therefore the sign is controlled entirely by `1+rho t`.

## 3. RQIR-CORR-001 — finite partner optimum for anti-correlated bands

### Case A: `rho >= 0`

The derivative is positive for all `t>0`.

Hence `R_beta` increases monotonically with partner-band strength and

`sup R_beta = 4 r_weak`,

reached only asymptotically as the partner rate diverges.

The old Iteration-084 weak-band interpretation remains valid in this nonnegative-correlation sector.

### Case B: `rho < 0`

The derivative vanishes at

`t_* = -1/rho`,

so the finite optimum is

`boxed{r_partner/r_weak = 1/rho^2}`.

Substitution gives

`boxed{R_beta,max = 4 r_weak/(1-rho^2)}`.

Because `1/(1-rho^2)>1`, the maximum exceeds the asymptotic `4 r_weak` value.

After the optimum, further increasing only the partner-band raw Fisher **reduces** the profiled common-amplitude information until it approaches `4 r_weak` from above.

This is a nuisance-geometry effect, not a violation of information monotonicity under adding independent data: changing one raw band rate while retaining a correlated covariance changes the relative whitened signal/nuisance geometry rather than merely adding a beta-blind calibration block.

## 4. Explicit counterexample to the over-strong ceiling

Take

`r_weak=1`, `rho=-0.5`.

The finite optimum occurs at

`r_partner = 1/rho^2 = 4`.

Then

`R_beta = 16/3 = 5.333333333333...`,

which is strictly larger than

`4 r_weak = 4`.

Thus the statement

`R_beta <= 4 r_weak`

is false as a global bound when `rho<0`.

The asymptotic statement

`r_partner -> infinity => R_beta -> 4 r_weak`

remains correct.

## 5. Correct target-rate feasibility floor

Optimizing the partner band at fixed weak-band rate gives

`R_beta,max(r_weak,rho) = 4 r_weak`, for `rho>=0`,

and

`R_beta,max(r_weak,rho) = 4 r_weak/(1-rho^2)`, for `rho<0`.

Therefore a target `R_*` requires at least

`boxed{r_weak >= R_*/4}` for `rho>=0`,

but only

`boxed{r_weak >= (1-rho^2) R_*/4}` for `rho<0`,

provided the apparatus can actually realize and stabilize the required anti-correlation and the finite optimal partner ratio.

Examples:

- `rho=-0.2`: minimum weak rate is `0.24 R_*`;
- `rho=-0.5`: minimum weak rate is `0.1875 R_*`;
- `rho=-0.9`: minimum weak rate is `0.0475 R_*`.

These are mathematical likelihood requirements, not hardware promises.

## 6. Near-singular anti-correlation is fragile

The apparent enhancement

`R_beta,max/r_weak = 4/(1-rho^2)`

diverges as `rho -> -1`.

But `|rho|=1` is a singular covariance boundary. Therefore arbitrarily large gains inferred from `rho` extremely close to `-1` are not robust apparatus claims.

A physical use of anti-correlation must include:

1. uncertainty on the estimated cross-PSD/correlation;
2. covariance conditioning/eigenvalue floor;
3. stability of the correlation over the campaign;
4. the same nuisance model used to infer the anti-correlation;
5. a reduced likelihood if the covariance is genuinely rank deficient.

This strengthens, rather than weakens, RQIR-NG-036: the full spectral matrix and its uncertainty are first-class inputs.

## 7. Fixed total raw Fisher budget

A different design problem fixes

`S = r2+r4`.

Let `q=sqrt(r2 r4)`. Then

`R_beta = 4 q^2/(S+2 rho q)`.

For `|rho|<1`, this increases with `q` over the physical domain `0<q<=S/2`.

Hence at fixed total raw band Fisher,

`boxed{r2=r4=S/2}`

remains optimal for every finite `|rho|<1`.

So two distinct design laws coexist:

- fixed weak band + tunable partner: anti-correlation can create a finite asymmetric optimum;
- fixed total raw Fisher: balanced raw rates remain optimal.

## 8. Correction to Iterations 084–085

Retain NG-035 in its original independent-band scope (`rho=0`).

For correlated bands, replace the global statement in Iteration 085 with:

> **RQIR-CORR-001:** the `4 r_weak` value is an asymptotic partner-band limit for every finite `|rho|<1`, but it is a global ceiling only for `rho>=0`. For `rho<0`, the global maximum occurs at `r_partner/r_weak=1/rho^2` and equals `4 r_weak/(1-rho^2)`.

Accordingly, the blanket correlated-band requirement `r_n>R_*/4` is withdrawn for `rho<0`.

## 9. Numerical regression

`analysis/correlated_partner_optimum_iteration086.py` checks:

- the explicit `rho=-0.5`, `(r_weak,r_partner)=(1,4)` counterexample;
- exact finite optimum for several negative correlations;
- monotone positive-correlation approach to `4 r_weak`;
- 1000 random negative-correlation cases against the analytic optimum;
- balanced-band optimality at fixed total raw Fisher.

The 1000-case numerical scan agrees with the analytic negative-correlation optimum to maximum relative discrepancy about `3.33e-15`.

## 10. Scientific consequence

The next apparatus search must not optimize marginal ASD values independently. It should optimize the **full two-band spectral geometry**:

`(r2,r4,rho_eff)`

subject to covariance conditioning and uncertainty.

A deliberately engineered anti-correlated readout could in principle improve the profiled RQIR science rate, but that becomes credible only after the cross-PSD is measured and its stability/uncertainty is propagated through the same likelihood.

This is a detector-inference design result, not evidence for new gravitational physics.
