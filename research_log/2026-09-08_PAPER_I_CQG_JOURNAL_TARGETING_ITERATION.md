# RQIR Paper I — CQG Journal-Targeting Iteration

**Date:** 2026-09-08  
**Task:** recover canonical author metadata from DSIR, select/freeze the Paper-I primary journal, establish journal priorities for the RQIR series, and create a journal-targeted Paper-I manuscript.

## Completed

1. Recovered canonical publication metadata from the DSIR paper branch `paper/dsir-i-observable-response-geometry`, file `papers/dsir1/AUTHOR_METADATA.yml`.
2. Created `docs/RQIR_AUTHOR_METADATA.yml` with:
   - Aleksey Buyanov;
   - Independent Researcher;
   - Moscow, Russia;
   - pppuu7@gmail.com;
   - ORCID 0009-0001-2621-9305;
   - explicit prohibition on invented institutional affiliation/funding/conflict declarations.
3. Verified current publisher scope/guidance for CQG and alternative target journals.
4. Froze journal priorities in `docs/RQIR_JOURNAL_PRIORITY_STRATEGY.md`:
   - Paper I: CQG > PRD > NJP;
   - Paper II: PRD > CQG > PRResearch;
   - Paper III: QST > PRApplied > PRResearch;
   - Paper IV: CQG > PRD > NJP;
   - Paper V, only if authorized: PRD > CQG > PRResearch.
5. Created `docs/PAPER_I_CQG_SUBMISSION_GATE.md` with nine fail-closed CQG hardening gates.
6. Created and cleaned `manuscripts/paper_I/main_cqg.tex`, a CQG-targeted Research-Paper working manuscript with:
   - canonical author metadata;
   - CQG-facing title and abstract;
   - keywords;
   - gravitational-physics framing;
   - semiclassical/stochastic and comparator positioning;
   - RQIR-THM-001 with positivity proof;
   - constructive-realization provenance warning;
   - operational hierarchy table;
   - Paper-II handoff;
   - conservative data/code availability statement.
7. Updated `docs/PAPER_I_CURRENT.md` to make the CQG-targeted manuscript and journal strategy canonical editorial authorities.

## Scientific guardrails retained

No journal targeting action changes the frozen Paper-I science. In particular the manuscript does not claim:

- that gravity couples to `D` or `chi^R` in nature;
- that a nonzero matter commutator proves quantized geometry;
- that the finite toy construction is a relativistically complete stress-energy model;
- detector-level identifiability after nuisance profiling;
- an observed anomaly or new physics.

The generic mean/noise/response split, CTP formalism, linear response and incomplete-measurement nullspace mathematics remain established background rather than RQIR novelty.

## Readiness after this iteration

These are project-management estimates, not acceptance probabilities.

- Paper-I scientific readiness: **100%**.
- Paper-I literature/novelty audit: **~80%**; final CQG-specific bibliometric/priority closure remains open.
- Paper-I manuscript/submission preparation: **~60%**, promoted from 50% because a concrete CQG-targeted manuscript, canonical author metadata, journal strategy and submission gate now exist.
- Candidate Gravity `MODEL_READINESS`: independent live metric; read from `candidate_gravity/recovery/CURRENT_QG_FRONT.md` when reporting current status.

## Exact next Paper-I gate

The highest-value remaining blocker is reproducibility authority for the constructive Toy009/Toy010 numerical claims. Recover the primary canonical scripts/results and map the manuscript chain:

`rank 24/25 -> positivity -> calibration equality -> ordered response -> detector-aware response -> calibration steering`.

Only after that binding and an independent clean reproduction should publication-final numerical figures/tables be generated.
