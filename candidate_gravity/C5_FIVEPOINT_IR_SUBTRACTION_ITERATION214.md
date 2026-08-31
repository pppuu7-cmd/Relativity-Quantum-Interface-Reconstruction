# RQIR Candidate Gravity — Iteration 214

## Scope

Close the leading infrared subtraction of the physical pure-Einstein five-graviton total-s cut introduced in Iteration 213. This is a comparator calculation, not a Candidate Gravity residual.

## Frozen convention

The external process is the Iteration-213 real massless `2->3`, all-outgoing `--+++`, with the fifth positive-helicity graviton soft. The cut integrand is the unique surviving helicity term

`M4(k1-,k2-,ell1+,ell2+) M5(k3+,k4+,k5+,-ell1-,-ell2-)`.

For the two beam endpoints define

`A_N = lim_{theta->0} (1-cos theta) I_cut`,

`A_S = lim_{theta->pi} (1+cos theta) I_cut`.

No coefficient is fitted to cap-regulated loop data.

## Main result

In the frozen KLT/sign convention,

`A_N(epsilon) = A_S(epsilon) = -2 i M5_tree(epsilon)`.

Numerical extrapolation using azimuthal averaging and a `[1,theta^2,theta^4]` endpoint fit confirms the identity at epsilon `0.04`, `0.01`, and `0.001`; all six north/south relative errors are approximately `1.46e-11` to `1.49e-11`.

At epsilon `0.01`,

`M5_tree = 645.5150777243653 - 124.71057541525806 i`,

so

`A = -249.42115083051613 - 1291.0301554487305 i`.

The predicted contribution of the two endpoint annuli under a halving of the angular cap is

`8 pi A log 2 = -4345.0882294083885 - 22490.63446934122 i`.

Direct raw-cut shell integrations approach this prediction with relative errors

`1.248e-2, 3.096e-3, 7.726e-4, 1.931e-4, 4.826e-5`

for successive cap halvings. The error decreases by approximately a factor of four, consistent with the subleading angular expansion.

## Canonical subtraction

Freeze

`I_sub(theta,phi) = I_cut(theta,phi) - A/(1-cos theta) - A/(1+cos theta)`.

The contribution of successively smaller excluded north+south cap shells has magnitudes

`296.99194, 73.66449, 18.37967, 4.59264, 1.14802`,

with fitted scaling exponent

`2.0033844483`.

Therefore the cap dependence of the azimuthally integrated subtracted cut vanishes as approximately `delta^2`. This establishes a scoped regulator-independent endpoint limit without relying on a global fit through the finite bulk peaks.

Pointwise the subtracted integrand may retain `1/theta` angular behavior, but the corresponding azimuthal coefficient integrates to zero at leading order; the physical cap-shell contribution is `O(delta^2)`.

## Important negative/guardrail result

Large finite peaks occur near the outgoing hard-leg directions, but the direct singularity map does **not** show additional `1/theta^2` nonintegrable endpoint poles there. They are a bulk quadrature problem, not an additional IR subtraction freedom.

Do not infer the finite hard remainder from a poorly converged whole-sphere quadrature. Regulator independence and bulk numerical convergence are separate gates.

## Classification

- `C5-CUT-013`: PASS — beam endpoint coefficient equals `-2 i M5_tree` in the frozen convention.
- `IR-NG-003`: PASS — raw halving shells approach `8 pi A log 2`.
- `IR-NG-004`: PASS_SCOPED — the canonical leading-pole-subtracted cap dependence vanishes as `delta^2` after azimuthal integration.
- Bulk finite cut: `NUMERICAL_CONVERGENCE_OPEN`.
- Candidate residual: none.
- `ANSATZ-003`: not created.
- Fisher/resources: forbidden.

## Next gate

Build a deterministic bulk quadrature that resolves the finite outgoing-hard-leg peaks without changing the subtraction convention. Then evaluate the IR-subtracted cut on the frozen Iteration-210 12-point epsilon grid and feed the resulting finite hard function into the regular+log extractor.

MODEL_READINESS: 23%
