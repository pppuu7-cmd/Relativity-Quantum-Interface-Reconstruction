# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **615**.
- Frozen Iter424 is **5/5 PASS**; Iter581 exact15 raw-valid PASS; Iter582 q2-resolved `D_s Gamma_{e=2}` assembly PASS/non-residual.
- Iter583–594 establish same-parent MSSC contacts, exact routing/normalization and the complete 13-family cubic source object; Iter605 independently raw-closes full source-level nonlinear Ward consistency.
- Iter606 raw-closes the prospective source-to-Iter582/native-linked mapping contract; Iter607 remains a preserved BLOCKED result because the explicit distributional projector was absent; Iter608 closes the universal scalar-pole distribution kernel only.
- Iter609–611 localize the missing native bridge to a minimal kinematic-rank obstruction: full source poles require three independent scalar data `(u,a_s,a_a)` whereas historical native `s` supplied only one coordinate.
- Iter612 proves that the two required auxiliary same-parent hard-channel constraints are absent from existing authority; therefore a new prospective completion, not a retroactive identification, is required.
- Iter613 prospectively freezes `MSSC001-NATIVE-S-KIN-V1` before any pole root is evaluated.
- Iter614 closes the positive-`s` simple-root support/Jacobian audit under that frozen trajectory.
- **Iter615 is authoritative source-side internal scalar-pole coefficient PASS/non-residual.** Two race-created independent implementations agree on all six aggregate normalized source-side cut coefficients to floating-point precision, so the duplicate representation is a cross-check rather than an authority conflict.

## Iter613 prospective kinematic completion
In the MSSC-001 / Iter594 source convention `(+---)`, freeze for `s>0`

`p0(s)=(sqrt(s),0,0,0)`

on the positive-frequency branch. Hold fixed under `D_s` the exact Iter368/588 mode vectors and polarizations, MSSC-001 mass `m=0.7`, all routing/sign/normalization and i0 conventions, and the rest-frame axis.

Thus

`u(s)=s`,

`a_i(s)=sqrt(s) q_i^0`,

and exact momentum closure implies `a_s+a_a+a_b=0`.

Generic retained routed scalar denominators are

`D_i^+(s)=m^2-s-q_i^2-2sqrt(s)q_i^0`,

`D_i^-(s)=m^2-s-q_i^2+2sqrt(s)q_i^0`.

Their derivatives were frozen before roots were inspected:

`partial_s D_i^+=-1-q_i^0/sqrt(s)`,

`partial_s D_i^-=-1+q_i^0/sqrt(s)`.

Iteration167 is only a pre-Candidate design precedent for positive-timelike rest-frame `s=omega^2`; it is a distinct linear `chi1R` observable and is not retroactively identified with the nonlinear bridge.

## Iter614 scalar-pole support / Jacobian authority
Under the frozen trajectory and the exact source-sector `(+---)` mode invariants

- `q_s^2=+1`, `q_a^2=+0.14`, `q_b^2=+0.34`,

which must not be conflated with the separate Iter582 connection-sector negative q2 labels, the positive-`s` support is:

- `D_s^+`: **no positive root**;
- `D_s^-`: `s=0.09`, `2.89`;
- `D_a^+`: `s=1.241314274283428`;
- `D_a^-`: `s=0.09868572571657197`;
- `D_b^+`: `s=1.726971411425142`;
- `D_b^-`: `s=0.013028588574858`.

All six supported root points are distinct and simple. Absolute Jacobians `|partial_s D|` are respectively `2.333333333333333`, `0.4117647058823529`, `0.6409796081665314`, `2.273306106119183`, `0.54342862858286`, and `6.25657137141714` in the order listed above.

Therefore Iter608 pulls back in ordinary simple-root form at every supported routed internal point:

`delta(D_A(s)) = sum_r delta(s-s_r)/|partial_s D_A(s_r)|`.

`D_s^+` support absence is not an amplitude-zero statement. All 13 source families remain retained; `zero_fill=false`. K3 remains local in this routed-internal scalar-pole classification.

