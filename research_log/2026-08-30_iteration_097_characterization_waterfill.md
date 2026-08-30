# RQIR Research Log — Iteration 097

**Date:** 2026-08-30  
**Track:** Paper III robust apparatus characterization.

## Result

Derived the exact finite-time allocation law for locally smooth independent Fisher-limited characterization channels.

With

`W ~= W_const + sum_i c_i/sqrt(I_i0+R_i t_i)`

and fixed total characterization time, convexity gives the global KKT optimum

`t_i(lambda)=max(0,[(c_i R_i/(2 lambda))^(2/3)-I_i0]/R_i)`,

with `lambda` chosen by `sum t_i=T_char`.

### New labels

- **RQIR-RESOURCE-050:** decision-weighted characterization water-filling law.
- **RQIR-NG-050:** equal characterization time or equal fractional uncertainty contraction is generally suboptimal.

The initial marginal reproduces Iteration 096 exactly:

`Xi_i=(1/2) Lambda_i R_i h_i^2`.

## Regression

Using the synthetic Iteration-094 box and equal normalized characterization Fisher rates only as a deterministic test:

- at `T=0.1`, only Toy014 `R_src` is active;
- at `T=1`, time splits between Toy014 and Toy009 `R_src`;
- at `T=3`, Toy014 `A` and duty also enter;
- all active channels finish with equal marginal decision value;
- the optimum beats equal-time allocation.

No hardware meaning is attached to these normalized times.

## Guardrails

Use the floor-aware Iteration-096 law for systematic floors. For correlated posterior updates use a joint Fisher/covariance model. NG-048 remains active at eigenvalue/corner/active-set switches.

## Next

Build a declared Toy009/Toy014 primitive characterization table with central values, uncertainty widths, physical characterization Fisher rates, floors/correlations and duty/cost.  Use externally sourced/measured apparatus quantities or explicitly parameterized design-envelope values; do not manufacture a hardware forecast.
