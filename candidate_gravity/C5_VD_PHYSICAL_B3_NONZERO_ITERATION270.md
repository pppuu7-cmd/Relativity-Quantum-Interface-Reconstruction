# RQIR Candidate Gravity — Iteration 270

## Explicit physical routed null-soft `B3=[U1 W]_3` nonzero certificate

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

## Starting authority

Iteration 269 corrected the condensed gravity gauge-density factor and restored endpoint-reversed transpose for physical routed `N2/Q2`. The exact remaining pre-tensor gate was therefore to construct the physical routed `A` coefficients, assemble the eight independent Iteration-266 `B3` transpose representatives, reconstruct their seven partners through endpoint reversal, and determine whether the complete 15-term null-soft numerator is explicitly nonzero.

This iteration performs that gate with no loop integration.

## Direct same-parent routed `A=R(DR)E`

Instead of expanding the 2/4/7 `K0/K1/K2` primitive library term-by-term, the numerical certificate evaluates the exact same-parent object

`A_{gamma delta}=R^i_gamma (D_i R^j_delta) E_j`

at finite background amplitudes and extracts its polarized Fourier coefficients. This is the unexpanded parent of the already frozen projected identity `A=K E`, so all `K0E3`, `K1E2`, and `K2E1` contributions are retained automatically.

Frozen ingredients:

- `D=4`, `Lambda=0`, DeWitt `a=-1/2`;
- linear covariant-metric split;
- the physical TT `s,a,b` modes of Iteration 264;
- affine diffeomorphism generator `R=L_xi g`;
- configuration-space Christoffel `Gamma(g)` with `c1=-1`, `c2=1/4`, `c3=1/4`, `c4=-1/8`;
- Einstein-action covector proportional to `sqrt(|g|) G^{mu nu}`;
- explicit condensed-index Fourier endpoints: for an `A_M` kernel mapping `p -> p+K_M`, the right gauge parameter carries `p` and the left/bra gauge parameter carries `-(p+K_M)`.

The extracted physical coefficients satisfy:

- `||A1[s]||_F = 1.00e-9`, numerically consistent with the frozen exact null-soft `A1[s]=0`;
- `||A1[a]||_F = 0.3538909325`;
- `||A1[b]||_F = 0.4373675400`;
- `||A2[s,a]||_F = 0.7472217396`;
- `||A2[s,b]||_F = 0.7529980727`;
- `||A2[a,b]||_F = 0.6505045916`;
- `||A3[s,a,b]||_F = 2.2278189997`.

`A3` permutation residual is `1.36e-10`. Endpoint-reversed transpose residuals are at or below `3.92e-7`, consistent with the finite-difference envelope.

## Exact 19 -> 15 null-soft realization

Expanding

`B=Q A Q`

with three distinct polarized background legs assigns every leg to the left `Q`, middle `A`, or right `Q`. Since `A0=0`, the generic cubic coefficient contains exactly

`3^3-2^3 = 19`

terms.

The four assignments with middle block `A1[s]` vanish in the exact null-soft limit. Numerically their total contamination has

`||B19-B15||_F = 2.56e-8`,

`max|B19-B15| = 1.11e-8`,

confirming the exact Iteration-261 19-to-15 reduction in the physical routed implementation.

## Eight independent transpose representatives

The eight Iteration-266 classes were evaluated directly in the forward `+K` sector. Representative Frobenius norms are:

1. `Q0 A3[s,a,b] Q0`: `1.8694069518`;
2. `Q1[s] A2[a,b] Q0`: `0.5904024824`;
3. `Q1[a] A2[s,b] Q0`: `1.2262842186`;
4. `Q1[b] A2[s,a] Q0`: `1.1798375441`;
5. `Q2[s,b] A1[a] Q0`: `0.4975674257`;
6. `Q2[s,a] A1[b] Q0`: `0.5149554056`;
7. `Q1[s] A1[a] Q1[b]`: `0.3155077936`;
8. `Q1[s] A1[b] Q1[a]`: `0.4095295780`.

Every representative is explicitly nonzero.

The seven partner terms were reconstructed and independently checked using endpoint reversal into the real `-K` Fourier sector, not by a raw same-routing matrix transpose. The worst representative/partner transpose residual is

`3.29e-7`.

The complete 15-term forward numerator obeys

`max|B15(+K)^T - B15(-K)| = 3.25e-7`.

The direct 15-term enumeration and exact `1 + 7*(X+X^T)` class reconstruction agree to

`2.78e-16`.

Thus both Iteration-266 transpose reduction and Iteration-267 endpoint-routing semantics survive explicit physical realization with the corrected Iteration-269 orbit metric.

## Explicit nonzero physical cubic numerator

At the frozen generic loop momentum

`p=(0.7,-0.4,0.5,0.9)`,

the complete surviving physical numerator is

`||B3[s,a,b]||_F = 2.2209140981`,

`max|B3[s,a,b]| = 1.3471946832`.

This is far above all numerical regression envelopes.

Step variation confirms stability:

- `(h_A2,h_A3)=(1e-3,2e-3)`: `||B3||_F=2.2209140431`;
- `(7e-4,1.5e-3)`: `2.2209141958`;
- `(5e-4,1e-3)`: `2.2209140981`;
- `(3e-4,8e-4)`: `2.2209142212`.

Freeze:

`PASS_SCOPED_PHYSICAL_ROUTED_NULLSOFT_B3_EXPLICIT_NONZERO_AND_TRANSPOSE_VALIDATED`.

## What this does and does not establish

This closes the algebraic nonzero gate that previously forbade tensor reduction. The physical same-parent finite-cubic `U1 W` numerator is no longer merely `BLOCKED_NOT_ZERO`; one explicit generic physical routed point is certified nonzero.

However, this is **not yet the final C5 RQIR comparator coordinate**. The following remain mandatory:

1. tensor/master-integral reduction of the routed numerator;
2. regular+log/nonanalytic extraction in the frozen hard channel;
3. source/Ward/contact completion appropriate to the linked observable;
4. Lorentzian hard-channel discontinuity projection;
5. IR/hard-remainder control and comparator normalization;
6. only then subtraction against C3/C4/nonlocal/asymptotic-safety authority and residual assessment.

Therefore this result must not be promoted to `ANSATZ-003` or a Candidate Gravity residual.

## Computational consequence

A **scoped tensor-reduction run is now authorized** for this frozen C5 numerator. A blind heavy full-C5 campaign is still not authorized; the next calculation should reduce the already-certified numerator, not broaden the model space.

Retain umbrella status

`BLOCKED_4D_EINSTEIN_VD_TENSOR_REDUCTION_SOURCE_PROJECTION_AND_LORENTZIAN_HARD_CHANNEL`,

with the old `RESOLVENT_VERTEX_LIBRARY` component now algebraically closed for this scoped null-soft `B3` target.

## Readiness

`MODEL_READINESS: 24%`

Change from Iteration 269: **0 percentage points under the frozen rubric**. This is a major internal milestone, but comparator foundation remains `24/25` until the numerator is converted into the actual physical C5 comparator coordinate. Robust unique residual remains `0/20`.

## Exact next gate — Iteration 271

Perform a scoped tensor/master-integral reduction of the certified routed `B3[s,a,b]` numerator at the frozen null-soft kinematics. Preserve the raised bubble/triangle topology bounds from Iterations 245/250. Extract the nonanalytic hard-channel structures needed for the linked `T_cut` coordinate before any source projection. Do not launch Fisher/resources or create `ANSATZ-003`; do not broaden to a blind heavy full-C5 run.
