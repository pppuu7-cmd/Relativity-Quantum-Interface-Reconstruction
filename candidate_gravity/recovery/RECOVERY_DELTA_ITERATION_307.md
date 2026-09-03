# RQIR Candidate Gravity Recovery Delta — Iteration 307

Date: 2026-09-03

MODEL_READINESS: 24%

## Authority

Iteration 307 combines only schema-valid immutable scientific artifacts from Iterations 302 and 305 and closes the full eight-family `e=1,c=2` weight-completed `Tr U1` normalized-cut subsector at the frozen timelike row.

Freeze:

`PASS_COMPLETE_WEIGHT_COMPLETED_TRU1_E1C2_EIGHT_FAMILY_NORMALIZED_CUT_AT_FROZEN_TIMELIKE_ROW`

Validated Actions provenance:

- run `33703335692`
- job `100487121536`
- head `4c7fe35ddfa1084bfeb7785d7cd2012d87da81be`
- artifact `9874302096`, `iteration307-result`
- artifact digest `sha256:7e620a8bdf096db25f971a06a118d94cb67f138880fd3392a8378e235bb45e71`
- scientific JSON SHA-256 `3bc271990d63b90da42b339139b8ca68b8c9830242292adcb18696cc111ef22e`
- exactly one top-level JSON object, sentinel `307`, validator PASS.

## Numerical result

Frozen row: `s=0.016`, `ks^2=0`, `ks.ka=-0.1`, `ka^2=-0.016`, `kb^2=-0.216`.

- four bubble families, Iteration 302: `D_s TrU1_bubble = -0.010850153804447154`
- bubble fitted `1/epsilon` residue sum: `1.077895050620636e-09`
- four triangle families, Iteration 305: `D_s TrU1_triangle = -0.5048578516117335`
- triangle fitted `1/epsilon` residue sum: `2.1177964337894638e-10`
- complete eight-family `e=1,c=2` `Tr U1` normalized cut:

`D_s TrU1[e=1,c=2] = -0.5157080054161807`

- complete fitted `1/epsilon` residue sum: `1.2896746939995822e-09`.

The result is nonzero and numerically finite at the tested accuracy in the common HV-like CUT scope certified by Iterations 301 and 304.

## Guardrails

- This is `Tr U1` only, not the complete C5 three-point effective-action coordinate.
- The effective-action coefficient `-i/2` multiplying `Tr U1` is not folded into this stored coordinate.
- Connection `e=2,c<=1` (`Tr U2` and `Tr U1^2`) remains open.
- Determinant `e=0,c<=3` remains open.
- Source/Ward/contact completion and matched `K2` subtraction remain open.
- The full finite-amplitude scheme remains separately blocked; Iterations 301/304 protect normalized cuts only.
- No comparator-subtracted residual exists; no `ANSATZ-003`; Fisher/resources remain forbidden.

## Exact next gate

Freeze the exact operator and trace placement of the `e=2,c<=1` connection sector from the already-authoritative Vilkovisky definitions and Iterations 243–245. Enumerate the complete first-background-order cubic partitions of `Tr U2` and `Tr U1^2`, including trace weights and loop routing, before any heavy numerator computation.
