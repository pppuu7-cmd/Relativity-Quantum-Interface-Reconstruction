# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **602**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` assembly is PASS, non-residual.
- Iter583–584 close the same-parent MSSC-001 quadratic K2 contact and mixed bilinear `K2(h1,h2)`.
- Iter586–590 freeze the timelike off-shell source completion, exact Iter368/582 fixture binding, K1/K2 normalization, and complete cubic family census `K3 + 6 K1/K2 + 6 K1^3`.
- Iter591–594 establish K3/K1^3 analytic structure and explicitly assemble the complete 13-family routed same-action cubic source object; it is finite/nonzero/permutation-symmetric but NON_WARD.
- Iter595–596 prospectively freeze the full nonlinear diffeomorphism Ward contract with five mandatory classes and exact Iter587 one-leg reduction.
- Iter597 is diagnostic only; Iter598 proves it used off-contract arbitrary scalar probes.
- Iter599 corrects the scalar route but fails the one-leg matrix anchor; Iter600 therefore blocks its cubic Ward numbers as nonauthoritative.
- **Iter601 derives the endpoint matrix realization directly from the frozen Fourier rule and raw-validates all 12 Iter587 anchors.**
- **Iter602 reruns the full frozen nonlinear Ward gate with only that endpoint realization changed. The frozen gate is a preserved negative result: 9/12 Ward rows have no threshold failure, while only `s/xi0`, `s/xi1`, `s/xi2` fail and simultaneously fail the frozen convergence criterion.**

## Iter601 endpoint covariance authority
Frozen Fourier rule:
`Delta_xi phi(k)=int xi(l)(k-l)_rho phi(k-l)`.

For row momentum `p_r=p_c+q`, the derived endpoint matrices are:
- right/column endpoint: `R_rc = xi . p_c`;
- left/dual-row endpoint: `L_rc = - xi . p_r`;
- Green covariance identity: `Delta G - R G - G L = 0`.

The old Iter599 use of `T^T` placed the left action on the wrong lattice shift. Raw Iter601 proves this rather than fitting it:
- run `34239749577`, job `102106569680`;
- head `763b2b3e4adab4e30669815f14121bf5f40dfc1d`;
- artifact `10061419511`, digest `sha256:ed7b7f783071c800a203838b2266da2f8ae2c38abd6f696b16705f38f09188c0`;
- raw result SHA-256 `25073d98c96581900a5b33c31f7204ec5d534dda34f2fc41e70fce4e636edd39`;
- max corrected one-leg anchor residual `6.88338845912217e-15 <= 2e-11`;
- old Iter599/600 residuals are reproduced by the omitted left endpoint to max error `6.663279669537638e-15`.

Classification:
`PASS_SCALAR_ENDPOINT_COVARIANCE_MATRIX_REALIZATION_REPRODUCES_ITER587_ANCHOR__NON_RESIDUAL`.

## Iter602 full nonlinear Ward authority
The only production change relative to Iter599 is the Iter601 endpoint realization. Iter596 five mandatory classes, Iter588 fixture, all 13 source families, symmetric per-gauge route, FD steps and thresholds remain unchanged.

Canonical provenance:
- evaluator commit `703eaf4635ed2b0ad82a2da51b350e1b51d9a8a2`;
- workflow/head commit `c3b5d0f796e32be0999e09224031e54b4d494742`;
- run `34240030976`, job `102107522186`;
- artifact `10061578531`, digest `sha256:09f7ef6a98327abff416d46b32a99bfec599a9b68d04edacd91c019ce3436d56`;
- raw result SHA-256 `2897821038b495562d316c56ea40bf051b969a258ece5a2ee2bddc944981d138`;
- raw audit SHA-256 `5cd7f4fa2f59e250d896d06862bfb079cfe27bec0cffe5b0c1d02b73890b71cb`.

Mandatory prerequisites now pass:
- all 12 one-leg anchors PASS, max `6.88338845912217e-15`;
- Iter594 13-family assembly cross-check PASS, max match `5.767843750358048e-08 <= 2e-5`.

Ward rows:
- `s/xi3`: `2.5406450559613046e-14`;
- largest `a` row: `4.925840285606124e-12`;
- largest `b` row: `1.172389197351933e-12`;
- only failures: `s/xi0=0.006096828631513357`, `s/xi1=0.0035599485158516048`, `s/xi2=0.0035599485212443388`.

The three failing `s` rows also fail the frozen convergence condition. For `s/xi0`, the real FD sequence at `(2e-2,1e-2,5e-3)` is
`1.5524867089244463 -> 1.78613555509661e-05 -> -0.0049883971870925`, with last-step `0.00607858101621395 >> 2e-5`.

Iter602 classification:
`FAIL_RAW_CONSUMED_FULL_SOURCE_LEVEL_NONLINEAR_WARD_WITH_ITER601_ENDPOINT_REALIZATION__PRESERVED_NEGATIVE_RESULT`.

This negative frozen-gate result is preserved. Because the only failing rows are also nonconvergent, it is not yet a stable model-level Ward-violation certificate.

## Active diagnostic — Iter603
A separately frozen **diagnostic-only / non-promoting** lattice-radius study is active:
- run `34240339709`, job `102108562629`;
- head `fcd8f27a6d72bb139bf3fc0f05eb1a74f51efbcf`;
- compares `LAT_R=3,4,5` while keeping the physical fixture, endpoint rule, all source families, FD steps and Ward thresholds unchanged.

Its result cannot promote Iter602. It only determines whether the three nonconvergent `s` rows are finite-lattice/boundary sensitive or radius-stable negative evidence. Any later production rerun requires a new prospective contract.

## Frozen nonlinear Ward convention
Use `f(x)=int exp(-ik.x) f(k)` and stripped generator `Delta_xi=i delta_xi`.
All five classes remain mandatory:
1. gauge-leg linear contraction;
2. spectator-u Lie derivative;
3. spectator-v Lie derivative;
4. left scalar/source endpoint transformation;
5. right scalar/source endpoint transformation.

The exact Iter588 fixture is inherited. No new momentum split, gauge normalization, result-dependent polarization, family deletion, threshold weakening or post-hoc source repartition is permitted. The scalar route attached to gauge leg `g` is exactly `p=-q_g/2`, `p'=+q_g/2`.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets kept distinct:
- Candidate `q^2=-1.0`: `+0.0003272233895861266 i`;
- Candidate `q^2=-0.34`: `-0.00371666346186323 i`;
- Candidate `q^2=-0.14`: `-0.0007997265433511544 i`.

No Source/Born subtraction has been performed.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iter601 removes a matrix-realization blocker and Iter602 is a real frozen negative gate, but no model-level rubric sector is yet closed.

## Exact next gate
Consume Iter603 raw diagnostic. If the three `s` rows are strongly lattice-radius sensitive, derive a new prospective finite-lattice boundary/convergence contract from the continuum Ward identity before any production rerun; the Iter602 FAIL remains historical authority. If the rows are radius-stable, localize the `s`-leg spectator/gauge algebra analytically under the unchanged continuum contract and preserve the result as stronger negative evidence.

Only after a prospectively valid full source-level Ward closure may source-to-Iter582/native-linked mapping and then the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient proceed.

Until then:
- no Source/Born subtraction;
- no source-to-Iter582 mapping;
- no comparator quotient;
- no `ANSATZ-003`;
- no Fisher/resources.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. A nonconvergent negative row is preserved but not promoted into a stable model-level claim. No post-hoc estimator, altered normalization, changed q2 grouping, threshold weakening, ansatz tuning, or unproved internal repartition. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
