# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 326**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority.

## Authoritative state

- Iteration 246 closes generic connection `e=3,c=0`; do not reopen it.
- Iteration 307 freezes the complete eight-family `e=1,c=2` weight-completed actual `Tr U1` normalized cut.
- Iterations 308-310 freeze `e=2,c<=1` bookkeeping/typed U2 contract/U1^2 routing; physical U2 `V1_1/V1_2/H0/H1` remains BLOCKED.
- Iteration 312 freezes the exact cubic `log det` operator topology.
- Iterations 314-317 derive and validate full routed physical ghost `N1/N2/N3` authority.
- Iteration 318 freezes the same-parent local graviton operator at `D=4, Lambda=0, a=-1/2`, `H=-(I Box+Pi)`.
- Iteration 319 freezes full routed physical graviton `H1/H2/H3` authority after a rank-3 non-collinear exact-geometry certificate. Run `33722207947`, artifact `9880621340`, result SHA-256 `517adcb91f53f5758adf9af01c8b68a21c0a645627241639312b66a01e659671`.
- Iteration 320 validates common-fixture H/N cubic assembly but its original Fourier triad is not trace-closed; Iteration 321 therefore retains it only as a routed/local integrand fixture.
- Iteration 321 raw authority: run `33722818612`, job `100545349697`, artifact `9880841854`, result SHA-256 `504fd85d0998e1c10ae94af1fa0f3883f9209a83da95fd3adfc8bf6fa062f77d`; classification `PASS_TRACE_CLOSURE_AUDIT__ITERATION320_IS_ROUTING_FIXTURE_NOT_PHYSICAL_TRACE`.
- Iteration 322 recomputes the common H/N cubic assembly on the non-collinear closed triad `q3=-(q1+q2)`, exactly `q_total=0`. Run `33723018932`, job `100545950518`, artifact `9880912068`, result SHA-256 `1510534fa6075289abee867bf40582f39e2167063fd6617a36620a2f68eb2f2f`. Its local closed-triad coefficient is graviton `-98.26141308373494`, ghost `-26.491576721630462`, effective `1/2 H-N=-22.639129820237006`.
- Iteration 323 audits the higher-level functional-trace momentum routing and finds `explicit_shifted_K0_inverse=false`; Iteration 322 is therefore retained only as `MOMENTUM_CLOSED_LOCAL_OPERATOR_ROUTING_FIXTURE_ONLY`.
- Iteration 324 implements the missing explicit ordered shifted-free-propagator routing engine. Validated rerun `33726739255`, job `100557310502`, artifact `9882247698`, artifact digest `sha256:4bec2f0a1fc9c5de098f6b3ac5fa6f35dd7b506a2b45cb6035f1981bc64fe97f`, scientific result SHA-256 `efd8c34ceb18a379396e6cfa9f9af2bacbb5d6d0d70d8408125dde2ee11d8717`. It validates six ordered pair and six ordered triple routes on the closed non-collinear `(1,1,1)` triad, with exact trace closure, explicit nonzero shifted propagators, finite/nonzero fixture denominators, and cyclic denominator-family equivalence up to a common loop-momentum translation. Certificate: `PASS_SHIFTED_FREE_PROPAGATOR_ROUTING_ENGINE_CYCLIC_EQUIVALENCE`.
- Iteration 325 attempted physical arbitrary-incoming-momentum H/N numerator validation. The diagnostic run `33732034116`, artifact `9884220998`, scientific JSON SHA-256 `7fbcac2f284f4036bfde903be789662601282afad7f5b182ee5be68fae892185`, showed that all 18 actually instantiated shifted pair/triple H/N insertions pass with max scaled errors of order `1e-9`. However, the validator itself omitted the singleton cubic `Tr(G0 K3)` topology and therefore never tested `(1,1,1)` H3/N3. Iteration 325 is retained as `FAIL_SCOPED_GATE_DESIGN_INCOMPLETE_CUBIC_TOPOLOGY__TESTED_SHIFTED_HN_INSERTIONS_PASS`. This is a gate-design/completeness failure, not a Candidate Gravity consistency FAIL and not a physical H/N-kernel FAIL. It is not retroactively edited.
- Iteration 326 creates a new gate version with exactly the same parent kernels, `h=2e-4`, and frozen thresholds, adding only the missing singleton `Tr(G0 K3)` topology. Validated run `33732390687`, job `100575080806`, artifact `9884357539`, artifact digest `sha256:147fe5e1a63d238310ecb26b46280420f2ef7f93db26e554d769c9dbf75e0470`, scientific JSON SHA-256 `12174bc74e9cb350a6c6ea9c15cdc4db255f9794b91d0289947519a59e75db35`. Full topology = one singleton + six ordered pairs + six ordered triples = `13` sequences and `19` unique incoming-shift/insertion requests. All routes close, nonzero shifted incoming momenta are tested, and the cubic `(1,1,1)` insertion is explicitly validated. Ghost max scaled errors by order `1/2/3`: `2.4427370126645087e-09`, `4.154289856561633e-09`, `3.5029705029235303e-06`; graviton: `7.896245324268136e-10`, `3.99741803894238e-09`, `8.485603715067437e-06`, all below unchanged frozen thresholds.

