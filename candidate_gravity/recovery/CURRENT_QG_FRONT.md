# Candidate Gravity Current Front

**Updated:** 2026-09-03  
**Infrastructure status:** READY — 100%  
**MODEL_READINESS:** **24%**  
**Permanent C5 reference:** `ANSATZ-PQG-EFT-001` v0.1  
**Active promotable ansatz:** none  
**Authoritative Candidate Gravity front:** **Iteration 331**

Repository commits, schema-validated Actions artifacts and recovery material are source of truth. A green workflow conclusion alone is never scientific authority.

## Authoritative state

- Iteration 246 closes generic connection `e=3,c=0`; do not reopen it.
- Iteration 307 freezes the complete eight-family `e=1,c=2` weight-completed actual `Tr U1` normalized cut.
- Iterations 308-310 freeze `e=2,c<=1` bookkeeping/typed U2 contract/U1^2 routing; physical U2 `V1_1/V1_2/H0/H1` remains BLOCKED.
- Iteration 312 freezes exact cubic `log det` topology.
- Iterations 314-319 derive/validate physical ghost and graviton components in common convention `D=4, Lambda=0, a=-1/2`.
- Iterations 320-324 establish common-background trace closure and freeze explicit ordered shifted propagators `G0(p+Q)` on the exact closed non-collinear triad.
- Iterations 325 and 327 remain preserved scoped gate-design FAILs; neither is a Candidate Gravity consistency FAIL.
- Iteration 328 proves the two translation-only triangle denominator orientations are one signed-affine integration family under `p -> -p + C`; denominator equivalence is not numerator equivalence.
- Iteration 329 closes the one-common-background H/N blocker and validates all 19 full-cubic routed insertion requests at correct `p+Q_before_insertion`. Run `33737812923`, job `100592429867`, artifact `9886457281`.
- Iteration 330 is preserved as a scoped gate-design FAIL. Its physical route maps and held-out numerator reconstructions passed, but an auxiliary assertion incorrectly required `q(TARGET)` to be nonzero despite exact trace closure `q1+q2+q3=0`.
- Iteration 331 corrects only that meta-assertion, leaving parent dynamics, topology weights, signed-affine maps, held-out points and threshold `5e-10` unchanged. Raw validated run `33742866100`, job `100608562495`, artifact `9888424625`, artifact digest `sha256:ab86eeeb40dcf4d1e0f9d6529e7560147c1ca83a0da9cb33da1247ad02027f28`, scientific JSON SHA-256 `813b7a770d8bcdd9b90b29bfe1027e92e20f23cf13ad3d0b844381faae1c7c29`. Maximum held-out numerator reconstruction error `1.3877787807814457e-17`; denominator-map error `1.1102230246251565e-16`.

Iteration-331 authority:
`PASS_PHYSICAL_CUBIC_DETERMINANT_NUMERATOR_SIGNED_AFFINE_FAMILY_RECONSTRUCTION_V2_CLOSED_TARGET_EXCLUDED_FROM_NONZERO_PROPER_SUBINDEX_CHECK`.

The determinant branch now has compatible authority for exact cubic logdet topology, one common closed H/N background, shifted propagators, arbitrary-incoming physical H/N insertions, signed-affine denominator quotient, route-specific transformed physical numerators and held-out family reconstruction.

## Active sectors

- connection `e=1,c<=2`: actual `Tr U1` cut frozen by Iteration 307.
- connection `e=2,c<=1`: physical U2 `V1_1/V1_2/H0/H1` remains independently BLOCKED; no zero-fill.
- determinant `e=0,c<=3`: physical cubic integrand is canonicalized into `1 singleton + 3 bubbles + 1 signed-affine triangle`.
  - singleton: scoped scaleless/local DR-zero-cut topology;
  - bubbles/triangle: cut-capable topology only; a nonzero discontinuity is not yet certified.

## Active computation / exact next gate

A prerequisite audit after Iteration 331 found that its frozen exact closed triad has `q_i^2>0` in signature `(-,+,+,+)`, so it is spacelike rather than a direct timelike-cut row. A direct timelike discontinuity must not be claimed from that fixture.

**Iteration 332:** rebuild the already-frozen route-specific numerator-family construction on the exact rank-2 closed timelike triad `q1=(1,0,0,0)`, `q2=(-0.4,0.1,0.1,0)`, `q3=(-0.6,-0.1,-0.1,0)`, for which all three `q_i^2<0`. Parent dynamics, common-background construction, logdet weights, shifted routing, signed-affine maps, held-out tests and threshold are unchanged.

The first run `33743095697`, job `100609311473`, produced no schema-valid scientific artifact: the numerical gate reached final JSON serialization and failed on a NumPy scalar (`ValueError: Circular reference detected`) before artifact upload. This is an operational serialization failure, not a scientific FAIL. The only repair casts the reported timelike invariants to builtin JSON scalars; no formula, fixture, threshold, routing or parent convention changed. Repair commit `b53b23733a718df3404fda4cda3554c14727ff72`.

The repaired gate is now queued as run `33743302046`, workflow head `b04ce242bf01d84a0588cf31ba8d14ee8a3fa124`.

If Iteration 332 passes raw artifact validation, the exact next gate is **Iteration 333:** scoped direct-timelike DR/discontinuity reduction of the three bubble families and one signed-affine triangle family on that certified timelike fixture, family by family. Certify zero/nonzero/BLOCKED discontinuity and classify pole/cut origin before any matched Source/Born subtraction.

The Iteration-297 evanescent/regulator warning remains binding for claims about the full finite DR remainder.

## Stable readiness rubric

- comparator foundation `24/25`
- robust unique residual `0/20`
- frozen parent dynamics/ANSATZ `0/20`
- consistency/positivity/Ward/causality `0/15`
- identifiability/Fisher `0/10`
- resource/experiment closure `0/10`

MODEL_READINESS: 24%

Change from Iteration 329: `0 pp`. The physical determinant numerator-family prerequisite closes, but no complete readiness bucket and no robust comparator-subtracted residual close.

## Retained guardrails

- Unsupported coordinates/kernels are `BLOCKED`, never zero-filled.
- Negative/scoped gate-design results remain preserved and are not retroactively edited into passes.
- Denominator equivalence is not numerator equivalence.
- Cut-capable topology is not a nonzero discontinuity certificate.
- Spacelike fixture data are not promoted to direct timelike-cut authority.
- Do not create `ANSATZ-003` before a concrete robust comparator-subtracted residual survives the fixed comparator quotient.
- Fisher/resources remain forbidden until a robust nonzero residual survives comparator subtraction.
- Source/Born subtraction only after pole/cut-origin classification in a matched observable.
- Full finite DR remainder remains subject to Iteration-297 evanescent/scheme authority.
- Blind heavy full-C5 remains unauthorized; closed C5 `e=3` authority is not reopened.

## Candidate state

No robust Candidate Gravity residual exists.  
`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Blind heavy full-C5 run: NOT AUTHORIZED.
