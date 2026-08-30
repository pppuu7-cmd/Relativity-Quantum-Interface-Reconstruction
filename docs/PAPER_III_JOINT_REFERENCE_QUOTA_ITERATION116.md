# RQIR Iteration 116 — Joint Reference Quota and No-Double-Counting Theorem

**Date:** 2026-08-31  
**Status:** Paper-III resource/scheduling closure; exact matrix quota result. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 115 reduced the same-state full-complex dual-tone transfer reference to the scalar common-gain rate relevant to the retained two-band science amplitude. The remaining scheduling risk is **double counting**: one physical reference acquisition may simultaneously constrain common transfer gain and several calibration-layer nuisance coordinates.

If the same acquisition is charged once as a transfer campaign and again as one or more calibration campaigns, wall time is overestimated. Conversely, if only marginal scalar rates are kept while a joint block has strong parameter correlations, wall time can be underestimated.

This iteration gives the exact matrix rule.

## 2. Required information matrix

Let `xi` denote all nuisance coordinates that a declared reference campaign is required to control. Construct a positive-semidefinite information requirement matrix

`H_* >= 0`

in those same coordinates. `H_*` may include, after the appropriate likelihood projection:

- the likelihood-derived common-gain requirement from Iterations 113–115;
- mandatory seven-layer calibration information requirements;
- any other reference quota that is truly obtained from the same physical block.

This notation deliberately does not assume that the requirements are diagonal or statistically independent.

Let one same-state reference campaign provide Fisher-rate matrix

`K_ref > 0`

per unit wall time in the same coordinates.

After reference time `T`, the accumulated information is

`T K_ref`.

The quota is satisfied iff

`T K_ref >= H_*`

in Loewner order.

## 3. RQIR-RESOURCE-082 — single joint-block quota theorem

Whiten by `K_ref` and define

`M = K_ref^(-1/2) H_* K_ref^(-1/2)`.

Then

`T K_ref >= H_*`

is equivalent to

`T I >= M`.

Therefore the exact minimum reference time is

`boxed{T_ref,* = lambda_max(K_ref^(-1/2) H_* K_ref^(-1/2))}`.

Equivalently this is the largest generalized eigenvalue of the pair `(H_*,K_ref)`.

This result is invariant under any nonsingular reparameterization of the nuisance coordinates.

If `K_ref` is singular, the quota is feasible only if every required direction lies in the identifiable support of `K_ref`; otherwise no finite reference time exists.

## 4. Diagonal simultaneous limit

If the required coordinates are independent in the declared basis,

`H_* = diag(h_1,...,h_n)`,

`K_ref = diag(r_1,...,r_n)`,

then RESOURCE-082 becomes

`boxed{T_joint = max_i h_i/r_i}`.

The same physical block accumulates all of the required coordinates at once.

By contrast, if each coordinate requires its own non-overlapping dedicated campaign, the wall time is

`T_sep = sum_i h_i/r_i`.

Hence

`boxed{1 <= T_sep/T_joint <= n}`.

The upper factor `n` is reached when all normalized burdens `h_i/r_i` are equal.

For a schematic common-gain plus seven scalar layer quotas, `n=8`, so an ideal perfectly simultaneous block can differ from a naive sum by as much as a factor of eight. This is an algebraic ceiling only; real RQIR layers are matrix-valued and may not share one measurement span.

### RQIR-RESOURCE-084 — simultaneous-reference saving bound

> When the same physical block independently accumulates several mandatory Fisher quotas, the correct wall time is set by the slowest normalized quota, not the sum of the individual times.

## 5. RQIR-NG-073 — marginal rates cannot replace the joint Fisher matrix

The diagonal `max` rule is invalid when the shared reference Fisher contains parameter correlations.

For example,

`K=[[1,rho],[rho,1]]`, `H_*=I`.

At `rho=0.8`, the marginal rates are both one, so a diagonal-only calculation would suggest `T=1`. RESOURCE-082 instead gives

`T_ref,*=5`.

The poorly measured eigen-combination is the bottleneck.

Therefore:

> **RQIR-NG-073:** a joint reference block must be propagated through its full Fisher matrix. Neither summing marginal calibration times nor replacing a correlated block by independent scalar rates is generally valid.

