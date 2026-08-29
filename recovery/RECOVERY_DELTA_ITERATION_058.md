# RQIR Recovery Delta — Iteration 058

**Date:** 2026-08-30

Apply after Iteration 057.

## New retained result

Balanced Toy012 independent source-amplitude metrology has been placed on one reset-aware Fisher-rate target for two explicit QND protocol classes.

Iteration-057 branch0/best4 break-even target:

`R_alpha*=2.2025279e-5 s^-1`.

### Gaussian QND pointer

- projective energy Fisher ceiling `F_E^alpha=0.00629727076`;
- zero-reset rate optimum `r*=1.44273`;
- `max R/(p_E Gamma_E)=0.00425193299`;
- at `p_E=.5`, zero-reset coupling threshold `Gamma_E~0.01036 s^-1`.

### Ramsey ancilla

- zero-reset rate optimum `phi*=1.57508`;
- `max R/(p_E Omega_E)=0.00213429284`;
- per-copy Fisher maximum `F_R,max=0.00349867283`;
- at `p_E=.5`, zero-reset threshold `Omega_E~0.02064 s^-1`.

Do not directly rank `Gamma_E` against `Omega_E` without a common apparatus Hamiltonian; they are different physical couplings.

## RQIR-RESOURCE-027 — hard reset ceiling

Any fresh-copy metrology obeys

`R_alpha <= p_E F_max/t_reset`.

Thus finite information per accepted copy creates a coupling-independent reset ceiling.

For `p_E=.5` and the current Toy012 branch target:

- pointer: `t_reset,max~142.96 s`;
- Ramsey: `t_reset,max~79.42 s`.

Beyond these values the respective protocol cannot make branch0 cheaper than best4 at any measurement strength.

## RQIR-PREP-004

Fresh-source preparation/reset throughput is a first-class architecture variable. Source Hamiltonian, preparation, metrology and gravitational calibration must be optimized jointly.

## Representative finite-reset thresholds

At `p_E=.5`, ideal visibility:

- reset 1 s: pointer `Gamma_E~0.01057 s^-1`, Ramsey `Omega_E~0.02091 s^-1`;
- reset 10 s: pointer `~0.01259 s^-1`, Ramsey `~0.02373 s^-1`.

## Next continuation step

Stop optimizing source-amplitude metrology in isolation. Build a total Toy012 D2 wall-clock budget that includes

1. absolute science detector signal penalty;
2. relational/direct-force mean calibration;
3. source metrology;
4. timing/additive control references;
5. science integration;
6. acceptance, coherence and dead/reset time.

Only then decide whether Toy012 is resource-competitive enough to replace Toy009 as the physical-source baseline.