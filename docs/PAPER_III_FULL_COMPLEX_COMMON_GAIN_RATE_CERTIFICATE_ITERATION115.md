# RQIR Iteration 115 — Full-Complex Common-Gain Rate Certificate

**Date:** 2026-08-31  
**Status:** Paper-III detector/transfer resource closure; exact local Fisher reduction and robust rate-ratio certificate. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 114 showed that in the retained two-band D2 likelihood the two fractional band gains split into

- a **common gain** direction exactly aligned with the science amplitude `beta`;
- a **differential gain** direction exactly aligned with the already-profiled spectral tilt.

It introduced a scalar effective common-gain reference Fisher `C_com` and the combined science/transfer rate

`R_DT = 1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

The remaining gap was physical: Iterations 101–103 define the same-state dual-tone calibration in the full four-real transfer space (two amplitudes and two phases), while Iteration 114 used a two-real gain quotient. This iteration derives the exact bridge from the measurable full complex per-block Fisher matrix to the scalar `R_c` needed by the Toy009/Toy014 architecture decision.

## 2. Physical per-block Fisher-rate matrix

Use local transfer coordinates

`x=(g2,g4,phi2,phi4)`,

where `g2,g4` are fractional/log-amplitude transfer coordinates and `phi2,phi4` are phase coordinates.

For one accepted same-state dual-tone reference block, Iteration 101 gives

`F_blk = J_chi^T Sigma_z^-1 J_chi`.

If independent attempts have acceptance `p_cal` and full cycle wall time `tau_cyc` (including acquisition, reset/readout and pure dead time), the expected Fisher-rate matrix is

`boxed{K_x = (p_cal/tau_cyc) F_blk}`

when rejected attempts carry no usable transfer Fisher. More generally use the actual expected Fisher per attempted cycle; do not multiply by `p_cal` if rejected blocks themselves carry information.

Independent reference subprotocols add at the rate-matrix level:

`K_x = sum_b K_x^(b)`.

Thus `K_x` has physical units of inverse-time in dimensionless local transfer coordinates and is the correct object to compare with science Fisher rates.

## 3. Common/differential transformation

Define

`g2=c-d`,

`g4=c+d`.

With

`y=(c,d,phi2,phi4)`,

the linear map is `x=T y`, so Fisher transforms as

`K_y=T^T K_x T`.

Write

`K_y = [[k_cc, k_cnu], [k_nuc, K_nunu]]`,

where the nuisance block is

`nu=(d,phi2,phi4)`.

### RQIR-RESOURCE-079 — full-complex common-gain Fisher rate

The exact scalar reference rate relevant to the science amplitude is

`boxed{R_c = k_cc - k_cnu K_nunu^-1 k_nuc}`.

Equivalently,

`R_c = Schur_c(K_y)`.

This profiles differential gain and both phase coordinates inside the same calibration likelihood before the reference rate is inserted into RESOURCE-078.

If `K_nunu` is singular, reduce the likelihood to its identifiable support or add a physically declared independent prior/reference Fisher. Do not hide a non-identifiable phase/gain direction with an arbitrary pseudoinverse threshold.

## 4. Associativity: phase-first and direct profiling agree

Partition `K_y` into gains `(c,d)` and phases `phi=(phi2,phi4)`.

First profile phase:

`K_g|phi = K_gg - K_gphi K_phiphi^-1 K_phig`.

Then profile differential gain:

`R_c = (K_g|phi)_cc - (K_g|phi)_cd^2/(K_g|phi)_dd`.

The quotient property of Schur complements gives exactly the same result as profiling `(d,phi2,phi4)` in one step.

The stored deterministic regression checks 1000 random positive-definite 4x4 matrices and finds maximum direct/nested relative disagreement

`< 1.6e-15`.

### RQIR-CAL-022 — nuisance-complete transfer-rate reduction

A quoted dual-tone amplitude SNR is not by itself the `R_c` entering the science schedule when amplitude and phase estimates are correlated. The full accepted-block Fisher/covariance must first be profiled over every transfer nuisance that is not the science-aligned common-gain coordinate.

## 5. Recovery of the Iteration-114 two-gain formula

If phases are absent or already independently known, let the 2x2 gain Fisher-rate matrix in `(g2,g4)` be

`K_g=[[K22,K24],[K24,K44]]`.

RESOURCE-079 reduces exactly to

`boxed{R_c = 4 det(K_g)/(K22+K44-2K24)}`.

For independent band references (`K24=0`),

`R_c = 4 K22 K44/(K22+K44)`.

Thus Iteration 114 is the phase-profiled 2D slice of the full-complex certificate, not a separate approximation.

## 6. Exact condition for `c=1`

For Toy009 and Toy014 define

`c = R_c,14/R_c,09`.

A **sufficient exact condition** for `c=1` is that the same-state reference campaign have the same physical Fisher-rate matrix in the same transfer coordinates:

`boxed{K_x,14 = K_x,09  =>  c=1}`.

This requires equality of the complete effective reference likelihood, including

- the dual-tone transfer Jacobian;
- full same-block covariance/cross-covariance;
- block duration and window;
- acceptance/reset/readout duty;
- feedback/trap/detector operating state;
- any phase or transfer nuisance priors included in the reference likelihood.

Merely using the same detector hardware is **not** sufficient if changing the source architecture changes one of these quantities.

### RQIR-NG-072 — hardware identity does not imply reference-rate identity

Do not set `c=1` because Toy009 and Toy014 are imagined on the same apparatus. `c=1` is licensed only by a source-independent same-state transfer likelihood/rate matrix, or by measurements showing equality within a declared interval.

This tightens the provisional `c=1` slice used only illustratively in Iteration 114.

## 7. Homogeneity and relative matrix bounds

RESOURCE-079 is homogeneous:

`R_c(lambda K)=lambda R_c(K)`, `lambda>0`.

It is also monotone in Loewner order. One useful variational representation is

`R_c(K)=min_nu [1,nu^T] K_y [1,nu^T]^T`.

Therefore

`K_A >= K_B > 0  =>  R_c(K_A)>=R_c(K_B)`.

Suppose a common positive-definite reference matrix `K0` satisfies

`m_i K0 <= K_i <= M_i K0`

for architecture `i`.

Then

`boxed{m_i R_c0 <= R_c,i <= M_i R_c0}`.

For Toy014/Toy009 this gives the robust ratio enclosure

`boxed{c in [m14/M09, M14/m09]}`.

### RQIR-RESOURCE-080 — Loewner-to-architecture transfer certificate

A full uncertain 4D complex transfer reference can be propagated to the scalar architecture variable `c` without assigning independent amplitude/phase error bars. Relative positive-semidefinite bounds on the measured Fisher-rate matrices are sufficient.

This is particularly useful when the same apparatus supplies both source designs and systematic uncertainty is naturally expressed as a common matrix envelope.

## 8. Combined science/transfer rate with an interval-valued reference ratio

Iteration 114 gives

`R_DT = 1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

