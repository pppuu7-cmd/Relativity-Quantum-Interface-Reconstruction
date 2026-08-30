# RQIR Recovery Delta — Iteration 077

**Date:** 2026-08-30

## Current front

Iteration 076 quantified Toy014 timing-reference recertification duty. Iteration 077 compresses the Iteration-071 physical Fisher-rate closure into the minimal measured apparatus certificate needed to decide among the surviving physical branches Toy009 / Toy014 / Toy013.

## Primitive per-branch inputs

For architecture `i`:

1. profiled science Fisher rate `R_beta,i`;
2. seven same-time dual-probe matrix calibration rates `R_cal,i,j`;
3. independent source-metrology rate `R_src,i` including preparation/reset/readout/acceptance/visibility;
4. timing/reference duty `d_i`.

The calibration rates must come from the full 2x2 PSD/cross-PSD likelihood. NG-005 still requires independent source metrology.

## Compressed certificate

For fixed significance `Z` and retained source-amplitude fraction `r`:

`C_prep=[r/(1-r)] Z^2`.

Current target `Z=5`, `r=.90` gives `C_prep=225`.

Define

`x_i=gamma_i R_beta,i/Z^2 sum_j 1/R_cal,i,j`,

`y_i=C_prep R_beta,i/(Z^2 R_src,i)`,

`m_i=1/(1-d_i)`.

Then

`T_total,i = m_i (Z^2/R_beta,i) (1+x_i+y_i)`.

**RQIR-RESOURCE-036 — minimal apparatus-rate certificate:** after the physical likelihood/profile are fixed, branch selection needs only `(R_beta,x,y,d)` per architecture. Retain the seven `R_cal,j` as audit inputs even though they compress to `x` in total wall clock.

## Pairwise architecture gate

Architecture `i` beats `k` iff

`q_s(i/k) (m_i/m_k) (1+x_i+y_i) < 1+x_k+y_k`,

with `q_s(i/k)=R_beta,k/R_beta,i`.

This gate does not assume common ASD, transduction, bandwidth, acceptance or reset.

## Regression checks

The code exactly reproduces previous special-case shared-kernel boundaries:

- Toy014 vs Toy009: `y > 7.6895205385 + 7.5421347000 x`;
- Toy013 vs Toy014: `x > 5.9842386660 + 98.2399220663 y`.

Therefore Iteration 077 is a strict generalization, not a replacement of the earlier projections.

## Measurement-priority rule

For payload `P=T_sci+T_cal+T_src`, the magnitude of the log-sensitivity to each Fisher rate equals that component's wall-clock fraction. Characterize most precisely whichever rate owns the largest time weight.

## New guardrail

**RQIR-NG-030 — uncertified near-boundary branch choice:** if conservative uncertainty intervals in rates/duty overlap in total time, do not promote a nominal central-value winner. Require `T_i^upper < T_k^lower` for robust dominance, or keep the architecture decision unresolved.

## Files

- `analysis/apparatus_certificate_iteration077.py`
- `docs/APPARATUS_RATE_CERTIFICATE_ITERATION077.md`
- `research_log/2026-08-30_iteration_077_apparatus_rate_certificate.md`
- `recovery/RECOVERY_DELTA_ITERATION_077.md`

## Next admissible gate

Instantiate the certificate from a repository-backed detector/source-metrology model for at least Toy009 and Toy014. Supply physical `R_beta`, seven matrix `R_cal,j`, `R_src`, and `d`; retain PSD/transduction/reset/visibility explicitly. Only launch Toy015 if this rate map demonstrates a source-design bottleneck rather than an apparatus/control bottleneck.

No new physics is claimed; full classical/stochastic/hybrid/full-QFT, relativistic, gauge/conservation/causality/EFT and experimental gates remain open.
