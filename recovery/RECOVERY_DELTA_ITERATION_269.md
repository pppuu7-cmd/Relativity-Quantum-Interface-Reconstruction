# RECOVERY DELTA — Candidate Gravity Iteration 269

**Date:** 2026-09-02  
**Authoritative iteration:** 269  
**MODEL_READINESS: 24%**

## Correction from the Iteration-268 follow-up audit

Primary same-parent authority fixes the explicit gravity gauge weight such that, in condensed-index normalization and up to the frozen overall sign,

`Y^up = g^-1/sqrt(|g|)`,

`Y_down = sqrt(|g|) g`,

with

`Nhat=Y^up N_orb`, `N_orb=Y_down Nhat`.

The representative density factor used in Iterations 252/258 was inverted. TT first order is unaffected because `delta sqrt(|g|)=0`; second order is affected.

For single-mode TT `H=eta^-1 eps`:

`Y_down = eta + t eps - t^2 (tr(H^2)/4) eta + ...`.

The previous `+tr(H^2)/4` coefficient is superseded.

## Corrected routed physical N/Q

Iteration-268 Fourier routing remains exact:

`Q1[x](p)=-Q0(p+k_x)N1[x](p)Q0(p)`

and

`Q2[x,y](p)=Q0(p+k_x+k_y)[N1[x](p+k_y)Q0(p+k_y)N1[y](p)+N1[y](p+k_x)Q0(p+k_x)N1[x](p)-N2[x,y](p)]Q0(p)`.

Corrected values at the frozen generic loop momentum:

- `||Q2[s,a]||_F=1.8689138370`;
- `||Q2[s,b]||_F=3.5158966341`;
- `||Q2[a,b]||_F=1.0700741894`.

Second-order inverse residuals are `<=4.45e-16`.

Endpoint-reversed transpose is restored:

- Q2 `sa`: `4.49e-8`;
- Q2 `sb`: `1.67e-8`;
- Q2 `ab`: `7.69e-9`.

The superseded density gives N2 endpoint-transpose residuals `0.03165`, `0.21036`, `0.62805`, proving the correction is necessary.

Freeze:

`PASS_PRIMARY_AUTHORITY_ORBIT_DENSITY_CORRECTION_AND_ROUTED_N2_Q2_TRANSPOSE_RESTORATION`.

Guardrail:

`USE_Y_UP=g^-1/sqrt|g| AND Y_DOWN=sqrt|g|*g; DO_NOT_USE_THE_INVERTED_DENSITY_FACTOR`.

## Supersession scope

- Iteration 252: supersede only its explicit density representative; retain `Nhat=Y^up N_orb` and TT `deltaY^up=-eps^up`.
- Iteration 258: supersede density inverse, second-order sign and Norb2 numerical values.
- Iteration 259: supersede numerical Q2 inherited from old Norb2; retain inverse-recursion algebra.
- Iteration 268: supersede numerical N2/Q2 only; retain Q1, exact routing and same-p rejection.

All other frozen C5 algebra/topology/polarization results remain authoritative.

Retain `BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`, `BLOCKED_NOT_ZERO`.

No robust residual; `ANSATZ-003` not created; Fisher/resources and heavy integration forbidden.

## Files

- `candidate_gravity/C5_VD_ORBIT_DENSITY_CORRECTION_ITERATION269.md`
- `candidate_gravity/code/iteration269_vd_orbit_density_correction.py`
- `candidate_gravity/results/iteration269_vd_orbit_density_correction.json`
- `research_log/2026-09-02_iteration_269_vd_orbit_density_correction.md`
- `recovery/RECOVERY_DELTA_ITERATION_269.md`

## Exact next gate — Iteration 270

Rebuild routed physical `K/A` and assemble the eight independent `+K` B3 representatives using corrected Q2. Reconstruct all seven transpose partners through endpoint reversal / real `-K` sector. Only after every pair passes may explicit nonzero B3 be frozen and tensor reduction considered.
