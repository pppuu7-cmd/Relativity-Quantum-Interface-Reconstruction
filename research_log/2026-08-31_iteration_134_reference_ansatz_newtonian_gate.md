# RQIR Research Log — Iteration 134

**Date:** 2026-08-31

## Starting authority

Recovered from repository front Iteration 132. The old post-Toy010 `C_a,gamma -> physical resource` task is already scientifically closed in Paper III and was not repeated.

## Iteration 133 — first real ansatz

Instantiated `ANSATZ-PQG-EFT-001`, a deliberately standard perturbative quantum-GR EFT reference with minimally coupled scalar matter.

Results:

- QG-001 PASS: physical perturbative state space specified with gauge/BRST separation;
- QG-002 PASS: one Einstein-Hilbert + scalar EFT action fixes gravity, matter and interaction;
- the model-derived RQIR hierarchy is `J=<T>`, centered `N`, retarded `chi^R`, and higher CTP correlators from the same dynamics;
- QG-007 FAIL because the ansatz is exactly comparator C5 at theory-class level.

Registered **CG-NG-003**: quantizing the weak metric / using standard perturbative quantum gravity cannot count as a novel Candidate Gravity relative to the C5 comparator. Detector optimization cannot repair exact theory-class degeneracy.

## Iteration 134 — QG-003

Derived the static weak-field limit from the declared normalization:

`G_00 ~= 2 nabla^2 Phi = 8 pi G rho`,

so

`nabla^2 Phi = 4 pi G rho`, `Phi=-GM/r`.

Regression with `G=6.67430e-11`, `M=1`, `r=2`:

- `4 pi G = 8.387172739141742e-10`;
- `Phi = -3.33715e-11`;
- `|a| = 1.668575e-11`.

QG-003 is therefore PASS for the declared low-energy reference domain. `conservation_bianchi_ward` advances to PARTIAL; quantum Ward/BRST and renormalized stress-tensor checks remain open.

## Scientific interpretation

This is not a new-physics result. It is the first successful use of the frozen Candidate Gravity gate system on an actual dynamics. The process correctly preserves a negative novelty result even while lower consistency gates pass.

## Next priority

Do not spend detector/Fisher resources on this reference branch's nonexistent C5-distinguishing beta direction. Highest-value next step is to instantiate a genuinely distinct ansatz at the dynamics level, then test QG-001/QG-002 before any RQIR discriminator optimization. The reference branch may separately be deepened through QG-004/QG-005/QG-006 for pipeline validation.
