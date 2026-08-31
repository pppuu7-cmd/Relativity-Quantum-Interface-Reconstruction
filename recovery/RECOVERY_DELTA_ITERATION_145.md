# Recovery Delta — RQIR Iteration 145

**Date:** 2026-08-31  
**Authoritative change:** soft-lock protocol and class-envelope saturation diagnostic completed.

## Previous front

Iteration 144 defined the abstract post-Gaussian quotient and required `ANSATZ-003` to survive a finite comparator span after exact hard constraints.

## New files

- `candidate_gravity/POST_GAUSSIAN_PROTOCOL_ITERATION145.md`
- `analysis/post_gaussian_class_envelope_iteration145.py`
- `results/post_gaussian_class_envelope_iteration145.json`
- `research_log/2026-08-31_iteration_145_soft_lock_class_envelope.md`
- `recovery/RECOVERY_DELTA_ITERATION_145.md`

## New retained results

### NG-FUNNEL-004 — SOFT_LOCK_NOT_NOVELTY

For the standard massless-GR/diffeomorphism boundary:

- leading soft behavior is a universal consistency lock;
- tree-level subleading soft behavior is likewise a protected lock in the declared local-EFT setting;
- local EFT operators can modify subsubleading graviton soft terms.

Therefore `soft0/soft1` are not candidate novelty coordinates and `soft2` must be compared explicitly to C5 EFT freedom.

### NG-FUNNEL-005 — CLASS_ENVELOPE_SATURATION

Full post-Gaussian protocol:

`y=(norm,N2,chi1R,C3sym,chi2R_even,chi2R_odd,soft0,soft1,soft2,tensor_geo,threshold)`.

Hard locks:

`norm, soft0, soft1`.

Reduced dimension: `8`.

Deliberately independent per-coordinate class capability envelopes give:

- C3 rank `7`;
- C4 rank `7`;
- C5 rank `8`;
- combined rank `8/8`.

This is an over-complete structural diagnostic, not a physical model no-go.

## Interpretation that must survive recovery

Do **not** conclude that Candidate Gravity is impossible because the class-envelope span is full.

The point is the opposite: broad class labels are too unconstrained to be used as comparator tangent matrices. They destroy internal parameter relations and Ward identities.

From Iteration 146 onward, every comparator block must be derived from a finite fixed realization/truncation:

`V_C = partial y / partial theta_C`.

Unsupported higher-order comparator coordinates must be labeled `BLOCKED`, never silently set to zero.

## `ANSATZ-003` state

Still **not frozen**.

This is deliberate. Neither propagator novelty, nonlinearity alone, soft-theorem modification alone, nor an order-sensitive nonlinear coordinate alone has yet been certified outside fixed comparator spans.

## Exact restart instruction

Resume at **Iteration 146 — finite C5 post-Gaussian tangent**.

Priority order:

1. freeze C5 perturbative/EFT order and renormalization convention;
2. freeze finite kinematics for the Iteration-145 protocol;
3. derive the Einstein-Hilbert nonlinear baseline;
4. include finite local EFT directions affecting `soft2`/finite-momentum response;
5. include or explicitly BLOCK loop/nonanalytic columns;
6. produce first physical `V_C5` and rank certificate;
7. only after C5 is finite, proceed to C3 and nonlinear C4 representative tangents.

Do not create `ANSATZ-003` merely to keep model count moving. The next ansatz is frozen only after a residual target remains outside concrete comparator spans.
