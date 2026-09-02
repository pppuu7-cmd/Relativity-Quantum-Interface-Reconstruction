# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 268**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–267 fixed physical multilinear polarization, the null-soft 19-to-15 reduction, exact inverse recursion, project-before-expand `A=K E`, physical `Gamma2[x,y]`, nonzero polarized Einstein `E2/E3`, the exact projected `K0/K1/K2` 2/4/7 primitive library, the 28-primitive null-soft `A3` target, the exact reduction of 15 surviving physical `B3[s,a,b]` terms to 8 transpose classes, and the condensed-index/Fourier momentum-routing semantics for those classes.

Iteration 268 now constructs the physical routed orbit-metric inverse layer itself.

For `Q0(p)=N0(p)^-1`,

`Q1[x](p)=-Q0(p+k_x) N1[x](p) Q0(p)`

and for distinct legs `x,y`,

`Q2[x,y](p)=Q0(p+k_x+k_y)[N1[x](p+k_y)Q0(p+k_y)N1[y](p)+N1[y](p+k_x)Q0(p+k_x)N1[x](p)-N2[x,y](p)]Q0(p)`.

Physical `N1/N2` are extracted from the same finite-amplitude curved minimal ghost operator and exact `N_orb=W^-1 Nhat` factorization already frozen in the repository. At the frozen generic loop momentum all `Q1` and all mixed `Q2` kernels are explicitly nonzero. First- and second-order convolution residuals of `NQ=I` are <= `8.89e-16`; mixed-leg exchange is stable within the finite-difference envelope.

A deliberately wrong same-loop-momentum implementation fails at first order with residuals `0.5414`, `0.2260`, `0.9130` for `s,a,b`. Thus routed endpoint/intermediate `Q0` factors are mandatory.

Freeze:

`PASS_SCOPED_PHYSICAL_ROUTED_N1_N2_Q1_Q2_KERNEL_LAYER`.

Guardrail:

`Q0 MUST BE EVALUATED AT EACH ROUTED ENDPOINT/INTERMEDIATE MOMENTUM; SAME-p RESOLVENT INSERTION IS FALSE`.

Retain Iteration-267 kernel-transpose guardrail:

`NO_FIXED_PLUS_K_MATRIX_TRANSPOSE_AS_KERNEL_TRANSPOSE`.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 267: **0 percentage points**. The physical routed inverse-resolvent half of the cubic kernel is now explicit, but routed physical `K/A`, assembled `B3`, tensor reduction, source projection and complete C5 comparator closure remain open.

## Frozen guardrails retained

- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists.
- `e+c<=3` remains the frozen finite-`R^3` truncation rule.
- Iteration 252 fixes `Nhat=W N_orb` and the `U1` factorization.
- Iteration 253 fixes complete `A3=K0E3+K1E2+K2E1`; standalone `K1E2` is not a Ward FAIL object.
- Iteration 254 fixes affine `R=L_xi g` in the linear metric split.
- Iteration 255 fixes configuration-space Christoffel `Gamma` in `D_iR`.
- Iterations 257–259 fix physical orbit-metric inverse recursion through `Q2`; no independent `N2/Q2` ansatz.
- Iteration 260 fixes exact coefficientwise weighted symmetry of complete same-parent `U1 W`; transpose mismatch is an implementation regression, not a new physical Ward FAIL.
- Iteration 261 fixes physical multilinear polarization and the null-soft 19-to-15 reduction.
- Iteration 262 fixes polarized `A` bookkeeping, `Q1/Q2` recursion, and proves `Q3/N3` unnecessary because `A0=0`.
- Iteration 263 fixes project-before-expand `A=K E`, eliminates full unprojected `H3/S5`, and freezes physical `Gamma2[x,y]`.
- Iteration 264 fixes nonzero, permutation-symmetric physical `E2/E3` and forbids zero-filling nonlinear EOM sectors from `E1[s]=0`.
- Iteration 265 fixes the exact polarized `K0/K1/K2` primitive library as 2/4/7, the null-soft projected `A3` primitive count as 28, and forbids `R2/R3/Gamma3` in this cubic route.
- Iteration 266 fixes the exact null-soft `B3` transpose-class reduction 15-to-8.
- Iteration 267 fixes condensed-index/Fourier momentum support and endpoint-reversed kernel transpose.
- Iteration 268 fixes physical routed `N1/N2/Q1/Q2`; all propagator inverses must use the actual routed momenta.

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

## Iteration 268 authority files

- `candidate_gravity/C5_VD_ROUTED_ORBIT_INVERSE_ITERATION268.md`
- `candidate_gravity/code/iteration268_vd_routed_orbit_inverse.py`
- `candidate_gravity/results/iteration268_vd_routed_orbit_inverse.json`
- `research_log/2026-09-02_iteration_268_vd_routed_orbit_inverse.md`
- `recovery/RECOVERY_DELTA_ITERATION_268.md`

## Exact next gate — Iteration 269

Construct the matching routed physical `K0/K1/K2` kernels from the frozen affine diffeomorphism generator, `P=partial R`, and `Gamma0/Gamma1/Gamma2` library. Contract them with certified physical `E1/E2/E3` to obtain routed `A1/A2/A3`. Then instantiate the eight forward `+K` `B3[s,a,b]` representatives using Iteration-268 `Q0/Q1/Q2`, reconstruct seven transpose partners only by endpoint reversal / the real-mode `-K` sector, and determine whether the assembled physical `B3[s,a,b]` is explicitly nonzero. Tensor reduction remains forbidden until that algebraic nonzero is established. Do not launch Fisher/resources, blind heavy full-C5 integration, or create `ANSATZ-003`.
