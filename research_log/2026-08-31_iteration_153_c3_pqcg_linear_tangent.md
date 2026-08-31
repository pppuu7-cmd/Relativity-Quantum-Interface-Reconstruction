# RQIR Candidate Gravity Research Log — Iteration 153

Date: 2026-08-31

Started from authoritative Iteration 152 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_152.md`, the latest research log, and recent commits.

## Work performed
Instantiated the first concrete finite C3 comparator block instead of a class-capability mask.

Frozen comparator: `C3-PQCG-LIN-001`, the linearized covariant stochastic metric sector of postquantum classical gravity, with positive spin-2/spin-0 diffusion parameters `(D2,D0)` and a single declared state/noise convention.

Reused the Iteration-149 finite spacelike probe/smearing layer. Derived the supported objects from the same linear stochastic dynamics: source `J`, retarded `chi1R=G_R`, and symmetric metric noise `N_s=2D_s|G_R|^2`.

Unsupported nonlinear/post-Gaussian coordinates were kept BLOCKED rather than filled by zeros.

## Numerical certificate
For the traced `N2` coordinate,

`N2=A(5 D2 + D0)`, `A=258.83104475297773`.

Supported tangent `(N2,chi1R)` x `(D2,D0)`:

`[[1294.1552237648887,258.83104475297773],[0,0]]`.

Rank `1/2`; singular values `[1319.7845479190407,0]`.

## New negative/scoped results
`C3-NG-001 — ONE_NOISE_COORDINATE_COLLAPSES_TWO_DIFFUSION_DIRECTIONS`: the single scalar `N2` coordinate sees only `5D2+D0`; this is regime-specific non-identifiability, not a consistency FAIL.

`NG-FUNNEL-011 — PARTIAL_COMPARATOR_ROWS_ARE_NOT_ZERO_ROWS`: BLOCKED comparator coordinates may not be zero-filled before quotienting.

## Status
PASS_SCOPED:
- first finite C3 stochastic `N2/chi1R` tangent;
- explicit two-parameter convention and finite rank/SVD certificate.

BLOCKED:
- C3 `C3sym`, `chi2R_even/odd`, soft2/tensor/threshold completion;
- full C3 quotient;
- higher-local and loop/nonanalytic C5;
- nonlinear C4;
- nonlocal and asymptotic-safety fixed tangents.

No Fisher/resources. No `ANSATZ-003`.

## Next
Iteration 154: freeze and derive the first **nonlinear C3 extension** from the same covariant CQ path-integral family, including one explicit nonlinear drift/backreaction or non-Gaussian noise term. Compute at least one genuine `chi2R` or `C3sym` column from that same dynamics and test whether it adds rank beyond the linear `N2` direction. If a literature-explicit nonlinear finite truncation cannot be instantiated without extra conventions, record that as BLOCKED and move to the fixed nonlinear C4 comparator rather than inventing unsupported C3 columns.
