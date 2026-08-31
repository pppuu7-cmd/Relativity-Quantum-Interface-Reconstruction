# Post-Gaussian RQIR Protocol — Iteration 145

**Date:** 2026-08-31  
**Status:** frozen design infrastructure; no `ANSATZ-003` promoted

## Purpose

Iteration 144 defined the abstract finite quotient. Iteration 145 freezes the first concrete observable-coordinate protocol and determines which soft/ordered coordinates may legitimately carry novelty before a new model is written down.

The main result is a two-part design constraint:

1. universal leading/subleading soft-graviton structure is a **lock/consistency condition**, not a candidate novelty coordinate;
2. broad theory-class capability envelopes are too large to serve as comparator tangent matrices — fixed finite realizations/truncations are mandatory.

## 1. Finite observable vector

For the first post-Gaussian pre-screen use the ordered coordinate vector

`y = (`

`  y_norm,`  
`  y_N2,`  
`  y_chi1R,`  
`  y_C3sym,`  
`  y_chi2R_even,`  
`  y_chi2R_odd,`  
`  y_soft0,`  
`  y_soft1,`  
`  y_soft2,`  
`  y_tensor_geo,`  
`  y_threshold`  
`)`.

Interpretation:

- `y_norm`: massless/long-range normalization calibration;
- `y_N2`: a frozen smeared two-point symmetric-noise coordinate;
- `y_chi1R`: a frozen linear retarded-response coordinate;
- `y_C3sym`: a frozen connected fully symmetrized third-cumulant coordinate;
- `y_chi2R_even`: exchange-even second-order causal response combination;
- `y_chi2R_odd`: exchange/order-sensitive second-order causal response combination;
- `y_soft0`: leading soft-graviton consistency residual;
- `y_soft1`: subleading soft-graviton consistency residual;
- `y_soft2`: first subsubleading soft-sensitive coordinate;
- `y_tensor_geo`: finite tensor/geometric coupling ratio not reducible to overall gain;
- `y_threshold`: finite-momentum/nonanalytic threshold-shape coordinate.

These are protocol slots. A future candidate must replace every slot it uses by a concrete smeared/renormalized observable with units, source geometry and detector map.

## 2. Hard locks

At the first design stage impose

`y_norm = 0` in tangent coordinates after calibration,

`y_soft0 = 0`,

`y_soft1 = 0`.

The reason for treating `soft0` and `soft1` as locks is not that all quantum-gravity theories are identical. It is that for an asymptotically flat massless graviton theory that retains the standard diffeomorphism/equivalence-principle boundary, the leading Weinberg soft factor is universal and the tree-level subleading graviton soft theorem is protected against local EFT deformations at the relevant order.

The project therefore forbids a future `ANSATZ-003` from claiming novelty merely by changing `soft0` or `soft1` while simultaneously claiming the same GR/diffeomorphism boundary.

Literature anchors:

- Cachazo & Strominger, arXiv:1404.4091 — universal leading soft pole and tree-level subleading relation;
- Elvang, Jones & Naculich, arXiv:1611.07534 — local EFT operators do not modify the subleading soft graviton theorem, while new graviton soft terms can enter at subsubleading order.

## 3. Subsubleading soft coordinate is not sufficient novelty

`y_soft2` is retained as a measured coordinate, not a hard lock.

However it is **not** a novelty certificate by itself: local diffeomorphism-invariant EFT operators can generate new subsubleading soft-graviton terms. Therefore C5 must carry an explicit `soft2` tangent at the declared EFT order.

Retained result:

**NG-FUNNEL-004 — SOFT_LOCK_NOT_NOVELTY:**

- `soft0/soft1` are consistency/lock coordinates for the standard GR boundary;
- `soft2` may carry dynamics, but is already an allowed C5-EFT comparison direction;
- a soft theorem by itself does not provide an RQIR residual outside C5.

## 4. Ordered nonlinear coordinates

The pair

`(y_chi2R_even, y_chi2R_odd)`

is retained because it distinguishes genuinely causal/order-sensitive nonlinear response from a fully symmetrized third cumulant.

But Iteration 145 does **not** assume that `y_chi2R_odd != 0` is gravity-specific. Quantum matter coupled to a classical stochastic spacetime, nonlinear mediator models and ordinary quantum gravity may all produce operationally order-sensitive nonlinear response after the full source/detector map is included.

Thus the ordered sector is a **search target**, not a theorem of quantum geometry.

## 5. Reduced coordinates after hard constraints

After removing `(y_norm,y_soft0,y_soft1)`, use

`z = (`

