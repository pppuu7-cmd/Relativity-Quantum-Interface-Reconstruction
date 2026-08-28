# RQIR Statistical Identifiability — from Exact Nullspaces to Profiled Fisher Geometry

**Date:** 2026-08-29  
**Version:** 0.1  
**Labels:** `DEF`, `DRV`, `OPEN`

## 1. Why this layer is necessary

Toys 005–007 used an exact operator-space null-pair construction.  A source-state difference `Delta` was required to satisfy a finite list of exact equalities while retaining a target ordered-response difference.

That construction is useful for proving existence of hidden response directions, but real experiments do not impose exact equalities. They measure noisy data with finite covariance and nuisance parameters.

Therefore RQIR now separates two different geometries:

1. **exact null-pair geometry** — useful for algebraic existence/no-go results;
2. **statistical identifiability geometry** — required for actual inference and experiment design.

Confusing these two geometries produces a false conclusion: that additional calibration necessarily destroys sensitivity. It can destroy an exact state-difference null pair while simultaneously improving statistical identifiability of the physical parameter of interest.

---

## 2. Exact null-pair geometry

Parameterize a Hermitian source-state difference by a real vector

\[
\delta\theta\in\mathbb R^p.
\]

For a `d`-level source before trace reduction, `p=d^2` in the Hermitian coordinate system used by Toys 004–007.

Let exact calibration constraints be

\[
A\,\delta\theta=0,
\]

and let the target response functional be

\[
\delta R=r^T\delta\theta.
\]

An exact response-bearing null pair exists iff

\[
\exists\,\delta\theta\in\ker A
\quad\text{such that}\quad
r^T\delta\theta\neq0.
\]

Equivalently,

\[
P_{\ker A}r\neq0.
\]

Toy 007 uses the normalized diagnostic

\[
\eta_R=\frac{\|P_{\ker A}r\|}{\|r\|}.
\]

---

## 3. RQIR-NG-004 — exact-null saturation theorem

Assume

\[
\operatorname{rank}A=p-1,
\]

so

\[
\ker A=\operatorname{span}\{n\}.
\]

Add one exact calibration row `a^T`.

If

\[
a^Tn\neq0,
\]

then

\[
\boxed{
\operatorname{rank}
\begin{pmatrix}
A\\a^T
\end{pmatrix}=p
}
\]

and therefore

\[
\boxed{
\ker
\begin{pmatrix}
A\\a^T
\end{pmatrix}=\{0\}.
}
\]

Hence any nonzero exact state-difference null pair disappears.

### Proof

Any vector in the old nullspace has the form `c n`.  The new equation requires

\[
c\,a^Tn=0.
\]

Because `a^Tn != 0`, this implies `c=0`.  Thus the augmented nullspace is trivial. QED.

### Scope

This is an exact linear-algebra statement about the **null-pair construction**. It is not a statement that more experimental calibration reduces physical sensitivity.

---

## 4. Why exact rank is insufficient experimentally

Let the measured calibration vector have local linear model

\[
y_c=\mu_c+A\theta+\epsilon_c,
\]

with covariance

\[
\Sigma_c=\langle\epsilon_c\epsilon_c^T\rangle.
\]

The calibration Fisher matrix is

\[
\boxed{
F_c=A^T\Sigma_c^{-1}A.
}
\]

After whitening,

\[
\widetilde A=\Sigma_c^{-1/2}A,
\]

and

\[
F_c=\widetilde A^T\widetilde A.
\]

The singular values of `A_tilde` measure **how strongly** different source directions are constrained. A mathematically full-rank matrix can remain nearly uninformative in a direction if its smallest singular value is tiny.

Therefore

\[
\boxed{\text{rank alone is not an experimental identifiability metric}.}
\]

Toy 007 is an explicit example: exact rank 24/25 coexists with condition number of order `10^3`.

---

## 5. Soft-null modes

Let the singular-value decomposition be

\[
\widetilde A=U\,\operatorname{diag}(s_1,\ldots,s_p)V^T,
\qquad
s_1\ge\cdots\ge s_p\ge0.
\]

The right singular vectors `v_i` are source-state directions and

\[
\theta^TF_c\theta
=\sum_i s_i^2(v_i^T\theta)^2.
\]

A small `s_i` is therefore a **soft-null direction**: not exactly invisible, but weakly constrained relative to the declared measurement covariance.

For the `q` weakest modes define

\[
P_q=\sum_{i=p-q+1}^{p}v_iv_i^T
\]

and a soft response fraction

\[
\boxed{
\eta_R^{(q)}
=\frac{\|P_qr\|}{\|r\|}.
}
\]

Unlike exact nullity, `q` is now an experiment-design choice tied to singular-value scale, covariance and nuisance priors rather than an absolute algebraic property.

---

## 6. Full parameter-of-interest / nuisance model

Let `beta` be a scalar interface parameter or local discriminator amplitude that RQIR wants to estimate, and let `theta` collect source, apparatus and detector nuisance coordinates.

For a local model

\[
\mu(\beta,\theta)
\approx
\mu_0+s\,\delta\beta+J\,\delta\theta,
\]

with data covariance `Sigma`, the Fisher blocks are

\[
F_{\beta\beta}=s^T\Sigma^{-1}s,
\]

\[
F_{\beta\theta}=s^T\Sigma^{-1}J,
\]

\[
F_{\theta\theta}=J^T\Sigma^{-1}J.
\]

The local information on `beta` after profiling nuisance parameters is the Schur complement

\[
\boxed{
F_{\beta|\theta}
=
F_{\beta\beta}
-
F_{\beta\theta}
F_{\theta\theta}^{-1}
F_{\theta\beta}.
}
\]

