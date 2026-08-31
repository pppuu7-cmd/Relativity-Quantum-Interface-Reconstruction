# ANSATZ-RQIR-KL-002 — positive-spectral continuum gravity

**Version:** 0.1  
**Status:** DRAFT / TESTING  
**Iterations:** 138–139  
**Purpose:** second RQIR-driven Candidate Gravity ansatz, constructed after the analytic rejection of `ANSATZ-RQIR-CTP-001` v0.1. The structural design rule is to make two-point positivity and absence of isolated negative-residue poles manifest at the frozen Gaussian level rather than infer them from Euclidean behavior.

## 1. Core idea

Define the physical weak-field two-point function directly by a nonnegative Källén–Lehmann-type spectral measure rather than multiplying the inverse GR kernel by a function that may cross zero after Lorentzian continuation.

The resolved transfer contains:

1. the ordinary massless GR pole with unchanged residue;
2. a positive continuous massive spin-2 spectral sector starting at scale `M_*`;
3. no additional isolated continuum pole in v0.1.

The continuum weight is controlled by one dimensionless amplitude `beta>=0`. The same spectral measure fixes retarded transfer, absorptive threshold and vacuum Gaussian fluctuations. These are not independent RQIR fit functions.

This is an effective weak-field model, not a UV completion and not yet a novelty claim.

## 2. Frozen spectral measure

`rho_g(mu^2) = delta(mu^2) + (beta/M_*^2) rho_hat(mu^2/M_*^2) Theta(mu^2-M_*^2)`,

with

`rho_hat(s)=exp(1-s) Theta(s-1)`,

`int_1^infty rho_hat(s) ds = 1`,

`beta>=0`, `M_*>0`.

The massless pole has fixed unit spectral weight in the frozen GR normalization and the continuum carries integrated dimensionless weight `beta`.

## 3. Tensor transfer after Iteration 139

For conserved external sources the massless and massive spin-2 exchange tensors are not identical.

The frozen linear tensor amplitude is

`A ~ [T_mn T'^mn - (1/2) T T']/(p^2+i0p^0)`

`    + beta int_1^infty ds rho_hat(s) [T_mn T'^mn - (1/3) T T']/(p^2-M_*^2 s+i0p^0)`.

Equivalently, in Barnes–Rivers language the continuum is a positive `P2` sector while the massless GR exchange contains the standard massless trace coefficient.

This is the conservative linear Fierz–Pauli tensor completion of the continuum. It propagates five physical polarizations for each massive spectral component. No nonlinear Vainshtein screening is assumed in v0.1.

The corresponding scalarized transfer used in Iteration 138 remains useful for spectral positivity, but static normalization must use the full tensor coefficients above.

## 4. Gaussian state / positivity interpretation

At v0.1 the continuum is a generalized free positive-norm spin-2 spectral sector. Its one-particle space may be viewed as a direct integral of positive massive spin-2 sectors weighted by `rho_g`, with the massless GR component separated explicitly.

This supplies a scoped linear positivity/unitarity certificate. It does **not** prove a nonlinear ghost-free interacting completion of a continuum of spin-2 modes.

## 5. Matter coupling

Matter is initially the same scalar QFT used by the C5 reference branch. At linear order the gravitational exchange couples universally to conserved stress energy.

`S_int = -(kappa/2) int d^4x h_mn T^mn`.

The matter source hierarchy remains

`J=<T>`,

`N=1/2 <{delta T,delta T}>`,

`chi_T^R=-i theta <[T,T]>`,

with the frozen RQIR smearing/renormalization conventions.

The gravity spectral measure propagates the hierarchy and fixes its own Gaussian vacuum fluctuation spectrum.

## 6. Causality and spectral positivity

The continuum retarded scalar denominator is

`1/(p^2-M_*^2 s+i0p^0)`.

A nonnegative spectral superposition preserves retarded support.

For positive frequency and `y=p^2/M_*^2>1`,

`Im D_R,cont = -(pi beta/M_*^2) rho_hat(y) <= 0`

in the frozen scalar retarded convention.

The smooth continuum therefore has nonnegative spectral weight and a branch cut beginning at `p^2=M_*^2`, with no isolated added pole.

