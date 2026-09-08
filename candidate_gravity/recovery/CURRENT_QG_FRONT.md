# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **627**.

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
- Iter625: CTP branch-orientation audit finds five positive-energy and one negative-energy internal scalar root.
- Iter626: historical CTP authority proves the native gravitational retarded/in-in sector and linked/amputated gravitational r/a protocol are frozen, but internal MSSC matter-scalar components were not.
- **Iter627: prospective combined matter+gravity Schwinger-Keldysh contract `MSSC001-GRAVITY-SK-MEAS-V1` is frozen and raw-valid. The measured scalar-probe component is `G_phi^{ra}=G_R`, physical metric insertions are `h_r` at `h_a=0`, and r/a matrix multiplication forces every surviving internal scalar propagator in this measured response to be retarded. No root-by-root branch assignment is permitted.**

## Frozen source support and historical projective data

Strict ascending-s root order and Iter615 normalized source-side coefficients in the historical common `K+i0` convention:

1. `D_b^-(0.013028588574858)`: `-0.00024912100468199333`;
2. `D_s^-(0.09)`: `+0.0007390333386357162`;
3. `D_a^-(0.09868572571657197)`: `+0.00019432750619153958`;
4. `D_a^+(1.241314274283428)`: `+0.0012850179378006798`;
5. `D_b^+(1.726971411425142)`: `-0.0007467205092433388`;
6. `D_s^-(2.89)`: `-0.0021373920072305236`.

`D_s^+` has no positive root; this is not amplitude zero. All 13 source families remain retained; `zero_fill=false`.

Iter618 projective ratios are authoritative only for the historical Iter608/615 pole convention:

`[-2.966563737084728, -0.7800526753639322, -5.158207913624242, 2.997420912767025, 8.57973421373656]`.

Because Iter627 prospectively selects the retarded scalar component for the native measurement map, the affected pole coefficients must be recomputed from the same source dynamics. They must not be hand-flipped or inferred by editing the historical values.

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

Under Iter627, for the measured retarded scalar response, the two common external endpoints are `G_R` and are the only scalar propagators amputated. Internal scalar propagators, K3 and all K1^3 chains remain.

The physical split is `g=eta+kappa h_phys`, hence `delta_g=kappa h_phys`. Iter270 connection geometry and Iter590 source geometry both add perturbations directly to `g`; an extra unknown `kappa` power is not part of the remaining bridge.

## Iter627 combined SK measurement authority

Prospective doubled functional:

`Z[J_phi+,J_phi-,J_g+,J_g-] = Integral exp{i S[g+,phi+] - i S[g-,phi-] + i(source+ - source-)}`.

r/a rotation for both matter and gravity:

`X_+=X_r+X_a/2`, `X_-=X_r-X_a/2`.

Physical metric background and insertions:

`h_a=0`, differentiate with respect to `h_r`.

Measured scalar probe:

`G_phi^{ra}=G_R`.

The same-branch unitary action gives exact rotation coefficients `rrr=0`, `arr=rar=rra=1`, `aaa=1/4`. With `G_rr=G_K`, `G_ra=G_R`, `G_ar=G_A`, `G_aa=0`, direct matrix multiplication gives

`(G dK G)_{ra}=G_R dK_R G_R`,

`(G dK G dK G)_{ra}=G_R dK_R G_R dK_R G_R`,

and the corresponding cubic retarded chain. Therefore all surviving internal scalar lines are induced as `G_R` by the observable definition.

Raw validation: Actions run `34284449139`, conclusion `success`, head `e701b1d0aa8a0222e7ec6cfbc6b5baf8263378c0`, artifact `10078890134`, digest `sha256:03a8167e23d946006024971ad02824070b700c94124465bb11982fed87dbe67e`; fail-closed exact comparison PASS.

## Iter582 connection coordinate

`D_s Gamma_e2(q^2)=+(i/2)D_s Tr U2-(i/4)D_s Tr U1^2`:

- `q^2=-1.0`: `+0.0003272233895861266 i`;
- `q^2=-0.34`: `-0.00371666346186323 i`;
- `q^2=-0.14`: `-0.0007997265433511544 i`.

These values were not used to choose the Iter627 SK branch/component contract.

## Repository-level KG start ledger

This is separate from `MODEL_READINESS`. A genuinely new KG may be instantiated only after:

1. **KGSTART-1 — ACTIVE:** with Iter627 measurement map now frozen, recompute the source pole coefficients in the induced retarded scalar component and derive the resulting absolute dimensionless source-to-native normalization without Candidate/comparator values.
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

Readiness change through Iter627: **0 percentage points**. A real measurement-map prerequisite closed, but robust unique residual remains `0/20` and no complete rubric sector closed.

## Exact next admissible work

**Iteration628:** recompute the six supported internal scalar-pole discontinuity coefficients under the prospectively frozen retarded internal-line prescription, preserving Iter613/614 kinematics, endpoint convention and all 13 source families. In the same iteration or an immediately preceding prospective sub-contract, derive the single common source-to-native phase/normalization from `MSSC001-GRAVITY-SK-MEAS-V1` without consulting Iter582 Candidate values. Only after this closes may native `Y/T_cut` projection begin.

## Compute status / ANTI-IDLE

No heavy numerical job is currently required for the contract itself. Iter628 is an algebraic/numerical recomputation and should reuse the existing reproducible MSSC machinery; do not duplicate an already-running Action.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, normalization fit, q2 regrouping, root summation, branch hand-flip, threshold weakening, ansatz tuning or unproved internal repartition. K1^3 remains retained. Repeated/coincident poles are never ordinary simple cuts. Source/Born subtraction remains `NOT_PERFORMED`. No comparator quotient before native binding closes. No `ANSATZ-003`; no Fisher/resources.
