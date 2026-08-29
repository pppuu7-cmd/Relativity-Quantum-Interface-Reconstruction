# RQIR Research Log — Iteration 049

**Date:** 2026-08-29  
**Target:** replace ideal projective energy-basis source metrology by a finite-resolution QND pointer and derive its physical Fisher-rate optimum.

## Result

Use the accepted-record model

`y|E_i ~ N(r E_i,1)`

for Toy009 energy populations `p_i(alpha)=1/5+0.08 alpha d_i`.

Because the hidden direction obeys both

`sum d_i=0`

and

`sum E_i d_i=0`,

the weak linear energy pointer has no trace or mean-energy sensitivity. Its leading Fisher is

`F_alpha(r) ~= 0.0158603616 r^4`.

This is **RQIR-NG-024 — conserved-moment weak-readout suppression**.

Finite-strength Fisher fractions of the projective energy measurement are about 21.7% at `r=1`, 57.6% at `r=2`, 81.4% at `r=3`, 93.5% at `r=4` and 99.6% at `r=6`.

For a QND diffusive energy monitor `r=2 sqrt(eta kappa_E T)`. With negligible source reset overhead, the Fisher rate is

`R_E=4 p_E eta_E kappa_E F(r)/r^2`.

The rate optimum is

- `r*=0.8677465`;
- `F_alpha(r*)=0.0015568125` per accepted copy;
- only `16.58%` of projective Fisher per copy;
- `R_E,max=0.0082700957 p_E eta_E kappa_E`.

This gives **RQIR-RESOURCE-022**: wall-clock-optimal independent energy metrology is generally finite-strength rather than projective when reset/preparation overhead is negligible.

At the transparent 100-Hz D2 benchmark, Branch 0 beats best4 if

`R_E > 2.13404e-4 s^-1`,

which at the zero-reset pointer optimum requires

`p_E eta_E kappa_E > 2.5804e-2 s^-1`.

Best4 beats best5 for the much weaker condition

`R_E > 2.93e-6 s^-1`.

## Files

- `analysis/qnd_energy_pointer_fisher_iteration049.py`
- `docs/QND_ENERGY_POINTER_FINITE_STRENGTH.md`
- `recovery/RECOVERY_DELTA_ITERATION_049.md`

## Next gate

Include explicit source preparation/reset overhead and optimize the finite-strength pointer rate in `(kappa_E,eta_E,p_E,t_reset)`. The current zero-reset optimum should not be used as a hardware forecast.
