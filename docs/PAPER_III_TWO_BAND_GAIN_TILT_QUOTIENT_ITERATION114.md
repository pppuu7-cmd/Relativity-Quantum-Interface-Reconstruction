# RQIR Iteration 114 — Two-Band Gain/Tilt Quotient Certificate

**Date:** 2026-08-31  
**Status:** Paper-III detector/transfer resource gate. Exact local two-real-band reduction; no apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 113 showed that scalar-beta transfer calibration is governed by a science-coupled transfer mode rather than by arbitrary independent amplitude/phase tolerances. For the current mature two-real-band D2 likelihood, an even stronger exact reduction is available before any apparatus-specific complex phase model is introduced.

The two fractional band gains span exactly the same local score space as the common science amplitude `beta` and the retained antisymmetric spectral-tilt nuisance. Therefore the amplitude-only transfer problem can be quotiented analytically. The remaining transfer bottleneck is one common-gain reference Fisher, while differential gain is locally redundant with the already-profiled spectral tilt.

## 2. Two-band score geometry

Let the two real matched-filter science amplitudes be `s=(s2,s4)` with positive-definite precision matrix `W`.

The scalar interface-amplitude score is

`v_beta=(s2,s4)`.

The retained relative spectral-tilt score is

`v_q=(-s2,s4)`.

Introduce local fractional transfer gains `(g2,g4)` with score columns

`v_g2=(s2,0)`, `v_g4=(0,s4)`.

Define common/differential gains

`g2=c-d`, `g4=c+d`.

Then exactly

`v_c=v_g2+v_g4=(s2,s4)=v_beta`,

`v_d=-v_g2+v_g4=(-s2,s4)=v_q`.

Hence `span{v_g2,v_g4}=span{v_beta,v_q}` whenever both science bands are nonzero.

### RQIR-NG-071 — free per-band gains retain an exact common-amplitude degeneracy

With unconstrained fractional gains in both retained bands,

`F_beta|tilt,g2,g4=0`

regardless of science exposure, source harmonic balance or positive-definite detector covariance.

Source redesign can rotate/reweight the transfer mode seen by a reference, but cannot eliminate this local common-amplitude degeneracy while both per-band gains remain free.

## 3. Quotient the transfer reference by differential gain

Let a same-state dual-tone reference provide a symmetric PSD Fisher matrix `C_g` in per-band gain coordinates `(g2,g4)`.

Use

`T=[[1,-1],[1,1]]`

so `(g2,g4)^T=T(c,d)^T`. The reference Fisher in `(c,d)` is

`C_cd=T^T C_g T`.

Write it as `[[C_cc,C_x],[C_x,C_dd]]`.

Because differential gain is science-degenerate with the free spectral tilt, the useful reference Fisher on common gain after profiling differential gain is

`boxed{C_com=C_cc-C_x^2/C_dd}`

for `C_dd>0`.

If `C_dd=0`, PSD implies `C_x=0`, and a direct common-mode reference contributes `C_com=C_cc` on its exact support.

### RQIR-RESOURCE-077 — common-gain quotient Fisher

For positive-definite

`C_g=[[C22,C24],[C24,C44]]`,

`boxed{C_com=4 det(C_g)/(C22+C44-2 C24)}`.

The transfer calibration therefore enters as a Schur complement, not as a sum of marginal gain SNRs.

## 4. Independent dual-tone reference

For independent band-gain Fisher values `C2,C4`,

`C_g=diag(C2,C4)`

and

`boxed{C_com=4 C2 C4/(C2+C4)}`.

At fixed independent calibration budget `C2+C4=C_tot`,

`C_com<=C_tot`,

with equality at `C2=C4=C_tot/2`.

### RQIR-DESIGN-017 — balance independent transfer calibration across retained bands

If calibration genuinely consists of two independent band references, over-calibrating one band cannot compensate for a weakly calibrated partner. Balance their Fisher allocation unless the apparatus supports a more direct common-mode reference.

A direct rank-one common-gain reference is allowed and need not be artificially split.

## 5. Exact beta Fisher after gain/tilt quotient

First profile the spectral tilt from science:

`F_s=s^T W s-(s^T W v_q)^2/(v_q^T W v_q)`.

After adding the gain-reference matrix and profiling differential gain plus tilt,