Iteration-326 authority:
`PASS_PHYSICAL_HN_ARBITRARY_INCOMING_MOMENTUM_FULL_CUBIC_TOPOLOGY_CERTIFICATE`.

The determinant branch now has jointly certified shifted free-propagator routing (Iteration 324) and physical arbitrary-incoming-momentum H/N numerator routing (Iteration 326). This permits assembly of the physical cubic determinant trace. It does not yet promote an integrated determinant coefficient, timelike discontinuity, comparator-subtracted residual, or novelty certificate.

## Active sectors

- connection `e=1,c<=2`: actual `Tr U1` cut frozen by Iteration 307.
- connection `e=2,c<=1`: physical U2 `V1_1/V1_2/H0/H1` remains BLOCKED; no zero-fill.
- determinant `e=0,c<=3`: exact cubic topology, full physical ghost/graviton kernels, trace closure, shifted free-propagator routing and arbitrary-incoming-momentum H/N numerator routing are frozen. Physical cubic determinant trace assembly and denominator-family/pole-cut-origin classification remain open.

## Exact next gate

**Iteration 327:** assemble the physical cubic graviton-minus-ghost determinant trace using the frozen Iteration-312 topology, Iteration-324 shifted free propagators and Iteration-326 routed H/N insertions. Canonicalize the resulting denominator families under proved loop-momentum translations and classify which terms can generate physical timelike pole/cut structure versus local/rational/scaleless pieces. Preserve the frozen graviton/ghost prefactors and parent convention. Source/Born subtraction remains forbidden until pole/cut-origin classification is complete.

Only after this origin classification may the determinant contour advance toward an integrated normalized cut and comparator quotient. Unsupported reductions remain `BLOCKED`, never zero-filled.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change from Iteration 326: `0 pp` relative to Iteration 325. A genuine determinant numerator-routing subgate closed, but no robust comparator-subtracted residual or complete new readiness bucket closed.

## Retained guardrails

- Unsupported coordinates/kernels are `BLOCKED`, never zero-filled.
- Do not create `ANSATZ-003` before a concrete robust comparator-subtracted residual.
- Fisher/resources remain forbidden until a robust nonzero residual survives comparator subtraction.
- Source/Born subtraction only in a matched observable after pole/cut-origin classification.
- Green Actions is not authority without sentinel/schema/raw-artifact audit.
- Negative/higher-level audits narrow interpretation without retroactively weakening frozen thresholds.
- Iteration 325 remains a preserved scoped gate-design failure; its thresholds and code are not retroactively rewritten into a pass.
- Blind heavy full-C5 remains unauthorized; closed C5 `e=3` authority is not reopened.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.
