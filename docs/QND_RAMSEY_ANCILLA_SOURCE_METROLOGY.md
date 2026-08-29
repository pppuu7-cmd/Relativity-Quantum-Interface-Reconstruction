# RQIR Iteration 051 — QND Ramsey-Ancilla Source Metrology

**Date:** 2026-08-29  
**Scope:** concrete independent Toy009 source-metrology protocol after Iterations 049–050.  
**Status:** constructive protocol model; no hardware implementation and no new-physics claim.

## 1. Motivation

Iterations 047–050 established that energy-basis source metrology can be much cheaper than adding more D2 covariance rows, but the most explicit model so far was a Gaussian pointer that attempts to resolve energy levels.

A simpler physical implementation class is a two-level ancilla coupled dispersively/QND to the source energy. It does not need to identify all five energy levels individually. Instead, it measures a selected Fourier component of the energy-population distribution.

## 2. QND Ramsey protocol

Prepare an ancilla in an equatorial superposition and apply a controlled phase commuting with the isolated source Hamiltonian:

`U(phi)=exp[-i phi H otimes sigma_z/2]`.

For source energy populations

`p_i(alpha)=1/5+0.08 alpha d_i`,

the reduced ancilla coherence is

`c(phi,alpha)=sum_i p_i(alpha) exp(-i phi E_i)`.

An equatorial binary ancilla measurement with angle `theta` has outcome probabilities

`P_+ = [1 + Re(e^{-i theta} c)]/2`,

`P_- = 1-P_+`.

Optimizing the readout quadrature at fixed `phi` gives the exact binary Fisher

`F_alpha(phi)=d_vec^T [I-c_vec c_vec^T]^{-1} d_vec`,

with

`c_vec=(Re c, Im c)`,

`d_vec=(Re partial_alpha c, Im partial_alpha c)`.

An ancilla visibility `V<1` is included by `c_vec -> V c_vec`, `d_vec -> V d_vec`.

## 3. Optimized ideal-visibility result

For the plus branch the optimal controlled phase is

`boxed: phi_* ~= 2.418668 rad`.

The corresponding Fisher is

`boxed: F_R^(alpha) ~= 0.00389040938`

per accepted plus-branch ancilla readout.

This is

`boxed: 41.42%`

of the full projective energy-population Fisher and about `4.58%` of the full Toy009 QFI.

For the minus branch the separate optimum is

`phi_*^- ~= 2.410233`,

`F_R,-^(alpha) ~= 0.00353595967`.

Thus a single binary ancilla measurement can capture a substantial fraction of the five-outcome energy-population information.

### RQIR-PREP-003 — binary QND characteristic-function metrology

> The current Toy009 hidden amplitude can be calibrated without resolving every energy population separately. A QND Ramsey ancilla measuring one optimized characteristic-function component carries about 41% of the projective energy-population Fisher per accepted plus-branch copy.

This gives a materially simpler source-metrology protocol class than ideal five-outcome energy resolution.

## 4. Current source-copy costs

Using only the plus-branch optimized Ramsey readout:

### Branch 0

For `C_alpha=4.55511`,

`N_R,0 ~= 1170.86`

accepted ancilla/source copies.

### best4 residual

For `C_alpha=0.05006144`,

`N_R,4 ~= 12.87`

accepted copies.

The current best4 residual is therefore still extremely cheap in absolute source-copy count compared with the `>1.18e6` covariance-trajectory floor.

## 5. D2 wall-clock crossovers

Use the same transparent 100-Hz covariance benchmark as Iteration 050:

- best4 covariance time `T4 ~= 5.864 h`;
- best5 covariance time `T5 ~= 10.608 h`.

If one accepted Ramsey source-metrology cycle has wall time `t_R` and acceptance/efficiency differences are absorbed into that accepted-cycle time, then:

### Branch 0 vs best4

`boxed: t_R ~= 18.23 s`

is the crossover.

If an accepted Ramsey cycle is faster than about 18 s, Branch 0 (no added force-covariance rows) is cheaper than best4.

### best4 vs best5

`boxed: t_R ~= 1327 s ~= 22.1 min`

is the crossover.

Thus best5 becomes preferable only if an accepted Ramsey source-metrology cycle is slower than roughly 22 minutes in this protocol/benchmark.

This is close to, but slightly stricter than, the ideal projective-energy boundaries from Iteration 048 because the binary Ramsey measurement carries less Fisher per source copy.

## 6. Visibility penalty

After reoptimizing `phi` at each ancilla visibility:

| visibility `V` | best `F_R^(alpha)` | Branch0/best4 cycle crossover | best4/best5 crossover |
|---:|---:|---:|---:|
| 1.0 | `3.8904e-3` | 18.23 s | 22.12 min |
| 0.9 | `3.0271e-3` | 14.18 s | 17.21 min |
| 0.8 | `2.3110e-3` | 10.83 s | 13.14 min |
| 0.5 | `8.3862e-4` | 3.93 s | 4.77 min |

Lower ancilla visibility therefore does not destroy the protocol, but it rapidly makes covariance completion relatively more attractive because more sacrificial source copies are needed.

## 7. Relation to RQIR-NG-024

The Ramsey protocol obeys the same weak-coupling suppression found for the Gaussian energy pointer.

Because

`sum_i d_i=0`

and

`sum_i E_i d_i=0`,

the derivative of the characteristic function satisfies

`partial_alpha c(phi)=O(phi^2)`

near `phi=0`.

Therefore Ramsey Fisher also begins as `O(phi^4)`.

RQIR-NG-024 is thus not an artifact of Gaussian energy resolution; it is a consequence of the exact trace+energy matching of the hidden direction for any weak analytic phase probe generated linearly by `H`.

## 8. Same-copy caution

The interaction is QND with respect to `H`, but a strong ancilla measurement still dephases source coherences when the ancilla is read out. RQIR-NG-023 therefore remains: the protocol is presently intended for independent/sacrificial source-metrology copies, not for strong readout on the science copy.

## 9. Reproducibility

Code:

`analysis/qnd_ramsey_ancilla_metrology_iteration051.py`

The script derives the optimized binary Fisher analytically over readout quadrature, numerically optimizes the controlled phase, includes finite visibility and converts the result into D2 branch cycle-time boundaries.

## 10. Next gate

The source-metrology uncertainty has now been reduced to an implementation question: what controlled-phase rate and fresh-copy preparation/reset time are achievable for a physical massive five-mode source?

The next scientifically useful step is to construct a minimal oscillator/internal-mode source realization in which:

- the five Toy009 levels map to explicit physical modes;
- `phi=g_R t` is generated by a declared QND/dispersive coupling;
- ancilla contrast and source reset are included;
- the resulting `R_E^(alpha)` is compared with the current Branch0/best4 threshold.