For Toy014/Toy009 define

`s=R_s,14/R_s,09`,

`c=R_c,14/R_c,09`,

`z=R_c,09/R_s,09`.

Then

`boxed{u_DT(s,c,z)=[(1+z^-1/2)/(s^-1/2+(c z)^-1/2)]^2}`.

The function is strictly increasing in `s` and `c` for positive arguments. For fixed `(s,c)`, its dependence on `z` is monotone as well; the sign is controlled by whether `s<c`. Consequently a rectangular interval in `(s,c,z)` is certified by its corners; no hidden interior extremum exists.

### RQIR-RESOURCE-081 — robust common-gain quotient box

For declared intervals

`s in [sL,sU]`, `c in [cL,cU]`, `z in [zL,zU]`,

the exact robust enclosure of the current separate-time science+transfer quotient is obtained by evaluating the eight corners of the box.

A deterministic dimensionless regression uses only to test the algebra

`s in [0.25,0.35]`, `c in [0.8,1.25]`, `z in [0.05,20]`

and obtains

`u_DT,min ~= 0.2957458954`,

`u_DT,max ~= 0.9247878849`.

A dense interior scan remains inside these bounds. These values are not Toy009/Toy014 apparatus forecasts.

## 9. Relation to D1/D2 identifiability and NG-005

This transfer reduction does not weaken the mature identifiability requirements.

- The detector science object remains `F_beta|theta` after source, spectral-shape, transfer and apparatus nuisance profiling.
- NG-005 remains active: gravitational-null data cannot self-calibrate the hidden source-preparation amplitude. Independent source metrology still contributes its own Fisher/time budget.
- NG-056/NG-071 remain active: free transfer gains erase the common science amplitude regardless of additional science exposure.
- RESOURCE-079 only tells us how a **real independent same-state transfer reference** repairs that detector-transduction degeneracy.
- D1 and D2 must each use their own physical transfer/noise likelihood; no D2 common-gain rate is silently imported into D1.

## 10. What this iteration closes

Closed:

- exact conversion from per-block full-complex dual-tone Fisher plus cycle/acceptance into a physical rate matrix;
- exact reduction of that 4D rate to the one common-gain rate relevant to the two-band science amplitude;
- proof that phase-first and direct nuisance profiling agree;
- exact condition under which the illustrative `c=1` assumption is valid;
- negative gate against assuming source-independent calibration from hardware identity alone;
- Loewner matrix bounds -> robust `c` interval;
- exact corner propagation from `(s,c,z)` to `u_DT`.

Still open:

- measured/defensibly specified same-state `K_x` for Toy009 and Toy014 under one apparatus;
- physical phase/gain drift matrix needed for recertification, if references are separate pure-dead blocks;
- the seven calibration-layer physical rate matrices in the same apparatus;
- geometry and additive SI control rates;
- final robust detector-side `u` and total architecture decision through RESOURCE-061/063 and NG-030.

## 11. Next admissible gate

Propagate RESOURCE-079/080 into the seven-layer campaign scheduler rather than treating transfer as an isolated scalar campaign. The key question is whether the same dual-tone blocks can simultaneously carry Fisher for transfer and any of the seven calibration-layer nuisance coordinates.

If their Fisher matrices share a physical acquisition block, use RESOURCE-057/064 and credit the joint matrix once. If they require non-overlapping pure-dead blocks, use the recertification/control overhead formalism of Iterations 107–112. This will produce the first non-double-counted robust interval for the full detector-side ratio `u` with common-gain transfer included.

## 12. Reproducibility

Run

`python analysis/full_complex_common_gain_rate_iteration115.py`.

The script verifies nested/direct Schur equality, recovery of the Iteration-114 formula, exact `c=1` under identical likelihoods, Loewner propagation and the robust `(s,c,z)` corner certificate.
