# RECOVERY DELTA — Iteration 644

Date: 2026-09-09

Authoritative predecessor: Iter643 external-tensor trajectory operational/provenance BLOCKED.

## New scientific authority

Iteration644 first proves that the missing continuation is not uniquely determined by Lorentz covariance plus the exact Iter368/588 anchor. The same-parent anchor tensors are arbitrary symmetric metric probes generated with RNG seed 319 and scale 0.12; they are not TT/on-shell graviton polarizations, so no new transversality/tracelessness/unit-normalization condition may be imposed.

For fixed `t0=0.14,u0=0.34`, use the exact anchor-connected canonical momentum family

- `q_s=(sqrt(s),0,0,0)`;
- `E_a=(u0-s-t0)/(2*sqrt(s))`;
- `q_a=E_a e0 + sqrt(E_a^2-t0) e1`, `e1=(0,1/sqrt(2),1/sqrt(2),0)`;
- `q_b=-q_s-q_a`.

It exactly recovers the Iter368 momenta at `s0=1` and preserves the three invariants and momentum closure through the ordinary-cut region `s>=1.96`.

A common O(2) spatial rotation about `e1` stabilizes all three momenta. Therefore any smooth `theta(s)` with `theta(1)=0` produces another covariant anchor-matched tensor trajectory. At `s=2`, `theta=1` preserves the Lorentz metric to `1.11e-16` and momenta to `5.55e-17`, while changing all three generic anchor tensors by O(0.16–0.18). Thus covariance+anchor have at least one arbitrary function of residual continuation freedom.

This residual freedom is not called regime-specific non-identifiability: it is pre-measurement observable-definition non-uniqueness.

## Frozen prospective contract

Before any numerator-weighted cut value is inspected, Iter644 freezes

`MSSC001-CLOSED-GAMMA3-TENSOR-TRANSPORT-V1`:

zero transverse twist in the canonical q_s-rest-frame fixed scattering-plane tetrad, with all tetrad components of each exact Iter368 metric probe held fixed. In the exact Iter368 coordinate frame this implies `h_s(s)=h_s(1)`, `h_a(s)=h_a(1)`, `h_b(s)=h_b(1)`. This is now an explicit versioned observable definition, not a post-hoc shortcut.

No gauge, transversality, tracelessness, or new unit-normalization condition is added. Tensor symmetry and fixed anchor tetrad components are retained.

Classification:
`PASS_ITER644_PROSPECTIVE_EXTERNAL_TENSOR_TRANSPORT_V1__COVARIANCE_ALONE_NONUNIQUE__ZERO_TWIST_TETRAD_COMPONENTS_FROZEN__NON_RESIDUAL`.

Reproducibility:
- `candidate_gravity/code/iteration644_external_tensor_transport_contract.py`
- `results/iteration644_external_tensor_transport_contract/result.json`

Strict interpretation: protocol/observable-definition PASS plus a preserved negative non-uniqueness result. Not Candidate-Gravity consistency FAIL/PASS, exact comparator identity, regime-specific non-identifiability, near-degeneracy, novelty statement or Candidate residual.

Guardrails unchanged: all 13 families retained; K3 analytic/contact; ordinary K1/K2 and K1^3 support remains `s>=1.96`; `zero_fill=false`; Candidate values unused; Source/Born subtraction `NOT_PERFORMED`; native Y/T_cut projection `NOT_PERFORMED`; fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient `NOT_PERFORMED`; no `ANSATZ-003`; no Fisher/resources.

MODEL_READINESS: 24%
Readiness change: 0 percentage points. Tensor-trajectory authority is now frozen prospectively, but robust unique residual remains `0/20` and no complete readiness-rubric sector closes.

Exact next gate — Iteration645: evaluate the numerator-weighted ordinary retarded s-channel cut densities family-by-family using only Iter594 vertices, Iter627/632 SK/state authority, Iter640/641 cut support/projector and `MSSC001-CLOSED-GAMMA3-TENSOR-TRANSPORT-V1`. K3 remains analytic/contact. Native projection, Source/Born subtraction, comparator quotient, ANSATZ-003, Fisher/resources remain downstream/forbidden.
