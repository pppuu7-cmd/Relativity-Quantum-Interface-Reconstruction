# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **620**.

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
- Iter617: historical-normalization authority audit PASS with negative answer: existing authority genuinely does not fix `N_native`.
- Iter618: six-root projective source-shape certificate PASS; five independent root-by-root ratios are invariant under any common nonzero real/complex `N_native`.
- Iter619: independent Iter615 representation reproduces the Iter618 projective ratios at floating-point level; diagnostic-only/non-promoting reproducibility PASS.
- **Iter620: normalization-invariant projective conditioning diagnostic PASS/non-promoting; no threshold introduced and `N_native` remains BLOCKED.**

## Frozen native-s support and Iter615 coefficients

Strict ascending-s root order:

1. `D_b^-(0.013028588574858)`: `-0.00024912100468199333`;
2. `D_s^-(0.09)`: `+0.0007390333386357162`;
3. `D_a^-(0.09868572571657197)`: `+0.00019432750619153958`;
4. `D_a^+(1.241314274283428)`: `+0.0012850179378006798`;
5. `D_b^+(1.726971411425142)`: `-0.0007467205092433388`;
6. `D_s^-(2.89)`: `-0.0021373920072305236`.

`D_s^+` has no positive root; this is not amplitude zero. All 13 source families remain retained and `zero_fill=false`.

## Iter616 exact endpoint / q2 binding

Iter588 mode identity across opposite signatures:

- source `s:+1.0` <-> Iter582 `-1.0`;
- source `b:+0.34` <-> Iter582 `-0.34`;
- source `a:+0.14` <-> Iter582 `-0.14`.

Distinct buckets are never summed.

For the full Iter594 source response

`d_abc G=-G Kabc G+sum_6(G Ki G Kjk G)-sum_6(G Ki G Kj G Kk G)`,

external scalar endpoint amputation is exactly

`S_amp^(3)=K0_out(d_abc G)K0_in`

`=-Kabc+sum_6(Ki G Kjk)-sum_6(Ki G Kj G Kk)`.

Only common external scalar propagators are removed. Internal scalar poles, K3 and all K1^3 chains remain. Direct and termwise forms agree on the frozen probes to maximum absolute difference `8.673617379884035e-19`.

## Iter617 exact minimal blocker

Existing authority fixes connection outer `+i` (Iter338), retarded gravitational response `chi2R=-G_R Gamma3 G_R G_R` (Iter147/149), `g=eta+kappa h` source convention (Iter149/218), source-internal relative factors (Iter589/594), q2 identity and scalar endpoint amputation (Iter588/616).

But there is no frozen equation mapping the scalar-endpoint-amputated MSSC probe response to the gravitational retarded/1PI `Gamma3` convention with an absolute phase/coupling normalization. Iter151 explicitly avoided importing an incompatible amputated-vertex normalization; repository history contains no prior Legendre/generating-functional/1PI bridge.

Therefore

`N_native = BLOCKED__NOT_DERIVABLE_FROM_EXISTING_REPOSITORY_AUTHORITY`.

Never set `N_native` to `+i`, `-i`, `1`, fit it from Candidate values, or tune it per root/q2 bucket.

## Iter618–620 projective source-shape authority

The anchor is the pre-coefficient, kinematically selected smallest-s root `D_b^-`. Five independent ratios are:

- `-2.966563737084728`;
- `-0.7800526753639322`;
- `-5.158207913624242`;
- `+2.997420912767025`;
- `+8.57973421373656`.

Raw source sign pattern: `[-,+,+,+,-,-]`.

These ratios are invariant under one common nonzero `N_native`. Direct scale tests under `2.5`, `-3`, `+i`, `2-1.5i` drift by at most `8.881784197001252e-16`.

The independent Iter615 recovery representation reproduces them with maximum absolute ratio difference `5.329070518200751e-15` and maximum relative ratio difference `6.211230307890725e-16`.

Iter620 adds a threshold-free componentwise conditioning diagnostic. Define

`M=|A_aggregate|/(|A_pair|+sum|A_K1cubed|)`, `kappa=1/M`.

Rootwise `kappa` values are `[1.227051600482995, 1.093790319820292, 1.0, 1.272764987610942, 2.45679285736057, 1.279568269456018]`. The minimum cancellation margin is `0.40703472293319004` at `D_b^+`; the absolute projective coefficient dynamic range is `10.998916463857647`.

This diagnostic is scale-invariant and non-promoting. It does not authorize dropping, rescaling, regrouping or summing roots. Any future common-`N_native` bridge that changes root-by-root ratios is implementation/projection corruption, not a physical residual.

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

Readiness change through Iter620: **0 percentage points**. Reproducibility, normalization-invariant source shape and conditioning are stronger, but no robust comparator-subtracted residual or complete readiness sector closed.

## Exact next admissible work

Preserve `N_native` as the minimal native-binding blocker and do not revise Iter606/616 normalization after seeing Candidate values.

Only normalization-invariant diagnostics or an independent non-biasing derivation/audit of the missing source-to-`Gamma3` absolute phase/coupling bridge are allowed. No value-dependent tolerance may be invented.

Full native projection, Source/Born subtraction and the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain forbidden until an independently justified source-to-Gamma normalization authority exists.

## Compute status / ANTI-IDLE

Useful Actions `queued=0`, `in_progress=0` at the Iter620 check. No scientifically useful heavy job is authorized: the remaining gate is algebraic/convention-level and depends on an absent source-to-`Gamma3` absolute normalization authority. A heavy numerical run cannot determine that missing bridge and would manufacture authority. Therefore ANTI-IDLE condition (b) is satisfied: the next model gate is explicitly BLOCKED by a prerequisite and no other independent model-promoting computational gate is currently admissible.

The latest automatic Iter581 exact15 path-trigger from the Iter619 front update completed with `failure`; it is a stale already-closed workflow and creates no new scientific authority.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, normalization fit, q2 regrouping, root summation, threshold weakening, ansatz tuning or unproved internal repartition. K1^3 remains retained. Repeated/coincident poles are never ordinary simple cuts. Source/Born subtraction remains `NOT_PERFORMED`. No comparator quotient before native binding closes. No `ANSATZ-003`; no Fisher/resources.
