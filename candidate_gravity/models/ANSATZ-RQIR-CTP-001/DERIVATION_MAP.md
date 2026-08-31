# DERIVATION MAP — ANSATZ-RQIR-CTP-001 v0.1

This file separates derived statements from declared assumptions and future gates.

## D-001 — one-kernel CTP construction

**Input:** weak-field CTP effective action with a transverse spin-2 self-energy and one positive spectral density `rho_hat`.

**Definition:**

`F_R(p) = zeta int_1^infty ds rho_hat(s)/(s+zeta)`,

`zeta = -(p^2+i0 p^0)/M_*^2`,

`K_R^(2) = K_GR,R^(2) [1+beta F_R]`.

**Output:** retarded response is fixed once `(beta,M_*,rho_hat)` are fixed.

**State:** DEFINED.

---

## D-002 — linked absorptive/noise sector

**Input:** the same causal kernel and the v0.1 vacuum/KMS-zero-temperature state choice.

**Relation:**

`Pi_H^(2) = -2 sgn(p^0) Im Pi_R^(2)`

up to the repository's final Hadamard/noise normalization convention.

**Output:** noise is not an independent fit direction.

**State:** STRUCTURAL / NORMALIZATION AUDIT OPEN.

---

## D-003 — positive normalized spectral shape

**Input:**

`rho_hat(s)=exp(1-s)Theta(s-1)`.

**Derivation:**

`rho_hat>=0`,

`int_1^infty exp(1-s) ds = 1`.

**State:** PASS.

---

## D-004 — spacelike form factor

For `x=-p^2/M_*^2>=0`,

`F_E(x)=x int_1^infty ds exp(1-s)/(s+x)`.

Substitute `u=s+x`:

`F_E(x)=x exp(1+x) E1(1+x)`.

**State:** PASS.

---

## D-005 — Euclidean bound and no-zero result

For `s>=1` and `x>=0`,

`0 <= x/(s+x) <= x/(1+x)`.

Averaging with the positive normalized `rho_hat` gives

`0 <= F_E(x) <= x/(1+x) < 1`.

For `beta>=0`,

`1+beta F_E(x) >= 1`.

Therefore the v0.1 multiplicative spin-2 kernel has no extra Euclidean zero on the spacelike axis.

**State:** PASS_SCOPED.

**Does not imply:** Lorentzian ghost freedom, microcausality, nonlinear stability, or UV completion.

---

## D-006 — infrared coefficient

Expand at `x=0`:

`F_E(x)=A1 x + O(x^2)`,

`A1=int_1^infty ds exp(1-s)/s = e E1(1)`.

Numerically

`A1 ~= 0.5963473623231726`.

Thus the deformation vanishes continuously at the GR pole and begins at derivative order `p^2/M_*^2` in the multiplicative inverse-kernel factor.

**State:** PASS_SCOPED.

---

## D-007 — threshold

Analytic continuation of the denominator `s+zeta` gives the first branch support when timelike `p^2>=M_*^2`, inherited from the lower support edge `s=1`.

**State:** STRUCTURAL.

**Open:** exact discontinuity, sign convention, spectral positivity of the full dressed propagator, possible zeros of `1+beta F_R` on non-Euclidean sheets.

---

## D-008 — linear Ward target

The model-specific tensor insertion is proportional to the transverse spin-2 projector `P2`. On conserved sources,

`p_m Pi_R^{mn,ab}=0`.

**State:** PASS at the declared projected linearized level.

**Open:** restoration of the complete tensor/constraint structure and nonlinear diffeomorphism consistency.

---

## D-009 — RQIR beta direction

Boundary:

`beta=0` -> perturbative-QG C5 reference.

Candidate direction:

`partial_beta D_R^(2)|_0 = - D_GR,R^(2) F_R` in the multiplicative convention.

The same beta fixes the linked absorptive/noise change.

**State:** DEFINED.

**Next required proof:** survive the exact finite calibration quotient and comparator nuisance space; raw nonzero response is not sufficient.

## Dependency order

`D-003 -> D-004 -> D-005/D-006 -> QG-003/QG-004 audits`

`D-001 -> D-002 -> D-009 -> QG-008 -> QG-009 -> QG-010`

`D-008 -> QG-005`

No later gate may be promoted by bypassing an unresolved earlier dependency.
