# Candidate Gravity Recovery Guide

**Date:** 2026-08-31  
**Scope:** future concrete gravity-model work only.

## 1. Recovery principle

The Candidate Gravity branch must be recoverable from repository state without relying on chat memory. Never infer a passed gate from narrative context if `GATE_STATUS.yaml` is not `PASS` with an authority.

## 2. Mandatory read order

Read:

1. repository `recovery/CURRENT_FRONT.md`;
2. repository `docs/MASTER_TABLE.md`;
3. repository `docs/READINESS_TRACKER.md`;
4. `candidate_gravity/recovery/CURRENT_QG_FRONT.md`;
5. `candidate_gravity/README.md`;
6. `candidate_gravity/MODEL_TO_RQIR_CONTRACT.md`;
7. the active model directory.

For the active model read in order:

- `MODEL.md`;
- `GATE_STATUS.yaml`;
- `ASSUMPTIONS_LEDGER.md`;
- `DERIVATION_MAP.md`;
- `COMPARATOR_STATUS.md`;
- latest model research log/recovery delta;
- canonical analysis/tests referenced by the gate file.

## 3. What never transfers silently

Do not carry forward without an explicit derivation/reference:

- a gauge choice as a physical observable;
- an effective kernel as fundamental dynamics;
- a fitted noise kernel as a predicted correlator;
- a classical/stochastic/hybrid exclusion from a previous model;
- an apparatus Fisher rate from a different setup;
- a renormalization prescription from another model/version;
- a PASS state from a superseded model version.

## 4. Model identity

A material change to any of the following normally creates a new model version:

- physical state space;
- gravitational variables;
- matter-gravity coupling;
- constraint algebra/gauge structure;
- causal prescription;
- UV/EFT content or truncation order;
- renormalization/subtraction scheme;
- open-system/channel structure.

## 5. Gate discipline

Allowed states:

`PASS`, `FAIL`, `BLOCKED`, `NOT_TESTED`, `NOT_APPLICABLE`.

Rules:

- PASS requires repository evidence.
- FAIL is retained permanently as provenance.
- BLOCKED means missing derivation/input.
- NOT_APPLICABLE requires a written reason.
- comparator degeneracy is not converted to PASS by stronger language.

## 6. Model→RQIR pipeline

Always reconstruct the chain

`model dynamics -> J,N,chi^R,higher correlators -> Paper I discriminator -> Paper II F_beta|theta -> Paper III resources`.

If an upstream object changes, invalidate downstream results until rerun.

## 7. Negative-result recovery

Negative results are first-class outputs. A no-go may be more valuable than another candidate tweak. Preserve:

- failed limits;
- inconsistent constraints;
- positivity/causality failures;
- comparator degeneracies;
- zero profiled Fisher;
- resource divergence or unavailable-measurement no-go.

## 8. Cross-project guard

RTK and DSIR remain separate. Their equations/results do not enter Candidate Gravity unless independently rederived under the RQIR Candidate Gravity contract.

## 9. Entry condition

Do not instantiate the first real ansatz until repository readiness is explicitly certified at 100% by a repository authority. This prevents process design from changing opportunistically after a preferred model is seen.
