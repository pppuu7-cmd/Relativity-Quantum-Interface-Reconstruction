# RQIR Current Front Pointer

**Updated:** 2026-08-31  
**Authoritative front:** through **Iteration 128**.

> Repository state, not chat history, is authoritative. Read `docs/RECOVERY_GUIDE.md`, `docs/MASTER_TABLE.md`, this pointer, `docs/READINESS_TRACKER.md`, and `recovery/RECOVERY_DELTA_ITERATION_128.md` before continuing. RQIR remains separate from RTK/DSIR. No current result is an empirical new-physics claim.

## Publication track

- **Paper I scientific scope:** CLOSED at Iteration 078.
- **Paper II scientific scope:** CLOSED at Iteration 079.
- **Paper III scientific scope:** **CLOSED at Iteration 128 — 100% scientific-content readiness for the frozen resource/design/certificate claim.**
- **Paper III submission readiness:** **97%**; remaining work is manuscript production/reviewer-style reproduction, not expansion of scientific scope.
- **Candidate Gravity:** may begin as a separate future branch from `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`; repository readiness to start is **90%**, but the concrete model itself remains **~10%** and has not passed QG-001…QG-010.

## Paper III closure statement

Frozen scientific chain:

`interface discriminant -> exact source/calibration constraints -> detector nuisance profile -> source metrology -> transfer/cross-PSD calibration -> calibration span/backaction/no-double-counting -> physical Fisher rates -> robust wall clock -> final architecture certificate`.

Every link required by this claim has a canonical repository authority and reproducibility/evidence classification.

### NG-084 — scientific closure is not apparatus closure

Do not paraphrase Paper-III 100% scientific readiness as a measured apparatus runtime, an experimental detection, or an experimentally established Toy009/Toy014 winner.

A numerical apparatus application remains conditional on a compatible same-apparatus closure vector.

### P3-CLOSE-001 — scope freeze

Absent an internal contradiction, failed regression or materially relevant new literature result, do not expand Paper III merely to continue iterations. Toy015/new source searches belong to later research unless a manuscript audit exposes a source-dependent gap required by the frozen claim.

## Canonical final-significance convention

Use

`F_*=Z_final^2`,

`F_final=A_raw C_src/(A_raw+C_src)`.

At a deliberately fixed retention `r`:

`A_raw=F_*/r`,

`C_src=F_*/(1-r)`.

For final `Z_final=5`, `r=.90`:

`A_raw=27.7777777778`, `C_src=250`, `F_final=25`.

**NUM-008:** historical `A_raw=25`, `C_src=225` is only a raw-5-sigma / 90%-retention regression and gives `Z_final=4.74341649`. Do not call `225` a final-5-sigma certificate.

The preferred final design is joint science/source-metrology optimization rather than imposing 90% retention a priori.

## Mandatory inference/resource backbone

Detector profiling:

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

Always eliminate exact hard constraints before profiling; retain centered covariance derivatives, spectral-tilt profiling, full PSD/cross-PSD Fisher, source-amplitude metrology, coherence/reset/dead time, transfer gain/phase, control recertification and backaction guards.

Campaign profile:

`Phi([[a,b^T],[b,N]])=a-b^T N^-1 b`.

Optimized/robust campaign rate:

`R_*=max_x Phi(sum_k x_k J_k)`

with the declared max-min uncertainty extension.

Final independent detector/source significance:

`T_min=F_*[1/sqrt(R_D)+1/sqrt(R_A)]^2`.

Architecture variables:

`u=R_D14/R_D09`,

`v=R_A14/R_A09`,

`z=R_A09/R_D09`,

`delta=(1-d14)/(1-d09)`.

Final ratio:

`Q14/Q09=delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

NG-030 remains mandatory: overlapping certified intervals mean unresolved, not a nominal winner.

## Late-front authority chain

### Iterations 101–105 — physical likelihood and final significance

- same-state temporal `f,2f` covariance/transfer protocol;
- full complex science/calibration campaign Fisher;
- robust source/science optimization and NUM-006 final-significance correction;
- compressed Toy009/Toy014 `(u,v,z,delta)` architecture crossover.

### Iterations 112–115 — transfer/control closure

- matrix gain/phase recertification;
- likelihood-derived transfer-retention budget;
- common-gain / spectral-tilt quotient;
- full-complex common-gain reference Fisher rate.

### Iterations 116–121 — non-double-counted calibration and detector interval

- joint-reference generalized-eigenvalue quota and no-double-counting rule;
- rank/span feasibility gate;
- exact Toy009/Toy014 source-nuisance span `22 = 14 mean + 8 covariance complement`;
- full covariance endpoint graph and four-matching output optimum in the declared class, with quantum backaction guard retained;
- strong/shared calibration-cover bracket;
- physical rate-level detector bracket yielding a robust interval for `u=R_D14/R_D09`.

### Iterations 122–127 — publication/evidence closure

- external apparatus audit: component feasibility exists, but no complete compatible public RQIR closure vector was found;
- claim/novelty audit: constituent Fisher/OED, QGEM/resource, classical/stochastic gravity and transfer/cross-spectrum methods are prior art;
- manuscript skeleton with explicit claim/evidence/limitation classes;
- canonical notation/dependency audit and NUM-008 supersession rule;
- minimum reviewer-scale reproducibility manifest and figure provenance rule REP-001;
- final finite-search priority audit: candidate contribution is the RQIR-specific end-to-end integration/closure discipline, not any constituent method.

### Iteration 128 — Paper III scientific closure

Canonical files:

- `analysis/paper3_scientific_closure_iteration128.py`
- `docs/PAPER_III_SCIENTIFIC_CLOSURE_ITERATION128.md`
- `research_log/2026-08-31_iteration_128_paper3_scientific_closure.md`
- `recovery/RECOVERY_DELTA_ITERATION_128.md`

Readiness:

- **Paper III scientific-content: 100%**;
- **Paper III submission: 97%**;
- **repository ready to start Candidate Gravity: 90%**;
- **concrete Candidate Gravity: ~10%**.

## Conditional apparatus extension — not a Paper-III scientific blocker

A numerical Toy009/Toy014 apparatus verdict still requires, in one compatible apparatus/accounting:

- same-state two-band science transduction and PSD/cross-PSD;
- full complex transfer-reference Fisher-rate matrix;
- seven physical calibration Fisher-rate matrices and correlated uncertainty;
- geometry/additive reference Fisher and drift/floor models;
- a physical measurement/backaction likelihood if covariance sharing is credited;
- measured independent source-metrology rate and duty;
- a robust `u` interval narrow enough for NG-030.

Do not splice numbers from different apparatuses into one forecast (NG-080).

## Immediate next work

### Paper III

Do **not** reopen scientific scope by default. Move to manuscript production:

1. generate/canonicalize figures and tables from `docs/PAPER_III_REPRODUCIBILITY_MANIFEST_ITERATION126.md`;
2. draft/polish prose from `docs/PAPER_III_MANUSCRIPT_SKELETON_ITERATION124.md`;
3. refresh literature immediately before submission;
4. perform one independent clean/reviewer-style rerun;
5. apply journal-specific formatting/references.

### Candidate Gravity

A separate branch may now start from `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`. A concrete candidate must independently pass QG-001…QG-010 plus gauge/relational, conservation/Bianchi/Ward, causality, positivity/unitarity/CP, GR/Newtonian and flat-QFT limits, EFT/renormalization, model-degeneracy and measurability gates.