## 6. RQIR-RESOURCE-083 — multiple reference-campaign SDP

Suppose several physically distinct reference campaigns are available, with rate matrices `K_k` and nonnegative wall times `t_k`.

The exact minimum-time quota problem is

`boxed{min sum_k t_k}`

subject to

`sum_k t_k K_k >= H_*`,

`t_k>=0`.

This is a semidefinite program.

Its dual is

`boxed{max_Y tr(H_* Y)}`

subject to

`Y>=0`,

`tr(K_k Y)<=1` for every campaign `k`.

The dual matrix `Y` identifies the expensive nuisance combination that sets the reference wall-clock bottleneck.

A physical acquisition that jointly estimates transfer and calibration coordinates appears **once** as one `K_k` with all cross terms retained. Separate non-overlapping acquisitions appear as separate campaign matrices.

## 7. Relation to RESOURCE-057 campaign optimization

RESOURCE-083 is a mandatory-reference quota problem. RESOURCE-057 is the full science-profile campaign optimization.

Use them as follows:

1. If a reference block carries no science `beta` information and is imposed only to satisfy a calibration/control requirement, it may be handled by RESOURCE-083.
2. If the same block also carries science information or changes the science nuisance geometry, insert the entire physical block once into RESOURCE-057/064 and impose any mandatory quotas as explicit constraints. Do **not** optimize the block as science and then add the same wall time again as calibration.

This is the required non-double-counting rule for Paper III.

### RQIR-CAL-023 — one physical record, one wall-clock charge

> Information extracted from one acquisition may enter several Fisher subblocks, but its wall time is charged once. The full joint likelihood determines how much simultaneous information is actually available.

## 8. Consequence for Toy009/Toy014

The next detector-side architecture object is no longer

`T_transfer + sum_j T_cal,j`

unless the corresponding campaigns are known to be non-overlapping.

Instead construct, for each architecture,

`H_*,i`

and the physically available same-state reference rate matrices `K_k,i`. Then solve RESOURCE-083 or the constrained RESOURCE-057 problem.

Only after this step should the resulting detector-side rate be compressed into

`u=R_D,14/R_D,09`

and inserted into the final architecture relation with source rate ratio `v`, baseline source/detector ratio `z`, duty `delta`, and NG-030 uncertainty intervals.

## 9. What this iteration closes

Closed:

- exact no-double-counted time for one matrix-valued joint reference block;
- exact simultaneous-vs-separate time relation in the independent diagonal limit;
- a correlation counterexample showing why marginal rates are insufficient;
- the exact multi-reference convex/SDP formulation;
- the rule for deciding when a reference block belongs inside RESOURCE-057 instead of a separate time budget.

Still open:

- the actual nuisance-coordinate span of one same-state dual-tone block relative to the seven RQIR calibration layers;
- physical same-apparatus `K_k` for Toy009/Toy014;
- geometry/additive SI transduction and drift/reference Fisher;
- final robust numerical detector ratio `u`.

## 10. Readiness snapshot after Iteration 116

These percentages are project-management estimates, not statistical quantities.

- **Repository readiness for writing Paper III — scientific content:** **89%**.
- **Paper III submission-ready state:** **70%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **84%**.
- **Concrete Candidate-Gravity model itself:** **~10%**; no dynamical candidate has yet passed QG-001…QG-010.

Paper III is held below completion mainly by the missing same-apparatus matrix instantiation, geometry/additive SI control closure and the final robust Toy009/Toy014 detector ratio. Candidate-Gravity readiness is high as a testing framework, but the theory itself has not been constructed.

## 11. Next admissible gate

Determine the **rank/span compatibility** between the four-real same-state dual-tone observation and the nuisance subspace required by common transfer gain plus the seven calibration layers.

A repeated block with an unchanged Jacobian cannot gain new Fisher rank merely by increasing SNR. The next iteration should derive the minimum number of distinct reference settings needed to span the required calibration subspace and identify a structural no-go if one dual-tone setting is rank-deficient.

## 12. Reproducibility

Run

`python analysis/joint_reference_quota_iteration116.py`.

The script checks the generalized-eigenvalue theorem, diagonal `max` reduction, the `n`-fold simultaneous-saving bound, a correlated counterexample, coordinate invariance and Loewner monotonicity.
