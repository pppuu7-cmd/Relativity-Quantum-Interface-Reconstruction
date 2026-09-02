# RQIR research log — Iteration 270

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Continued immediately after the Iteration-269 primary-authority orbit-density correction.

Constructed the direct physical same-parent routed kernel `A=R(DR)E` at finite background amplitudes using the frozen physical TT modes, affine diffeomorphism generator, configuration-space Christoffel and Einstein-action covector. Explicit Fourier bra/input momenta were used for every coefficient.

Key A-layer checks:
- `||A1[s]||=1.00e-9`, consistent with exact null-soft zero;
- `||A1[a]||=0.3539`, `||A1[b]||=0.4374`;
- all mixed A2 are `~0.65-0.75`;
- `||A3[s,a,b]||=2.227819`;
- A3 permutation residual `1.36e-10`;
- endpoint-transpose residuals `<=3.92e-7`.

Enumerated the exact 19 cubic `Q A Q` Leibniz assignments. Four `A1[s]` terms are numerically zero at `~1e-8`, leaving the frozen 15 surviving null-soft terms.

Evaluated the eight Iteration-266 independent forward `+K` classes using corrected Iteration-269 Q2. Every representative is nonzero. Reconstructed/check all seven transpose partners through endpoint reversal into the real `-K` sector; worst pair residual `3.29e-7`.

The 15-term direct sum and 8-class reconstruction agree to `2.78e-16`. Full endpoint-transpose residual is `3.25e-7`.

Physical routed cubic numerator:

`||B3[s,a,b]||_F = 2.2209140981`,

`max|B3| = 1.3471946832`.

Step scans keep `||B3||` within roughly `2e-7` across the tested A2/A3 finite-difference range, excluding numerical near-zero.

Freeze:

`PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED`.

This closes the algebraic nonzero gate and authorizes scoped tensor/master-integral reduction. It is not yet the final C5 comparator coordinate or Candidate Gravity residual. Readiness remains 24% under the frozen rubric. `ANSATZ-003`, Fisher/resources and blind heavy full-C5 runs remain forbidden.
