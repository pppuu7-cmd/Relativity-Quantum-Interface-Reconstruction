# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **624**.

- Iter424 physical fallback: **5/5 PASS**.
- Iter581 exact15 / complete `Tr U1^2`: raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}`: PASS/non-residual.
- Iter583–594: same-parent MSSC contacts, routing, relative normalization and complete 13-family cubic source object.
- Iter605: full source-level nonlinear Ward consistency PASS.
- Iter606: prospective source-to-native mapping contract PASS/non-residual.
- Iter607: preserved scientific `BLOCKED` result.
- Iter608: universal scalar-pole distribution law PASS.
- Iter609–612: native bridge kinematic-rank obstruction localized; historical auxiliary constraints absent.
- Iter613: prospective `MSSC001-NATIVE-S-KIN-V1` frozen before roots.
- Iter614: six positive simple-root/Jacobian support points closed.
- Iter615: six finite nonzero normalized source-side internal scalar-pole coefficients; independent implementations agree.
- Iter616: exact q2 bucket identity and scalar endpoint amputation closed; native-binding ambiguity reduced to one common nonzero scalar `N_native`.
- Iter617: historical-normalization authority audit PASS with negative answer: existing authority does not fix `N_native`.
- Iter618–620: six-root projective source-shape / reproducibility / conditioning diagnostics PASS, normalization-invariant and non-promoting.
- Iter621: authority graph/rank audit proves exactly one relative complex normalization DOF remains.
- **Iter622: both computational sectors are derivatives with respect to the same direct metric perturbation `delta_g=kappa h_phys`; the explicit kappa power is stripped on both sides, so `N_native` is not an unknown power of Newton's constant.**
- **Iter623: repository-level KG-start ledger frozen; six final dependency gates remain before a genuinely new KG ansatz may be created.**
- **Iter624: source-vs-native functional-object audit proves that a generic Legendre-transform sign or Iter338 `+i` cannot by itself fix `N_native`; a concrete combined matter+gravity measurement-level CTP bridge is required.**

## Frozen source support and projective authority

Strict ascending-s root order and normalized source-side coefficients:

1. `D_b^-(0.013028588574858)`: `-0.00024912100468199333`;
2. `D_s^-(0.09)`: `+0.0007390333386357162`;
3. `D_a^-(0.09868572571657197)`: `+0.00019432750619153958`;
4. `D_a^+(1.241314274283428)`: `+0.0012850179378006798`;
5. `D_b^+(1.726971411425142)`: `-0.0007467205092433388`;
6. `D_s^-(2.89)`: `-0.0021373920072305236`.

`D_s^+` has no positive root; this is not amplitude zero. All 13 source families remain retained; `zero_fill=false`.

Iter618 projective ratios to the kinematically selected smallest-s anchor are:

`[-2.966563737084728, -0.7800526753639322, -5.158207913624242, 2.997420912767025, 8.57973421373656]`.

Any legitimate one-common-`N_native` bridge must preserve these root-by-root ratios exactly up to declared arithmetic precision. Distinct roots are never summed merely because they share a q2 bucket.

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

The declared physical split is `g=eta+kappa h_phys`, hence `delta_g=kappa h_phys`. Iter270 connection geometry and Iter590 source geometry both introduce perturbation amplitudes directly into `g`, so stored coefficients on both sides are derivatives with respect to the same `delta_g`; an extra unknown kappa power is not part of `N_native`.

## Remaining native normalization blocker after Iter624

Native authority is a gravitational retarded/1PI object, schematically

`chi2R = - G_R Gamma3 G_R G_R`.

Source authority is a third background-metric derivative of the MSSC scalar propagator `G_phi=K_phi[g]^-1`, followed by scalar endpoint amputation.

These are distinct functional objects. Therefore no generic `W <-> Gamma` Legendre identity, Iter338 effective-action `+i`, or the retarded minus sign alone may be used to set the missing normalization.

The remaining bridge is:

`N_native = one common dimensionless nonzero complex measurement/convention normalization`

that must be derived from a **combined matter+gravity CTP/in-in measurement functional** specifying:

1. the measured connected scalar-probe observable;
2. the gravitational propagator/vertex/contact contraction entering that observable;
3. exact amputation/projection onto the native Iter582 coordinate;
4. all remaining i/sign/factorial conventions;
5. preservation of the Iter618/619 projective ratios.

Never set `N_native` to `1`, `+i`, or `-i` by convention and never fit it from Iter582/Iter615 values.

## Iter582 connection coordinate

`D_s Gamma_e2(q^2)=+(i/2)D_s Tr U2-(i/4)D_s Tr U1^2`:

- `q^2=-1.0`: `+0.0003272233895861266 i`;
- `q^2=-0.34`: `-0.00371666346186323 i`;
- `q^2=-0.14`: `-0.0007997265433511544 i`.

These values are never used to fit `N_native`.

## Repository-level KG start ledger — Iter623

This is separate from `MODEL_READINESS`. A genuinely new KG may be instantiated only after the following chain closes:

1. **KGSTART-1 — ACTIVE BLOCKER:** derive the dimensionless source-to-`Gamma3`/retarded-effective-action measurement bridge and unique common `N_native` prospectively.
2. **KGSTART-2:** execute full native `Y/T_cut` projection with all roots/families retained, then freeze and perform matched Source/Born subtraction.
3. **KGSTART-3:** execute the fixed applicable C0–C6 comparator quotient in the same observable/nuisance convention.
4. **KGSTART-4:** obtain a robust nonzero comparator-subtracted algebraic residual.
5. **KGSTART-5:** challenge that residual against known gravity / quantum-gravity model realizations under the same frozen RQIR funnel, without tuning the funnel to benchmark outcomes.
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

Readiness change through Iter624: **0 percentage points**. This is correct: the repository methodology has advanced, but no Candidate model residual/rubric sector has closed.

## Exact next admissible work

Prospectively freeze the combined matter+gravity CTP measurement-level bridge. The lowest-order calibration must use already-authoritative common-field/source information (including the `delta_g` convention and same-parent scalar source vertex) and must be independent of Iter582/Iter615 numerical Candidate values. Only after this bridge is derived may full native projection be attempted.

## Compute status / ANTI-IDLE

No scientifically useful heavy numerical job is currently authorized. The active blocker is algebraic/functional-definition level; heavy computation cannot determine it and would manufacture authority.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, normalization fit, q2 regrouping, root summation, threshold weakening, ansatz tuning or unproved internal repartition. K1^3 remains retained. Repeated/coincident poles are never ordinary simple cuts. Source/Born subtraction remains `NOT_PERFORMED`. No comparator quotient before native binding closes. No `ANSATZ-003`; no Fisher/resources.
