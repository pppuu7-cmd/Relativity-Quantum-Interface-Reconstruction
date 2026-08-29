# RQIR Research Log — Iteration 020: Source-Preparation Quantum Fisher Rate

**Date:** 2026-08-29

## Starting point

RQIR-NG-005 requires independent source-preparation metrology because the gravitational NP3 null observables contain zero information about the hidden amplitude `a`. Previous resource layers represented that metrology by `C_a` or standardized `xi_prep`.

## QFI derivation

For the accepted Iteration-011 Toy009 null operator `Delta0`, use

`rho(a)=I/5+a Delta0`.

Because `[rho(a),Delta0]=0`, the amplitude family is commuting. The QFI is therefore

`F_Q(a)=sum_i d_i^2/p_i(a)`, `p_i=1/5+a d_i`,

and is saturated in principle by projective measurement in the `Delta0` eigenbasis.

Deterministic reconstruction gives

`eig(Delta0)=(-0.97233836,-0.36204793,-0.16708132,0.50146762,1.0)`

and at `a=0.08`

`F_Q ~= 13.270686` per accepted copy.

## Result

Recorded as **RQIR-PREP-001**: the hidden-amplitude obstruction is channel-specific, not an intrinsic lack of quantum Fisher information. The gravitational null set has zero information on `a`, while an independent source-basis measurement has finite QFI.

At detector information 25:

- 80% retention: `C_a=100`, QFI limit `~7.54` accepted copies -> ceiling 8;
- 90%: `C_a=225`, `~16.95` -> 17;
- 95%: `C_a=475`, `~35.79` -> 36;
- 99%: `C_a=2475`, `~186.5` -> 187.

Thus the earlier `xi_prep=1` conversion was bookkeeping, not a fundamental copy lower bound.

## Measurement efficiency and rate

If only fraction `eta_P` of the QFI is extracted per accepted copy and preparation acceptance is `p_P`,

`R_P=p_P eta_P F_Q/t_P`.

For the 90% benchmark, accepted copies scale as `225/(eta_P F_Q)`. At `eta_P=0.1` this is about 170 copies; at 0.01 about 1695.

The practical unresolved issue is therefore measurement-basis realizability and source cycle rate, not intrinsic Toy009 amplitude distinguishability.

## Files

- `analysis/source_preparation_qfi_iteration020.py`
- `docs/SOURCE_PREPARATION_QFI_RATE.md`
- this log

## Next gate

Combine physical detector rate (Iteration 019), source-preparation QFI rate (Iteration 020), corrected gravitational calibration information (Iteration 015), explicit systematic-control priors (Iteration 016), and reference/gain resources (Iterations 017–018) in one wall-clock profiled-Fisher optimization. In parallel, search for a physical local observable/control protocol approximating the `Delta0` eigenbasis measurement.
