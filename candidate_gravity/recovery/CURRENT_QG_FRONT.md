# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 269**

## Current scientific state

The active program remains finite Vilkovisky C5 authority improvement. Iterations 261–267 fixed physical multilinear polarization, the null-soft 19-to-15 reduction, exact inverse recursion, project-before-expand `A=K E`, physical `Gamma2[x,y]`, nonzero polarized Einstein `E2/E3`, the exact projected `K0/K1/K2` 2/4/7 primitive library, the 28-primitive null-soft `A3` target, the exact reduction of 15 surviving physical `B3[s,a,b]` terms to 8 transpose classes, and condensed-index/Fourier momentum routing.

Iteration 268 instantiated the routed physical orbit inverse and proved that endpoint/intermediate `Q0` factors must be evaluated at their actual routed momenta. A follow-up transpose regression then exposed a second-order density-convention mismatch.

Iteration 269 audits the primary same-parent convention and corrects it. From the explicit gravity gauge-fixing density and the definition `Nhat=Y^up N_orb`, freeze, up to the common convention sign,

`Y^up = g^-1/sqrt(|g|)`,

`Y_down = sqrt(|g|) g`,

`N_orb = Y_down Nhat`.

For TT `g=eta+t eps`, the correct single-mode second-order coefficient is

`Y_down,2 = -(tr(H^2)/4) eta`, `H=eta^-1 eps`,

not the previously used positive sign. The first-order TT result is unchanged because `delta sqrt(|g|)=0`.

The routed recursion itself remains exact:

`Q1[x](p)=-Q0(p+k_x) N1[x](p) Q0(p)`

and

`Q2[x,y](p)=Q0(p+k_x+k_y)[N1[x](p+k_y)Q0(p+k_y)N1[y](p)+N1[y](p+k_x)Q0(p+k_x)N1[x](p)-N2[x,y](p)]Q0(p)`.

With corrected density, all second-order `NQ=I` residuals are `<=4.45e-16`, mixed-leg exchange is `<=4.41e-9`, and endpoint-reversed `Q2` transpose residuals are `<=4.49e-8`. The superseded density leaves stable `N2` transpose residuals `0.03165`, `0.21036`, `0.62805`.

Freeze:

`PASS_PRIMARY_AUTHORITY_ORBIT_DENSITY_CORRECTION_AND_ROUTED_N2_Q2_TRANSPOSE_RESTORATION`.

Guardrail:

`USE_Y_UP=g^-1/sqrt|g| AND Y_DOWN=sqrt|g|*g; DO_NOT_USE_THE_INVERTED_DENSITY_FACTOR`.

## Supersession boundary

- Iteration 252: supersede only the explicit density representative; retain exact `Nhat=Y^up N_orb` orientation and TT `deltaY^up=-eps^up`.
- Iteration 258: supersede `Y_down=g/sqrt|g|`, the positive second-order TT density sign, and derived `Norb2` numerical values.
- Iteration 259: supersede numerical `Q2` inherited from old `Norb2`; retain exact inverse-recursion algebra.
- Iteration 268: supersede numerical second-order `N2/Q2` only; retain `Q1`, Fourier routing, exact convolution recursion and rejection of same-`p` routing.
- No topology, `E2/E3`, `Gamma`, `K`-primitive, polarization or 15-to-8 transpose-class result is revoked.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 268: **0 percentage points**. A real implementation/provenance error was removed and the physical routed second-order orbit layer now obeys both exact inverse recursion and endpoint-reversed same-parent transpose, but routed physical `K/A`, assembled `B3`, tensor reduction, source projection and complete C5 comparator closure remain open.

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
- Iterations 257–259 fix exact physical inverse recursion through `Q2`; Iteration 269 corrects the second-order orbit-density numerical input.
- Iteration 260 fixes exact coefficientwise weighted symmetry of complete same-parent `U1 W`; transpose mismatch is an implementation regression, not a new physical Ward FAIL.
- Iteration 261 fixes physical multilinear polarization and the null-soft 19-to-15 reduction.
- Iteration 262 fixes polarized `A` bookkeeping and proves `Q3/N3` unnecessary because `A0=0`.
- Iteration 263 fixes project-before-expand `A=K E`, eliminates full unprojected `H3/S5`, and freezes physical `Gamma2[x,y]`.
- Iteration 264 fixes nonzero, permutation-symmetric physical `E2/E3` and forbids zero-filling nonlinear EOM sectors from `E1[s]=0`.
- Iteration 265 fixes the exact polarized `K0/K1/K2` primitive library as 2/4/7, null-soft projected `A3` primitive count 28, and forbids `R2/R3/Gamma3` in this cubic route.
- Iteration 266 fixes the exact null-soft `B3` transpose-class reduction 15-to-8.
- Iteration 267 fixes condensed-index/Fourier momentum support and endpoint-reversed kernel transpose.
- Iteration 268 fixes physical routed inverse recursion and same-`p` rejection; use Iteration-269 corrected second-order `N2/Q2` values.
- Iteration 269 fixes the primary density orientation and restores routed second-order endpoint transpose.

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

## Iteration 269 authority files

- `candidate_gravity/C5_VD_ORBIT_DENSITY_CORRECTION_ITERATION269.md`
- `candidate_gravity/code/iteration269_vd_orbit_density_correction.py`
- `candidate_gravity/results/iteration269_vd_orbit_density_correction.json`
- `research_log/2026-09-02_iteration_269_vd_orbit_density_correction.md`
- `recovery/RECOVERY_DELTA_ITERATION_269.md`
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION269.md`

## Exact next gate — Iteration 270

Rebuild routed physical `K0/K1/K2 -> A1/A2/A3` using the frozen affine generator and `Gamma0/Gamma1/Gamma2`, then instantiate the 8 independent forward `+K` `B3[s,a,b]` representatives with the corrected Iteration-269 `Q2`. Reconstruct all seven partners through endpoint reversal / real `-K` Fourier sector. Only if every transpose regression passes may the complete 15-term physical `B3` be frozen as explicitly nonzero. Tensor reduction remains forbidden until that certificate exists. Do not launch Fisher/resources, blind heavy full-C5 integration, or create `ANSATZ-003`.
