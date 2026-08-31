# Candidate Gravity — Iteration 175: tensor/soft Ward decomposition

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Status:** scalar `WardLock` replaced by a physically resolved soft/tensor decomposition; no Candidate Gravity residual yet

## 1. Why Iteration 172's scalar Ward coordinate is insufficient

Iteration 174 established that a fixed closed-unitary, diffeomorphism-invariant nonlocal tree action is annihilated exactly by the coarse relation map

`R_aar=Gamma_aar`,

`R_unit=Gamma_aaa-Gamma_arr/4`,

`R_W=WardLock`.

That map distinguishes violations of consistency but cannot distinguish different consistent closed quantum gravity families. A vanishing scalar Ward residual is therefore a **necessary consistency lock**, not a novelty coordinate.

The next protocol must retain the tensor content of the soft Ward identity.

## 2. 1PI soft decomposition

For a source-completed amputated cubic graviton vertex with one soft momentum `k`, general covariance fixes a part of the vertex in terms of the same quadratic 1PI inverse kernel `K^(2)`. Schematically write

\[
\boxed{
\Gamma^{(3)}_{\rm soft}
=
\mathcal W[K^{(2)}]
+
R^{(1)}_{\mu\rho\nu\sigma}(k,\epsilon)\,
B^{\mu\rho\nu\sigma}
+
O(k^3)
}
\]

where

- `W[K^(2)]` is the Ward/covariantization-determined soft part fixed by the two-point kernel and source convention;
- `R^(1)` is the linearized Riemann tensor of the soft graviton;
- `B` is an independent gauge-invariant three-point/nonminimal form-factor structure not fixed by the two-point kernel alone.

This is the appropriate structural form for the next RQIR quotient. The Ward-determined piece is shared consistency structure; the `R^(1):B` sector is the first candidate model-dependent transverse/off-shell space.

The relevant literature basis is the 1PI soft-graviton analysis of Sen and of Laddha–Sen. In generic quantum gravity the universal leading/subleading structure is fixed by covariance, while non-universal three-point information can first enter the sub-subleading soft term. Local EFT analyses likewise show that local operators do not modify the subleading graviton soft theorem in the frozen setting, whereas sub-subleading terms can receive operator-dependent corrections.

## 3. Linearized Riemann tensor

Use the Fourier-space convention

\[
R^{(1)}_{\mu\nu\rho\sigma}
=-\frac12\left(
 k_\rho k_\nu\epsilon_{\mu\sigma}
+k_\sigma k_\mu\epsilon_{\nu\rho}
-k_\sigma k_\nu\epsilon_{\mu\rho}
-k_\rho k_\mu\epsilon_{\nu\sigma}
\right).
\]

For a pure-gauge soft polarization

\[
\epsilon^{\rm gauge}_{\mu\nu}
=k_\mu\xi_\nu+k_\nu\xi_\mu,
\]

the exact continuum identity is

\[
R^{(1)}[\epsilon^{\rm gauge}]=0.
\]

For a physical TT polarization, `R^(1)` is generally nonzero.

## 4. Reproducible tensor certificate

Freeze a null soft momentum along `+z`,

`k=(1,0,0,1)`,

and a deterministic gauge vector

`xi=(0.3,0.7,-0.2,0.4)`.

For the pure-gauge polarization `eps=k⊗xi+xi⊗k`, the validator obtains

- `max |R^(1)| = 5.55e-17`;
- `||R^(1)|| = 1.36e-16`.

For the normalized plus-type TT polarization

`eps_xx=1/sqrt(2)`, `eps_yy=-1/sqrt(2)`,

the same tensor gives

- `max |R^(1)| = 0.35355339059327373`;
- `||R^(1)|| = 2` to floating-point precision.

Thus the proposed transverse/nonminimal tensor structure is gauge invariant in the required linearized sense and is not identically zero on a physical TT soft graviton.

## 5. Soft-order certificate

Scale the soft momentum as `k -> a k` while keeping the polarization fixed. Since the linearized Riemann contains two powers of `k`,

\[
R^{(1)}(a k)=a^2R^{(1)}(k).
\]

The validator finds

- `a=0.5`: norm ratio `0.25`;
- `a=2`: norm ratio `4`;
- `a=3`: norm ratio `9.000000000000002`.

Maximum scaling error is

