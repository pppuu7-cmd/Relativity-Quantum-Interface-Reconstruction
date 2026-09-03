# RQIR Candidate Gravity — Iteration 318

Date: 2026-09-03

MODEL_READINESS: 24%

## Authoritative predecessor
Iteration 317 froze full physical ghost N1/N2/N3 component authority. The determinant branch remained BLOCKED on executable physical graviton H1/H2/H3.

## Scientific step
The same-parent local graviton authority was re-read directly from Giacchini, de Paula Netto and Shapiro, Phys. Rev. D 102, 106006 (2020), arXiv:2006.04217v4. In the frozen Vilkovisky choice a=-1/2, the local operator is H=-(I Box+Pi). For D=4 and Lambda=0, the paper's coefficients satisfy exactly p1=p2=p3=1 for every allowed nondegenerate linear parametrization (gamma1 != 0 and gamma1+4 gamma2 != 0).

Therefore the physical local graviton potential specializes without any post-hoc gamma2 choice to

Pi^{munu}_{alphabeta} = 2 R^mu_.alpha^nu_.beta - 1/2 g^{munu} R_{alphabeta} - 1/2 g_{alphabeta} R^{munu} + 1/4 g^{munu} g_{alphabeta} R - 1/2 delta^{munu}_{alphabeta} R.

A reproducible SymPy check is stored at candidate_gravity/code/iteration318_graviton_operator_specialization_check.py; the frozen result summary is candidate_gravity/results/iteration318_graviton_operator_specialization_summary.json.

Freeze:
`PASS_D4_LAMBDA0_VD_GRAVITON_OPERATOR_PARAMETRIZATION_INDEPENDENT_SPECIALIZATION__H123_ROUTING_REMAINS_BLOCKED`.

## Scope boundary
This closes the operator-form/linear-parametrization ambiguity for the local graviton determinant sector. It does NOT yet derive executable H1/H2/H3. In particular, the covariant Box acting on symmetric tensors and all curvature terms in Pi must still be expanded under g=eta+kappa h with one explicit 10-component basis and momentum routing. No missing Hn is zero-filled, and Iteration-312 determinant insertion remains forbidden until independent routing validation passes.

This is not a Candidate Gravity residual, not a comparator identity, not a consistency FAIL, not regime-specific non-identifiability, not near-degeneracy, and not a novelty certificate. ANSATZ-003 remains NOT CREATED; Fisher/resources remain forbidden.

## Exact next gate
Construct H[g]=H0+kappa H1+kappa^2 H2+kappa^3 H3+... from the now-frozen D=4,Lambda=0 operator, including the full symmetric-tensor covariant-Box connection terms and Pi curvature expansion. Use an explicit 10-component symmetric-tensor convention and independently validate the series on non-collinear multimode backgrounds against a direct exact-geometry oracle before inserting H1/H2/H3 into the Iteration-312 cubic logdet topology.

MODEL_READINESS: 24%
Change from Iteration 317: 0 pp. A genuine determinant authority ambiguity is closed, but no readiness-rubric component and no robust comparator-subtracted residual is yet closed.
