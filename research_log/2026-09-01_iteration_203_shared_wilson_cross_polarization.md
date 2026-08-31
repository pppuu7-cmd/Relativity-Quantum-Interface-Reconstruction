# RQIR Research Log — Iteration 203

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Starting point

Iteration 202 reopened the C5 comparator truncation gate: the local Riemann-chain derivative tower can interpolate either frozen 12-row polarization protocol separately when extended to sufficiently high Box power.

## Physical correction

C5 Wilson coefficients belong to one theory and must be identical across v3-A and v3-B. Therefore stack the two protocols and use common coefficients.

For the declared tower:

`S_A(i)=r_A(i) f(x_i)` and `S_B(i)=r_B(i) f(x_i)`.

Hence twelve exact family relations hold:

`r_B(i) S_A(i)-r_A(i) S_B(i)=0`.

## Numerical certificate

The Box^0...Box^11 common-coefficient matrix has shape `24x12` and rank `12`.

Left-null dimension: `12`.

The explicit 12 relation rows have rank `12` and annihilate the tower at max absolute numerical error `9.03e-16`.

Condition number of the 12-column stack: `9.15e12`; exact relation and finite-noise usability remain separate issues.

## Retained results

- `REL-NG-016` — twelve exact cross-polarization relations for the shared-Wilson Riemann derivative family;
- `C5-NG-020` — separate finite saturation does not imply shared-coefficient 24-row saturation;
- `NG-FUNNEL-058` — comparator Wilsons must be shared across settings.

## Limitation

Do not elevate these to full C5 null relations. All-orders gravitational EFT contains additional independent high-dimension tensor/derivative structures. Their polarization carriers have not been enumerated in the current source-completed null-soft protocol.

## Readiness

`MODEL_READINESS: 23%` — unchanged.

## Next gate

Iteration 204: enumerate/bound the additional all-orders C5 tensor carriers relevant to the cross-polarization soft2 observable, or design a controlled low-energy EFT-remainder protocol. AS and C3 authority work continues independently.
