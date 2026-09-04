# RECOVERY DELTA — ITERATION 436

**Status at allocation:** prospectively frozen; workflow result not yet consumed.  
**Authority target:** Iteration-270 `N1` 80/120-digit precision closure only.  
**MODEL_READINESS:** 24% at launch.

## Frozen scientific object

The authoritative Iteration 436 object is the complete parent chain

`geometry -> nhat -> y_down -> norb -> N1`

for `M=POS`, legs `s/a/b`, `P0=[0.7,-0.4,0.5,0.9]`, and the unchanged Iteration-270 symmetric amplitude derivative step `h=3e-5`.

## Frozen acceptance before result inspection

- precision levels: 80 and 120 decimal digits;
- `max_scaled_abs[N1_80-N1_120] <= 1e-40`;
- for every frozen leg and every `+h/-h` endpoint, `max_scaled_abs[norb_binary64-norb_120] <= 1e-12`;
- all endpoint and N1 values finite;
- legacy `N1_binary64` vs `N1_120` is classified against `2e-5`, the unchanged physical reference tolerance, but this comparison does not control whether the multiprecision implementation itself is internally closed.

A valid raw PASS certifies only N1 numerical realization. `Q1=-Q0(p+k)@N1@Q0(p)` requires a separate later authority after N1 passes.

## Guardrails

No change to `h`, momenta, polarizations, parent dynamics, routing, sign or normalization. No physical `D_s` promotion, no zero fill, no threshold weakening, no `ANSATZ003`, and no Fisher/resource claims.
