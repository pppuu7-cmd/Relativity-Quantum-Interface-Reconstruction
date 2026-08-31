# Recovery Delta — RQIR Iteration 172

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Previous front

Iteration 171 froze the linked/amputated CTP three-point protocol and showed that generic closed-unitary cubic dynamics obeys `Gamma_aar=0`, `Gamma_aaa=Gamma_arr/4` in the declared normalization.

## New authoritative result

On six frozen amputated kinematic rows, use raw coordinates `(Gamma_arr,Gamma_aar,Gamma_aaa,WardLock)`.

A conservative generic closed-unitary C4/C5 comparator is allowed one independent cubic amplitude per row while preserving the exact CTP relation and `WardLock=0`. Add only the fixed C3 PQCG tree response already supported by Iteration 155.

Raw comparator matrix: `24x7`, rank `7/7`, `s_min/s_max=0.0126780602`.

Relation map per row:

`R_aar=Gamma_aar`,

`R_unit=Gamma_aaa-Gamma_arr/4`,

`R_W=WardLock`.

All six generic closed-unitary quantum amplitude columns vanish under this map. The supported fixed C3 tree contributes one relation vector `R_unit=-B_EH/4`, norm `4.917063349196141`; supported relation rank is `1`.

## Retained results

- `CTP-NG-003 — GENERIC_CLOSED_UNITARY_C4_C5_REMOVES_ROW_LOCAL_CUBIC_AMPLITUDE_BUT_NOT_RELATION_VIOLATIONS`;
- `CTP-NG-004 — FIXED_PQCG_TREE_ADDS_ONE_EH_SHAPED_CLASSICAL_RELATION_DIRECTION`;
- `NG-FUNNEL-032 — WARD_LOCK_VIOLATION_IS_CONSISTENCY_FAIL_NOT_NOVELTY`.

## Blockers

- fixed C3 diffusion/MSR ordered `r/a` cubic completion: BLOCKED;
- C4/C5 loop/noise CTP three-point completion: BLOCKED;
- nonlinear real-time nonlocal/AS source-completed relation: BLOCKED.

Do not zero-fill these pieces. The current complement is therefore not a novelty certificate.

## Readiness

`MODEL_READINESS: 24%` — unchanged. The first relation-level rank certificate is closed, but robust unique residual remains `0/20` and parent Candidate Gravity dynamics remains absent.

## Exact restart instruction

Resume at **Iteration 173 — fixed PQCG diffusion/MSR ordered CTP completion**.

Derive the ordered cubic response-field vertices from the same PQCG parent action and parameter convention. If an extra stochastic/discretization convention is required beyond what is fixed by the comparator authority, record `BLOCKED_C3_CTP_ORDERED_COMPLETION` and move to the next fixed nonlinear nonlocal/AS relation. Do not create `ANSATZ-003`; do not run Fisher/resources.
