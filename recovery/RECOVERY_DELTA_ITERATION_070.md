# RQIR Recovery Delta — Iteration 070

**Date:** 2026-08-30

## Continuation point

Iteration 069 established the full `2x2` same-time dual-probe matrix-Fisher calibration likelihood. Iteration 070 translates that result into a declared equivalent-force PSD reference likelihood and combines it with the Toy009/Toy013 wall-clock dominance boundary.

## Equations to retain

For one rectangular equivalent-force template of duration `T` and one-sided white PSD `S_F=A_F^2`:

`I_F = 2 F^2 T/S_F`.

For symmetric dual-probe correlation `rho`:

`I_cal,min = 2 F_cal^2 T/[S_F(1+|rho|)]`.

Define

`r_F=F_sci/F_cal`.

Under the explicit common-PSD/common-schedule reference likelihood:

`x=T_cal/T_sci = 296.184784604 (1+|rho|) r_F^2`

for Toy009 at `Z=5`.

Combine with Iteration-066:

`x > 25.8350584 + 376.305592 y`,

`y=T_src009/T_sci009`.

Therefore

`296.184784604 (1+|rho|) r_F^2 > 25.8350584 + 376.305592 y`.

Equivalent critical force-scale ratio:

`r_F,crit = sqrt[(25.8350584+376.305592 y)/(296.184784604(1+|rho|))]`.

## Numerical anchors

At `r_F=1`:

- `rho=0`: `x=296.184784604`, `ycrit=0.718431328`;
- `rho=0.5`: `x=444.277176906`, `ycrit=1.111974224`;
- `rho=0.9`: `x=562.751090748`, `ycrit=1.426808540`.

At `rho=0`:

- `y=0`: `r_F,crit~0.29534`;
- `y=0.1`: `r_F,crit~0.46298`;
- `y=1`: `r_F,crit~1.16510`.

## New labels

- **RQIR-RESOURCE-032:** physical transduction-ratio closure of the Toy009 mean-calibration/science wall-clock ratio under one declared equivalent-force likelihood.
- **RQIR-NG-028:** absolute ASD cancellation is conditional on common science/calibration transfer, PSD, acceptance and acquisition structure; otherwise separate matched-filter integrals are mandatory.

## Interpretation guard

The white common-PSD likelihood is a controlled reference benchmark only. It is not a claimed apparatus sensitivity. It is useful because it identifies the physical ratio that must replace the old abstract calibration-SNR placeholder.

## Active gates unchanged

Keep NG-005, NG-006, NG-023, NG-026, NG-027 and all gauge/conservation/positivity/causality/EFT/renormalization/full-QFT/stochastic/classical-gravity degeneracy gates open.

## Reproduce

`python analysis/d2_force_psd_wallclock_surface_iteration070.py`

## Next exact task

Replace the common-PSD/common-schedule benchmark by separate

`K_sci=4 int |H_sci|^2/S_sci df`

and

`K_cal,j=4 int J_j^dag S_j^-1 J_j df`,

including acceptance, dead time, coherence windows and source reset/visibility. Then evaluate one unified total-wall-clock surface without assuming cancellations that are not structurally justified.
