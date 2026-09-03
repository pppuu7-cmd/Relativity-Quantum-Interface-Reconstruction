# RQIR Candidate Gravity Recovery Delta — Iteration 365

Date: 2026-09-03

MODEL_READINESS: 24%

## Scope

Independent prerequisite for the 18 timelike simple-simple cut channels inside repeated `(2,1,1)` physical `Tr U2` families. In these channels the unique double-pole momentum group remains uncut.

## Validated authority

- run `33801694987`
- job `100802477487`
- workflow/head commit `d1a0535ad5f37851614d58bc26ad40f71c27cc1d`
- code commit `0984d947075c1dbeaf7bdf5d277e299423035f7d`
- artifact `9911314614`, `iteration365-result`
- artifact digest `sha256:ab8b911fb3ea8c3f70da654dd9f7e552cb84512879fe433a275689dfb14dc26d`
- raw scientific JSON SHA-256 `a7da997b0faf9a3c9f50f6ae3fb251a52c1292a853f2bc4b1a37430ee10012e5`
- sentinel/schema and raw artifact audit PASS.

Freeze:

`PASS_U2_REPEATED_FAMILY_SIMPLE_SIMPLE_18_CHANNEL_PREREQUISITE__ALL_REGULAR`

## Result

- typed target channels: `18`;
- `REGULAR=18`;
- `BLOCKED=0`;
- exactly `6` channels in each external discontinuity bucket `q^2=-1`, `q^2=-0.34`, `q^2=-0.14`;
- minimum analytic full-sphere separation of the uncut double pole: `0.11857864376269048`;
- frozen separation threshold: `1e-10`;
- maximum scaled direct repeated factor versus auxiliary-mass derivative representation error: `1.2724338053133424e-11` under frozen `1e-8`.

The direct uncut repeated factor and the auxiliary-mass identity agree on deterministic on-shell angular fixtures. This is a prerequisite only; no physical normalized cut integral is frozen by this iteration.

## Exact next gate

Integrate the 18 normalized massless simple-simple cuts with the double pole retained directly as `D^-2`; independently reconstruct the same high-grid integral using the auxiliary-mass derivative representation; require angular convergence, representation agreement and cut-shell closure without weakening thresholds. Keep the three `q^2` variables separate.

No Source/Born subtraction. No effective-action coefficient folding. No `ANSATZ-003`. No Fisher/resources.

MODEL_READINESS: 24%
Change from prior assessment: `0 pp`; a physical-integration prerequisite closed but no complete readiness-rubric bucket and no robust comparator-subtracted residual closed.
