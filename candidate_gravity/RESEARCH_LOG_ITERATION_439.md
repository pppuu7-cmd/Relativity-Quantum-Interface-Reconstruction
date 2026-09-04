# RQIR Candidate Gravity — Research Log Iteration 439

## Prospective diagnostic freeze

Iteration 439 is allocated uniquely before its numerical result is inspected. It is an independent binary64 conditioning diagnostic for the exact Iteration-270 `Acoef` signed finite-difference combinations. It neither assumes nor requires the outcome of Iteration 438.

## Frozen object

For each of the seven nonempty subsets of `LEGS=('s','a','b')`, at `M=POS`, `p=P0`, and unchanged parent amplitude steps

- `h1=1e-4` for one leg,
- `h2=5e-4` for two legs,
- `h3=1e-3` for three legs,

the diagnostic evaluates the exact `A_finite` node set entering

`Acoef = sum_sigma [prod(sigma) A_finite(sigma*h)] / (2h)^n`.

## Frozen metrics

For every matrix component of every subset, before division by `(2h)^n`, measure

`cancellation_amplification = sum_sigma |A_finite_sigma| / |sum_sigma prod(sigma) A_finite_sigma|`.

Also record:

- maximum componentwise amplification per subset;
- maximum signed numerator magnitude and minimum nonzero signed numerator magnitude;
- `Acoef` Frobenius norm;
- an independent reconstruction check between the explicit signed node sum and the parent `Acoef` implementation.

## Scientific validity rule

The diagnostic is scientifically valid if:

- all 26 `A_finite` node values and all seven `Acoef` outputs are finite;
- node census is exactly 26 and subset census exactly 7;
- explicit signed-sum `Acoef` reproduces parent `Acoef` with max scaled discrepancy `<=1e-12`.

No upper limit on cancellation amplification is a physical acceptance rule. Large amplification is a localization diagnostic only and cannot by itself block or promote a physical coordinate.

## Scope/readiness

Diagnostic-only, non-promoting. No change to `MODEL_READINESS=24%`; no `D_s` promotion, no step/threshold change, no zero fill, no `ANSATZ003`, no Fisher/resources.
