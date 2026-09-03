# RQIR Candidate Gravity — Iteration 316

Date: 2026-09-03

MODEL_READINESS: 24%

## Authoritative predecessor
Iteration 315 validated the ghost inverse-metric/principal-symbol plus Ricci/mixed-Ricci recursion, but left the vector covariant-Box connection routing BLOCKED.

## Corrected execution and scientific result
The first Iteration-316 execution failed before schema/audit artifact preservation and was therefore only an operational/unobservable failure. The code defect was then identified without changing any scientific threshold: `Rm` had been allocated only at order zero while the routed code populated orders 1..3. Commit `debc401e441e5ed0ec16706cdaaf1a75500a722b` fixes only that coefficient allocation and explicitly prevents silent zero-fill/index loss.

The corrected dependent run is scientifically schema-valid:
- run `33717509817`
- job `100529695008`
- head/code commit `debc401e441e5ed0ec16706cdaaf1a75500a722b`
- artifact `9879043723`
- artifact digest `sha256:4fa8792815eb5a2e41ec3232d292c2f985221d1493dc2cbcaf6e46ee866f558b`
- scientific execution PASS
- sentinel/schema audit PASS
- artifact upload PASS
- final frozen scientific gate PASS.

Freeze:
`PASS_FULL_ROUTED_GHOST_N123_SINGLE_MODE_CERTIFICATE__MULTIMODE_CROSS_ROUTING_REMAINS_TO_BE_TESTED`.

The executable same-parent operator remains
`N^a_b = delta^a_b Box + R^a_b`
with one convention `D=4, Lambda=0, a=-1/2`. Order `n` routes ghost momentum `p -> p+n q`. The implementation now includes the full vector covariant-Box terms together with the already validated Ricci/mixed-Ricci layer.

## Scope boundary
This is a genuine scientific PASS, but it is a **single-mode** routing certificate. A one-mode background cannot independently expose all mixed Fourier routing terms, especially cubic cross terms involving three distinct background momenta. Therefore full arbitrary-background ghost authority is not promoted yet.

A stricter independent Iteration 317 has been added to test three non-collinear Fourier modes with explicit multi-index convolutions, including the cubic `(1,1,1)` coefficient. Run `33717920513` is queued and must not be duplicated or promoted before schema-valid completion.

This result is not a Candidate Gravity residual, not a comparator identity, not a consistency FAIL, not near-degeneracy, and not a novelty certificate. Graviton `H1/H2/H3` remains BLOCKED and determinant insertion remains forbidden until both ghost mixed-routing and graviton authority are closed.

MODEL_READINESS: 24%
Change from Iteration 315: `0 pp`; the full single-mode routed ghost operator closed, but no readiness-rubric block or robust comparator-subtracted residual closed.
