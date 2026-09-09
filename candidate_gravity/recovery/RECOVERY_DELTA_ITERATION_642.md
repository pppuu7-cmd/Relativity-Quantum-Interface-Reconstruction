# RECOVERY DELTA — Iteration 642

Date: 2026-09-09

Authoritative predecessor: Iter641 raw-valid denominator spectral-kernel contract.

Canonical Iter642 Action: run `34298137965`, head `0765961e3fd62af4e404244004a0be9e3662de82`, artifact `10083900312`, digest `sha256:76f329b38a557092a34e5d0a75d33760c769b5b5e11f30e7fc28e98d7e1d8735`, conclusion `success`. Independent raw artifact consumption verified `result.json` SHA-256 `f67a8d48e277cd0a062718866165ffe5c56b1bf0e3134fe3ed89f58b51234fc7`, `authority_audit.json` SHA-256 `f26aecac014fd521d1dd4de36f3f0c4c7cae3eb56434a76ef19c7ab8cc2a2dcb`, `failures=[]`.

Authority: the exact same-parent MSSC001 vertex machinery needed for explicit cut numerators is machine-recoverable from committed authority. `analysis/source_full_cubic_routed_assembly_iteration594.py` provides reusable `K1`, `K2`, `K3_mixed`, `first_coeff`, `mixed_coeff`, `mdot`, `G` and routing/assembly machinery with all three families present. Source SHA-256 recorded by raw audit: `21307dadff9bc0272d640bec6ae401608c42bcb9ba49c19e23e32a3b1f9d174a`.

Classification: `PASS_ITER642_SAME_PARENT_VERTEX_AUTHORITY_MACHINE_RECOVERABLE__NON_RESIDUAL`.

However, explicit closed-loop numerator evaluation along variable `s` also requires the external metric-tensor/polarization continuation along the Iter636 invariant family. Iter368/588 supplies an exact tensor fixture at `s0`, but this must not be extended post hoc without a frozen continuation contract. Iter643 has therefore been launched to audit that prerequisite.

Guardrails unchanged: `zero_fill=false`; Candidate values unused; Source/Born subtraction `NOT_PERFORMED`; native Y/T_cut projection `NOT_PERFORMED`; comparator quotient `NOT_PERFORMED`; no ANSATZ-003; no Fisher/resources.

MODEL_READINESS: 24%
Readiness change: 0 percentage points.

Exact next gate: raw-consume Iter643. If external tensor trajectory authority is absent, prospectively derive/freeze the minimal Lorentz-covariant continuation consistent with the exact s0 fixture and fixed `(t0,u0)` before viewing any cut-numerator outputs. If already frozen, proceed directly to explicit K1/K2 and K1^3 retarded cut-numerator contractions.
