# RECOVERY DELTA — ITERATION 440

**Status:** prospectively frozen and launched; raw result pending.  
**Authority target:** Iteration-270 `Acoef/Asub` 80/120-digit signed-assembly arithmetic closure only; non-promoting.  
**MODEL_READINESS:** 24%.

## Preconditions consumed

- Iteration 438 raw-valid PASS: exact `A_finite` arithmetic core closed across all 26 signed nodes.
- Iteration 439 raw-valid diagnostic PASS: signed `Acoef` assembly is strongly cancellation-conditioned, with maximum componentwise amplification `1790391356.9083405`; this is diagnostic only, not a physical ceiling.
- Physical index 2 remains blocked by Iteration 421 and is not changed here.

## Frozen Iteration 440 contract

Object:

`Acoef = sum_sigma prod(sigma) A_finite(sigma*h)/(2h)^n`, identical to Iteration 270 `Asub`.

Inputs and steps are unchanged:
- `M=POS`, `p=P0`;
- `h1=1e-4`, `h2=5e-4`, `h3=1e-3`;
- seven nonempty subsets, 26 signed nodes total;
- 80 and 120 decimal digit evaluations use the raw-valid Iteration-438 `A_finite_mp` implementation.

Acceptance frozen before result:
- max scaled 80-vs-120 `Acoef` discrepancy `<=1e-30`;
- finite outputs;
- exact 26-node / 7-subset census.

Binary64-vs-120 discrepancy is diagnostic only. PASS does not certify finite-difference truncation or downstream physical authority.

## Launch provenance

Code commit: `a1b62afb4936d98b069280d25975fd09cade3a25`.  
Workflow commit: `c84a9991c8d11c5d863d7f8b39bd01e5eeb4d5f9`.  
GitHub Actions run: `33904321843` (queued immediately after workflow creation).

## Guardrails

No step reduction, no parent-dynamics change, no threshold weakening, no zero fill. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. Physical index 2 and Iteration 412 exact15 remain BLOCKED pending full precision/representation closure.
