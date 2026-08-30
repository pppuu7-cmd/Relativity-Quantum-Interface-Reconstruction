# Candidate Gravity Derivation Map Template

Purpose: make every model claim traceable from dynamics to RQIR observable to code/test and gate status.

| Claim ID | Model statement | Derived equation/object | Approximation order | RQIR object/gate | Code/test | Comparator checked | Status |
|---|---|---|---|---|---|---|---|
| D-001 | ... | ... | exact / O(eps^n) | J / N / chi^R / QG-00x | ... | C0...C6 | OPEN / VERIFIED / FAILED |

## Mandatory derivation chains

### Dynamics → source hierarchy

`action/H/channel -> equations/CTP -> J,N,chi^R,higher correlators`

### Source hierarchy → finite discriminator

`J,N,chi^R,... -> calibration quotient -> Paper-I response difference`

### Finite discriminator → detector likelihood

`response difference -> detector transfer/noise -> scores/Fisher -> F_beta|theta`

### Detector likelihood → physical resources

`F_beta|theta -> source metrology + calibration + controls + wall clock`

## Error accounting

Every approximate derivation must record:

- expansion parameter;
- retained order;
- estimated remainder/error bound or convergence test;
- regime in which the approximation is used downstream.

## Failure provenance

A failed derivation/test remains in the map. Do not erase a negative result by replacing the file; supersede it with a new model version and preserve the previous authority.
