# ANSATZ-RQIR-KL-002 — positive-spectral continuum gravity

**Version:** 0.1  
**Status:** REFERENCE / NOT PROMOTABLE  
**Iterations:** 138–141  
**Purpose:** second RQIR-driven Candidate Gravity ansatz, retained as a positive-spectral control after passing scoped consistency gates but failing QG-007 by exact Gaussian equivalence to an allowed C4/KK-like mediator continuum.

## 1. Core idea

The model defines the physical weak-field two-point function directly by a nonnegative Källén–Lehmann-type spectral measure.

The resolved transfer contains:

1. the ordinary massless GR pole with unchanged residue;
2. a positive continuous massive spin-2 spectral sector starting at scale `M_*`;
3. no additional isolated continuum pole.

The continuum weight is controlled by one dimensionless amplitude `beta>=0`. The same spectral measure fixes retarded transfer, absorptive threshold and vacuum Gaussian fluctuations.

The model is a useful linear-Gaussian spectral reference but is no longer a candidate for promotion as novel gravity.

## 2. Frozen spectral measure

`rho_g(mu^2) = delta(mu^2) + (beta/M_*^2) rho_hat(mu^2/M_*^2) Theta(mu^2-M_*^2)`,

with

`rho_hat(s)=exp(1-s) Theta(s-1)`,

`int_1^infty rho_hat(s) ds = 1`,

`beta>=0`, `M_*>0`.

## 3. Linear conserved-source tensor transfer

For conserved external sources,

massless GR exchange:

`A_0 ~ [T_mn T'^mn - (1/2) T T']/(p^2+i0p^0)`.

Positive massive spin-2 continuum exchange:

`A_c ~ beta int_1^infty ds rho_hat(s) [T_mn T'^mn - (1/3) T T']/(p^2-M_*^2 s+i0p^0)`.

This is the conservative linear Fierz–Pauli tensor completion of the continuum. It propagates five physical polarizations for each massive spectral component. No nonlinear Vainshtein screening belongs to v0.1.

## 4. Gaussian state / positivity interpretation

The continuum is a generalized free positive-norm spin-2 spectral sector. Its one-particle space is representable as a direct integral of positive massive spin-2 sectors weighted by `rho_g`, with the massless GR component separated explicitly.

This gives a scoped linear positivity/unitarity certificate but not a nonlinear diffeomorphism-complete gravity theory.

## 5. Matter coupling and RQIR hierarchy

Matter is the same scalar QFT used by the C5 reference branch. At linear order the gravitational exchange couples universally to conserved stress energy,

`S_int = -(kappa/2) int d^4x h_mn T^mn`.

Matter source objects remain

`J=<T>`,

`N=1/2 <{delta T,delta T}>`,

`chi_T^R=-i theta <[T,T]>`.

The gravity spectral measure propagates this hierarchy and fixes its own Gaussian vacuum fluctuation spectrum.

## 6. Causality and spectral positivity

For positive frequency and `y=p^2/M_*^2>1`,

`Im D_R,cont = -(pi beta/M_*^2) rho_hat(y) <= 0`

in the frozen scalar retarded convention.

The continuum is a nonnegative retarded spectral superposition and generates a branch cut beginning at `p^2=M_*^2`, with no isolated added pole.

## 7. Static tensor signature

For two nonrelativistic conserved sources,

massless coefficient `1/2`,

massive spin-2 coefficient `2/3`.

Hence the continuum/GR tensor ratio is the standard vDVZ factor

`4/3`.

The frozen static potential is

`Phi(r) = -G M/r [1 + (4/3) beta W(M_* r)]`,

`W(u)=int_1^infty ds rho_hat(s) exp(-u sqrt(s))`,

with

`0<W(u)<=exp(-u)`.

For a traceless conserved probe the trace term vanishes, so after NR calibration the continuum response has fixed relative factor `3/4`.

## 8. RQIR-linked Gaussian fingerprint

The same `(beta,M_*)` determines:

1. NR static transfer with the `4/3` factor;
2. traceless-probe transfer with the linked `3/4` relation;
3. dynamic threshold absorption;
4. Gaussian spectral fluctuations.

These relations improve falsifiability of the spectral model but do not establish gravity-specific novelty.

## 9. Iteration-140 C5 infrared degeneracy

Below threshold, with `x=q^2/M_*^2`,

`C(x)=int_1^infty ds rho_hat(s)/(s+x)`

has the convergent expansion

`C(x)=sum_{n>=0}(-x)^n A_(n+1)` for `|x|<1`.

Thus at any fixed finite derivative order the candidate continuum is representable by local EFT Wilson coefficients. Strictly below threshold it is not independently identifiable against C5 plus Wilson-coefficient freedom.

Retained result: `CG-NG-005`.

## 10. Iteration-141 exact C4/KK Gaussian degeneracy

The spectral representation itself gives an exact direct-integral realization:

`h = h_GR + sqrt(beta) direct_integral ds sqrt(rho_hat(s)) H_s`,

where `H_s` are independent positive-norm Gaussian massive spin-2 fields with `m_s^2=M_*^2 s`.

Therefore

`<hh> = D_GR + beta int ds rho_hat(s) D_s`,

which is exactly the frozen `KL-002` two-point function.

With the same linear conserved-stress coupling, the direct-integral mediator model has identical retarded and Hadamard kernels. Hence it has the same Gaussian CTP influence functional and all linear-Gaussian RQIR likelihoods are identical.

**QG-007 FAIL — `EXACT_GAUSSIAN_C4_KK_DEGENERACY`.**

Retained result `CG-NG-006`:

> A positive Källén–Lehmann spin-2 continuum with only linear conserved-stress coupling is exactly equivalent at Gaussian RQIR level to an ordinary positive-norm continuum/tower of quantum spin-2 mediators. Two-point response/noise optimization cannot establish gravity-specific novelty.

## 11. Why detector optimization cannot rescue v0.1

The comparator identity is at the complete Gaussian influence-functional level, not merely at one plotted spectrum. Better sensitivity, more bands, nuisance profiling or physical resources cannot distinguish two models that define the same likelihood family at the frozen level.

Accordingly QG-008/QG-009/QG-010 are not pursued for promotion.

## 12. Scientific value retained

`KL-002` remains useful as:

- a positive-spectral consistency control;
- a C4/KK continuum comparator;
- a demonstration of the vDVZ-linked tensor cross-channel structure;
- a proof that propagator-only novelty is insufficient for the next Candidate Gravity architecture.

## 13. Design requirement exported to the next ansatz

The next Candidate Gravity must add at least one derived structure unavailable to a Gaussian mediator continuum, such as:

- nonlinear stress-energy self-coupling fixed by diffeomorphism/Ward bootstrap;
- connected three- and higher-point gravitational correlators tied to the same dynamics;
- a nonlinear constraint/relational identity linking higher response to the two-point sector;
- another gravity-specific non-Gaussian relation that survives C4/C5/nonlocal comparator audits.

The next model should be designed only after testing the strongest existing nonlinear/nonlocal gravity comparators against this requirement.
