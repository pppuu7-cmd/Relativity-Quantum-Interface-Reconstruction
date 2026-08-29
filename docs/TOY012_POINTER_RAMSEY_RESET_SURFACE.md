# RQIR Iteration 058 — Toy012 QND Pointer vs Ramsey Reset Surface

**Date:** 2026-08-30  
**Scope:** independent/sacrificial source-amplitude metrology for balanced Toy012 after Iteration 057.  
**Status:** physical Fisher-rate comparison; no hardware forecast and no new-physics claim.

## 1. Motivation

Iteration 057 showed that on balanced Toy012 the best four added force-covariance rows at `y_ref=-4` are worth acquiring only if independent source metrology is slower than approximately

`R_alpha = 2.20253e-5 s^-1`.

The next question is whether physically explicit QND source-metrology protocols can exceed this rate once source reset/preparation time is included.

Two channels are compared:

1. finite-resolution Gaussian energy pointer;
2. QND Ramsey ancilla.

Both are assigned to independent/sacrificial source copies because NG-023 remains active.

## 2. Gaussian pointer

For

`y|E_i ~ N(r E_i,1)`

and

`r=2 sqrt(Gamma_E T)`, `Gamma_E=eta kappa_E`,

the Fisher rate is

`R_ptr(r)=p_E F_ptr(r)/(t_reset+r^2/(4 Gamma_E))`.

For balanced Toy012, the projective energy-population ceiling is

`F_E^alpha ~= 0.00629727`.

At zero reset, the Fisher/sec optimum occurs at

- `r_rate ~= 1.44273`;
- `F_alpha(r_rate) ~= 0.00221257`;
- `max R/(p_E Gamma_E) ~= 0.00425193`.

For `p_E=0.5`, exceeding the Iteration-057 covariance break-even rate requires only

`Gamma_E >~ 0.01036 s^-1`

in this normalized pointer model.

## 3. Ramsey ancilla

For controlled phase `phi=Omega_E T`,

`R_R(phi)=p_E F_R(phi)/(t_reset+phi/Omega_E)`.

Balanced Toy012 has zero-reset rate optimum

- `phi_rate ~= 1.57508`;
- `max R/(p_E Omega_E) ~= 0.00213429`.

For `p_E=0.5`, the same source-metrology rate target requires

`Omega_E >~ 0.02064 s^-1`.

`Gamma_E` and `Omega_E` belong to different physical interaction models and must **not** be equated numerically without a common apparatus Hamiltonian. These values are protocol-specific design targets, not a statement that the pointer is twice as good hardware.

## 4. RQIR-RESOURCE-027 — per-copy Fisher creates a hard reset ceiling

At very large coupling, interaction time can approach zero but fresh-source/reset overhead remains. Therefore any metrology protocol obeys

`R_alpha <= p_E F_max / t_reset`,

where `F_max` is the maximum Fisher obtainable from one accepted source copy in that protocol.

Thus a required target rate `R_*` is impossible whenever

`t_reset >= p_E F_max/R_*`.

This is independent of detector coupling strength.

For Toy012 and `p_E=0.5`, using the Iteration-057 target `R_*=2.20253e-5 s^-1`:

### Gaussian pointer

The strong pointer approaches projective energy-population Fisher

`F_max ~= 0.00629727`,

so

`boxed: t_reset,max ~= 142.96 s`.

If source preparation/reset takes longer than about 143 s, no amount of pointer measurement strength can make the no-extra-force-covariance branch beat best4 on the current source-amplitude closure comparison.

### Ramsey ancilla

Optimized per-copy Ramsey Fisher is

`F_R,max ~= 0.00349867`,

so

`boxed: t_reset,max ~= 79.42 s`.

If reset exceeds about 79 s, the binary Ramsey channel can no longer exceed the same branch0/best4 rate target at any `Omega_E`.

This ceiling is distinct from coherence time: it is caused by finite information per freshly prepared source copy.

## 5. Representative finite-reset coupling requirements

For `p_E=0.5`, ideal visibility and the same target rate:

| reset | pointer `Gamma_E` threshold | Ramsey `Omega_E` threshold |
|---:|---:|---:|
| `0 s` | `~0.01036 s^-1` | `~0.02064 s^-1` |
| `1 s` | `~0.01057 s^-1` | `~0.02091 s^-1` |
| `10 s` | `~0.01259 s^-1` | `~0.02373 s^-1` |

The modest change between 0 and 10 s shows that interaction time still dominates in that regime. Near the hard reset ceilings, required coupling diverges.

## 6. Architecture implication

Iteration 058 strengthens the Iteration-057 conclusion but also makes its domain explicit.

Independent source metrology is a robust alternative to added force covariance when

- source copies can be prepared/reset substantially faster than roughly a minute;
- either the pointer or Ramsey coupling can reach its corresponding Fisher-rate threshold;
- visibility/acceptance are adequate.

If fresh-source preparation becomes very slow, covariance closure can recover its role because it reuses the gravitational calibration architecture rather than demanding many new source copies.

### RQIR-PREP-004 — source-copy throughput is an architecture variable

> The relevant preparation resource is not only Fisher per copy or measurement strength. The product of per-copy information and fresh-copy throughput imposes a hard architecture boundary. Source preparation/reset must therefore be optimized jointly with the source Hamiltonian and detector calibration.

## 7. What is not yet comparable

Pointer `Gamma_E` and Ramsey `Omega_E` have different physical normalization. A universal winner cannot be declared until a concrete source/ancilla/pointer Hamiltonian maps both to common resources such as

- coupling energy;
- control power;
- source disturbance;
- ancilla coherence;
- preparation/reset apparatus.

The robust protocol-independent conclusion is the reset ceiling and the required physical Fisher rate.

## 8. Reproducibility

Code:

`analysis/toy012_pointer_ramsey_reset_surface_iteration058.py`

## 9. Next gate

The source-amplitude closure problem is now sufficiently physical to stop optimizing it in isolation. The next useful step is to combine Toy012's

- absolute D2 signal penalty;
- centered relational/force mean calibration;
- independent source-metrology rate;
- timing/additive controls;
- science detector integration

into one total wall-clock budget.

That will show whether Toy012's local physicality can be purchased by a modest total-time penalty or whether a further local-source redesign is needed.