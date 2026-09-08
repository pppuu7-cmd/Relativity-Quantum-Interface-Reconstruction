# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority
- Latest authoritative research iteration: **614**.
- Frozen Iter424 is **5/5 PASS**; Iter581 exact15 raw-valid PASS; Iter582 q2-resolved `D_s Gamma_{e=2}` assembly PASS/non-residual.
- Iter583–594 establish same-parent MSSC contacts, exact routing/normalization and the complete 13-family cubic source object; Iter605 independently raw-closes full source-level nonlinear Ward consistency.
- Iter606 raw-closes the prospective source-to-Iter582/native-linked mapping contract; Iter607 remains a preserved BLOCKED result because the explicit distributional projector was absent; Iter608 closes the universal scalar-pole distribution kernel only.
- Iter609–611 localize the missing native bridge to a minimal kinematic-rank obstruction: full source poles require three independent scalar data `(u,a_s,a_a)` whereas historical native `s` supplied only one coordinate.
- Iter612 proves that the two required auxiliary same-parent hard-channel constraints are absent from existing authority; therefore a new prospective completion, not a retroactive identification, is required.
- **Iter613 prospectively freezes `MSSC001-NATIVE-S-KIN-V1` before any pole root is evaluated.**
- **Iter614 is authoritative `PASS_ITER614_FROZEN_NATIVE_S_SCALAR_POLE_ROOT_AND_JACOBIAN_AUDIT__NON_RESIDUAL`.**

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

All six supported root points are distinct and simple. Minimum root separation is `0.00868572571657195`.

Absolute Jacobians `|partial_s D|`:

- `D_s^-(0.09)`: `2.333333333333333`;
- `D_s^-(2.89)`: `0.4117647058823529`;
- `D_a^+`: `0.6409796081665314`;
- `D_a^-`: `2.273306106119183`;
- `D_b^+`: `0.54342862858286`;
- `D_b^-`: `6.25657137141714`.

Therefore Iter608 pulls back in ordinary simple-root form at every supported point:

`delta(D_A(s)) = sum_r delta(s-s_r)/|partial_s D_A(s_r)|`.

Support counts:
- denominator types with positive support: **5/6**;
- distinct positive simple-root points: **6**;
- K1/K2 routed terms with positive support: **5/6**;
- K1^3 ordered chains with positive support: **6/6**.

`D_s^+` support absence is not an amplitude-zero statement. All 13 source families remain retained; `zero_fill=false`. K3 remains local in this scalar-pole classification.

## Iter582 operator coordinate
`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`:
- `q^2=-1.0`: `+0.0003272233895861266 i`
- `q^2=-0.34`: `-0.00371666346186323 i`
- `q^2=-0.14`: `-0.0007997265433511544 i`

## Stable readiness rubric
- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter614: **0 percentage points**. The native kinematic definition and pole/Jacobian prerequisite are now closed prospectively, but no additional complete model-level rubric sector has closed.

## Exact next gate — source numerator/sign and native normalization binding
Evaluate the unchanged Iter594/605 MSSC-001 source numerator and routing sign on every Iter614 supported simple root, preserving the full K3 + six K1/K2 + six K1^3 source family set. Verify that no two retained routed denominators vanish simultaneously on a listed root before using the ordinary simple-root distribution formula. Then bind the resulting distributional source object to the native Iter205 `Y/T_cut` sign/normalization convention and the Iter582 operator coordinate.

Source/Born subtraction remains `NOT_PERFORMED` until the matched observable and pole/cut origin are bound. No fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient before that map closes. No `ANSATZ-003`; no Fisher/resources.

## Compute status
No scientifically useful heavy numerical job is required for the Iter613–614 gates. Duplicate heavy authority runs remain forbidden. The next gate is an algebraic/lightweight source-residue audit; only after its definition is complete may a numerical validation workflow be justified.

## Retained guardrails
Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, altered normalization, changed q2 grouping, threshold weakening, ansatz tuning or unproved internal repartition. Distinct source-signature q2 values and Iter582 connection q2 labels are never merged or summed. K1^3 remains retained. Repeated/coincident poles, if later encountered, are never treated as ordinary simple cuts. Old weighted-B3 proxy residues are not actual `Tr U1` authority. Closed C5 null-soft e=3 authority is not reopened.
