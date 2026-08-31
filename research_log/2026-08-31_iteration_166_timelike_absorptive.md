# Research Log — Iteration 166

**Date:** 2026-08-31

## Objective

Exit the spacelike TT finite-shape sector saturated in Iteration 165 and test a causal/nonanalytic observable where arbitrary local Hermitian tree Wilson coefficients cannot reproduce a branch discontinuity.

## Work performed

1. Froze eight timelike benchmark invariants `s=0.004,...,0.032` with positive/negative frequencies.
2. Defined odd absorptive observable `A_odd=[Im chi_R(+omega)-Im chi_R(-omega)]/(2*pi)`.
3. Proved/audited that real local Hermitian tree contributions have zero off-pole absorptive rank.
4. Added a leading massless-loop log positive control and checked the retarded branch numerically.
5. Tested a four-shape logarithmic descendant stress family; rank is 4/4 after dimensionless scaling.
6. Added direct Lorentzian asymptotic-safety spectral comparator `AS-LOR-SPEC-002` from arXiv:2507.22169 and arXiv:2111.13232.
7. Verified that its leading IR logarithmic absorptive shape is collinear with the perturbative-C5 massless-log direction after gain profiling.

## Numerical summary

- local-tree absorptive rank: `0`;
- leading log rank: `1`;
- maximum causal-even leakage: `0` at stored precision;
- stress-test log-descendant rank: `4`;
- log-descendant condition number: `165.3462206489`;
- `A_h=61/(60*pi)=0.32361505095352056`;
- `z_spec~=1.486`;
- AS-vs-C5 leading shape combined rank: `1`;
- normalized AS residual after C5-log shape projection: `1.7153451629555285e-16`.

## Scientific interpretation

This is the first post-Iteration-165 protocol direction for which local tree derivative completion cannot recreate a signal by finite interpolation. However, the first nonzero absorptive direction is already occupied by known quantum-gravity comparators: standard C5 massless loops and Lorentzian asymptotic safety share the leading IR logarithmic shape.

Therefore the useful target is not 'nonzero absorption' but **sub-leading source-completed frequency dependence after the universal log direction is removed**.

No Candidate Gravity ansatz is frozen. No Fisher or resource forecast is allowed.

## Readiness

`MODEL_READINESS: 24%`, unchanged.
