# RECOVERY DELTA — ITERATION 438

**Status:** raw-consumed PASS; parent arithmetic-core precision closure, non-promoting.  
**Classification:** `PASS_ITER270_A_FINITE_80_120_DIGIT_ARITHMETIC_CORE__NON_PROMOTING`  
**MODEL_READINESS:** 24% (unchanged).

## Raw provenance

Run `33901348951`, job `101115917242`, artifact `9947778073`, digest `sha256:52442233d7b721ef9196033dd392b02c6af4c5145e2b29bd79e7057466b24f1a`; raw scientific JSON SHA-256 `2c693cf1507f4c0e07fd6d587a479343b52a6c9d8d96b8c75103a6fa16a1a110`.

## Frozen object

The exact Iteration-270 arithmetic chain

`geometry -> action_covector + gamma_tensor + R_and_dR + lie_on_tensor -> A_finite`

was evaluated at all 26 signed finite-amplitude nodes entering the seven nonempty frozen `Acoef/Asub` subsets at unchanged `h1=1e-4`, `h2=5e-4`, `h3=1e-3`.

## Frozen acceptance and observed result

- max 80-vs-120 digit `A_finite` scaled discrepancy: `9.243186772758836e-84 <= 1e-40`;
- max binary64-vs-120-digit `A_finite` scaled discrepancy: `6.527324701910789e-19 <= 1e-9`;
- all values finite;
- exactly 26 nodes / 7 subsets.

Thus the individual `A_finite` arithmetic core is closed by an enormous margin. At this frozen scope it is not a material candidate for the downstream numerical blocker.

## Scientific consequence

The unresolved parent precision risk moves from individual finite-amplitude evaluation to the signed finite-difference assembly `Acoef/Asub`, where close `A_finite` values are combined with alternating signs and divided by powers of the frozen amplitude steps. Arithmetic precision and finite-difference truncation remain separate error sources.

Iteration 439 independently measures this signed-sum conditioning without assigning a physical pass/fail ceiling.

## Guardrails

No physical `D_s` promotion, no threshold weakening, no amplitude-step change, no parent-dynamics/routing/sign/normalization change, no zero fill, no `ANSATZ003`, no Fisher/resource claims.
