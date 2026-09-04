# Candidate Gravity Research Log — Iteration 407

Date: 2026-09-04

At entry, the source-of-truth front was Iteration 406 with MODEL_READINESS 24%. GitHub Actions showed zero queued and zero in-progress RQIR runs, while the formerly active Iteration 401 run had completed. The run colour was not used as scientific authority; artifact `9922183136` was downloaded and raw-parsed.

Iteration 401 raw result: `PASS_TRU1SQ_CHANNEL4_ANALYTIC_AZIMUTH_STRUCTURE_ORACLE`. Run `33830352712`, head `065ef4199a2cef50a4ec9f321c2edf4e780db572`, artifact digest `sha256:82ebf8b245f61365474c6180a772619854ece34b64a897c649c7afa35690b0eb`, scientific JSON SHA-256 `046ef14ba3ab7baf0552adcd233907c9f6078f37dcb1b1af347765d789417d4b`. The independent audit reports `scientific_authority_pass=true`.

The structure oracle is strong but scope-limited: affine-denominator error `1.1102230246251565e-16`, Fourier tail `4.4190104140298897e-16`, independent-phi mean error `6.534223913356486e-16`, and held-out degree-4 azimuth-mean polynomial error `1.7438316162996242e-06`, all within prospectively frozen thresholds. It promotes no physical channel value.

Anti-idle action: added Iteration 407 analytic/spectral channel-4 evaluator in commit `3c236e8b9a1be7c9798b39d95bc6a34cf35b058e` and its dedicated workflow in commit `26ecca2bc0706e3ace22e361e2a73994f9f92f70`. Run `33835806522` launched from that workflow and is active. The gate preserves the exact Iteration-379/389 integrand, central4 x central4 mass stencil, sign/normalization, and the physical `2e-5` convergence threshold. It replaces only the angular evaluation with the validated degree-4 azimuth mean plus analytic one-affine-denominator z integral and requires held-out direct original-integrand sphere checks.

No `Tr U1^2` blocker is removed until the raw Iteration 407 artifact is independently validated. Exact unresolved double-double set remains `[2,4,11]`. Complete `Tr U2` remains closed from Iteration 406. No e=2 effective-action combination, Source/Born subtraction, ANSATZ-003, Fisher or resources are allowed yet.

MODEL_READINESS: 24%.
