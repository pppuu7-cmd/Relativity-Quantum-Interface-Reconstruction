# Research log — RQIR Candidate Gravity Iteration 238

Date: 2026-09-01

MODEL_READINESS: 24%

Started from repository authority at Iteration 237. Read `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_237.md`, the Iteration-237 research log, recent commits, and GitHub Actions state. Latest authority commit was `21439cf9ab8df318f94c4eeefaa635bfa19036d3`; no active workflow runs existed.

## Scientific action

Tested whether the full generalized-LSZ / Schwinger-Keldysh causal radiation observable in the minimally coupled massive-scalar GR branch is structurally identical to the unchanged frozen linked coordinate

`T_cut = D_s Gamma3_ret,soft - W[D_s K2]`.

Fresh authority used:
- Caron-Huot et al., JHEP 01 (2024) 139, arXiv:2308.02125;
- Biswas–Parra-Martinez, JHEP 07 (2025) 037, arXiv:2411.09016;
- Bini et al., Phys. Rev. D 109, 125008 (2024), arXiv:2402.06604.

Generalized LSZ correctly upgrades the in-out five-point amplitude to the causal in-in observable by adding the required cut/product terms. However, the resulting object remains a mixed five-point causal response with four massive-scalar legs and one metric/radiation leg, schematically `phi^4 h`.

Frozen RQIR `Gamma3_ret` is a pure-gravity three-metric response `h^3`, linked by the Ward/soft map to the same-parent metric two-point kernel `h^2`. Neither LSZ amputation, causal cut completion nor the soft graviton theorem changes external field species/valence. The lower-point soft factor is a matter scattering amplitude, not the metric inverse kernel `K2`.

Therefore the massive-scalar causal branch cannot populate frozen `T_cut` without an extra, independently derived source-reduction map converting `phi^4 h -> h^3` and `phi^4 -> h^2`. No such identity follows from the audited authority. Adding one ad hoc would redefine the comparator model/observable post hoc.

## Result

Freeze:

`CAUSAL_RESPONSE_BRANCH_PHYSICALLY_VALID_BUT_T_CUT_VALENCE_INCOMPATIBLE`

and

`BLOCKED_COMPARATOR_INCOMPATIBLE_FUNCTIONAL_VALENCE_MIXED_PHI4H_VS_H3_LINKED_H2`.

New labels:
- `REL-NG-018`;
- `REL-CUT-018`;
- `REL-BLOCK-003`;
- `NG-FUNNEL-094`.

This is a comparator-incompatibility / observable-identity negative result, not a consistency FAIL of GR, not exact comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a zero comparator column.

No heavy computation launched because exact observable identity fails upstream. No Candidate Gravity residual. No `ANSATZ-003`. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Readiness change from Iteration 237: 0 percentage points. Comparator foundation remains `24/25`; robust unique residual remains `0/20`. The branch is now correctly excluded from the promotable linked-cut path, but no readiness rubric block closes.

Next gate: Iteration 239 must look only for a native causal `h^3` linked to `h^2` branch in one declared physical convention, preferably perturbative Einstein gravity / gravity EFT formulated directly in Schwinger-Keldysh or causal-response language. Do not reuse matter `2 -> 3` radiation as a proxy and do not redefine `T_cut`.