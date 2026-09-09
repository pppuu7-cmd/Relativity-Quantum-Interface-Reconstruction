# RECOVERY DELTA — ITERATION 660

Date: 2026-09-09

## Authority entering
Iter659 retained the normalized same-parent closed-SK Gamma3 six-term topology and required a fixed-epsilon routing/support audit before any numerator-weighted soft-family cut evaluation.

## Result
Using the Iter655 fixed-epsilon soft family

- `q1=p=(sqrt(s),0,0,0)`,
- `q3=-eps n`, `n=(1,0,0,1)`,
- `q2=-q1-q3=-p+eps n`,

one has exactly

- `q3^2=0`,
- `q1^2=s`,
- `q2^2=s-2 eps sqrt(s)`.

For `m^2=49/100`, the massive two-particle threshold is `4m^2=49/25`.

The soft-transfer K1K2 bubble with denominators `D(l),D(l+q3)` has no massive ordinary two-particle cut because `q3^2=0`. The q1 bubble has support for `s>=4m^2`. The q2 bubble has support for `s-2 eps sqrt(s)>=4m^2`, equivalently `sqrt(s)>=eps+sqrt(eps^2+4m^2)`.

Both K1^3 triangle orientations have the same invariant set `{0,s,s-2 eps sqrt(s)}`. For the equal-mass triangle, the Feynman polynomial may be written `F=m^2-alpha1 alpha2 s-alpha0 alpha2 u`, with `u=s-2 eps sqrt(s)`. Interior stationarity would require `alpha2(s-u)=2 alpha2 eps sqrt(s)=0`; at fixed `eps>0`, `sqrt(s)>0`, and positive `alpha2`, this is impossible. Hence there is no fixed-epsilon positive-alpha leading triangle Landau point. The obstruction disappears only at the coincident `eps->0` boundary; because the frozen protocol takes the cut before the soft limit, that boundary is not promoted to fixed-epsilon leading-Landau support.

Classification: `PASS_ITER660_SOFT_ROUTING__Q3_BUBBLE_NO_MASSIVE_CUT__Q1_Q2_THRESHOLDS_EXPLICIT__NO_FIXED_EPS_POSITIVE_ALPHA_LEADING_TRIANGLE_LANDAU__NON_RESIDUAL`.

## Canonical raw Actions provenance
- run: `34334410816`
- head: `6c74089df150fa4eb465e636e29d81d36f2e7f84`
- artifact: `10097091086`
- artifact digest: `sha256:ff04eca955253dac3a6cdd8531fc3b9763937d6c2e272f0ff596303fdd178069`
- raw result: `failures=[]`, `scientific_gate_pass=true`, `candidate_numerator_cut_values_read=false`, `zero_fill_allowed=false`.

## Guardrails
The soft bubble is classified as analytically no-cut, not zero-filled amplitude. No Candidate numerator cut values were read. Source/Born subtraction remains `NOT_PERFORMED`. Finite-family support claims are not substituted for the soft family. The Iter653 common `i/2` parent normalization and Iter655 cut-before-soft-limit ordering remain frozen.

## Readiness
MODEL_READINESS: 24%

Delta: 0 percentage points. A support/routing gate closed, but robust unique residual discovery remains `0/20` and no stable readiness-rubric sector gained a point.

## Exact next gate
Iteration661: construct quotient-safe plus-TT numerator-weighted `D_s` integrands for the two hard-transfer K1K2 bubbles and both K1^3 triangles at fixed `eps>0`, using only same-parent Iter594 vertices and Iter653 normalized parent. Retain the soft-transfer bubble explicitly as no-cut. Evaluate `D_s=Disc_s/(2*pi*i)` before `eps->0`; keep Source/Born subtraction `NOT_PERFORMED` until the matched observable contribution is independently classified.
