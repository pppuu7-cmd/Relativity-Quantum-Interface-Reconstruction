# Candidate Gravity Current Front

**Updated:** 2026-09-09  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none

Repository commits, validated Actions artifacts, recovery deltas, research logs and this file are source of truth. Workflow colour alone is never scientific authority. Race-created newer repository state wins; authoritative iteration IDs are never reused.

## Current authority

Latest authoritative research iteration: **631**.

Historical authority through Iter627 remains unchanged: Iter581 exact15 PASS; Iter582 q2-resolved connection coordinate PASS/non-residual; Iter594 complete 13-family MSSC source object; Iter605 source nonlinear Ward PASS; Iter613 frozen native hard-channel trajectory; Iter614 six simple-root/Jacobian support points; Iter615 historical common-`K+i0` source coefficients; Iter616 exact q2/end-point identity; Iter627 raw-valid combined matter+gravity SK measurement contract.

### Iter628 — open retarded scalar-response authority

The six supported scalar-pole coefficients are raw-valid authority only for the open endpoint-amputated scalar response under the Iter627 retarded internal-line prescription. They remain preserved and are not direct gravitational-1PI coefficients.

### Iter629 — universal `N_native` rejected

Canonical raw authority: run `34285497992`, job `102260007489`, head `f35fc211b684957901c62aebc683aa94147960b9`, artifact `10079284705`, digest `sha256:654d85897d882d41ccdeb1675d5088db6a74665f9388542b284bd94308ba50dc`; raw result SHA-256 `272bd82b5f9b84b3c1450fdf337a7d611457304bdede650b6b9918d5990abc25`, audit SHA-256 `0987a721095573387b10e95763f21a4fa2297efeb088c1aa5104023e21fddc3a`, `failures=[]`.

Open family totals `(-1,+6,-6)` and closed `ThirdDerivative Tr log K` totals `(+1,-3,+2)` have ratios `(-1,-2,-3)`. No single complex `N_native` can map the open scalar response to closed gravitational 1PI. Fitting one is forbidden.

### Iter630 — closed retarded loop needs `G_K`

Canonical raw authority: run `34289414837`, job `102272371234`, head `6aee9bcdddffa7fe29ad65eeb35b7adbe965f2d5`, artifact `10080743600`, digest `sha256:ee5a9b16d0e0a79d2346115090cf8a76f9767902add8c54ecba27c05d2ec616e`; raw runtime SHA-256 `48363b1e9efbe4a646899cffd6e5e988e5d66d60f41c36fdd250892b23dd7c14`, audit SHA-256 `26ad06b1dbe6637dc81a0feb62bee10507da7e42bd5546d74d80d2448d337db9`, `failures=[]`.

From the Iter627 r/a matrix `G=[[G_K,G_R],[G_A,0]]` and metric vertices derived from the doubled MSSC001 quadratic functional:

- K3 one-a closed contact: `G_K`;
- K1/K2 one-a/one-r trace: `G_K G_A + G_K G_R`;
- K1^3 arr/rar/rra trace: `G_K G_A^2 + G_K G_R G_A + G_K G_R^2`.

Every closed retarded scalar-loop family contains exactly one statistical/Keldysh propagator. Iter628 cannot be promoted to gravitational retarded `Gamma3` by common or root-wise reweighting.

### Iter631 — scalar state underdetermined by Iter627

Canonical raw authority: run `34289607051`, job `102272978390`, head `0cbb7daf76000f1b00ac0d109be52ef92b1efacd`, artifact `10080814393`, digest `sha256:6c8fb7fd6802bf4a996d3336c5e2dc76eb07cd0b83bd00b96eb368713145697c`; raw runtime SHA-256 `5adb9e853cc6b45cbf70d187e55fdd722d70870536c030ab77566acf034b36a8`, audit SHA-256 `cd6d76153002b8edecb1373bcf22f276387abdf25d3684c37dd4b8cf7fb62816`, committed-result copy SHA-256 `af6d5d16dce618057bd91b7670752827a4d47ed18598d5e71b2dc6c6e028ee91`, `failures=[]`.

