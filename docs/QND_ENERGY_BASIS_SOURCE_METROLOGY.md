# RQIR Iteration 047 — QND Energy-Basis Source Metrology

**Date:** 2026-08-29  
**Scope:** Toy009 hidden-amplitude/source-calibration layer after reciprocal-linear backaction gates.  
**Status:** constructive source-metrology result plus same-copy negative gate; no hardware implementation and no new-physics claim.

## 1. Motivation

Iterations 043–046 showed that strong same-copy force monitoring is expensive in coherence: in the reciprocal linear quantum-limited class, obtaining enough mean Fisher inevitably attenuates the ordered-response signal and worsens the profiled nuisance geometry.

A natural escape is a QND/backaction-evading source observable.

For the current Toy009 source Hamiltonian

`H=diag(1,2,3,4,6)`,

the spectrum is nondegenerate. Therefore every exact Hermitian observable satisfying

`[M,H]=0`

is diagonal in the energy basis.

Iteration 047 asks:

1. can the full energy-diagonal/QND observable sector constrain the remaining relational source null;
2. how much hidden-amplitude information is available from a simple energy-basis population measurement;
3. whether such QND measurement is safe on the same science copy.

## 2. QND diagonal tangent dimension

The Hermitian commutant of nondegenerate `H` is five-dimensional: all diagonal matrices.

After exact trace and energy directions are removed, the hard QND calibration sector has dimension

`5-2=3`.

For the centered finite-reference relational branch at `y_ref=-4`:

- relational hard rank is `22/23`;
- adding a complete three-row diagonal QND basis gives `23/23`.

Thus the current residual relational null is **not invisible to all exact-QND observables**.

The QND basis projection of the current hidden state has norm

`~0.0864047`,

so the hidden direction carries a finite diagonal population component.

### RQIR-CAL-016 — QND diagonal completion of the current relational null

> In Toy009, the one-dimensional hard null left by the finite-reference relational calibration can be removed locally by a complete set of three independent energy-diagonal observables commuting with the source Hamiltonian.

This is finite-dimensional local calibration completion, not global tomography and not yet an experimental protocol.

## 3. Simple energy-basis population Fisher

The hidden family is

`rho(a)=I/5+a Delta0`,

with nominal branch amplitudes `a=+/-0.08`.

A projective measurement in the energy basis gives probabilities

`p_i(a)=1/5+a (Delta0)_ii`.

Its classical Fisher for physical amplitude `a` is

`F_E^(a)=sum_i (Delta0_ii)^2/p_i(a)`.

Numerically:

- plus branch: `F_E^(a) ~= 1.46748`;
- minus branch: `~1.49674`.

Transforming to the current fractional amplitude `alpha`, `a=0.08 alpha`:

- plus branch: `F_E^(alpha) ~= 0.00939188` per accepted copy;
- minus branch: `~0.00957913`;
- one independent plus/minus pair: `~0.0189710`.

The full Toy009 QFI is

`F_Q^(alpha) ~= 0.0849324`.

So a simple plus-branch energy population measurement extracts about

`boxed: 11.1%`

of the full QFI per copy.

### RQIR-PREP-002 — energy-basis metrology is a finite, simpler preparation channel

> The hidden Toy009 amplitude does not require an ideal `Delta0`-eigenbasis measurement to be observable. A projective energy-basis population measurement already carries finite Fisher, about 11% of the full QFI per plus-branch copy, and is exactly QND with respect to the isolated source Hamiltonian.

This materially weakens the practical source-metrology concern left open by Iteration 020, although physical implementation on a massive source is still an experimental gate.

## 4. Current source-copy requirements

For the centered best4 branch residual

`C_alpha ~= 0.05006144`,

energy-basis population metrology needs only approximately

- `5.33` accepted plus-branch copies, or
- `2.64` independent plus/minus pair equivalents.

For comparison, the no-extra-force-covariance branch requirement

`C_alpha ~= 4.55511`

would need about

- `485` plus-branch copies, or
- `240` plus/minus pairs.

The generic isolated-amplitude 90% requirement `C_alpha=9` would need about

- `958` plus-branch copies, or
- `474` plus/minus pairs.

These are still ideal information counts: acceptance, readout efficiency, reset time and actual energy/population measurement time must multiply the wall-clock cost.

## 5. QND does not mean response-preserving

A projective energy measurement is QND relative to `H`, but it dephases all energy coherences on the measured copy.

Applying complete energy-basis dephasing to the current Toy009 hidden pair before evaluating the D2 ordered-response detector gives

- response-norm retention `~0.29848`;
- response-direction alignment `~0.82052`.

So the same-copy response is strongly damaged.

### RQIR-NG-023 — QND is not equivalent to ordered-response nondemolition

> An observable commuting with the source Hamiltonian can still destroy the coherences required by the ordered-response discriminator. QND relative to `H` is therefore insufficient as a shared-science criterion; the measurement must also preserve the detector-relevant response/nuisance subspace.

For the current Toy009 energy measurement, the correct use is therefore **independent/sacrificial source metrology**, not strong measurement on the science copy.

## 6. Resource implication

This result strongly reinforces the current hybrid architecture:

`best4 covariance/science + small independent source metrology`.

The fifth covariance row was previously shown to cost roughly `9.55e5` additional shared detector trajectories merely to remove the tiny best4 residual `C_alpha`.

By contrast, ideal energy-basis population metrology supplies that residual in only a few accepted source copies.

Therefore the fifth covariance row is even less attractive unless one source-metrology cycle is extraordinarily slower than a detector trajectory.

The comparison should now use the **energy-basis metrology rate**, not the unattainable/full-QFI `Delta0` eigenbasis as the only preparation benchmark.

## 7. What remains open

Energy-basis measurement is mathematically simple in the five-level model, but a physical source implementation still needs:

- a clear mapping from the five source energy modes to experimentally distinguishable preparation/readout outcomes;
- acceptance and reset rates;
- proof that source metrology does not correlate with gravitational detector nuisances;
- extension beyond the five-level nonrelativistic toy source;
- apparatus stress-energy/conservation and relativistic consistency.

## 8. Reproducibility

Code:

`analysis/qnd_energy_basis_source_metrology_iteration047.py`

The script verifies hard-rank completion by the three-dimensional QND diagonal sector, computes plus/minus energy-basis Fisher, converts it to the fractional-amplitude coordinate, compares it with the full QFI, and quantifies same-copy response destruction under projective energy dephasing.

## 9. Next gate

Replace the abstract source-metrology rate `R_P^(alpha)` in the D2 wall-clock comparison with an explicit energy-basis rate

`R_E^(alpha)=p_E eta_E F_E^(alpha)/t_E`,

and recompute the best4-vs-best5/resource phase boundary. This will show quantitatively how slow an energy/population readout would need to be before the fifth covariance row becomes preferable.