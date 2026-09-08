# RQIR Article II claim ledger

Target journal: Physical Review Research

## Status vocabulary

- **THEOREM** - analytic statement proved in the manuscript under explicit assumptions.
- **LOCKED NUMERICAL** - reproduced from locked RQIR artifacts/equations and regression-guarded arithmetic.
- **PENDING RERUN** - original end-to-end nonlinear computation has not yet been rerun in the current environment.
- **LIMITATION** - explicit boundary that must remain visible in the submission.

## Analytic claims

### C1 - Projection--Schur equivalence [THEOREM]
For Gaussian mean model with parameter-independent positive-definite covariance,

I_prof(beta) = g^T (I - P_N) g
             = F_bb - F_bη F_ηη^+ F_ηb.

Rank-deficient nuisance tangent matrices are allowed via the Moore--Penrose pseudoinverse.

### C2 - Local first-order identifiability [THEOREM]

I_prof(beta) > 0 iff the whitened beta tangent is not in the nuisance tangent span.

Boundary: this is local/tangent identifiability, not a proof of global nonlinear identifiability.

### C3 - Nuisance monotonicity [THEOREM]
If N1 is a subspace of N2, then I_prof(beta;N2) <= I_prof(beta;N1).

### C4 - Shared nuisance bound [THEOREM]
For independent branches, replacing a genuinely shared nuisance coefficient by independent branch-specific copies enlarges the nuisance space and therefore gives

I_joint_shared >= I_separate_copies.

Equality requires compatible best-fit nuisance compensation across branches.

## Numerical claims

### N1 - Signed/global branch [LOCKED NUMERICAL]
Audit point (beta,p,gamma)=(1,1,1).

Profiled coefficient per common event multiplier:
9.645289993133134e-3.

With N_eff=100 and J_W=1e-29:
I_beta = 9.645289993133135e-30,
sigma_beta ~= 3.220e14.

For target sigma_beta=0.1:
N_eff,required ~= 1.0367796180388115e33.

Interpretation: locally identifiable in the specified nuisance model, but quantitatively hopeless under the current normalization.

### N2 - Positive/local branch [LOCKED NUMERICAL]
Raw floating result after locked profile:
-2.2737367544323206e-13.

Because Fisher information is nonnegative, this is treated as floating roundoff at the exact boundary and clipped to zero.

Therefore sigma_beta=infinity and no finite exposure multiplier reaches a finite target precision in the local Fisher approximation.

Interpretation: not "prior rescued" under the current locked nuisance/prior model.

### N3 - Regression guard [LOCKED NUMERICAL]
`python tests/test_branch_specific_physical_fisher_rates.py`
Current locked record: 48 passed.

## Reproducibility boundary

### R1 [PENDING RERUN]
Historical Nim nonlinear-profile programs were not rerun in the current container because the Nim runtime was unavailable. Before submission, rerun the original computational path in a documented environment and compare all locked coefficients.

## Submission limitations that must not be removed

1. Fixed-covariance Fisher geometry is the baseline; parameter-dependent covariance adds the standard trace term.
2. Fisher positivity is a local result; nonlinear/global aliases remain possible.
3. Priors and likelihood information must not be conflated.
4. Signed/global numerical weakness is conditional on the locked normalization/event-weight model.
5. Branch Fisher results are diagnostics, not posterior model probabilities.
