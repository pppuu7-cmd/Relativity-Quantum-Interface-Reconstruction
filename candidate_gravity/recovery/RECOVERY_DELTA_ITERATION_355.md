# Recovery Delta — Candidate Gravity Iteration 355

Date: 2026-09-03

## Scope

Held-out physical traced numerator transport for every multi-member denominator-translation candidate from Iteration 354, using additive propagator-stripped subterms and the frozen Iteration-352 physical providers. Negative numerator equivalence is preserved as a scientific result; denominator equivalence alone never merges families.

## Raw Actions authority

- authoritative run: `33788922786`
- artifact: `9906532014` (`iteration355-result`)
- artifact digest: `sha256:8eb3e0f4400be8ba53d8c7055e87601d33160ceb556729170fb8e82eb6b9cac0`
- scientific JSON SHA-256: `6f2f031ef4cd6200d4592e8f85cc4bedec037140d2163c3f77c7612eb1eea50f`
- workflow head: `7f59b657da732de10b702e1c673651dcf0ad2bfc`

Raw artifact contains exactly one Iteration-355 object and `scientific_authority_pass=true`.

## Result

- additive subterms: `42`
- denominator candidate classes: `30`
- multi-member denominator candidates: `9`
- held-out loop momenta: `4`
- numerator-equivalent multi-member classes: `0`
- numerator-distinct multi-member classes: `9`
- max stripped-factor reconstruction scaled error: `1.6978418670987586e-15`
- fixed reconstruction threshold: `2e-10`
- fixed numerator-transport threshold: `2e-10`
- max observed numerator-transport scaled mismatch: `0.004476953018918176`

Authority:

`PASS_U2_HELDOUT_PHYSICAL_NUMERATOR_TRANSLATION_TRANSPORT_CLASSIFICATION__ONLY_PROVEN_EQUIVALENCES_MERGED`.

No multi-member denominator candidate may be merged. Therefore the physical additive U2 family partition remains 42 distinct subterms.

A second same-gate run `33788975824` was triggered by workflow-registration timing and completed successfully; it is redundant and is not used to create additional authority.

## Next gate

Classify the 42 distinct numerator+denominator families by kinematic origin and propagator topology: local/scaleless/rational versus cut-capable, including repeated-pole structure. Do not integrate cuts until this origin classification is frozen.

MODEL_READINESS: 24%
