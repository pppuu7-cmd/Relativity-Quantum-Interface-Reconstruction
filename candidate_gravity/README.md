# RQIR Candidate Gravity Workspace

**Status:** infrastructure only. No concrete Candidate Gravity model is declared by this directory.

This workspace is the canonical entry point for building and testing future dynamical gravity–quantum candidates after Paper I–III scientific closure.

## Separation rule

- Papers I–III remain frozen reconstruction / identifiability / resource results.
- A future model lives under `candidate_gravity/models/<MODEL_ID>/`.
- A model is not called an RQIR Candidate Gravity model until it has a filled model specification, a derivation map, declared comparator set and a machine-readable QG gate state.
- `PASS` means an explicit derivation/test authority exists. Missing evidence is `BLOCKED` or `NOT_TESTED`, never implicitly passed.

## Canonical files

- `MODEL_SPEC_TEMPLATE.md` — minimum dynamical model specification.
- `MODEL_TO_RQIR_CONTRACT.md` — exact interface a model must supply to Papers I–III.
- `GATE_STATUS_TEMPLATE.yaml` — QG-001…QG-010 and cross-gate state machine.
- `BASELINE_COMPARATORS.md` — mandatory alternative-model/degeneracy registry.
- `ASSUMPTIONS_LEDGER_TEMPLATE.md` — explicit assumptions, domain and supersession history.
- `DERIVATION_MAP_TEMPLATE.md` — claim -> equation -> code/test -> RQIR observable provenance.
- `recovery/CURRENT_QG_FRONT.md` — Candidate-Gravity-only recovery pointer.

## Model lifecycle

1. Create `models/QGxxx/` from the templates.
2. Freeze the declared state space, action/Hamiltonian/channel and parameter domain.
3. Derive the Model→RQIR contract objects from the same dynamics.
4. Run QG-001…QG-010 and cross-cutting gates.
5. Compare against all applicable baseline comparators.
6. Propagate surviving discriminants through Paper I, II and III.
7. Record negative results and failed gates as first-class outcomes.
8. Advance the model only when the repository authority and recovery pointer agree.

## Naming discipline

`QG001`, `QG002`, ... identify concrete candidate models, not research iterations. Research iterations continue using the repository-wide Iteration numbering.

A speculative ansatz that has not supplied QG-001 and QG-002 is named `ANSATZ-*`, not `QGxxx`.
