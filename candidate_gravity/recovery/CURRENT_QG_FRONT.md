# Candidate Gravity Current Front

**Updated:** 2026-09-08  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated raw Actions artifacts, recovery deltas, research logs, and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repo state wins and authoritative iteration IDs are never reused.

## Current authority

- Latest authoritative research iteration: **616**.
- Frozen Iter424 is **5/5 PASS**; Iter581 exact15 raw-valid PASS; Iter582 q2-resolved `D_s Gamma_{e=2}` assembly PASS/non-residual.
- Iter583–594 establish same-parent MSSC contacts, exact routing/relative normalization and the complete 13-family cubic source object; Iter605 independently raw-closes full source-level nonlinear Ward consistency.
- Iter606 raw-closes the prospective source-to-Iter582/native-linked mapping contract; Iter607 is preserved as scientific `BLOCKED`; Iter608 closes the universal scalar-pole distribution law.
- Iter609–612 localize the missing native bridge to a kinematic-rank obstruction and prove the required historical auxiliary constraints are absent.
- Iter613 prospectively freezes `MSSC001-NATIVE-S-KIN-V1`; Iter614 closes positive-s simple-root support/Jacobians.
- Iter615 closes all six supported routed internal scalar-pole source coefficients as finite and nonzero, with two independent implementations agreeing.
- **Iter616 closes exact source/Iter582 q2 bucket identity and exact external scalar endpoint amputation, and narrows the remaining native binding ambiguity to one common nonzero scalar `N_native`. The full native binding therefore remains `BLOCKED`, not FAIL and not residual.**

## Frozen native-s kinematics / pole support

In MSSC-001 convention `(+---)`, for `s>0`:

`p0(s)=(sqrt(s),0,0,0)`.

Hold fixed the exact Iter368/588 mode vectors/polarizations, mass `m=0.7`, routing/sign/normalization/i0 conventions and rest-frame axis. Thus

`u(s)=s`, `a_i(s)=sqrt(s) q_i^0`, `a_s+a_a+a_b=0`,

`D_i^+(s)=m^2-s-q_i^2-2sqrt(s)q_i^0`,

`D_i^-(s)=m^2-s-q_i^2+2sqrt(s)q_i^0`.

Positive simple roots:

- `D_s^+`: no positive root;
- `D_s^-`: `0.09`, `2.89`;
- `D_a^+`: `1.241314274283428`;
- `D_a^-`: `0.09868572571657197`;
- `D_b^+`: `1.726971411425142`;
- `D_b^-`: `0.013028588574858`.

No support absence is amplitude zero. All 13 source families remain retained; `zero_fill=false`.

## Iter615 source-side normalized internal scalar-pole coefficients

With Iter608 `Disc[1/(D+i0)] = -2*pi*i delta(D)` and Iter205 `D_s=Disc_s/(2*pi*i)`, the six aggregate source-side normalized coefficients are:

- `D_b^-(0.013028588574858)`: `-0.00024912100468199333`;
- `D_s^-(0.09)`: `+0.0007390333386357162`;
- `D_a^-(0.09868572571657197)`: `+0.00019432750619153958`;
- `D_a^+(1.241314274283428)`: `+0.0012850179378006798`;
- `D_b^+(1.726971411425142)`: `-0.0007467205092433388`;
- `D_s^-(2.89)`: `-0.0021373920072305236`.

All are finite and nonzero. K1/K2 and K1^3 terms are retained with their frozen same-action relative signs. K3 is local in this routed-internal pole classification; this is not an amplitude-zero claim.

## Iter616 endpoint-amputation and minimal normalization blocker

### Exact q2 bucket identity

Iter588 already froze the same Iter368 mode vectors under opposite metric signatures, `ETA_C=(-+++)` and `ETA_S=-ETA_C`. Therefore the map is an identity of the physical mode label, not a fitted correspondence:

