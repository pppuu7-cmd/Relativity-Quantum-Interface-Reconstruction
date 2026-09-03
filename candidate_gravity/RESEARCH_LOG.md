# Candidate Gravity Research Log

## 2026-09-03 — Iterations 319-324

### Iteration 319 — physical graviton routed components
Validated the Iteration-318 frozen minimal tensor Laplace operator `H=-(I Box+Pi)` through cubic background order in a fixed 10-component symmetric contravariant tensor basis. A truncated multivariate routing expansion was checked against an independent direct exact-geometry oracle on three non-collinear Fourier modes. Raw Actions artifact passed sentinel/schema and frozen numerical thresholds. Run `33722207947`; artifact `9880621340`; result SHA-256 `517adcb91f53f5758adf9af01c8b68a21c0a645627241639312b66a01e659671`. Full routed graviton `H1/H2/H3` authority is frozen in this scope.

### Iteration 320 — common-fixture determinant assembly
Reconstructed both frozen graviton and ghost layers on the same three-mode background and applied the Iteration-312 cubic logdet topology. The validated routed `(1,1,1)` fixture produced graviton `-189.6092989171087`, ghost `-40.548553581771024`, effective `1/2 H-N=-54.25609587678333`. Run `33722485847`; artifact `9880718552`; result SHA-256 `04f782373f1a831ad62fe0c934fb1f0d09c7ed7553b42d336b9e91c4778b51fe`.

### Iteration 321 — trace-closure audit
Before promoting Iteration 320 to a physical functional trace, checked total injected Fourier momentum. The fixture has `q1+q2+q3=(0.36,0.26,0.14,0.23)` and norm `0.5193264869039513`, hence it is not trace-closed. Iteration 320 is retained as a valid routing/local-operator fixture but is not a delta-supported physical determinant coefficient. Run `33722818612`; job `100545349697`; artifact `9880841854`; result SHA-256 `504fd85d0998e1c10ae94af1fa0f3883f9209a83da95fd3adfc8bf6fa062f77d`.

### Iteration 322 — momentum-closed triad
Recomputed the common H/N cubic assembly after replacing the third Fourier mode by `q3=-(q1+q2)`. Raw artifact validated exact trace closure and the local routed coefficient: graviton `-98.26141308373494`, ghost `-26.491576721630462`, effective `1/2 H-N=-22.639129820237006`. Run `33723018932`; job `100545950518`; artifact `9880912068`; result SHA-256 `1510534fa6075289abee867bf40582f39e2167063fd6617a36620a2f68eb2f2f`.

### Iteration 323 — shifted-free-propagator audit
Audited the higher-level functional-trace routing before denominator-family promotion. Raw result found `single_K0_inverse_assignment=true`, `A_uses_single_K0_inverse=true`, and `explicit_shifted_K0_inverse=false`, while pair/triple trace terms are present. Therefore Iteration 322 remains a validated momentum-closed local operator/routing fixture only; it is not yet a physical loop-integrand determinant coefficient. Run `33723183698`; job `100546443379`; artifact `9880968545`; result SHA-256 `39101bb6ee6aaf49dca554474fa40fb260c6bfa8bc770f7767d8a49e80933880`.

### Iteration 324 — shifted-free-propagator routing engine
The first run `33726453589` failed operationally before scientific execution because `numpy` was absent. Only the workflow dependency was repaired; no scientific code or frozen threshold was changed. Validated rerun `33726739255` then passed the full scientific/sentinel/schema/artifact gate. For the closed non-collinear `(1,1,1)` triad the engine enumerates six ordered pair and six ordered triple routes with successive `G0(p+Q)` inverses. Exact trace closure, finite/nonzero fixture denominators, explicit nonzero shifted propagators, and cyclic denominator-family equivalence up to common loop translation all pass. Classification: `PASS_SHIFTED_FREE_PROPAGATOR_ROUTING_ENGINE_CYCLIC_EQUIVALENCE`. Artifact `9882247698`; artifact digest `sha256:4bec2f0a1fc9c5de098f6b3ac5fa6f35dd7b506a2b45cb6035f1981bc64fe97f`; scientific result SHA-256 `efd8c34ceb18a379396e6cfa9f9af2bacbb5d6d0d70d8408125dde2ee11d8717`.

### Active computation
The denominator/routing skeleton is now frozen. The next dependent gate is to refactor/evaluate the already-authoritative physical graviton `H1/H2/H3` and ghost `N1/N2/N3` insertion kernels as functions of the correct arbitrary incoming loop momentum `p+Q` for every ordered route, and independently validate them against exact same-parent geometry before assembling the physical cubic determinant trace. Missing numerator evaluations remain `BLOCKED`, never zero-filled.

### Guardrails
No comparator residual has been claimed. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. Physical U2 `V1_1/V1_2/H0/H1` remains BLOCKED and is not zero-filled. No Source/Born subtraction before matched-observable pole/cut-origin classification. No blind heavy full-C5 run and no reopening of the closed C5 `e=3` sector.

MODEL_READINESS: 24%

Change from Iteration 323: `0 pp`. A determinant-routing subgate closed, but no robust comparator-subtracted residual or complete new readiness bucket closed.
