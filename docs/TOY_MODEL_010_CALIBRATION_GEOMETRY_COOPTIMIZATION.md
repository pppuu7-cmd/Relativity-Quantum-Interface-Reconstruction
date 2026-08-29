# RQIR Toy Model 010 — Calibration Geometry Co-Optimization

**Date:** 2026-08-29  
**Labels:** `DRV`, `NUM`, `OPEN`  
**Status:** fixed-source NP3 calibration redesign; not a global optimum or experimental-readiness claim.

## 1. Purpose

Toy 009 showed that source design must be optimized only after the calibration and detector maps are included. Toy 010 asks the next question:

> With the Toy 009 source held completely fixed, can the *finite NP3 calibration geometry itself* be redesigned so that more detector-level response survives while conditioning improves?

The variables changed here are only:

- the position of the second Newtonian calibration probe;
- five non-target calibration times.

The source operator, energy spectrum, physical five-site embedding, target response time, number/type of calibration rows and detector definitions are unchanged.

---

## 2. Fixed Toy 009 source

Energy spectrum:

\[
E=(1,2,3,4,6).
\]

Source radii remain

\[
\boxed{
(1.00000,\;1.60090,\;1.77911,\;2.60901,\;5.90724).
}
\]

Probe 0 remains at

\[
y_0=0.
\]

The inherited target response time remains

\[
\boxed{t_R=3.583928899215236.}
\]

No source-side parameter was changed in this iteration.

---

## 3. Inherited Toy 009 calibration

Toy 009 inherited from Toy 007:

\[
y_1=-3.5955271928522547
\]

and times

\[
(0,
3.0709312961,
t_R,
3.7352146497,
4.18983,
4.8970328749,
5.6572697959).
\]

For this fixed Toy 009 source, the inherited calibration gives approximately

\[
\eta_R=0.568823,
\]

\[
s_{min}=1.51222\times10^{-3},
\]

\[
\kappa_A\approx3033.4.
\]

---

## 4. Joint calibration search

A deterministic local random search varies the second probe position and the five non-target time samples while retaining the same calibration-row pattern.

Candidate designs are accepted only if all four quantities are no worse than the inherited Toy 009 calibration:

\[
S_{eff}^{D1},
\quad
S_{eff}^{D2},
\quad
\eta_R,
\quad
s_{min}.
\]

The search therefore looks for a true local Pareto improvement rather than maximizing a single detector score at the cost of calibration stability.

Recorded search seeds:

- broad local stage: `2026082903`;
- deterministic refinement: `2026082904`.

---

## 5. Accepted Toy 010 calibration geometry

Second probe:

\[
\boxed{y_1\approx-3.76453144.}
\]

Calibration times:

\[
\boxed{
(0,
2.99076642,
t_R,
2.86845279,
4.17773776,
4.88882082,
4.99774842).
}
\]

The times need not be chronologically ordered in the stored operator list; they are independent measurement settings. The smallest pair separation in the set remains finite, about `0.109` in dimensionless source time.

---

## 6. Exact NP3 checks

The redesigned equality matrix still has

\[
\boxed{rank(A)=24/25,}
\]

so exactly one Hermitian null direction remains.

For

\[
\rho_\pm=I/5\pm0.08\Delta_0,
\]

the state spectra are approximately

\[
\operatorname{eig}(\rho_+)
=(0.12226,0.17604,0.18370,0.23800,0.28000),
\]

\[
\operatorname{eig}(\rho_-)
=(0.12000,0.16200,0.21630,0.22396,0.27774).
\]

Both density matrices remain positive.

Maximum selected equality residual:

\[
\boxed{<2\times10^{-16}.}
\]

At the inherited target time,

\[
\langle B_0\rangle_+
=
\langle B_0\rangle_-
\approx0.54785973,
\]

and centered target self-noise matches:

\[
N_{00,+}=N_{00,-}
\approx0.01326059.
\]

The ordered response remains opposite and grows in magnitude:

\[
\boxed{
D_{00,+}\approx+0.01328591,
\qquad
D_{00,-}\approx-0.01328591.
}
\]

The sign orientation of the null vector is conventional; the physically relevant result is the nonzero split.

---

## 7. Calibration geometry improvement

Response-survival fraction becomes

\[
\boxed{\eta_R\approx0.600174.}
\]

This is about

\[
\boxed{5.5\%}
\]

above the Toy 009 inherited calibration and about `31%` above Toy 007.

The normalized smallest singular value becomes

\[
\boxed{s_{min}\approx2.21101\times10^{-3}.}
\]

This is approximately

\[
\boxed{46.2\%}
\]

above Toy 009.

The normalized condition number improves from approximately `3033` to

\[
\boxed{\kappa_A\approx2084.2.}
\]

Thus Toy 010 is both more informative and less ill-conditioned.

---

## 8. Detector-level improvement

The new NP3 null pair has D1 potential-response harmonics

\[
\boxed{
H_2\approx0.00286032-i\,0.01044850,
}
\]

\[
\boxed{
H_4\approx-0.00455057-i\,0.01255465.
}
\]

The same Protocol-002C profiled two-band information becomes

\[
\boxed{
S_{eff}^{D1}(010)
\approx1.67881\,S_{eff}^{D1}(009).
}
\]

Relative to Toy 007:

\[
\boxed{
S_{eff}^{D1}(010)
\approx2.05123\,S_{eff}^{D1}(007).
}
\]

For D2 gradient/force response:

