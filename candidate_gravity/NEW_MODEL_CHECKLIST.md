# New Candidate Gravity Model Boot Checklist

Use this checklist before any equations from a new ansatz are treated as an active model branch.

## A. Create identity

- [ ] Choose `ANSATZ-<short-name>`; do not assign `QGxxx` yet.
- [ ] Add an entry to `MODEL_REGISTRY.md`.
- [ ] Create `candidate_gravity/models/<ID>/`.
- [ ] Copy/fill `MODEL_SPEC_TEMPLATE.md` as `MODEL.md`.
- [ ] Copy/fill `GATE_STATUS_TEMPLATE.yaml` as `GATE_STATUS.yaml`.
- [ ] Create `ASSUMPTIONS_LEDGER.md`, `DERIVATION_MAP.md`, `COMPARATOR_STATUS.md`.

## B. Freeze foundational definition

Before model-specific RQIR fitting/search:

- [ ] physical state space declared;
- [ ] gravity and matter variables declared;
- [ ] primary dynamics declared;
- [ ] interaction/coupling declared;
- [ ] constraints/gauge structure declared;
- [ ] parameter dimensions/domain declared;
- [ ] approximation/EFT order declared;
- [ ] renormalization/smearing prescription declared or explicitly BLOCKED.

## C. Initial gate discipline

- [ ] QG-001 evaluated with authority.
- [ ] QG-002 evaluated with authority.
- [ ] foundational gauge/conservation/causality cross-gates evaluated at least as PASS/BLOCKED/FAIL.
- [ ] no PASS state lacks evidence.

Only after the promotion rules are satisfied may the model be renamed/promoted to `QGxxx`.

## D. Derive before fitting

- [ ] derive `J`;
- [ ] derive `N`;
- [ ] derive `D`/`chi^R` as applicable;
- [ ] derive required higher correlators;
- [ ] record ordering/smearing/causal/gauge conventions;
- [ ] populate `DERIVATION_MAP.md`.

Do not choose these objects independently to improve an RQIR score.

## E. Comparator pass

- [ ] C0 classical GR/Newtonian;
- [ ] C1 semiclassical;
- [ ] C2 stochastic gravity;
- [ ] C3 classical-channel/hybrid/postquantum;
- [ ] C4 conventional quantum/technical mediators where relevant;
- [ ] C5 perturbative quantum gravity where applicable;
- [ ] C6 full-QFT-source + classical-interface alternatives.

Record `DISTINCT/DEGENERATE/BLOCKED/N/A` with an authority.

## F. RQIR pipeline

- [ ] Paper-I discriminator;
- [ ] Paper-II profiled `F_beta|theta`;
- [ ] Paper-III physical resources;
- [ ] robust uncertainty and NG-030-style interval logic where applicable.

## G. Recovery before stopping work

At every material model iteration:

- [ ] update model gate state;
- [ ] update assumptions/derivation/comparator status;
- [ ] write research log;
- [ ] write recovery delta;
- [ ] update `candidate_gravity/recovery/CURRENT_QG_FRONT.md`;
- [ ] preserve failed/superseded result authorities.
