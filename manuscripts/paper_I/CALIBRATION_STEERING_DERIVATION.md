# Calibration-nullvector steering derivation

Date: 2026-09-08
Status: analytic support note for Paper I

## Setting

Let `A(t)` be a differentiable real `m x p` calibration matrix on an interval, with constant full row rank `m=p-1`. Then `ker A(t)` is one-dimensional. Choose a differentiable normalized null vector `n(t)` satisfying

`A(t)n(t)=0`,  `||n(t)||_2=1`.

The sign of `n(t)` is chosen continuously locally; the formula below is local and is unaffected by the overall sign convention.

## Derivation

Differentiate the null relation:

`A' n + A n' = 0`.

Because `A` has full row rank, `A A^+ = I_m`, so a particular solution is

`n'_p = -A^+ A' n`.

The general solution can differ by a nullspace component:

`n' = -A^+ A' n + alpha n`.

For a full-row-rank matrix, the range of `A^+` is the row space of `A`, which is orthogonal to `ker A`. Hence

`n^T A^+ A' n = 0`.

Differentiate the normalization condition `n^T n=1`:

`n^T n' = 0`.

Substituting the general solution gives `alpha=0`. Therefore, in the normalized local gauge,

`n' = -A^+ A' n`.

## Conditioning bound

Using the operator 2-norm and `||n||_2=1`,

`||n'||_2 <= ||A^+||_2 ||A'||_2`.

For full row rank,

`||A^+||_2 = 1/sigma_min(A)`,

where `sigma_min(A)` is the smallest nonzero singular value. Thus

`||n'||_2 <= ||A'||_2 / sigma_min(A)`.

## Claim boundary

The derivative formula is valid under all of the following local assumptions:

1. `A(t)` is differentiable;
2. `rank A(t)=p-1` is constant in the neighborhood;
3. the nullspace is therefore one-dimensional;
4. `n(t)` is chosen differentiably and normalized;
5. the Moore–Penrose pseudoinverse and Euclidean/operator 2-norm are used for the stated conditioning bound.

The bound becomes weak near loss of rank because `sigma_min(A)` approaches zero. It should therefore be interpreted as a local conditioning statement, not as a global guarantee that calibration steering remains controlled through a singular-value crossing.

## Response derivative

If the ordered-response functional also depends smoothly on the calibration parameter, `c=c(t)`, then

`d[c(t)n(t)]/dt = c' n - c A^+ A' n`.

If `c` is fixed while only calibration geometry changes, this reduces to

`d[c n]/dt = -c A^+ A' n`.

This is the precise sense in which calibration geometry can rotate the unresolved direction and change the response coordinate without changing the underlying source model.

## Manuscript action

Paper I should either include these assumptions immediately around the steering equation or move this derivation to a compact appendix. Once incorporated, claim C6 in `CLAIMS_EVIDENCE_MATRIX.md` can be promoted from AMBER-GREEN to GREEN at the analytic level; a numerical illustration remains optional rather than logically required.
