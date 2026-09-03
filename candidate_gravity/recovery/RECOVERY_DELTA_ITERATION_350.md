# Recovery Delta — Candidate Gravity Iteration 350

Date: 2026-09-03

## Scope

Re-audit whether the Iteration-308/346 singleton-soft `A1=0` pruning survives the exact Iteration-348 matched timelike rebase before any physical U2 route substitution.

## Raw Actions authority

- run: `33782652005`
- job: `100739812001`
- artifact: `9904177872` (`iteration350-result`)
- artifact digest: `sha256:af10e53d0e1754e171b5b846fc9c646c40e48ffe5ed13db0fdad197f79cf176a`
- scientific JSON SHA-256: `280f1fe620d8b40a5458192c2cec4391d9c4763d793f12cc5a45a7489edb3704`
- workflow head: `c102bf08edc7427c8642277d3456133f811b60d6`

The raw artifact and authority audit were downloaded and inspected independently of workflow conclusion. Exactly one Iteration-350 object was present and `scientific_authority_pass=true`.

## Result

The timelike rebase does **not** preserve the previous singleton-soft zero:

- designated former soft mode `(1,0,0)` physical `A1` max abs = `0.15244821081057558`;
- exact-zero threshold = `1e-12`;
- other first-order modes are also nonzero: `0.00703595144704195` and `0.009534510280358474`.

Authority:

`PASS_AUDIT_TIMELIKE_REBASE_BREAKS_SINGLETON_SOFT_A1_ZERO__ITERATION346_12_SURVIVORS_NOT_PHYSICAL_AUTHORITY__REBUILD_30_ROUTE_CENSUS_NEXT`.

This is a negative but decisive scientific audit result. It does not fail Candidate Gravity. It invalidates only the attempted transfer of the Iteration-346 **12-route null-soft survivor subset** onto the exact timelike fixture. The 18 routes formerly killed by a soft-limit `A1=0` may not be zero-filled after timelike rebase.

## Next gate

Rebuild the matched-timelike physical cubic U2 route census from all 30 raw Iteration-308 placements. First classify structural exact component zeros with the physical Iteration-348 A1/A2 provider; then evaluate full route products with Iteration-349 N/Y/Hinv, exact shifted incoming momentum and Iteration-345 functional transpose before any family reduction or cut integration.

Iteration 351 has been launched for the structural 30-route census.

Unsupported remains `BLOCKED`; no Source/Born subtraction, no `ANSATZ-003`, no Fisher/resources, no blind full-C5.

MODEL_READINESS: 24%

Change from Iteration 349: `0 pp`.
