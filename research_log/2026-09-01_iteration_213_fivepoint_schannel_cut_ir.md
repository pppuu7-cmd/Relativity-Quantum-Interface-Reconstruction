# Research Log — RQIR Iteration 213

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Constructed the first real physical pure-Einstein five-graviton total-s two-particle cut geometry from the validated Iteration-212 KLT tree engine.

Frozen external all-outgoing sector: `--+++`. Tree helicity selection reduces the cut to one nonzero product `M4(--++) * M5(++ + --)`.

The real massless 2->3 family passes mass-shell and momentum-conservation checks at ~`1e-16`.

Infrared endpoint diagnostic at `epsilon=0.01`:

- `theta^2 |I_cut|` tends toward a finite nonzero constant (~`2.64e3` by `theta=0.002`), so the raw integrand behaves as `theta^-2`;
- with the two-body angular measure this implies a logarithmic endpoint divergence;
- direct cap-regulated angular integrations grow linearly with `log(1/delta)`; the six-smallest-cap magnitude fit has relative residual `1.19e-3`.

Therefore the raw five-point cut is forbidden as input to the regular+log soft extractor. The universal gravitational loop IR term must be analytically subtracted or inclusively cancelled first.

No Candidate Gravity residual; readiness unchanged.
