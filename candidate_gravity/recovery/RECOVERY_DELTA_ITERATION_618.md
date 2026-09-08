# RECOVERY DELTA — Iteration 618

Date: 2026-09-08

## Authoritative result

`PASS_ITER618_SIX_ROOT_PROJECTIVE_SOURCE_SHAPE_CERTIFICATE__N_NATIVE_INVARIANT_NON_RESIDUAL`

Iteration 618 extracts the maximal simple projective information from Iter615 that is invariant under the one common nonzero `N_native` left BLOCKED by Iter617.

## Frozen ordering and anchor

- roots remain separate and are ordered by strict ascending Iter614 `s`;
- the anchor is the smallest-s root `D_b^-(0.013028588574858)`, chosen by pre-existing kinematics rather than coefficient magnitude;
- no roots are summed by q2 bucket.

Five independent ratios to the anchor:

1. `D_s^-(0.09) / D_b^-(0.013028588574858) = -2.966563737084728`;
2. `D_a^-(0.09868572571657197) / anchor = -0.7800526753639322`;
3. `D_a^+(1.241314274283428) / anchor = -5.158207913624242`;
4. `D_b^+(1.726971411425142) / anchor = +2.997420912767025`;
5. `D_s^-(2.89) / anchor = +8.57973421373656`.

Raw source sign pattern in ascending-s order: `[-,+,+,+,-,-]`.

Projective scale-invariance regression under common multipliers `2.5`, `-3`, `+i`, `2-1.5i` has maximum ratio drift `8.881784197001252e-16`.

## Fail-closed role

Any future native bridge claiming one common `N_native` must preserve these ratios root-by-root. Ratio drift is projection/implementation corruption, not a physical residual, and blocks Source/Born subtraction and comparator quotient.

## Reproducibility

- code: `candidate_gravity/code/iteration618_six_root_projective_source_shape_certificate.py`
- result: `candidate_gravity/results/iteration618_six_root_projective_source_shape_certificate.json`
- log: `candidate_gravity/research_log/2026-09-08_iteration_618.md`

`N_native` remains BLOCKED. Source/Born subtraction remains `NOT_PERFORMED`; comparator quotient remains blocked; no ANSATZ-003; no Fisher/resources.

MODEL_READINESS: 24%

Readiness change from Iter617: `0 pp`.
