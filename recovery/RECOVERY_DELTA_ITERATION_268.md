# RECOVERY DELTA — Candidate Gravity Iteration 268

**Date:** 2026-09-02  
**Authoritative iteration:** 268  
**MODEL_READINESS: 24%**

## Delta from Iteration 267

Iteration 267 froze exact Fourier momentum support for the eight independent null-soft `B3[s,a,b]` transpose representatives. Iteration 268 now constructs the physical routed orbit-metric inverse layer required by those representatives.

Using the same finite-amplitude curved minimal ghost operator and exact factorization `N_orb=W^-1 Nhat`, physical kernels `N1[x](p)` and `N2[x,y](p)` are extracted for the frozen `s,a,b` TT modes.

Exact routed inverse recursion:

`Q1[x](p)=-Q0(p+k_x)N1[x](p)Q0(p)`.

`Q2[x,y](p)=Q0(p+k_x+k_y)[N1[x](p+k_y)Q0(p+k_y)N1[y](p)+N1[y](p+k_x)Q0(p+k_x)N1[x](p)-N2[x,y](p)]Q0(p)`.

At loop momentum `(0.7,-0.4,0.5,0.9)`:

- `||Q1[s]||_F=1.5811155828`, `||Q1[a]||_F=2.6872621928`, `||Q1[b]||_F=2.3701956679`;
- `||Q2[s,a]||_F=1.8134643518`, `||Q2[s,b]||_F=3.0273925480`, `||Q2[a,b]||_F=1.2474224374`;
- exact first/second-order `NQ=I` coefficient residuals <= `8.89e-16`;
- worst Q2 mixed-leg exchange mismatch `2.66e-10` within finite-difference envelope.

The deliberately wrong same-`p` recursion `Q1_wrong=-Q0(p)N1Q0(p)` fails with residuals `0.5414`, `0.2260`, `0.9130`, proving routed endpoint/intermediate propagators are mandatory.

Freeze:

`PASS_SCOPED_PHYSICAL_ROUTED_N1_N2_Q1_Q2_KERNEL_LAYER`.

Guardrail:

`Q0 MUST BE EVALUATED AT EACH ROUTED ENDPOINT/INTERMEDIATE MOMENTUM; SAME-p RESOLVENT INSERTION IS FALSE`.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`,

`BLOCKED_NOT_ZERO`.

No robust Candidate Gravity residual. `ANSATZ-003` not created. Fisher/resources and blind heavy integration remain forbidden.

## Files

- `candidate_gravity/C5_VD_ROUTED_ORBIT_INVERSE_ITERATION268.md`
- `candidate_gravity/code/iteration268_vd_routed_orbit_inverse.py`
- `candidate_gravity/results/iteration268_vd_routed_orbit_inverse.json`
- `research_log/2026-09-02_iteration_268_vd_routed_orbit_inverse.md`
- `recovery/RECOVERY_DELTA_ITERATION_268.md`

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 267: **0 percentage points**. A physical routed comparator-building subblock closes, but the complete C5 comparator coordinate remains incomplete; comparator foundation stays `24/25`, unique residual `0/20`.

## Exact next gate — Iteration 269

Build routed physical `K0/K1/K2 -> A1/A2/A3` using the frozen affine generator, `P=partial R`, and `Gamma0/Gamma1/Gamma2`, with explicit endpoint/intermediate momenta. Then instantiate the eight forward `+K` B3 representatives using the routed Q layer from Iteration 268 and reconstruct seven transpose partners only via endpoint-reversed / `-K` kernel transpose. Determine explicit algebraic nonzero before tensor reduction.