## 7. Static / Newtonian structure after tensor completion

For two nonrelativistic conserved sources,

massless GR exchange coefficient:

`1 - 1/2 = 1/2`,

massive spin-2 exchange coefficient:

`1 - 1/3 = 2/3`.

Therefore the continuum correction is enhanced by the standard linear vDVZ factor

`(2/3)/(1/2)=4/3`.

The frozen static potential becomes

`Phi(r) = -G M/r [1 + (4/3) beta W(M_* r)]`,

where

`W(u)=int_1^infty ds rho_hat(s) exp(-u sqrt(s))`.

Because `sqrt(s)>=1`,

`0<W(u)<=exp(-u)`.

Hence

`|delta Phi/Phi_GR| <= (4/3) beta exp(-M_* r)`.

The asymptotic long-range GR pole remains unchanged. The vDVZ tensor factor is a real prediction/constraint of the **linear** v0.1 completion, not an automatic rejection because the continuum is gapped and finite-range.

## 8. Traceless-probe cross-channel relation

If one conserved probe is traceless, its trace term vanishes in both the massless and massive exchange amplitudes. Thus the continuum/massless tensor coefficient ratio for the traceless channel is `1`, whereas the nonrelativistic calibration ratio is `4/3`.

After calibrating the continuum strength using a nonrelativistic force measurement, a traceless-probe response carries the fixed relative factor

`3/4`.

This provides an additional RQIR cross-channel fingerprint that cannot be tuned independently of the static force within v0.1.

## 9. RQIR-linked fingerprint

The same `(beta,M_*)` and spectral shape determine:

1. nonrelativistic static transfer with the `4/3` tensor factor;
2. traceless-probe transfer with the linked `3/4` relative relation after NR calibration;
3. dynamic branch-cut/absorptive threshold at `p^2=M_*^2`;
4. Gaussian gravitational spectral fluctuations.

A serious Paper-I discriminator should combine at least two of these manifestations. A single static Yukawa-like anomaly is too easy for C0/C4 nuisance models to mimic.

## 10. Relation to known theory classes

This ansatz is **not claimed novel**. Positive massive spin-2 continua occur or can emerge in generalized spectral fields, extra-dimensional/Kaluza–Klein scenarios, hidden-sector continuum mediators, massive-gravity/DGP-like constructions, interacting spectral representations and nonlocal gravity.

The standard massive spin-2 `-1/3` trace coefficient and vDVZ behavior are known prior physics; their presence here is a consistency/signature result, not a novelty claim.

QG-007 therefore requires explicit comparison with:

- C5 perturbative quantum GR including interaction-generated cuts;
- C4 hidden/KK/unparticle-like spin-2 continua;
- nonlocal/form-factor quantum gravity;
- C2/C3 stochastic classical transfer models;
- nonlinear massive-gravity completions if Vainshtein screening is invoked in any future version.

No Vainshtein mechanism may be imported into v0.1 without defining a materially new nonlinear model version.

## 11. Immediate falsification conditions

Reject/supersede v0.1 if:

- the positive linear spin-2 continuum cannot be embedded in a consistent nonlinear constraint structure;
- a required nonlinear completion introduces negative-norm/Boulware–Deser-type sectors in the relevant domain;
- the fixed vDVZ-linked static/traceless relation is experimentally or internally inconsistent in the parameter region needed for RQIR discrimination;
- the full fingerprint is exactly degenerate with C4/C5/nonlocal/KK comparators;
- the candidate direction is removed by exact calibration/nuisance profiling;
- physical resources are divergent or undefined throughout the admissible domain.

## 12. Current status

Passed/retained scoped results:

- positive spectral measure;
- retarded spectral superposition;
- no isolated added continuum pole;
- linear conserved-source tensor completion with standard massive-spin-2 exchange structure;
- finite-range Newtonian recovery with fixed `4/3` correction coefficient;
- linked `3/4` traceless-vs-NR calibration relation.

Still blocking promotion:

- nonlinear tensor/constraint completion;
- exact comparator distinction;
- finite Paper-I hard-constraint quotient;
- Paper-II profiled Fisher;
- Paper-III resource closure.
