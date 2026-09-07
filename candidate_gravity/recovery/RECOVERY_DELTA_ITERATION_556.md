# RECOVERY DELTA — ITERATION 556

Date: 2026-09-07

## Authority added
QUARTER rank8 `(u,v)=(+1.25e-6,-1.25e-6)` is raw-consumed PASS.

Canonical provenance:
- run `34153849866`;
- job `101841466120`;
- artifact `10032056133`;
- artifact digest `sha256:4ec3d3633b9bddeafd492ad6616350441515a21fed34a68794064ac45b0996bd`;
- run head `b1ec70bd5cab311921e514e31594b1476f1381ce`;
- result SHA-256 `8d498f746c5ee5aecb24949259227ac81731ff007ca1c8681b8169e510962cdb`;
- authority-audit SHA-256 `7416d9e1e2e2e51c9fd348092298caf11aa7f50f9db3e4e93dc412a191bb8bb7`.

Observed: 80/80 finite; MP80↔MP120 max `3.21415799361858209211589830142e-80 <= 1e-30`; radial Richardson max `2.56632452688472147151010572675e-15 <= 5e-4`.

Machine-readable authority: `candidate_gravity/results/iteration556_iter424_quarter_rank8_raw_consumption.json`.

## Coverage
- new QUARTER coordinates raw-closed: `8/12`;
- full QUARTER coordinate coverage including exact HALF-overlap corners: `12/16 = 75%`.

## Active process after recovery
Exactly one rank9 heavy run is authorized:
- coordinate `(u,v)=(+1.25e-6,+1.25e-6)`;
- run `34160111095`;
- job `101859912600`;
- head `7be4b22384c6680d669e88c0fb7990ba53ceff3e`.

On recovery, inspect this run first. Do not launch a duplicate.

If rank9 is terminal, workflow colour is insufficient: download raw artifact and verify classification, exact frozen coordinate/rank, 80 samples, finiteness, MP80/MP120 threshold, radial threshold, and result hash binding. Only raw-valid PASS authorizes rank10 `(+1.25e-6,+2.5e-6)`.

Scientific FAIL/BLOCKED stops successor advancement. Operational failure permits only minimal technical repair and rerun of rank9 under unchanged science.

## Guardrails retained
No u↔v support substitution; no threshold weakening; no node, precision, routing or parent-dynamics changes; no physical index2 promotion from local support alone; no ANSATZ-003; no Fisher/resources.

MODEL_READINESS: 24%
