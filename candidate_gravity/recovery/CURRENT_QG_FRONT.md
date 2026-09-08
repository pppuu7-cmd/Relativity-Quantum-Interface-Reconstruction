# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **600**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` assembly is PASS, non-residual.
- Iter583–584 close the same-parent MSSC-001 quadratic K2 contact and mixed bilinear `K2(h1,h2)`.
- Iter586 proves the Iter582 timelike buckets require off-shell MSSC source completion.
- Iter587 raw-validates symmetric off-shell K1 routing and the inverse-propagator Ward term.
- Iter588 binds source routing to the exact Iter368/Iter582 three-mode singleton/pair fixture with both block orientations.
- Iter589 fixes relative K1/K2 normalization from one scalar inverse kernel.
- Iter590 proves cubic source-response completeness requires K3 + six K1/K2 + six K1^3 families.
- Iter591 raw-validates local MSSC K3 as nonzero but ordinary finite hard-channel `D_s K3=0`; K3 remains in the complete source Ward tree.
- Iter592 raw-validates K1^3 as nonzero meromorphic scalar-source tree family with scalar poles but no ordinary finite branch cut away from poles.
- Iter593 closes family-by-family source-to-`T_cut` projection negatively: individual K1^3 pole assignments are not themselves frozen observables under the Iter183 split-invariant protocol.
- Iter594 explicitly assembles the complete routed same-action cubic source object containing K3 + all six K1/K2 placements + all six ordered K1^3 chains; it is finite/nonzero/permutation-symmetric on inherited probes but explicitly NON_WARD.
- Iter595 finds the full cubic nonlinear diffeomorphism Ward target underdetermined until spectator-graviton and scalar/source endpoint transformations are prospectively frozen.
- Iter596 prospectively freezes and raw-validates the full nonlinear Ward contract and analytic one-leg reduction target.
- Iter597 produced negative numbers on arbitrary scalar `PROBES`; Iter598 raw-validates that this violates the frozen Iter596 per-gauge symmetric scalar route, so Iter597 remains diagnostic only.
- Iter599 repairs that routing exactly and is raw-consumed, but its implemented **matrix covariance one-leg anchor fails the mandatory Iter587 reduction by O(10^-1–1)** while the frozen tolerance is `2e-11`.
- **Iter600 therefore fail-closes the Iter599 cubic Ward rows as NONAUTHORITATIVE diagnostics and localizes the remaining blocker to the scalar endpoint/covariance matrix realization.**

## Iter599/600 raw authority
Corrected Iter599 route:
`p=-q_g/2`, `p'=+q_g/2` separately for every `g in (s,a,b)`; no arbitrary `PROBES` in anchor or Ward rows.

Canonical corrected run:
- run `34236758448`, job `102096346284`;
- head `491f55d9f88b2d40f7e737108f2dfc24bfe3f6e4`;
- artifact `10060216987`, digest `sha256:577bb2d4a8f56f24f86aecdfb4abc6e9616d0a9a28bfb3bae40330505b0eed3d`;
- fail-closed consumer run `34237037608`;
- committed raw result SHA-256 `9bafe4cf47c35e8a5e2537d94605e5f0e54345bc28ef03af16c9b7e3675ac855`.

The corrected cubic diagnostic has `max |W| = 0.13675071724815208` and `max last-step = 0.006078581018494812`, but these numbers are **not Candidate-Gravity consistency FAIL authority** because the mandatory one-leg anchor already fails. Examples at frozen symmetric routing:
- `s/xi0 = 2.083333333333334`;
- `a/xi0 = 0.4395604395604424`, `a/xi1=a/xi2=0.1098901098901106`;
- `b/xi0 = 0.7407407407407341`, `b/xi1=b/xi2=0.1234567901234587`.

Frozen anchor tolerance: `2e-11`.

Iter596 explicitly states that failure of spectator-free reduction to Iter587 invalidates numerical nonlinear Ward evaluation. Therefore Iter600 classification is:
`BLOCKED_ITER599_FULL_WARD_NUMBERS_NONAUTHORITATIVE_BECAUSE_MANDATORY_ITER587_ANCHOR_FAILS__ENDPOINT_COVARIANCE_REALIZATION_DIAGNOSIS_REQUIRED`.

## Frozen nonlinear Ward convention
Use `f(x)=int exp(-ik.x) f(k)` and stripped generator `Delta_xi=i delta_xi`.

For the full cubic source Ward gate, all five classes remain mandatory:
1. gauge-leg linear contraction;
2. spectator-u Lie derivative;
3. spectator-v Lie derivative;
4. left scalar/source endpoint transformation;
5. right scalar/source endpoint transformation.

The exact Iter588 three-mode fixture is inherited. No new momentum split, gauge normalization, result-dependent polarization or family deletion is permitted. The spectator-free limit must reproduce Iter587 exactly. The scalar route attached to gauge leg `g` remains exactly `p=-q_g/2`, `p'=+q_g/2`.

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

Readiness change from Iter598: **0 percentage points**. Iter599/600 localize a real endpoint/covariance realization blocker but do not close a model-level readiness sector.

## Exact next gate
Derive and prospectively freeze the scalar endpoint/covariance **matrix realization** directly from the already frozen Fourier rule
`Delta_xi phi(k)=int xi(l)(k-l)_rho phi(k-l)`, including explicit row/column momentum orientation and the signs/orientations of both endpoint actions. Before any cubic Ward rerun, require this matrix identity to reproduce the Iter587 one-graviton Ward relation on all three exact symmetric routes:

`q_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu`, with `p=-q/2`, `p'=+q/2`.

Only after that anchor closes may the full K3 + six K1/K2 + six K1^3 nonlinear Ward gate be rerun. Only after full source-level Ward closure may source-to-Iter582/native-linked mapping and then the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient proceed.

Until then:
- do not perform Source/Born subtraction;
- do not map the blocked Ward object into Iter582/comparator quotient;
- do not create `ANSATZ-003`;
- do not run Fisher/resources.

The fixed comparator quotient remains **operational BLOCKED**.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. A failed mandatory reduction anchor blocks downstream Ward interpretation. No post-hoc estimator, altered normalization, changed q2 grouping, premature Source/Born subtraction, threshold weakening, ansatz tuning, or unproved internal repartition. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
