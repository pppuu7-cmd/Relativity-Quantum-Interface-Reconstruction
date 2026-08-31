# C3-PQCG-LIN-001 — fixed linear stochastic comparator

**Iteration frozen:** 153  
**Comparator class:** C3 — classical-channel / postquantum classical-quantum gravity  
**Status:** finite scoped comparator block; NOT a candidate ansatz and NOT a full nonlinear C3 closure.

## Literature anchor
This comparator freezes only the linearized stochastic pure-gravity sector motivated by the covariant classical-quantum path-integral program of Oppenheim & Weller-Davies and the explicit stochastic metric-mode analysis of Oppenheim & Sajjad. The 2026 PRX construction establishes a manifestly covariant completely-positive classical-quantum path-integral framework with classical spacetime; the 2026 stochastic-modes analysis identifies diffusing spin-2 and spin-0 metric modes around Minkowski spacetime.

Authorities:
- Oppenheim & Weller-Davies, Phys. Rev. X 16, 031007 (2026), DOI 10.1103/2rcd-dzcf.
- Oppenheim & Sajjad, arXiv:2605.05375 (2026), `Stochastic modes in postquantum classical gravity`.
- Grudka et al., arXiv:2402.17844, for the renormalised postquantum-classical gravity stochastic action context.

## Frozen dynamics and convention
Metric perturbations are decomposed into covariant transverse spin sectors `s=2,0` around Minkowski. In this scoped linear stochastic block,

`box h_s = J_s + xi_s`,

with Gaussian stochastic forcing

`<xi_s(x) xi_s'(y)> = 2 D_s delta_ss' delta^4(x-y)`.

Parameter vector:

`theta_C3 = (D2, D0)`, with `D2>0`, `D0>0` and tangent taken at an interior positive point.

On the frozen spacelike probes, `G_R(k)=1/k^2`; therefore

`N_s(k)=2 D_s |G_R(k)|^2`.

The finite operational smearing reuses the Iteration-149 Gaussian window `(tau,L)=(0.8,0.6)` and all 18 momenta `{q_i,r_i,q_i+r_i}`. The `N2` coordinate is the traced transverse symmetric-tensor noise. In four dimensions the Barnes-Rivers spin-projector ranks are `Tr(P2)=5`, `Tr(P0)=1`, hence

`N2 = A (5 D2 + D0)`,

where the frozen finite probe sum gives

`A = 258.83104475297773`.

The linear retarded response `chi1R=G_R` is supported and nonzero but does not depend on `(D2,D0)` in this parameter convention.

## What is NOT claimed
The linear stochastic block does not contain a derived nonlinear matter-backreaction vertex or a derived non-Gaussian noise functional. Consequently `C3sym`, `chi2R_even`, `chi2R_odd`, `soft2`, `tensor_geo`, and `threshold` are **BLOCKED**, not zero.

This distinction is mandatory: filling these rows with zeros would artificially shrink the C3 quotient.
