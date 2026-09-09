# RECOVERY DELTA — ITERATION 660

Date: 2026-09-09

## Authority entering
Iter659 retained the normalized same-parent closed-SK Gamma3 six-term topology and required a fixed-epsilon routing/support audit before any numerator-weighted soft-family cut evaluation.

## Result
Using frozen Iter655 kinematics, `q1^2=s`, `q3^2=0`, and `q2^2=s-2 eps sqrt(s)`. With `m^2=49/100`, the massive two-particle threshold is `4m^2=49/25`.

The q3-transfer K1K2 bubble has no massive ordinary two-particle cut. The q1 bubble has support for `s>=49/25`; the q2 bubble has support for `s-2 eps sqrt(s)>=49/25`, equivalently `sqrt(s)>=eps+sqrt(eps^2+4m^2)`.

For both K1^3 triangle orientations, fixed `eps>0` gives no positive-alpha leading Landau point because interior stationarity requires `alpha2(s-u)=2 alpha2 eps sqrt(s)=0`. The coincident `eps->0` boundary is not promoted because `D_s` is frozen before the soft limit.

Classification: `PASS_ITER660_SOFT_ROUTING__Q3_BUBBLE_NO_MASSIVE_CUT__Q1_Q2_THRESHOLDS_EXPLICIT__NO_FIXED_EPS_POSITIVE_ALPHA_LEADING_TRIANGLE_LANDAU__NON_RESIDUAL`.

## Canonical raw Actions provenance
- run: `34334410816`
- job: `102410321810`
- head: `6c74089df150fa4eb465e636e29d81d36f2e7f84`
- artifact: `10097091086`
- artifact digest / downloaded ZIP SHA-256: `e98203376c103d6119efb10d2fdab66b8e378d26a3e9ac29639c727170735232`
- raw JSON SHA-256: `777003d4f8d31bf9222ebb7b392002647699924324487d234e9e72a5dafed75a`
- raw result: `failures=[]`, `scientific_gate_pass=true`, `candidate_numerator_cut_values_read=false`, `zero_fill_allowed=false`.

The earlier persisted digest was replaced after direct artifact API/download verification; the scientific payload and classification are unchanged.

## Guardrails
The soft bubble is analytically no-cut, not a zero-filled amplitude. No Candidate numerator cut values were read. Source/Born subtraction remains `NOT_PERFORMED`. Iter653 common `i/2` parent normalization and Iter655 cut-before-soft-limit ordering remain frozen.

## Readiness
MODEL_READINESS: 24%

Delta: 0 percentage points. Robust unique residual discovery remains `0/20`.

## Exact next gate
Iteration661: construct quotient-safe plus-TT numerator-weighted `D_s` integrands for the q1/q2 hard-transfer K1K2 bubbles and both K1^3 triangles at fixed `eps>0`, using exact Iter594 vertices and Iter653 normalized parent; retain q3 transfer explicitly as no-cut and keep Source/Born subtraction `NOT_PERFORMED`.
