# Research log — RQIR Candidate Gravity Iteration 223

Date: 2026-09-01

MODEL_READINESS: 23%

Started from actual repository authority, not stale `CURRENT_QG_FRONT`: recent commits showed Iteration 222 as the latest completed calculation. Iteration 222 fixed the source-cut collinear residues to `R_in=R_out=-8 M_Born` across five scattering angles and both linear spin-2 polarizations.

This iteration defined the pointwise Born-fixed source hard kernel

`I_hard = I_cut - R/(1+n_z) - R/(1-n·n_out)`

without fitting any cap-regulated integral. Exact spherical annuli `rho in [delta/2,delta]` were integrated for `delta={0.08,0.04,0.02,0.01,0.005}` around both singular directions.

Across 20 endpoint tests the small-shell power is `1.9991758663...2.0066517080`; the maximum incoming/outgoing relative mismatch at the smallest shell is `2.84e-6`. Therefore the Born-subtracted cap contribution vanishes as `delta^2` in the scoped cross-kinematic protocol.

Classification: `PASS_SCOPED_LOCAL_IR_COMPLETION`, not a global hard-remainder closure and not Candidate Gravity novelty.

Retain `SRC-CUT-004`, `IR-NG-007`, `NG-FUNNEL-079`.

No `ANSATZ-003`. No Fisher/resources. GitHub Actions had no active runs, so no heavy computation was duplicated.

MODEL_READINESS: 23%

Readiness change: 0 percentage points. Local source-cut IR regulator removal is now certified, but comparator foundation is still incomplete because global bulk quadrature, AS real-time authority, and C3 ordered completion remain open.

Next gate: deterministic singularity-aware bulk quadrature for the already Born-subtracted MSSC-001 source cut, with independent convergence checks, followed only then by a nonanalytic-structure comparison to the separate pure-graviton positive control.
