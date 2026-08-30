# RQIR Research Log — Iteration 110

**Date:** 2026-08-30

## Goal

Search prior RQIR discussion history for useful material that might not have been transferred into the repository, reconcile it against repository source-of-truth, and migrate only genuinely missing RQIR content.

## Findings

High-value early numerical/scientific results recovered from chats were already present and reproducible in the repository:

- RQIR-NUM-001 and revocation of false `6.3x/4.6x` heterogeneous-calibration gains;
- Iteration-032 force-native D2 rank/null/covariance-complementarity results;
- source QFI in both physical-amplitude and fractional-amplitude coordinates;
- Paper I/II/III and later Candidate Gravity publication separation.

No high-confidence missing scientific result was found that should override or extend the mature repo chain without rederivation.

## Migrated missing planning content

The explicit future Candidate Gravity entry checklist discussed in prior RQIR chats was not present as a dedicated repository object. Added:

`docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`

with QG-001…QG-010 gates. This is planning only and does not open a QG branch.

## Provenance guard

Registered **RQIR-RECOVERY-001**: project provenance is a hard recovery constraint. RTK/DSIR results cannot enter RQIR solely because gravity/Fisher/consistency terminology overlaps. The cross-chat audit rejected such contamination.

## Coordinate reconciliation

Verified

`F_Q^(alpha)=0.08^2 F_Q^(a)`

using repository values `F_Q^(a)~=13.270686` and `F_Q^(alpha)~=0.0849324`.

An ideal full-QFI target `C_alpha=9` therefore corresponds to `~105.97` accepted-copy QFI units. This is only a coordinate/accounting check; realistic energy-population and Ramsey channels retain their separately derived copy budgets.

## Active frontier

Scientific work remains Paper III. Iteration 109 supplies the scalar control-recertification Fisher envelope; the next gate is the parameterized control-threshold surface for constrained detector ratio `u`, using physical reference Fisher/drift/floor variables for timing/geometry/additive/gain controls.

Toy015 remains closed.
