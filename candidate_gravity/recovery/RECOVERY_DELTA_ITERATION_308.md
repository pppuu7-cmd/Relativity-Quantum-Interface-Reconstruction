# RQIR Candidate Gravity Recovery Delta — Iteration 308

Date: 2026-09-03

MODEL_READINESS: 24%

## Authority

Iteration 308 freezes the exact cubic-background-order placement and singleton-null-soft pruning map for the remaining connection `e=2,c<=1` sector. It starts from the already-authoritative Iteration 307 full eight-family `e=1,c=2 Tr U1` cut and does not reopen or modify that result.

Freeze:

`PASS_E2C1_CUBIC_BACKGROUND_PLACEMENT_AND_NULLSOFT_PRUNING_AUDIT__EXACT_V1_H_KERNEL_IMPLEMENTATION_REMAINS`

Validated Actions provenance:

- run `33703692659`
- job `100488195810`
- head `2bfd7ac2cdab22aeca3f443aa329d012ab7ecb3b`
- artifact `9874425140`, `iteration308-result`
- artifact digest `sha256:bfbdb7e04859109b79f337132a29d94624fa226d089dbee9f95410a8c0dc53e3`
- scientific JSON SHA-256 `7623aa20ab729d2fe13a3da8f8d464431d32fc431b042c94a712a169f125db5b`
- exactly one top-level JSON object, sentinel `308`, validator PASS.

## Exact placement result

Frozen operator order:

- `U1 = N_L V2 N_R Y`
- `U2 = N_L V1_L H V1_R N_R Y`
- connection EOM-degree-2 contribution: `+(i/2) Tr U2 -(i/4) Tr U1^2`.

At cubic background order on distinct external legs `(s,a,b)`:

### Tr U2

- raw ordered primitive placements: `30`
- exact singleton-soft kills: `18`
- surviving ordered placements: `12`
- survivors by extra site: `2` each on `N_L`, `V1_L`, `H`, `V1_R`, `N_R`, `Y`.

### Tr U1^2

- raw ordered primitive placements: `42`
- exact singleton-soft kills: `26`
- surviving ordered placements: `16`
- surviving cyclic trace classes: `8`
- survivors by second-order extra site: `4` each on `V2`, `N_L`, `N_R`, `Y`.

## Frozen zero rule

Only a singleton null-soft leg on a linear EOM vertex `V1` or `V2` is killed through `E^(1)[h_s]=0`. Mixed soft-hard quadratic EOM vertices are retained. No unproven left/right or reversal quotient is applied to U2 survivors.

## Scientific scope

This is an exact placement/pruning certificate only. It does not numerically evaluate `Tr U2` or `Tr U1^2`, does not close the determinant sector, source/Ward/contact completion, matched K2 bridge, or comparator quotient, and is not a Candidate Gravity residual or novelty certificate.

## Readiness

MODEL_READINESS: 24%

Change from previous assessment: `0 pp`. Comparator foundation remains `24/25`; robust unique residual remains `0/20`. The e2c1 enumeration prerequisite is closed, but no stable readiness-rubric block has closed.

## Exact next gate

Derive/freeze the exact primary U2 index formula into an executable same-parent `V1-H-V1` kernel, including index spaces/transposes, flat `H0`, and first-background `H1/V1_2` ingredients required by the 12 surviving placements. Reuse authoritative U1 primitives for the 8 cyclic `Tr U1^2` classes. Only after exact trace/transpose/routing checks may scoped numerator reconstruction start.
