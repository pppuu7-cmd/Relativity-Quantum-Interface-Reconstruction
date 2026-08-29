# RQIR Recovery Delta — Iteration 060

**Date:** 2026-08-30

## New retained result

**RQIR-RESOURCE-028:** On balanced Toy012, the wall-clock-optimal centered relational-covariance subset depends on the independent source-metrology Fisher rate. Covariance and source-amplitude Fisher are substitutable nuisance resources with different acquisition costs.

Resource-relevant branches at `f_gap=100 Hz`, `p=0.5`, `dead=1 ms`:

- k4 `(2,4,5,6)`: `C_alpha*=15.0619395586`, `rho^2=2`, covariance floor `19.83028348 h`;
- k5 `(2,3,4,5,6)`: `C_alpha*=13.8194786356`, `rho^2=(5+sqrt(5))/2=3.618033989`, covariance floor `35.87331982 h`;
- all8: `C_alpha*=13.6694147191`, `rho^2=6`, covariance floor `59.49085045 h`.

Crossings:

- k4 -> k5 at `R_alpha=2.15126380613e-5 s^-1`;
- k5 -> all8 at `R_alpha=1.76497796977e-6 s^-1`.

Toy012 mean-calibration lower bound for two independent seven-layer families:

`T_mean = 52.04402941 / xi_mu^2 h`.

At `xi_mu=3`, `T_mean=5.782669934 h`.

## Important limitations

- `xi_mu` remains a normalized row sensitivity, not yet an SI apparatus parameter.
- Covariance times are optimistic graph/Fisher lower bounds, not a complete detector likelihood.
- Independent source-metrology rate `R_alpha` must already include reset/preparation/visibility penalties from Iteration 058.
- No new-physics or experimental-feasibility claim.

## Next executable gate

Attach physical force transduction and detector equivalent-force PSD/ASD to Toy012 direct-force mean rows, convert `gamma_mean` into actual shot/time requirements, then combine with absolute D2 science Fisher rate on one common physical parameter budget.
