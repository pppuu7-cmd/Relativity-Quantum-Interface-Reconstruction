# Candidate Gravity Iteration 138 — positive-spectral continuum ansatz

**Date:** 2026-08-31  
**Model:** `ANSATZ-RQIR-KL-002` v0.1  
**Decision:** START / DRAFT_TESTING

## Motivation from the rejected model

Iteration 136 proved that `ANSATZ-RQIR-CTP-001` v0.1 has an unavoidable extra below-threshold timelike zero with opposite residue sign for every frozen `beta>0`. The next candidate therefore changes the dynamical architecture rather than tuning the rejected function.

The new design principle is:

> Put positivity in the physical two-point spectral measure itself, so absence of isolated negative-residue poles is structural at the Gaussian level.

## Spectral definition

`rho_g(mu^2)=delta(mu^2)+(beta/M_*^2) exp(1-mu^2/M_*^2) Theta(mu^2-M_*^2)`,

with `beta>=0`, `M_*>0`.

The retarded scalarized spin-2 transfer is

`D_R(p)=int_0^infty dmu^2 rho_g(mu^2)/(p^2-mu^2+i0p^0)`.

The massless GR pole is unchanged. The added sector is a smooth positive continuum beginning at `M_*^2`, not an isolated pole.

## First scoped results

### Positive spectral measure

The continuum density is nonnegative by construction and normalized to integrated weight `beta`.

### Retarded causal support

`D_R` is a linear superposition of standard retarded spectral components. Retarded support is therefore preserved at the Gaussian level.

### Absorptive sign

For positive frequency and `p^2>M_*^2`,

`Im D_R,cont=-(pi beta/M_*^2) rho_hat(p^2/M_*^2)<=0`

in the frozen scalar retarded convention, corresponding to nonnegative spectral weight.

### No isolated added pole

The smooth continuum generates a branch cut at `p^2>=M_*^2`. There is no extra continuum delta function and hence no analogue of the Iteration-136 isolated pole.

### Long-range Newtonian recovery

The static potential has

`Phi(r)=-GM/r [1+beta W(M_*r)]`,

`W(u)=int_1^infty ds exp(1-s) exp(-u sqrt(s))`.

Since `sqrt(s)>=1`,

`0<W(u)<=exp(-u)`.

Therefore

`|delta Phi/Phi_GR|<=beta exp(-M_*r)`.

The massless long-range `1/r` term is unchanged. Full tensor/PPN normalization remains open.

## Reproducible numerical audit

Files:

- `analysis/candidate_gravity_positive_spectral_iteration138.py`;
- `results/candidate_gravity_positive_spectral_iteration138.json`.

Recorded result: `PASS_SCOPED`.

Representative `W(u)` values:

| `u=M_*r` | `W(u)` | `exp(-u)` bound |
|---:|---:|---:|
| 0.1 | 0.8716151239 | 0.9048374180 |
| 1 | 0.2630346632 | 0.3678794412 |
| 5 | 0.0021013831 | 0.0067379470 |
| 10 | 8.0716e-6 | 4.53999e-5 |

## RQIR fingerprint

The same `(beta,M_*)` controls:

1. finite-range static transfer;
2. dynamic branch-cut/absorptive threshold;
3. Gaussian gravitational spectral fluctuations.

The first serious discriminator should use at least two of these sectors simultaneously. A static fifth-force-like anomaly alone is too easy for C0/C4 nuisance models to mimic.

## Current bottlenecks

### QG-005 — full tensor/helicity consistency

The positive scalar spectral representation is not enough. We must construct the conserved-source tensor sector and determine whether the continuum can be completed without negative-norm helicities, bad constraints or Bianchi/Ward failure.

### QG-007 — comparator degeneracy

Positive continua are known structures. The new ansatz may be operationally equivalent to:

- the interaction-generated continuum of perturbative quantum GR;
- hidden/KK/unparticle-like spin-2 mediators;
- nonlocal/form-factor gravity;
- sufficiently general stochastic classical transfer models at two-point level.

If so, `KL-002` will be retained as a comparator/control and the next candidate must add a structural relation that those classes cannot reproduce.

## Article significance already available

Iterations 135–138 produce a useful methodological sequence:

1. RQIR-driven construction;
2. scoped Euclidean pass;
3. independent Lorentzian gate finds an analytic failure;
4. failed version is frozen and rejected rather than retuned;
5. the next architecture incorporates the negative theorem as a design constraint;
6. existing theory classes are simultaneously audited as funnel comparators.

This sequence is suitable for a methods/results section even if `KL-002` is later rejected.

## Frozen next step

**Iteration 139:** full tensor/helicity and C5-continuum comparison preparation.

The priority order is:

1. write the most conservative tensor spectral decomposition compatible with conserved sources;
2. audit massless vs massive/continuum projector content and residue positivity;
3. determine the unavoidable scalar/helicity-0 contribution, if any, and its Newtonian/PPN consequence;
4. freeze the corresponding C5 spectral baseline at the same perturbative order;
5. only then decide whether a nonzero candidate spectral direction exists for Paper I.
