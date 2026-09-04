# Candidate Gravity Research Log — Iteration 409

Date: 2026-09-04

Repository source of truth was read first: validated Iteration 406, active physical Iteration 407 for double-double index 4, and active structure-only Iteration 408 for indices 2 and 11. Recent commits and the latest recovery material were checked; no running heavy job was duplicated.

Iteration 407 has now completed and its raw artifact was independently consumed fail-closed. Run `33835806522`, job `100907970715`, artifact `9924759934`, artifact digest `sha256:eec059d48944771897d09341d888a4f0691664ce12f6c6258ff4cc3aad8947ae`, raw scientific JSON SHA-256 `bba7c203ca9694c70b79f762820cdcd26768ee6bb286d1dbc8c31c8ee93eee68`. The artifact authority audit agrees with this hash and declares scientific authority PASS.

For global double-double index 4 / class 5 / `q^2=-1`, `D_s TrU1^2 = +0.003562716046166582` with frozen scaled mass-step error `1.694511628814576e-05 < 2e-05`. Direct original-integrand cross-check reaches `2.0657185788308663e-09 < 2e-06`; denominator-affinity, held-out polynomial and Richardson checks pass by large margins; minimum analytic uncut separation is `0.11857147221810008`.

Therefore blocker 4 is removed without threshold weakening and without changing parent dynamics, routing, numerator, mass stencil or sign convention. The exact unresolved double-double physical set contracts from `[2,4,11]` to `[2,11]`. This is a scoped physical numerical PASS, not a full-model consistency result and not a Candidate residual. The `-i/4` effective-action weight remains separate.

Iteration 408 remains in progress and structure-only; it is not duplicated and cannot by itself remove indices 2 or 11.

MODEL_READINESS: 24%

Change: 0 pp. Removing one genuine numerical blocker is important progress but does not yet close a full readiness-rubric bucket; complete `Tr U1^2`, e=2 assembly, Source/Ward/K2 closure, fixed comparator quotient and robust residual remain downstream.
