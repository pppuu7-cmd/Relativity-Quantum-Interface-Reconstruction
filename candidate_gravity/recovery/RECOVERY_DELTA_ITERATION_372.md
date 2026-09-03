# RQIR Candidate Gravity Recovery Delta — Iteration 372

Date: 2026-09-04

MODEL_READINESS: 24%

## Validated authority

Iteration 372 raw artifact was independently downloaded and inspected; green workflow status alone was not used as scientific authority.

- workflow: `rqir-iteration372-tru1sq-timelike-cut-support-topology`
- run: `33807434918`
- job: `100821143369`
- artifact: `9913468040`, `iteration372-result`
- artifact digest: `sha256:430936e6bbfc0cb374ab0db0d79f7082a6364d1e99317836a0ea6b20c72898ee`
- raw scientific JSON SHA-256: `10938d2749dfd437c9385b68540a23dbb8a5fde4eb77c60ce60e97777a740bc4`
- authority-audit JSON SHA-256: `56756aa50e3342f93a1acd6d941188c3140bc19c3821d1ad104cc4ca117c45e4`
- workflow head: `16c262b221c5d02cb5a6c6129e4e1cb6fca96a3b`

Authority:
`PASS_TRU1SQ_21_PHYSICAL_FAMILIES_TIMELIKE_CUT_SUPPORT_AND_SINGULARITY_TOPOLOGY`.

## Scientific result

Across the 21 physically distinct `Tr U1^2` families there are 57 timelike two-line channels, exactly 19 for each of `q^2=-1`, `q^2=-0.34`, and `q^2=-0.14`.

Singularity census:
- `simple-simple`: `6` total = `2` per q^2;
- `simple-double`: `36` total = `12` per q^2;
- `double-double`: `15` total = `5` per q^2.

Thus only 6/57 channels are eligible for the ordinary-simple regularity/separation gate. The remaining 51 channels contain at least one physical double pole and ordinary-simple Cutkosky substitution is forbidden for them. This gate performs no discontinuity integral and produces no candidate residual.

## Anti-idle continuation

Iteration 373 was created and launched immediately for only the six simple-simple channels. It reuses the frozen physical routed integrand/denominator families, analytically certifies every uncut denominator group on the exact massless cut sphere, and tests the stripped physical numerator by a symmetric two-shell radial limit. Double-pole channels are excluded.

- code commit: `e16d24d56e3e2df838667fabaf9e384ef5904be5`
- workflow head: `0e4790fc220f698482b08832f9436e3ec2b59868`
- run: `33811317505`
- job: `100833556196`
- status at recovery write: `in_progress`

## Guardrails

Unsupported remains `BLOCKED`, never zero-filled. Physical multiplicity-two factors remain double poles by Iteration 371. No ordinary-simple formula may be applied to simple-double/double-double channels. No Source/Born subtraction, `ANSATZ-003`, Fisher/resources, or blind heavy full-C5.

## Exact next gate

Consume Iteration 373 raw artifact. If all six channels are `REGULAR`, perform a normalized q2-resolved simple-simple `Tr U1^2` discontinuity using frozen normalization conventions. In parallel/downstream, generalize and validate the auxiliary-mass derivative/distributional bridge for exact simple-double and double-double multiplicities before any integration of the remaining 51 channels.

Authoritative iteration: 372.
MODEL_READINESS: 24%
