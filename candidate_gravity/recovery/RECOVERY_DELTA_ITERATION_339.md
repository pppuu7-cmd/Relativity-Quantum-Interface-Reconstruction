# RQIR Candidate Gravity Recovery Delta — Iteration 339

Date: 2026-09-03

MODEL_READINESS: 24%

## Authority

Iteration 339 closes only the graviton-Green `H0/H1` part of the older Iteration-309 physical `U2` blocker in the active connection `e=2,c<=1` sector. It does not invent or promote the still-missing physical `V1_1/V1_2` kernels and does not assemble an `U2` numerator.

Freeze:

`PASS_E2C1_U2_GRAVITON_GREEN_H0_H1_SAME_PARENT_ROUTING_BRIDGE__V1_KERNELS_REMAIN_BLOCKED`

Validated Actions provenance:

- run `33759581615`
- job `100662270347`
- head/workflow commit `b37be711ccb04db614c0159880731c9580118c47`
- code commit `e82ba168bad888f445a54a1df58613b668ff23e3`
- artifact `9894856112`, `iteration339-result`
- artifact digest `sha256:9e8593512de6fbef0238b0c1001950a34183d5f6484b179dd34c9e0f46528b05`
- scientific JSON SHA-256 `9cdbedc4897d4ed8be746ac0d2ac4fc3c73251b36dce23f7a243322ab779e318`
- exactly one top-level JSON object, sentinel `339`, `scientific_authority_pass=true`.

## Notation disambiguation and same-parent bridge

Iteration 309 denotes the field-space Green operator inside

`U2 = N_L V1_L H V1_R N_R Y`

by `H`. Iteration 319 instead uses `H` for the minimal graviton differential operator. Iteration 339 removes that collision by calling the frozen Iteration-319 differential operator `K` and its inverse field-space Green operator `G`.

For a physical Fourier insertion `q`, the routed first variation is frozen as

`G0(p) = K0(p)^-1`,

`G1(q;p) = -G0(p+q) K1(q;p) G0(p)`.

The left Green factor must carry the shifted output momentum `p+q`; replacing it by `G0(p)` is not an equivalent routing.

The executable gate uses the actual physical Iteration-319 `K1` matrix in the frozen convention `D=4, Lambda=0, a=-1/2`, reconstructs `K0` independently at both `p` and `p+q`, and checks the identity against an explicit two-momentum-sector block inverse.

## Numerical closure

For the frozen test route

- `p = (0.61,-0.33,0.24,0.52)`,
- `q = (0.27,-0.19,0.31,0.11)`,
- `p+q = (0.88,-0.52,0.55,0.63)`,

one has `p^2=0.0648` and `(p+q)^2=0.1954`, so both flat Green operators are nonsingular.

Checks:

- flat `K0(p)=p^2 I_10` error: `0.0`;
- flat `K0(p+q)=(p+q)^2 I_10` error: `5.551115123125783e-17`;
- maximum exact block-inverse routed `G1` error: `8.881784197001252e-16`;
- central finite-difference inverse derivative error: `1.7763568394002505e-15`;
- norm separating the correct shifted formula from the incorrect unshifted-left formula: `78.53690403309817`.

All frozen thresholds pass by many orders of magnitude.

## Scope consequence

The Iteration-309 blocker is narrowed:

- `U2 H0` flat graviton Green: FROZEN from the same parent;
- `U2 H1` first-background graviton Green: FROZEN from the same parent and explicit shifted routing;
- `V1_1` physical flat momentum kernel: still BLOCKED;
- `V1_2` physical mixed-background kernel: still BLOCKED;
- any required `N/Y` inverse/weight routing bridge for `U2`: not closed by this gate;
- physical `e=2,c<=1 U2` numerator: NOT AUTHORIZED.

This is not a Candidate Gravity consistency FAIL, comparator identity, non-identifiability result, near-degeneracy result or novelty certificate.

## Readiness

MODEL_READINESS remains 24%. Change: `0 pp`. A hard U2 prerequisite was removed, but no complete readiness-rubric bucket and no robust comparator-subtracted residual closed.

## Exact next gate

Derive and freeze same-parent physical `V1_1` and `V1_2` kernels in the exact Iteration-309 left/right index orientation. Separately bridge any required `N/Y` inverse routing before physical `U2` numerator assembly. Do not zero-fill missing kernels, do not perform Source/Born subtraction, and do not create `ANSATZ-003`, Fisher or resource calculations.

The already-running Iteration 335 determinant triangle `q^2=-1` convergence calculation remains independent and must not be duplicated.
