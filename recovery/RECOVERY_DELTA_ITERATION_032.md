# RQIR Recovery Delta — Iteration 032

**Date:** 2026-08-29

## New confirmed result

The D2 covariance/noise observable family was made consistent with detector-native force calibration.

The old Iteration-026 `native-replace` branch used force-gradient mean rows but retained potential covariance rows. It remains mathematically valid as a mixed protocol, but it is not a fully force-native D2 branch.

A fully native `14 force means + 8 force covariances` branch remains rank `22/23` on the exact trace+energy constrained source tangent space. Its exact null has

- old-hidden overlap `~0.95003346`;
- detector alignment `~0.99003961`.

At corrected current weights:

- `F_beta|theta(C_a=0,lambda=1)~0.0194450`;
- `C_a*~8.29464` for 90% at `lambda=1`;
- strong-preparation minimum `lambda~0.1537665`.

## New calibration rules

**RQIR-CAL-011 — observable-family consistency:** changing a detector-native mean observable requires covariance/noise calibration to be derived from the same physical observable family, unless a hybrid protocol is explicitly declared.

**RQIR-CAL-012 — covariance complementarity:** in current Toy009 D2, targeted force-covariance observables can remove most of the remaining detector-relevant nuisance penalty after relational-potential + force mean calibration.

## Complementary branch result

With finite-reference relational-potential means, force means, relational covariance and force covariance, the hard rank is `23/23`.

At `y_ref=-4`:

- `F_beta|theta~0.8994327` at `C_a=0`, `lambda=1`;
- `C_a*~0.06708` reaches 90% at `lambda=1`;
- without preparation information, `lambda~1.00632` reaches 90%.

The best four added force-covariance rows at `y_ref=-4` are `(0,1,3,7)`, giving

- `F_beta|theta~0.894857`;
- `C_a*~0.58896`;
- calibration-only 90% at `lambda~1.05755`.

## Interpretation correction

Do not use the Iteration-028 phase diagram as the final fully physical D2 branch map. Its force-replacement region corresponds to the mixed force-mean/potential-covariance protocol inherited from Iteration 026.

No Iteration-026/028 number is deleted; the protocol label is narrowed.

## Reproducibility

- `analysis/d2_native_covariance_completion_iteration032.py`
- `docs/D2_NATIVE_COVARIANCE_COMPLETION.md`
- `research_log/2026-08-29_iteration_032_d2_native_covariance_completion.md`

## Next action

Close physical Fisher rates for relational-potential covariance and force covariance under one D2 PSD/bandwidth/duty model, then optimize `y_ref`, `lambda`, `C_a`, and covariance-row subset in wall-clock time.
