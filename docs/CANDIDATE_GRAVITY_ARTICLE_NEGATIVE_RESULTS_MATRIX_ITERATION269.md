# Candidate Gravity article / negative-results matrix — Iteration 269

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## New correction result

A post-Iteration-268 endpoint-transpose audit exposed a second-order orbit-kernel inconsistency. Primary-authority comparison fixes the condensed gravity gauge weight as

`Y^up=g^-1/sqrt(|g|)`, `Y_down=sqrt(|g|) g`,

up to the common convention sign. The density representative inherited from Iteration 252 was inverted; this is invisible at first TT order but changes the second-order `Norb2/Q2` coefficient.

With the corrected density factor the routed physical second-order inverse layer simultaneously satisfies:

- exact `NQ=I` coefficient identities at `<=4.45e-16`;
- mixed-leg exchange within `4.41e-9`;
- endpoint-reversed Fourier transpose within `4.49e-8`.

The superseded factor leaves stable `N2` endpoint-transpose errors `0.03165`, `0.21036`, `0.62805`.

Freeze:

`PASS_PRIMARY_AUTHORITY_ORBIT_DENSITY_CORRECTION_AND_ROUTED_N2_Q2_TRANSPOSE_RESTORATION`.

## Publication-use classification

This is a valuable audit/correction result: internal inverse identities alone are insufficient to validate a condensed-index implementation when a common density convention is wrong, because an internally consistent but incorrectly weighted `Norb` can still be inverted exactly. Endpoint-reversed kernel symmetry supplies an independent same-parent regression capable of detecting the mistake.

Do not present this as a new-gravity effect, consistency failure of Vilkovisky gravity, Candidate Gravity residual, or final comparator result. It is a correction to our implementation/provenance.

## Funnel status

- C3: unchanged formal nonlinear-completion blocker.
- C4: unchanged mediator degeneracy.
- C5: corrected routed `N/Q` second-order layer now consistent; routed `K/A`, complete physical `B3`, tensor reduction and source projection remain open.
- Candidate residual: absent.
- `ANSATZ-003`: not created.
- Fisher/resources: forbidden.

MODEL_READINESS: 24%.
