# RQIR Research Log — Iteration 113

**Date:** 2026-08-31

## Goal

Derive the admissible complex-transfer uncertainty budget from detector-level profiled Fisher geometry rather than assign independent amplitude/phase tolerances.

## Main derivation

After exact hard-constraint elimination and profiling all non-transfer nuisance coordinates, write

`J_bar=[[F0,b^T],[b,G]]`.

An independent transfer reference contributes Fisher `C` in the same coordinates, so

`F_beta(C)=F0-b^T(G+C)^-1 b`.

For target retained fraction `q`,

`F_beta(C)>=qF0`

is exactly equivalent to

`RESOURCE-074: G+C >= b b^T/[(1-q)F0]`.

For covariance `Sigma=C^-1`, the exact admissible object is therefore a set rather than a unique full covariance matrix.

## NG-069

There is generally no unique largest full `Sigma_*` in Loewner order for scalar-beta retention. A full SPD tolerance matrix can overconstrain transfer directions that are weakly coupled to the science amplitude.

## Science-coupled transfer mode

Define

`B=b^T G^-1 b`, `ell0=B/F0`, `q_free=1-ell0`.

If `q>q_free`, define

`kappa*=ell0/(1-q)-1`,

`a=b/sqrt(B)`.

Then the targeted rank-one reference

`RESOURCE-075: C*=kappa* a a^T`

satisfies `F_beta(C*)=qF0` exactly.

The equivalent likelihood-derived variance budget is

`a^T Sigma a <= 1/kappa*`.

Thus only the generalized transfer coordinate `eta=a^T g` needs a scalar beta-retention budget in the canonical targeted design.

## Physical recertification bridge

For same-state transfer reference Fisher-rate matrix `F_ref`, drift covariance rate `Q` and floor `Sigma_f`, define

`R_eta=1/[a^T F_ref^-1 a]`,

`D_eta=a^T Q a`,

`sigma_f,eta^2=a^T Sigma_f a`,

`S_eta=1/kappa*-sigma_f,eta^2`.

If `S_eta>0`,

`RESOURCE-076:`

`t_ref*=2/(R_eta S_eta)`,

`tau*=S_eta/D_eta`,

`r_eta*=2D_eta/(R_eta S_eta^2)`.

If `S_eta<=0`, reference speed cannot rescue the requested retention.

## Regression results

A deterministic four-real-component test with free-transfer loss fraction `0.8`, `F0=3` and `q=0.9` gives

- `kappa*=7`;
- exact profiled `F=2.7`;
- exact LMI boundary saturation to floating precision.

The scalar fully aligned regression recovers NG-005/NUM-006:

- raw `F0=25`, q=0.9 -> `C=225`, `F=22.5`, Gaussian prior sigma `1/15=6.67%`;
- final target `F=25` at q=0.9 -> raw `F0=27.7777778`, `C=250`.

## NG-070

Iteration-101's `5.13%` transfer-amplitude target is a deterministic worst-case attenuation bound. The new `6.67%` scalar example is a Gaussian nuisance-prior standard deviation. They have different uncertainty semantics and must not be substituted for one another.

## Active frontier

Next: compute source-specific `(F0,b,G)` for Toy009/Toy014 and compare their science-coupled transfer modes against the same-state dual-tone reference Fisher geometry. Keep physical stability symbolic unless the same-apparatus drift/floor data exist.
