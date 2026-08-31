# Candidate Gravity Article Scaffold — Funnel / Negative-Result Matrix

**Iteration:** 151  
**Status:** working article table; scoped claims only.

`FAIL` = frozen scientific claim/model failure. `BLOCKED` = missing comparator/observable implementation. `PASS_SCOPED` = only the explicitly tested subspace.

| Construction | Furthest established point | Limiting result | Article-safe interpretation |
|---|---|---|---|
| C3 postquantum classical gravity | broad class understood | fixed nonlinear ordered tangent not yet instantiated | BLOCKED comparator, not zero |
| C4 Gaussian KL spin-2 | exact Gaussian direct-integral/tower identity | `CG-NG-006` | valid Gaussian comparator; no novelty |
| C5 perturbative GR EFT on-shell | 12x10 local tangent rank 10/10 | `NG-FUNNEL-006` | valid on-shell reference only |
| C5 source-completed finite probe layer | physical metric/source + six off-shell TT probes | `NG-FUNNEL-009` | probe PASS is not vertex PASS |
| C5 explicit local tree nonlinear response | EH TT baseline + two curvature-cubic columns | local `6x2` tangent rank `2/2`, `smin/smax=0.2294` | first finite local retarded-response tangent, PASS_SCOPED |
| naive off-shell longitudinal-null test | isolated EH 3-vertex nonzero | `NG-FUNNEL-010` | invalid gate, not a GR FAIL |
| source-completed EH off-shell Ward identity | action-level `B3[L_xi]+B2[Lie_xi]` tested on six probes | worst relative residual `2.724e-6`, with ~4x reduction per step halving | **PASS_SCOPED**; nonlinear Lie/source-contact terms cancel isolated longitudinal cubic variation |
| curvature-cubic Ward completion | TT response columns exist | completed diffeomorphism identity not yet tested for both operators | BLOCKED_VALIDATION, not zero |
| C5 higher local directions | not implemented in off-shell response basis | missing explicit columns | BLOCKED, not zero |
| C5 loop/nonanalytic sector | causal need recognized | no finite implemented columns | BLOCKED, not zero |
| nonlinear C4 / massive spin-2 | not yet fixed | finite interacting realization missing | BLOCKED |
| nonlocal / asymptotic-safety comparators | program-level candidates known | no frozen finite tangent | BLOCKED; program labels are not comparators |

## Retained funnel rules

- `NG-FUNNEL-005`: broad capability masks are not physical finite tangent matrices.
- `NG-FUNNEL-006`: on-shell amplitude tangent != ordered CTP/retarded RQIR tangent.
- `NG-FUNNEL-007`: on-shell 4pt kinematics do not fix off-shell retarded 3pt.
- `NG-FUNNEL-008`: an EOM-reduced on-shell basis is not automatically an off-shell response basis.
- `NG-FUNNEL-009`: a source-completed projector/probe PASS is not a nonlinear vertex certificate.
- `NG-FUNNEL-010`: `k·Gamma3=0` is not the standalone off-shell gravitational Ward identity. Iteration 151 confirms the correct completed identity passes for EH.

## Current funnel

`C5 on-shell local rank` -> PASS_SCOPED;

`retarded factorization` -> PASS_SCOPED;

`source-completed six-probe protocol` -> PASS_SCOPED;

`EH + first two local curvature-cubic response columns` -> PASS_SCOPED, rank 2/2;

`EH source-completed off-shell Ward identity` -> **PASS_SCOPED**;

`curvature-cubic completed Ward validation` -> **BLOCKED_VALIDATION**;

therefore full C5 comparator quotient is still not closed and Fisher/resources or `ANSATZ-003` promotion remain inadmissible.
