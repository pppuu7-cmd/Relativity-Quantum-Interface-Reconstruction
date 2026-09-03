# 2026-09-03 — Iteration 304 triangle evanescent cut protection

MODEL_READINESS: 24%

Validated run `33702437466` / job `100484390001` / artifact `9873994705` at head `477e957511eb7e7051ecf0d8b61d14f279cd30dc` passes the fail-closed scientific sentinel/schema audit. Scientific JSON SHA-256: `27efdba75eee39591ed5be0d2a766627c8fb1bf38af901a7aa823c441fd1086d`.

Classification:

`PASS_HV_TRIANGLE_EVANESCENT_CUT_PROTECTION_ALL_274_HIDDEN_POLYNOMIAL_COEFFICIENTS_CUT_NULL_WITHIN_SCOPE`.

The 274 hidden HV-like polynomial coefficients counted in Iteration 303 are not inferred to vanish. Instead, all corresponding `mu^(2r)` layers are protected from contributing to the normalized common timelike discontinuity after the required dimension-shift screens. The certificate is explicitly cut-only and assumes regular same-parent D-dimensional coefficients near `D=4`.

Observed numerical maxima: master cut pole residue `8.606328628868795e-09`; hidden evanescent cut limit `8.606328628868795e-09`; hard-edge swap covariance residual `1.8705037518884637e-12`; ordinary triangle calibration residual `1.0668019356785408e-08`.

No robust comparator-subtracted residual exists. ANSATZ-003 remains uncreated and Fisher/resources forbidden.

Next gate: actual visible direct-timelike ordinary + three raised triangle numerator integrations from Iteration 295 in the same normalized-cut convention, with analytic-continuation-safe Feynman-parameter tensor reduction, raw epsilon scans, branch conjugacy and Laurent stability checks.
