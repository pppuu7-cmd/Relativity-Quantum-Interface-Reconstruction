# RQIR Candidate Gravity — Iteration 326

Date: 2026-09-03

## Purpose

Close the numerator-routing blocker left by Iteration 324 using the exact full cubic logdet topology and the already-frozen same-parent ghost `N1/N2/N3` and graviton `H1/H2/H3` operators.

Iteration 326 is a new gate version after Iteration 325 exposed a topology-coverage defect. It adds only the missing singleton `Tr(G0 K3)` sequence. Physical kernels, incoming-momentum convention, mixed-finite-difference step `h=2e-4`, and all frozen thresholds are unchanged.

## Full topology and routing

For target multiindex `(1,1,1)` on the same closed non-collinear triad as Iteration 324, the gate contains:

- `1` singleton cubic sequence;
- `6` ordered pair sequences;
- `6` ordered triple sequences;
- `13` full cubic topology sequences total;
- `19` unique `(incoming shift, insertion multiindex)` requests.

Every insertion is evaluated as the frozen physical kernel `K_a(p+Q_before_insertion)`. All routes close exactly, nonzero shifted incoming momenta are exercised, and the required singleton cubic `(1,1,1)` insertion is tested.

## Independent exact-geometry oracle

The routed polynomial insertions were compared with the same-parent direct exact-geometry operator using symmetric mixed finite differences.

Ghost request counts by order: `12 / 6 / 1` for orders `1 / 2 / 3`.

Ghost max scaled errors:

- order 1: `2.4427370126645087e-09` versus threshold `2e-6`;
- order 2: `4.154289856561633e-09` versus threshold `3e-4`;
- order 3: `3.5029705029235303e-06` versus threshold `8e-2`.

Graviton request counts by order: `12 / 6 / 1`.

Graviton max scaled errors:

- order 1: `7.896245324268136e-10` versus threshold `3e-6`;
- order 2: `3.99741803894238e-09` versus threshold `5e-4`;
- order 3: `8.485603715067437e-06` versus threshold `1.2e-1`.

All frozen gates pass without threshold weakening.

## Provenance

Validated Action run `33732390687`, job `100575080806`, artifact `9884357539`.

Artifact digest: `sha256:147fe5e1a63d238310ecb26b46280420f2ef7f93db26e554d769c9dbf75e0470`.

Scientific JSON SHA-256: `12174bc74e9cb350a6c6ea9c15cdc4db255f9794b91d0289947519a59e75db35`.

Single top-level object, sentinel `326`, scientific exit code `0`, final scientific enforcement PASS.

## Frozen certificate

`PASS_PHYSICAL_HN_ARBITRARY_INCOMING_MOMENTUM_FULL_CUBIC_TOPOLOGY_CERTIFICATE`

The determinant branch now has jointly certified shifted free-propagator routing (Iteration 324) and physical arbitrary-incoming-momentum H/N numerator routing (Iteration 326). This makes physical cubic determinant trace assembly permissible.

It does **not** yet establish an integrated determinant coefficient, a timelike cut, a comparator-subtracted residual, or novelty. Source/Born subtraction remains forbidden before pole/cut-origin classification.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 325: `0 pp`. A real determinant numerator-routing subgate closed, but no complete stable-rubric bucket and no robust comparator-subtracted residual have closed.

## Exact next gate

Assemble the physical cubic graviton-minus-ghost determinant trace using the Iteration-312 topology, Iteration-324 shifted propagators and Iteration-326 routed H/N insertions. Canonicalize denominator families and classify pole/cut origins before any Source/Born subtraction. Do not start Fisher/resources and do not create `ANSATZ-003`.