`  N2, chi1R, C3sym, chi2R_even, chi2R_odd, soft2, tensor_geo, threshold`  
`)`.

Dimension: `8`.

## 6. Class-envelope saturation diagnostic

Before freezing concrete comparators, represent each broad theory class only by a conservative **capability envelope**: if a class can in principle alter a coordinate, that axis is allowed independently.

This is deliberately more permissive than a physical model.

At class-label level:

- C3 stochastic/postquantum-classical models can in principle occupy symmetric noise/higher cumulants and nonlinear causal-response sectors with nontrivial spectral shape;
- C4 nonlinear quantum-mediator/massive-spin-2 families can occupy Gaussian and post-Gaussian response/cumulant/tensor/threshold sectors;
- C5 perturbative quantum-gravity EFT can occupy the full declared reduced sector once local higher-dimension operators, loops, nonlinear graviton interactions and subsubleading soft corrections are treated as independent class capabilities.

The resulting capability-envelope span is full rank in the eight-dimensional reduced protocol.

This is reproduced by

`analysis/post_gaussian_class_envelope_iteration145.py`.

## 7. Interpretation of full-rank class envelope

The full-rank result is **not** a no-go theorem for new gravity.

It means that a label such as `C5 = all perturbative quantum-gravity EFT freedom` cannot be used as an unconstrained nuisance matrix. Doing so erases the correlations and Ward identities that make a concrete theory predictive.

Therefore the next comparator blocks must be finite parameterized realizations:

`V_Ci = partial y / partial theta_Ci`

for a frozen action/truncation/state/renormalization convention.

Retained result:

**NG-FUNNEL-005 — CLASS_ENVELOPE_SATURATION:**

A post-Gaussian novelty quotient built from broad per-coordinate theory-class capability masks is vacuous. RQIR must compare the candidate against fixed model/truncation tangent matrices, preserving each comparator's internal relations.

## 8. Frozen representative comparator program for Iteration 146+

### C3-PQCG representative

Freeze a concrete postquantum-classical gravity realization from the covariant classical–quantum path-integral program, including its stochastic action and finite parameter set. Two-point results alone are insufficient; any post-Gaussian tangent used in the quotient must actually be derived from the fixed realization.

Current literature anchors:

- Grudka et al., arXiv:2402.17844, renormalisation/stochastic classical-quantum gravity;
- Oppenheim & Sajjad, arXiv:2605.05375, explicit stochastic metric modes/two-point spectra.

Until a nonlinear response/cumulant is explicitly derived in the selected realization, the corresponding comparator column is `BLOCKED`, not set to zero.

### C4 representative

Retain `ANSATZ-RQIR-KL-002` only as the exact Gaussian continuum control. Add a finite nonlinear massive-spin-2/dRGT-style realization only when its action and finite parameter vector are frozen.

### C5 representative

Use the `ANSATZ-PQG-EFT-001` boundary augmented to the declared post-Gaussian order:

- Einstein-Hilbert tree nonlinearities;
- the required perturbative loop/nonanalytic baseline at the same order;
- a finite local diffeomorphism-invariant EFT operator basis through the first order capable of modifying the selected `soft2`/finite-momentum observables.

The operator basis and renormalization convention must be explicit before numerical tangent columns are accepted.

### Nonlocal comparator

Use one fixed covariant weakly/nonlocal action rather than the label `nonlocal gravity`. The action must be expanded to the same two-/three-point observable protocol.

### Asymptotic-safety comparator

Use a fixed vertex truncation, not the program label. A suitable authority class is a calculation with momentum-dependent three-/four-graviton vertices and reconstructed effective action, e.g. Pawlowski & Tränkle, arXiv:2309.17043.

## 9. Design rule for `ANSATZ-003`

Do not freeze `ANSATZ-003` from a soft-theorem modification alone.

The minimum viable target is now:

1. exact C5 boundary at `beta=0`;
2. unchanged hard `soft0/soft1` locks;
3. a finite-momentum ordered nonlinear response component;
4. a derived symmetric/post-Gaussian partner from the same CTP dynamics;
5. a Ward/soft relation tying those components to the same universal stress-energy coupling;
6. a nonzero quotient residual only after **fixed** C3/C4/C5/nonlocal/asymptotic-safety tangent matrices are inserted.

## 10. Immediate next action

Iteration 146 should instantiate the first **finite representative comparator tangent**, starting with the C5 post-Gaussian baseline because it defines the exact `beta=0` boundary of any serious `ANSATZ-003`.

No Fisher/resource work is allowed before at least C3/C4/C5 fixed comparator tangents exist in the same protocol.
