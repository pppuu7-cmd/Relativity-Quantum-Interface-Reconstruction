# Iteration 464 Recovery Delta

Date: 2026-09-05

## Entry authority
Latest completed numerical authority at entry is Iteration 463. Physical/operator authority remains Iteration 411. Physical blocker authority remains Iteration 421 with unresolved set `[2]`. Canonical rank-5 Actions run `33962417750` is still in progress and was not duplicated.

## New exact result
For frozen central4 nodes `(-2,-1,+1,+2)` and coefficients `(1/12,-2/3,+2/3,-1/12)`, exact rational moments through `k=9` are

`m0=0, m1=1, m2=m3=m4=0, m5=-4, m6=0, m7=-20, m8=0, m9=-84`.

Hence

`D_h f = f' - h^4 f^(5)/30 - h^6 f^(7)/252 + O(h^8)`

and for the tensor product

`D_uv,h F = F_uv - h^4(F_{5,1}+F_{1,5})/30 - h^6(F_{7,1}+F_{1,7})/252 + O(h^8)`.

The first product cross-term from the two `h^4` one-dimensional errors enters only at `h^8` as `+h^8 F_{5,5}/900`.

With `h_HALF=h_BASE/2`, isolated leading `h^4` and `h^6` truncation pieces have exact BASE/HALF ratios `16` and `64`, respectively. `(16 D_half-D_base)/15` is retained only as a diagnostic cancellation of a pure `h^4` term. It is explicitly forbidden as a promoted estimator: physical authority remains `ds=-d_base`; frozen BASE↔HALF threshold remains `<=2e-5`; assembled MP80↔MP120 threshold remains `<=2e-6`.

Classification: `PASS_CENTRAL4_LEADING_TRUNCATION_STRUCTURE__DIAGNOSTIC_ONLY_NON_PROMOTING`.

No consistency FAIL, comparator identity, non-identifiability, near-degeneracy, or novelty certificate is claimed. A future absence of exact 16/64 empirical scaling is not by itself a physics FAIL because mixed truncation orders/non-asymptotic terms can coexist.

`MODEL_READINESS: 24%`

Readiness change: 0 pp; no stable-rubric component was newly closed.

## Exact next gate
Raw-consume canonical run `33962417750` fail-closed at Iteration-455 distinct rank 5, `u=-5e-6, v=-5e-6`. No later mass coordinate may be launched before raw consumption.
