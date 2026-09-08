# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **618**.

- Iter424 physical fallback: **5/5 PASS**.
- Iter581 exact15 / complete `Tr U1^2`: raw-valid PASS.
- Iter582 q2-resolved `D_s Gamma_{e=2}`: PASS/non-residual.
- Iter583–594: same-parent MSSC contacts, routing, relative normalization and complete 13-family cubic source object.
- Iter605: full source-level nonlinear Ward consistency PASS.
- Iter606: prospective source-to-native mapping contract PASS/non-residual.
- Iter607: preserved scientific `BLOCKED` result.
- Iter608: universal scalar-pole distribution law PASS.
- Iter609–612: missing native bridge localized to kinematic rank; historical auxiliary constraints absent.
- Iter613: prospective `MSSC001-NATIVE-S-KIN-V1` frozen before roots.
- Iter614: six positive simple-root/Jacobian support points closed.
- Iter615: six finite nonzero normalized source-side internal scalar-pole coefficients; independent implementations agree.
- Iter616: exact q2 bucket identity and scalar endpoint amputation closed; remaining native-binding ambiguity reduced to one common nonzero scalar `N_native`.
- Iter617: historical-normalization authority audit PASS with negative answer: existing authority genuinely does not fix `N_native`.
- **Iter618: six-root projective source-shape certificate PASS; five independent root-by-root ratios are frozen and invariant under any one common nonzero real or complex `N_native`.**

## Frozen native-s source support

MSSC-001 convention `(+---)`, mass `m=0.7`, trajectory `p0(s)=(sqrt(s),0,0,0)` with exact Iter368/588 mode vectors held fixed.

Positive simple roots:

- `D_b^-`: `s=0.013028588574858`;
- `D_s^-`: `s=0.09`;
- `D_a^-`: `s=0.09868572571657197`;
- `D_a^+`: `s=1.241314274283428`;
- `D_b^+`: `s=1.726971411425142`;
- `D_s^-`: `s=2.89`;
- `D_s^+`: no positive root.

Support absence is never amplitude zero. All 13 source families remain retained; `zero_fill=false`.

## Iter615 normalized source-side coefficients

In strict ascending-s order:

1. `D_b^-`: `-0.00024912100468199333`;
2. `D_s^-`: `+0.0007390333386357162`;
3. `D_a^-`: `+0.00019432750619153958`;
4. `D_a^+`: `+0.0012850179378006798`;
5. `D_b^+`: `-0.0007467205092433388`;
6. `D_s^-`: `-0.0021373920072305236`.

No same-action K1/K2–K1^3 cancellation removes any supported pole.

## Iter616 endpoint/bucket binding

Iter588 fixes mode identity across opposite signatures:

- source `s:+1.0` <-> Iter582 `-1.0`;
- source `b:+0.34` <-> Iter582 `-0.34`;
- source `a:+0.14` <-> Iter582 `-0.14`.

Buckets remain distinct and are never summed.

For Iter594

`d_abc G=-G Kabc G + sum_6(G Ki G Kjk G)-sum_6(G Ki G Kj G Kk G)`,

scalar endpoint amputation is exactly

`S_amp^(3)=K0_out(d_abc G)K0_in`

`=-Kabc+sum_6(Ki G Kjk)-sum_6(Ki G Kj G Kk)`.

It removes only the two common external scalar propagators; internal poles, K3 and every K1^3 chain remain. Two frozen probes agree between direct and termwise forms to `8.673617379884035e-19` maximum absolute difference.

## Iter617 historical-normalization result

Existing authority does **not** fix the one common cross-sector scalar `N_native`.

Known factors include Iter338 connection outer `+i`, Iter147/149 retarded relation `chi2R=-G_R Gamma3 G_R G_R`, Iter149/218 `g=eta+kappa h`, Iter218 stripped common gravitational coupling in the displayed MSSC vertex, and Iter589/594 same-action source relative factors. But no frozen equation maps the scalar-endpoint-amputated MSSC probe response to the gravitational retarded/1PI `Gamma3` convention with an absolute phase/coupling normalization. Iter151 explicitly avoided importing an incompatible amputated-vertex normalization; history searches found no Legendre/generating-functional/1PI bridge.

Thus

`N_native = BLOCKED__NOT_DERIVABLE_FROM_EXISTING_REPOSITORY_AUTHORITY`.

Never set it to `+i`, `-i`, `1`, fit it from Candidate values, or tune it by root/q2 bucket.

## Iter618 projective source-shape authority

The root ordering is fixed by pre-existing Iter614 kinematics: strict ascending `s`. The projective anchor is therefore the smallest-s root `D_b^-`, not a coefficient selected by magnitude.

Five independent ratios to that anchor are:

- `D_s^-(0.09) / D_b^-(0.013028588574858) = -2.966563737084728`;
- `D_a^-(0.09868572571657197) / anchor = -0.7800526753639322`;
- `D_a^+(1.241314274283428) / anchor = -5.158207913624242`;
- `D_b^+(1.726971411425142) / anchor = +2.997420912767025`;
- `D_s^-(2.89) / anchor = +8.57973421373656`.

Raw source sign pattern in ascending-s order: `[-,+,+,+,-,-]`.

These five ratios are unchanged under any one common nonzero real or complex multiplication of all six source coefficients. Regression under `2.5`, `-3`, `+i`, and `2-1.5i` gives maximum ratio drift `8.881784197001252e-16`.

Fail-closed future rule: any claimed common-`N_native` bridge that changes one of these root-by-root ratios is projection/implementation corruption, not a physical residual, and blocks promotion before Source/Born subtraction or comparator quotient. Distinct roots are not summed merely because they share a q2 bucket.

## Iter582 connection coordinate

`D_s Gamma_e2(q^2)=+(i/2)D_s Tr U2-(i/4)D_s Tr U1^2`:

- `q^2=-1.0`: `+0.0003272233895861266 i`;
- `q^2=-0.34`: `-0.00371666346186323 i`;
- `q^2=-0.14`: `-0.0007997265433511544 i`.

These values are never used to fit `N_native`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter618: **0 percentage points**. A new normalization-invariant certificate is closed, but no robust comparator-subtracted residual or complete readiness sector is closed.

## Exact next admissible work

Preserve `N_native` as the exact minimal native-binding blocker. Do not revise Iter606/616 normalization after seeing Candidate values.

Continue only normalization-invariant diagnostics or independent non-biasing theory/comparator work. A useful next source-side gate is a **projective perturbation-stability / conditioning audit** of the five Iter618 ratios using only the already-declared numerical precision/error information from their parent authorities; no new thresholds may be invented from the values themselves.

A full native projection, Source/Born subtraction and fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain forbidden until an independently justified source-to-Gamma normalization authority exists.

## Compute status

No scientifically useful heavy job is authorized. Current work is exact/lightweight; duplicate heavy runs are forbidden.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, normalization fit, q2 regrouping, root summation, threshold weakening, ansatz tuning or unproved internal repartition. K1^3 remains retained. Repeated/coincident poles are never ordinary simple cuts. Source/Born subtraction remains `NOT_PERFORMED`. No fixed comparator quotient before native binding closes. No `ANSATZ-003`; no Fisher/resources.
