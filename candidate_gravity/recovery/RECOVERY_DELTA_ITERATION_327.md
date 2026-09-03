# RQIR Candidate Gravity — Recovery Delta Iteration 327

Date: 2026-09-03

## Authoritative change

Iteration 327 audits the compatibility of the Iteration-324 closed-triad denominator routing with the Iteration-326 full-cubic arbitrary-incoming-momentum H/N numerator certificate before any physical determinant trace is assembled.

Frozen result:

`FAIL_SCOPED_GATE_DESIGN_ITERATION326_NOT_COMMON_CLOSED_TRIAD_BACKGROUND`

Iteration 326 rebinds only incoming `p`. It directly loads graviton kernels from Iteration 319 and ghost kernels from Iteration 317 without rebinding their external `qs` or metric perturbations `hs` to one shared Iteration-322 closed-triad background.

## Exact evidence

Closed triad used by Iterations 322/324:

`[(0.27,-0.19,0.31,0.11), (-0.13,0.37,0.17,-0.29), (-0.14,-0.18,-0.48,0.18)]`.

Iteration-319 graviton fixture differs in its third mode, with maximum component difference `0.36`.

Iteration-317 ghost fixture differs from the closed triad with maximum component difference `0.34`.

The two historical fixtures also use independent background generators: seed/scale `319/0.12` for graviton and `317/0.2` for ghost.

Iteration 322 already defines the correct shared-background precedent: close the graviton triad first, then reconstruct ghost N from the same graviton `hs/qs/p` parent through the Iteration-320 shared assembly.

## Scope correction without retroactive editing

Iteration 326 remains preserved and valid for the narrower claim that all 19 full-topology requests pass arbitrary-incoming-`p` validation on their respective historical H and N fixtures. It is no longer promoted as a common-background closed-triad physical numerator certificate compatible with Iteration-324 denominators.

This is a scoped gate-design failure and dependent physical-trace BLOCKED state, not a Candidate Gravity consistency FAIL and not a physical H/N-kernel FAIL.

A structural denominator census may be retained: the 13 sequences reduce under proved loop translations to `1` singleton, `3` pair/bubble and `2` triple/triangle families. This is not a nonzero-cut certificate.

## Guardrails

- `ITERATION326_NOT_RETROACTIVELY_EDITED`
- `DO_NOT_COMBINE_DENOMINATORS_AND_NUMERATORS_FROM_DIFFERENT_BACKGROUND_FIXTURES`
- `ONE_SHARED_BACKGROUND_FOR_GRAVITON_AND_GHOST`
- `CUT_CAPABLE_TOPOLOGY_IS_NOT_NONZERO_DISCONTINUITY`
- no threshold weakening
- no Source/Born subtraction before origin classification
- no `ANSATZ-003`
- no Fisher/resources
- no blind heavy full-C5

## Readiness

MODEL_READINESS: 24%

Change from Iteration 326: `0 pp`. A real blocker was found, but no complete readiness bucket is newly closed or invalidated. Comparator foundation remains `24/25`; robust unique residual remains `0/20`.

## Exact next gate

Iteration 328: create a new common-background closed-triad arbitrary-incoming-momentum H/N gate using the Iteration-322 parent contract. Rebind both `qs` and incoming `p` for graviton H, reconstruct ghost N on exactly the same `hs/qs/p`, and revalidate all 19 full-cubic requests against same-parent exact geometry using unchanged frozen thresholds. Only after that PASS may physical determinant trace assembly resume.
