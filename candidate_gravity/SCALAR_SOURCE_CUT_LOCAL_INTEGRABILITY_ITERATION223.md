# Candidate Gravity — Iteration 223: local existence of the Born-subtracted source hard remainder

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

Use the Born-fixed Iteration-222 subtraction

`I_sub = I_cut - R/(1-n.n_in) - R/(1-n.n_out)`, with `R=-8 M_Born`.

For both collinear directions and five fixed local azimuths, the remaining kernel has fitted small-angle powers between approximately `-0.98` and `-1.08`, consistent with

`I_sub = O(1/delta)`.

At `delta=0.001`, `delta*|I_sub|` remains finite for every tested azimuth and agrees between incoming/outgoing neighborhoods.

Because `dOmega ~ delta d(delta) d(phi)`, this behavior is locally integrable. Thus the leading `delta^-2` divergence is physically removed by the Born-fixed subtraction and the hard remainder exists locally as an improper phase-space integral.

This does **not** certify a global numerical integral; global quadrature convergence is a separate gate.

Retain `SRC-CUT-004`, `IR-NG-007`, `NG-FUNNEL-079`.

`MODEL_READINESS: 23%` — unchanged.
