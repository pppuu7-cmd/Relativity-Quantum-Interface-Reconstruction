# RQIR Iteration 110 — Cross-Chat Recovery and Consolidation Audit

**Date:** 2026-08-30  
**Status:** recovery/provenance audit. No new toy, no apparatus forecast and no new-physics claim.

## 1. Purpose

The RQIR programme has been discussed across several chat threads. The repository is the source of truth, so this iteration compares high-value results recovered from prior RQIR discussions against the current repository and migrates anything that existed only as planning context.

RTK and DSIR material is explicitly excluded even where earlier chat summaries used similar gravity/Fisher vocabulary.

## 2. Recovered scientific results that were already safely in the repository

### Hard-constraint numerical correction

Prior RQIR discussions emphasized that the early heterogeneous-calibration gains of roughly `6.3x` (D1) and `4.6x` (D2) were numerical artifacts of large soft penalties plus thresholded pseudoinverses.

Repository check: **present** in `docs/HARD_CONSTRAINT_FISHER_AUDIT.md` and reproducible code.

Retained corrected gains are only approximately

- D1 `~1.07x`;
- D2 `~1.14x`.

`RQIR-NUM-001` remains authoritative: eliminate declared exact constraints analytically before Fisher profiling.

### Fully force-native D2 / covariance completion

Cross-chat values recovered:

- fully force-native hard rank `22/23`;
- null detector alignment `~0.99003961`;
- no-preparation `F_beta|theta~0.019445`;
- relational-potential + force complementary branch full rank `23/23`;
- at `y_ref=-4`, full covariance result `F_beta|theta~0.8994327`, `C_a*~0.06708`;
- strong four-row force-covariance subset `(0,1,3,7)` with `F_beta|theta~0.894857`.

Repository check: **all present** in `docs/D2_NATIVE_COVARIANCE_COMPLETION.md` and its code/log/recovery files.

### Source-preparation QFI coordinate reconciliation

Prior discussions used both the physical source amplitude `a` and the later fractional coordinate `alpha` with

`a=0.08 alpha`.

Repository check:

- `F_Q^(a) ~= 13.270686` is present in `docs/SOURCE_PREPARATION_QFI_RATE.md`;
- `F_Q^(alpha) ~= 0.0849324` is present in `docs/QND_ENERGY_BASIS_SOURCE_METROLOGY.md` and later resource work.

They are consistent because

`F_Q^(alpha)=(da/dalpha)^2 F_Q^(a)=0.08^2 F_Q^(a)`.

Therefore an ideal full-QFI fractional-amplitude target `C_alpha=9` corresponds to about

`9/0.0849324 ~= 105.97`

accepted-copy QFI units before integer rounding. This is a coordinate conversion, not a new resource claim; realistic energy-population/Ramsey channels have different per-copy Fisher and larger copy counts.

### Paper architecture

The previously discussed division into

1. operational reconstruction;
2. statistical identifiability;
3. physical resources/experiment architecture;
4. only later a Candidate Gravity paper

is **already present** in `docs/RQIR_ARTICLE_SERIES_ARCHITECTURE.md`.

Paper I and Paper II remain scientifically closed at Iterations 078 and 079. Paper III remains active.

## 3. Material recovered from chats that was not yet explicit in the repository

The main genuinely missing object was not a numerical result but the explicit **Candidate Gravity entry checklist** discussed in prior RQIR planning.

It has now been migrated to

`docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`.

The new planning file records QG-001 through QG-010:

- physical state space;
- matter-gravity interaction;
- controlled Newtonian/GR limit;
- Hermiticity/unitarity/positivity;
- gauge/constraint consistency;
- semiclassical and ordinary-QM limits;
- first model-specific discriminator;
- Paper-I finite-discriminant propagation;
- nuisance-profiled statistical identifiability;
- physical resource/measurability closure.

This does **not** open the QG branch. It only prevents the agreed entry criteria from being lost in chat history.

## 4. Cross-chat contamination guard

A semantic history search can retrieve nearby material from RTK/DSIR because those projects also discuss gravity, Fisher information, consistency gates and physical resources.

### RQIR-RECOVERY-001 — project provenance is a hard constraint

A result may enter RQIR recovery only if its derivation belongs to the RQIR source hierarchy / toys / detector-resource programme or is independently rederived inside RQIR.

RTK/DSIR equations, constraints, dark-sector phenomenology or model-specific results must not be copied into RQIR merely because terminology overlaps.

The current audit rejected such cross-project material.

## 5. What was not found as a missing scientific result

The audit did **not** identify a high-confidence RQIR scientific/numerical result from the recovered chat history that is both

1. absent from the repository, and
2. sufficiently derived/reproducible to promote directly into the mature science chain.

The major early corrections, Toy009/Toy010 identifiability logic, force-native D2 work, QFI/source-metrology work, Toy012–014 design results and Paper-I/II closures are all represented in the repository.

This materially reduces dependence on chat continuity.

## 6. Current active frontier after reconciliation

The reconciliation does not change the Paper-III scientific priority.

Iteration 109 adds a control-recertification Fisher envelope:

`S=sigma_*^2-sigma_floor^2`,

`sigma_ref^2=S/2`,

`t_ref^*=2/(R_ref S)`,

`tau_live^*=S/D`,

`r_min=2D/(R_ref S^2)`.

The remaining apparatus bottleneck is still the common physical transduction/stability/reference-Fisher closure for geometry, additive mean/covariance and complex gain/phase, followed by constrained robust bounds on

`u=R_D,14/R_D,09`.

Toy015 remains premature until this analysis demonstrates a source-dependent residual bottleneck.

## 7. Recovery rule for future chats

From this point, a new RQIR chat should recover in this order:

1. `docs/RECOVERY_GUIDE.md`;
2. `docs/MASTER_TABLE.md`;
3. `recovery/CURRENT_FRONT.md`;
4. latest `recovery/RECOVERY_DELTA_ITERATION_*.md`;
5. relevant Paper-I/II closure docs or active Paper-III docs;
6. `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md` only when discussing the future QG branch.

Chat history is supplementary evidence, never authority over repository state.
