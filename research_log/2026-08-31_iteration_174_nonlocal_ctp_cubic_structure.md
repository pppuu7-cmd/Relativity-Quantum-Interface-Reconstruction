# RQIR Research Log — Iteration 174

**Date:** 2026-08-31  
**MODEL_READINESS: 24%**

## Starting authority

Auto-research advanced the authoritative front through Iteration 173. Iteration 172 built the first finite CTP relation-level comparator matrix; Iteration 173 established `BLOCKED_C3_CTP_ORDERED_COMPLETION` for the fixed PQCG comparator because the available conserved-diffusion linear completion does not uniquely determine the nonlinear ordered MSR cubic vertex.

## Fixed nonlocal comparator

Use `QG-NL-EXP-001`:

`S = Mpl^2/2 int sqrt(-g) [R + G_mn F(Box) R^mn] + S_m`,

`F(Box)=(exp(-lambda Box)-1)/Box`, `lambda=1` at the frozen reference point.

## Cubic operator audit

The covariant curvature expansion gives

`S_NL^(3) ~ G2 F0 R1 + G1 F0 R2 + sqrtg1 G1 F0 R1 + G1 (delta F)_1 R1`.

The last operator-variation term is not contained in propagator-only reasoning.

Using

`F(A)=-int_0^lambda exp(-alpha A)dalpha`,

derive

`delta F(A)=int_0^lambda dalpha int_0^alpha du exp(-(alpha-u)A)(delta A)exp(-uA)`.

Between eigenmodes this is the divided difference

`[F(a)-F(b)]/(a-b)`.

Six numerical checks, including the diagonal limit, give zero floating-point discrepancy.

## Parent-action vs propagator distinction

For the exact frozen `QG-NL-EXP-001` action, the full tree cubic vertex is fixed in principle; there is no independent curvature-cubic potential in the frozen definition.

For the broader weakly-nonlocal class, the same two-point propagator does not uniquely define the cubic sector because independent higher-curvature potentials/form-factor structures can be added without affecting the quadratic kernel. This is already explicit in `NL-WNL-001`.

## Relation-level result

The current Iteration-172 relation map is

`R_aar=Gamma_aar`,

`R_unit=Gamma_aaa-Gamma_arr/4`,

`R_W=WardLock`.

Any closed-unitary cubic tree action satisfies

`Gamma_aar=0`, `Gamma_aaa=Gamma_arr/4`.

A source-completed diffeomorphism-invariant parent action satisfies `WardLock=0`.

Therefore the fixed nonlocal tree comparator maps identically to zero in the current relation coordinates, independent of its raw cubic amplitude.

Certificate:

- generic six-row raw amplitude rank: `6`;
- relation rank: `0`;
- maximum absolute relation entry: `0.0`.

## Retained results

- `NL-NG-003 — COVARIANT_NONLOCAL_CUBIC_VERTEX_CONTAINS_OPERATOR_FRECHET_VARIATION_NOT_VISIBLE_IN_PROPAGATOR_ONLY_REASONING`;
- `CTP-NG-005 — CLOSED_UNITARY_DIFFEO_INVARIANT_NONLOCAL_TREE_ACTION_IS_ANNIHILATED_BY_CURRENT_COARSE_CTP_RELATION_MAP`;
- `NG-FUNNEL-034 — ZERO_WARD_LOCK_PLUS_GENERIC_UNITARY_RA_RELATION_CANNOT_DISTINGUISH_QUANTUM_GRAVITY_FAMILIES`.

## Scientific interpretation

This closes the nonlocal tree occupancy of the **current coarse relation quotient**, but it does not provide a Candidate Gravity residual. Instead it proves that the current relation map is too coarse: generic quantum unitarity and Ward consistency are shared by C4, C5 and nonlocal quantum gravity.

## Literature check

Donà et al., JHEP 08 (2015) 038 / arXiv:1506.04589, show that broad Ricci/scalar weakly-nonlocal form-factor theories can share Einstein tree on-shell amplitudes via field-redefinition equivalence, while Riemann-sector additions alter amplitudes. Biswas–Koivisto–Mazumdar, arXiv:1302.0532, provide the general covariant flat-space propagator framework used by the nonlocal comparator family.

RQIR is intentionally off-shell/source-response sensitive, so this on-shell equivalence is a guardrail rather than a substitute for the cubic source-completed map.

## Readiness

`MODEL_READINESS: 24%` — unchanged.

Reason: comparator structure is sharpened, but no unique residual, parent dynamics, candidate consistency, Fisher or resources block closes.

## Next gate

Iteration 175 should replace scalar `WardLock=0` by a **tensor/soft Ward decomposition**:

1. derive a finite source-completed 1PI Ward map tying the longitudinal cubic vertex to the same inverse two-point kernel;
2. project out that Ward-determined longitudinal sector as consistency/shared structure;
3. define finite transverse cubic form-factor coordinates left after that projection;
4. test C4/C5/nonlocal occupancy there before any candidate construction;
5. preserve AS real-time three-point completion and unresolved C3 ordered pieces as BLOCKED unless actually derived.
