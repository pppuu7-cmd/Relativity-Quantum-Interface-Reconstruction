# RQIR Candidate Gravity — Iteration 327

Date: 2026-09-03

## Purpose

Audit the last prerequisite before assembling the physical cubic determinant trace. Iteration 324 routes free denominators on the Iteration-322 closed non-collinear triad, while Iteration 326 claims full-topology arbitrary-incoming-momentum H/N numerator coverage. The two layers may be combined only if H and N use the same background metric modes and exactly the same closed external momenta.

## Finding

Iteration 326 correctly enumerates the full `1 + 6 + 6 = 13` cubic topology and rebinds the incoming loop momentum `p -> p+Q_before_insertion`, but its `load_frozen_prefix` changes only `p`.

It loads graviton insertions directly from `iteration319_det_graviton_three_mode_routing.py` and ghost insertions directly from `iteration317_det_ghost_three_mode_routing.py` without rebinding either source's `qs` or `hs` to the common Iteration-322 background.

This violates the common-background contract required for a physical graviton-minus-ghost determinant trace.

### External-momentum mismatch

Iteration-322 / Iteration-324 closed triad:

- `q1 = (0.27,-0.19,0.31,0.11)`
- `q2 = (-0.13,0.37,0.17,-0.29)`
- `q3 = (-0.14,-0.18,-0.48,0.18)`

Iteration-319 graviton fixture has the same first two modes but

- `q3 = (0.22,0.08,-0.34,0.41)`,

with maximum component difference `0.36` from the closed triad.

Iteration-317 ghost fixture uses

- `q1 = (0.30,-0.20,0.40,0.10)`
- `q2 = (-0.10,0.50,0.20,-0.30)`
- `q3 = (0.20,0.10,-0.40,0.45)`,

with maximum component difference `0.34` from the closed triad.

### Background-metric mismatch

The two historical fixture files also generate independent metric perturbations:

- graviton: RNG seed `319`, `h` scale `0.12`;
- ghost: RNG seed `317`, `h` scale `0.2`.

Thus a common incoming `p` does not make the H and N insertions one physical determinant background.

Iteration 322 already encoded the correct precedent: it replaces the graviton third mode by `q3=-(q1+q2)` and then reconstructs ghost N from the same graviton `hs/qs/p` through the shared Iteration-320 parent assembly.

## Typed disposition

`FAIL_SCOPED_GATE_DESIGN_ITERATION326_NOT_COMMON_CLOSED_TRIAD_BACKGROUND`

This is a **scoped gate-design failure** and dependent physical-trace blocker. It is not:

- a Candidate Gravity consistency FAIL;
- a physical H/N-kernel FAIL;
- an exact comparator identity;
- regime-specific non-identifiability;
- a near-degeneracy result;
- a novelty certificate.

Iteration 326 is not retroactively edited. Its retained valid scope is: all 19 requests of the full `1+6+6` topology were tested for arbitrary incoming `p` on their respective historical H and N fixture kernels. What is withdrawn is only the stronger interpretation that those requests constitute a common-background closed-triad numerator certificate compatible with Iteration-324 denominators.

## Denominator-family census retained as structural information

Before the blocker, exact loop-translation quotienting of the 13 topology sequences gives:

- 1 singleton translation family;
- 3 pair/bubble translation families;
- 2 triple/triangle translation families.

This census is structural only. A cut-capable denominator topology is not evidence of a nonzero discontinuity; no determinant cut is promoted until numerator/background authority is repaired.

## Reproducibility

Added `candidate_gravity/code/iteration327_audit_iteration326_common_closed_background_contract.py` and result JSON `candidate_gravity/results/iteration327_iteration326_common_closed_background_contract_audit.json`.

The audit is a light exact source-contract check; no heavy GitHub Action is scientifically required. Parent sources and current repository contents are the provenance.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 326: `0 pp`. The iteration found a blocker and narrowed an over-broad certificate interpretation; it did not close or destroy any complete readiness-rubric bucket. Comparator foundation remains `24/25` and robust unique residual remains `0/20`.

## Exact next gate

Create Iteration 328 as a new gate version from the Iteration-322 common closed-triad background. Rebind both external `qs` and arbitrary incoming `p` in the graviton factory, reconstruct ghost `N1/N2/N3` on exactly the same `hs/qs/p` parent as Iteration 320, and revalidate all 19 full-cubic routed insertion requests against same-parent exact geometry with the existing frozen thresholds. Only after that PASS may the physical determinant trace be assembled and denominator families be promoted to pole/cut-origin analysis.

Source/Born subtraction, `ANSATZ-003`, Fisher/resources and blind heavy full-C5 remain forbidden.
