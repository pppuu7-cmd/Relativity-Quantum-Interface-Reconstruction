# RQIR Research Log — Iteration 202

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Starting point

Iteration 201 froze a cross-polarization anti-overfitting gate on v3-A and v3-B. The supported local C5 zero-K2 soft2 nuisance was rank 4/12 in each protocol because the comparator was truncated at dimension 12.

## New question

Is that finite complement stable against the higher local derivative tower already suggested by the Iteration-178 `RiemannChain Box^n` construction?

## Exact arbitrary-n soft identity

At cubic order around flat space, for the covariant Riemann-chain derivative family, `Box^n` acts on one linearized curvature. In the null-soft protocol:

- if it acts on the soft leg, `k_soft^2=0` and the term vanishes;
- if it acts on either hard momentum eigenmode, it gives `(-q^2)^n`;
- four of six permutations survive.

Therefore

`v_0(i)=r_i`,

`v_n(i)=(2/3) r_i (-x_i)^n`, `n>=1`.

Iteration 178 explicitly verified this for n=1,2,3; the operator argument contains no n-specific step.

## Rank theorem

For N distinct hard nodes and nonzero base carrier r_i, the first N columns are row-scaled Vandermonde and have exact rank N.

Both frozen v3-A and v3-B have 12 distinct x values and 12 nonzero base carriers.

High-precision 12-column determinants:

- A: `3.6219999948776965700299598809683147035e-56`;
- B: `-3.2101534944510024202218188366614935333e-54`.

The double-precision rank eventually appears to drop because the high-power basis is catastrophically ill-conditioned; the exact determinant is nonzero.

## Immediate consequence

The dimension-12 rank-4 complement is a scoped truncation result, not a model-independent C5 complement. Dimension 14 already raises the family rank to 5; dimension 16 to 6; extending through Box^11 gives exact rank 12 on each 12-row protocol.

The largest frozen v3 node is x=0.994896, so higher powers are not suppressed by x over that row: x^11≈0.94527. No Wilson/remainder bound currently authorizes ignoring them.

## Literature guardrail

- Donoghue 1994: gravitational EFT separates controlled low-energy effects from unknown short-distance local terms; nonanalytic massless effects are the universal low-energy content.
- Ruhdorfer–Serra–Weiler 2020: nonredundant gravitational EFT operators can be constructed at arbitrary dimension and extended systematically to all orders.

Do not overclaim that every displayed Box^n representative is independently nonredundant after every 4D identity. The RQIR conclusion is the need for EFT truncation/remainder control before finite analytic residual promotion.

## Retained results

- `C5-NG-019` local derivative tower finite-row saturation;
- `REL-NG-015` dimension-12 complement is scoped only;
- `NG-FUNNEL-057` require EFT remainder control or noninterpolable linked observable;
- `READINESS-CORR-001` reopen one comparator-foundation point.

## Readiness

`MODEL_READINESS: 23%`, down from 24%.

Reason: the comparator foundation was previously credited using a finite C5 cutoff whose omitted local analytic remainder is not controlled over the current v3 energy range.

## Next gate

Iteration 203: shared-Wilson v3-A+v3-B derivative-tower quotient. Common physical Wilson coefficients must fit both protocols simultaneously. This may leave cross-polarization relations even though each protocol separately is finitely interpolable. Full all-orders C5 tensor remainder remains open.
