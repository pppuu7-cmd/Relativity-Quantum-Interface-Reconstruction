# RQIR Source-Preparation Quantum Fisher Rate — Iteration 020

**Date:** 2026-08-29  
**Status:** finite-dimensional Toy009 source-metrology bound; not a hardware implementation and not a new-physics claim.

## 1. Question

RQIR-NG-005 established that the hidden exact-null amplitude cannot be self-calibrated by the gravitational NP3 observables. Independent source metrology is logically required. Iterations 012–018 represented its information by a free number `C_a` or standardized sensitivity `xi_prep`.

Iteration 020 asks a more fundamental question:

> How much information about the Toy009 hidden-state amplitude is available in one ideal copy of the prepared source state?

This gives a quantum Fisher upper bound on any source-metrology protocol and tells us whether the amplitude itself is intrinsically hard to estimate.

## 2. Toy009 amplitude family

Let the accepted Iteration-011 exact-null operator be `Delta0`, normalized so its largest absolute eigenvalue is one. Define

`rho(a)=I/5 + a Delta0`.

The nominal prepared branch uses `a=0.08`.

The deterministic accepted calibration gives approximately

`eig(Delta0)=(-0.97233836,-0.36204793,-0.16708132,0.50146762,1.0)`.

Hence at `a=0.08`,

`eig(rho)= (0.12221293,0.17103617,0.18663349,0.24011741,0.28)`.

## 3. Exact commuting-family simplification

Because

`rho(a)=I/5+a Delta0`,

we have

`[rho(a),Delta0]=0`.

Therefore the eigenbasis does not change with `a`, and the quantum Fisher information for amplitude `a` reduces to the classical Fisher information of a projective measurement in the `Delta0` eigenbasis:

`F_Q(a)=sum_i d_i^2/p_i(a)`,

where

`p_i(a)=1/5+a d_i`.

At the nominal Toy009 point,

`F_Q(0.08) ~= 13.270686` per accepted copy.

No collective entangled measurement across many copies is needed to saturate this toy-model QFI in principle; an ideal projective measurement in the `Delta0` eigenbasis is sufficient.

### RQIR-PREP-001 — hidden-amplitude metrology is not intrinsically information-poor in Toy009

The exact-null obstruction is an **observability-channel obstruction**, not a statement that the amplitude has vanishing quantum Fisher information. The gravitational null observables carry zero information about `a`, while an independent measurement in the correct source basis carries finite and relatively large information per copy.

This distinction is central: `A n=0` does not imply `F_Q(a)=0`.

## 4. Copies required for the previous retention benchmarks

At detector information `S_D=25` (the historical detector SNR=5 normalization), isolated amplitude calibration requires

`C_a=S_D r/(1-r)`

to retain fraction `r` of detector information.

Using the QFI limit `F_Q=13.270686`:

| retention | `C_a` | QFI-limited accepted copies | integer ceiling |
|---:|---:|---:|---:|
| 80% | 100 | 7.54 | 8 |
| 90% | 225 | 16.95 | 17 |
| 95% | 475 | 35.79 | 36 |
| 99% | 2475 | 186.50 | 187 |

Thus the previous standardized `xi_prep=1` interpretation (`225` accepted shots for 90%) was not a fundamental lower bound. In the ideal Toy009 source basis, the QFI limit is about 17 accepted copies.

## 5. Measurement-efficiency penalty

Let `eta_meas` be the fraction of QFI actually extracted per accepted copy. Then

`F_copy=eta_meas F_Q`

and

`N=C_a/(eta_meas F_Q)`.

For the 90% benchmark `C_a=225`:

- `eta_meas=1` -> `~17` accepted copies;
- `0.5` -> `~34`;
- `0.1` -> `~170`;
- `0.01` -> `~1695`.

Therefore the practical source-metrology bottleneck is likely the physical implementation efficiency of a measurement approximating the `Delta0` eigenbasis, plus state-preparation/reset time and acceptance, not the intrinsic distinguishability of `a` inside the finite-dimensional model.

## 6. Physical Fisher rate

For preparation/metrology cycle time `t_P`, acceptance probability `p_P`, and QFI extraction efficiency `eta_P`, define

`R_P = p_P eta_P F_Q / t_P`.

This is the source-preparation Fisher rate needed by the Iteration-018 wall-clock allocation law.

Example only: with `p_P=0.5`, `eta_P=0.5`:

- `t_P=1 ms` -> `R_P ~= 3318 /s`, so `C_a=225` takes about `0.068 s`;
- `t_P=10 ms` -> `~332 /s`, time `~0.68 s`;
- `t_P=100 ms` -> `~33.2 /s`, time `~6.8 s`.

These are toy-model rate examples. They do **not** assert that a massive gravitational source can be prepared and measured in the required eigenbasis on millisecond timescales.

## 7. What this does and does not solve

This result resolves one ambiguity in the resource model:

- independent source metrology is logically mandatory (RQIR-NG-005 survives unchanged);
- but the hidden amplitude is not fundamentally QFI-starved in Toy009;
- the unknown hardware problem is how to implement a high-efficiency measurement of the required source observable without destroying the preparation protocol or introducing a new gravity-correlated nuisance.

The result therefore moves the next bottleneck from an abstract `C_a` toward **measurement-basis realizability and cycle rate**.

## 8. Next gate

Combine

- D1 or D2 physical detector rate from Iteration 019;
- `R_P=p_P eta_P F_Q/t_P` from this iteration;
- corrected gravitational calibration Fisher from Iteration 015;
- explicit control priors from Iteration 016;
- reference/gain requirements from Iterations 017–018;

into one common wall-clock `F_beta|theta/T_wall` optimization.

A second parallel gate is to search for a physically realizable local observable or control sequence that approximates the `Delta0` eigenbasis measurement. Until that is done, the QFI result is a bound, not an experimental protocol.

## Reproducibility

Code: `analysis/source_preparation_qfi_iteration020.py`.
