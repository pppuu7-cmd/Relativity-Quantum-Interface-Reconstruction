# Candidate Gravity Current Front

**Updated:** 2026-09-02  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 289**

## Current scientific state

Iterations 278–280 established translation-closed timelike C5 support, non-scaleless raised bubble/triangle families and the scalar retarded cut-support basis. Iterations 281–286 canonicalized the denominator sectors, corrected the incomplete topology-only numerator basis, and certified complete actual-oracle polynomial reconstructions: 70 monomials for each degree-`<=4` bubble and 210 for each degree-`<=6` triangle.

Iteration 287 completed the first actual coefficient-level DR tensor reduction. Both hard raised bubbles are nonzero:

- `C_a = -0.1247249362037728` at `q^2=0.41`;
- `C_b = +0.10231503679645079` at `q^2=0.21`;
- loop-reflection residuals: `0.0`;
- held-out numerator reconstruction errors: `7.52e-10` and `3.24e-9`.

Freeze:

`PASS_COMPLETE_70_MONOMIAL_BUBBLE_TENSOR_MOMENT_REDUCTION_NONZERO`.

The older exploratory bubble-a value `-0.64977` is superseded.

## Iterations 288–289 — complete triangle reduction and IR-pole correction

Iteration 288 successfully reduced all three complete 210-monomial triangle numerators with rank-0/2/4/6 tensor moments. The scalar `l^2` cancellation control reproduces the ordinary one-null two-mass triangle cut with absolute errors `7.84e-6`, `8.26e-6`, `1.36e-5`, and all loop-reflection residuals are `0.0`.

However, the raw actual-numerator epsilon scans are not finite as `epsilon -> 0`. The ordinary polynomial extrapolated values produced by the first Iteration-288 workflow are therefore **not physical finite coefficients**.

Iteration 289 performs the correct Laurent audit

`D_common(epsilon) = A/epsilon + B + O(epsilon)`.

Actual triangle residues:

- `(0,0.21)`: `A=-0.05908474654789776`;
- `(0,0.41)`: `A=+0.003959618177742245`;
- `(0.21,0.41)`: `A=-0.006164685444448067`.

Total:

`A_triangle,total = -0.061289813814603585`.

Controls:

- maximum absolute scalar-calibration pole residue: `6.06e-8`;
- minimum actual-sector pole magnitude: `3.96e-3`;
- maximum cubic-vs-quadratic residue difference: `4.46e-7`.

Thus the pole is robust and belongs to the current partial same-parent C5 `B3` block rather than to the numerical extrapolation procedure.

Freeze:

`PASS_DETECTED_ROBUST_UNCANCELLED_TRIANGLE_COMMON_CUT_IR_POLE__FINITE_COEFFICIENT_BLOCKED`.

The diagnostic Laurent finite triangle sum `-0.3171725193424992` and diagnostic bubble+triangle finite sum `-0.3395824187498212` are **not authoritative physical finite coefficients** while the total pole is nonzero.

## Current C5 blocker

`BLOCKED_LINKED_SOURCE_WARD_CONTACT_IR_POLE_CANCELLATION_BEFORE_FINITE_C5_T_CUT`.

The next problem is no longer numerator reconstruction or raw tensor reduction. The current partial three-point block has an uncancelled IR pole, so the missing source/Ward/contact completion and the same-parent linked two-point term must be included before a finite comparator coordinate is defined.

The frozen target remains

`T_cut = D Gamma3_ret,soft - W[D K2]`.

## Stable readiness rubric

- comparator foundation `24/25`;
- robust unique residual `0/20`;
- frozen parent dynamics/ANSATZ `0/20`;
- consistency/positivity/Ward/causality `0/15`;
- identifiability/Fisher `0/10`;
- resource/experiment closure `0/10`.

MODEL_READINESS: 24%

Change from Iteration 287: **0 percentage points**. Tensor reduction advanced substantially, but the physical linked C5 comparator coordinate remains blocked by the required IR/source/Ward completion.

## Retained guardrails

- Repository recovery files and recent commits are source of truth.
- Unsupported comparator coordinates are `BLOCKED`, never zero-filled.
- Keep consistency FAIL, exact comparator identity, regime-specific non-identifiability, operational BLOCKED, near-degeneracy and absence of novelty certificate distinct.
- Hard constraints precede profiling/Fisher.
- Do not create `ANSATZ-003` until a concrete residual survives the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero algebraic residual exists after comparator subtraction.
- Do not reintroduce box masters from unclosed routing.
- Apply loop shifts/reflections to primitive numerators before sector summation.
- Do not use the superseded denominator-only 9/50 bases.
- Do not use Iteration-288 ordinary polynomial epsilon extrapolations as finite triangle coefficients.
- Do not promote diagnostic finite Laurent terms before the total linked `1/epsilon` pole is cancelled.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.

## Iteration 289 authority files

- `candidate_gravity/results/iteration288_triangle_common_cut_raw_scan.json`
- `candidate_gravity/code/iteration288_triangle_common_cut_reduction.py`
- `candidate_gravity/code/iteration289_triangle_ir_pole_audit.py`
- `candidate_gravity/results/iteration289_triangle_ir_pole_audit.json`
- `candidate_gravity/C5_TRIANGLE_IR_POLE_AUDIT_ITERATION289.md`
- `candidate_gravity/recovery/RECOVERY_DELTA_ITERATION_289.md`
- `research_log/2026-09-02_iteration_289_triangle_ir_pole_audit.md`

## Exact next gate — Iteration 290

1. Return to the linked observable `T_cut = D Gamma3_ret,soft - W[D K2]`.
2. Inventory all source, Ward/covariantization, contact and same-parent two-point pieces omitted from the current scoped `B3` block.
3. Extract their `1/epsilon` hard-channel residues before computing finite terms.
4. Test cancellation against the measured current residue `-0.061289813814603585`.
5. Only after pole cancellation extract a finite C5 linked comparator coordinate and continue comparator subtraction.
6. `ANSATZ-003`, Fisher/resources and blind heavy full-C5 remain forbidden.
