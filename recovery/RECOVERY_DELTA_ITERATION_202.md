# Recovery Delta — RQIR Iteration 202

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Previous front

Iteration 201 froze separate v3-A/v3-B cross-polarization validation, with a dimension-12 local C5 soft2 nuisance of rank 4/12 in each protocol and AS/C3 still BLOCKED.

## New critical result

The dimension-12 local-C5 complement is not stable without an EFT truncation/remainder bound.

For the declared Riemann-chain derivative family, the Iteration-178 soft identity extends to arbitrary n:

`v_0(i)=r_i`,

`v_n(i)=(2/3) r_i (-x_i)^n`, `n>=1`.

Reason: flat `Box^n` acting on the null soft curvature gives zero; acting on either hard momentum eigenmode gives `(-q^2)^n`; four of six cubic permutations survive.

For N distinct x_i with r_i nonzero, the first N columns are a row-scaled Vandermonde matrix and have exact rank N.

Both v3-A and v3-B satisfy the hypotheses for N=12.

High-precision determinant certificates:

- v3-A: `3.6219999948776965700299598809683147035e-56`;
- v3-B: `-3.2101534944510024202218188366614935333e-54`.

Thus the local analytic family can saturate each finite 12-row protocol when extended through Box^11. Severe numerical conditioning at high n does not change the exact rank statement.

## EFT-control problem

Current hard nodes include `x_max=0.994896`. At this row,

`x^4≈0.97974`, `x^8≈0.95989`, `x^11≈0.94527`.

Therefore omitted higher-derivative powers are not parametrically small over the full v3 range solely by powers of x. No declared Wilson-coefficient/remainder bound currently makes dimension 12 a model-independent approximation at the required precision.

General gravity EFT contains higher-dimension local operators to arbitrary order; a finite truncation is predictive only in a controlled low-energy/power-counting regime.

## Scope caveat

Do not claim every explicit `RiemannChain Box^n` representative is independently nonredundant after every 4D IBP/Bianchi/EOM identity. The robust conclusion is that the existing finite dimension-12 soft2 comparator cannot define a model-independent residual space without controlling omitted local analytic EFT directions.

## Retained results

- `C5-NG-019 — LOCAL_RIEMANN_CUBIC_DERIVATIVE_TOWER_CAN_SATURATE_ANY_FINITE_NULLSOFT_ROW_SET_WITH_DISTINCT_HARD_NODES`;
- `REL-NG-015 — DIMENSION12_RANK4_COMPLEMENT_IS_NOT_A_MODEL_INDEPENDENT_C5_RESIDUAL_SPACE_WITHOUT_EFT_REMAINDER_CONTROL`;
- `NG-FUNNEL-057 — FINITE_ANALYTIC_SOFT2_NOVELTY_REQUIRES_CONTROLLED_EFT_TRUNCATION_OR_A_NONINTERPOLABLE_LINKED_OBSERVABLE`;
- `READINESS-CORR-001 — C5_TRUNCATION_BLOCKER_REOPENS_ONE_COMPARATOR_FOUNDATION_POINT`.

## Readiness correction

`MODEL_READINESS: 23%`, reduced from 24%.

Breakdown:

- comparator foundation `23/25`;
- robust unique residual `0/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

This follows the frozen rubric rule that a newly discovered blocker may reduce readiness.

## Cross-polarization nuance

Physical C5 Wilson coefficients must be common across v3-A and v3-B. The single derivative family has only one coefficient per n on the 24-row vertical stack, so its stacked rank is at most 12. This motivates a shared-Wilson cross-polarization quotient rather than independent post-hoc fits.

## Exact restart instruction

Resume at **Iteration 203 — shared-Wilson cross-polarization derivative-tower audit**.

1. stack v3-A and v3-B vertically;
2. use the same coefficient for each local derivative operator in both protocols;
3. compute the rank and left-null structure of the Riemann-chain tower as n increases;
4. quantify which A/B relations this one-family tower can never absorb;
5. do not treat leftover directions as Candidate Gravity residuals because the full all-orders C5 tensor basis, AS and C3 remain incomplete;
6. in parallel design a controlled low-energy/remainder-bounded protocol or a linked nonanalytic/functional observable less vulnerable to finite analytic interpolation.

No `ANSATZ-003`. No Fisher/resources.
