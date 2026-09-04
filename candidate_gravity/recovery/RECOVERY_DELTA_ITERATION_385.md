# Candidate Gravity Recovery Delta — Iteration 385

Date: 2026-09-04

MODEL_READINESS: 24%

## Scope

Resource-only repair of operationally cancelled Iteration 379 for the first prospectively frozen physical `Tr(U1^2)` double-double channel. The Iteration-379 physics arithmetic, mixed auxiliary-mass derivative, radial Richardson rule, angular grids, signs and thresholds are unchanged. Only independent angular points are parallelized with ordered `fork` mapping; a fixed serial-vs-parallel oracle is mandatory.

## Raw Actions authority

- run: `33817847310`
- job: `100853847266`
- workflow head: `dd657f3a1ba115e57fdd0fc5c8b3f2c2fe31615d`
- code commit: `bd8f33cd3135966050309711c0a151c445f90f7b`
- artifact: `9917692253` (`iteration385-result`)
- artifact digest: `sha256:7fd2afc6d5f38422625c7a6d3a81439767d3515e39c6717c7f48ce6704726d0b`
- raw scientific JSON SHA-256: `9455e75eaf0e12510113de3bf9e644866a1668ffcc3b629ef8cf15449304c966`
- authority audit: `scientific_authority_pass=true`, valid single top-level JSON, sentinel `385`.

## Result

Classification:

`PASS_TRU1SQ_DOUBLE_DOUBLE_PARALLEL_ONE_CHANNEL_PILOT__CONVERGED`

Selected channel:

- frozen rule: first double-double channel in Iteration-372 order;
- class id: `1`;
- `q^2=-1`;
- multiplicities `2 x 2`;
- status: `CONVERGED`;
- normalized operator coordinate:

`D_s TrU1^2_double-double = -0.0021448992853041436`.

Diagnostics:

- scaled angular/step convergence error: `1.7976503775178967e-06 < 2e-5`;
- max radial Richardson scaled error: `5.16535599015544e-15 < 5e-4`;
- max cut-shell absolute error: `2.639515599904378e-16 < 2e-10`;
- minimum Kallen function: `0.99996 > 0`;
- serial-vs-parallel oracle scaled error: exactly `0.0 < 2e-13`;
- runtime: `944.963664277 s`.

`minimum_sampled_uncut_abs_denominator=Infinity` is expected for this two-group channel: after both repeated groups are cut there is no remaining uncut denominator; it is not a singularity or missing-value zero certificate.

## Interpretation

This closes the complete physical mixed-derivative pipeline for one prospectively selected double-double channel and proves the Iteration-379 cancellation was operational/resource, not a physics failure. It does **not** authorize extrapolating the value to the remaining 14 channels.

The measured runtime and exact serial-parallel identity now justify a prospectively frozen complete-15 architecture with one double-double channel per job, identical numerical physics and bounded parallelism. Any later nonconvergent channel remains `BLOCKED_CONVERGENCE`; thresholds must not be weakened.

No effective-action `-i/4` weight is folded here. Distinct `q^2` coordinates remain separate. No Source/Born subtraction. No `ANSATZ-003`. No Fisher/resources.

## Readiness

MODEL_READINESS: 24%

Change: `0 pp`. A hard numerical sub-sector architecture is validated, but complete `Tr U1^2`, complete `Tr U2`, the linked source/Ward/K2 relation and robust comparator-subtracted residual remain open.
