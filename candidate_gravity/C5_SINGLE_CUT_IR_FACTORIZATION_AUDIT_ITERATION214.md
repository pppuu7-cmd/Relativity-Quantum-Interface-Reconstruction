# RQIR Candidate Gravity — Iteration 214

## Scope
Audit whether the logarithmic endpoint divergence of the frozen physical five-graviton total-s cut from Iteration 213 can be removed by a channel-local subtraction and then passed to the Iteration-210 regular+log extractor.

## Literature authority
Weinberg's gravitational IR theorem establishes cancellation of soft/collinear infrared singularities only for the properly assembled gravitational S-matrix treatment, including the relevant real-emission sector. Donoghue–Torma explicitly demonstrate the cancellation for graviton-graviton scattering after combining the virtual one-loop contribution with soft bremsstrahlung; their subtraction is tied to the on-shell Born amplitude and dimensional-regularization convention. Neither result licenses an arbitrary local counterterm on one isolated unitarity-cut channel.

## Direct endpoint certificate
Using the exact Iteration-213 KLT tree engine, not a cap fit, evaluate

`r_N(phi)=lim theta^2 I_cut(theta,phi)` and `r_S(phi)=lim (pi-theta)^2 I_cut(theta,phi)`.

At `epsilon=0.01`, with `theta=1e-4` and 32 azimuths,

- north mean residue: `-498.8422458 - 2582.0602955 i`;
- south mean residue: `-498.8422458 - 2582.0602955 i`;
- relative north/south difference: `~2.5e-14`;
- finite-theta azimuthal spread: `2.92e-4`.

The two endpoints therefore share the same leading collinear residue. Their predicted raw angular logarithmic coefficient is

`2 pi (r_N+r_S) = -6268.64 - 32447.13 i`,

with magnitude `3.3047e4`, consistent with the Iteration-213 cap-growth magnitude slope `3.2231e4` given finite-cap contamination.

## Classification
This quantitatively certifies the origin of the raw cut divergence, but does **not** provide a physical IR subtraction. The full amplitude/inclusive completion fixes how channel pieces and real emission combine. Therefore:

`SINGLE_CUT_LOCAL_SUBTRACTION = NOT_AUTHORIZED_AS_PHYSICAL_IR_COMPLETION`.

This is an operational/theoretical BLOCKED state, not a consistency FAIL, exact comparator identity, near-degeneracy, or novelty certificate.

## Retained results
- `IR-NG-003 — THE_TWO_COLLINEAR_ENDPOINTS_OF_THE_FROZEN_S_CUT_SHARE_THE_SAME_TREE_LEVEL_RESIDUE`.
- `C5-CUT-013 — THE_OBSERVED_CAP_LOG_IS_QUANTITATIVELY_EXPLAINED_BY_THE_DIRECT_TREE_ENDPOINT_RESIDUES`.
- `IR-NG-004 — UNIVERSAL_GRAVITATIONAL_IR_CANCELLATION_DOES_NOT_AUTHORIZE_AN_ISOLATED_CHANNEL_CUT_LOCAL_COUNTERTERM`.
- `NG-FUNNEL-071 — PHYSICAL_LOOP_CUT_IMPORT_REQUIRES_FULL_IR_SAFE_OR_EXPLICITLY_SUBTRACTED_AMPLITUDE_AUTHORITY_NOT_ENDPOINT_FITTING`.

## Consequence
Do not feed the cap-regulated or locally endpoint-subtracted single s-cut into the regular+log extractor. The next admissible route is either (a) a published/full one-loop five-graviton hard remainder in a declared IR subtraction convention, or (b) an inclusive IR-safe five-graviton observable where the real-emission completion and measurement resolution are explicitly fixed.

`MODEL_READINESS: 23%` — unchanged. The IR origin is now certified, but the physical standard-QG regular+log control remains incomplete.
