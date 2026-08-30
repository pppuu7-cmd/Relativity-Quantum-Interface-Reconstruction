# RQIR Iteration 108 — Exact Timing-Reference Overhead Convention

**Date:** 2026-08-30  
**Status:** Paper-III resource-accounting consistency correction; retained timing numbers are benchmarks, not apparatus forecasts and not new-physics claims.

## 1. Purpose

Iteration 107 introduced an exact finite periodic-reference schedule. Re-reading the mature Iteration-076 timing-recertification calculation against that convention exposed a small but conceptually important resource-accounting mismatch.

Iteration 076 defined

`r_ref = T_ref/T_cad`

where `T_cad` is the allowed informative/live interval between reference blocks, and referred to `r_ref` as a duty fraction. It then used the payload multiplier `1/(1-r_ref)`.

Under the explicit Iteration-107 convention, however, `r_ref` is a **reference-overhead / live-time ratio**, not a fraction of total wall time.

## 2. RQIR-NUM-007 — duty versus overhead-to-live ratio

If

`r = T_ref/T_live`,

then the exact total wall time per period is

`T_wall=T_live+T_ref=T_live(1+r)`.

Therefore

`boxed{m_wall=1+r}`,

`boxed{d_wall=r/(1+r)}`,

and

`boxed{eta_live=1/(1+r)}`.

The old expression `1/(1-r)` agrees only to first order in small `r`.

This does not invalidate Iteration 076's conclusion that timing overhead is small in its transparent low/moderate-diffusion examples. It corrects the finite-overhead interpretation and removes the unphysical finite point at which a nominal “100% duty” was previously reached.

## 3. Toy009/Toy014 corrected benchmark values

Iteration 076 retained the overhead/live ratios

### `D_tau=100 us^2/h`

- Toy014 `r14=8.78286241090e-4`;
- Toy009 `r09=3.52631154895e-5`.

The exact total-wall reference fractions are instead

- Toy014 `d14=8.77515531272e-4` (`0.0877516%`);
- Toy009 `d09=3.52618720460e-5`.

### `D_tau=1000 us^2/h`

- Toy014 `r14=8.78286241090e-3`;
- Toy009 `r09=3.52631154895e-4`.

Exact total-wall fractions:

- Toy014 `d14=8.70639533854e-3` (`0.870640%`);
- Toy009 `d09=3.52506849997e-4`.

The approximately 25x relative Toy014/Toy009 timing-reference burden remains essentially unchanged because that ratio was already a ratio of the underlying overhead quantities.

## 4. Corrected projected Toy014/Toy009 boundary

Using the retained Iteration-074 projected resource factors only as a regression slice,

`(q_s,q_c,q_p)=(3.53338589945,3.48482822888,0.67054046027)`, 

the exact pure-dead timing multiplier gives

`eta=(1+r09)/(1+r14)`.

The Toy014<Toy009 boundary becomes

`y > (q_s-eta)/(eta-q_p) + [(q_c-eta)/(eta-q_p)] x`.

This gives:

### `D_tau=100 us^2/h`

`boxed{y > 7.71179277314 + 7.56402916784 x}`.

Iteration 076 had `7.711813 + 7.564049 x`; the correction is negligible at this small overhead.

### `D_tau=1000 us^2/h`

`boxed{y > 7.91566900880 + 7.76444739107 x}`.

Iteration 076 had `7.917790 + 7.766532 x`; still a small correction, but now the wall-clock convention is exact.

These are historical projected-resource regressions, not the current final-significance architecture certificate.

## 5. Corrected high-overhead thresholds

In the zero-floor Brownian/reference benchmark of Iteration 076, `r14` is linear in `D_tau`.

An exact **10% fraction of total wall time** in the timing reference means

`d_wall=.1`, hence

`r=.1/.9=1/9`.

For Toy014 this occurs at

`boxed{D_tau ~= 1.26509e4 us^2/h}`,

not the earlier `~1.14e4` value, which corresponded to `r=.1` and therefore an exact wall fraction of only `1/11 ~= 9.09%`.

Likewise the old formal point `r=1` is not 100% wall duty. It is

`d_wall=1/2`.

For Toy014 it occurs at

`boxed{D_tau ~= 1.13858e5 us^2/h}`

and represents 50% reference time.

No finite `r` yields exactly 100% total-wall reference duty; `d_wall -> 1` only as `r -> infinity`. Before that limit, stability-floor failure or breakdown of the simple periodic architecture is the physically relevant obstruction.

## 6. RQIR-RESOURCE-066 — exact pure-dead control correction to `u`

For a detector-side **live** optimized rate ratio

`u_live=R_D,14^live/R_D,09^live`,

if timing references are genuinely pure dead time, the wall-clock detector ratio is

`boxed{u_wall=u_live (1+r09)/(1+r14)}`.

Thus a final-significance detector threshold `u_req` from Iteration 106 translates to the required live-rate ratio

`boxed{u_live > u_req (1+r14)/(1+r09)}`.

This makes the control burden directly composable with RESOURCE-062/063 without confusing reference-over-live ratio and total duty fraction.

If the reference blocks carry nuisance Fisher, RESOURCE-066 must **not** be used; those blocks belong inside the constrained Fisher scheduler of Iteration 107.

## 7. Scientific consequence

The correction is numerically small for the retained `D_tau=100–1000 us^2/h` illustrative range, so no earlier qualitative architecture conclusion changes.

Its importance is methodological:

- low-overhead reference blocks may be approximated by a scalar duty;
- finite/high-overhead regimes require the exact live/reference accounting;
- information-bearing reference blocks require the full constrained Fisher schedule, not any scalar duty correction.

This keeps the Paper-III wall-clock bookkeeping internally consistent before robust Toy009/Toy014 apparatus bounds are assembled.

## 8. Next gate

Timing is now sufficiently parameterized to enter a constrained `u` certificate. Geometry/additive/gain references are less closed physically: their Toy-unit tolerances exist, but a common apparatus transduction, drift spectrum and reference Fisher-rate model are still absent.

The next admissible step is therefore to construct a **control-cut status matrix** for Toy009/Toy014, separate the timing cut that can already be parameterized from geometry/additive/gain cuts that remain data-underdetermined, and derive the minimum measurements required to turn each open cut into a RESOURCE-064 Fisher campaign.

Do not fabricate SI drift rates for those still-open coordinates and do not start Toy015 yet.

## 9. Reproducibility

Run

`python analysis/timing_overhead_convention_iteration108.py`.
