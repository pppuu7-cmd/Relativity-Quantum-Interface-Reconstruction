# Candidate Gravity Research Log — Iteration 405

Date: 2026-09-04

Fresh source-of-truth audit consumed `CURRENT_QG_FRONT.md`, `RECOVERY_DELTA_ITERATION_402.md`, the main Candidate Gravity research log, and commits through Iteration 404 before touching the active front.

## Iteration 399 raw result

Run `33828617524` completed. Artifact `9921602344`, digest `sha256:94e6a21b6f5609ac97b4ad7ea945d69745c8e9ceae8d805b850220aca96ea686`, was downloaded and parsed. Channel 5 of the 15-channel double-double `Tr U1^2` sector is `CONVERGED` at the unchanged frozen gate: `D_s TrU1^2 = 0.000119747535002548`, scaled convergence error `1.8393013149631406e-7`, result SHA-256 `63cf00714ce2c17abc5c0d9a223b5698df889c7d8586adac80c1cc74f5407e87`. This removes the former operational gap but does not resolve convergence-blocked indices 2,4,11.

## Iteration 400 raw result

Run `33829453920` completed. All four remaining repeated-U2 indices 14-17 have valid raw scientific JSON, PASS authority audits, `CONVERGED` status and Iteration-392 topology-mask consistency. No threshold or arithmetic was changed. Values: index 14 `-1.1341677230793501e-4` at `q^2=-0.34`; index 15 `-1.9874443441835922e-4` at `q^2=-0.14`; index 16 `+6.290774853610352e-4` at `q^2=-0.14`; index 17 `+6.894241423070089e-5` at `q^2=-1`.

The frozen Iteration-404 44/48 diagnostic sums therefore predict exact-48 repeated-cut sums `q^2=-1: 0.0004825971545254671`, `q^2=-0.34: -0.0005645318371195369`, `q^2=-0.14: -0.0014213811702222749`. Promotion waits for the new exact-index assembly authority.

## Iteration 405

Committed exact raw provenance inputs, a fail-closed exact-48 assembler, and a dedicated Actions workflow. Run `33832181526` is active from head `069ea4ad388f73998a8bca3f594d496f13710637`. The gate requires 48 unique indices 0..47, all CONVERGED, with q2 buckets kept distinct and no `+i/2` folding.

Iteration 401 analytic-azimuth structure oracle remains active independently. No duplicate heavy job was launched.

MODEL_READINESS: 24%. No readiness rubric point closes from numerical bookkeeping alone.
