# RECOVERY DELTA — Iteration 622

Date: 2026-09-08

## New authority

Iteration 622 closes a field-variable/coupling subgate downstream of Iter621.

Classification:
`PASS_ITER622_COMMON_DIRECT_DELTA_G_VARIABLE_AND_COMMON_KAPPA_STRIPPING__N_NATIVE_DIMENSIONLESS_CONVENTION_BRIDGE_REMAINS_BLOCKED_NON_RESIDUAL`.

The declared physical split is `g=eta+kappa h_phys`, hence `delta_g=kappa h_phys`. Both computational branches use mode amplitudes added directly to `g`: the connection geometry inherited from Iter270 and the MSSC source geometry inherited by Iter590/594. Thus their stored perturbative coefficients are expressed with respect to the same direct metric perturbation `delta_g`; the explicit gravitational-coupling conversion has already been stripped in both sectors.

Therefore the one remaining Iter621 relative complex normalization degree of freedom is not an unknown power of `kappa`/`G`. It is a dimensionless common source-observable <-> native Gamma3/effective-action convention factor.

No Candidate/comparator values were used. `N_native` is still not fixed; setting it to `1`, `+i` or `-i` remains forbidden. No Source/Born subtraction or comparator quotient is authorized.

MODEL_READINESS: 24%.

## Exact next gate

Derive prospectively the remaining dimensionless generating-functional / Legendre / in-in source-to-Gamma3 normalization. If the chosen MSSC physical response is not universally identical to a native Gamma3 insertion, freeze the exact additional measurement-level bridge required rather than choosing a normalization convention post hoc.
