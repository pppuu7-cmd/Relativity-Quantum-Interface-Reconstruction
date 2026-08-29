# RQIR Recovery Delta — Iteration 034

**Date:** 2026-08-29

## Mandatory physical-coordinate correction

Iteration 020 computed `F_Q^(a)~=13.27068619` for the physical single-branch amplitude `a` in `rho(a)=I/5+a Delta0`. Later detector Fisher calculations use a fractional hidden-amplitude nuisance `alpha` with `a=EPS alpha`, `EPS=0.08`.

Therefore the coordinate-consistent source QFI is

`F_Q^(alpha)=EPS^2 F_Q^(a)~=0.0849323916`

per accepted single-branch copy.

At `S_D=1`, 90% retention (`C_alpha=9`) needs about `105.97` accepted single-branch copies or `52.98` independent plus/minus pair equivalents. At historical `S_D=25`, `C_alpha=225` needs about `2649.17` single-branch copies or `1324.58` pair equivalents.

The old `~17 copies for C_a=225` physical mapping is withdrawn for the current fractional-amplitude Fisher. The QFI formula itself remains correct.

**RQIR-NUM-002 — Fisher-coordinate Jacobian rule:** transform Fisher/QFI/rates to one parameter coordinate before comparing them.

Current preparation rate coordinate:

`R_P^(alpha)=p_P eta_P EPS^2 F_Q^(a)/t_P`

per single-branch cycle.

## Mandatory centered-noise correction

The RQIR noise kernel is centered. For a symmetric state pair around `rho0=I/5`, the correct linear covariance-difference row is

`C_AB = sym(A,B) - <A>0 B - <B>0 A`

up to a trace-irrelevant identity term.

Raw symmetrized second moments are equivalent only under exact mean conditioning or when raw second moments are explicitly the measured statistic.

**RQIR-CAL-013 — centered-noise linearization rule.**

Exact Toy009/Toy010 null geometry survives:

- raw rank `24/25`;
- centered rank `24/25`;
- null overlap `1.0` numerically.

## New preferred normalized 90% row weights

Centered covariance derivative, exact trace+energy basis:

- D1: `gamma_mean~1.26572e6`, `gamma_cov~0.621783e6`, allocation gain `~1.09308`;
- D2: `gamma_mean~1.83026e6`, `gamma_cov~0.590127e6`, allocation gain `~1.18719`.

Old Iteration-015 weights remain a raw-second-moment protocol benchmark, not the preferred centered-noise baseline.

## Updated D2 centered results

Fully force-native centered branch:

- rank `22/23`;
- `F_beta(C_alpha=0,lambda=1)~0.0195153`;
- `C_alpha90~7.78026`;
- strong-preparation `lambda90~0.10013`.

Complementary relational+force branch at `y_ref=-4` with both centered covariance families:

- `F_beta(C_alpha=0,lambda=1)~0.905293`;
- `C_alpha90=0`;
- calibration-only `lambda90~0.94149`.

Centered force-covariance selection at `y_ref=-4`:

- best 4 `(0,1,3,7)`: `C_alpha*=0.0500614`;
- best 5 `(0,1,3,6,7)`: `C_alpha*=0`.

Equal-row local break-even using centered `gamma_cov`:

- first four: `q_cov/R_P^(alpha) > ~5.24e5`;
- fifth after first four: `> ~1.18e7`.

## Downstream warning

Revalidate before reuse as current physical numbers:

- Iteration-016 timing/additive priors;
- Iterations 018/021 wall-clock allocations using them;
- raw-covariance D2 branch phase/resource numbers;
- stationary PSD examples for the current Toy009 covariance rows.

Exact Toy009/Toy010 and structural no-go results remain retained.

## Reproducibility

- `analysis/physical_coordinate_centered_covariance_audit_iteration034.py`
- `docs/PHYSICAL_COORDINATE_CENTERED_COVARIANCE_CORRECTION.md`
- `research_log/2026-08-29_iteration_034_physical_coordinate_centered_covariance.md`

## Next action

Audit stationarity and operator ordering of the centered covariance observables. Use a phase-referenced/cyclostationary or repeated two-time likelihood if stationary PSD assumptions fail. Then recompute systematics/control priors on the centered likelihood before the next full wall-clock optimization.
