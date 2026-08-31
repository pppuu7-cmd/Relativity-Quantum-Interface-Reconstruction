# Candidate Gravity — Iteration 149: source-completed finite off-shell C5 protocol

**Date:** 2026-08-31  
**Status:** protocol/source-completion gate PASS; physical `V_C5^(chi2R)` remains BLOCKED at the explicit cubic-vertex implementation.

## Objective

Iteration 148 showed that an on-shell/EOM-reduced gravitational EFT basis cannot be re-used as a basis-independent off-shell response basis without transforming the physical source/observable map. This iteration removes that ambiguity before any rank/SVD claim.

## Frozen operational convention

We choose the conservative option: **undo the on-shell EOM/field-redefinition reduction off shell** rather than attempting to reconstruct all induced contact operators in the reduced coordinates.

Frozen tuple:

- spacetime: D=4 Minkowski, signature `(-,+,+,+)`;
- metric variable: `g_mn = eta_mn + kappa h_mn`;
- physical matter/source definition: a covariant matter action `S_m[g,Psi]` with
  `T_mn = -2/sqrt(-g) delta S_m/delta g^mn`;
- probes are conserved external stress-tensor perturbations, not arbitrary coordinate sources;
- CTP state/prescription: interacting Minkowski vacuum with the retarded/in-in convention frozen in Iteration 147;
- local EFT order: the same low-energy parity-even tree sector through mass dimension 12 used in Iteration 146, but **represented off shell in a complete unreduced covariant basis**, including EOM-redundant/Ricci-type directions required for source-completed response;
- loop/nonanalytic columns remain separate and BLOCKED until derived in this same CTP convention.

This convention means that the ten EOM-reduced Wilson coordinates of Iteration 146 remain an on-shell amplitude chart only. They are not silently recycled as the off-shell response chart.

## Finite off-shell kinematics

Six deterministic triplets `(p,q,r)` are frozen with `p=q+r`. Every leg is spacelike and separated from the massless pole. In cutoff units the invariant ranges are

- `p^2`: 0.4239 ... 0.7473;
- `q^2`: 0.2882 ... 0.5076;
- `r^2`: 0.2278 ... 0.3313.

Exact vectors and invariants are in `analysis/c5_source_completed_protocol_iteration149.py` and `results/c5_source_completed_protocol_iteration149.json`.

The finite measurement window is Gaussian,

`W(k)=exp[-1/2 ((tau k0)^2 + (L |k|)^2)]`,

with `tau=0.8`, `L=0.6`. Across the frozen legs `W` lies in `[0.8381451361499129, 0.9567587587766662]`; no leg is removed by an implicit zero-weight limit.

## Conserved spin-2 probe map

For each non-null momentum define

`theta_mn(k)=eta_mn-k_m k_n/k^2`,

and the D=4 transverse-traceless spin-2 projector

`P2_mn,rs = 1/2(theta_mr theta_ns + theta_ms theta_nr) - 1/3 theta_mn theta_rs`.

The reproducible regression checks every `p,q,r` leg and obtains

- max `|k^m P2_mn,rs| = 1.2533377113932431e-16`;
- max metric trace = `2.636779683484747e-16`;
- max projector idempotence error = `3.3306690738754696e-16`.

Thus the probe layer itself has no numerical longitudinal/gauge contamination at the reported precision.

## Frozen scalar `chi2R` extraction rule

The nonlinear response remains the Iteration-147 causal object

`chi2R_A;BC = - G_R(p) Gamma3 G_R(q) G_R(r)`

with all tensor indices retained before projection.

For each frozen triplet, the scalar observables are defined only after applying the conserved spin-2 projectors and the declared Gaussian windows on all three legs. Two independent projected channels are to be formed from two fixed projected seed tensors per leg; parity-even and parity-odd labels refer to the seed construction, not to an assumed value of the response. A zero odd channel may be claimed only after the explicit parity-even C5 vertex is evaluated in this protocol.

No unprojected coordinate Green function is admissible as `chi2R_even/odd`.

## What is now closed

The Iteration-148 `BLOCKED_SOURCE_COMPLETION` is resolved at the protocol level:

1. physical metric variable fixed;
2. source is a conserved covariant stress tensor;
3. EOM reduction is explicitly undone off shell;
4. CTP state and perturbative regime fixed;
5. finite non-pole kinematics fixed;
6. smearing/window normalization fixed;
7. conserved spin-2 projector passes Ward/gauge-null regression.

## What is not closed

The first physical numerical `V_C5^(chi2R)` is **not** yet computed.

Reason: the repository does not yet contain the complete Einstein-Hilbert plus unreduced dimension-12 local gravitational cubic vertex in the above field/source convention. Importing the Iteration-146 on-shell amplitude derivatives would violate NG-FUNNEL-006/007/008.

Classification:

`BLOCKED_VERTEX_IMPLEMENTATION`, not zero tangent, not rank deficiency, and not a C5 consistency FAIL.

The local response rank must remain `NOT_COMPUTED` until the vertex is generated/validated and contracted with the frozen projectors.

## New retained rule

### NG-FUNNEL-009 — PROJECTOR_PASS_IS_NOT_VERTEX_CERTIFICATE

A conserved finite off-shell probe protocol can close gauge/source ambiguity without certifying the comparator tangent. Ward-safe projectors do not determine the nonlinear gravitational vertex. Therefore a projector-level PASS may not be promoted to a C5 `chi2R` rank/SVD PASS.

## Literature relevance

The 2026 off-shell equivalence analysis of Kuntz & Liberati stresses that off-shell equivalence must be formulated operationally in terms of observables/probes rather than coordinate Green functions. This directly supports the source-completed convention used here. The Schwinger-Keldysh/in-in literature likewise treats retarded response as a real-time observable requiring its own source/state prescription, consistent with the Iteration-147 factorization.

## Authorities

- `analysis/c5_source_completed_protocol_iteration149.py`;
- `results/c5_source_completed_protocol_iteration149.json`.

## Next scientific gate — Iteration 150

Implement and independently validate the **unreduced EH + local-EFT cubic vertex** in the frozen metric/source convention, beginning with EH plus the lowest nontrivial curvature-cubic directions. Contract it on the six frozen triplets with the conserved projectors/windows; verify longitudinal replacement null tests and field-coordinate/source-completion invariance; then compute the first scoped `V_C5^(chi2R)` rank/SVD. Higher-dimension and loop/nonanalytic columns may remain explicitly BLOCKED, but they may not be set to zero.

No Fisher/resources and no `ANSATZ-003` before a nonzero algebraic residual survives the concrete comparator quotient.
