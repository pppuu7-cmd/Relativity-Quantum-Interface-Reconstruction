# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **595**.
- Frozen Iter424 is **5/5 PASS**; post-Iter580 unresolved physical set is `[]`.
- Iter581 exact15 `Tr U1^2` is raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}` assembly is PASS, non-residual.
- Iter583–584 close the same-parent MSSC-001 quadratic K2 contact and mixed bilinear `K2(h1,h2)`.
- Iter586 proves the Iter582 timelike buckets require off-shell MSSC source completion.
- Iter587 raw-validates symmetric off-shell K1 routing and the inverse-propagator Ward term.
- Iter588 binds source routing to the exact Iter368/Iter582 three-mode singleton/pair fixture with both block orientations.
- Iter589 raw-validates relative K1/K2 normalization from one scalar inverse kernel.
- Iter590 proves cubic source-response completeness requires K3 + six K1/K2 + six K1^3 families.
- Iter591 raw-validates that local MSSC K3 is nonzero but ordinary finite hard-channel `D_s K3=0`; K3 is still retained in the full same-action source Ward tree until full gauge closure is tested.
- Iter592 raw-validates that K1^3 is a nonzero meromorphic scalar-source tree family: it has scalar poles but no ordinary finite branch cut away from poles.
- Iter593 closes the attempted family-by-family source-to-`T_cut` projection negatively: under the frozen Iter183 split-invariant protocol, an individual K1^3 pole-discontinuity assignment is not itself a frozen observable. K1^3 must remain inside the full same-action source-completed response unless an independent same-parent map was frozen beforehand.
- Iter594 explicitly assembles the complete routed same-action cubic source object containing K3 + all six K1/K2 placements + all six ordered K1^3 chains. On both frozen loop probes it is finite, nonzero, and permutation-symmetric within the inherited Iter590 numerical envelope. This is an assembly PASS only, not yet a nonlinear Ward PASS.
- **Iter595 audits the nonlinear Ward target itself and finds that the currently frozen data do not yet define the full cubic diffeomorphism Ward identity. A naive replacement `h -> q⊗xi+xi⊗q` with the other two source legs held fixed is only a linearized gauge-leg contraction; the nonlinear Lie-derivative action on spectator graviton legs and scalar/source endpoints is not yet prospectively frozen in Fourier space. The correct status is operational BLOCKED, not PASS/FAIL.**

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`, q2 buckets kept distinct:
- Candidate `q^2=-1.0`: `+0.0003272233895861266 i`;
- Candidate `q^2=-0.34`: `-0.00371666346186323 i`;
- Candidate `q^2=-0.14`: `-0.0007997265433511544 i`.

No Source/Born subtraction has been performed.

## Source convention / routing authority
Candidate uses `eta=(-+++)` and timelike `s=-q^2`; MSSC-001 uses `eta=(+---)`. Same physical source buckets are `q^2=s={1,0.34,0.14}`. With `m=0.7`, all lie below `4m^2=1.96`, so the matched source must be off-shell/source-completed.

Iter587 freezes `q=(sqrt(s),0,0,0)`, `p=-q/2`, `p'=+q/2`, with `q_mu V^{mu nu}=(m^2-s/4)q^nu`. Iter588 binds this to the exact Iter368 fixture modes `s,a,b`. Iter589 fixes the single MSSC inverse kernel `K[g]=-p'_cov (sqrt(-g) g^-1) p_cov + m^2 sqrt(-g)`; no independent K1/K2 sign/factor is permitted.

## Cubic source-response authority
For `G=K^-1`,

`d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G)`.

Thus a complete same-action cubic source tree contains:
1. local K3 contact;
2. six K1/K2 placements;
3. six ordered K1^3 chains.

Iter594 proves this full routed object can be assembled on the exact fixture and is finite/nonzero/permutation-symmetric on the inherited probes. It remains explicitly NON_WARD.

## Iter595 nonlinear Ward target authority
Machine-readable authority:
`candidate_gravity/results/iteration595_nonlinear_ward_target_authority_audit.json`.

Classification:
`PASS_NONLINEAR_WARD_TARGET_AUTHORITY_AUDIT__FULL_TARGET_NOT_YET_FROZEN__OPERATIONAL_BLOCKED_NON_RESIDUAL`.

The one-graviton anchor remains Iter587:

`q_mu V^{mu nu}=(p'^2-m^2)p^nu-(p^2-m^2)p'^nu`.

But a nonlinear diffeomorphism acts on the perturbation as

`delta_xi h_{mu nu}=partial_mu xi_nu+partial_nu xi_mu + xi^rho partial_rho h_{mu nu}+h_{rho nu} partial_mu xi^rho+h_{mu rho} partial_nu xi^rho+O(h^2)`.

Therefore the full cubic Ward identity additionally requires a prospectively frozen Fourier-space convention for:
- the gauge parameter on the exact Iter588 three-mode fixture;
- the Lie-derivative action on both spectator graviton legs;
- scalar/source endpoint transformation terms;
- the resulting recursive cubic RHS joining K3, six K1/K2 and six K1^3 contributions;
- an exact one-leg reduction back to Iter587.

Until that contract exists, a pure-gauge polarization substitution with fixed spectator legs must not be promoted as the full nonlinear Ward test.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change: **0 percentage points**. Iter595 closes an authority ambiguity and prevents a false Ward PASS/FAIL, but does not close a full readiness sector or create a robust comparator-subtracted residual.

## Exact next gate
Create a separate **pre-result** nonlinear Ward contract that prospectively freezes the full momentum-space diffeomorphism recursion on the exact Iter588 three-mode fixture. It must include spectator-graviton Lie-derivative terms and scalar/source endpoint terms, and its spectator-free limit must reproduce Iter587 exactly.

Only after that contract is frozen may the full Iter594 K3 + six K1/K2 + six K1^3 object be numerically contracted and classified. Only after source-level Ward closure may a full-observable source-to-Iter582/native-linked map be applied and the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient become eligible.

Until that gate closes:
- do not call Iter594 or a naive pure-gauge substitution a nonlinear Ward PASS;
- do not perform Source/Born subtraction;
- do not map an incomplete or un-Ward-closed source response into Iter582/comparator quotient;
- do not create `ANSATZ-003`;
- do not run Fisher/resources.

The fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remains **operational BLOCKED**.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. No post-hoc estimator, altered normalization, changed q2 grouping, premature Source/Born subtraction, threshold weakening, ansatz tuning, or unproved internal repartition. `ANSATZ-003` remains forbidden until a concrete robust comparator-subtracted residual survives the fixed quotient. Fisher/resources remain forbidden until a nonzero algebraic residual exists.