\[
\boxed{
G_2\approx0.00331456-i\,0.01716597,
}
\]

\[
\boxed{
G_4\approx-0.00533146-i\,0.01470909.
}
\]

and

\[
\boxed{
S_{eff}^{D2}(010)
\approx1.58406\,S_{eff}^{D2}(009),
}
\]

or

\[
\boxed{
S_{eff}^{D2}(010)
\approx2.22336\,S_{eff}^{D2}(007).
}
\]

No source operator was changed to obtain these gains; they arise from a better finite calibration geometry and the corresponding different allowed NP3 null pair.

---

## 9. Null-direction rotation

Let `n_009` and `n_010` be unit Hermitian-vector representatives of the one-dimensional exact nullspaces before and after the calibration redesign.

Their absolute overlap is

\[
|n_{009}^Tn_{010}|\approx0.79107,
\]

corresponding to an operator-space angle

\[
\boxed{\theta_N\approx37.7^\circ.}
\]

Thus the finite calibration redesign substantially rotates the state-difference direction that remains invisible to the declared calibration measurements.

This explains why the detector projections can change strongly even though the source Hamiltonian and gravitational readout operator are unchanged.

---

## 10. Analytic identity: null-direction steering

Let a smooth calibration matrix `A(q)` have constant rank `p-1` in a `p`-dimensional parameter/operator space, and let `n(q)` be its unit null vector:

\[
A(q)n(q)=0,
\qquad
n^Tn=1.
\]

Differentiate with respect to a design coordinate `q`:

\[
A' n + A n'=0.
\]

For rank `p-1`, the Moore-Penrose pseudoinverse maps into the row-space, which is orthogonal to `n`. The normalized null-vector derivative is therefore

\[
\boxed{
n'=-A^+A'n.
}
\]

For a fixed target response vector `c`, the surviving response

\[
r=c^Tn
\]

obeys

\[
\boxed{
r'=-c^TA^+A'n.
}
\]

If `c` itself depends on `q`, add the direct term `c'^Tn`.

A useful sensitivity bound follows:

\[
\boxed{
\|n'\|\le\|A^+\|\,\|A'\|
=\frac{\|A'\|}{s_{min}(A)}.
}
\]

### RQIR-CAL-002 — null-direction steering and fragility

> Finite calibration geometry is an active experimental-design variable: changing probe positions or sample times rotates the exact unobserved direction. Poor conditioning amplifies this rotation, because null-direction sensitivity is bounded by `1/s_min`.

This identity is linear algebra, not new fundamental physics. Its RQIR role is to explain why detector-aware calibration co-design is necessary and why large gains obtained from very ill-conditioned calibrations should be treated as fragile.

---

## 11. Four-switch D1 consequence

For the Toy 010 D1 harmonics, the analytic four-switch family has optimum near

\[
\boxed{a\approx2.24169}
\]

with

\[
|W_2|\approx0.49864,
\qquad
|W_4|\approx0.31000.
\]

The resulting two-band Fisher proxy is approximately

\[
\boxed{1.819}
\]

times the old Toy 007 eight-switch bounded-window value.

Thus the redesigned calibration allows a four-switch protocol to outperform the original eight-switch design substantially.

Using the same purely illustrative physical assumptions as Detector Comparison 001, the previous Toy 007 bounded-window benchmark

\[
m_sm_p\approx8.1\times10^{-29}\;kg^2
\]

would scale to approximately

\[
\boxed{m_sm_p\approx6.01\times10^{-29}\;kg^2.}
\]

Equal masses would correspond to

\[
\boxed{m\approx7.75\times10^{-15}\;kg.}
\]

This remains an idealized scaling benchmark, not a present experimental forecast.

For the same optimistic D2 force-noise benchmark used previously, the mass-product illustration scales to roughly

\[
\boxed{1.61\times10^{-18}\;kg^2.}
\]

D2 remains far from the small coherent-source regime.

---

## 12. Interpretation

Toy 010 changes the project architecture in an important way:

1. Toy 009 showed that source and detector cannot be optimized independently of calibration.
2. Toy 010 shows that calibration should not be treated as a passive verification layer either.
3. The actual design object is the combined map

\[
\boxed{
(\text{source},\text{calibration},\text{detector},\text{noise})
\longrightarrow
F_{\beta|\theta}.
}
\]

The same physical source can support substantially different useful discriminants depending on which finite calibration geometry defines and constrains the nuisance/state-difference manifold.

---

## 13. Limits

- The optimization is local and finite-dimensional.
- The exact NP3 null-pair language is still stronger/more artificial than a full noisy likelihood treatment.
- The second probe and times are not yet subject to detailed laboratory-access constraints.
- The source remains one-particle, nonrelativistic and five-mode.
- Apparatus stress-energy, Bianchi/conservation, gauge/relational and renormalized covariant stress-tensor gates remain open.
- No claim of quantum gravity or new empirical physics is made.

---

## 14. Reproducibility

See

`analysis/toy010_calibration_geometry_optimization.py`.

Default execution verifies the accepted geometry. `--search` reproduces the deterministic local random-search procedure.

---

## 15. Next target

Move from exact-null co-design to a fully **noisy calibration Fisher** design:

- assign covariance to each mean/noise calibration measurement;
- optimize probe position and measurement times under a finite measurement budget;
- profile source-state nuisance directions statistically rather than forcing exact equality;
- include the D1 four-switch detector covariance in the same Fisher matrix;
- test whether the Toy 010 gain survives finite calibration errors.
