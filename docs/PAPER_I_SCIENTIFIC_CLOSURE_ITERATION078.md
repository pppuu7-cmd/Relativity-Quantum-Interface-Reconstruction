# RQIR Iteration 078 — Paper I Scientific Closure Audit

**Date:** 2026-08-30  
**Status:** scientific-scope closure for RQIR Paper I; not a quantum-gravity claim and not a substitute for a manuscript literature/novelty audit.

## 1. Question

Can the core Paper-I claim be stated as a clean finite-dimensional result rather than as a collection of Toy001–Toy010 examples, while preserving the strict boundary between an operational source discriminant and evidence for quantum gravity?

Yes.

Paper I studies what ordered source information can remain distinct under a declared finite calibration map. It does **not** claim that gravity necessarily transmits every such source functional.

## 2. Ordered second-order information

For fixed smeared source operators, write

`G^> = N + i D`,  
`G^< = N - i D`,

with `N` the centered symmetrized kernel and `D` the commutator/ordered-response kernel in the convention used by `FOUNDATIONS.md`. The retarded response is obtained from the commutator with causal support, up to the declared sign convention.

Thus matching one-point means and `N` does not, as an algebraic matter, imply matching `D`. Any equivalence requires an additional model identity, commutativity condition, spacelike-separation statement, equilibrium relation, or other assumption. Toy009/Toy010 provide an explicit finite-dimensional realization of this separation.

This is an information-structure statement, not an ontological statement about quantum geometry.

## 3. RQIR-THM-001 — finite nullspace response-discriminant existence

Let `V` be the real tangent space of Hermitian source-state perturbations after all exact hard linear constraints that are part of the declared preparation domain have been eliminated. Let

`A: V -> R^m`

be a finite linear calibration map with one-dimensional nullspace

`ker A = span{n}`,

and let

`c: V -> R`

be a linear response functional. Suppose:

1. `c(n) != 0`;
2. the nominal density operator `rho0` is in the interior of the physical state set on the retained finite-dimensional Hilbert space;
3. `n` is represented by a Hermitian traceless perturbation compatible with the already imposed exact constraints.

Then there exists `epsilon>0` such that

`rho_+ = rho0 + epsilon n`,  
`rho_- = rho0 - epsilon n`

are both physical states and satisfy

`A(rho_+ - rho0) = A(rho_- - rho0) = 0`,

while

`c(rho_+ - rho_-) = 2 epsilon c(n) != 0`.

### Proof

Because `rho0` is strictly positive, choose

`0 < epsilon < lambda_min(rho0)/||n||_op`.

Then Weyl's eigenvalue bound guarantees `rho0 +/- epsilon n` remain positive. Trace and any other exact linear preparation constraints are preserved because `n` lies in the reduced tangent space. Since `A n=0`, all declared finite linear calibration rows agree for the pair. Since `c(n) != 0`, the response differs. QED.

For centered covariance rows used in the mature toys, means are included among the declared equalities; the relevant symmetrized second-moment rows are linear expectations of fixed operators, so equality of those rows plus equality of the means gives equality of the corresponding centered covariance entries.

## 4. Toy009/Toy010 instantiate the theorem

Toy009 and Toy010 already verify the nontrivial numerical ingredients rather than assuming them:

- exact rank `24/25`;
- positive hidden pair;
- equality residuals below numerical `~1e-15` scale;
- equal selected mean/noise rows;
- nonzero opposite ordered response;
- detector-aware response survives the declared finite calibration map.

Toy010 further demonstrates that changing only finite calibration geometry rotates the one-dimensional null direction. Its analytic identity

`n' = -A^+ A' n`

and the bound

`||n'|| <= ||A'||/s_min(A)`

explain why calibration is an active design variable rather than a passive verification step.

## 5. What Paper I may now claim

The scientifically retained Paper-I statements are:

1. At second order, ordered source information contains distinct mean, symmetrized-noise and commutator/retarded-response sectors unless an additional physical identity relates them.
2. Finite calibration can leave a physical null direction on which an ordered-response functional remains nonzero.
3. Toy009/Toy010 provide constructive positive-state examples of that finite discriminant.
4. Calibration geometry can rotate that hidden direction and therefore alter detector-relevant response without changing the underlying source Hamiltonian.
5. Source, calibration and detector geometry must be co-designed.

## 6. What Paper I must not claim

Paper I does **not** establish:

- that gravity couples to `D` or `chi^R` in nature;
- that a nonzero commutator is evidence for quantized geometry;
- that the finite toys are relativistically complete stress-energy models;
- that the discriminant survives noisy source preparation or detector/systematic nuisances;
- that any empirical anomaly or new physics has been observed.

The last two items are precisely the bridge to Paper II and the later consistency programme.

## 7. Scientific-scope decision

**Paper I scientific scope is closed at Iteration 078.** No additional toy search is required to support the claims assigned to Paper I in `RQIR_ARTICLE_SERIES_ARCHITECTURE.md`.

Remaining work before journal submission is manuscript work: literature/novelty positioning, exposition, figures, compact derivations, references and independent reproduction. Those tasks must not be confused with an unresolved Paper-I scientific gate.

The correct endpoint is RQIR-NG-005: exact response separation is not yet statistical identifiability when the hidden source amplitude is uncertain.
