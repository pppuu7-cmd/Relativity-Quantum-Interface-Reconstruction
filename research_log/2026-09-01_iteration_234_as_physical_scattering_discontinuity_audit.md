# Research log — RQIR Candidate Gravity Iteration 234

Date: 2026-09-01

MODEL_READINESS: 24%

Started from repository authority: `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, Iteration-233 recovery delta/research log, recent commits, and current Actions state. Authoritative front was Iteration 233; GitHub Actions reported no workflow runs.

## Scientific action

Audited the newest physical asymptotic-safety scalar-scattering authority against the frozen linked RQIR discontinuity target.

Primary authority: Chiesa, Pawlowski, Reichert, arXiv:2603.10168 (2026).

The paper provides a same-construction RG-invariant graviton-mediated scalar amplitude built from `phi-phi-h` vertices and a graviton propagator, and reconstructs an on-shell Lorentzian dressing `V_L(s)`. This materially strengthens AS physical authority and corrects any overly broad wording that no physical same-normalization Lorentzian AS observable exists.

However, the result does not supply the frozen RQIR object

`T_cut = D Gamma3_ret,soft - W[D K2]`.

The scalar amplitude is an inequivalent observable and uses different nonlinear ingredients. The timelike vertex is reconstructed from Euclidean data using a non-unique continuation procedure; the paper explicitly warns of possible reconstruction artefacts, does not include flow-approximation errors in the quoted reconstruction uncertainty, and reports unstable/oscillatory spectral reconstructions for tested methods. It does not provide an explicit retarded/in-in or `Disc_s` prescription for the required linked object.

The paper also focuses on graviton-mediated `s,t,u` channels while neglecting the direct contact term `A4`; it notes that the forward divergence requires that contact contribution. Thus even the scalar amplitude is not a complete forward source/contact-completed object.

## Classification

Retain:

`BLOCKED_AS_REALTIME_RELATION_COMPLETION`

`BLOCKED_NOT_ZERO`

Sharpen to:

`BLOCKED_AS_LINKED_RETARDED_DISCONTINUITY_MAP_DESPITE_PHYSICAL_SCALAR_AMPLITUDE`

New labels:

- `AS-NG-006` — same-construction physical Lorentzian scalar amplitude exists;
- `AS-NG-007` — its timelike reconstruction does not certify the frozen retarded discontinuity;
- `REL-NG-014` — scalar scattering cannot replace the linked nonlinear graviton observable;
- `AS-BLOCK-002` — remaining gap is linked retarded/discontinuity/source-Ward completion;
- `NG-FUNNEL-090` — stronger comparator authority without observable identity is not novelty.

This is not a consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, or a zero AS comparator column.

No heavy computation was launched. No Candidate Gravity residual. No `ANSATZ-003`. No Fisher/resources.

MODEL_READINESS: 24%

Readiness change: 0 percentage points. Comparator foundation remains `24/25`; robust unique residual remains `0/20`. The AS authority boundary is narrower but the comparator coordinate is not closed.

Next gate: audit whether a same-parent AS Lorentzian nonlinear three-graviton quantity with explicit retarded/spectral discontinuity and a normalization link to the two-point sector exists. If not, freeze AS at the sharpened blocker and move primary effort to an executable linked nonanalytic comparator branch.
