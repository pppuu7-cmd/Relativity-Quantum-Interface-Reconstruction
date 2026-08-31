# Recovery Delta — RQIR Candidate Gravity Iteration 178

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Previous authoritative front:** Iteration 177  
**New local result:** dimension-12 local-C5 null-soft TT `B_T` completion has physics-aware rank 4.

## Source-of-truth files

- `analysis/c5_soft_transverse_dimension12_iteration178.py`
- `results/c5_soft_transverse_dimension12_iteration178.json`
- `candidate_gravity/C5_SOFT_TRANSVERSE_DIMENSION12_ITERATION178.md`
- `research_log/2026-08-31_iteration_178_c5_soft_transverse_dimension12.md`

## Frozen protocol

Do not change the six Iteration-177 rows:

`k1=eps*(1,0,0,1)`, `k2=q_i`, `k3=-q_i-k1`,

with the same soft plus-TT polarization, hard TT seeds and `eps` ladder.

All Iteration-178 operators start at cubic order around Minkowski, so operator-specific `K2=0` and `W[K2]=0`.

## New exact/scoped relations

For the null TT soft leg:

- `Rmn^(1)=0`;
- `Ricci3 B_T = 0`;
- `RicciChain Box^n B_T = 0`, `n=1,2,3`;
- `mixed RicciRicciRiemann B_T = Riemann3 B_T / 12`;
- `RiemannChain Box^n B_T = (2/3)(-q_i^2)^n Riemann3 B_T`, `n=1,2,3`.

Therefore the frozen nine-column local cubic set reduces to four independent physical columns across the six rows.

## Numerical guard

Blind SVD of extrapolated columns yields a fifth value `1.2254e-8`; the extrapolation discrepancy is `5.2626e-6`. Exact soft identities remove that fifth direction. Do not record rank 5.

Physics-aware rank: `4`.  
Physics-aware singular values:

`[2.0192478812, 0.0752839640, 0.0037576657, 4.7032262e-5]`.

Maximum pure-gauge soft-leg residue: `9.51e-23`.

## Retained results

- `C5-NG-009 — DIMENSION12_LOCAL_C5_NULL_SOFT_TT_BASIS_COMPRESSES_TO_RIEMANN_CHAIN_POLYNOMIAL_RANK_FOUR`.
- `SOFT-NG-005 — NULL_SOFT_TT_KINEMATICS_KILLS_RICCI_CHAIN_AND_REDUCES_DERIVATIVE_RIEMANN_DESCENDANTS_TO_HARD_Q2_MOMENTS`.
- `NUM-NG-001 — SUB_ERROR_SINGULAR_VALUE_MUST_NOT_BE_PROMOTED_WHEN_EXACT_KINEMATIC_IDENTITIES_REMOVE_IT`.

## Guardrails

The remaining two algebraic dimensions after local C5 alone are **not** Candidate Gravity residuals. C4, nonlocal, AS and C3 transverse/ordered comparator sectors are not complete and must not be zero-filled.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.

## Exact next gate

Iteration 179: audit fixed C4 compatibility with the null-soft TT `B_T` protocol. `C4-DRGT-001` is a nonzero-mass spin-2 comparator, so first determine whether the frozen null massless-soft relation is physically applicable at its fixed `m^2=0.04`. If not, record a protocol-incompatibility BLOCKED status rather than a zero column and freeze a compatible massless C4 control before quotienting.
