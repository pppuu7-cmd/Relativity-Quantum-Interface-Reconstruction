# Recovery Delta — RQIR Iteration 237

Date: 2026-09-01

MODEL_READINESS: 24%

## New authority

Iteration 237 starts from authoritative Iteration 236 and audits the observable-identity gate for the executable minimally coupled GR massive-scalar radiative branch.

Fresh causal-response authority:
- Caron-Huot, Giroux, Hannesdottir, Mizera, JHEP 01 (2024) 139, arXiv:2308.02125 — generalized LSZ for asymptotic in-in observables and amplitude/product-of-amplitudes representation;
- Biswas, Parra-Martinez, JHEP 07 (2025) 037 — amputated causal response functions in the Schwinger–Keldysh basis;
- Bini et al., Phys. Rev. D 109, 125008 (2024) — gravitational waveform contains a five-point amplitude term plus a separate unitarity-cut term;
- Capatti, Zeng, Phys. Rev. D 111, 125002 (2025) — tested amplitude/worldline equivalence with retarded causal flow emerging after the appropriate cut/uncut combination.

## New status

The Iteration-236 shortcut is rejected:

`ON_SHELL_PROXY_NOT_OBSERVABLE_IDENTICAL`.

More precise blocker:

`BLOCKED_CAUSAL_RESPONSE_COMPLETION_REQUIRED_BEYOND_SINGLE_2TO3_UNITARITY_DISCONTINUITY`.

The published one-loop `2 -> 3` amplitude discontinuity is a calculable ingredient, but not by itself the complete in-in/retarded radiation observable. Generalized LSZ / Keldysh ordering requires additional cut/product-of-amplitudes contributions.

Therefore do not populate

`T_cut = D Gamma3_ret,soft - W[D K2]`

from the single `2 -> 3` unitarity discontinuity.

## New labels

- `REL-NG-017` — single in-out `2 -> 3` discontinuity is not the complete in-in retarded radiation observable;
- `REL-CUT-017` — generalized-LSZ causal-response authority identifies the missing amplitude-plus-cut completion;
- `REL-BLOCK-002` — frozen `T_cut` cannot be populated without explicit causal-response reconstruction;
- `NG-FUNNEL-093` — executable on-shell branch fails observable-identity gate without failing GR dynamics.

## Classification guardrails

This is not consistency FAIL, exact comparator identity, regime-specific non-identifiability, near-degeneracy, zero comparator column, or Candidate Gravity novelty.

## Candidate state

- robust Candidate Gravity residual: `NONE`;
- `ANSATZ-003`: `NOT_CREATED`;
- Fisher/resources: `FORBIDDEN`;
- heavy computation: not launched because causal observable completion remains an upstream hard constraint.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 236: 0 percentage points. The proxy-identity question is now resolved negatively, but comparator foundation remains `24/25`; robust unique residual remains `0/20`.

## Exact restart instruction

Iteration 238: construct or falsify a direct generalized-LSZ causal-response representation of the frozen linked observable in the same massive-scalar GR parent. Fix one Keldysh convention, retarded leg assignment, LSZ normalization, hard-channel discontinuity, contact/source Ward completion and IR subtraction. If the resulting in-in causal observable is structurally different from the frozen `Gamma3_ret - W[K2]` target, classify the branch as comparator-incompatible and do not redefine the target post hoc.