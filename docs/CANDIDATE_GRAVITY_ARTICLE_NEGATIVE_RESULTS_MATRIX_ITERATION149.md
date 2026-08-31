# Candidate Gravity Article Scaffold — Funnel / Negative-Result Matrix

**Iteration:** 149  
**Status:** working article table; scoped claims only.

## Interpretation rule

`FAIL` = failure of a frozen claim/model/gate. `BLOCKED` = comparator or observable not yet instantiated enough for the requested inference. `PASS_SCOPED` applies only to the explicitly tested object.

| Construction | Furthest established point | Limiting result | Article-safe interpretation |
|---|---|---|---|
| C3 postquantum classical gravity | broad class understood | fixed nonlinear ordered tangent not yet instantiated | BLOCKED comparator, not zero |
| C4 Gaussian KL spin-2 | exact Gaussian direct-integral/tower identity | `CG-NG-006` | valid Gaussian comparator; no novelty |
| C5 perturbative GR EFT | on-shell 12x10 local tangent rank 10/10; retarded factorization fixed | full RQIR tangent not yet instantiated | viable reference comparator |
| C5 on-shell tangent -> RQIR | finite amplitude certificate | `NG-FUNNEL-006` | S-matrix tangent is not `chi2R` tangent |
| on-shell 4pt kinematics -> retarded 3pt | retarded factorization known | `NG-FUNNEL-007` | off-shell protocol must be frozen independently |
| EOM-reduced C5 basis used off shell | field-redefinition audit complete | `NG-FUNNEL-008` | source/observable completion mandatory |
| source-completed finite C5 probe protocol | physical metric/source, six off-shell triplets, Gaussian windows and TT projectors frozen; Ward/projector checks ~1e-16 | `NG-FUNNEL-009`: projector PASS does not instantiate cubic vertex | source ambiguity closed; tangent now `BLOCKED_VERTEX_IMPLEMENTATION` |
| nonlinear C4 / massive spin-2 | not yet fixed | finite interacting realization missing | BLOCKED |
| nonlocal / asymptotic-safety comparators | program-level candidates known | no frozen finite tangent | BLOCKED; program labels are not comparators |

## Retained funnel rules

- `NG-FUNNEL-005`: broad capability masks saturate the finite reduced space and are not physical tangent matrices.
- `NG-FUNNEL-006`: on-shell amplitude tangent != ordered CTP/retarded RQIR tangent.
- `NG-FUNNEL-007`: on-shell 4pt kinematics do not fix off-shell retarded 3pt.
- `NG-FUNNEL-008`: an EOM-reduced on-shell basis is not automatically a basis-independent off-shell response basis.
- `NG-FUNNEL-009`: a Ward-safe source-completed probe layer is not a nonlinear-vertex/rank certificate.

## Current funnel

`C5 local on-shell rank` -> PASS_SCOPED;

`retarded causal factorization` -> PASS_SCOPED;

`off-shell source/observable equivalence` -> source completion required;

`Iteration-149 physical source + finite conserved probes` -> PASS_SCOPED;

`unreduced EH+local-EFT cubic vertex on those probes` -> **BLOCKED_VERTEX_IMPLEMENTATION**;

therefore no comparator quotient, Fisher/resource calculation, or `ANSATZ-003` promotion is yet admissible.
