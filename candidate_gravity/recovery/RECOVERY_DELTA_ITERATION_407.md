# Candidate Gravity Recovery Delta — Iteration 407

Date: 2026-09-04

MODEL_READINESS: 24%

## Fresh source-of-truth audit

At the start of this iteration the repository front was Iteration 406. GitHub Actions had `0` queued and `0` in-progress runs. The previously active Iteration 401 run `33830352712` had completed successfully, so its workflow colour was not promoted by itself; the raw artifact was downloaded and parsed.

## Iteration 401 raw authority

Run: `33830352712`  
Job head: `065ef4199a2cef50a4ec9f321c2edf4e780db572`  
Artifact: `9922183136` (`iteration401-channel4-analytic-azimuth-structure`)  
Artifact digest: `sha256:82ebf8b245f61365474c6180a772619854ece34b64a897c649c7afa35690b0eb`  
Scientific JSON SHA-256: `046ef14ba3ab7baf0552adcd233907c9f6078f37dcb1b1af347765d789417d4b`

Raw classification is `PASS_TRU1SQ_CHANNEL4_ANALYTIC_AZIMUTH_STRUCTURE_ORACLE` with `scientific_authority_pass=true` in the independent artifact audit. The gate is structural only and promotes no physical `D_s` value.

Observed fail-closed checks:

- maximum denominator-affine scaled error: `1.1102230246251565e-16` <= `2e-11`;
- maximum Fourier tail above |m|=8: `4.4190104140298897e-16` <= `2e-6`;
- maximum independent-phi phase mean error: `6.534223913356486e-16` <= `2e-6`;
- maximum held-out degree-4 azimuth-mean polynomial error: `1.7438316162996242e-06` <= `2e-6`;
- maximum radial Richardson error seen: `9.161250859486547e-15`.

Therefore channel 4 is scientifically authorized to proceed to the analytic/spectral fixed-mass reduction specified in the previous front. This does not resolve double-double blockers 2,4,11 by itself.

## Iteration 407 launched

Code commit: `3c236e8b9a1be7c9798b39d95bc6a34cf35b058e`  
Workflow/launch commit: `26ecca2bc0706e3ace22e361e2a73994f9f92f70`  
Run: `33835806522` (`rqir-iteration407-tru1sq-channel4-analytic-spectral-reduction`)

The gate changes no physical numerator, routing, normalization, auxiliary-mass stencil or threshold. It keeps the frozen central4 x central4 stencil, `D_s(double-double)=-sphere_mean[d_mu1 d_mu2 G]`, and physical scaled convergence threshold `2e-5`. It uses the Iteration-401 degree-4 azimuth-mean structure, analytically integrates the remaining one-affine-denominator z dependence at each fixed mass node, applies the unchanged mixed derivative, and requires held-out original-integrand sparse-sphere cross-checks. Any failed representation/cross-check remains BLOCKED/FAIL-CLOSED; no threshold weakening or blind angular-grid escalation is permitted.

## Authority and guardrails

Latest validated Candidate Gravity authority remains **Iteration 406** until Iteration 407 produces and passes an independently checked raw artifact. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. No Source/Born subtraction. Unsupported remains BLOCKED, never zero-filled.

MODEL_READINESS: 24%

## Exact next gate

Raw-consume Iteration 407. If channel 4 is `CONVERGED`, replace only blocker index 4 and apply the same prospectively frozen analytic/spectral architecture separately to unresolved indices 2 and 11 with their own held-out checks. If Iteration 407 is `BLOCKED_CONVERGENCE`, preserve the negative result and diagnose only the failed fixed-mass representation or mass-step convergence without weakening the frozen `2e-5` gate.