- `s`: source `q^2=+1.0` <-> Iter582 connection `q^2=-1.0`;
- `b`: source `q^2=+0.34` <-> Iter582 connection `q^2=-0.34`;
- `a`: source `q^2=+0.14` <-> Iter582 connection `q^2=-0.14`.

Buckets remain distinct and are never summed.

### Exact external endpoint amputation

For the complete Iter594 same-action cubic scalar response

`d_abc G = -G Kabc G + sum_6(G Ki G Kjk G) - sum_6(G Ki G Kj G Kk G)`,

freeze

`S_amp^(3)=K0_out (d_abc G) K0_in`,

hence

`S_amp^(3)=-Kabc+sum_6(Ki G Kjk)-sum_6(Ki G Kj G Kk)`.

This amputates only the two common external scalar propagators. Internal scalar propagators and pole support, K3 contact and all K1^3 chains remain retained. On the two frozen Iter594 probes, direct and termwise amputation agree with maximum absolute discrepancy `8.673617379884035e-19`, consistent with stored decimal rounding.

### Remaining binding dimension

The remaining ambiguity is exactly one common nonzero scalar:

`N_native` = source-response <-> Iter582 native effective-action/retarded phase and absolute normalization.

Historical authority fixes all relative source-sector factors (Iter589/594), the cut sign/distribution (Iter608/615), the native-s pullback/Jacobians (Iter613/614), q2 identity (Iter588) and endpoint amputation (Iter616), but does not yet supply one explicit cross-sector equation fixing `N_native`.

`N_native` must **not** be fitted to the six Iter615 values, separately tuned by root or q2 bucket, or inferred by weakening/redefining any frozen convention.

Iter616 classification:

`BLOCKED_ITER616_ENDPOINT_AMPUTATION_AND_Q2_BINDING_CLOSED__ONE_COMMON_NATIVE_NORMALIZATION_SCALAR_UNRESOLVED__NON_RESIDUAL`.

## Iter582 connection operator coordinate

`D_s Gamma_e2(q^2) = +(i/2)D_s Tr U2 -(i/4)D_s Tr U1^2`:

- `q^2=-1.0`: `+0.0003272233895861266 i`;
- `q^2=-0.34`: `-0.00371666346186323 i`;
- `q^2=-0.14`: `-0.0007997265433511544 i`.

These values are not to be used to fit `N_native`.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter616: **0 percentage points**. The source/native mapping ambiguity is now one-dimensional, but no robust comparator-subtracted residual or complete readiness sector is closed.

## Exact next gate — independent lower-order normalization anchor

Prospectively determine `N_native` from an **independent lower-order/common-field normalization identity** that uses the same physical metric perturbation and the same retarded/effective-action convention, without consulting any projected Iter615 Candidate value.

The audit must answer fail-closed:

1. whether the MSSC source derivative variable and connection-sector metric perturbation are the same physical `delta g` variable or differ by an explicitly fixed `kappa` convention;
2. whether the retarded/source response and Iter582 effective-action coordinate carry an already frozen common `i`/sign convention;
3. whether these facts fix one unique `N_native` independent of root and q2 bucket.

If repository authority does not fix it, record the exact one-scalar blocker rather than choosing a convention post hoc. Only a prospectively fixed `N_native` may authorize full native `Y/T_cut` projection, then Source/Born subtraction, and only afterwards the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.

## Compute status

No scientifically useful heavy job is currently required. The next gate is algebraic/convention-level; duplicate heavy authority runs are forbidden.

## Retained guardrails

Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory change, estimator, normalization fit, q2 regrouping, threshold weakening, ansatz tuning or unproved internal repartition. Distinct q2 buckets are never summed. K1^3 remains retained. Repeated/coincident poles are never treated as ordinary simple cuts. Source/Born subtraction remains `NOT_PERFORMED`. No fixed comparator quotient before native binding closes. No `ANSATZ-003`; no Fisher/resources.
