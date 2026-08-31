# AS-PT-001 — Supplemental Numerical Audit Alias

**Frozen:** 2026-08-31  
**Authoritative comparator:** `AS-FRG-TT-001`  
**Primary authority:** Pawlowski & Tränkle, Phys. Rev. D 110, 086011 (2024), arXiv:2309.17043  
**Status:** SUPPLEMENTAL_AUDIT_ONLY / NOT_A_SEPARATE_COMPARATOR

## Reconciliation

This file was created manually in parallel with the hourly automation. The automation completed the authoritative Iteration 159 first and froze `AS-FRG-TT-001`. Therefore this document is retained only as a quantitative kinematic audit of the same Pawlowski–Tränkle truncation.

It must not be counted as an additional comparator or as additional model-readiness credit.

## Supplemental result

The published completely TT reconstruction uses momentum-symmetric n-point configurations,

`Gamma_tt^(n)(p_vec)=gamma_g^(n)(p) T_R,tt^(n)(p_vec)`.

The six frozen RQIR off-shell triplets `(p,-q,-r)` are strongly non-symmetric. The relative spreads of `(p^2,q^2,r^2)` are

`[0.7868,0.7466,0.4391,0.8336,1.0191,0.6094]`.

Hence:

- minimum spread: `0.4390756302521009`;
- maximum spread: `1.0191298981795742`;
- symmetric-compatible probes: `0/6`.

This quantitatively supports the authoritative `AS-FRG-TT-001` blocker: the symmetric-point TT dressing is not itself the general six-probe off-shell retarded tangent.

## Causal boundary

The 2024 work reconstructs a Euclidean covariant effective action and performs a Wick rotation for its black-hole application. That operation does not by itself specify the source-completed in-in/CTP retarded three-point prescription required by RQIR.

Recent Lorentzian spectral/scattering developments remain contextual only and are not spliced into this comparator across different truncations.

## Authorities

- authoritative comparator: `candidate_gravity/comparators/AS-FRG-TT-001.md`;
- reproducible supplemental audit: `analysis/asymptotic_safety_protocol_audit_iteration159.py` and `results/asymptotic_safety_protocol_audit_iteration159.json`.

**MODEL_READINESS: 22% (authoritative Iteration 159; unchanged by this supplemental audit).**
