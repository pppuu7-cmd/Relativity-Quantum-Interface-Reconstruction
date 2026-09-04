# Iteration 427 Recovery Delta

**Date:** 2026-09-04  
**MODEL_READINESS:** 24% (unchanged)  
**Authority:** exact analytic contract; non-promoting  
**Raw-valid run:** 33886660110  
**Artifact:** 9942115984  
**Artifact digest:** `sha256:cf92be01da583f07f12fc6b487cea2e3dbb8e178067d9eef3e6af9a54944269e`  
**Raw scientific JSON SHA-256:** `fab84900f469dcdb9bae95f1070ebfedbf967a8f8fb5ef0387ccedb9a4ae2d9b`

## What was established

Iteration 425 showed that the frozen Iteration-407 fixed-mass function has the complete mass dependence

`F(u,v)=1/2 beta(u,v) H(alpha(u,v),rho(u,v))`,

where `H` includes both the traced-numerator / phi-mean polynomial coefficients and the affine analytic moments. Iteration 427 performs the exact chain rule at `u=v=0`, with `s=-q^2>0`, before the active Iteration-421 result is known.

The kinematic derivatives are

- `alpha_0=-1/2`, `alpha_u=-1/(2s)`, `alpha_v=+1/(2s)`, `alpha_uv=0`;
- `rho_0=sqrt(s)/2`, `rho_u=rho_v=-1/(2sqrt(s))`, `rho_uv=-1/s^(3/2)`;
- `beta_0=1`, `beta_u=beta_v=-1/s`, `beta_uv=-2/s^2`.

Substitution into the exact product/chain rule cancels all coefficients multiplying `H_alpha`, `H_rho`, and `H_alpharho`. The exact result is

`D_s := -F_uv(0,0) = H/s^2 + H_alphaalpha/(8 s^2) - H_rhorho/(8 s)`.

For the unresolved target `q^2=-1`, hence `s=1`,

`D_s = H + (H_alphaalpha - H_rhorho)/8`.

The SymPy identity check, coefficient-by-coefficient cancellation check, and target `s=1` specialization all passed in the raw-valid workflow authority.

## Scientific significance

This is not a physical `D_s` value and does not close double-double index 2. It is an exact change of derivative coordinates for the complete frozen representation. If Iteration 421 returns `BLOCKED_CONVERGENCE`, the Iteration-424 high-precision/AD fallback should prefer evaluating the full `H` together with its pure `alpha-alpha` and `rho-rho` second derivatives, rather than another mixed `u,v` finite difference. This removes the first-derivative and mixed `alpha-rho` chain terms algebraically and may substantially reduce the conditioning burden.

Crucially, `H` is the **complete** non-measure fixed-mass function: numerator/phi-mean coefficients plus affine moments. Denominator-only differentiation remains forbidden.

## Guardrails

- prospective before Iteration-421 physical result;
- no physical coordinate promotion;
- no threshold weakening;
- no smaller mass step as a rescue;
- no zero fill;
- no denominator-only shortcut;
- `ANSATZ003` remains uncreated;
- Fisher/resources remain forbidden.

## Next gates

1. Raw-consume Iteration 421 fail-closed.
2. Continue Iteration 426 phi-mean 16-vs-32 diagnostic independently; it is diagnostic-only.
3. If 421 is `CONVERGED`, ignore fallback and execute frozen Iteration-412 exact15 assembly with index 2 appended.
4. If 421 is `BLOCKED_CONVERGENCE`, implement the Iteration-424 fallback using the Iteration-427 exact full-H kinematic-coordinate reduction, preserving the frozen 80/120-digit and consistency thresholds.
