# RECOVERY DELTA — ITERATION 441

**Status:** prospectively frozen and launched; raw result pending.  
**Authority target:** Iteration-270 `Acoef/Asub` fixed-h representation/truncation closure; non-promoting.  
**MODEL_READINESS:** 24%.

## Preconditions consumed

Iteration 440 is raw-valid PASS for 80/120-digit arithmetic precision of the exact frozen signed `Acoef/Asub` assembly. Its max scaled 80-vs-120 discrepancy is `1.4149749985220297e-75`, with exact 26-node / 7-subset census and finite outputs. Binary64-vs-120 disagreement is diagnostic only and peaks at `1.890704312519492e-10` for `(s,a,b)`.

## Frozen object

Compare the exact Iteration-270 central two-point-per-axis stencil to an independent fourth-order tensor-product derivative rule using the same base spacings and only `±h, ±2h` nodes:

`f'(0) ~= [f(-2h)-8f(-h)+8f(h)-f(2h)]/(12h)`.

Frozen spacings remain:
- `h1=1e-4`;
- `h2=5e-4`;
- `h3=1e-3`.

No smaller amplitude spacing is introduced.

## Frozen acceptance before result

- 80/120-digit high-order oracle discrepancy `<=1e-30`;
- central-vs-high-order 120-digit scaled discrepancy `<=2e-5` across all seven subsets;
- all outputs finite;
- exact high-order node census `124` per precision level and seven subsets.

The `2e-5` ceiling is fixed prospectively and cannot be weakened after inspection.

## Launch provenance

Research-log freeze commit: `10f2cc3ec23f11c54a33d34c0a7d9e058f4dbd78`.  
Code commit: `8c7f51e8c84a81a708fc146c6f498f290f264111`.  
Workflow commit: `ebd52b26936d7f6d15a9541d0cbdcfe5cb0f66b0`.  
GitHub Actions run: `33904593636`.

## Guardrails

No physical `D_s` promotion, no smaller amplitude h, no physical mass-step change, no threshold weakening, no parent-dynamics/routing/sign/normalization change, no zero fill. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. Iteration 412 exact15 remains BLOCKED until index 2 gets raw-valid physical authority.
