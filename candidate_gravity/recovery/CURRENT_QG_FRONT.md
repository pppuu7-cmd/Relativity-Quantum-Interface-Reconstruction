# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **617**.

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
- Iter615: all six source-side normalized internal scalar-pole coefficients finite and nonzero; independent implementations agree.
- Iter616: exact q2 bucket identity and scalar endpoint amputation closed; remaining native-binding ambiguity reduced to one common nonzero scalar `N_native`.
- **Iter617: historical-normalization authority audit PASS with a negative answer: existing repository authority genuinely does not fix `N_native`.**

## Frozen native-s source support

MSSC-001 convention `(+---)`, mass `m=0.7`, positive-frequency trajectory

`p0(s)=(sqrt(s),0,0,0)`.

With the exact Iter368/588 mode vectors held fixed:

`D_i^+(s)=m^2-s-q_i^2-2sqrt(s)q_i^0`,

`D_i^-(s)=m^2-s-q_i^2+2sqrt(s)q_i^0`.

Positive roots:

- `D_s^+`: none;
- `D_s^-`: `0.09`, `2.89`;
- `D_a^+`: `1.241314274283428`;
- `D_a^-`: `0.09868572571657197`;
- `D_b^+`: `1.726971411425142`;
- `D_b^-`: `0.013028588574858`.

All supported roots are simple. Support absence is never interpreted as amplitude zero. All 13 source families remain retained; `zero_fill=false`.

## Iter615 normalized source-side pole coefficients

Using Iter608 `Disc[1/(D+i0)]=-2*pi*i delta(D)` and Iter205 `D_s=Disc_s/(2*pi*i)`:

- `D_b^-(0.013028588574858)`: `-0.00024912100468199333`;
- `D_s^-(0.09)`: `+0.0007390333386357162`;
- `D_a^-(0.09868572571657197)`: `+0.00019432750619153958`;
- `D_a^+(1.241314274283428)`: `+0.0012850179378006798`;
- `D_b^+(1.726971411425142)`: `-0.0007467205092433388`;
- `D_s^-(2.89)`: `-0.0021373920072305236`.

No same-action K1/K2–K1^3 cancellation removes any supported scalar-pole contribution.

## Iter616 exact endpoint/bucket binding

Iter588 already froze the same physical modes under `ETA_C=(-+++)` and `ETA_S=-ETA_C`:

- source `s:+1.0` <-> Iter582 `-1.0`;
- source `b:+0.34` <-> Iter582 `-0.34`;
- source `a:+0.14` <-> Iter582 `-0.14`.

Buckets remain distinct and are never summed.

For the complete Iter594 source response

`d_abc G=-G Kabc G + sum_6(G Ki G Kjk G)-sum_6(G Ki G Kj G Kk G)`,

the exact scalar endpoint amputation is

`S_amp^(3)=K0_out(d_abc G)K0_in`

so

`S_amp^(3)=-Kabc+sum_6(Ki G Kjk)-sum_6(Ki G Kj G Kk)`.

Only the two common external scalar propagators are removed. Internal scalar poles, K3 and all K1^3 chains remain. Two frozen probes agree between direct and termwise forms to maximum absolute difference `8.673617379884035e-19`.

## Iter617 historical normalization audit

Question: can the one remaining common scalar `N_native` be recovered from pre-existing authority without using Candidate values?

Answer: **no**.

Known exact factors:

- Iter338: connection one-loop effective-action outer factor `+i`, including `D_s Gamma_det=+i D_s C_det`.
- Iter147/149: retarded gravitational response `chi2R=-G_R Gamma3 G_R G_R`.
- Iter149/218: physical metric/source convention uses `g=eta+kappa h`.
- Iter218: the displayed MSSC one-graviton source vertex explicitly strips the common gravitational coupling.
- Iter589/594: all source-internal relative factors/signs are fixed from one parent scalar action.
- Iter588/616: q2 identity and scalar endpoint amputation are fixed.

Missing authority:

There is **no frozen equation** mapping the scalar-endpoint-amputated MSSC probe response to the gravitational retarded/1PI `Gamma3` convention with one absolute phase/coupling normalization. Iter151 explicitly avoided importing an incompatible amputated-vertex normalization. Commit-history searches found no pre-existing `Legendre`, `generating functional`, or `1PI` authority supplying that bridge.

Therefore

`N_native = BLOCKED__NOT_DERIVABLE_FROM_EXISTING_REPOSITORY_AUTHORITY`.

It is forbidden to set `N_native` to `+i`, `-i`, `1`, fit it to Iter615/Iter582 values, or tune it separately per root/q2 bucket.

## Iter582 connection coordinate

`D_s Gamma_e2(q^2)=+(i/2)D_s Tr U2-(i/4)D_s Tr U1^2`:

- `q^2=-1.0`: `+0.0003272233895861266 i`;
- `q^2=-0.34`: `-0.00371666346186323 i`;
- `q^2=-0.14`: `-0.0007997265433511544 i`.

These numbers are never used to fit `N_native`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter617: **0 percentage points**. The native binding blocker is now precisely localized, but no robust comparator-subtracted residual or complete readiness sector is closed.

## Exact next admissible work

Do **not** revise the Iter606/616 normalization after seeing Candidate values. Preserve `N_native` as the minimal blocker. Continue only work invariant under one common nonzero source normalization, or other independent theory/comparator audits that cannot tune `N_native`.

The highest-value immediate diagnostic is a six-root **projective source-shape certificate**: retain every root separately, construct normalization-invariant sign/ratio/projective data from Iter615, and prospectively freeze invariants that can later test any legitimate native bridge for corruption. No roots may be summed merely because they share a q2 bucket.

A full native projection, Source/Born subtraction and fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient remain forbidden until an independently justified source-to-Gamma normalization authority exists.

## Compute status

No scientifically useful heavy job is authorized. Current work is exact/lightweight; duplicate heavy runs are forbidden.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, normalization fit, q2 regrouping, threshold weakening, ansatz tuning or unproved internal repartition. Distinct roots and q2 buckets are never summed without an explicit observable law. K1^3 remains retained. Repeated/coincident poles are never treated as ordinary simple cuts. Source/Born subtraction remains `NOT_PERFORMED`. No fixed comparator quotient before native binding closes. No `ANSATZ-003`; no Fisher/resources.
