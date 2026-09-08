# Recovery Delta — Iteration 592

Date: 2026-09-08

## Authoritative change
Iteration 592 raw-validates the analytic-origin class of the same-action MSSC K1^3 tree family.

Canonical provenance:
- run `34214083326`
- job `102021606620`
- head `57b3a430abe387376376bd559c7f66cd7fa230f4`
- artifact `10051001153`
- digest `sha256:d3d0e4e4e57bbe047dc8019bd159d3434118542b4c28696a88692e97ac9f7c21`
- result SHA256 `f2765720fddaf578df48bfaf40820c66412282f81968d4ad77a04a940aac94a6`
- authority audit SHA256 `34eeaed0819efe1bd8942052acd3b67d119f9b795899cf5b04991c6b303c20eb`
- failures `[]`

## Scientific result
K1 is polynomial and each internal same-action scalar propagator is meromorphic rational `1/(m^2-p^2)`. Hence the finite K1^3 tree has no ordinary finite hard-channel branch cut away from scalar poles. The exact fixture remains nonzero in all three singleton roles; minimum internal `|K0|` is respectively `0.24`, `0.145`, `0.005`, so the sampled authority is not on a scalar pole.

Scoped classification:
`PASS_K1CUBED_MEROMORPHIC_ORIGIN__LINKED_T_CUT_PROJECTION_BLOCKED__NON_RESIDUAL`.

## Blocker
The remaining issue is not numerical support but an observable-definition prerequisite. A retarded/Feynman scalar pole has a distributional discontinuity, while the frozen Candidate-Gravity linked `T_cut` belongs to the native split-invariant `Y=(K2,S_soft2_full)` observable. Repository authority does not yet provide an explicit source-to-native-linked distributional map identifying or excluding those scalar-pole terms.

Therefore:
- `K1cubed_under_frozen_linked_T_cut = BLOCKED__NEEDS_EXPLICIT_SOURCE_TO_T_CUT_DISTRIBUTIONAL_MAP`;
- six K1/K2 terms are NOT yet authorized as the complete discontinuity-bearing source block;
- K1^3 remains retained in the full same-action source Ward tree;
- Source/Born subtraction remains NOT_PERFORMED.

## Exact next gate
Construct/freeze the matched source-to-native-linked-observable distributional map. It must state how MSSC scalar pole terms project (or provably do not project) into the existing `Y/T_cut` protocol without importing unrelated on-shell Born subtraction. Only after this map exists can the full source-Ward response be projected into Iter582/comparator space.

No other heavy numerical model gate is presently authorized by current repo authority without first supplying that mapping; launching blind heavy C5 or residual/Fisher work would violate frozen guardrails.

MODEL_READINESS: 24%.
