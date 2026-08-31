# Recovery Delta — Candidate Gravity Iteration 140

**Date:** 2026-08-31  
**Authoritative front:** Iteration 140

## If resuming from another chat

Read first:

1. `candidate_gravity/recovery/CURRENT_QG_FRONT.md`;
2. `candidate_gravity/MODEL_REGISTRY.md`;
3. `candidate_gravity/models/ANSATZ-RQIR-KL-002/MODEL.md`;
4. `candidate_gravity/models/ANSATZ-RQIR-KL-002/GATE_STATUS.yaml`;
5. `candidate_gravity/models/ANSATZ-RQIR-KL-002/COMPARATOR_STATUS.md`;
6. `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`.

## Frozen negative controls

### `ANSATZ-PQG-EFT-001`

Reference C5, not promotable due exact theory-class degeneracy.

### `ANSATZ-RQIR-CTP-001` v0.1

REJECTED. Do not modify/revive.

Analytic reason:

`F(y)=-y exp(1-y)E1(1-y)` is strictly decreasing from 0 to `-infinity` on `0<y<1`; every `beta>0` forces one sub-threshold root of `1+beta F`, with negative relative residue factor.

Authority:

`docs/CANDIDATE_GRAVITY_LORENTZIAN_ITERATION136.md`.

## Active model

`ANSATZ-RQIR-KL-002` v0.1.

Spectral measure:

`rho_g(mu^2)=delta(mu^2)+(beta/M_*^2) exp(1-mu^2/M_*^2) Theta(mu^2-M_*^2)`.

Linear conserved-source tensor exchange:

massless:

`T.T'-(1/2)TT'`,

continuum massive spin-2:

`T.T'-(1/3)TT'`.

Static result:

`Phi=-GM/r[1+(4/3)beta W(M_*r)]`,

`0<W(u)<=exp(-u)`.

Cross-channel result:

traceless-probe continuum response is `3/4` of the NR-calibrated continuum response in the frozen linear tensor normalization.

## Current C5 degeneracy theorem

For `x=q^2/M_*^2`, `|x|<1`,

`C(x)=int_1^infty ds rho_hat(s)/(s+x)=sum_{n>=0}(-x)^n A_(n+1)`.

Therefore at any fixed finite derivative order the below-threshold beta effect is in the local EFT Wilson-coefficient span.

Retained result:

`CG-NG-005` — deep-IR finite-order measurements do not identify `KL-002` against C5 EFT.

Do not run Fisher/resource optimization in that regime.

## Existing-model audit available for article

Authorities:

- `candidate_gravity/landscape/RQIR_FUNNEL_AUDIT_ITERATION137.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_FUNNEL_SECTION_ITERATION137.md`.

These distinguish:

- internal consistency failure;
- novelty/comparator failure;
- operational blocking.

Do not describe an RQIR promotion failure as a global disproof of an existing theory unless the scope genuinely supports that claim.

## Exact next action — Iteration 141

1. Freeze a perturbative order for C5 including mandatory loop/nonanalytic response.
2. Define the tested candidate direction as `C5 baseline + beta excess spectral density`, with `beta=0` exactly C5 at that order.
3. Compare the excess threshold/tensor structure with:
   - hidden continuum mediators;
   - KK/DGP-like massive-spin-2 continua;
   - nonlocal/form-factor gravity;
   - stochastic/postquantum classical gravity at the two-point channel level.
4. Search for a residual linked observable involving at least two of:
   - NR `4/3` channel;
   - traceless `3/4` relation;
   - threshold absorption;
   - spectral/noise covariance.
5. Only if the residual direction is outside the exact comparator/calibration span, proceed to Paper-I finite quotient.

## Forbidden shortcuts

- Do not revive rejected `CTP-001` by flipping beta sign or changing its spectral shape inside v0.1.
- Do not call a deep-IR analytic continuum correction new physics relative to C5.
- Do not assume Vainshtein screening for `KL-002` v0.1.
- Do not call the positive spectral continuum novel before C4/C5/KK/nonlocal comparison.
- Do not optimize detector resources for an unidentifiable comparator-contained direction.
