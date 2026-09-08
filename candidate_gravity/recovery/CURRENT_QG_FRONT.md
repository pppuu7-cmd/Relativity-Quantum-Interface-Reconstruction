# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **626**.

- Iter424 physical fallback: **5/5 PASS**.
- Iter581 exact15 / complete `Tr U1^2`: raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}`: PASS/non-residual.
- Iter583–594: same-parent MSSC contacts, routing, relative normalization and complete 13-family cubic source object.
- Iter605: full source-level nonlinear Ward consistency PASS.
- Iter606: prospective source-to-native mapping contract PASS/non-residual.
- Iter607: preserved scientific `BLOCKED` result.
- Iter608: universal algebraic/Feynman-like scalar-pole distribution law PASS in its frozen `K+i0` scope.
- Iter609–612: native bridge kinematic-rank obstruction localized; historical auxiliary constraints absent.
- Iter613: prospective `MSSC001-NATIVE-S-KIN-V1` frozen before roots.
- Iter614: six positive simple-root/Jacobian support points closed.
- Iter615: six finite nonzero normalized source-side internal scalar-pole coefficients; independent implementations agree.
- Iter616: exact q2 bucket identity and scalar endpoint amputation closed.
- Iter617–621: historical/graph audits reduce the normalization problem, within the existing convention graph, to one relative complex scale `N_native`.
- Iter622: source and connection numerical branches use the same direct `delta_g=kappa h_phys`; unknown powers of `kappa` are eliminated from the bridge.
- Iter623: KG-start ledger frozen; six final dependency gates precede any genuinely new KG ansatz.
- Iter624: MSSC source response and native gravitational `Gamma3` are different functional objects; a generic Legendre sign or Iter338 `+i` alone cannot bridge them.
- Iter625: CTP branch-orientation audit finds five positive-energy and one negative-energy internal scalar root. Therefore a one-common-`N_native` retarded binding is conditional on the actual CTP line/component assignment; a naive all-retarded conversion would generate a root-dependent sign.
- **Iter626: historical CTP authority audit proves that the repository freezes the native gravitational retarded/in-in sector and linked/amputated gravitational r/a protocol, but does not freeze the `+/-` or r/a component of the internal MSSC matter-scalar lines. The bridge is therefore operationally BLOCKED until a prospective combined matter+gravity SK generating-functional contract is frozen.**

## Frozen source support and projective data

Strict ascending-s root order and Iter615 normalized source-side coefficients:

1. `D_b^-(0.013028588574858)`: `-0.00024912100468199333`;
2. `D_s^-(0.09)`: `+0.0007390333386357162`;
3. `D_a^-(0.09868572571657197)`: `+0.00019432750619153958`;
4. `D_a^+(1.241314274283428)`: `+0.0012850179378006798`;
5. `D_b^+(1.726971411425142)`: `-0.0007467205092433388`;
6. `D_s^-(2.89)`: `-0.0021373920072305236`.

`D_s^+` has no positive root; this is not amplitude zero. All 13 source families remain retained; `zero_fill=false`.

Iter618 projective ratios to the kinematically selected smallest-s anchor are:

`[-2.966563737084728, -0.7800526753639322, -5.158207913624242, 2.997420912767025, 8.57973421373656]`.

These are authoritative for the frozen Iter608/615 pole convention. Any later common multiplicative bridge in the same source component must preserve them; if the CTP bridge selects a different scalar component/prescription, the affected source coefficients must be recomputed rather than hand-flipped.

## Exact q2 / endpoint / field-variable binding

Iter588 mode identity across opposite signatures:

- source `s:+1.0` <-> Iter582 `-1.0`;
- source `b:+0.34` <-> Iter582 `-0.34`;
- source `a:+0.14` <-> Iter582 `-0.14`.

For the complete Iter594 source response

`d_abc G=-G Kabc G+sum_6(G Ki G Kjk G)-sum_6(G Ki G Kj G Kk G)`,

scalar endpoint amputation is

`S_amp^(3)=K0_out(d_abc G)K0_in`

`=-Kabc+sum_6(Ki G Kjk)-sum_6(Ki G Kj G Kk)`.

Only the two common external scalar propagators are removed; internal scalar poles, K3 and all K1^3 chains remain.

The physical split is `g=eta+kappa h_phys`, hence `delta_g=kappa h_phys`. Iter270 connection geometry and Iter590 source geometry both add perturbations directly to `g`, so stored coefficients are derivatives with respect to the same `delta_g`; an extra unknown `kappa` power is not part of the remaining bridge.

## Iter624–626 measurement/CTP blocker

Native authority is a gravitational retarded/1PI object, schematically

`chi2R = - G_R Gamma3 G_R G_R`.

Source authority is a third background-metric derivative of `G_phi=K_phi[g]^-1`, followed by scalar endpoint amputation. These are distinct functional objects, so no generic `W <-> Gamma` identity equates them.

Iter625 evaluates the internal scalar energy orientation at every supported root and finds five positive-energy roots and one negative-energy root, `D_s^-(0.09)` with `r0=-0.7`. Iter608/615 used one common algebraic/Feynman-like `K+i0` rule, while a scalar retarded prescription is energy-oriented.

Iter626 audits the older CTP authority. Iter149 freezes a Minkowski interacting-vacuum retarded/in-in gravitational probe sector; Iter171 freezes linked/amputated CTP comparison and gravitational r/a normalization; Iter172 uses the associated gravitational vertex coordinates. **No authoritative file in that chain specifies the doubled scalar-probe source branches, the `+/-` assignment, or the r/a component of the internal MSSC matter-scalar lines.** Therefore gravitational retardedness alone cannot choose the scalar internal-line prescription.

This does not invalidate Iter608/615 and does not authorize flipping `D_s^-(0.09)` by hand. A prospective combined matter+gravity Schwinger-Keldysh generating-functional contract is required before native projection.

## Iter582 connection coordinate

`D_s Gamma_e2(q^2)=+(i/2)D_s Tr U2-(i/4)D_s Tr U1^2`:

- `q^2=-1.0`: `+0.0003272233895861266 i`;
- `q^2=-0.34`: `-0.00371666346186323 i`;
- `q^2=-0.14`: `-0.0007997265433511544 i`.

These values are never used to choose the source/native bridge.

## Repository-level KG start ledger

This is separate from `MODEL_READINESS`. A genuinely new KG may be instantiated only after:

1. **KGSTART-1 — ACTIVE:** freeze the combined matter+gravity CTP measurement map, including scalar-line component/branch assignment, and derive the resulting absolute dimensionless source-to-native normalization without Candidate/comparator values.
2. **KGSTART-2:** execute full native `Y/T_cut` projection with all roots/families retained, then freeze and perform matched Source/Born subtraction.
3. **KGSTART-3:** execute the fixed applicable C0–C6 comparator quotient in the same observable/nuisance convention.
4. **KGSTART-4:** obtain a robust nonzero comparator-subtracted algebraic residual.
5. **KGSTART-5:** challenge that residual against known gravity / quantum-gravity model realizations under the same frozen RQIR funnel, without tuning the funnel to outcomes.
6. **KGSTART-6:** issue one decision: `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED`.

Only `NEW_REQUIRED` authorizes creation of `ANSATZ-003` as a genuinely new Candidate Gravity model.

## Stable model-readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter626: **0 percentage points**. Historical CTP authority is now sharply scoped, but no Candidate residual/model-rubric sector closed.

## Exact next admissible work

**Iteration627:** prospectively freeze a combined matter+gravity Schwinger-Keldysh generating-functional contract `Z[J_phi^+,J_phi^-,J_g^+,J_g^-]` for the measured scalar-probe observable. It must specify source insertion branches, r/a rotation, endpoint amputation, and the induced component of every retained internal scalar line, and must reduce exactly to the Iter149/171 gravitational CTP conventions in their overlap. No Iter582/Iter615 projected numerical values may be used to choose the branch or normalization.

## Compute status / ANTI-IDLE

No heavy numerical job is currently authorized. The active gate is analytic/CTP-definition level; heavy computation cannot resolve an unspecified contour component.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, normalization fit, q2 regrouping, root summation, branch hand-flip, threshold weakening, ansatz tuning or unproved internal repartition. K1^3 remains retained. Repeated/coincident poles are never ordinary simple cuts. Source/Born subtraction remains `NOT_PERFORMED`. No comparator quotient before native binding closes. No `ANSATZ-003`; no Fisher/resources.
