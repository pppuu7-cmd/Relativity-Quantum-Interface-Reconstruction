# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **619**.

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
- **Iter619: the independent Iter615 representation reproduces the Iter618 projective ratios at floating-point level; diagnostic-only/non-promoting reproducibility PASS.**

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

## Iter618/619 projective source-shape authority

The anchor is the pre-coefficient, kinematically selected smallest-s root `D_b^-`. Five independent ratios are:

- `-2.966563737084728`;
- `-0.7800526753639322`;
- `-5.158207913624242`;
- `+2.997420912767025`;
- `+8.57973421373656`.

Raw source sign pattern: `[-,+,+,+,-,-]`.

These ratios are invariant under one common nonzero `N_native`. Direct scale tests under `2.5`, `-3`, `+i`, `2-1.5i` drift by at most `8.881784197001252e-16`.

The independent Iter615 recovery representation gives ratios

`[1, -2.966563737084729, -0.7800526753639321, -5.158207913624242, 2.9974209127670246, 8.579734213736554]`.

Against the canonical representation:

- maximum absolute ratio difference: `5.329070518200751e-15`;
- maximum relative ratio difference: `6.211230307890725e-16`.

Iter619 is reproducibility-only and does not promote model readiness.

Future fail-closed rule: any claimed common-`N_native` bridge that changes these root-by-root ratios is implementation/projection corruption, not a physical residual. Distinct roots remain separate.

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

Readiness change through Iter619: **0 percentage points**. Reproducibility and normalization-invariant structure improved, but no robust comparator-subtracted residual or complete readiness sector closed.

## Exact next admissible work

Preserve `N_native` as the minimal native-binding blocker and do not revise Iter606/616 normalization after seeing Candidate values.

Only normalization-invariant diagnostics or independent non-biasing theory/comparator audits are allowed. A future projective conditioning calculation may propagate already-declared parent precision information, but must not invent a value-dependent tolerance.

Full native projection, Source/Born subtraction and the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain forbidden until an independently justified source-to-Gamma normalization authority exists.

## Compute status

No scientifically useful heavy job is authorized. Current gate is algebraic/convention-level; duplicate heavy runs are forbidden.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, normalization fit, q2 regrouping, root summation, threshold weakening, ansatz tuning or unproved internal repartition. K1^3 remains retained. Repeated/coincident poles are never ordinary simple cuts. Source/Born subtraction remains `NOT_PERFORMED`. No comparator quotient before native binding closes. No `ANSATZ-003`; no Fisher/resources.
