# RQIR Research Log — Iteration 039

**Date:** 2026-08-29  
**Target:** replace the optimistic eight-independent-output shared covariance model by the actual endpoint-sharing structure of the best centered D2 rows `(0,1,3,7)`.

## Endpoint reconstruction

The four rows are:

- `0`: `cov[G0(TR),G0(0)]`;
- `1`: `cov[G0(T1),G1(0)]`;
- `3`: `cov[G1(TR),G0(0)]`;
- `7`: `cov[G0(T6),G1(0)]`.

They use six unique scalar endpoints and form two disjoint degree-two stars.

## New detector-architecture bound

For a natural whitened cross-covariance-only Gaussian encoding, each row derivative is an off-diagonal edge matrix

`H_i=a(|u><v|+|v><u|)`.

The signed derivative sum on a degree-two star has operator norm `a sqrt(2)`. Full-hypercube positivity therefore requires

`a<1/sqrt(2)`.

Since `K_ii=1/2 Tr(H_i^2)=a^2`, each row has

`K_ii<1/2`.

This is **RQIR-NG-018 — shared-endpoint covariance bound**. It is stricter than the generic `m=6,q=4` trace bound `lambda_min<3/4` because two covariance directions share each star center.

## Resource implication

At centered `gamma_cov~0.590127e6`, an ideal shared trajectory needs

`>1.180254e6`

accepted cycles at `lambda=1`. A near-saturating `a=0.999/sqrt(2)` construction requires `~1.182618e6`.

The four covariance rows save only `Delta C_alpha~4.5050486`, or `~53.04` accepted single-branch source-metrology copy equivalents at the corrected QFI.

Thus the equal-efficiency break-even becomes

`t_P/t_C > ~2.22510e4`.

At 100 Hz the shared trajectory must remain coherent for at least `7.94319 ms`, giving a necessary source-metrology cycle

`t_P>~176.74 s`

before detector overhead, or `~198.99 s` with a transparent `1 ms` dead/readout time.

This strengthens the conclusion that covariance-only complementarity is resource-competitive only if independent source verification is intrinsically slow or the same detector trajectory carries additional useful information.

## Files

- `analysis/d2_covariance_endpoint_graph_iteration039.py`
- `docs/D2_COVARIANCE_ENDPOINT_GRAPH.md`
- `recovery/RECOVERY_DELTA_ITERATION_039.md`

## Next gate

Use the same six-endpoint trajectory to accumulate force-mean and covariance Fisher jointly. The next likelihood must include endpoint means, the four cross-covariances, timing/additive controls, imprecision and backaction in one profiled Fisher rather than treating covariance as a separate campaign.
