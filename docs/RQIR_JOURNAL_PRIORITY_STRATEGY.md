# RQIR Journal Priority Strategy

**Fixed:** 2026-09-08  
**Status:** CANONICAL EDITORIAL TARGETING AUTHORITY  
**Scope:** RQIR Papers I--V

## Purpose

This file fixes the default journal-targeting order so that each RQIR manuscript is written, structured, illustrated and packaged with its most plausible readership in mind from the beginning rather than being reformatted only at the end.

The priorities below are **editorial-fit priorities, not acceptance probabilities**. Scientific claims, frozen closures, negative results and comparator boundaries must never be changed merely to improve perceived journal fit.

## Priority matrix

| RQIR paper | Primary target | Secondary target | Fallback target | Editorial rationale |
|---|---|---|---|---|
| **Paper I — operational hierarchy / finite calibration discriminants** | **Classical and Quantum Gravity (CQG)** | Physical Review D (PRD) | New Journal of Physics (NJP) | The paper is fundamentally a gravitational-physics / quantum-gravity interface methodology paper, explicitly connected to semiclassical and stochastic gravity, QFT in curved-spacetime/open-system structures and laboratory probes of the gravity--quantum interface. |
| **Paper II — statistical identifiability / nuisance geometry** | **Physical Review D (PRD)** | Classical and Quantum Gravity (CQG) | Physical Review Research (PRResearch) | The central result is a quantitative inference/field-theory/gravity methodology with a compact Fisher/null-space core and direct relevance to gravitation and quantum-gravity tests. |
| **Paper III — physical resource budgets / experimental architecture** | **Quantum Science and Technology (QST)** | Physical Review Applied (PRApplied) | Physical Review Research (PRResearch) | The manuscript should foreground quantum sensing/metrology, experimentally interpretable resource budgets, calibration architecture and realizability. The dedicated QST final-3% gate remains authoritative. |
| **Paper IV — existing gravity/QG frameworks through the RQIR funnel** | **Classical and Quantum Gravity (CQG)** | Physical Review D (PRD) | New Journal of Physics (NJP) | A broad but technical comparator paper spanning semiclassical, stochastic, hybrid/postquantum and quantum-gravity realizations is naturally addressed to a gravitational-physics readership. |
| **Paper V — conditional RQIR-derived Candidate Gravity** | **Physical Review D (PRD)** | Classical and Quantum Gravity (CQG) | Physical Review Research (PRResearch) | If and only if Paper IV returns `NEW_REQUIRED`, Paper V becomes a concrete dynamics/model paper whose state space, consistency limits, quantum-gravity/EFT relations and discriminator are most naturally assessed as fundamental gravitation/field theory. |

## Exceptional stretch route

**Physical Review Letters (PRL)** is not the baseline target for any RQIR paper. It becomes an exceptional stretch route only if a future result can be reduced to one compact, independently reproducible and broadly important advance without sacrificing essential assumptions, comparator definitions or caveats.

## Paper-I decision

`PAPER_I_PRIMARY_TARGET = CQG`.

Paper I is to be prepared as a **CQG Research Paper**, not as a Letter, unless a later editorial audit explicitly changes that decision. The manuscript should therefore:

- state the gravitational-physics significance in the title, abstract and first page;
- remain accessible to the broad CQG readership of gravitational theorists and experimentalists;
- distinguish established stochastic/semiclassical/CTP structures from the RQIR-specific calibration-quotient construction;
- foreground the finite physical null-direction proposition and its operational meaning;
- keep the non-claims about gravitational ontology explicit;
- include reproducible numerical provenance before submission;
- embed final figures/tables near the corresponding discussion;
- provide keywords, author metadata, ORCID, data/code availability and submission metadata consistent with current IOP guidance.

## Paper-III decision

`PAPER_III_PRIMARY_TARGET = QST`.

Canonical final hardening gate: `docs/PAPER_III_QST_SUBMISSION_GATE.md`.

## Publisher-scope evidence checked on 2026-09-08

The targeting decision was checked against current publisher descriptions on 2026-09-08:

- CQG: original research across gravitational physics and spacetime, including quantum gravity, QFT in curved spacetime and semiclassical quantization; Research Papers are an accepted article type.  
  `https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/about-classical-quantum-gravity/`
- CQG author guidance: broad-readership context, concise informative title/abstract, reproducible method, embedded figures/tables, keywords and research-data compliance.  
  `https://publishingsupport.iopscience.iop.org/journals/classical-and-quantum-gravity/`
- PRD: significant developments in field theory, gravitation, general relativity, field theory in curved space, string theory and quantum gravity.  
  `https://journals.aps.org/prd/about`
- QST: theoretical and experimental results across quantum science and technology, with broad quantum-science/technology relevance and lasting scientific or technological impact.  
  `https://publishingsupport.iopscience.iop.org/journals/quantum-science-technology/about-quantum-science-technology/`
- NJP: original research across the whole of physics, including quantum physics, high-energy physics, cosmology and interdisciplinary physics.  
  `https://publishingsupport.iopscience.iop.org/journals/new-journal-of-physics/about-new-journal-physics/`

These links are evidence for fit only. Exact templates, article types, peer-review mode, length guidance, data policy, reference style, APC/open-access options and submission metadata **must be rechecked against the live publisher pages immediately before each submission**.

## Change-control rules

1. A journal-priority change requires a dated repository entry stating why the previous audience fit is no longer preferred.
2. Journal fit never authorizes expansion of claims beyond repository evidence.
3. A scientifically closed Paper I--III is not reopened merely because a target journal prefers a different narrative emphasis.
4. If the primary journal rejects a manuscript, the scientific content is preserved; only justified editorial adaptation is made for the next journal in the priority chain.
5. A desk rejection or referee rejection is not scientific evidence for or against RQIR and is not used to alter physics gates.
6. The author metadata authority is `docs/RQIR_AUTHOR_METADATA.yml` unless explicitly superseded.
7. `docs/PAPER_I_CQG_SUBMISSION_GATE.md` controls Paper-I journal hardening; `docs/PAPER_III_QST_SUBMISSION_GATE.md` controls Paper-III final hardening.

## Frozen editorial decisions

`PAPER_I_PRIMARY_TARGET_CQG`  
`PAPER_II_PRIMARY_TARGET_PRD`  
`PAPER_III_PRIMARY_TARGET_QST`  
`PAPER_IV_PRIMARY_TARGET_CQG`  
`PAPER_V_PRIMARY_TARGET_PRD_IF_AUTHORIZED`
