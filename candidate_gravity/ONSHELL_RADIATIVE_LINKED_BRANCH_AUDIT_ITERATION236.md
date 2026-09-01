# RQIR Candidate Gravity — Iteration 236

Date: 2026-09-01

MODEL_READINESS: 24%

## Question

After freezing AS, C3 and the finite-CPT3 C5 route at their current authority boundaries, is there an executable **same-parent physical branch** that can test the unchanged linked nonanalytic target

\[
T_{\rm cut}=D\Gamma^{(3)}_{\rm ret,soft}-W[D K_2]
\]

without replacing it by a different observable?

## Selected executable branch

The strongest branch found is minimally coupled GR with two massive spinless scalar sources and one radiated graviton:

- elastic `2 -> 2` massive-scalar gravitational scattering;
- radiative `2 -> 3` massive-scalar scattering plus one graviton;
- the one-loop radiative amplitude in the near-forward/classical regime;
- explicit unitarity cuts and a soft theorem relating the radiative amplitude to the one-loop four-point amplitude.

Primary authority:

1. A. Georgoudis, C. Heissenberg, I. Vazquez-Holm, **Inelastic Exponentiation and Classical Gravitational Scattering at One Loop**, JHEP 06 (2023) 126, arXiv:2303.07006.
2. A. Brandhuber et al., **One-loop Gravitational Bremsstrahlung and Waveforms from a Heavy-Mass Effective Field Theory**, JHEP 06 (2023) 048, arXiv:2303.06111.
3. A. Georgoudis, C. Heissenberg, R. Russo, **An eikonal-inspired approach to the gravitational scattering waveform**, JHEP 03 (2024) 089, arXiv:2312.07452.
4. A. Georgoudis, C. Heissenberg, R. Russo, **Post-Newtonian Multipoles from the Next-to-Leading Post-Minkowskian Gravitational Waveform**, Phys. Rev. D 109 (2024) 106020, arXiv:2402.06361.

## Why this branch is materially stronger than the frozen AS route

The 2023 radiative calculation supplies, in one declared GR matter system:

- an explicit one-loop `2 -> 3` amplitude;
- the corresponding one-loop `2 -> 2` amplitude entering its soft limit;
- a fixed Feynman `i0` / analytic-continuation convention;
- explicit unitarity cuts for imaginary parts;
- leading and subleading soft-region information capturing nonanalytic terms in transferred momentum and graviton frequency;
- a direct check that the most singular soft term reduces to a universal soft factor times the one-loop four-point amplitude.

The paper states that the displayed one-loop radiative terms agree with Weinberg soft factorization and that their imaginary pieces arise from the expected unitarity cuts. In impact-parameter space it gives an explicit relation between the one-loop radiative amplitude and lower-point elastic data.

Thus this branch is **executable at the S-matrix level** and has same-parent lower-/higher-point ingredients. It is not merely a generic formalism.

## Critical guardrail: S-matrix soft relation is not yet the frozen retarded relation

The frozen RQIR object is not an arbitrary soft theorem. It specifically requires

1. `D Gamma3_ret,soft` in the declared source-completed retarded convention;
2. `W[D K2]` from the same parent dynamics and parameter convention;
3. the same hard-channel discontinuity definition `D = Disc/(2 pi i)`;
4. source/Ward/contact completion;
5. identical IR subtraction and branch prescription.

The cited radiative amplitude is a physical time-ordered/on-shell S-matrix object. Its unitarity cut is physical, but this **does not by itself prove** the exact identity

\[
D\mathcal A_{2\to3}^{\rm soft}
\stackrel{?}{=}
D\Gamma^{(3)}_{\rm ret,soft}
\]

nor does Weinberg factorization by itself prove that its lower-point term is exactly the frozen `W[D K2]` after the RQIR source/contact convention is applied.

Therefore the branch may be used only after an explicit LSZ/Schwinger-Keldysh/retarded observable-identity map is established.

## Classification

`EXECUTABLE_ONSHELL_LINKED_BRANCH_IDENTIFIED`

with mandatory unresolved gate

`BLOCKED_ONSHELL_TO_RETARDED_SOURCE_COMPLETED_OBSERVABLE_IDENTITY_MAP`.

This is not:

- a consistency FAIL;
- an exact comparator identity;
- regime-specific non-identifiability;
- near-degeneracy;
- a novelty certificate;
- permission to replace `T_cut` by a waveform, an N-operator matrix element, or an S-matrix soft factor.

## New scoped results

- `REL-CUT-016` — `MASSIVE_SCALAR_GR_RADIATIVE_BRANCH_HAS_SAME_PARENT_ONE_LOOP_2TO3_AND_2TO2_SOFT_LINK_WITH_EXPLICIT_UNITARITY_CUTS`.
- `REL-NG-016` — `AN_ONSHELL_SOFT_FACTOR_RELATION_IS_NOT_AUTOMATICALLY_THE_RQIR_RETARDED_SOURCE_COMPLETED_LINKED_RELATION`.
- `REL-BLOCK-001` — `ONSHELL_TO_RETARDED_SOURCE_COMPLETED_OBSERVABLE_IDENTITY_MUST_BE_PROVED_BEFORE_POPULATING_T_CUT`.
- `NG-FUNNEL-092` — `EXECUTABLE_PHYSICAL_BRANCH_SELECTED_WITHOUT_CANDIDATE_NOVELTY_PROMOTION`.

## Candidate state

Robust Candidate Gravity residual: `NONE`.

`ANSATZ-003`: `NOT_CREATED`.

Fisher/resources: `FORBIDDEN`.

No heavy calculation is justified yet because observable identity is a hard prerequisite.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 235: **0 percentage points**. The executable branch-selection problem is now closed, but the last comparator-foundation point remains open until the branch is proven observable-identical to the frozen retarded/source-completed relation. Unique residual remains `0/20`.

## Exact next gate

Iteration 237 must perform an **observable-identity audit**, not a fit:

1. freeze a concrete LSZ convention for two massive scalar source legs plus one emitted graviton;
2. write the CTP/retarded three-point discontinuity with the same external states and hard channel;
3. derive whether the physical unitarity discontinuity of the `2 -> 3` amplitude equals the required retarded discontinuity after LSZ;
4. derive `W[D K2]` from the same `2 -> 2` parent amplitude and the same momentum/normalization convention;
5. include soft/contact/source Ward terms and the same IR subtraction;
6. only if the equality is established may the existing amplitude formulas be sampled on frozen RQIR rows.

If the map fails or requires extra arbitrary completion, classify the branch `ON_SHELL_PROXY_NOT_OBSERVABLE_IDENTICAL` and do not populate the comparator column.