## Iter615 source-side internal scalar-pole coefficient authority
For a supported routed internal denominator write the singular source contribution as

`C_A(s)/(D_A(s)+i0)`.

Using Iter608

`Disc[1/(D+i0)] = -2*pi*i delta(D)`

and Iter205 `D_s=Disc_s/(2*pi*i)`, the source-side normalized simple-pole coefficient is

`-C_A(s_r)/|partial_s D_A(s_r)|`.

`C_A` is evaluated from the unchanged Iter594/605 same-action source identity as the one matching K1/K2 placement plus the two matching ordered K1^3 chains with the already frozen overall K1^3 minus sign. No matching K1^3 chain has a coincident second routed internal denominator at any of the six roots.

Canonical aggregate normalized source-side coefficients:

- `D_b^-(0.013028588574858)`: `-0.00024912100468199333`;
- `D_s^-(0.09)`: `+0.0007390333386357162`;
- `D_a^-(0.09868572571657197)`: `+0.00019432750619153958`;
- `D_a^+(1.241314274283428)`: `+0.0012850179378006798`;
- `D_b^+(1.726971411425142)`: `-0.0007467205092433388`;
- `D_s^-(2.89)`: `-0.0021373920072305236`.

All six are finite and nonzero. Thus none of the supported routed internal scalar-pole contributions disappears through same-action K1/K2–K1^3 cancellation.

Canonical Iter615 classification:

`PASS_ITER615_FROZEN_NATIVE_S_INTERNAL_SCALAR_POLE_SOURCE_COEFFICIENT_AUDIT__NON_NORMALIZED_NON_RESIDUAL`.

A second race-created implementation independently evaluated the finite pre-Jacobian `C_A` representation and reproduces the same six normalized coefficients within floating-point rounding; this is retained as a numerical/algebraic cross-check, not promoted as a separate scientific iteration.

Scope remains routed **internal** scalar poles. Common external endpoint factors of the unamputated source Green-function response are not silently reclassified; their amputation/endpoint treatment must be stated explicitly in the next native binding. K3 remains retained in the full 13-family source object but has no routed internal scalar-pole distribution in this sector.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`:
- `q^2=-1.0`: `+0.0003272233895861266 i`
- `q^2=-0.34`: `-0.00371666346186323 i`
- `q^2=-0.14`: `-0.0007997265433511544 i`

Source-sector q squares under `(+---)` are `(+1,+0.14,+0.34)` and are never merged with these separate Iter582 connection-sector labels.

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter615: **0 percentage points**. The source-side internal pole support, Jacobians and nonzero normalized distribution coefficients are explicit, but native matched-observable normalization and robust unique residual are still absent.

## Exact next gate — prospective native Y/T_cut binding
Before inspecting any projected Candidate value, freeze an identity-preserving source-side distribution -> Iter205/Iter582 native `Y=(K2,S_soft2,full)/T_cut` binding that specifies:

1. relative sign and normalization between the six source-side delta weights and the frozen Iter582 operator coordinate;
2. exact source-q / Iter582-q2 bucket correspondence without merging their opposite-sign conventions;
3. explicit external-endpoint/amputation convention for the common unamputated source Green-function factors;
4. treatment of local K3/contact origin without zero-filling or pretending that absence of an internal scalar pole is amplitude zero.

Only after that contract is frozen may the six source-side weights be projected into the native observable. Source/Born subtraction remains `NOT_PERFORMED` until the matched observable and pole/cut origin are bound. No fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient before that map closes. No `ANSATZ-003`; no Fisher/resources.

## Compute status
No scientifically useful heavy numerical job is required for Iter615; the gate is algebraic/lightweight and two independent implementations already agree on the aggregate coefficients. Duplicate heavy authority runs remain forbidden.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, altered normalization, changed q2 grouping, threshold weakening, ansatz tuning or unproved internal repartition. Distinct source-signature q2 values and Iter582 connection q2 labels are never merged or summed. K1^3 remains retained. Repeated/coincident poles are never treated as ordinary simple cuts. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Closed C5 null-soft e=3 authority is not reopened.
