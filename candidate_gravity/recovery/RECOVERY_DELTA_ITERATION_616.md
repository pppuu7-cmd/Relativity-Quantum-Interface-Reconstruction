# RECOVERY DELTA — Iteration 616

Date: 2026-09-08

## Authoritative result

Iteration 616 narrows the Iter615 native-binding blocker without evaluating or fitting any projected Candidate value.

Classification:

`BLOCKED_ITER616_ENDPOINT_AMPUTATION_AND_Q2_BINDING_CLOSED__ONE_COMMON_NATIVE_NORMALIZATION_SCALAR_UNRESOLVED__NON_RESIDUAL`.

This is `BLOCKED`, not Candidate-Gravity scientific FAIL.

## Newly closed

- Exact q2 bucket identity is inherited from Iter588, which already bound the same Iter368 vectors under opposite metric signatures: source `(+1,+0.34,+0.14)` maps by mode identity to Iter582 `(-1,-0.34,-0.14)` as `s,b,a` respectively. Buckets remain distinct.
- External source endpoint convention is now explicit and exact:

  `S_amp^(3)=K0_out (d_abc G) K0_in`

  with

  `S_amp^(3)=-Kabc+sum_6(Ki G Kjk)-sum_6(Ki G Kj G Kk)`.

  Only the two common external scalar propagators are amputated. Internal scalar poles, K3 and all K1^3 chains remain retained; `zero_fill=false`.
- On the two frozen Iter594 probes, direct and termwise amputation agree to maximum absolute discrepancy `8.673617379884035e-19` from stored floating-point rounding.
- Relative source-sector factors/signs remain fixed by Iter589/594; scalar-pole distribution, native-s pullback and six nonzero source-side coefficients remain fixed by Iter608/613/614/615.

## Remaining blocker

The remaining source->Iter582 binding ambiguity is one common nonzero scalar `N_native`: the absolute cross-sector phase/normalization between the amputated MSSC source-response convention and the Iter582 connection effective-action/retarded native convention.

No historical authority currently supplies one explicit cross-sector equation fixing this scalar. It must not be inferred by fitting the six Iter615 coefficients or separately tuned per root/q2 bucket.

Source/Born subtraction remains `NOT_PERFORMED`. Comparator quotient remains blocked. No `ANSATZ-003`; no Fisher/resources.

## Reproducibility

- code: `candidate_gravity/code/iteration616_native_binding_endpoint_amputation_and_normalization_audit.py`
- machine result: `candidate_gravity/results/iteration616_native_binding_endpoint_amputation_and_normalization_audit.json`
- deterministic audit: `candidate_gravity/results/iteration616_native_binding_endpoint_amputation_and_normalization_audit_authority.json`
- stored result SHA256: `4420ed19c7ec5cc9100de56934350e7308a5f7e04af0a94daf2580812d86a07c`

## Exact next gate

Prospectively determine `N_native` from an independent lower-order/common-field normalization identity using the same physical metric perturbation and retarded/effective-action convention, without consulting any projected Iter615 Candidate value. If no such repository-supported identity exists, record that exact normalization as the minimal remaining blocker rather than choosing a convention post hoc.

Only a prospectively fixed `N_native` may authorize rerunning the full native `Y/T_cut` binding, followed later by Source/Born subtraction and the fixed comparator quotient.

MODEL_READINESS: 24%

Readiness change from Iter615: `0 pp`.
