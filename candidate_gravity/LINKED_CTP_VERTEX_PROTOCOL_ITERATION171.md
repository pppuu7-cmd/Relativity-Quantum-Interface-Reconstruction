# Candidate Gravity — Iteration 171: linked/amputated CTP cubic protocol

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**  
**Status:** linked post-Gaussian protocol frozen; no Candidate Gravity residual

## Motivation

Iteration 170 closed standalone positive linear spectral shape as a gravity-specific novelty route against C4. The next RQIR observable must therefore compare **higher-point relations conditioned on the same two-point kernel**.

## Full CTP amputation

Let `G_ab` be the calibrated two-point CTP/Keldysh matrix in a fixed physical field/source convention and `G3_abc` the connected three-point tensor. The exact Legendre-transform relation is schematically

\[
G^{(3)}_{abc}
=-G_{aa'}G_{bb'}G_{cc'}\Gamma^{(3)}_{a'b'c'}.
\]

Thus, once the full two-point matrix is treated as measured/shared data, the corresponding source-completed 1PI three-point kernel is obtained by amputation. This removes arbitrary external-leg spectral dressing from the novelty carrier.

The physical source/field convention remains the unreduced source-completed convention frozen in Iterations 148–149. Naive coordinate Green functions or a field-redefined vertex without its induced source contacts are not admissible.

## Numerical dressing-control illustration

A deterministic six-row projected cubic kernel was dressed on all three external legs by nontrivial positive momentum-dependent factors. The raw nonlinear response changes by

`25.5556366906597%`,

while the reconstructed amputated kernel changes by no more than

`1.11e-16`.

This is an algebraic control, not a model prediction.

Retain:

`CTP-NG-002 — TWO_POINT_EXTERNAL_LEG_DRESSING_DISAPPEARS_AFTER_FIXED_CONVENTION_THREE_POINT_AMPUTATION`.

## Closed-unitary cubic r/a identity

For any symmetric cubic functional

\[
S_3[h]=\frac1{3!}B(h,h,h),
\]

use

\[
h_+=r+a/2,\qquad h_-=r-a/2.
\]

Then

\[
S_3[h_+]-S_3[h_-]
=\frac12B(a,r,r)+\frac1{24}B(a,a,a).
\]

Writing the cubic CTP action in the convention

\[
\Gamma_3^{CTP}\supset
\frac{\Gamma_{arr}}{2!}arr
+\frac{\Gamma_{aar}}{2!}aar
+\frac{\Gamma_{aaa}}{3!}aaa,
\]

gives the exact tree-level closed-unitary relation

\[
\boxed{\Gamma_{aar}=0},
\qquad
\boxed{\Gamma_{aaa}=\frac14\Gamma_{arr}}.
\]

The relation follows only from the `S[h_+]-S[h_-]` structure and the r/a convention. It is not special to gravity.

Therefore both a quantum C5 gravitational cubic action and an ordinary quantum C4 mediator with a cubic self-interaction can satisfy the same relation.

Retain:

`CTP-NG-001 — CLOSED_UNITARY_CUBIC_AAA_OVER_ARR_RATIO_IS_NOT_GRAVITY_SPECIFIC`.

Classical statistical/MSR descriptions can differ at bare level because the deterministic drift is linear in the response field and Gaussian noise contributes even-response-field terms; the absence/presence of the quantum vertex is useful as a quantum-vs-classical control but cannot distinguish gravity from an ordinary quantum C4 mediator. Non-Gaussian classical noise can also add higher response-field vertices, so broad C3 alternatives must still be instantiated rather than assumed zero.

## Minimal linked coordinates going forward

The two-point kernel is now a calibrated/shared layer. A future finite post-Gaussian protocol should expose, in one source-completed convention, at least

- `Gamma_arr^(3)` — causal/deterministic cubic response vertex;
- `Gamma_aar^(3)` — noise/response mixed vertex when present;
- `Gamma_aaa^(3)` — genuinely quantum or higher-noise CTP vertex component;
- the Ward/soft/constraint relation tying `Gamma_arr` to the same universal stress coupling and two-point inverse kernel.

Raw `C3sym` and `chi2R` remain experimentally meaningful, but comparator novelty should be evaluated after the common two-point kernel is conditioned/amputated.

## Funnel consequence

A candidate cannot be promoted because:

- its raw three-point response differs after a novel two-point form factor;
- it has a nonzero `aaa` vertex;
- it satisfies the generic closed-unitary `aaa/arr=1/4` relation.

The residual must be a linked CTP/tensor/Ward relation that is outside fixed C3, C4, C5, nonlocal and asymptotic-safety multi-point comparator families.

Retain:

`NG-FUNNEL-031 — CANDIDATE_RESIDUAL_MUST_BE_A_LINKED_CTP_VERTEX_RELATION_AFTER_TWO_POINT_AMPUTATION`.

## Comparator status

### C3

The fixed PQCG comparator has supported `N2` and `C3sym` information and a common-EH tree causal response, but its full source-completed r/a three-point vertex, including diffusion-dependent ordered/MSR pieces, remains BLOCKED.

### C4

The fixed dRGT tree cubic action is an ordinary closed quantum action and therefore belongs to the same generic closed-unitary r/a identity class. Full C4 Gaussian-noise / loop / helicity completion remains BLOCKED.

### C5

EH and local EFT cubic vertices are closed-unitary tree controls and obey the same r/a identity before open-system/loop influence terms are included. Quantum loop/noise CTP three-point components remain to be instantiated in the same finite protocol.

### Nonlocal / asymptotic safety

Their two-point form factors/spectra are external-leg data after amputation. Their nonlinear CTP vertex relations remain relevant and currently BLOCKED in the required real-time source-completed convention.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

The linked protocol is now better posed, but no actual multi-point residual has survived concrete comparator subtraction.

No `ANSATZ-003`. No Fisher. No resource optimization.