`1.78e-15`.

Therefore the independent `R^(1):B` structure begins at the **sub-subleading `O(k^2)` soft order**, exactly where the earlier RQIR soft analysis already required C5 EFT operator freedom to be included rather than treated as novelty.

Retain:

`SOFT-NG-002 — LINEARIZED_RIEMANN_THREE_POINT_FORM_FACTOR_IS_GAUGE_INVARIANT_AND_ENTERS_AT_SUBSUBLEADING_K2_ORDER`.

## 6. New finite relation coordinates

The old scalar coordinate `WardLock` is demoted to a consistency check only.

For each of the six frozen amputated kinematic rows, define conceptually

\[
\boxed{
B_T^{(i)}
=
P_T\left[
\Gamma^{(3)}_{arr,i}
-
\mathcal W_i[K^{(2)}]
\right]
}
\]

where `P_T` projects onto the independent transverse/linearized-Riemann tensor structure after the Ward-determined longitudinal part has been removed.

Before comparator subtraction this yields a six-row transverse relation space.

Important: `B_T` is **not** automatically a Candidate Gravity residual. Standard local C5 EFT, nonlinear C4, fixed nonlocal gravity and asymptotic-safety vertex truncations can all populate sub-subleading transverse three-point structure.

## 7. Comparator interpretation

### C3 postquantum-classical

The ordered nonlinear metric-CTP completion remains `BLOCKED_C3_CTP_ORDERED_COMPLETION`. No `B_T` column may be invented or zero-filled.

### C4

A generic closed quantum mediator may have its own nonminimal/transverse cubic form factors. The fixed C4 parent realization must be projected into `B_T`; generic `r/a` unitarity alone no longer decides the comparison.

### C5

Local diffeomorphism-invariant EFT operators can modify sub-subleading soft graviton structure. Therefore the first required concrete transverse comparator is the finite C5 EFT operator basis at the already frozen perturbative/derivative order.

### Fixed nonlocal comparator

For `QG-NL-EXP-001`, the full covariant parent action fixes the tree cubic structure in principle, including the operator Fréchet insertion established in Iteration 174. Its projection into the new transverse `B_T` coordinates remains to be computed.

### Asymptotic safety

The two-point spectral function remains calibration/shared data. A real-time/source-completed three-point vertex or controlled map from the fixed vertex truncation into `B_T` is still BLOCKED.

## 8. Retained results

### `SOFT-NG-001 — WARD_DETERMINED_SOFT_CUBIC_PART_IS_SHARED_STRUCTURE_FIXED_BY_THE_TWO_POINT_KERNEL`

The soft cubic component required by the 1PI diffeomorphism Ward identity is not a new model direction once the same quadratic kernel and source convention are conditioned on.

### `SOFT-NG-002 — LINEARIZED_RIEMANN_THREE_POINT_FORM_FACTOR_IS_GAUGE_INVARIANT_AND_ENTERS_AT_SUBSUBLEADING_K2_ORDER`

The first independent gauge-invariant soft three-point structure is naturally represented by a linearized-Riemann tensor times a three-point form factor and appears at `O(k^2)`.

### `NG-FUNNEL-035 — REPLACE_SCALAR_WARDLOCK_WITH_WARD_SUBTRACTED_TRANSVERSE_CUBIC_COORDINATES`

A scalar Ward pass/fail coordinate cannot distinguish consistent quantum-gravity families. The RQIR novelty quotient must first subtract the tensor Ward-determined component and then compare the remaining transverse cubic form factors.

## 9. Readiness

`MODEL_READINESS: 24%` — unchanged.

A sharper and physically correct residual space is now frozen, but its fixed C5/C4/nonlocal/AS comparator columns are not yet all instantiated. No robust unique residual exists.

No `ANSATZ-003`. No Fisher. No resource optimization.

## 10. Next gate

Iteration 176 should instantiate the **first finite C5 transverse soft comparator basis** in the six `B_T` rows:

1. freeze the local diffeomorphism-invariant EFT operator subset capable of changing sub-subleading soft structure at the declared order;
2. project its source-completed cubic vertices into the Ward-subtracted transverse coordinates;
3. compute rank/SVD without target optimization;
4. only then add fixed C4 and nonlocal transverse columns;
5. preserve C3 ordered and AS real-time columns as BLOCKED until derived.
