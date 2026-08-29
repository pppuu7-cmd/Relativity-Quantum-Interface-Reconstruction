# RQIR Recovery Delta — Iteration 020

**Date:** 2026-08-29  
**Applies after:** `docs/RECOVERY_GUIDE.md` v1.6 and `docs/RECOVERY_DELTA_ITERATION_019.md`

## New source-metrology result

For the accepted Iteration-011 Toy009 null direction `Delta0`, define

`rho(a)=I/5+a Delta0`.

Because `[rho(a),Delta0]=0`, the source-amplitude family is commuting and the amplitude QFI is

`F_Q(a)=sum_i d_i^2/(1/5+a d_i)`.

Deterministic accepted-null reconstruction gives

`eig(Delta0) ~= (-0.97233836,-0.36204793,-0.16708132,0.50146762,1.0)`

and at nominal `a=0.08`

`F_Q ~= 13.270686` per accepted copy.

**RQIR-PREP-001:** RQIR-NG-005 is an observability-channel obstruction, not an intrinsic absence of information about the hidden amplitude. Gravitational NP3 null observables have zero information on `a`, while an independent measurement in the `Delta0` eigenbasis has finite, saturable QFI.

At detector information `S_D=25`, QFI-limited accepted-copy requirements are approximately:

- 80% retention: 8 copies;
- 90%: 17;
- 95%: 36;
- 99%: 187.

These are lower-bound/ideal-measurement counts. If only fraction `eta_P` of QFI is extracted, multiply counts by `1/eta_P`.

Physical source-metrology rate:

`R_P = p_P eta_P F_Q / t_P`,

with preparation/measurement cycle `t_P` and acceptance `p_P`.

## Critical interpretation

Do not replace RQIR-NG-005 by the statement that source calibration is easy. Independent metrology remains logically mandatory. The new result says only that, in the finite Toy009 state family, amplitude `a` is not fundamentally QFI-starved. The unresolved experimental gate is realizing a high-efficiency `Delta0`-basis (or equivalent) measurement on a physical source with acceptable cycle time and without introducing new correlated nuisances.

## Current continuation target

The immediate next wall-clock gate is to combine:

1. Iteration-019 D1/D2 native detector rates;
2. Iteration-020 source-preparation QFI rate;
3. Iteration-015 corrected hard-constrained gravitational calibration Fisher;
4. Iteration-016 explicit timing/offset priors;
5. Iterations-017/018 gain/reference-control budgets;

into one profiled `F_beta|theta/T_wall` resource optimization.

Parallel physical-realizability gate: find a local observable/control protocol that approximates the `Delta0` eigenbasis measurement.

All mandatory G1/G2/G3/G4a/G8/G9/G10/G12/G13 gates remain open.
