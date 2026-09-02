# RQIR Candidate Gravity — projected Hessian route and physical Gamma2

**Iteration:** 263  
**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Purpose

Continue from authoritative Iteration 262 without changing the frozen parent: `D=4`, `Lambda=0`, DeWitt `a=-1/2`, linear covariant-metric split, and the same Vilkovisky `U1 W = Q A Q` construction.

Iteration 262 identified `H1,H2,H3` in `A=-R R H`, `H=D E`, as an apparent remaining library. This iteration proves that the physical cubic numerator must not construct the full unprojected `H3` tensor as a primary object. The exact same-parent gauge identity gives the lower-order projected route

`A = K E`,  with  `K^j_{gamma delta}=R^i_gamma (D_i R^j_delta)`.

Since the flat Einstein background obeys `E0=0`, multilinear coefficients are

`A1[x] = K0 E1[x]`,

`A2[x,y] = K0 E2[x,y] + K1[x]E1[y] + K1[y]E1[x]`,

`A3[x,y,z] = K0 E3[x,y,z] + K1[x]E2[y,z] + K1[y]E2[x,z] + K1[z]E2[x,y] + K2[x,y]E1[z] + K2[x,z]E1[y] + K2[y,z]E1[x]`.

For the frozen null-soft leg `s`, `E1[s]=0`, therefore the last `K2[a,b]E1[s]` term vanishes exactly and physical `A3[s,a,b]` has six surviving projected terms.

## Why this is a genuine reduction

Writing `H_ij = S_,ij - Gamma^k_ij E_k`, a direct background expansion of unprojected `H3` contains the fifth functional derivative of the Einstein action (`S5`) together with connection/EOM pieces that are constrained to cancel after contraction with the two gauge generators. In contrast, `A=K E` needs only `E1,E2,E3` and `K0,K1,K2`; `E3` reaches only the fourth action variation. Thus the gauge projection removes one unnecessary action-variation order before tensor expansion.

Freeze:

`PASS_EXACT_PROJECT_BEFORE_EXPAND_A_EQUALS_K_E_CUBIC_REDUCTION`

`NO_FULL_UNPROJECTED_H3_OR_S5_REQUIRED_FOR_PHYSICAL_U1W_B3`

The `-RRH` representation remains a valid independent regression/cross-check, but it is no longer a required primary construction route for the physical cubic numerator.

## Minimal K library

The frozen affine generator is

`R=R0+R1`,  `R_n=0` for `n>=2`.

Let `P_i^j := partial_i R^j`, which is background-independent in the linear split, and

`D_i R^j = P_i^j + Gamma^j_{ik} R^k`.

With `Gamma = Gamma0 + Gamma1 + Gamma2 + ...`, define

`D0 = P + Gamma0 R0`,

`D1[x] = Gamma1[x] R0 + Gamma0 R1[x]`,

`D2[x,y] = Gamma2[x,y]R0 + Gamma1[x]R1[y] + Gamma1[y]R1[x]`.

Then

`K0 = R0 D0`,

`K1[x] = R1[x]D0 + R0 D1[x]`,

`K2[x,y] = R1[x]D1[y] + R1[y]D1[x] + R0 D2[x,y]`.

Hence no `Gamma3`, `R2`, or `R3` is required for the cubic physical `A3`.

## Second polarized field-space Christoffel

Iteration 255 fixed the exact point-local Christoffel `Gamma(g)` of the DeWitt configuration-space metric. For distinguishable metric perturbations `x,y`, define the physical mixed coefficient without an ansatz:

`Gamma2[x,y] := d^2/dt_x dt_y Gamma(eta+t_x x+t_y y)|_0`.

A reproducible certificate evaluates this coefficient from the exact compact tensor formula and independently from the 10-dimensional DeWitt field-space metric. For

`eta=diag(-1,1,1,1)`,

`x=diag(0,1,-1,0)`,

`y_12=y_21=1`,

with inner field-metric derivative step `1e-4` and mixed background step `2e-3`, it finds

- `max |Gamma2_direct-Gamma2_formula| = 9.4322526123e-08`;
- maximum tested component scale `= 5.00008028696e-01`;
- formula input-pair symmetry residual `= 0`;
- mixed-leg exchange is exact by the mixed derivative construction.

Freeze:

`PASS_SCOPED_FIELDSPACE_CHRISTOFFEL_SECOND_POLARIZED_VARIATION`

`NO_INDEPENDENT_GAMMA2_ANSATZ`.

## Consequence for the physical null-soft A library

The primary construction now needs only

`E1[x], E2[x,y], E3[s,a,b], R0/R1, Gamma0/Gamma1/Gamma2, P=partial R`,

plus the already frozen orbit-metric `N1/N2 -> Q1/Q2` recursion.

In particular:

- `A1[s]=K0 E1[s]=0` directly;
- `A2[s,a]=K0E2[s,a]+K1[s]E1[a]` (the `K1[a]E1[s]` term vanishes);
- `A2[s,b]` similarly has two projected terms;
- `A2[a,b]` has three projected terms;
- `A3[s,a,b]` has six projected terms.

These are exact same-parent reductions. They do not assert that the remaining terms vanish.

## Classification

This is an exact algebraic/projected-library reduction and a scoped geometric PASS. It is not a consistency FAIL, not an exact Candidate-vs-GR comparator identity, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate.

Retain:

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and `BLOCKED_NOT_ZERO`.

No robust Candidate Gravity residual exists. `ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy full-C5 integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 262: **0 percentage points**. A major unnecessary tensor/action-variation layer has been removed and `Gamma2` is now frozen, but the physical `E2/E3`, complete nonzero `B3`, tensor reduction, and final C5 comparator coordinate remain open. Comparator foundation stays `24/25`; unique residual remains `0/20`.

## Exact next gate — Iteration 264

Construct polarized Einstein EOM coefficients `E2[x,y]` and `E3[s,a,b]` in the same frozen convention (with `E1` already fixed), and use the frozen `Gamma0/Gamma1/Gamma2`, `R0/R1`, and `P=partial R` to build `K0,K1,K2`, hence the projected `A1,A2,A3` above. In parallel construct physical `N1[x],N2[x,y]` and obtain `Q1,Q2` only by frozen inverse recursion. Assemble the 15 surviving null-soft `B3[s,a,b]` terms. Tensor reduction remains forbidden until a nonzero physical numerator exists; Fisher/resources, blind heavy integration, and `ANSATZ-003` remain forbidden.