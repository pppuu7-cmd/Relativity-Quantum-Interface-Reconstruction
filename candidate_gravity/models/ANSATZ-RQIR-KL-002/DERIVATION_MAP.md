# DERIVATION MAP — ANSATZ-RQIR-KL-002 v0.1

## KL-D001 — positive normalized continuum shape

`rho_hat(s)=exp(1-s)Theta(s-1)`.

Then `rho_hat>=0` and

`int_1^infty rho_hat(s) ds=1`.

**State:** PASS.

---

## KL-D002 — nonnegative full spectral measure

`rho_g(mu^2)=delta(mu^2)+(beta/M_*^2)rho_hat(mu^2/M_*^2)Theta(mu^2-M_*^2)`.

For `beta>=0`, every spectral weight is nonnegative.

**State:** PASS_SCOPED at Gaussian two-point level.

---

## KL-D003 — retarded superposition

`D_R(p)=int_0^infty dmu^2 rho_g(mu^2)/(p^2-mu^2+i0p^0)`.

Each component is retarded. Linearity of the spectral integral preserves retarded support.

**State:** PASS_SCOPED.

---

## KL-D004 — no isolated added pole

The continuum component is

`beta int_1^infty ds rho_hat(s)/(p^2-M_*^2 s+i0p^0)`.

Since `rho_hat` is smooth and has no delta support for `s>1`, the additional spectral sector produces a cut beginning at `p^2=M_*^2`, not an isolated pole. The only frozen delta-function pole is the GR massless pole at `p^2=0`.

**State:** PASS_SCOPED.

---

## KL-D005 — absorptive sign

For positive frequency and `y=p^2/M_*^2>1`, use

`Im [1/(p^2-M_*^2s+i0)] = -pi delta(p^2-M_*^2s)`.

Hence

`Im D_R,cont = -(pi beta/M_*^2) rho_hat(y) <=0`.

Thus the continuum discontinuity corresponds to nonnegative spectral weight.

**State:** PASS_SCOPED in the frozen scalar transfer convention.

---

## KL-D006 — Euclidean positivity

For `q^2>0`,

`D_E(q^2)=1/q^2+beta int_1^infty ds rho_hat(s)/(q^2+M_*^2s)`.

Every term is positive for `beta>=0`.

**State:** PASS_SCOPED.

---

## KL-D007 — static potential correction

The 3D Fourier transform of each Euclidean massive denominator yields a Yukawa kernel. Therefore

`Phi(r)=-GM/r [1+beta W(u)]`, `u=M_*r`,

`W(u)=int_1^infty ds rho_hat(s) exp(-u sqrt(s))`.

Since `sqrt(s)>=1`,

`0<W(u)<=exp(-u) int rho_hat ds=exp(-u)`.

Also `W(0)=1`.

Therefore

`|delta Phi/Phi_GR|<=beta exp(-M_*r)`.

**State:** PASS_SCOPED for the scalarized conserved-source transfer. Full tensor/PPN normalization remains open.

---

## KL-D008 — linked RQIR signature

The same `(beta,M_*)` and `rho_hat` determine:

- the static Yukawa-mixture correction;
- the dynamic branch-cut threshold and absorptive response;
- the Gaussian vacuum spectral fluctuations.

No independent amplitudes are introduced for those three sectors.

**State:** DEFINED.

---

## KL-D009 — beta=0 boundary

At `beta=0`,

`rho_g -> delta(mu^2)`

and the gravity transfer reduces to the massless reference propagator in the declared linearized sector.

**State:** PASS_SCOPED.

---

## Open derivations

### KL-D010 — full tensor/helicity completion

Need a covariant/conserved-source realization of the positive continuum and proof that no negative norm or constraint inconsistency appears when the complete spin structure is restored.

**State:** BLOCKED / highest priority.

### KL-D011 — C5 interaction-continuum subtraction

Compute the corresponding standard perturbative-QG spectral continuum at the same order and define the genuinely new candidate direction only after subtracting/profiling C5.

**State:** NOT_STARTED.

### KL-D012 — finite Paper-I quotient

Build the finite source/detector map containing both static and dynamic channels and prove that the candidate direction survives exact calibration constraints.

**State:** NOT_STARTED.

## Dependency order

`KL-D001 -> KL-D002 -> KL-D003/D004/D005/D006`

`KL-D002 + KL-D007 -> QG-003/QG-004 scoped results`

`KL-D010 -> QG-005 -> QG-007`

`KL-D011 -> QG-007 -> KL-D012/QG-008 -> QG-009 -> QG-010`
