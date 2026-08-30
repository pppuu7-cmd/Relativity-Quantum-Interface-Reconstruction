# RQIR Research Log — Iteration 076

**Date:** 2026-08-30

## Question

How does Toy014's stricter timing tolerance enter wall clock when timing reference must be periodically recertified under a Brownian drift benchmark?

## Result

With a timing-reference block targeting `sigma_ref=sigma_target/3` and zero independent floor,

`T_ref=(t_cycle/p)(sigma_event/sigma_ref)^2`

and

`T_cad=(16/9)sigma_target^2/D_tau` hours.

Therefore

`d_tau=T_ref/T_cad proportional to D_tau sigma_event^2 t_cycle / sigma_target^4`.

New retained result **RQIR-RESOURCE-035 — timing recertification has a fourth-power tolerance penalty**.

For the transparent common benchmark `sigma_event=10 us`, `p=.5`, dead/read `1 ms`:

- at `D=100 us^2/h`: Toy014 timing-reference duty `0.0878%`, Toy009 `0.00353%`;
- at `D=1000`: Toy014 `0.878%`, Toy009 `0.0353%`.

Thus Toy014 pays about `24.91x` the Toy009 timing-reference duty under equal drift/jitter assumptions because its timing tolerance is much stricter. But absolute duty is still below 1% across these two illustrative diffusion levels.

Including duty as payload multiplier `m=1/(1-d)` shifts the Toy014-vs-Toy009 projected boundary from

`y > 7.6895 + 7.5421 x`

to approximately

- `D=100`: `y > 7.7118 + 7.5640 x`;
- `D=1000`: `y > 7.9178 + 7.7665 x`.

So the control correction is modest in this drift range.

Toy014 reaches 10% timing-reference duty near `D~1.14e4 us^2/h`; the simple cadence model formally saturates near `D~1.14e5 us^2/h`. A nonzero stability floor can make cadence fail much earlier, consistent with NG-007.

## Next

Use the Iteration-071 general rate closure to define the minimal set of apparatus ratios that must actually be measured to decide among Toy009, Toy014 and Toy013: profiled science Fisher rate, seven matrix calibration rates, source-metrology rate, and timing/reference drift duty. Avoid arbitrary ASD substitution until a concrete detector model exists.