`boxed{F_beta=F_s C_com/(F_s+C_com)}`,

hence

`boxed{1/F_beta=1/F_s+1/C_com}`.

The stored deterministic script checks this against the full Fisher matrix `(beta,g2,g4,q)` over 300 random SPD science/reference problems.

## 6. Fixed-retention target

For retained fraction `q`,

`F_beta>=q F_s`

iff

`boxed{C_com >= [q/(1-q)] F_s}`.

At `q=0.90`, `C_com>=9 F_s`.

For a final target `F_*=25` at fixed 90% retention,

`F_s=25/0.9=27.7777778`,

`C_com=250`.

Thus the Fisher target is architecture-independent; its wall-clock accumulation rate is not.

## 7. Rate form and optimal schedule

Let `R_s` be the transfer-fixed, tilt-profiled science rate and `R_c` the common-gain quotient reference rate. For separate campaign times,

`F_s=R_s T_s`, `C_com=R_c T_c`.

Then

`1/F_beta=1/(R_s T_s)+1/(R_c T_c)`.

Therefore

`T_s/T_c=sqrt(R_c/R_s)`,

`T_min=F_*[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

### RQIR-RESOURCE-078 — detector+common-transfer effective rate

`boxed{R_DT=1/[1/sqrt(R_s)+1/sqrt(R_c)]^2}`.

This is the minimum-wall-clock effective rate for current two-real-band science plus a separate amplitude-transfer reference, before seven calibration layers, source metrology and other controls.

## 8. Architecture ratio before remaining controls

For Toy014/Toy009 define

`s=R_s,14/R_s,09`, `c=R_c,14/R_c,09`, `z_c=R_c,09/R_s,09`.

Then

`boxed{u_DT=[(1+z_c^-1/2)/(s^-1/2+(c z_c)^-1/2)]^2}`.

Limits:

- `z_c -> infinity`: `u_DT -> s`;
- if `c=1` and a common transfer reference is very slow, `z_c -> 0`: `u_DT -> 1`.

Thus a common transfer bottleneck can compress a science-rate difference without proving either architecture globally superior.

## 9. Toy014/Toy009 regression slice

Iteration 074 gives the equal-ASD/shared-kernel science-only ratio

`s=0.28301465746`.

This is not a physical common-apparatus detector ratio and is used only as a regression slice.

For illustrative `c=1`:

| `z_c=R_c,09/R_s,09` | `u_DT` |
|---:|---:|
| `0.01` | `0.85738` |
| `0.1` | `0.68148` |
| `1` | `0.48234` |
| `10` | `0.35926` |
| `100` | `0.30873` |

As transfer calibration becomes fast, the ratio approaches `0.28301`; as a shared transfer reference becomes dominant, the architectures approach the same transfer-limited rate.

These are not apparatus predictions.

## 10. Consequence for Toy009/Toy014 transfer burden

At the amplitude-only two-real-band level:

1. both architectures have the same exact beta/common-gain degeneracy type;
2. both require `C_com/F_s=q/(1-q)` at fixed retention;
3. at fixed final Fisher and retention, the required total `C_com` is the same;
4. architecture differences enter through physical rates `R_s` and `R_c`, not through different algebraic `kappa` values;
5. source harmonic balance can alter which reference direction is expensive but cannot remove common-gain calibration.

Therefore the next physical comparison should certify `R_c,09` and `R_c,14` in one common transfer coordinate rather than search for a source with a smaller formal gain-prior coefficient.

## 11. Scope guard

This iteration is exact only for two real sufficient band amplitudes with one free antisymmetric spectral-tilt nuisance and local fractional amplitude gains.

It does not close complex phase directions, finite-window phase/amplitude coupling, nonlinear/intermodulation calibration, transfer-dependent covariance, time-domain stability, geometry or additive controls. Retain Iterations 112–113 matrix/LMI machinery for those cases.

## 12. Next admissible gate

Use the same-state dual-tone reference likelihood of Iterations 101–103 to define the physical common-gain quotient rate `R_c` and its uncertainty interval under one detector operating state. If a source-independent apparatus reference is justified, evaluate `c=1`; otherwise retain `c` as an interval.

Then insert the resulting `R_DT` interval into the seven-layer/control scheduler and update the robust detector-side ratio `u`. Do not invent complex phase stability or SI drift.
