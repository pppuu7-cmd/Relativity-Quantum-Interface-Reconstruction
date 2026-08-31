# COMPARATOR STATUS — ANSATZ-RQIR-KL-002 v0.1

No novelty claim is active. The positive spectral continuum is treated as a hypothesis to be attacked by the strongest known comparator classes.

| Comparator | State | Earliest candidate difference | Main degeneracy risk |
|---|---|---|---|
| C0 classical GR/Newtonian | BLOCKED | finite-range tensor-linked static correction plus dynamic threshold | classical fifth-force/Yukawa phenomenology may mimic the static sector |
| C1 semiclassical mean gravity | POTENTIALLY_DISTINCT | vacuum gravitational spectral continuum is not mean-only | source/QFT effects could imitate part of the response |
| C2 stochastic gravity | BLOCKED | positive quantum spectral continuum with linked ordered response and vacuum fluctuations | classical stochastic kernels may reproduce two-point noise/response unless a nonclassical ordering/channel witness is included |
| C3 classical-channel/postquantum classical gravity | BLOCKED | quantum spectral/Hilbert-space interpretation and possible nonclassical channel behavior | modern stochastic classical spacetime models can produce threshold/noise spectra |
| C4 ordinary quantum matter + non-gravitational mediator | BLOCKED_HIGH_PRIORITY | universal stress-tensor spin-2 geometry plus linked NR/traceless/dynamic scaling | hidden continuum mediators, KK modes and unparticle-like sectors can reproduce a positive spin-2 spectral continuum |
| C5 perturbative quantum GR EFT | DEGENERATE_IR / BLOCKED_THRESHOLD | resolved excess threshold/support/shape after the standard C5 loop baseline is frozen | below `|q^2|<M_*^2`, the candidate continuum is analytic and is absorbed order-by-order into local EFT Wilson coefficients at any fixed finite derivative order |
| C6 QFT source + classical interface | BLOCKED | same cross-consistency across transfer/noise/static channels | quantum source statistics plus classical transfer may mimic lower-order observables |

## C5 low-energy degeneracy theorem — Iteration 140

For Euclidean `x=q^2/M_*^2` below the continuum threshold,

`C(x)=int_1^infty ds rho_hat(s)/(s+x)`.

Because `s>=1`, for `|x|<1`

`1/(s+x)=sum_{n>=0} (-x)^n/s^(n+1)`,

so

`C(x)=sum_{n>=0} (-x)^n A_(n+1)`,

`A_k=int_1^infty ds rho_hat(s)/s^k`.

The first moments for the frozen shape are

`A1=0.5963473623`,

`A2=0.4036526377`,

`A3=0.2981736812`,

`A4=0.2339421063`,

`A5=0.1915144734`.

Every finite truncation is therefore a polynomial in `q^2/M_*^2` and is operationally equivalent to a finite set of local higher-derivative EFT coefficients unless additional cross-channel information removes that freedom.

**Retained result CG-NG-005:** a gapped positive spectral continuum is not distinguishable from C5 plus local Wilson-coefficient freedom in a strictly below-threshold finite-order EFT measurement.

This is a regime-specific degeneracy, not a statement that the full threshold theory equals C5.

## Required route out of C5 degeneracy

At least one of the following is required before QG-007 can progress:

1. resolve frequencies/momenta approaching or crossing `p^2=M_*^2`, where the branch cut/nonanalyticity cannot be represented by a finite local derivative expansion;
2. use the linked NR-force / traceless-probe / absorptive-threshold / noise relations with common `(beta,M_*)` and show that no allowed C5 Wilson/nuisance family reproduces them jointly;
3. subtract a frozen explicit C5 loop spectral baseline and identify a residual positive spectral direction.

## Other required comparator work

- Compare with hidden-sector/continuum mediator and extra-dimensional/Kaluza–Klein spin-2 representations.
- Compare with nonlocal/form-factor gravity whose spectral representation may have positive weight and the same local limit.
- Check whether C2/C3 classical stochastic kernels can reproduce both retarded threshold and noise covariance after all hard calibration constraints.
- Require at least one observable combination involving tensor/geometric coupling or quantum ordering/channel structure that generic C4/C6 mediators cannot absorb.

## Current decision

`ANSATZ-RQIR-KL-002` survives the first consistency/tensor screens, but **deep-IR detector optimization is now forbidden as scientifically non-identifying**. The useful search region is the resolved-threshold/cross-channel regime.

If the full threshold fingerprint is still reproduced by C4/C5/nonlocal/KK comparators, retain `KL-002` as a control and require the next ansatz to add a structural relation unavailable to those classes.
