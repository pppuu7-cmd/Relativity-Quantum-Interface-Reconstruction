# RQIR Recovery Delta — Iteration 047

**Date:** 2026-08-29

## QND/source-metrology result

For the nondegenerate Toy009 Hamiltonian, exact Hermitian QND observables are diagonal in the energy basis. After trace+energy removal this gives a three-dimensional hard calibration sector.

At `y_ref=-4`, centered relational calibration alone has hard rank `22/23`; adding a complete diagonal QND basis gives `23/23`.

**RQIR-CAL-016:** the current relational null is locally visible to the exact-QND diagonal sector.

Simple projective energy-basis population metrology gives

- `F_E^alpha(+)=0.0093918844` per accepted plus-branch copy;
- `F_E^alpha(-)=0.0095791291`;
- plus/minus pair `0.0189710135`.

The plus branch carries about `11.1%` of full Toy009 QFI per copy.

**RQIR-PREP-002:** hidden-amplitude metrology has a simpler finite-information energy-basis channel; the ideal `Delta0` eigenbasis is not the only useful source measurement.

Current best4 residual `C_alpha=0.05006144` costs only `~5.33` plus-branch copies or `~2.64` pair equivalents at the ideal energy-population Fisher.

## Same-copy warning

Projective energy measurement is QND relative to `H` but fully dephases energy coherences. On the same science copy it leaves only `~0.29848` of the D2 ordered-response norm.

**RQIR-NG-023:** QND relative to the source Hamiltonian is not equivalent to nondemolition of the ordered-response resource.

Use energy-basis metrology on independent/sacrificial copies unless a weaker response-preserving protocol is explicitly demonstrated.

## Next

Use the concrete energy-basis Fisher rate to recompute D2 branch wall-clock crossovers.