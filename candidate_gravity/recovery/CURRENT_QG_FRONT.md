# Candidate Gravity Current Front

**Updated:** 2026-08-31  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **22%** under the frozen model-only rubric  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Rejected consistency control:** `ANSATZ-RQIR-CTP-001` v0.1  
**Positive-spectral Gaussian comparator:** `ANSATZ-RQIR-KL-002` v0.1  
**Active promotable ansatz:** none — intentionally withheld pending full fixed comparator quotient  
**Authoritative Candidate Gravity front:** **Iteration 158**

## Scientific state in one sentence

The fixed comparator funnel now contains concrete scoped C3 postquantum-classical, nonlinear dRGT C4, local quantum-GR EFT C5, and weakly-nonlocal form-factor blocks. Iteration 158 shows that a nonlocal form factor can generate a substantial finite linear-response shape after common-gain subtraction, but the propagator does not fix the nonlinear interaction sector: independent curvature-potential directions are invisible at quadratic order, and the two explicitly frozen cubic potential directions are already contained in the current C5 `R^3` span.

## Stable readiness rubric

Authority: `candidate_gravity/MODEL_READINESS_RUBRIC.md`.

Weights:

- comparator foundation: 25%;
- robust unique Candidate Gravity residual: 20%;
- frozen parent dynamics / ANSATZ: 20%;
- candidate consistency/positivity/Ward/causality: 15%;
- identifiability/Fisher: 10%;
- resource/experiment closure: 10%.

Formal baseline Iteration 157: `20%`.

Iteration 158: **`22%`**.

Current accounting:

- comparator foundation `19/25`;
- unique residual discovery `3/20`;
- parent dynamics `0/20`;
- candidate consistency `0/15`;
- Fisher `0/10`;
- resources `0/10`.

The earlier conversational estimate around 35–40% mixed infrastructure readiness with model readiness and is superseded by this stricter stable rubric.

## Frozen post-Gaussian protocol

Reduced coordinates after hard locks:

`z=(N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft2,tensor_geo,threshold)`.

Novelty pre-gate:

`rank([M,b]) > rank(M)`

or nonzero

`r_beta=(I-MM^+)b`,

only after fixed comparator/nuisance columns are derived and exact hard constraints removed.

Retained funnel rules now include `NG-FUNNEL-001` through `NG-FUNNEL-015`.

## C3 — fixed postquantum-classical comparator

### Linear noise

`N2=A(5D2+D0)`, `A=258.83104475297773`.

One scalar noise coordinate gives rank `1/2`.

Retain `C3-NG-001`.

### Nonlinear symmetric cumulant

From the same covariant PQCG Onsager–Machlup action

`S[g]=1/2 int sqrt(-g)[alpha R_mn R^mn-beta R^2]`,

with

`D2=1/(2alpha)`, `D0=1/[8(alpha-3beta)]`,

the six TT probes give

`C3sym_TT=B D2^2`, `B=-617.4340282011477`.

Thus

`V_C3=[[5A,A],[2BD2,0]]`

is rank `2/2` for all physical `D2>0`.

Retain `C3-NG-002` and `NG-FUNNEL-012`.

### Tree causal response

The same nonlinear Einstein drift gives nonzero

`chi2R=-G_R Gamma3_EH G_R G_R`,

but after hard calibration of the common GR/Newton coupling

`partial chi2R_tree/partial D2 = partial chi2R_tree/partial D0 = 0`.

Retain `C3-NG-003` and `NG-FUNNEL-013`.

Still BLOCKED: diffusion-dependent ordered/MSR-loop corrections, exact `chi2R_odd`, non-TT tensor completion, threshold and full C3 quotient.

## C4 — `C4-DRGT-001`

Frozen dRGT point:

`m^2=0.04`, `alpha3=0`, `alpha4=0`.

TT cubic interaction:

`V3_dRGT=m^2(3+alpha3)/8 Tr(H^3)`.

`alpha4` is blind at cubic TT order.

Tangent `(log m^2,alpha3)` is rank `2/2`, singular values

`[3.062684454379795,0.4175708275716087]`.

After the stronger shared-EH/gain quotient:

- `log m^2` residual fraction: `0.00126 ... 0.00320` -> **NEAR_DEGENERATE_NOT_PROMOTABLE**;
- `alpha3` residual fraction: `0.0472 ... 0.0694` -> **SCOPED_RESIDUAL_SURVIVES**.

