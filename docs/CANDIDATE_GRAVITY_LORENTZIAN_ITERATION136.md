# Candidate Gravity Iteration 136 — Lorentzian sub-threshold pole rejection

**Date:** 2026-08-31  
**Model:** `ANSATZ-RQIR-CTP-001` v0.1  
**Decision:** REJECT v0.1 at QG-004

## Frozen model under test

Iteration 135 froze

`K_R^(2)=K_GR,R^(2)[1+beta F_R]`, `beta>0`,

with

`F_R=zeta int_1^infty ds exp(1-s)/(s+zeta)`,

`zeta=-(p^2+i0 p^0)/M_*^2`.

No parameter sign or spectral shape is changed in this audit.

## Timelike region below the first cut

For positive frequency and

`y=p^2/M_*^2`, `0<y<1`,

the retarded form factor is real because the spectral support begins at `y=1`:

`F(y)=-y exp(1-y) E1(1-y)`.

Define

`g(y)=y exp(1-y) E1(1-y)>0`,

so `F=-g`.

Let `a=1-y` and `h(a)=exp(a)E1(a)`. Since

`d h/da = h-1/a <0`,

we have

`d h(1-y)/dy = 1/(1-y)-h(1-y)>0`.

Therefore

`g'(y)=h(1-y)+y[1/(1-y)-h(1-y)]>0`,

and hence

`F'(y)<0` on the entire interval `0<y<1`.

Boundary behavior is

`F(0)=0`,

`F(y)->-infinity` as `y->1-`.

## Forced extra pole theorem

For every frozen `beta>0`,

`Q(y)=1+beta F(y)`

is continuous and strictly decreasing with

`Q(0)=1`,

`Q(y)->-infinity` as `y->1-`.

Hence by continuity and monotonicity there exists **exactly one**

`y0 in (0,1)`

such that

`1+beta F(y0)=0`.

Thus v0.1 necessarily introduces an additional real timelike pole below the spectral threshold `M_*`.

For small beta the pole is exponentially close to the threshold. Using

`E1(a)=-gamma-ln(a)+O(a)`

gives

`1-y0 ~ exp[-gamma-1/beta]`.

The pole therefore exists even when finite double-precision scans can miss it for very small beta.

## Residue sign

In the frozen scalarized spin-2 propagator convention

`D~1/[p^2(1+beta F)]`.

At the extra root the derivative of the denominator is proportional to

`y0 beta F'(y0)`.

Since

`y0>0`, `beta>0`, `F'(y0)<0`,

the additional-pole residue factor

`R_extra = 1/[y0 beta F'(y0)]`

is negative relative to the massless GR pole convention used by the ansatz.

Representative numerical values:

| beta | y0=p^2/M_*^2 | 1-y0 | relative residue factor |
|---:|---:|---:|---:|
| 0.1 | 0.9999745091291923 | 2.5490871e-5 | -2.5492170e-4 |
| 1 | 0.7482950903197800 | 0.2517049096802200 | -0.4038256774 |
| 10 | 0.1504373014700336 | 0.8495626985299665 | -0.8960964538 |

## Scientific decision

**QG-004 = FAIL — `EXTRA_NEGATIVE_RESIDUE_TIMELIKE_POLE`.**

The v0.1 model is rejected and retained as a negative-control branch.

This is stronger than merely finding a bad benchmark point: the failure is analytic for every `beta>0` in the frozen version.

## Why Iteration 135 was still useful

Iteration 135 proved a correct scoped statement: there is no extra zero on the Euclidean/spacelike axis. Iteration 136 shows why the RQIR Candidate-Gravity funnel requires a separate Lorentzian analytic-structure gate. Euclidean stability alone was insufficient.

This produces retained negative result **CG-NG-004**:

> A positive-beta Stieltjes-type multiplicative spectral deformation can be Euclidean-safe yet Lorentzian-inconsistent because the below-threshold continuation forces an opposite-residue timelike pole.

## Reproducibility

- `analysis/candidate_gravity_lorentzian_iteration136.py`
- `results/candidate_gravity_lorentzian_iteration136.json`

## Next design constraint

A replacement ansatz must avoid the theorem above structurally, not by tuning after inspection. At minimum it must prevent a continuous real below-threshold kernel factor from running from `+1` to `-infinity` while preserving the required causal/spectral sign and the GR infrared limit.

Possible new branches must be treated as materially new model versions and independently audited for spectral positivity, gauge consistency, comparator degeneracy and RQIR identifiability.
