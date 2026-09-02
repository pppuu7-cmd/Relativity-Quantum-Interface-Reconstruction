# Research Log — Iteration 281

Repository recent commits were treated as source of truth and showed the factual chain had advanced through Iteration 280 while `candidate_gravity/recovery/CURRENT_QG_FRONT.md` still displayed 274.

Iteration 278 certified nonzero translation-closed timelike B3/orbit trace across eight rows. Iteration 279 family-resolved the non-scaleless trace into bubble-a, bubble-b and triangle contributions. Iteration 280 established a three-dimensional scalar retarded cut-support basis on the same controlled timelike slice.

Iteration 281 tested and rejected a tempting but invalid shortcut: replacing the pre-integration non-scaleless family trace by three constant coefficients multiplying those scalar cut-support shapes. Best-fit coefficients are `(-0.18793735,-21.47800082,7.01934896)` with relative L2 residual `0.08675993597017234` and max absolute residual `3.39573961`.

Classification:

`FAIL_SCOPED_CONSTANT_MASTER_COEFFICIENT_SURROGATE_ON_TIMELIKE_SLICE`.

This is a scoped negative result, not a consistency FAIL. It establishes that actual kinematic coefficient functions must come from genuine p-dependent tensor/IBP reduction; they cannot be inferred from constant fitting of the family-summed pre-integration trace.

No new heavy Action was started; the repository's only recent workflow run is completed successfully.

MODEL_READINESS: 24%

Change: 0 percentage points. Comparator foundation remains 24/25 and robust unique residual remains 0/20; no readiness rubric block closed.

Exact next gate: reconstruct bubble-a, bubble-b and triangle p-dependent combined numerators in a finite Lorentz-covariant tensor/rational basis, validate on held-out loop momenta, then tensor/IBP reduce to actual coefficient functions multiplying the Iteration-280 scalar cut-support basis. Source/Ward/contact completion, Lorentzian comparator quotient, Fisher/resources and `ANSATZ-003` remain downstream/forbidden as previously frozen.
