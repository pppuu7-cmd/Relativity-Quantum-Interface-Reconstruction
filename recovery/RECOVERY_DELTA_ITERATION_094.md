# RQIR Recovery Delta — Iteration 094

**Date:** 2026-08-30

## Authority

This delta advances the authoritative RQIR front from Iteration 093 to Iteration 094. Read it together with `recovery/CURRENT_FRONT.md`, `docs/RECOVERY_GUIDE.md`, and `docs/MASTER_TABLE.md`.

## What changed

Iteration 093 introduced exact robust crossover boundaries and the NG-043 unresolved throughput band. Iteration 094 differentiates those boundaries analytically to rank apparatus characterization priorities.

For any active boundary

`B=-D/S`,

retain

`dB=-(1/S)dD+(D/S^2)dS`.

For an interval `x=[x_-,x_+]`, use midpoint `c`, half-width `h`, and contraction coordinate

`x_-(eta)=c-eta h`, `x_+(eta)=c+eta h`.

Define unresolved width `W=U-L` and decision leverage

`Lambda_x=(1/W)dW/deta_x` at `eta=1`.

### RQIR-RESOURCE-046

The robust crossover/dead-zone sensitivity to `A_i`, `R_src,i`, and `d_i` is analytic. The contraction-coordinate derivative gives a comparable local measure of characterization value across unlike physical coordinates.

### RQIR-DESIGN-006

Prioritize apparatus characterization by reduction of the NG-043 unresolved decision band, not by raw percentage uncertainty alone.

### RQIR-NG-045

Largest raw uncertainty need not be highest-value measurement because crossover sensitivity contains different nonlinear weights: source rate enters through `1/R_src`, duty through `m=(1-d)^-1`, and detector/calibration through `A/R0`.

### RQIR-NG-046

The leverage ranking is local to the declared uncertainty set. Recompute after large interval contraction. If primitive uncertainties are correlated, use their joint uncertainty geometry rather than independent Cartesian boxes.

## Regression numbers — synthetic only

Using exactly the Iteration-093 synthetic box:

- lower boundary `L=0.025237237237237236`;
- upper boundary `U=0.08006274509803925`;
- width `W=0.05482550786080201`.

Local leverage ranking:

1. Toy014 source rate `0.51911`;
2. Toy009 source rate `0.42737`;
3. Toy014 `A` `0.18110`;
4. Toy014 duty `0.15900`;
5. Toy009 duty `0.10243`;
6. Toy009 `A` `0.03528`.

These numbers are not apparatus forecasts.

## Reproducibility

- `analysis/crossover_value_of_information_iteration094.py`
- `docs/PAPER_III_CROSSOVER_VALUE_OF_INFORMATION_ITERATION094.md`
- `research_log/2026-08-30_iteration_094_crossover_value_of_information.md`

## Next admissible gate

Propagate primitive source-specific uncertainty (`r2,r4,rho`, seven calibration matrix blocks, source reset/visibility/coupling, timing/control duty) into the physical summaries `A_i`, `R_src,i`, `d_i`, then compute primitive-level decision leverage. Toy015 remains premature unless this analysis reveals a source-dependent dominant bottleneck.
