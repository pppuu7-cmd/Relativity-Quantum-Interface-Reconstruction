# RQIR Iteration 039 — D2 Covariance Endpoint Graph and Joint-Trajectory Bound

**Date:** 2026-08-29  
**Scope:** high-value centered D2 covariance rows `(0,1,3,7)` after Iterations 034–038.  
**Status:** detector-architecture/resource bound; no new-physics claim.

## 1. Why Iteration 038 was still optimistic

Iteration 038 treated the four high-value covariance rows as if a minimal joint readout had eight independent scalar outputs, two for each covariance row. But the actual Toy009/Iteration-011 row pattern reuses endpoints.

The four rows are

- row `0`: `cov[G0(TR),G0(0)]`;
- row `1`: `cov[G0(T1),G1(0)]`;
- row `3`: `cov[G1(TR),G0(0)]`;
- row `7`: `cov[G0(T6),G1(0)]`.

They involve only six unique phase/probe endpoints:

`G0(0), G0(TR), G0(T1), G1(0), G1(TR), G0(T6)`.

Therefore a natural phase-referenced shared trajectory is six-dimensional, not eight-dimensional.

## 2. Endpoint graph

Represent each scalar detector endpoint as a graph vertex and each desired cross-covariance as an edge.

The graph has six vertices and four edges. It decomposes into two degree-two stars:

- center `G0(0)` connected to `G0(TR)` and `G1(TR)`;
- center `G1(0)` connected to `G0(T1)` and `G0(T6)`.

This shared-endpoint structure matters because the four covariance entries cannot all be varied as if they occupied four independent two-dimensional detector blocks.

## 3. Natural cross-covariance encoding

Take a whitened Gaussian detector covariance with nominal `Sigma0=I_6`. Let each source covariance coordinate change only the corresponding off-diagonal detector covariance entry.

For an edge `(u,v)`, define

`H_i = a (|u><v| + |v><u|)`.

The covariance Fisher matrix is

`K_ij = 1/2 Tr(H_i H_j)`.

The four distinct edges are Frobenius-orthogonal, so

`K=a^2 I_4`.

However, positivity for the full calibration hypercube is controlled by the signed adjacency matrix of each degree-two star. Its nonzero eigenvalues are

`+/- a sqrt(2)`.

Therefore full-hypercube positivity requires

`a < 1/sqrt(2)`.

Hence

`boxed: K_ii < 1/2`.

## 4. RQIR-NG-018 — shared-endpoint covariance bound

For the current six-endpoint, cross-covariance-only implementation of rows `(0,1,3,7)`, each simultaneously measured covariance coordinate carries less than one-half Fisher unit per accepted Gaussian trajectory sample under the full-range affine positivity requirement.

This is stricter than the generic Iteration-038 `m=6,q=4` trace bound

`lambda_min(K)<3/4`.

The loss comes from **endpoint sharing**: two covariance directions compete for the same detector variable at each star center.

This is a detector-architecture bound, not a fundamental bound on all possible measurements of the source correlators. Diagonal-variance response, extra independent channels, non-Gaussian readout or a different physical parameter domain can change it.

## 5. Accepted shared-cycle lower bound

The preferred centered D2 covariance weight is

`gamma_cov~=0.590127e6`.

With the graph limit `lambda_min(K)<1/2`, reproducing the four-row covariance Fisher block at `lambda=1` requires

`boxed: N_joint > 1.180254e6 accepted trajectories`.

An explicit near-saturating choice

`a=0.999/sqrt(2)`

gives

`K=0.4990005 I_4`

and requires approximately

`1.182618e6`

accepted trajectories.

Thus the actual endpoint-sharing geometry halves the ideal weakest-direction Fisher of the disjoint-eight-output construction from Iteration 038.

## 6. Source-metrology break-even becomes stricter

The best four covariance rows save

`Delta C_alpha~=4.5050486`.

With

`F_Q^(alpha)=0.0849323916`,

that corresponds to only

`~53.04`

accepted single-branch source-metrology copy equivalents.

Using the optimistic graph limit `K_ii->1/2`, covariance can beat preparation only if

`boxed:
(p_C eta_C)/(p_P eta_P) * t_P/t_C > ~2.22510e4`.

At equal acceptance/efficiency this is twice the already demanding `m=8` ideal shared-shot ratio from Iteration 038.

## 7. Coherence-coupled threshold

The endpoint set contains `G0(T6)` with

`T6=4.99085067`

in dimensionless source phase. Therefore a shared trajectory must remain coherent at least until

`T_coh,min=T6/(2 pi f_gap)`.

At `100 Hz`,

`T_coh,min~=7.94319 ms`.

Combining with the graph Fisher ceiling gives the necessary equal-efficiency preparation-cycle threshold

`boxed: t_P > ~176.74 s`.

Adding a transparent `1 ms` detector dead/readout overhead gives

`boxed: t_P > ~198.99 s`.

So, in the natural six-endpoint cross-covariance architecture, source metrology must be slower than roughly **three minutes per accepted effective copy** at 100 Hz before the covariance-only route even has the possibility of winning wall-clock time under otherwise ideal assumptions.

Representative no-dead-time scaling:

| gap | covariance coherence floor | necessary preparation cycle |
|---:|---:|---:|
| 10 Hz | ~79.43 ms | ~1767 s (~29.5 min) |
| 100 Hz | ~7.943 ms | ~176.7 s (~2.95 min) |
| 1 kHz | ~0.7943 ms | ~17.67 s |

## 8. Interpretation

This strengthens the resource-side lesson from Iterations 037–038:

- covariance complementarity is geometrically powerful;
- shared acquisition helps substantially;
- but the actual phase/probe endpoint graph limits how much independent covariance information one trajectory can contain;
- source verification remains extremely competitive because the corrected hidden-amplitude QFI needs only about 53 copy equivalents to replace the first-four covariance contribution.

Therefore a covariance-only D2 implementation is unlikely to be the preferred resource path unless source metrology is intrinsically slow or the detector extracts additional useful information from the same trajectory.

## 9. What can evade the bound

The present bound does not exclude architectures where:

1. the six scalar endpoints are measured by multiple independent detector quadratures/channels;
2. the source coordinate changes diagonal detector variances as well as cross-covariances;
3. the same trajectory provides strong force-mean Fisher in addition to covariance Fisher;
4. the physical calibration domain is narrower than the normalized full hypercube;
5. a non-affine/non-Gaussian measurement is used;
6. continuous weak measurement and smoothing extract a larger effective record while explicitly accounting for backaction.

These possibilities define the next gate rather than being assumed.

## 10. Reproducibility

Code:

`analysis/d2_covariance_endpoint_graph_iteration039.py`

It reconstructs the six endpoint labels and four-edge graph, verifies the degree pattern, checks full-hypercube positivity of a near-saturating edge encoding, computes the covariance Fisher block, compares with the generic `m=6` bound and evaluates the corrected source-QFI/coherence break-even.

## 11. Next gate

Build a **joint trajectory mean+covariance likelihood on these six endpoints**. The same source trajectory naturally contains endpoint means as well as cross-covariances. The next calculation must determine whether the force-mean Fisher accumulated by those same trajectories can make the complementary branch resource-competitive despite the covariance-only bound, while profiling timing, additive, imprecision and backaction nuisances.
