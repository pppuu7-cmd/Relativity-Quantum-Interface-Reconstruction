# RQIR post-483 BASE-Q11 spectral-raw recovery delta

Date: 2026-09-06

**MODEL_READINESS:** 24% (unchanged)  
**Physical promotion:** none

## Context

Iteration 483 is the current authoritative research front for the stencil-sensitivity audit. The sole heavy mass-support gate remains frozen manifest rank 12 `(u,v)=(+1e-5,-1e-5)`, run `33997856739`, job `101391409387`; at this snapshot its main MP stage is still in progress. Do not duplicate it.

## Exact class-3 spectral reconstruction

A new lightweight fail-closed diagnostic used only exact raw Actions parent samples from already-certified manifest ranks `5,6,9,10` and the exact class-3/index-2 spectral geometry. The latter is not borrowed from class 5: it is reconstructed by the same frozen Iteration-431 specialization contract that changes the Iteration-407 target from index 4/class 5 to index 2/class 3 before the execution boundary.

For each of the four mass nodes, the diagnostic:

1. averages the 16 exact raw azimuth samples at each of the five frozen training-z values;
2. solves the frozen degree-4 polynomial interpolation at MP80 and MP120;
3. applies the class-3 affine-denominator monomial recurrence and terminal spectral contraction;
4. combines the four node values with the exact BASE inner-inner central4 coefficient:

`Q11_spectral = (4/9)/BASE_H^2 * (F_rank5 - F_rank6 - F_rank9 + F_rank10)`.

Rank-10 part 2 is bound using the post-482 provenance correction for artifact `9959560285`: current GitHub metadata and independently downloaded ZIP digest `sha256:ac18e784e54414c89e08830d917679ffe0403028abc5ecf6e4e2cdd289158909`, while the scientific result JSON SHA remains the historically frozen `2467e807b8b5f1c8a93a83a1e5be2107d2c5ae3d8747bb2f5f586b16501d1c03`.

## Result

Classification: `PASS_BASE_Q11_CLASS3_SPECTRAL_RAW_MP80_MP120__NON_PROMOTING`.

- `Q11_MP120 = -0.0005950103541045262985709553084433932831639811233377887442131869717958638797413732...`
- `Q11_MP80  = -0.00059501035410452629857095530844339328316398112333778874421318697179594894023793966...`
- scaled MP80↔MP120 discrepancy: `8.506049656645329822605200157347746312433e-71`
- quartet cancellation-condition proxy: `5.485386655942740473e9`
- each reconstructed fixed-mass spectral F node separately agrees MP80↔MP120 at approximately `1.7e-80` to `2.0e-80` scaled discrepancy.

This is a stronger localization than the raw-sample Q11 PASS because the same dominant-stencil quartet is now stable through the downstream 16-phi averaging, degree-4 z interpolation, affine-denominator recurrence, and terminal spectral contraction.

## Interpretation and strict limits

The result materially weakens arithmetic-cancellation and downstream spectral-algebra precision as explanations for the Iteration-421 `~2e-5` blocker, at least on the already-certified high-weight BASE inner-inner quartet. It does **not** prove the complete BASE derivative stable: remaining BASE ranks `12..15` are not all certified, and low stencil-L1 weight is not a bound on their actual numerical contribution. It also says nothing authoritative about the still mostly untested HALF derivative.

The diagnostic cannot recompute the frozen held-out-z structural validation because the local mass-support raw artifacts intentionally contain only the five training-z slabs. That structural contract remains inherited from the already-retained architecture and must not be silently reinterpreted as newly tested here.

Next order remains unchanged: raw-consume rank 12 fail-closed when complete; then only rank 13 if PASS; finish frozen manifest through rank 27; only after all 28 distinct nodes are local authorities perform full independent BASE and HALF MP80/MP120 derivative assembly and the retained BASE↔HALF mass-step comparison. No Richardson promotion: Iteration 465 proves two levels do not identify a truncation order.

Guardrails: no support reorder, no threshold weakening, no class-5 geometry substitution, no physical `D_s` promotion, no ANSATZ-003, no Fisher/resources.
