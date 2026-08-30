# Candidate Gravity Baseline Comparator Registry

Every concrete model must be compared against all applicable baseline classes below before a model-specific RQIR discriminator is called distinctive.

## Required comparator classes

### C0 — Classical GR / Newtonian gravity

Use the controlled classical limit appropriate to the experimental regime.

Question: is the claimed signal already reproduced by ordinary classical gravitational dynamics plus the declared matter state and apparatus noise?

### C1 — Semiclassical gravity

Representative structural baseline:

`G_mn = 8 pi G <T_mn>`

or the appropriate controlled semiclassical EFT formulation.

Question: does the candidate differ beyond mean-source backreaction once source/preparation/calibration freedom is included?

### C2 — Stochastic gravity / noise-kernel baseline

Include models in which stress-energy fluctuations/noise kernels drive classical metric fluctuations.

Question: can the candidate's `N`, response or higher-statistics signature be reproduced by an admissible stochastic source/kernel?

### C3 — Classical-channel / measurement-feedback / postquantum hybrid gravity

Include classical communication, measurement-feedback, stochastic classical metric, and related hybrid constructions that can generate decoherence/noise while mediating effective interactions.

Question: is the proposed discriminator genuinely quantum-gravitational, or only evidence for a broader non-semiclassical classical/hybrid channel?

### C4 — Ordinary quantum matter + quantized/non-gravitational mediator nuisance

Where experimentally relevant, include conventional quantum interactions, electromagnetic/Casimir/patch/technical channels and quantized mediator alternatives that can mimic transfer/correlation structure.

### C5 — Perturbative quantum gravity / low-energy quantum GR

Use as comparator when the candidate claims a modification relative to standard quantized weak-field gravity or when the observable lies in its controlled EFT regime.

### C6 — Full QFT source + classical detector/interface alternatives

Include ordinary QFT source correlations combined with a classical or phenomenological transfer channel.

Question: does the RQIR signal require a quantum gravitational interface, or only quantum source statistics plus a non-quantum transfer map?

## Comparator status per model

Each model must create `COMPARATOR_STATUS.md` with one row per applicable comparator:

| Comparator | State | Observable tested | Nuisance/profile result | Authority |
|---|---|---|---|---|
| C0 | DISTINCT / DEGENERATE / BLOCKED / N/A | ... | ... | ... |

## Decision rule

A model-specific difference is publishable only at the weakest level justified by the registry.

Examples:

- distinct from C1 but not C2 -> evidence against a specific semiclassical-mean model, not evidence for quantum gravity;
- distinct from C1–C3 but degenerate with C5 -> evidence consistent with quantum gravity but not a novel theory discriminator;
- distinct only before nuisance profiling -> not statistically identified;
- distinct only with unavailable apparatus inputs -> conditional resource forecast, not experimental closure.

## Update rule

The comparator registry is living infrastructure. Before a serious model claim or Paper-IV submission, refresh the literature and add materially relevant comparator classes rather than forcing new work into an outdated taxonomy.
