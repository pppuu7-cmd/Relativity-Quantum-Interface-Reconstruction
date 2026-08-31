# Recovery Delta — RQIR Iteration 216

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Iteration 215 provided a physical pure-Einstein five-graviton finite-cut vector on the frozen 12-point soft grid with pointwise conservative numerical errors.

Iteration 216 stress-tests its polyhomogeneous compression.

Key results:

- `n<=2` regular+log basis fails numerical completeness: max residual/error `1209.93`, RMS `368.37`;
- `n<=3` basis `[1,L,z,zL,z^2,z^2L,z^3,z^3L]` is the first tested order that fits the entire physical vector inside its pointwise numerical envelope: max residual/error `0.6374`, RMS `0.2467`;
- full-window `n=3` condition number `2.7955e5`;
- fixed window coefficient shifts are `1e-4...5e-4` for the useful 10-point audits and remain inside the conservative compression-sensitivity envelope;
- a fit trained on the ten larger-epsilon points predicts the two smallest-epsilon points within `0.196 sigma_num`;
- a fit trained on the ten smaller-epsilon points fails badly on the two largest-epsilon points (`>2.16e4 sigma_num`), proving resolved higher-order finite-soft content at the large-epsilon edge.

Authority change:

`PRIMARY C5 ON-SHELL COMPARATOR DATUM = physical 12-point finite-cut vector + pointwise numerical error envelope`.

Regular+log coefficients are compression only, not exact theory authority.

Retain `C5-CUT-016`, `SOFT-NG-009`, `NUM-NG-018`, `NG-FUNNEL-073`.

Readiness unchanged: comparator foundation still lacks the source-completed off-shell C5 linked cut plus AS/C3 nonlinear real-time cuts.

Next: test whether the on-shell control uniquely determines the off-shell/source-completed `T_cut`; if not, freeze the bridge as non-identifiable and construct the cut directly at observable/source level.
