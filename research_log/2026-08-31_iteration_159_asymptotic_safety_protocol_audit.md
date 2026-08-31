# RQIR Supplemental Audit — Iteration 159

**Date:** 2026-08-31  
**Role:** supplemental numerical check of authoritative `AS-FRG-TT-001`, not a separate comparator iteration  
**AUTHORITATIVE MODEL_READINESS: 22%**

## Reconciliation note

This file was created manually while the hourly automation was simultaneously completing the authoritative Iteration 159. The automation committed `AS-FRG-TT-001`, `recovery/RECOVERY_DELTA_ITERATION_159.md`, and advanced `CURRENT_QG_FRONT.md` first.

Therefore:

- authoritative comparator id: `AS-FRG-TT-001`;
- authoritative Iteration-159 readiness: **22%**;
- this file adds only a numerical kinematic mismatch certificate;
- it creates no additional comparator-foundation credit and must not be interpreted as `23%` readiness.

## Supplemental finite-protocol audit

The six frozen RQIR probes use general off-shell triplets `(p,-q,-r)`, while the published scalar TT dressing used in the Pawlowski–Tränkle reconstruction is evaluated at momentum-symmetric configurations.

Squared leg virtualities and relative spreads:

1. `(0.7473,0.5076,0.3313)`, spread `0.7867860`;
2. `(0.6157,0.3854,0.2935)`, spread `0.7466399`;
3. `(0.4418,0.4260,0.2746)`, spread `0.4390756`;
4. `(0.6120,0.3153,0.2773)`, spread `0.8335547`;
5. `(0.6682,0.4004,0.2278)`, spread `1.0191299`;
6. `(0.4239,0.2882,0.2321)`, spread `0.6094048`.

Symmetric-compatible probes: `0/6`.

Thus the direct insertion of the one-variable symmetric-point TT dressing into the six frozen general off-shell triplets is quantitatively unjustified.

Reproducible files:

- `analysis/asymptotic_safety_protocol_audit_iteration159.py`;
- `results/asymptotic_safety_protocol_audit_iteration159.json`.

## Interpretation

This supports, rather than replaces, the authoritative Iteration-159 result:

`BLOCKED_OFF_SYMMETRIC_RETARDED_VERTEX_MAP`.

It is not a consistency FAIL of asymptotic safety and no unavailable comparator row is set to zero.

## Readiness

**MODEL_READINESS: 22% (authoritative, unchanged).**

No point is added because this supplemental audit improves provenance/quantification but does not produce a usable six-probe AS retarded tangent.