When the nuisance block is singular, a Moore–Penrose inverse or an explicitly stated prior/regularization is required, and identifiability conditions must be checked rather than hidden.

---

## 7. Geometric form

Define whitened derivatives

\[
\tilde s=\Sigma^{-1/2}s,
\qquad
\tilde J=\Sigma^{-1/2}J.
\]

Let `P_J` project onto the nuisance derivative span. Then

\[
\boxed{
F_{\beta|\theta}
=\|(I-P_J)\tilde s\|^2.
}
\]

Interpretation:

> only the component of the whitened interface signal that cannot be reproduced by nuisance variations contributes to local discriminability.

This is the detector-level statistical analogue of the earlier operator-space response projection, but now with measurement covariance and nuisance response included explicitly.

---

## 8. RQIR-CAL-001 — calibration monotonicity theorem

Split the data into target data and statistically independent calibration data. Assume the added calibration data are **beta-blind**: they depend on nuisance parameters `theta` but not on the parameter of interest `beta`.

Let the old Fisher matrix be

\[
F=
\begin{pmatrix}
F_{\beta\beta} & F_{\beta\theta}\\
F_{\theta\beta} & F_{\theta\theta}
\end{pmatrix},
\]

with

\[
F_{\theta\theta}\succ0.
\]

Let independent calibration add

\[
C\succeq0
\]

to the nuisance block only:

\[
F'=
\begin{pmatrix}
F_{\beta\beta} & F_{\beta\theta}\\
F_{\theta\beta} & F_{\theta\theta}+C
\end{pmatrix}.
\]

Then

\[
(F_{\theta\theta}+C)^{-1}
\preceq
F_{\theta\theta}^{-1}.
\]

Therefore

\[
\boxed{
F'_{\beta|\theta}
\ge
F_{\beta|\theta}.
}
\]

### Meaning

Independent calibration that carries no direct `beta` dependence cannot reduce the local profiled Fisher information on `beta` under these assumptions. It can leave the information unchanged or improve it by constraining nuisance directions.

### Important distinction

This does **not** contradict RQIR-NG-004.

- NG-004: more exact constraints can eliminate the existence of two distinct source states with exactly identical calibration values.
- CAL-001: more noisy beta-blind calibration can improve the ability to distinguish an interface parameter from nuisance variation.

The objects being optimized are different.

---

## 9. Toy 007 scalar identifiability demonstration

Use the accepted normalized Toy 007 calibration matrix

\[
\widetilde A\in\mathbb R^{24\times25},
\qquad
\operatorname{rank}\widetilde A=24.
\]

Let the normalized target response vector be `r_hat`.  The old null vector `n` satisfies

\[
|\hat r^Tn|
\approx0.457682.
\]

Consider the illustrative target datum

\[
y_R=\beta+\hat r^T\theta+\epsilon_R.
\]

Because the calibration leaves `n` completely unconstrained and the target is sensitive to `n`, a change in `beta` can be absorbed by a nuisance displacement along `n`.  The local profiled Fisher information is therefore zero to numerical precision.

This is not a failure of response physics; it is a nuisance-identifiability failure.

Adding one calibration datum with a nonzero component along `n` restores positive information.

Reproducibility: `analysis/toy007_fisher_calibration_demo.py`.

---

## 10. New RQIR experiment-design objective

For actual experiments, the primary optimization target should no longer be

\[
\dim\ker A=1
\]

or maximal exact rank.

Instead use a declared likelihood/Fisher model and maximize a quantity such as

\[
\boxed{
\mathcal J_{\rm stat}
=
\frac{F_{\beta|\theta}^{1/2}}
{\sqrt{\mathcal C_{\rm exp}}}
}
\]

where `C_exp` is an explicit experiment cost or resource measure, subject to physical constraints.

Equivalent decision-level objectives may include expected likelihood ratio, Asimov significance, Bayes factor or posterior contraction, depending on the inference regime.

The important requirement is that source-state, gravitational-transfer, apparatus and detector nuisance directions be included in the same statistical model.

---

## 11. Multi-channel version

For response waveform/channel vector `s_beta` and nuisance Jacobian `J_theta`,

\[
\boxed{
F_{\beta|\theta}
=
\tilde s_\beta^T
(I-P_{\tilde J_\theta})
\tilde s_\beta.
}
\]

This immediately explains why the spectral structure found after Toy 007 can help: multiple response harmonics may create a signal vector whose shape cannot be reproduced by the allowed nuisance waveform span, even when a single-time scalar response is degenerate.

Thus the next experiment-design problem is not merely `measure more times`; it is:

> choose source drive, probe geometry, frequencies and calibration channels so that the **whitened interface waveform is maximally orthogonal to the nuisance waveform manifold**.

---

## 12. Gates and caveats

- `G3 positivity`: Fisher linearization does not replace density-matrix positivity; local nuisance domains must remain physically admissible.
- `G4 causality`: response derivatives must respect the causal transfer law.
- `G10 covariance`: the covariance model must include correlated source, detector and environmental noise.
- `G12 degeneracy`: nuisance sets must include classical/stochastic/full-QFT alternatives, not only source-state coordinates.
- `G13 measurability`: derivatives and covariances must correspond to actual detector outputs.

The Fisher approximation is local. Strongly non-Gaussian or multimodal inference requires likelihood-level validation.

---

## 13. Immediate next tasks

1. Build a joint calibration+response likelihood for the Toy 007/008 source.
2. Promote the two dominant response harmonics into a multi-frequency signal vector.
3. Include nuisance amplitudes for source preparation, probe position, energy scale, detector gain and environmental phase noise.
4. Optimize `F_{beta|theta}` rather than exact nullity.
5. Push the same statistical geometry through the source→gravity→detector transfer law.
6. Compare interface classes by likelihood-level fingerprints, not single observables.
