# ANSATZ-RQIR-KL-002 — positive-spectral continuum gravity

**Version:** 0.1  
**Status:** DRAFT / TESTING  
**Iteration introduced:** 138  
**Purpose:** second RQIR-driven Candidate Gravity ansatz, constructed after the analytic rejection of `ANSATZ-RQIR-CTP-001` v0.1. The structural design rule is to make two-point positivity and absence of isolated negative-residue poles manifest at the frozen Gaussian level rather than infer them from Euclidean behavior.

## 1. Core idea

Instead of modifying the inverse graviton kernel by a factor that can cross zero under Lorentzian continuation, define the physical spin-2 two-point function directly by a nonnegative Källén–Lehmann-type spectral measure.

The resolved weak-field gravitational transfer contains:

1. the ordinary massless GR pole with unchanged residue;
2. a positive continuous spin-2 spectral sector starting at scale `M_*`;
3. no additional isolated pole in v0.1.

The continuum weight is controlled by one dimensionless amplitude `beta>=0`. The same spectral measure fixes the retarded transfer, absorptive threshold and vacuum Gaussian fluctuation kernel; these are not independently fitted RQIR functions.

This is an effective weak-field model, not a UV completion and not yet a novelty claim.

## 2. Frozen spectral measure

Use spectral mass variable `mu^2` and define

`rho_g(mu^2) = delta(mu^2) + (beta/M_*^2) rho_hat(mu^2/M_*^2) Theta(mu^2-M_*^2)`,

with

`rho_hat(s)=exp(1-s) Theta(s-1)`,

`int_1^infty rho_hat(s) ds = 1`,

`beta>=0`, `M_*>0`.

Thus the massless pole has fixed unit spectral weight in the frozen GR normalization and the continuum carries integrated dimensionless weight `beta`.

## 3. Retarded spin-2 transfer

On the conserved-source spin-2 sector, suppressing the frozen tensor projector and overall GR sign convention,

`D_R(p) = 1/(p^2+i0 p^0) + beta int_1^infty ds rho_hat(s)/(p^2-M_*^2 s+i0 p^0)`.

Equivalently,

`D_R(p)=int_0^infty dmu^2 rho_g(mu^2)/(p^2-mu^2+i0 p^0)`.

The Euclidean transfer is

`D_E(q^2)=1/q^2 + beta int_1^infty ds rho_hat(s)/(q^2+M_*^2 s)`.

For `q^2>0` every term is nonnegative.

## 4. Gaussian state / physical-state interpretation

At v0.1 the spin-2 sector is a generalized free quantum field specified by a positive spectral measure. Equivalently, its one-particle space can be viewed as a direct integral of positive-norm spectral sectors weighted by `rho_g`, with the massless GR component separated explicitly.

This supplies a scoped Gaussian positivity/unitarity certificate for the two-point sector. It does **not** prove a nonlinear diffeomorphism-complete interacting gravity theory.

The exact completion of the continuum tensor/helicity content is deliberately left as a QG-005 gate. No claim is made that an arbitrary collection of Pauli–Fierz massive fields already supplies the correct nonlinear completion.

## 5. Matter coupling

Matter is initially the same scalar QFT used by the reference branch. At linear order the resolved gravitational field couples universally to the conserved stress tensor,

`S_int = -(kappa/2) int d^4x h_mn T^mn`,

where `h_mn` denotes the RQIR-facing conserved-source spin-2 transfer combination.

The source hierarchy remains

`J=<T>`,

`N=1/2 <{delta T,delta T}>`,

`chi_T^R=-i theta <[T,T]>`,

with renormalization/smearing conventions inherited from the RQIR contract.

The model-specific gravity sector propagates these source objects through the positive spectral transfer `D_R`; its own vacuum Gaussian fluctuations are fixed by the same `rho_g`.

## 6. Causality and spectral positivity

Each spectral component has the standard retarded prescription. A nonnegative superposition of retarded massive propagators remains retarded.

For positive frequency and `p^2>M_*^2`,

`Im D_R,cont(p) = -pi beta rho_hat(p^2/M_*^2)/M_*^2 <= 0`

in the frozen scalar retarded convention.

Hence the continuum spectral discontinuity has nonnegative Källén–Lehmann weight.

There is no isolated continuum pole because `rho_hat` is smooth on `s>=1`; instead there is a branch cut beginning at `p^2=M_*^2`.

This avoids the Iteration-136 theorem that rejected the previous ansatz.

## 7. Infrared / Newtonian structure

The massless pole and its residue are unchanged, so the asymptotic long-range Newtonian `1/r` term is preserved at the frozen linearized level.

For a static point-source transfer, each continuum mass produces a Yukawa factor. The potential therefore has the schematic form

`Phi(r) = -G M/r [1 + beta W(M_* r)]`,

where

`W(u)=int_1^infty ds rho_hat(s) exp(-u sqrt(s))`.

Because `sqrt(s)>=1` and the spectral shape is normalized,

`0 < W(u) <= exp(-u)` for `u>0`,

and `W(0)=1`.

Thus the correction is finite-range and the asymptotic Newtonian limit is exponentially recovered:

`|delta Phi/Phi_GR| <= beta exp(-M_* r)`.

The complete tensor normalization/PPN audit remains open before QG-003 can fully PASS.

## 8. RQIR-linked fingerprint

The same pair `(beta,M_*)` controls three sectors:

1. **static transfer:** the Yukawa-mixture correction `W(M_* r)`;
2. **dynamic ordered response:** the retarded continuum threshold at `p^2=M_*^2`;
3. **vacuum Gaussian gravitational fluctuations:** the positive spectral continuum fixed by `rho_g`.

Therefore source calibration is not allowed to tune the static, absorptive and noise signatures independently.

The intended RQIR discriminator is the cross-consistency of these three manifestations after the exact hard-constraint quotient.

## 9. Relation to known theory classes

This ansatz is **not claimed novel**. Positive spectral continua occur in generalized free fields, interacting Källén–Lehmann representations, hidden-sector/continuum mediator models, extra-dimensional/Kaluza–Klein constructions, unparticle-like models, and some nonlocal quantum-gravity descriptions.

Accordingly QG-007 is BLOCKED until the model is compared explicitly against:

- C5 perturbative quantum GR including its interaction-generated continuum;
- nonlocal/form-factor gravity;
- hidden/non-gravitational quantum mediator nuisance C4;
- extra-dimensional/continuum spin-2 models where operationally relevant;
- stochastic/classical-channel alternatives that may reproduce lower-order transfer/noise.

A failure of novelty will be retained as a useful negative result rather than repaired by changing `rho_hat` post hoc.

## 10. Immediate falsification conditions

Reject/supersede v0.1 if:

- the positive spectral measure cannot be embedded in a consistent conserved-source spin-2 physical-state space;
- restoring the full tensor/helicity structure introduces negative-norm states or violates Ward/Bianchi consistency;
- the Newtonian/PPN limit fails after full tensor normalization;
- the linked static/dynamic/noise fingerprint is exactly degenerate with C5 or another required comparator;
- the candidate direction disappears under exact RQIR calibration/nuisance profiling;
- required physical resources are divergent/undefined in every admissible region.

## 11. Current scientific status

The model is stronger than v0.1 only in a **scoped two-point sense**: positivity, retarded support and absence of an isolated opposite-residue pole are built into the spectral representation.

It is not yet `QG001` and should remain `ANSATZ-*` until the tensor/gauge, comparator and RQIR finite-discriminator gates are completed.
