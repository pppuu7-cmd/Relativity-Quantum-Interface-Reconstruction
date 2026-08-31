# RQIR Candidate Gravity Research Log — Iteration 200

Date: 2026-08-31

## Trigger

The hourly automation and the concurrent manual research path independently froze two admissible TT-polarization seed streams on the same v3 hard q geometry before their respective cubic C5 evaluations. Their numerical C5 soft2 vectors differ.

## Reconciliation

Do not overwrite or select a branch post hoc. Define:

- `v3-A`: automation seed stream;
- `v3-B`: manual seed stream.

Both are target-independent frozen observable protocols and both produce local C5 rank `4/12`.

Principal angles between their rank-4 nuisance images are

`[1.3074°,70.5977°,76.7404°,83.6588°]`.

Projector distances:

- Frobenius `2.37712`;
- operator norm `0.993882`.

Thus only one direction is nearly shared; the other three are strongly rotated. The apparent discrepancy is protocol sensitivity, not a physics contradiction.

The horizontal union of the two alternate subspaces has rank 8, but this is not eight C5 parameters. A same-parameter 24-row vertical-stack diagnostic remains rank 4 and has column-normalized condition `1749.72`.

## Status

✅ Concurrency discrepancy reconciled without deleting either branch.

✅ v3-A: valid rank-4 C5 protocol.

✅ v3-B: valid rank-4 C5 protocol.

✅ Polarization sensitivity quantified by principal angles/projector distance.

🟡 Future candidate gate must require polarization robustness, not post-hoc protocol selection.

🟡 AS/C3: BLOCKED, not zero.

❌ Candidate residual: not tested.

❌ `ANSATZ-003`: not created.

`MODEL_READINESS: 24%`

Readiness unchanged.

## Next gate

Freeze an explicit multi-protocol polarization-robustness rule before any candidate target is constructed. At minimum, a future candidate residual must independently survive the supported quotient in both v3-A and v3-B (or a separately preregistered multi-polarization protocol). Do not merge alternate subspaces as if they were independent theory parameters.
