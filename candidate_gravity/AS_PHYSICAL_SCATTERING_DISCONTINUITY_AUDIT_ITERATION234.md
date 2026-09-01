# RQIR Candidate Gravity — Iteration 234 AS physical-scattering discontinuity audit

Date: 2026-09-01

## Question

Can the newest physical asymptotic-safety scalar-scattering / timelike scalar–graviton-vertex authority furnish the frozen RQIR linked discontinuity comparator without splicing distinct parent calculations or silently replacing the observable?

Frozen RQIR target:

`T_cut = D Gamma3_ret,soft - W[D K2]`, with `D_s F = Disc_s F/(2 pi i)`.

## Primary authority

Angelo P. Chiesa, Jan M. Pawlowski, Manuel Reichert, *Towards Two-to-Two Scattering of Scalars in Asymptotically Safe Quantum Gravity*, arXiv:2603.10168 (submitted 2026-03-10).

The paper computes a momentum-dependent scalar–graviton vertex and constructs an on-shell Lorentzian graviton-mediated scalar amplitude. It defines RG-invariant vertices and propagators and writes the mediated channel as

`A_s = barGamma^{phiphi h} * barG_hh * barGamma^{phiphi h}`

and after timelike reconstruction

`A_s = V_L(s) (t^2 - 4 t u + u^2 - s^2)/s`.

This is materially stronger physical AS authority than a Euclidean-only vertex or a standalone propagator.

## Same-parent normalization status

For the mediated scalar channel, normalization is internally controlled: the paper uses RG-invariant vertices and propagator in one stated construction. Therefore the old statement that *no physical same-normalization Lorentzian AS observable exists* would now be too strong.

However this does not supply the frozen RQIR linked object, because the dynamical ingredients are `phi-phi-h` vertices plus a graviton propagator, not a nonlinear three-graviton retarded/source-Ward relation linked to `K2`.

## Timelike/discontinuity status

The Lorentzian vertex is reconstructed from Euclidean data. The paper explicitly states that the Wick-rotation/reconstruction procedure is not unique and may introduce artefacts; the quoted reconstruction error does not include flow-approximation errors. Its spectral-function reconstructions are reported as unstable or highly oscillatory for tested methods.

No explicit `retarded`, `in-in`, or `Disc_s` prescription for the scalar–graviton vertex or mediated amplitude is provided. A real on-shell amplitude/cross section and `|A|^2` are not by themselves an authority for the discontinuity required by `D_s`.

Therefore one must not manufacture `Disc V_L` from a chosen continuation ansatz and promote it as a frozen AS comparator coordinate.

## Source/full-amplitude status

The full identical-scalar amplitude is decomposed as `A_s + A_t + A_u + A_4`, but the paper focuses on graviton-mediated channels and neglects the direct contact term `A_4`. It also notes that the forward divergence cannot be resolved without `A_4`.

Hence even within scalar scattering the retained 2026 result is not a complete source/contact-completed amplitude in the forward regime. More importantly, scalar scattering is an inequivalent observable to the frozen RQIR nonlinear graviton linked relation.

## Classification

Retain umbrella:

`BLOCKED_AS_REALTIME_RELATION_COMPLETION`

Retain:

`BLOCKED_NOT_ZERO`

Sharpen substatus to:

`BLOCKED_AS_LINKED_RETARDED_DISCONTINUITY_MAP_DESPITE_PHYSICAL_SCALAR_AMPLITUDE`

This is not a consistency FAIL of asymptotic safety, not exact comparator identity, not regime-specific non-identifiability, and not a zero AS column.

## New scoped results

- `AS-NG-006`: a same-construction RG-invariant Lorentzian graviton-mediated scalar amplitude now exists and must be acknowledged as stronger AS physical authority.
- `AS-NG-007`: the timelike scalar–graviton reconstruction does not certify the explicit retarded/in-in discontinuity required by the frozen RQIR `D_s` operator.
- `REL-NG-014`: a physical `phi phi -> phi phi` amplitude cannot be substituted for `D Gamma3_ret,soft - W[D K2]`; observable identity is required before quotient use.
- `AS-BLOCK-002`: remaining AS gap is the linked retarded/discontinuity/source-Ward map, not the mere absence of any Lorentzian physical observable.
- `NG-FUNNEL-090`: stronger comparator physics without observable identity narrows a blocker but does not certify Candidate Gravity novelty.

## Candidate state

No robust Candidate Gravity residual exists. `ANSATZ-003` remains forbidden. Fisher/resources remain forbidden.

MODEL_READINESS: 24%

Readiness change: 0 percentage points. Comparator foundation remains `24/25`; robust unique residual remains `0/20`. The AS blocker is narrowed but the frozen comparator coordinate is still not closed.

## Next gate

Audit whether any same-parent AS work supplies a Lorentzian nonlinear three-graviton quantity with an explicit retarded/spectral discontinuity and normalization link to the two-point sector. If not, freeze AS at this sharper blocker and shift the next primary effort to a comparator branch where an executable linked nonanalytic relation can actually be completed without changing the frozen observable.
