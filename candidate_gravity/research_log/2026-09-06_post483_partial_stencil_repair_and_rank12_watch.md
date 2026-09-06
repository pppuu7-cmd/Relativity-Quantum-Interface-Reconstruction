# RQIR post483 — partial-stencil repair and rank12 watch

Date: 2026-09-06

## Status

- MODEL_READINESS remains **24%**. No rubric component closed in this iteration.
- Certified occurrence-weighted mass-support remains **16/32 = 50%** pending manifest rank12 authority.
- Canonical manifest rank12 run `33997856739` / job `101391409387` remains the sole active heavy gate. The expensive stage is still in progress; raw-authority audit and artifact upload remain pending. No duplicate heavy run is launched.

## New finding: post483 exact-moment audit infrastructure bug

The first post483 partial-stencil moment workflow failed before result validation because the audit script contained incorrect exact expectations at polynomial moment k=5.

Frozen central4 nodes and coefficients:

- nodes: `[-2,-1,+1,+2]`
- coefficients: `[1/12,-2/3,+2/3,-1/12]`

Correct exact moments are:

- full stencil k=0..5: `[0,1,0,0,0,-4]`
- known rows i=0..2: `[1/12,7/6,1/3,2/3,4/3,-4/3]`
- missing row i=3: `[-1/12,-1/6,-1/3,-2/3,-4/3,-8/3]`

The previous script incorrectly expected `+8/3` and `-20/3` for the two k=5 partial contributions. The code was corrected and the workflow was strengthened to assert all six exact moments, including the missing-row vector. The rerun completed successfully and committed `candidate_gravity/results/post483_partial_stencil_moment_defect_audit.json`.

Classification: `PASS_PARTIAL_WEIGHT_COVERAGE_NOT_DERIVATIVE_COMPLETION__NON_PROMOTING`.

Scientific meaning is unchanged but now exact and CI-backed: a high absolute weight-coverage fraction for ranks 0..11 is not a fractional derivative-completion measure. The omitted outer BASE row is algebraically essential for restoring the derivative moment identities, so partial BASE sums must not be promoted to physical `D_s`.

## Post483 spectral partial diagnostic

The existing known-12 BASE spectral diagnostic remains non-promoting. It reports extremely strong MP80↔MP120 agreement for the known-node contribution, but a large partial cancellation-condition proxy and an incomplete final BASE u-row. Therefore it supports arithmetic stability of the known 12-node contribution only; it does not replace ranks 12..15 and cannot be compared directly with physical `D_s`.

## Guardrails retained

- no zero-fill of missing support;
- no u↔v symmetry substitution;
- no support reordering;
- no threshold weakening;
- no physical index-2 promotion from partial BASE information;
- no ANSATZ-003 / Fisher / resources work before a robust nonzero residual exists.

## Next gate

1. Wait on the canonical rank12 heavy run without duplication.
2. If rank12 raw-consumes PASS, update support to `17/32 = 53.125%` and advance exactly to rank13 `(u,v)=(+1e-5,-5e-6)` under the unchanged frozen protocol.
3. If rank12 BLOCKED, localize the first failing z/phi/radial sample and preserve the negative result without threshold or support changes.
4. Full BASE derivative authority still requires manifest ranks 0..15; full physical closure then additionally requires the frozen HALF assembly and BASE↔HALF comparison.
