# RQIR Research Log — Iteration 128

**Date:** 2026-08-31

## Question

Can Paper III be declared scientifically complete at 100% for its stated resource/design/certificate scope without hiding unresolved apparatus measurements inside normalized placeholders?

## Audit result

Yes.

The closure audit finds a continuous authority chain for all scientific links required by the frozen Paper-III claim:

`interface discriminant -> exact constraints/source calibration -> detector nuisance profile -> source metrology -> transfer/cross-PSD calibration -> calibration span/backaction/no-double-counting -> physical Fisher rates -> robust wall clock -> final architecture certificate`.

The key late-front authority paths referenced by the reproducibility/closure manifests were explicitly checked in the repository before closure, including the final-significance crossover, calibration-span/partition/bracket chain, external-apparatus audit, novelty audit, reproducibility manifest and priority audit.

No remaining open item is a hidden prerequisite of the stated Paper-III claim. The unresolved items are apparatus-specific inputs needed only for a numerical experimental runtime or an NG-030 Toy009/Toy014 winner.

## Closure decision

**Paper III scientific scope is CLOSED at Iteration 128.**

Registered:

- **NG-084:** scientific closure is not apparatus closure. Do not paraphrase 100% scientific readiness as a measured runtime or an experimentally established architecture winner.
- **P3-CLOSE-001:** freeze Paper-III scientific scope. Do not launch Toy015 or expand the scientific claim absent an internal contradiction, failed regression or materially relevant new literature result.

The apparatus-specific conditional extension remains explicit: same-apparatus two-band PSD/cross-PSD/transduction, full complex transfer Fisher, seven physical calibration rates, geometry/additive drift/reference rates, a physical covariance/backaction likelihood if sharing is credited, source-metrology rate/duty and a sufficiently narrow robust `u` interval.

## Reproducibility scope

The repository is reproducible for what Paper III actually claims: derivations, deterministic toy regressions, parameterized/robust resource certificates, literature-evidence classification and claim boundaries.

It does not contain a measured same-apparatus RQIR closure dataset and therefore does not claim to reproduce one.

## Readiness snapshot

Project-management estimates, not statistical confidence measures:

- **Paper III scientific-content readiness: 100%.**
- **Paper III submission readiness: 97%.**
- **Repository readiness to begin a concrete Candidate-Gravity model: 90%.**
- **Concrete Candidate-Gravity model itself: ~10%.**

## Next work

Paper III now moves from research-scope expansion to manuscript production:

1. generate/canonicalize figures and tables from the reproducibility manifest;
2. draft prose from the Iteration-124 manuscript skeleton;
3. refresh literature immediately before submission;
4. perform an independent clean/reviewer-style rerun;
5. apply journal-specific formatting.

Candidate Gravity may proceed as a separate branch from `docs/CANDIDATE_GRAVITY_ENTRY_CRITERIA.md`; it must not retroactively change the frozen Paper-III claim unless a real contradiction is found.
