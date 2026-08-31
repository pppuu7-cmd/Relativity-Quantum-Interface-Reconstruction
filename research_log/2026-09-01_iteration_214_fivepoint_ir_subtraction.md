# RQIR Research Log — Iteration 214

Date: 2026-09-01

Goal: remove the universal leading IR endpoint divergence from the physical pure-Einstein five-graviton cut without fitting the subtraction coefficient to cap data.

Result:

1. Reused the validated Iteration-212/213 KLT and real `2->3` kinematics through a shared no-side-effect helper.
2. Verified both beam endpoint coefficients satisfy `A_N=A_S=-2 i M5_tree` across epsilon `0.04, 0.01, 0.001` with relative errors `~1.5e-11` after azimuthal averaging and even-power endpoint extrapolation.
3. At epsilon `0.01`, froze `A=-249.42115083051613-1291.0301554487305 i`.
4. Verified raw halving shells approach the predicted `8 pi A log 2`; relative errors fall `1.248e-2 -> 4.826e-5` over five halvings.
5. After subtracting `A/(1-mu)+A/(1+mu)`, excluded cap-shell magnitudes scale with exponent `2.0033844483`, establishing regulator-independence of the endpoint limit.
6. Separate singularity mapping shows the large outgoing-leg features are finite peaks rather than additional `theta^-2` endpoint poles.

Classification:

- leading IR subtraction: PASS_SCOPED;
- finite bulk hard remainder: NUMERICAL_CONVERGENCE_OPEN;
- no Candidate Gravity residual;
- no ANSATZ-003;
- no Fisher/resources.

Next: deterministic bulk quadrature, then evaluate the IR-subtracted finite cut on the frozen Iteration-210 epsilon grid and run the regular+log extractor.

MODEL_READINESS: 23%
