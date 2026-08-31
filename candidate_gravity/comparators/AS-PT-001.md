# AS-PT-001 — Fixed Asymptotic-Safety Vertex Comparator

**Frozen:** Iteration 159, 2026-08-31  
**Authority:** Pawlowski & Tränkle, Phys. Rev. D 110, 086011 (2024), arXiv:2309.17043  
**Status:** FIXED_TRUNCATION / RQIR_RETARDED_MAP_BLOCKED

## 1. Role

This is the first concrete asymptotic-safety comparator in the Candidate Gravity funnel. It replaces the program label `asymptotic safety` by one published vertex-expansion realization.

It is not a Candidate Gravity ansatz and carries no novelty claim.

## 2. Frozen truncation content

The comparator uses the fluctuation-vertex reconstruction of the diffeomorphism-invariant background effective action.

The published background action is expanded through second order in curvature while retaining full covariant momentum dependence in the form factors,

`Gamma[g] ~ int sqrt(g){ Rcal(Delta,R) + R f_R2(Delta) R + R_mn f_Ricci2(Delta) R^mn }`.

The underlying fluctuation calculation uses fully dressed graviton correlation functions in a vertex expansion. The 2024 reconstruction computes momentum-dependent three- and four-graviton couplings and reconstructs the effective action from them.

The specific TT projection used for the reconstruction parameterises the completely TT n-point functions at the momentum-symmetric point as

`Gamma_tt^(n)(p_vec)=gamma_g^(n)(p) T_R,tt^(n)(p_vec)`.

For the 3-point tensor/operator selection:

- `R^2` does not contribute to the TT graviton 3-point function;
- `R_mn R^mn` has nonzero TT 3-point overlap;
- therefore the `p^4` contribution to the symmetric-point TT 3-point can be assigned to the Ricci-squared form factor within the declared truncation.

## 3. Why this is a finite comparator

The model/truncation is fixed by:

- the explicit fluctuation-field vertex expansion;
- a specified TT projection;
- momentum-dependent wave function and Newton coupling avatars;
- curvature expansion through `R^2` and `Ricci^2` form factors;
- an explicit approximate Nielsen-identity map between fluctuation vertices and the diffeomorphism-invariant background action.

This is materially stronger than treating all asymptotic-safety theories as one unconstrained capability mask.

## 4. RQIR protocol-compatibility audit

RQIR uses six frozen off-shell triplets `(p,-q,-r)` with `p=q+r`.

The published scalar dressing `gamma_g^(3)(p)` used in the reconstruction is a momentum-symmetric-point object. Direct use on a general triplet would require at minimum equal leg virtualities at that symmetric point.

For the six frozen RQIR probes the relative spread

`(max(p^2,q^2,r^2)-min(p^2,q^2,r^2))/mean(p^2,q^2,r^2)`

is

`[0.7868,0.7466,0.4391,0.8336,1.0191,0.6094]`.

Thus:

- minimum mismatch: `0.4390756302521009`;
- maximum mismatch: `1.0191298981795742`;
- symmetric-compatible probes: `0/6`.

Consequently the published one-variable symmetric-point TT dressing cannot be inserted directly into the six-probe RQIR retarded tangent.

## 5. Lorentzian/causal boundary

The 2024 work reconstructs the Euclidean effective action and then Wick-rotates the effective action for its black-hole analysis. This is valuable but does not by itself provide the source-completed in-in/CTP retarded 3-point kernel on the six RQIR off-shell triplets.

Separate 2026 progress exists:

- Lorentzian graviton spectral functions and quadratic effective action have been computed directly in Lorentzian FRG (Assant, Litim & Reichert, arXiv:2606.19321);
- scalar-graviton three-point data have been analytically continued and used in scalar scattering (Chiesa, Pawlowski & Reichert, arXiv:2603.10168).

These are important feasibility evidence, but they are **not spliced into `AS-PT-001`**, because they are separate calculations/truncations and do not supply the missing pure-graviton source-completed 3-point kernel of this comparator.

## 6. Decision

`BLOCKED_OFF_SYMMETRIC_RETARDED_VERTEX_MAP`.

This is an operational comparator-instantiation boundary, not a consistency failure of asymptotic safety.

No missing entry is zero-filled.

## 7. Retained results

### `AS-NG-001 — SYMMETRIC_POINT_VERTEX_NOT_GENERAL_OFFSHELL_TANGENT`

A momentum-dependent graviton vertex computed at the symmetric point is not a finite general off-shell RQIR `chi2R` tangent when the measurement protocol uses non-symmetric triplets.

### `NG-FUNNEL-016 — FIXED_TRUNCATION_STILL_REQUIRES_KINEMATIC_AND_CAUSAL_MAP`

Replacing a broad theory class by a finite truncation is necessary but still not sufficient: the truncation must also supply the actual kinematic domain and retarded/CTP continuation required by the operational protocol before it can enter the quotient matrix.

## 8. Authorities

- Pawlowski & Tränkle, Phys. Rev. D 110, 086011 (2024), arXiv:2309.17043;
- Denz, Pawlowski & Reichert, Phys. Rev. D 98, 126002 (2018), arXiv:1612.07315;
- contextual Lorentzian progress only: Assant, Litim & Reichert, arXiv:2606.19321; Chiesa, Pawlowski & Reichert, arXiv:2603.10168.
