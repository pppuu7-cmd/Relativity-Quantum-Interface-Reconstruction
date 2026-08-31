# NL-WNL-001 — Fixed Weakly-Nonlocal Comparator

**Frozen:** Iteration 158, 2026-08-31  
**Status:** PARTIAL_FIXED_COMPARATOR; full nonlocal cubic/CTP map remains BLOCKED

## 1. Role

This is the first fixed nonlocal/form-factor comparator in the Candidate Gravity funnel. It is not a Candidate Gravity ansatz and carries no novelty claim.

It exists to prevent a propagator-only or form-factor-only effect from being promoted as new gravity before the interaction potential and off-shell causal map are also fixed.

## 2. Frozen action convention

Use the weakly-nonlocal covariant structure

`S=-2/kappa^2 int sqrt(-g)[R + R gamma0(box) R + R_mn gamma2(box) R^mn + V]`.

For the scoped transverse-traceless linear sector freeze

`D_TT(k;sigma)=exp[-H(sigma k^2)]/(k^2+i0 k0)`

with

`H(z)=z^2`, `sigma0=1`.

This entire function is a deliberately fixed representative, not a preferred phenomenological form factor.

Freeze the local interaction-potential sub-block

`V=lambda_Ricci3 Tr(Ricci^3) + lambda_Riemann3 cyclic(Riemann^3)`.

Finite parameter vector:

`theta_NL=(log sigma, lambda_Ricci3, lambda_Riemann3)`.

## 3. Literature rationale

Weakly nonlocal gravity actions contain both nonlocal quadratic curvature form factors and a separate higher-curvature potential `V`. The potential starts at higher curvature order and therefore can change nonlinear vertices without changing the quadratic propagator.

Relevant anchors:

- Donà, Giaccari, Modesto, Rachwał & Zhu, JHEP 08 (2015) 038, arXiv:1506.04589;
- Briscese, Calcagni, Modesto & Nardelli, JHEP 08 (2024) 204, arXiv:2405.14056;
- Bas i Beneito, Calcagni & Rachwał, arXiv:2211.05606.

The 2015 amplitude/field-redefinition analysis also shows that broad Ricci-form-factor classes can share Einstein-Hilbert on-shell tree amplitudes while differing off shell. This is directly relevant to RQIR because the ordered retarded protocol is off shell.

## 4. Supported linear six-probe block

Use the six output momenta `p=q+r` already frozen in the Iteration-149 protocol and the same Gaussian window `(tau,L)=(0.8,0.6)`.

At `sigma=1`, the reference scalarized TT responses are

`[0.6416368934, 0.9691197992, 1.6339276996, 0.9648998132, 0.8164419290, 1.7608814202]`.

The `d/dlog sigma` tangent is

`[-0.7166536013,-0.7347604461,-0.6378436761,-0.7227948713,-0.7290683386,-0.6328298261]`.

A common response-gain column has rank `1`; adding `log sigma` raises the six-probe linear rank to `2`.

SVD:

`[3.3576236639554855,0.6000359203875203]`,

`smin/smax=0.17870850948216196`.

After projecting out common gain, the `log sigma` residual fraction is

`0.3996471300114534`.

Interpretation: the frozen nonlocal form factor produces a real finite shape direction in this known comparator. This is not a Candidate Gravity residual.

## 5. Supported nonlinear potential block

The two frozen potential derivatives are exactly the already computed and Ward-validated local C5 curvature-cubic response columns on the same six probes:

- `lambda_Ricci3` -> Iteration-150 `Ricci3_response`;
- `lambda_Riemann3` -> Iteration-150 `Riemann3_response`.

Their two-column rank is `2`.

Residual norms against the current C5 `R^3` span are numerical zero:

- Ricci3: `4.73e-16`;
- Riemann3: `1.91e-15`.

Thus these explicit interaction-potential directions do not enlarge the current nonlinear comparator span beyond C5.

## 6. Crucial BLOCKED sector

The same form factor that modifies the propagator also induces nonlocal cubic and higher vertices when the full covariant action is expanded. Those terms have **not** yet been derived in the frozen source-completed retarded convention.

Therefore:

- `form_factor_induced_chi2R`: BLOCKED;
- full Lorentzian nonlocal causal completion: BLOCKED;
- quantum-state `N2/C3sym`: BLOCKED;
- full nonlocal quotient: BLOCKED.

These entries must never be zero-filled.

## 7. Retained results

### `NL-NG-001 — FORM_FACTOR_DOES_NOT_FIX_NONLINEAR_RESPONSE`

Fixing the quadratic form factor does not fix the nonlinear RQIR response because independent higher-curvature potential coefficients are invisible at quadratic order.

### `NL-NG-002 — LOCAL_CUBIC_POTENTIAL_ALREADY_IN_C5_SPAN`

For the two explicitly frozen curvature-cubic potential directions, the nonlinear response is already contained in the current local C5 comparator span.

### `NG-FUNNEL-015 — FIX_PROPAGATOR_AND_INTERACTION_POTENTIAL_SEPARATELY`

A nonlocal gravity program or form-factor label is not a finite nonlinear comparator. RQIR must freeze the form factor, interaction potential, physical metric/source convention, and off-shell retarded map separately.
