# Recovery Delta — Iteration 572

## Closed scope
All frozen QUARTER support is raw-valid: `12/12 = 100%` new coordinates, `16/16 = 100%` full grid including the four exact HALF-overlap corners. Iteration 572 assembles this complete grid at the raw MP80/MP120 `(z,phi)` sample layer.

Observed sample-layer checks: all 80 assembled outputs finite; QUARTER MP80↔MP120 scaled max `1.2787277797888786e-68`; HALF↔QUARTER sample-layer scaled max `2.8064444557403413e-6`; independent direct/u→v/v→u/orbit assembly routes agree at `~1e-114`; raw-grid bilinear-fit diagnostic max `4.588236089297399e-15`.

## Critical scope guard
This authority is **pre-spectral**. The assembled rows are stripped-numerator angular/radial samples, not the final degree-4/affine-log spectrum-integrated `F(u,v)` and not physical scalar `D_s`. Therefore the sample-layer HALF↔QUARTER discrepancy is not the frozen Iteration-424 physical mass-step discrepancy, and the raw-grid bilinear diagnostic is not the frozen physical tensor-degree-(1,1) fit residual.

The machine-readable Iteration-572 result was corrected to state this explicitly and to keep the physical clauses BLOCKED rather than overclaiming PASS.

## Exact next gate
Use only the already raw-valid artifacts to reconstruct full spectrum-integrated `F(u,v)` at MP80/MP120 with the frozen Iteration-407 pipeline: phi-average at the five TRAIN_Z nodes, degree-4 interpolation, frozen affine coefficients and analytic affine-log recurrence. Then central4-assemble BASE/HALF/QUARTER physical `D_s` and evaluate the frozen mass-step/cross-precision/finiteness clauses. Separately recover the exact post-421/424 authority definition/mapping of the full tensor-degree-(1,1) clause before any physical promotion.

No new heavy mass-node run is currently needed. No u↔v substitution, zero-fill, smaller h, altered mass nodes/precision, threshold weakening, ANSATZ-003, Fisher or resources.

**MODEL_READINESS: 24%**.