Retain `C4-NG-001/002/003` and `NG-FUNNEL-014`.

Still BLOCKED: helicity-0/1, Vainshtein/nonperturbative response, `N2/C3sym`, alpha4 higher-point direction, full C4 quotient.

## C5 — perturbative quantum GR EFT

Retained scoped blocks:

- on-shell local `V_amp`: `12x10`, rank `10/10`, on-shell only;
- source-completed six-probe protocol: PASS_SCOPED;
- EH + `Ricci^3/Riemann^3` local retarded response: `6x2`, rank `2/2`, Ward validated.

Still BLOCKED:

- higher local directions;
- loop/nonanalytic directions;
- C5 `N2/C3sym` in the same finite CTP map.

## Nonlocal comparator — `NL-WNL-001` (Iteration 158)

Frozen weakly-nonlocal action structure:

`S=-2/kappa^2 int sqrt(-g)[R + R gamma0(box)R + Ric gamma2(box)Ric + V]`.

Scoped TT form factor:

`D_TT(k;sigma)=exp[-H(sigma k^2)]/(k^2+i0k0)`,

`H(z)=z^2`, `sigma0=1`.

Independent potential:

`V=lambda_Ricci3 Tr(Ricci^3)+lambda_Riemann3 cyclic(Riemann^3)`.

### Linear shape result

On six frozen output probes:

- common gain rank `1`;
- gain + `log sigma` rank `2`;
- singular values `[3.3576236639554855,0.6000359203875203]`;
- `smin/smax=0.17870850948216196`;
- `log sigma` residual fraction after common gain: **`0.3996471300114534`**.

This is a known-comparator shape direction, not Candidate Gravity novelty.

### Nonlinear potential result

The two frozen local cubic potential derivatives are exactly the existing C5 `Ricci^3/Riemann^3` response columns.

Residual norms against current C5 `R^3` span:

`4.73e-16`, `1.91e-15`.

Therefore they add zero new nonlinear span.

### Retained nonlocal results

- `NL-NG-001 — FORM_FACTOR_DOES_NOT_FIX_NONLINEAR_RESPONSE`;
- `NL-NG-002 — LOCAL_CUBIC_POTENTIAL_ALREADY_IN_C5_SPAN`;
- `NG-FUNNEL-015 — FIX_PROPAGATOR_AND_INTERACTION_POTENTIAL_SEPARATELY`.

### Nonlocal blockers

The form factor itself induces nonlocal cubic/higher vertices in the full covariant expansion. Those vertices have not yet been source-completed in the frozen retarded protocol.

Therefore:

- `d chi2R/dlog sigma` from the nonlocal cubic vertex: BLOCKED;
- full Lorentzian nonlocal causal completion: BLOCKED;
- nonlocal `N2/C3sym`: BLOCKED;
- full nonlocal quotient: BLOCKED.

Never zero-fill these sectors.

Literature anchors:

- Donà et al., JHEP 08 (2015) 038, arXiv:1506.04589;
- Briscese et al., JHEP 08 (2024) 204, arXiv:2405.14056;
- Bas i Beneito, Calcagni & Rachwał, arXiv:2211.05606.

## Article material

Latest matrix:

`docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION158.md`.

The model paper can now use explicit calculations to distinguish:

- consistency rejection;
- exact comparator identity;
- protocol blindness;
- near-degeneracy after nuisance quotient;
- propagator/interactions under-specification in nonlocal gravity.

## `ANSATZ-003` state

Still intentionally **not frozen**.

No robust Candidate Gravity residual has yet survived the complete fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.

Fisher/resources remain forbidden.

## Immediate next scientific priority — Iteration 159

Instantiate one concrete **asymptotic-safety vertex truncation** as the next independent strong QG comparator.

Required order:

1. freeze a published finite parameterization/truncation with momentum-dependent 2-/3-graviton information;
2. map only actually supported finite response directions into the frozen probe language;
3. apply common EH/gain and existing C4/C5/nonlocal subtraction;
4. if the literature result does not determine a source-completed off-shell retarded tangent, record the exact BLOCKED boundary instead of inventing a vertex;
5. keep broad asymptotic-safety program labels out of the tangent matrix;
6. no `ANSATZ-003`, Fisher or resources until a robust Candidate Gravity residual survives the full funnel.