Classification: `BLOCKED_ITER631_ITER627_CTP_CAUSAL_CONTRACT_DOES_NOT_FIX_SCALAR_KELDYSH_STATE__GK_REQUIRES_PROSPECTIVE_STATE_BOUNDARY_CONDITION__NON_RESIDUAL`.

Iter627 fixes causal r/a slots but not the scalar initial density matrix, occupation, temperature, vacuum/Hadamard condition or absolute state normalization. Therefore `G_R/G_A` do not uniquely determine `G_K`. This is a prerequisite BLOCKED, not Candidate-Gravity FAIL. Iter628 remains preserved.

## Active run / ANTI-IDLE

The Iter631 blocker is scientifically resolvable prospectively before any closed-loop result. **Iteration632 is queued:** run `34289739464`, head `20916a5430873eb48dcc3abd09b46c9491eb33cf`.

Iter632 prospectively freezes `MSSC001-SCALAR-STATE-MINKOWSKI-VACUUM-V1` before inspecting any closed-loop/native Candidate value: zero-temperature, Poincare-invariant, positive-energy Hadamard Minkowski state for the already-flat MSSC001 parent, with `G_K(k)=sgn(k0)[G_R(k)-G_A(k)]` in the Iter627 convention. Workflow colour will not count as PASS until its raw artifact is independently checked.

## Frozen support retained

All 13 MSSC source families remain retained; `zero_fill=false`. Iter613 hard-channel trajectory remains frozen. `D_s^+` having no positive root is not amplitude zero. No root/family may be deleted to simplify the bridge. Source/Born subtraction remains `NOT_PERFORMED`; native projection `NOT_PERFORMED`.

## Iter582 connection coordinate

`D_s Gamma_e2(q^2)=+(i/2)D_s Tr U2-(i/4)D_s Tr U1^2`:

- `q^2=-1.0`: `+0.0003272233895861266 i`;
- `q^2=-0.34`: `-0.00371666346186323 i`;
- `q^2=-0.14`: `-0.0007997265433511544 i`.

These Candidate-side values are forbidden for choosing state, normalization, branch prescription or closed-loop decomposition.

## KG start ledger

1. **KGSTART-1 — ACTIVE:** close same-parent retarded scalar-loop gravitational `Gamma3`, including state/`G_K` contract and pole/cut-origin classification.
2. **KGSTART-2:** full native `Y/T_cut` projection with all supported roots/families, then matched Source/Born subtraction.
3. **KGSTART-3:** fixed C0–C6 comparator quotient in the same observable/nuisance convention.
4. **KGSTART-4:** robust nonzero comparator-subtracted algebraic residual.
5. **KGSTART-5:** challenge residual against known gravity/QG realizations without funnel tuning.
6. **KGSTART-6:** issue `EXISTING_SUFFICIENT`, `ADAPT_EXISTING`, `HYBRID_REQUIRED`, or `NEW_REQUIRED`; only `NEW_REQUIRED` authorizes `ANSATZ-003`.

## Stable model-readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

**MODEL_READINESS: 24%**

Readiness change through Iter631: **0 percentage points**. No robust unique residual or complete new rubric sector has closed.

## Exact next gate

Terminal Iter632 -> independent raw artifact consumption. Only after raw-valid state-contract closure may Iter633 derive/evaluate closed retarded K3/K1K2/K1^3 pole/cut support and integration measure on Iter613 kinematics. No native `Y/T_cut` projection or Source/Born subtraction before pole/cut origin is classified.

## Guardrails

Unsupported is `BLOCKED`, never zero-filled. Operational failure is not scientific FAIL. Negative results are preserved. No post-hoc trajectory/state/estimator/normalization fit, q2 regrouping, root summation, branch hand-flip, threshold weakening or ansatz tuning. K1^3 remains retained. Repeated/coincident poles are never ordinary simple cuts. No comparator quotient before native binding. No `ANSATZ-003`; no Fisher/resources.
