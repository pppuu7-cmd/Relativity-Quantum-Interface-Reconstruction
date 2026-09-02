# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 270**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–267 fixed physical multilinear polarization, the null-soft 19-to-15 reduction, project-before-expand `A=K E`, physical `Gamma2[x,y]`, nonzero polarized Einstein `E2/E3`, the exact projected `K0/K1/K2` 2/4/7 primitive library, the 28-primitive null-soft `A3` target, the exact 15-to-8 `B3` transpose-class reduction, and condensed-index/Fourier endpoint routing.

Iteration 268 instantiated exact routed physical inverse recursion. Iteration 269 then corrected the physical orbit-density orientation from primary same-parent authority:

`Y^up = g^-1/sqrt(|g|)`,

`Y_down = sqrt(|g|) g`,

`N_orb = Y_down Nhat`.

Use Iteration-269 corrected second-order `N2/Q2`; its inverse residuals are machine precision and endpoint-reversed transpose is restored. Do not use the superseded inverted density representative from Iterations 258/259/268.

Iteration 270 audits the remaining projected numerator identity

`A_{gamma delta}=K^j_{gamma delta} E_j`

in condensed-index/Fourier space. The contracted field-space index `j` contains a spacetime momentum. For a polarized factor `K_m[S] E_n[T]`, with the frozen Iteration-267 convention,

`p_out-p_in = k_S + q_j`,

and contraction with `E[T]` fixes

`q_j = k_T`.

Therefore the physical kernel support is

`p_out-p_in = k_S+k_T`.

The momentum of the contracted EOM/field index must remain explicit until the `K E` contraction is performed. A finite matrix `K_m(p)` labelled only by orbit momentum and the explicit background subset `S` is under-specified for physical `A` and can generate a false-positive nonzero `B3` by silently dropping the field-space Fourier convolution.

Freeze:

`PASS_EXACT_PROJECTED_A_CONTRACTED_FIELD_MOMENTUM_ROUTING`.

Guardrails:

`NO_DROP_CONTRACTED_EOM_MOMENTUM_IN_K_KERNEL`.

`NO_PREMATURE_LOCAL_MATRIX_K_TIMES_E_AS_PHYSICAL_A`.

The reproducible route enumeration preserves all earlier physical/null-soft counts:

- `A1[s]`: 0 surviving projected terms;
- `A2[s,a]`: 2;
- `A2[s,b]`: 2;
- `A2[a,b]`: 3;
- `A3[s,a,b]`: 6.

All eight forward `B3[s,a,b]` transpose-class representatives retain total support `k_s+k_a+k_b`, but numerical physical `A1/A2/A3` must now be instantiated with the contracted-field routing before multiplication by the corrected Iteration-269 `Q` kernels.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 269: **0 percentage points**. A mandatory physical-routing ambiguity in the projected `A` layer has been eliminated, but explicit routed numerical `K/A/B3`, tensor reduction, source projection and complete C5 comparator closure remain open; no readiness-rubric category closes.

## Frozen guardrails retained

- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists.
- `e+c<=3` remains the frozen finite-`R^3` truncation rule.
- Iteration 252 fixes orbit/minimal-ghost factorization and TT first-order weight variation, subject to the Iteration-269 density correction.
- Iteration 253 fixes complete `A3=K0E3+K1E2+K2E1`; standalone `K1E2` is not a Ward FAIL object.
- Iteration 254 fixes affine `R=L_xi g` in the linear metric split.
- Iteration 255 fixes configuration-space Christoffel `Gamma` in `D_iR`.
- Iterations 257–259 fix exact inverse-recursion algebra through `Q2`; Iteration 269 corrects the second-order orbit-density numerical input.
- Iteration 260 fixes exact coefficientwise weighted symmetry of complete same-parent `U1 W`; transpose mismatch is an implementation regression, not a new physical Ward FAIL.
- Iteration 261 fixes physical multilinear polarization and the null-soft 19-to-15 reduction.
- Iteration 262 fixes polarized `A` bookkeeping and proves `Q3/N3` unnecessary because `A0=0`.
- Iteration 263 fixes project-before-expand `A=K E`, eliminates full unprojected `H3/S5`, and freezes physical `Gamma2[x,y]`.
- Iteration 264 fixes nonzero, permutation-symmetric physical `E2/E3` and forbids zero-filling nonlinear EOM sectors from `E1[s]=0`.
- Iteration 265 fixes the exact polarized `K0/K1/K2` primitive library as 2/4/7, null-soft projected `A3` primitive count 28, and forbids `R2/R3/Gamma3` in this cubic route.
- Iteration 266 fixes the exact null-soft `B3` transpose-class reduction 15-to-8.
- Iteration 267 fixes condensed-index/Fourier momentum support and endpoint-reversed kernel transpose.
- Iteration 268 fixes exact routed inverse recursion and same-`p` rejection; use Iteration-269 corrected second-order `N2/Q2` values.
- Iteration 269 fixes the primary density orientation and restores routed second-order endpoint transpose.
- Iteration 270 fixes the contracted field/EOM momentum routing required by projected `A=K E`; do not collapse `K^j` to a one-momentum local matrix before contraction.

## Retained comparator state

### C3
`BLOCKED_FORMAL_UNDERDETERMINATION_OF_NONLINEAR_CONSERVED_COMPLETION` — not zero and not consistency FAIL.

### C4
Standalone positive two-point spectral/cut information remains mediator-degenerate.

### C5
`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

`BLOCKED_NOT_ZERO`.

### Other routes
Asymptotic-safety, nonlocal and proxy routes retain their frozen blockers; no proxy replaces the frozen comparator identity.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Heavy full C5 run: NOT AUTHORIZED.

## Iteration 270 authority files

- `candidate_gravity/C5_VD_PROJECTED_A_FIELD_MOMENTUM_ROUTING_ITERATION270.md`
- `candidate_gravity/code/iteration270_vd_projected_a_field_momentum_routing.py`
- `candidate_gravity/results/iteration270_vd_projected_a_field_momentum_routing.json`
- `research_log/2026-09-02_iteration_270_vd_projected_a_field_momentum_routing.md`
- `recovery/RECOVERY_DELTA_ITERATION_270.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION270.md`

## Exact next gate — Iteration 271

Implement the physical routed kernel `K_m[S](p_out,p_in;q_j)` or an exactly equivalent representation from the frozen affine generator, `Gamma0/Gamma1/Gamma2` and the 2/4/7 primitive library. Contract it with certified `E1/E2/E3` to obtain numerical routed `A1/A2/A3`. Then instantiate the eight independent forward `+K` `B3[s,a,b]` representatives using corrected Iteration-269 `Q2`, reconstruct all seven partners through endpoint reversal / real `-K` Fourier sector, and require every transpose regression to pass before freezing a nonzero physical `B3`. Tensor reduction remains forbidden until that certificate exists. Do not launch Fisher/resources, blind heavy full-C5 integration, or create `ANSATZ-003`.
