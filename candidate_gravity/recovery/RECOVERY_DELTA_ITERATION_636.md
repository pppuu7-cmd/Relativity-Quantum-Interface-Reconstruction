# RECOVERY DELTA — Iteration 636

Date: 2026-09-09

Starting authority: Iter635 raw-validly proved that native positive-timelike `D_s` exists but the closed retarded `Gamma3` external channel and a one-parameter external kinematic family were not frozen. The exact three-mode fixture is only an anchor point, not itself a discontinuity trajectory.

Iter636 prospectively freezes `MSSC001-CLOSED-GAMMA3-INV-FAMILY-V1` before inspecting any bubble/triangle support or Candidate values. For scalar-denominator singularity geometry only:
- `s := q_s^2 > 0` is the external channel;
- `t := q_a^2=t0` and `u := q_b^2=u0` remain fixed at the exact-fixture anchor values;
- `q_s+q_a+q_b=0` exactly;
- `q_s.q_a=(u-s-t)/2`, `q_s.q_b=(t-s-u)/2`, `q_a.q_b=(s-t-u)/2`;
- scalar loop momentum `ell` is integrated independently and is never identified with Iter613 open-source `p0(s)`;
- `m_phi=0.7` is retained from MSSC001.

This contract is deliberately limited to Cutkosky/Landau singularity locations. Tensor numerator/polarization transport is downstream and may not be fitted to Candidate values.

Canonical raw authority: Actions run `34290339702`, head `3975d5cca742dc41e27491881caed05e9a48827a`, artifact `10081080144`, digest `sha256:cc8475ed718e6cfc09dd380ab67e2757fb9d758b1372a305199eabf40ba748e7`. Raw runtime SHA-256 `d296abe64cd8a891ee68548eb034f15539b1dc7117b1bf40e09beda116aef06b`; authority-audit SHA-256 `a1d9ac5d9e1b8836b77eb2699c9110aedbffecfad0802d1fb804b16efd0a3339`; audit classification `PASS_RAW_AUTHORITY_AUDIT_ITER636_CLOSED_GAMMA3_INVARIANT_FAMILY`, `failures=[]`.

Guardrails: Candidate values unused; bubble/triangle support was not inspected before freeze; normalization fit unused; `zero_fill=false`; Source/Born subtraction/native projection `NOT_PERFORMED`.

MODEL_READINESS: 24%.
Readiness change: 0 percentage points.

ANTI-IDLE: Iter637 is launched as a repository-wide fail-closed authority discovery for the exact fixture anchor `t0,u0`. It parses committed JSON, accepts only explicit four-vector triplets with exact momentum closure, computes `+---` invariant triples, preserves all candidates, and promotes an anchor only if the invariant triple is unique. No `t0/u0` is invented.