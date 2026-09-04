# RQIR Candidate Gravity — Iteration 433 Recovery Delta

## Authority status

Physical/operator authority remains Iteration 411. Latest physical blocker authority remains Iteration 421 (`BLOCKED_CONVERGENCE` for double-double index 2). `MODEL_READINESS: 24%`.

Iteration 432 parent-primitive recursive-closure workflow run `33894344918`, job `101093336026`, completed and uploaded artifact `9945106288` with digest `sha256:4232ad499e6cba069477ce2cad08502b78fd0623306fd303bed3ab101ece8b7a`. This is source/provenance diagnostic work only and does not promote a physical coordinate.

## Iteration 433

Purpose: deepest-first 80/120-digit numerical subclosure for Iteration-270 primitives `Q0` and `y_down` on frozen representative inputs, before attempting `Q1`, `Asub`, or the outward 368/370 chain.

Frozen acceptance:
- max 80-vs-120 digit discrepancy `<= 1e-40`;
- binary64 parent reproduction against the 120-digit reference `<= 1e-12`;
- finite outputs;
- no physical `D_s` value and no physical promotion.

Run `33898986792`, job `101108325427`, failed before producing an artifact because the runner lacked the `mpmath` dependency. This is `OPERATIONAL_FAILURE`, not scientific FAIL. No threshold/input/convention was changed.

Repaired workflow commit: `adc50099868ca12b8ece13590163acf5fb7d6490`. The repair only installs pinned `mpmath==1.3.0`.

Current repaired run: `33899067536`, job `101108587795`, `in_progress` at the time of this recovery update.

## Guardrails retained

Unsupported remains BLOCKED; no zero fill; no smaller auxiliary-mass step; no angular-grid escalation; no threshold weakening; no ANSATZ-003; no Fisher/resources; no reopening closed e=3 authority.

## Exact next gate

Raw-consume Iteration 433 fail-closed. If `Q0/y_down` pass, continue deepest-first to a separately auditable 80/120-digit `Q1`/`N1` closure and only then to `Asub`/`Acoef/A_finite`. If Iteration 433 scientifically blocks, preserve the negative result and localize the primitive mismatch before any outward precision claim.

`MODEL_READINESS: 24%`
